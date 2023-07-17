# 0x12. Web stack debugging #2
#### `DevOps` `SysAdmin` `Scripting` `Debugging`

### Concepts
For this project, we expect you to look at this concept:

* [Web stack debugging](https://intranet.alxswe.com/concepts/68)

## Tasks
0. Run software as another user
For the containers that you are given in this project as well as the checker, everything is run under the `root` user, which has the ability to run anything as another user.

Requirements:

* write a Bash script that accepts one argument
* the script should run the `whoami` command under the user passed as an argument
* make sure to try your script by passing different users

1. Run Nginx as Nginx
Fix this container so that Nginx is running as the nginx user.

Requirements:

* `nginx` must be running as `nginx` user
* `nginx` must be listening on all active IPs on port `8080`
* You cannot use `apt-get remove`
* Write a Bash script that configures the container to fit the above requirements

2. 7 lines or less
Using what you did for task #1, make your fix short and sweet.

Requirements:

* Your Bash script must be 7 lines long or less
* There must be a new line at the end of the file
* You respect Bash script requirements
* You cannot use `;`
* You cannot use `&&`
* You cannot use `wget`
* You cannot execute your previous answer file (Do not include the name of the previous script in this one)
