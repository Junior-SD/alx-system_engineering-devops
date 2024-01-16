Web stack debugging #3


0x17. Web stack debugging #3
Overview
This project involves debugging a WordPress website running on a LAMP stack. The task is to use strace to find out why Apache is returning a 500 error, fix the issue, and then automate the fix using Puppet.

Files
0-strace_is_your_friend.pp: Puppet manifest containing the fix for the Apache 500 error.

Task Details
0. Strace is your friend
Using strace, identify and fix the reason for Apache returning a 500 error. Create a Puppet manifest (0-strace_is_your_friend.pp) to automate the fix.

Example:

$ curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

$ puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds

$ curl -sI 127.0.0.1:80
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

