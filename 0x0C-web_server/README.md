0x0C. Web server


In this project, some of the tasks will be graded on 2 aspects:

Is your web-01 server configured according to requirements
Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)
For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

General:
Questions	Answers
What is the main role of a web server	to store and serve static content to users who request it.
What is a child process	this is a process created by another process, the root process is called parent process or creator process. To view proccess along with their Child process try ps axf
Why web servers usually have a parent process and child processes	to handle multiple incoming client requests simultaneously
What are the main HTTP requests	Get, Post, Put, Delete, Patch, Head, Options
Main http requests	uses
Get	This request is used to retrieve data from the server. When a client sends a get request it asks the web server to send back the resource the client requested for
Post	This requests are used to send data to the server, e.g to submit a form on a website. Just like filling some input fields
Put	This requests are used to update or create a resource on the server on a specific url. Just like putting something on the server, e.g imagine a user updating their profile on a website they send the updated data or save the updated data, this is them sending a put request to the server to update or create a resource already on the server
Delete	This requests are used to request a removal of a resource from the server at a specific website
Patch	This requests are used to apply partial modifications to a resource on the server. Just like the name implies patch(partial modifications). Application of this request involves: a user that'd like to edit specific fields or attributes of a resource but not edit everything, rather than sending the complete resource data again, they just edit one or two fields.
Options	This requests are used to request information about the communication options available for a specific url e.g: a developer is building a frontend application that interacts with another api to manage user accounts and the developer would like to know what http methods and headers are supported by the api for the user resource, the developer can make an options request to the api endpoint for the user to retrieve this information. The options request might look like this" OPTIONS /api/users HTTP/1.1 Host: johndoe.com The server response might look like this: HTTP/1.1 200 ok\nAllow: GET, POST, PUT, DELETE\nAccess-Control-Allow-Methods: GET, POST, PUT, DELETE\nAccess-Control-Allow-Headers: Authorization, Content-Type
Header	This request only asks for the header of the retrieved response, not the actual content, it's similar to a Get request but only retrieve the metadata about a resource without transferring the full content like a Get request
