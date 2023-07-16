# 0x11. What happens when you type google.com in your browser and press Enter
#### `DevOps` `Network` `SysAdmin`

## Background Context
Being a Full-Stack Software Engineer means you’re comfortable interacting with any layer of the stack.

A way to easily assess this is to simply ask an engineer to explain how a software system works. They can have a general overview of the flow or can choose to dig deep in a certain area.

Let’s practice by exploring the infrastructure side (network, servers, security…) of the question.

## Tasks
0. What happens when...
Write a blog post explaining what happens when you type https://www.google.com in your browser and press Enter.

Requirements, your post must cover:

DNS request
TCP/IP
Firewall
HTTPS/SSL
Load-balancer
Web server
Application server
Database
Publish your blog post on Medium or LinkedIn; share the URL of your blog post in your answer file.

1. Everything's better with a pretty diagram
Add a schema to your blog post illustrating the flow of the request created when you type `https://www.google.com` in your browser and press `Enter`.

The diagram should show:

* DNS resolution
* that the request hitting server IP on the appropriate port
* that the traffic is encrypted
* that the traffic goes through a firewall
* that the request is distributed via a load balancer
* that the web server answers the request by serving a web page
* that the application server generates the web page
* that the application server request data from the database
[Gliffy](https://www.gliffy.com/) is free and what I personally use, but feel free to use what fits you best.

Share the URL of your diagram image in your answer file.

2. Contribute!
Folks on the Internet have been trying to put together a comprehensive answer to the question. Help them by submitting a pull request. Paste the link in your answer file.

[https://github.com/alex/what-happens-when#the-g-key-is-pressed](https://github.com/alex/what-happens-when#the-g-key-is-pressed)

Requirements:

* The pull request must bring meaningful value (not a typo correction or style improvement)
* Share the pull request URL in your answer file.
