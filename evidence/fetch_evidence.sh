#!/usr/bin/env bash
# Download report evidence from GitHub Actions into this folder. Safe to re-run:
# runs already fetched are skipped, so run it after every load test, DAST run or release.
#
#   bash evidence/fetch_evidence.sh      (from the hawkerflow-qa repo root; then commit and push)
#
# Captures:
#   loadtest/  every hawkerflow-qa "Load test" run (k6 results, charts, USL fit)
#   dast/      every hawkerflow-qa "DAST" run (authz report, ZAP reports)
#   cd/<repo>/ every CI/CD run on `release` (ZAP report, SBOM, pip-audit, test reports)
# Each run folder gets a run.md (link, date, commit, result, per-job outcome).
# GitHub keeps artifacts for 90 days; this folder keeps them for the report.

set -uo pipefail
ORG=nus-mtechse-hawkerflow
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKIP_ARTIFACTS="scanned-image"   # 100+ MB image tarball, only needed by the deploy job

fetch_run() {   # repo run_id dest_dir
  local repo=$1 id=$2 dest=$3
  if [ -f "$dest/run.md" ]; then return 0; fi
  mkdir -p "$dest"
  local names
  names=$(gh api "repos/$ORG/$repo/actions/runs/$id/artifacts" --jq '.artifacts[] | select(.expired | not) | .name')
  for name in $names; do
    case " $SKIP_ARTIFACTS " in *" $name "*) continue ;; esac
    gh run download "$id" -R "$ORG/$repo" -n "$name" -D "$dest/$name" >/dev/null 2>&1 \
      || echo "  ! could not download $name from $repo run $id"
  done
  gh run view "$id" -R "$ORG/$repo" --json displayTitle,event,headBranch,headSha,conclusion,createdAt,updatedAt,url,attempt,jobs \
    --jq '"# \(.displayTitle)\n\n- Run: \(.url)\n- Repo: '"$repo"'\n- Event: \(.event) on `\(.headBranch)` @ `\(.headSha[0:7])`\n- Started: \(.createdAt)  Finished: \(.updatedAt)  Attempt: \(.attempt)\n- Result: **\(.conclusion)**\n\n| Job | Result |\n|---|---|\n" + ([.jobs[] | "| \(.name) | \(.conclusion) |"] | join("\n"))' \
    > "$dest/run.md"
  echo "  + $dest"
}

slug() { tr -c 'A-Za-z0-9._-' '-' | tr -s '-' | sed 's/^-//;s/-$//' | cut -c1-50; }

echo "Load tests (hawkerflow-qa):"
gh run list -R "$ORG/hawkerflow-qa" -w load-test.yml -L 100 --json databaseId,status,createdAt \
  --jq '.[] | select(.status == "completed") | "\(.databaseId) \(.createdAt)"' |
while read -r id created; do
  profile=$(gh api "repos/$ORG/hawkerflow-qa/actions/runs/$id/artifacts" --jq '.artifacts[0].name // "unknown"' | sed -E 's/^loadtest-([a-z]+)-.*/\1/')
  note=$(gh run view "$id" -R "$ORG/hawkerflow-qa" --log 2>/dev/null | grep -m1 -oE -- '--title "HawkerFlow [^"]*"' | sed -E 's/--title "HawkerFlow [a-z]+ test ?//;s/"$//' | slug)
  fetch_run hawkerflow-qa "$id" "$HERE/loadtest/${created:0:10}_${created:11:2}${created:14:2}Z_${profile}${note:+_$note}_run$id"
done

echo "DAST (hawkerflow-qa):"
gh run list -R "$ORG/hawkerflow-qa" -w dast.yml -L 100 --json databaseId,status,createdAt \
  --jq '.[] | select(.status == "completed") | "\(.databaseId) \(.createdAt)"' |
while read -r id created; do
  fetch_run hawkerflow-qa "$id" "$HERE/dast/${created:0:10}_${created:11:2}${created:14:2}Z_run$id"
done

echo "CD runs on release:"
for repo in hawkerflow-service-order hawkerflow-service-hawker hawkerflow-service-customer \
            hawkerflow-service-analytics diner-ui hawker-ui; do
  gh run list -R "$ORG/$repo" -b release -e push -L 50 --json databaseId,status,createdAt,workflowName \
    --jq '.[] | select(.status == "completed" and .workflowName != "CodeQL") | "\(.databaseId) \(.createdAt)"' |
  while read -r id created; do
    [[ "$created" < "2026-10-17" ]] && continue   # new pipeline only (first release run: 17 Oct)
    fetch_run "$repo" "$id" "$HERE/cd/$repo/${created:0:10}_${created:11:2}${created:14:2}Z_run$id"
  done
done

# Index of everything captured.
{
  echo "# HawkerFlow evidence"
  echo
  echo "Downloaded from GitHub Actions by \`fetch_evidence.sh\` (re-run it after every test or release)."
  for section in loadtest dast cd; do
    [ -d "$HERE/$section" ] || continue
    echo; echo "## $section"; echo
    find "$HERE/$section" -name run.md | sort | while read -r f; do
      dir=$(dirname "$f"); rel=${dir#"$HERE"/}
      result=$(grep -m1 -oE 'Result: \*\*[a-z_]+\*\*' "$f" | sed 's/Result: //')
      files=$(cd "$dir" && find . -type f ! -name run.md | sed 's#^\./##' | sort | tr '\n' ' ')
      echo "- [\`$rel\`]($rel/run.md) $result: ${files:-no artifacts}"
    done
  done
} > "$HERE/INDEX.md"
echo "Wrote $HERE/INDEX.md"
