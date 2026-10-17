# ZAP Scanning Report

ZAP by [Checkmarx](https://checkmarx.com/).


## Summary of Alerts

| Risk Level | Number of Alerts |
| --- | --- |
| High | 0 |
| Medium | 0 |
| Low | 4 |
| Informational | 3 |




## Insights

| Level | Reason | Site | Description | Statistic |
| --- | --- | --- | --- | --- |
| Low | Warning |  | ZAP warnings logged - see the zap.log file for details | 10    |
| Info | Informational |  | Percentage of network failures | 2 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of responses with status code 2xx | 8 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of responses with status code 4xx | 91 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of endpoints with content type application/json | 100 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of endpoints with method GET | 84 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of endpoints with method POST | 15 % |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Count of total endpoints | 132    |
| Info | Informational | https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com | Percentage of slow responses | 100 % |







## Alerts

| Name | Risk Level | Number of Instances |
| --- | --- | --- |
| Cross-Origin-Resource-Policy Header Missing or Invalid | Low | 2 |
| Strict-Transport-Security Header Not Set | Low | 2 |
| Unexpected Content-Type was returned | Low | 2 |
| X-Content-Type-Options Header Missing | Low | 2 |
| A Client Error response code was returned by the server | Informational | 135 |
| Re-examine Cache-control Directives | Informational | 2 |
| Storable and Cacheable Content | Informational | 2 |




## Alert Detail



### [ Cross-Origin-Resource-Policy Header Missing or Invalid ](https://www.zaproxy.org/docs/alerts/90004/)



##### Low (Medium)

### Description

Cross-Origin-Resource-Policy header is an opt-in header designed to counter side-channels attacks like Spectre. Resource should be specifically set as shareable amongst different origins.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub`
  * Method: `GET`
  * Parameter: `Cross-Origin-Resource-Policy`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 2

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

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 2

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

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub`
  * Method: `GET`
  * Parameter: `x-content-type-options`
  * Attack: ``
  * Evidence: ``
  * Other Info: `This issue still applies to error type pages (401, 403, 500, etc.) as those pages are often still affected by injection issues, in which case there is still concern for browsers sniffing pages away from their actual content type.
At "High" threshold this scan rule will not alert on client or server error responses.`


Instances: 2

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
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.zap3552922782416125163
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/.zap3552922782416125163`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/5136717597667873720
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/5136717597667873720`
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
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/4617225895771921654
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/4617225895771921654`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1 (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1 (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/6015757669803541511
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/6015757669803541511`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/.env
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/.env`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/.htaccess
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/.htaccess`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/9147417464153839500
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/9147417464153839500`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/trace.axd`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user%3Fclass.module.classLoader.DefaultAssertionStatus=nonsense
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user (class.module.classLoader.DefaultAssertio...)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user%3Fname=abc
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user (name)`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/trace.axd
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/trace.axd`
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
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/zap3690409873054957933
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/zap3690409873054957933`
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
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/ (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo splvtdc8d80a...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/ (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo splvtdc8d80ax9w9w7za',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo splvtdc8d80a...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo splvtdc8d80ax9w9w7za',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo splvtdc8d80a...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo splvtdc8d80ax9w9w7za',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1 ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1 (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo splvtdc8d80a...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1 (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo splvtdc8d80ax9w9w7za',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo splvtdc8d80a...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo splvtdc8d80ax9w9w7za',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo splvtdc8d80a...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo splvtdc8d80ax9w9w7za',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `404`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub ()(class.module.classLoader.DefaultAssertio...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('cmd.exe /C echo splvtdc8d80a...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub%3F-d+allow_url_include%253d1+-d+auto_prepend_file%253dphp://input
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub (-d allow_url_include=1 -d auto_prepend_f...)(<?php exec('echo splvtdc8d80ax9w9w7za',$...)`
  * Method: `POST`
  * Parameter: ``
  * Attack: ``
  * Evidence: `405`
  * Other Info: ``


Instances: 135

### Solution



### Reference



#### CWE Id: [ 388 ](https://cwe.mitre.org/data/definitions/388.html)


#### WASC Id: 20

#### Source ID: 4

### [ Re-examine Cache-control Directives ](https://www.zaproxy.org/docs/alerts/10015/)



##### Informational (Low)

### Description

The cache-control header has not been set properly or is missing, allowing the browser and proxies to cache content. For static assets like css, js, or image files this might be intended, however, the resources should be reviewed to ensure that no sensitive content will be cached.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub`
  * Method: `GET`
  * Parameter: `cache-control`
  * Attack: ``
  * Evidence: ``
  * Other Info: ``


Instances: 2

### Solution

For secure content, ensure the cache-control HTTP header is set with "no-cache, no-store, must-revalidate". If an asset should be cached consider setting the directives "public, max-age, immutable".

### Reference


* [ https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching ](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html#web-content-caching)
* [ https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control ](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control)
* [ https://grayduck.mn/2021/09/13/cache-control-recommendations/ ](https://grayduck.mn/2021/09/13/cache-control-recommendations/)


#### CWE Id: [ 525 ](https://cwe.mitre.org/data/definitions/525.html)


#### WASC Id: 13

#### Source ID: 3

### [ Storable and Cacheable Content ](https://www.zaproxy.org/docs/alerts/10049/)



##### Informational (Medium)

### Description

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users. If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/health`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`
* URL: https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub
  * Node Name: `https://pczpxdtbbh.execute-api.ap-southeast-1.amazonaws.com/customer/v1/customer/user/cust_sub`
  * Method: `GET`
  * Parameter: ``
  * Attack: ``
  * Evidence: ``
  * Other Info: `In the absence of an explicitly specified caching lifetime directive in the response, a liberal lifetime heuristic of 1 year was assumed. This is permitted by rfc7234.`


Instances: 2

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


