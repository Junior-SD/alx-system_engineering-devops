#puppet code representation of the 2-ssh_config file
exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
path    => '/bin/'
}
