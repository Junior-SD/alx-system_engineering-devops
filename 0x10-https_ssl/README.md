0x10. HTTPS SSL

HTTPS SSL
0-world_wide_web:
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

1-haproxy_ssl_termination:
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

ADVANCED TASKS
100-redirect_http_to_httpsL:
Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

100-redirect_http_to_https must be your HAproxy configuration file

How to install certbot and get a ssl certificate
 STEP 1:

sudo apt update

sudo apt install certbot

 STEP 2:

sudo systemctl stop nginx

sudo service haproxy stop

 STEP 3: Get a certificate

sudo certbot certonly --standalone -d {domain name}

You should get a path to your private and certificate

 STEP 4:
copy all content of private key and certificate from /etc/letsencrypt/live/{domain name/privkey.pem} for certificate: /etc/letsencrypt/live/{domain name/fullchain.pem}

copy contents of private key and contents of certificate to /etc/ssl/certs/ssl.pem or /etc/ssl/certs/anywhere you want it

/etc/ssl/certs/anywhere you want it should look like this:

-----BEGIN PRIVATE KEY-----
_______some key______
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
______some words ______
-----END CERTIFICATE-----
 SETP 5:
Go to sudo /etc/haproxy/haproxy.cfg

add this config

frontend www-http
        bind *:80
        reqadd X-Forwarded-Proto:\ http
        default_backend web-backend
	redirect scheme https code 301 if !{ ssl_fc } # redirect http traffic to https also return a 301 Moved Permanently page
frontend www-https
        bind *:443 ssl crt /etc/ssl/certs/ssl.pem or where you saved the certificate and private key
        reqadd X-Forwarded-Proto:\ https
        default_backend web-backend
backend web-backend
        balance roundrobin
        redirect scheme https if !{ ssl_fc }
        server {server name} {ipv4}:port80 check
        server {server name} {ipv4}port80 check
