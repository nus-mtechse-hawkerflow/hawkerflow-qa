# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 0 |
| Low | 4 |
| Informational | 6 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Medium | Exceeded High | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of responses with status code 4xx | 94 % |
| Low | Warning |  | ZAP warnings logged - see the zap.log file for details | 11    |
| Low | Exceeded High | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of slow responses | 100 % |
| Info | Informational |  | Percentage of network failures | 1 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of responses with status code 2xx | 5 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of endpoints with content type application/json | 100 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of endpoints with method GET | 78 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of endpoints with method POST | 21 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Count of total endpoints | 202    |







## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Cross-Origin-Resource-Policy Header Missing or Invalid | Low | 3 |
| Strict-Transport-Security Header Not Set | Low | Systemic |
| Unexpected Content-Type was returned | Low | 2 |
| X-Content-Type-Options Header Missing | Low | 3 |
| A Client Error response code was returned by the server | Informational | 204 |
| Non-Storable Content | Informational | 3 |
| Re-examine Cache-control Directives | Informational | 3 |
| Session Management Response Identified | Informational | 1 |
| Storable and Cacheable Content | Informational | 3 |
| User Agent Fuzzer | Informational | Systemic |




## Alert Detail



### [ Cross-Origin-Resource-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Resource-Policy header is an opt-in header designed to counter side-channels attacks like Spectre. Resource should be specifically set as shareable amongst different origins.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 3

### Solution

Ensure that the application/web server sets the Cross-Origin-Resource-Policy header appropriately, and that it sets the Cross-Origin-Resource-Policy header to 'same-origin' for all web pages.
'same-site' is considered as less secured and should be avoided.
If resources must be shared, set the header to 'cross-origin'.
If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Resource-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-resource-policy).

### Reference


* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cross-Origin-Embedder-Policy)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 14

#### Source ID: 3

### [ Strict-Transport-Security Header Not Set ](https://www.zaproxy.org/docs/alerts/10035/)



##### Low (High)

### Description

HTTP Strict Transport Security (HSTS) is a web security policy mechanism whereby a web server declares that complying user agents (such as a web browser) are to interact with it using only secure HTTPS connections (i.e. HTTP layered over TLS/SSL). HSTS is an IETF standards track protocol and is specified in RFC 6797.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders (status)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders (status)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution

