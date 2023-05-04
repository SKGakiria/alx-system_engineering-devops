0x07. Networking basics #0

Tasks
0. OSI model

The project we will mainly focus on:

The Transport layer and especially TCP/UDP
On the Network layer with IP and ICMP

Questions:

What is the OSI model?

How is the OSI model organized?

1. Types of network

Questions:

What type of network a computer in local is connected to?

What type of network could connect an office in one building
to another office in a building a few streets away?

What network do you use when you browse www.google.com from
your smartphone (not connected to the Wifi)?

2. MAC and IP address

Questions:

What is a MAC address?

What is an IP address?

3. UDP and TCP

Questions:

Which statement is correct for the TCP box:

Which statement is correct for the UDP box:

Which statement is correct for the TCP worker:

4. TCP and UDP ports

Write a Bash script that displays listening ports:

That only shows listening sockets
That shows the PID and name of the program to which each socket belongs

5. Is the host on the network

Write a Bash script that pings an IP address passed as an argument.

Requirements:

Accepts a string as an argument
Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument
passed
Ping the IP 5 times
