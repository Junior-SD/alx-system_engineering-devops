instructions on how to use nigix and config own web server
install nigix

sudo apt update
sudo apt install nginx
before testing nigix adjust the firewall software to allow nginx service, nginx registers it self as a service with ufw upon installation

To view list of application configured that ufw knows how to work with enter:

sudo ufw app list
to adjust firewall to allow nginx http https or nginx full service

sudo ufw allow 'Nginx HTTPS'
to adjust firewall to disallow nginx http https or nginx full service

sudo ufw deny 'Nginx HTTP'
to verify status enter:

sudo ufw status
to check if nginx service is running:

systemctl status nginx
NOW READY TO GO TO WEB IP
to get ip address enter:

curl -4 icanhazip.com
this website above would return your public ip address

you can http or https + your public ip to check webpage but if you don't configure a web page you'd get the normal nginx web page

https://server_ip
managing the nginx process
to stop web server:

sudo systemctl stop nginx
to start after stopping:

sudo systemctl start nginx
to restart:

sudo systemctl restart nginx
if you made changes to the web server or any configuration changes you can reload web server instead of stopping and starting

to reload:

sudo systemctl reload nginx
by default nginx is set to start anytime your server boots up, you can disable this and enable this setting

to disable nginx boot on startup behaviour

sudo systemctl disable nginx
to enable nginx boot on startup behavior

sudo systemctl enable nginx
SETTING SERVER BLOCKS:
When using nginx web server, server blocks can be used to encapsulate configuration details and host more than one domain from a single server. Lets set up a domain called sample_domain

Nginx on Ubuntu 20.04 has one server block enabled by default that is configured to serve documents out of a directory at /var/www/html

while this works for a single site, it's recommended to create a directory structure within /var/www for our sample_domain leaving /var/www/html in place as the default directory to be served if a clinet request doesn't match any other sites.

Lets create the directory for the sample_domain using the -p flag to create any necessary parent directories

sudo mkdir -p /var/www/sample_domain/html
Assing ownership of the directory using the $USER env variable

sudo chown -R $USER:$John_doe /var/www/sample_domain/html
The permissions of the web roots should be correct if you haven’t modified your umask value, which sets default file permissions. To ensure that your permissions are correct and allow the owner to read, write, and execute the files while granting only read and execute permissions to groups and others, you can input the following command:

sudo chmod -R 755 /var/www/sample_domain
now create a sample .html page, if you already have a page, copy or move it to the /var/www/sample_domain/html/ otherwise create it using:

sudo vi /var/www/sample_domain/html/sample.html
Inorder for Nginx to serve this content, it's necessary to create a server block with the correct directives. Instead of modifying the default configuration file you can create a new one at /etc/nginx/sites-available/sample_domain

enter to create a new server block:

sudo vi /etc/nginx/sites-available/sample_domain
use this configuration block:

server {
	listen 80;
	listen [::]:80;

	root /var/www/sample_domain/html;
	index index.html index.htm index.nginx-debian.html;

	server_name your_domain www.your_domain;

	location / {
		try_files $uri $uri/ =404;
	}
}
In the above configuration file we’ve updated the root configuration to our new directory, and the server_name to our domain name

Next enable the file by creating a link from it to the sites-enabled directory, which nginx reads from during startup/bootup

sudo ln -s /etc/nginx/sites-available/sample_domain /etc/nginx/sites-enabled/
this allows our file to be loaded up when our server starts

Two server blocks are now enabled and configured to respond to requests based on their listen and server_name directives, this means:

sample_domain will now respond to requests for sample_domain and www.your_domain

default: Will respond to any requests on port 80 that do not match the other two blocks.

To avoid a possible hash bucket memory problem that can arise from adding additional server names, it is necessary to adjust a single value in the /etc/nginx/nginx.conf file. Open the file:

sudo vi /etc/nginx/nginx.conf
Find the server_names_hash_bucket_size directive and remove the # symbol to uncomment the line.

NOTE: Commenting out lines of code – usually by putting # at the start of a line – is another way of disabling them without needing to actually delete them.

...
http {
    ...
    server_names_hash_bucket_size 64;
    ...
}
...
should look like this when you're done

You can test to make sure they're no syntax errors in any of the nginx files:

sudo nginx -t
if none restart nginx