Ensure that your web server, application server, load balancer, etc. is configured to enforce Strict-Transport-Security.

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html ](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)
* [ https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security ](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)
* [ https://caniuse.com/stricttransportsecurity ](https://caniuse.com/stricttransportsecurity)
* [ https://datatracker.ietf.org/doc/html/rfc6797 ](https://datatracker.ietf.org/doc/html/rfc6797)


#### CWE Id: [ 319 ](https://cwe.mitre.org/data/definitions/319.html)


#### WASC Id: 15

#### Source ID: 3

### [ Unexpected Content-Type was returned ](https://www.zaproxy.org/docs/alerts/100001/)



##### Low (High)

### Description

A Content-Type of text/html was returned by the server.
This is not one of the types expected to be returned by an API.
Raised by the 'Alert on Unexpected Content Types' script

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com%3Faaa=bbb
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com (aaa)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `text/html`
  * Other Info: ``


Instances: 2

### Solution



### Reference




#### Source ID: 4

### [ X-Content-Type-Options Header Missing ](https://www.zaproxy.org/docs/alerts/10021/)



##### Low (Medium)

### Description

The Anti-MIME-Sniffing header X-Content-Type-Options was not set to 'nosniff'. This allows older versions of Internet Explorer and Chrome to perform MIME-sniffing on the response body, potentially causing the response body to be interpreted and displayed as a content type other than the declared content type. Current (early 2014) and legacy versions of Firefox will use the declared content type (if one is set), rather than performing MIME-sniffing.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`


Instances: 3

### Solution

Ensure that the application/web server sets the Content-Type header appropriately, and that it sets the X-Content-Type-Options header to 'nosniff' for all web pages.
If possible, ensure that the end user uses a standards-compliant and modern web browser that does not perform MIME-sniffing at all, or that can be directed by the web application/web server to not perform MIME-sniffing.

### Reference


* [ https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85) ](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/compatibility/gg622941(v=vs.85))
* [ https://owasp.org/www-community/Security_Headers ](https://owasp.org/www-community/Security_Headers)


#### CWE Id: [ 693 ](https://cwe.mitre.org/data/definitions/693.html)


#### WASC Id: 15

#### Source ID: 3

### [ A Client Error response code was returned by the server ](https://www.zaproxy.org/docs/alerts/100000/)



##### Informational (High)

### Description

A response code of 404 was returned by the server.
This may indicate that the application is failing to handle unexpected input correctly.
Raised by the 'Alert on HTTP Response Code Error' script

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com%3Faaa=bbb
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com (aaa)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `400`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/ (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.DS_Store
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.DS_Store`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/._darcs
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/._darcs`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.bzr
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.bzr`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.git/config
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.git/config`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.hg
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.hg`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.idea/WebServers.xml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.idea/WebServers.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.php_cs.cache
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.php_cs.cache`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.ssh/id_dsa
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.ssh/id_dsa`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.ssh/id_rsa
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.ssh/id_rsa`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.svn/entries
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.svn/entries`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.svn/wc.db
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.svn/wc.db`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.zap7245666567878019319
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.zap7245666567878019319`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/5099276383563726115
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/5099276383563726115`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/BitKeeper
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/BitKeeper`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/CHANGELOG.txt
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/CHANGELOG.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/CVS/root
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/CVS/root`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/DEADJOE
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/DEADJOE`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/FileZilla.xml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/FileZilla.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WEB-INF/applicationContext.xml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WEB-INF/applicationContext.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WEB-INF/web.xml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WEB-INF/web.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WS_FTP.INI
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WS_FTP.INI`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WS_FTP.ini
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WS_FTP.ini`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WinSCP.ini
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/WinSCP.ini`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/_framework/blazor.boot.json
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/_framework/blazor.boot.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/_wpeprivate/config.json
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/_wpeprivate/config.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/actuator/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/actuator/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/adminer.php
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/adminer.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/api-docs
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/api-docs`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/app/etc/local.xml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/app/etc/local.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/composer.json
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/composer.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/composer.lock
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/composer.lock`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/computeMetadata/v1/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/computeMetadata/v1/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/config/database.yml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/config/database.yml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/config/databases.yml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/config/databases.yml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/core
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/core`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/docs/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/docs/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/elmah.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/elmah.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/favicon.ico
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/favicon.ico`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/filezilla.xml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/filezilla.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/i.php
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/i.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/id_dsa
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/id_dsa`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/id_rsa
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/id_rsa`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/info.php
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/info.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/key.pem
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/key.pem`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/latest/meta-data/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/latest/meta-data/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/lfm.php
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/lfm.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/metadata/instance
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/metadata/instance`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/metadata/v1
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/metadata/v1`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/myserver.key
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/myserver.key`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/opc/v1/instance/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/opc/v1/instance/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/opc/v2/instance/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/opc/v2/instance/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/openapi.json
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/openapi.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/openapi.yaml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/openapi.yaml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/openstack/latest/meta_data.json
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/openstack/latest/meta_data.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `403`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/9109309207306848738
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/9109309207306848738`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1 (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1 (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/5376945617673920650
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/5376945617673920650`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/8391334071275975795
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/8391334071275975795`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10 (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10 (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/5474700731533822271
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/5474700731533822271`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/8662147212541952907
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/8662147212541952907`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10 (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10 (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/6689888570641690368
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/6689888570641690368`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders%3Fstatus=&class.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders (class.module.classLoader.DefaultAssertio...,status)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `401`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders (status)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `401`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/8526141446543241268
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/8526141446543241268`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/1489022753194350977
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/1489022753194350977`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders%3Fstatus=&class.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders (class.module.classLoader.DefaultAssertio...,status)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `401`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders (status)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `401`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/phpinfo.php
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/phpinfo.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/privatekey.key
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/privatekey.key`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/server-info
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/server-info`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/server-status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/server-status`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/server.key
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/server.key`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/sftp-config.json
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/sftp-config.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/sitemanager.xml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/sitemanager.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/sites/default/files/.ht.sqlite
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/sites/default/files/.ht.sqlite`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/sites/default/private/files/backup_migrate/scheduled/test.txt
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/sites/default/private/files/backup_migrate/scheduled/test.txt`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger-ui/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger-ui/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger-ui/index.html
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger-ui/index.html`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger.json
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger.json`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger.yaml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger.yaml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger/ui/index.html
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/swagger/ui/index.html`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/test.php
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/test.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/v2/api-docs
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/v2/api-docs`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/v3/api-docs
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/v3/api-docs`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/vb_test.php
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/vb_test.php`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/vim_settings.xml
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/vim_settings.xml`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/winscp.ini
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/winscp.ini`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/ws_ftp.ini
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/ws_ftp.ini`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/zap3868875026218284858
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/zap3868875026218284858`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com ()(multipart:1,0)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/ (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/ (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1 ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1 (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1 (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `422`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10 ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10 (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10 (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10 ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10 (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10 (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders (status)(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo h19g129jplqd...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo h19g129jplqdab5cxbz4',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders (status)(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``


Instances: 204

### Solution



### Reference



#### CWE Id: [ 388 ](https://cwe.mitre.org/data/definitions/388.html)


#### WASC Id: 20

#### Source ID: 4

### [ Non-Storable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are not storable by caching components such as proxy servers. If the response does not contain sensitive, personal or user-specific information, it may benefit from being stored and cached, to improve performance.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `202`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders (status)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `authorization:`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/me/orders (status)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `authorization:`
  * Other Info: ``


Instances: 3

### Solution

The content may be marked as storable by ensuring that the following conditions are satisfied:
The request method must be understood by the cache and defined as being cacheable ("GET", "HEAD", and "POST" are currently defined as cacheable)
The response status code must be understood by the cache (one of the 1XX, 2XX, 3XX, 4XX, or 5XX response classes are generally understood)
The "no-store" cache directive must not appear in the request or response header fields
For caching by "shared" caches such as "proxy" caches, the "private" response directive must not appear in the response
For caching by "shared" caches such as "proxy" caches, the "Authorization" header field must not appear in the request, unless the response explicitly allows it (using one of the "must-revalidate", "public", or "s-maxage" Cache-Control response directives)
In addition to the conditions above, at least one of the following conditions must also be satisfied by the response:
It must contain an "Expires" header field
It must contain a "max-age" response directive
For "shared" caches such as "proxy" caches, it must contain a "s-maxage" response directive
It must contain a "Cache Control Extension" that allows it to be cached
It must have a status code that is defined as cacheable by default (200, 203, 204, 206, 300, 301, 404, 405, 410, 414, 501).

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ Re-examine Cache-control Directives ](https://www.zaproxy.org/docs/alerts/10015/)



##### Informational (Low)

### Description

The cache-control header has not been set properly or is missing, allowing the browser and proxies to cache content. For static assets like css, js, or image files this might be intended, however, the resources should be reviewed to ensure that no sensitive content will be cached.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/queue/order_ref`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 3

### Solution

For secure content, ensure the cache-control HTTP header is set with "no-cache, no-store, must-revalidate". If an asset should be cached consider setting the directives "public, max-age, immutable".

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching ](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching)
* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control)
* [ https://grayduck.mn/2021/09/13/cache-control-recommendations/ ](https://grayduck.mn/2021/09/13/cache-control-recommendations/)


#### CWE Id: [ 525 ](https://cwe.mitre.org/data/definitions/525.html)


#### WASC Id: 13

#### Source ID: 3

### [ Session Management Response Identified ](https://www.zaproxy.org/docs/alerts/10112/)



##### Informational (High)

### Description

The given response has been identified as containing a session management token. The 'Other Info' field contains a set of header tokens that can be used in the Header Based Session Management Method. If the request is in a context which has a Session Management Method set to "Auto-Detect" then this rule will change the session management to use the tokens identified.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders%3Fstatus=
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/stalls/10/orders (status)`
  * Method: `GET`
  * Parameter: `status`
  * Attack: ``
  * Evidence: `status`
  * Other Info: `url:status`


Instances: 1

### Solution

This is an informational alert rather than a vulnerability and so there is nothing to fix.

### Reference


* [ https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id/ ](https://www.zaproxy.org/docs/desktop/addons/authentication-helper/session-mgmt-id/)



#### Source ID: 3

### [ Storable and Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users. If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/orders/10`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`


Instances: 3

### Solution

Validate that the response does not contain sensitive, personal or user-specific information. If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user:
Cache-Control: no-cache, no-store, must-revalidate, private
Pragma: no-cache
Expires: 0
This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request.

### Reference


* [ https://datatracker.ietf.org/doc/html/rfc7234 ](https://datatracker.ietf.org/doc/html/rfc7234)
* [ https://datatracker.ietf.org/doc/html/rfc7231 ](https://datatracker.ietf.org/doc/html/rfc7231)
* [ https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html ](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html)


#### CWE Id: [ 524 ](https://cwe.mitre.org/data/definitions/524.html)


#### WASC Id: 13

#### Source ID: 3

### [ User Agent Fuzzer ](https://www.zaproxy.org/docs/alerts/10104/)



##### Informational (Medium)

### Description

Check for differences in response based on fuzzed User Agent (eg. mobile sites, access as a Search Engine Crawler). Compares the response statuscode and the hashcode of the response body with the original response.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)`
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)`
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko`
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/order/v1/order/sqs/status`
  * Method: `GET`
  * Parameter: `Header User-Agent`
  * Attack: `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3739.0 Safari/537.36 Edg/75.0.109.0`
  * Evidence: ``
  * Other Info: ``

Instances: Systemic


### Solution



### Reference


* [ https://owasp.org/www-project-web-security-testing-guide/ ](https://owasp.org/www-project-web-security-testing-guide/)



#### Source ID: 1


