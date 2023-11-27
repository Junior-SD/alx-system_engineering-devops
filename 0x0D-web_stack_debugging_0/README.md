Web stack debugging #0
install docker

0-give_me_a_page:
In this first debugging project, you will need to get Apache to run on the container and to return a page containing Hello Holberton when querying the root of it.

Lets talk about installing docker and what you can do with the containers you'd create using docker

To install docker on ubuntu 20.4.6

sudo apt update

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

apt-cache policy docker-ce

sudo apt install docker-ce
To check if docker is running:

sudo systemctl status docker
Lets add our username to the docker group so we avoid entering sudo everytime we try docker packages.

sudo usermod -aG docker ${USER}
To apply new group membership enter:

su - ${USER}
You will be prompted to enter your user’s password to continue.

to confirm your user is added to the docker group enter:

groups
If you need to add a user to the docker group that you’re not logged in as, declare that username explicitly using:

sudo usermod -aG docker username
To stop and remove all Docker containers and services:

sudo docker stop $(sudo docker ps -aq)
Remove all stopped containers

sudo docker rm $(sudo docker ps -aq)
to remove all docker images:

sudo docker rmi $(sudo docker images -q)
to stop docker service:

sudo systemctl stop docker
to check if there's an existing Apache process already running in the container. You can use the ps command to see the running processes

sudo docker exec -ti {process_name} ps aux
To build a docker image:

docker build -t {img_name} .
You'd need to be in the directory where the dockerfile is

to reset user password:

sudo passwd {username}
you'll be prompyted to enter new password as long as you're logged in
