Load balancer

Background Context
You have been given 2 additional servers:

gc-[STUDENT_ID]-web-02-XXXXXXXXXX
gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

0-custom_http_response_header:
Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)

1-install_load_balancer:
Install and configure HAproxy on your lb-01 server.

Requirements:

Configure HAproxy so that it send traffic to web-01 and web-02

Distribute requests using a roundrobin algorithm

ADVANCED TASKS
2-puppet_custom_http_response_header.pp:
Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

The name of the custom HTTP header must be X-Served-By

The value of the custom HTTP header must be the hostname of the server Nginx is running on
