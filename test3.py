Computer network is a set of nodes connected by communications links

Nodes-computer,printer (capable of send/receive data)
communication links-wired(ethernet-switch/hub) or wireless links(wifi)

protocol:
set of rules to communicate

Topology:
Network topology refers to the physical and logical arrangement of nodes on a network. The common network topologies include bus, star, ring, mesh, and tree.

ipaddress:(logical address)
Every node in the computer network is identified with help of ip address.Routers need ip address to forward data

Mac address:(physical address)
Every node in the LAN is identified with help of mac address.switch need mac add to forward data

Port address:
Every process in a node is uniquely identified using port numbers.
In a node many processess will be running,data which are sent/received must reach right process

Switching:
It helps in deciding the best route for data transmission if there ia multiple paths in a larger network.One to one connection

Layering:
means decomposing the problem into more manageable components(layers)
layered architectures:
1.The OSI reference model
2.The TCP/IP Model

The OSI model:
Open System Interconnection
It is model for understanding and designing a network architecture that is flexible,robust
The pupose of osi model is to facilitate communication b/w diff systems without requiring changes to logic of hardware,software
It is a guidelines ,was never fully implemented

OSI Model layers:[refer javatpoint]
Application layer:
it enables the user to access the newtwork resources.(This layer provide services to the user)
services
File tansfer and access management,mail services,directory services

Presentation layer:
It is responsible for translation,encryption and compressions.

Session layer:
it establishes,maintains,and synchronizes the interaction among communication devices.
services
dialog control,synchronization

Transport layer:
It is responsible for process to process delivery of entire msg
services
port addressing,Sgementation and reassembly,connection control,end to end flow control,error control.

Network layer:
It is responsible for delivery of data from original source to destination network.
services
logical addressing(ip address),routing

data link layer:
It is responsible for moving data(framing) from one node to another node
services
framing,physical addressing(mac address),flow control,error control,access control

Physical layer:
It is responsible for transmitting bits over a medium (wired or wireless medium)
Services
Representation of bits,Physical characteristics of media,data rate

TCP/IP:
Developed prior of osi model,it is implemented model
Application,transport,internet,network access

HUB:
used to set up LAN,layer 1
Has multiple ports,star topology,has no memory
When packet arrives at one port ,it is copied to the other ports so that all segments of LAN can see all packets-disadvantages

Switch:
It is a networking hardware that connects devices on a computer network to establish a LAN
It has memory,stores MAC address in table,layer 2 device for setting up LAN

Router:
It is a networking device that forwards data packets between computer networks.
It is connected to at least two networks,commonly two LANs or WANs or a LANand its ISP's networks.
It is a layer 3(network layer) device,stores routing table



cmd:
1.ipconfig --ipaddress
2.ipconfig/all --macaddress
3.netstat -a --port address (or) resmon {It is an app it is not a command}
4.nslookup www.google.com --DNS Server: DNS stands for Domain Name System. DNS is basically a server that translates web addresses or URLs (ex: www.google.com) into their corresponding IP addresses. 
  We don’t have to remember all the IP addresses of each and every website. The command ‘nslookup’ gives you the IP address of the domain you are looking for. This also provides information on our DNS Server.
5.ping 142.250.195.164 -- 142 ...is a ipaddress of google.com or we can give (ping www.google.com).
  It checks whether google.com is reachable from my computer.And sends 4 packets and receives 4 packets means it is existing
6.tracert www.google.com --it will trace the route how it will reach the google.com like first will reach the default gateway that we see in ipconfig.
  This will show some details like timings, ipaddress from start to end ,end will ip address of google.com 
