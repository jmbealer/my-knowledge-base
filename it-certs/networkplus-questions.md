Question 7

Which of the following steps of the troubleshooting methodology would most
likely include checking through each level of the OSI model after the problem
has been identified?

    A. Establish a theory.
    B. Implement the solution.
    C. Create a plan of action.
    D. Verify functionality.

Answer(s): A. Establish a theory.

Explanation: After identifying the problem, the next step in the CompTIA
troubleshooting model is to establish a theory of probable cause. Technicians
commonly walk up the OSI model to help form that theory and isolate which layer
the issue may exist on.

Question 8

While troubleshooting a VoIP handset connection, a technician's laptop is able
to successfully connect to network resources using the same port. The technician
needs to identify the port on the switch. Which of the following should the
technician use to determine the switch and port?

    A. LLDP
    B. IKE
    C. VLAN
    D. netstat

Answer(s): A. LLDP

Explanation: LLDP (Link Layer Discovery Protocol) provides device-to-device
discovery information. It lets a technician identify which switch and port a
device is connected to. The other options are unrelated to physical port
discovery.

Question 9

A network administrator needs to set up a file server to allow user access. The
organization uses DHCP to assign IP addresses. Which of the following is the
best solution for the administrator to set up?

    A. A separate scope for the file server using a /32 subnet
    B. A reservation for the server based on the MAC address
    C. A static IP address within the DHCP IP range
    D. A SLAAC for the server

Answer(s): B. A reservation for the server based on the MAC address

Explanation: A DHCP reservation ensures the file server always receives the same
IP address while remaining centrally managed. This avoids IP conflicts and keeps
DNS mappings consistent.

Question 10

Which of the following technologies are X.509 certificates most commonly
associated with?

    A. PKI
    B. VLAN tagging
    C. LDAP
    D. MFA

Answer(s): A. PKI

Explanation: X.509 certificates are the foundational standard used in Public Key
Infrastructure (PKI). They authenticate identities in TLS/SSL, code signing, and
secure email.

Question 11

A network administrator wants to implement an authentication process for
temporary access to an organization's network. Which of the following
technologies would facilitate this process?

    A. Captive portal
    B. Enterprise authentication
    C. Ad hoc network
    D. WPA3

Answer(s): A. Captive portal

Explanation: A captive portal forces users to authenticate or acknowledge usage
terms before accessing the network. It is ideal for temporary or guest access.

Question 12

A user is unable to navigate to a website because the provided URL is not
resolving to the correct IP address. Other users are able to navigate to the
intended website without issue. Which of the following is most likely causing
this issue?

    A. Hosts file
    B. Self-signed certificate
    C. Nameserver record
    D. IP helper

Answer(s): A. Hosts file

Explanation: A user’s local hosts file can override DNS and cause incorrect IP
resolution. Since only one user is affected, this is the most likely cause.

Question 13

A network administrator is planning to host a company application in the cloud,
making the application available for all internal and third-party users. Which
of the following concepts describes this arrangement?

    A. Multitenancy
    B. VPC
    C. NFV
    D. SaaS

Answer(s): A. Multitenancy

Explanation: Multitenancy allows multiple internal or external users (tenants)
to access a shared application while maintaining logical data separation.

Question 14

Which of the following should be used to obtain remote access to a network
appliance that has failed to start up properly?

    A. Crash cart
    B. Jump box
    C. Secure Shell
    D. Out-of-band management

Answer(s): D. Out-of-band management

Explanation: If an appliance fails to boot, in-band access like SSH is
unavailable. Out-of-band management (console server, management port, or modem)
allows remote access even when normal network functions are down.

Question 15

Which of the following attacks utilizes a network packet that contains multiple
network tags?

    A. MAC flooding
    B. VLAN hopping
    C. DNS spoofing
    D. ARP poisoning

Answer(s): B. VLAN hopping

Explanation: VLAN hopping (double-tagging) inserts two VLAN tags into a packet
to exploit switch misconfigurations and reach unauthorized VLANs.

Question 16

A network administrator is configuring a new switch and wants to connect two
ports to the core switch to ensure redundancy. Which of the following
configurations would meet this requirement?

    A. Full duplex
    B. 802.1Q tagging
    C. Native VLAN
    D. Link aggregation

Answer(s): D. Link aggregation

Explanation: Link aggregation (LACP) bonds multiple physical links into a single
logical interface, providing redundancy and increased bandwidth.

Question 17

Which of the following ports is used for secure email?

    A. 25
    B. 110
    C. 143
    D. 587

Answer(s): D. 587

Explanation: Port 587 is the standard SMTP submission port and typically uses
TLS encryption, making it the secure method for sending email.

Question 18

A client wants to increase overall security after a recent breach. Which of the
following would be best to implement? (Choose two.)

    A. Least privilege network access
    B. Dynamic inventories
    C. Central policy management
    D. Zero-touch provisioning
    E. Configuration drift prevention
    F. Subnet range limits

Answer(s): A. Least privilege network access, C. Central policy management

Explanation: -Least privilege reduces unnecessary network access. -Central
policy management ensures consistent application of security rules across
devices.

Question 19

Which of the following is a cost-effective advantage of a split-tunnel VPN?

    A. Web traffic is filtered through a web filler.
    B. More bandwidth is required on the company's internet connection.
    C. Monitoring detects insecure machines on the company's network.
    D. Cloud-based traffic flows outside of the company's network.

Answer(s): D. Cloud-based traffic flows outside of the company's network.

Explanation: Split tunneling allows cloud and general internet traffic to leave
directly, reducing load on the company VPN and conserving bandwidth.

Question 20

A network technician is troubleshooting a web application's poor performance.
The office has two internet links that share the traffic load. Which of the
following tools should the technician use to determine which link is being used
for the web application?

    A. netstat
    B. nslookup
    C. ping
    D. tracert

Answer(s): D. tracert

Explanation: Traceroute shows the hop-by-hop path traffic takes, revealing which
WAN circuit or ISP path is in use.

Question 21

Which of the following attacks can cause users who are attempting to access a
company website to be directed to an entirely different website?

    A. DNS poisoning
    B. Denial-of-service
    C. Social engineering
    D. ARP spoofing

Answer(s): A. DNS poisoning

Explanation: DNS poisoning corrupts DNS lookup results, redirecting users to
malicious or incorrect IP addresses.

Question 22

As part of an attack, a threat actor purposefully overflows the
content-addressable memory (CAM) table on a switch. Which of the following types
of attacks is this scenario an example of?

    A. ARP spoofing
    B. Evil twin
    C. MAC flooding
    D. DNS poisoning

Answer(s): C. MAC flooding

Explanation: MAC flooding overwhelms the CAM table, forcing the switch to flood
traffic and enabling packet sniffing.

Question 23

A company's office has publicly accessible meeting rooms equipped with network
ports. A recent audit revealed that visitors were able to access the corporate
network by plugging personal laptops into open network ports. Which of the
following should the company implement to prevent this in the future?

    A. URL filters
    B. VPN
    C. ACLs
    D. NAC

Answer(s): D. NAC

Explanation: Network Access Control (NAC) evaluates and authorizes devices
before they join the network, stopping unauthorized guest devices.

Question 24

A user notifies a network administrator about losing access to a remote file
server. The network administrator is able to ping the server and verifies the
current firewall rules do not block access to the network fileshare. Which of
the following tools would help identify which ports are open on the remote file
server?

    A. dig
    B. nmap
    C. tracert
    D. nslookup

Answer(s): B. nmap

Explanation: Nmap scans remote hosts to determine which TCP/UDP ports are open
or filtered.

Question 25

Which of the following technologies is the best choice to listen for requests
and distribute user traffic across web servers?

    A. Router
    B. Switch
    C. Firewall
    D. Load balancer

Answer(s): D. Load balancer

Explanation: A load balancer receives client requests and distributes them
across multiple backend servers for performance and redundancy.

Question 26

A company is hosting a secure server that requires all connections to the server
to be encrypted. A junior administrator needs to harden the web server. The
following ports on the web server are open: Which of the following ports should
be disabled?

    A. 22
    B. 80
    C. 443
    D. 587

Answer(s): B. 80

Explanation: Disabling port 80 (HTTP) ensures that all traffic is forced through
encrypted HTTPS on port 443.

Question 27

Which of the following is the next step to take after successfully testing a
root cause theory?

    A. Determine resolution steps.
    B. Duplicate the problem in a lab.
    C. Present the theory for approval.
    D. Implement the solution to the problem.

Answer(s): A. Determine resolution steps.

Explanation: Once the theory is confirmed, the next step is to create a plan of
action, which includes determining the resolution steps.

Question 28

A network administrator is configuring a new switch and wants to ensure that
only assigned devices can connect to the switch. Which of the following should
the administrator do?

    A. Configure ACLs.
    B. Implement a captive portal.
    C. Enable port security.
    D. Disable unnecessary services.

Answer(s): C. Enable port security.

Explanation: Port security restricts which MAC addresses are allowed on an
interface, preventing unauthorized devices from connecting.

Question 29

A customer needs six usable IP addresses. Which of the following best meets this
requirement?

    A. 255.255.255.128
    B. 255.255.255.192
    C. 255.255.255.224
    D. 255.255.255.240

Answer(s): D. 255.255.255.240

Explanation: A subnet with six usable addresses requires a /29, which
corresponds to 255.255.255.248. However, among the options, the smallest mask
that still exceeds the requirement is /28 = 255.255.255.240, providing 14 usable
hosts.

Question 30

A user reports having intermittent connectivity issues to the company network.
The network configuration for the user reveals the following: IP address:
192.168.1.10 Subnet mask: 255.255.255.0 Default gateway: 192.168.1.254 The
network switch shows the following ARP table: Which of the following is the most
likely cause of the user's connection issues?

    A. A port with incorrect VLAN assigned
    B. A switch with spanning tree conflict
    C. Another PC with manually configured IP
    D. A router with overlapping route tables

Answer(s): C. Another PC with manually configured IP

Explanation: Two different MAC addresses mapping to the same IP indicates an IP
conflict, usually caused by another device configured with a static IP.

Question 31

Which of the following is created to illustrate the effectiveness of wireless
networking coverage in a building?

    A. Logical diagram
    B. Layer 3 network diagram
    C. Service-level agreement
    D. Heat map

Answer(s): D. Heat map

Explanation: Phones typically tag voice VLAN traffic, while the workstation uses
untagged data VLAN traffic passed through the phone. If the PC cannot reach the
network but the phone can, the data VLAN assignment is incorrect.

Question 32

Which of the following cloud deployment models is most commonly associated with
multitenancy and is generally offered by a service provider?

    A. Private
    B. Community
    C. Public
    D. Hybrid

Answer(s): C. Public

Explanation: A public cloud supports multitenancy—multiple customers share the
same physical infrastructure while being logically isolated. Public cloud
providers (AWS, Azure, GCP) deliver scalable, on-demand resources to many
organizations simultaneously.

Question 33

A network administrator needs to create an SVI on a Layer 3-capable device to
separate voice and data traffic. Which of the following best explains this use
case?

    A. A physical interface used for trunking logical ports
    B. A physical interface used for management access
    C. A logical interface used for the routing of VLANs
    D. A logical interface used when the number of physical ports is insufficient

Answer(s): C. A logical interface used for the routing of VLANs

Explanation: An SVI (Switched Virtual Interface) is a logical interface created
on a Layer 3 switch to provide routing between VLANs. Creating SVIs for voice
and data VLANs allows the switch to route traffic between them.

Question 34

A network administrator is performing a refresh of a wireless environment. As
the APs are being placed, they overlap a little bit with each other. Which of
the following 2.4GHz channels should be selected to ensure that they do not
conflict?

    A. 1, 3, 5
    B. 1, 6, 11
    C. 2, 6, 10
    D. 3, 6, 9

Answer(s): B. 1, 6, 11

Explanation: In the 2.4GHz band, only channels 1, 6, and 11 are non-overlapping.
Using these prevents adjacent APs from interfering with each other

Question 35

Which of the following network cables involves bouncing light off of protective
cladding?

    A. Twinaxial
    B. Coaxial
    C. Single-mode
    D. Multimode

Answer(s): D. Multimode

Explanation: Multimode fiber uses modal dispersion, where multiple light paths
bounce off the fiber cladding. This is the characteristic behavior that
differentiates multimode from single-mode fiber.

Question 36

Which of the following would allow a network administrator to analyze attacks
coming from the internet without affecting latency?

    A. IPS
    B. IDS
    C. Load balancer
    D. Firewall

Answer(s): B. IDS

Explanation: An IDS (Intrusion Detection System) inspects mirrored traffic
passively and does not sit inline, so it adds no latency. IPS and firewalls sit
inline and can add delay.

Question 37

A technician is troubleshooting wireless connectivity near a break room.
Whenever a user turns on the microwave, connectivity to the user's laptop is
lost. Which of the following frequency bands is the laptop most likely using?

    A. 2.4GHz
    B. 5GHz
    C. 6GHz
    D. 900MHz

Answer(s): A. 2.4GHz

Explanation: Microwaves emit interference around 2.4GHz, the same frequency used
by many Wi-Fi devices. Devices on 5GHz or 6GHz would not be affected.

Question 38

A network administrator needs to implement routing capabilities in a hypervisor.
Which of the following should the administrator most likely implement?

    A. VPC
    B. Firewall
    C. NFV
    D. IaaS

Answer(s): C. NFV

Explanation: NFV (Network Function Virtualization) virtualizes network
appliances—including routers—inside a hypervisor. This allows routing,
switching, and firewalling to be deployed as software.

Question 39

A network technician needs to install patch cords from the UTP patch panel to
the access switch for a newly occupied set of offices. The patch panel is not
labeled for easy jack identification. Which of the following tools provides the
easiest way to identify the appropriate patch panel port?

    A. Toner
    B. Laptop
    C. Cable tester
    D. Visual fault locator

Answer(s): A. Toner

Explanation: A toner and probe lets you send a signal down a cable and quickly
trace it to the correct port on the patch panel, making identification simple.

Question 40

A network administrator received complaints of intermittent network connectivity
issues. The administrator investigates and finds that the network design
contains potential loop scenarios. Which of the following should the
administrator do?

    A. Enable spanning tree.
    B. Configure port security.
    C. Change switch port speed limits.
    D. Enforce 802.1Q tagging.

Answer(s): A. Enable spanning tree.

Explanation: STP (Spanning Tree Protocol) prevents network loops by blocking
redundant links. Without STP, loops cause broadcast storms and intermittent
connectivity.

Question 41

Which of the following routing technologies uses a successor and a feasible
successor?

    A. IS-IS
    B. OSPF
    C. BGP
    D. EIGRP

Answer(s): D. EIGRP

Explanation: EIGRP maintains both a successor (primary route) and a feasible
successor (backup route) using the DUAL algorithm. No other routing protocol
uses this terminology.

Question 42

Which of the following best describes what an organization would use port
address translation for?

    A. VLANs on the perimeter
    B. Public address on the perimeter router
    C. Non-routable address on the perimeter router
    D. Servers on the perimeter

Answer(s): C. Non-routable address on the perimeter router

Explanation: PAT (Port Address Translation) allows many internal non-routable
private IPs to share a single public IP by translating port numbers. It is used
specifically to allow private networks to communicate externally.

Question 43

A company is implementing a wireless solution in a high-density environment.
Which of the following 802.11 standards is used when a company is concerned
about device saturation and coverage?

    A. 802.11ac
    B. 802.11ax
    C. 802.11g
    D. 802.11n

Answer(s): B. 802.11ax

Explanation: 802.11ax (Wi-Fi 6) is designed specifically for high-density
environments. It improves performance when many devices compete for airtime by
using OFDMA, better scheduling, and improved throughput efficiency.

Question 44

Which of the following network traffic types is sent to all nodes on the
network?

    A. Unicast
    B. Broadcast
    C. Multicast
    D. Anycast

Answer(s): B. Broadcast

Explanation: A broadcast packet is delivered to all devices within the broadcast
domain. Unicast is one-to-one, multicast is one-to-many (subscribed devices),
and anycast delivers to the nearest of many possible receivers.

Question 45

Which of the following cable types provides the highest possible transmission
speed?

    A. Plenum
    B. Ethernet
    C. Fiber-optic
    D. DAC

Answer(s): C. Fiber-optic

Explanation: Fiber-optic cabling supports the highest bandwidth and distance
capabilities, far exceeding copper, DAC, or plenum-rated cables. Fiber can reach
multi-gigabit and long-distance links reliably.

Question 46

Which of the following layers of the OSI model is responsible for end-to-end
encryption?

    A. Presentation
    B. Application
    C. Session
    D. Transport

Answer(s): A. Presentation

Explanation: The Presentation layer (Layer 6) handles data formatting,
compression, and encryption. TLS/SSL operations conceptually fall here, even
though implementations span layers.

Question 47

A network security administrator needs to monitor the contents of data sent
between a secure network and the rest of the company. Which of the following
monitoring methods will accomplish this task?

    A. Port mirroring
    B. Flow data
    C. Syslog entries
    D. SNMP traps

Answer(s): A. Port mirroring

Explanation: Port mirroring (SPAN) replicates packet contents for analysis. Flow
data does not include payload, and syslog provides only device logs.
Availability monitoring tracks uptime—not traffic inspection.

Question 48

Which of the following does a full-tunnel VPN provide?

    A. Lower bandwidth requirements
    B. The ability to reset local computer passwords
    C. Corporate inspection of all network traffic
    D. Access to blocked sites

Answer(s): C. Corporate inspection of all network traffic

Explanation: A full-tunnel VPN forces all user traffic — internet and internal —
through the organization’s VPN concentrator, allowing the company to inspect,
filter, and log all traffic.

Question 49

Which of the following does a hash provide?

    A. Non-repudiation
    B. Integrity
    C. Confidentiality
    D. Availability

Answer(s): B. Integrity

Explanation: A hash verifies integrity, ensuring data has not been altered. It
does not encrypt (confidentiality) or authenticate the sender (non-repudiation).

Question 50

A company wants to implement a disaster recovery site for non-critical
applications, which can tolerate a short period of downtime. Which of the
following types of sites should the company implement to achieve this goal?

    A. Hot
    B. Cold
    C. Warm
    D. Passive

Answer(s): C. Warm

Explanation: A warm site contains partially pre-configured systems and
up-to-date backups, allowing faster recovery than a cold site but not as
immediate as a hot site.

Question 51

Which of the following is an XML-based security concept that works by passing
sensitive information about users, such as log-in information and attributes, to
providers?

    A. IAM
    B. MFA
    C. RADIUS
    D. SAML

Answer(s): D. SAML

Explanation: SAML is an XML-based framework used for SSO and federated
authentication, passing user identity information securely between providers.

Question 52

Which of the following routing technologies uses unequal cost load balancing and
port 88?

    A. EIGRP
    B. BGP
    C. RIP
    D. OSPF

Answer(s): A. EIGRP

Explanation: EIGRP supports unequal-cost load balancing using its variance
feature and uses protocol port 88. No other protocol in the list uses these
characteristics.

Question 53

A wireless network consultant is deploying a large number of WAPs and wants to
centrally control them from one wireless LAN controller. Which of the following
network types should the consultant employ?

    A. Mesh
    B. Infrastructure
    C. Point-to-point
    D. Ad hoc

Answer(s): B. Infrastructure

Explanation: An infrastructure WLAN uses lightweight APs managed centrally by a
WLC (wireless LAN controller), allowing configuration, monitoring, and RF
management from a single point.

Question 54

Which of the following network topologies involves sending all traffic through a
single point?

    A. Mesh
    B. Hybrid
    C. Hub-and-spoke
    D. Point-to-point

Answer(s): C. Hub-and-spoke

Explanation: In a hub-and-spoke topology, every remote node (spoke) communicates
through a central device (hub). This single hub becomes the relay point for all
traffic. This design simplifies management but introduces a single point of
failure and potential bottlenecks.

Question 55

Which of the following functions is used to prioritize network traffic based on
the type of traffic?

    A. QoS
    B. VPN
    C. CDN
    D. TTL

Answer(s): A. QoS

Explanation: Quality of Service (QoS) classifies and prioritizes network
traffic. It ensures critical services—such as VoIP, video, or real-time
apps—receive bandwidth and low latency even when networks are congested.

Question 56

Which of the following most likely determines the size of a rack for
installation? (Choose two.)

    A. KVM size
    B. Switch depth
    C. Hard drive size
    D. Cooling fan speed
    E. Outlet amperage
    F. Server height

Answer(s): B. Switch depth, F. Server height

Explanation: Rack installation depends heavily on: Switch depth – Racks must be
deep enough to accommodate network switches and allow room for cabling. Server
height – Measured in rack units (U), this determines how many devices fit
vertically in a rack. Other options do not directly define rack size
requirements.

Question 57

A network administrator is planning to implement device monitoring to enhance
network visibility. The security team requires that the solution provides
authentication and encryption. Which of the following meets these requirements?

    A. SIEM
    B. Syslog
    C. NetFlow
    D. SNMPv3

Answer(s): D. SNMPv3

Explanation: SNMPv3 is the only version of SNMP that provides: Authentication
Encryption Integrity checking SNMPv1/v2 lack security, and the other options do
not offer encrypted device polling.

Question 58

A network administrator needs to change where the outside DNS records are
hosted. Which of the following records should the administrator change at the
registrar to accomplish this task?

    A. NS
    B. SOA
    C. PTR
    D. CNAME

Answer(s): A. NS

Explanation: NS (Name Server) records at the registrar define which DNS servers
host a domain’s authoritative zone. Changing the NS records moves DNS hosting to
a different provider.

Question 59

A support agent receives a report that a remote user's wired devices are
constantly disconnecting and have slow speeds. Upon inspection, the support
agent sees that the user's coaxial modem has a signal power of - 97dB. Which of
the following should the support agent recommend to troubleshoot the issue?

    A. Removing any splitters connected to the line
    B. Which of the following should the support agent recommend to troubleshoot the issue?
    C. Moving the devices closer to the modem
    D. Lowering the network speed

Answer(s): A. Removing any splitters connected to the line

Explanation: A signal power of –97 dB indicates severe signal attenuation.
Splitters degrade coax signal strength significantly. Removing splitters helps
restore acceptable signal levels for stable wired connectivity.

Question 60

Which of the following does OSPF use to communicate routing updates?

    A. Unicast
    B. Anycast
    C. Multicast
    D. Broadcast

Answer(s): C. Multicast

Explanation: OSPF routers use multicast addresses (224.0.0.5 and 224.0.0.6) to
send LSAs and hello packets to neighbors, instead of sending separate unicasts
or generic broadcasts.

Question 61

A storage network requires reduced overhead and increased efficiency for the
amount of data being sent. Which of the following should an engineer most likely
configure to meet these requirements?

    A. Link speed
    B. Jumbo frames
    C. QoS
    D. 802.1q tagging

Answer(s): B. Jumbo frames

Explanation: Jumbo frames increase the Ethernet MTU (for example, to 9000
bytes), which reduces header overhead per byte of data and improves efficiency
for large storage transfers (SAN, iSCSI, etc.).

Question 62

A security administrator is creating a new firewall object for a device with IP
address 192.168.100.1/25. However, the firewall software only uses dotted
decimal notation in configuration fields. Which of the following is the correct
subnet mask to use?

    A. 255.255.254.0
    B. 255.255.255.1
    C. 255.255.255.128
    D. 255.255.255.192

Answer(s): C. 255.255.255.128

Explanation: A /25 prefix means 25 bits of 1s in the mask:
11111111.11111111.11111111.10000000 → 255.255.255.128 So /25 corresponds to
255.255.255.128.

Question 63

Which of the following disaster recovery metrics describes the average length of
time a piece of equipment can be expected to operate normally?

    A. RPO
    B. RTO
    C. MTTR
    D. MTBF

Answer(s): D. MTBF

Explanation: MTBF (Mean Time Between Failures) is the predicted average time
that a device operates correctly between failures. It describes expected
uptime/operating life, which is exactly what the question asks.

Question 64

A network administrator logs on to a router and sees an interface with an IP
address of 10.61.52.34 255.255.255.252. Which of the following best describes
how this interface IP address is being used?

    A. As a point-to-point connection
    B. To connect to the internet
    C. As a virtual address for redundancy
    D. For out-of-band management

Answer(s): A. As a point-to-point connection

Explanation: A subnet mask of 255.255.255.252 (/30) provides 4 addresses total
(2 usable hosts). This /30 is typically used on point-to-point links between two
routers, which matches option A.

Question 65

A network technician is troubleshooting a faulty NIC and tests the theory. Which
of the following should the technician do next?

    A. Develop a theory.
    B. Establish a plan of action.
    C. Implement the solution.
    D. Document the findings.

Answer(s): B. Establish a plan of action.

Explanation: After confirming the theory, the next troubleshooting step is to
establish a plan of action before implementing the fix.

Question 66

A network administrator is configuring access points for installation in a dense
environment where coverage is often overlapping. Which of the following channel
widths should the administrator choose to help minimize interference in the
2.4GHz spectrum?

    A. 11MHz
    B. 20MHz
    C. 40MHz
    D. 80MHz 160MHz

Answer(s): B. 20MHz

Explanation: Only 20MHz channels should be used in 2.4GHz deployments, because
the band has limited spectrum and only three non-overlapping channels. Wider
channels cause severe interference.

Question 67

A network manager wants to view network traffic for devices connected to a
switch. A network engineer connects an appliance to a free port on the switch
and needs to configure the switch port connected to the appliance. Which of the
following is the best option for the engineer to enable?

    A. Trunking
    B. Port mirroring
    C. Full duplex
    D. SNMP

Answer(s): B. Port mirroring

Explanation: Port mirroring (SPAN) duplicates traffic from selected ports or
VLANs and sends it to a monitoring port for analysis by IDS/IPS or packet
analyzers.

Question 68

A network administrator is in the process of installing 35 PoE security cameras.
After the administrator installed and tested the new cables, the administrator
installed the cameras. However, a small number of the cameras do not work. Which
of the following is the most likely reason?

    A. Incorrect wiring standard
    B. Power budget exceeded
    C. Signal attenuation
    D. Wrong voltage

Answer(s): B. Power budget exceeded

Explanation: PoE switches have a fixed power budget. If the total wattage of all
connected devices exceeds this limit, additional devices will fail to power up.

Question 69

A network administrator is troubleshooting an application issue after a firewall
change. The administrator has confirmed that the port and protocol are
accessible to the user, but the application is still having issues. Which of the
following tools allows the administrator to look at traffic on the application
layer of the OSI model?

    A. ifconfig
    B. tcpdump
    C. nslookup
    D. traceroute

Answer(s): B. tcpdump

Explanation: tcpdump can capture packets including layer 7 (application layer)
data. It's used to analyze whether proper traffic is flowing after a firewall
rule change.

Question 70

Which of the following ports should a network administrator enable for encrypted
log-in to a network switch?

    A. 22
    B. 23
    C. 80
    D. 123

Answer(s): A. 22

Explanation: Port 22 is SSH, which provides secure encrypted remote management.
Telnet (port 23) is not encrypted.

Question 71

Which of the following is used to stage copies of a website closer to
geographically dispersed users?

    A. VPN
    B. CDN
    C. SAN
    D. SDN

Answer(s): B. CDN

Explanation: A CDN caches and distributes website content from geographically
distributed edge servers to reduce latency and improve performance.

Question 72

Which of the following appliances provides users with an extended footprint that
allows connections from multiple devices within a designated WLAN?

    A. Router
    B. Switch
    C. Access point
    D. Firewall

Answer(s): C. Access point

Explanation: An access point extends wireless coverage and allows multiple
clients to connect to the WLAN.

Question 73

An administrator is configuring a switch that will be placed in an area of the
office that is accessible to customers. Which of the following is the best way
for the administrator to mitigate unknown devices from connecting to the
network?

    A. SSE
    B. ACL
    C. Perimeter network
    D. 802.1X

Answer(s): D. 802.1X

Explanation: 802.1X provides port-based authentication. Devices cannot join the
network unless authenticated, even if they plug into an exposed port.

Question 74

Which of the following diagrams would most likely include specifications about
fiber connector types?

    A. Logical
    B. Physical
    C. Rack
    D. Routing

Answer(s): B. Physical

Explanation: A physical diagram shows cabling types, connector types (LC, SC,
ST), and physical layout of devices and wiring.

Question 75

Which of the following is the most likely reason an insurance brokerage would
enforce VPN usage?

    A. To encrypt sensitive data in transit
    B. To secure the endpoints
    C. To maintain contractual agreements
    D. To comply with data retention requirements

Answer(s): A. To encrypt sensitive data in transit

Explanation: Insurance data often includes PII. VPNs encrypt all data in
transit, protecting it from interception.

Question 76

An organization moved its DNS servers to new IP addresses. After this move,
customers are no longer able to access the organization's website. Which of the
following DNS entries should be updated?

    A. AAA
    B. CNAME
    C. MX
    D. NS

Answer(s): D. NS

Explanation: NS (Name Server) records specify which DNS servers are
authoritative for the domain. If the DNS servers' IPs change, you must update
the NS records at the registrar, or no outside client will know where the
domain’s authoritative DNS now resides.

Question 77

Which of the following are environmental factors that should be considered when
installing equipment in a building? (Choose two.)

    A. Fire suppression system
    B. UPS location
    C. Humidity control
    D. Power load
    E. Floor construction type
    F. Proximity to nearest MDF

Answer(s): A. Fire suppression system, F. Proximity to nearest MDF

Explanation: Fire suppression systems must be designed for electronics
(Halon-type or inert gas systems). Humidity control prevents static discharge
and condensation, both of which can damage network equipment. These are direct
environmental requirements for safe equipment operation.

Question 78

A customer lost the connection to the telephone system. The administration
console is configured with multiple network interfaces and is connected to
multiple switches. The network administrator troubleshoots and verifies the
following: The support team is able to connect remotely to the administration
console. Rebooting the switch shows solid link and activity lights even on
unused ports. Rebooting the telephone system does not bring the system back
online. The console is able to connect directly to individual modules
successfully. Which of the following is the most likely reason the customer lost
the connection?

    A. A switch failed.
    B. The console software needs to be reinstalled.
    C. The cables to the modules need to be replaced.
    D. A module failed.

Answer(s): D. A module failed.

Explanation: All troubleshooting indicators point to only one module not
responding, while the administration console and switches operate normally. The
console connects successfully to individual modules, indicating the telephone
system module itself has failed.

Question 79

A systems administrator is configuring a new device to be added to the network.
The administrator is planning to perform device hardening prior to connecting
the device. Which of the following should the administrator do first?

    A. Update the network ACLs.
    B. Place the device in a screened subnet.
    C. Enable content filtering.
    D. Change the default admin passwords.

Answer(s): D. Change the default admin passwords.

Explanation: The first step in hardening any new device is changing default
credentials. Leaving default passwords in place is a major security risk since
they are publicly known.

Question 80

A network administrator needs to connect two network closets that are 492ft
(150m) away from each other. Which of the following cable types should the
administrator install between the closets?

    A. Single-mode fiber
    B. Coaxial
    C. DAC
    D. STP

Answer(s): A. Single-mode fiber

Explanation: 492 ft / 150 m exceeds copper Ethernet limits unless specialized
extended-reach technologies are used. Single-mode fiber is appropriate for
long-distance backbone links and supports high bandwidth reliably.

Question 81

An IT manager needs to connect ten sites in a mesh network. Each needs to be
secured with reduced provisioning time. Which of the following technologies will
best meet this requirement?

    A. SD-WAN
    B. VXLAN
    C. VPN
    D. NFV

Answer(s): A. SD-WAN

Explanation: SD-WAN is designed for quickly deploying secure, scalable WAN
connections across many sites. It simplifies provisioning compared to
traditional VPN mesh builds and automates security and routing policies across
all locations.

Question 82

Which of the following is most likely responsible for the security and handling
of personal data in Europe?

    A. GDPR
    B. SCADA
    C. SAML
    D. PCI DSS

Answer(s): A. GDPR

Explanation: GDPR (General Data Protection Regulation) is the legislation that
governs how organizations must protect and handle personal data belonging to EU
residents. The other options are technologies or frameworks, not legal
data-protection requirements.

Question 83

An organization has a security requirement that all network connections can be
traced back to a user. A network administrator needs to identify a solution to
implement on the wireless network. Which of the following is the best solution?

    A. Implementing enterprise authentication
    B. Requiring the use of PSKs
    C. Configuring a captive portal for users
    D. Enforcing wired equivalent protection

Answer(s): A. Implementing enterprise authentication

Explanation: Enterprise authentication (802.1X + RADIUS) provides per-user
credentials, making every wireless connection uniquely identifiable. PSKs cannot
identify individual users, captive portals authenticate only at login (not per
packet), and WEP is obsolete and insecure.

Question 84

A customer is adding fiber connectivity between adjacent buildings. A technician
terminates the multimode cable to the fiber patch panel. After the technician
connects the fiber patch cable, the indicator light does not tum on. Which of
the following should a technician try first to troubleshoot this issue?

    A. Reverse the fibers.
    B. Reterminate the fibers.
    C. Verify the fiber size.
    D. Examine the cable runs for visual faults.

Answer(s): A. Reverse the fibers.

Explanation: On duplex fiber links, TX must connect to RX on the other side. If
the indicator light does not turn on, the most common cause is reversed fiber
polarity. Swapping the two strands is the fastest and correct first
troubleshooting step.

Question 85

Users cannot connect to an internal website with an IP address 10.249.3.76. A
network administrator runs a command and receives the following output:
![image for questions 85](https://free-braindumps.com/images/exam-dumps/N10-009/242f1018-93af-49ba-9dbf-3bd746dddc8a.jpg)
Which of the following command-line tools is the network administrator using?

    A. tracert
    B. netstat
    C. tcpdump
    D. nmap

Answer(s): A. tracert

Explanation: A traceroute/tracert command shows the path packets take to a
destination, displaying each hop along the route. The hop-by-hop output
referenced in the scenario matches traceroute behavior.

Question 86

After running a Cat 8 cable using passthrough plugs, an electrician notices that
connected cables are experiencing a lot of cross talk. Which of the following
troubleshooting steps should the electrician take first?

    A. Inspect the connectors for any wires that are touching or exposed.
    B. Restore default settings on the connected devices.
    C. Terminate the connections again.
    D. Check for radio frequency interference in the area.

Answer(s): A. Inspect the connectors for any wires that are touching or exposed.

Explanation: Exposed, uneven, or touching wire pairs at the connector
termination are the most common cause of excessive crosstalk when using
passthrough plugs. The first step is to inspect the connector for improper wire
alignment or exposed copper.

Question 87

A technician is troubleshooting a user's laptop that is unable to connect to a
corporate server. The technician thinks the issue pertains to routing. Which of
the following commands should the technician use to identify the issue?

    A. tcpdump
    B. dig
    C. tracert
    D. arp

Answer(s): C. tracert

Explanation: Tracert identifies routing failures by showing each hop from the
source to the destination. It reveals where packets stop or are misrouted.

Question 88

After installing a series of Cat 8 keystones, a data center architect notices
higher than normal interference during tests. Which of the following steps
should the architect take to troubleshoot the issue?

    A. Check to see if the end connections were wrapped in copper tape before terminating.
    B. Use passthrough modular crimping plugs instead of traditional crimping plugs.
    C. Connect the RX/TX wires to different pins.
    D. Run a speed test on a device that can only achieve 100Mbps speeds.

Answer(s): A. Check to see if the end connections were wrapped in copper tape
before terminating.

Explanation: Cat 8 cabling requires proper shield continuity. Keystones must be
wrapped with shielding copper tape before termination to prevent EMI leakage and
interference.

Question 89

A small business is deploying new phones, and some of the phones have full HD
videoconferencing features. The Chief Information Officer is concerned that the
network might not be able to handle the traffic if the traffic reaches a certain
threshold. Which of the following can the network engineer configure to help
ease these concerns?

    A. A VLAN with 100Mbps speed limits
    B. An IP helper to direct VoIP traffic
    C. A smaller subnet mask
    D. Full duplex on all user ports

Answer(s): A. A VLAN with 100Mbps speed limits

Explanation: Applying rate limiting on a VLAN prevents VoIP/video endpoints from
consuming excessive bandwidth. HD video conferencing can saturate links, so
capping bandwidth ensures stability for other services.

Question 90

A virtual machine has the following configuration: IPv4 address: 169.254.10.10
Subnet mask: 255.255.0.0 The virtual machine can reach collocated systems but
cannot reach external addresses on the internet. Which of the following is most
likely the root cause?

    A. The subnet mask is incorrect.
    B. The DHCP server is offline.
    C. The IP address is an RFC1918 private address.
    D. The DNS server is unreachable.

Answer(s): B. The DHCP server is offline.

Explanation: A 169.254.x.x APIPA address indicates DHCP failed. Without a valid
DHCP lease, the VM cannot reach networks beyond the local link.

Question 91

Which of the following is used to estimate the average life span of a device?

    A. RPO
    B. RTO
    C. MTTR
    D. MTBF

Answer(s): D. MTBF

Explanation: MTBF (Mean Time Between Failures) represents expected operational
lifespan and overall reliability of hardware components.

Question 92

Which of the following is the most secure way to provide site-to-site
connectivity?

    A. VXLAN
    B. IKE
    C. GRE
    D. IPSec

Answer(s): D. IPSec

Explanation: IPSec provides encrypted, authenticated tunnels with integrity and
confidentiality, making it the most secure site-to-site method listed.

Question 93

A network technician is terminating a cable to a fiber patch panel in the MDF.
Which of the following connector types is most likely in use?

    A. F-type
    B. RJ11
    C. BNC
    D. SC
    F. Which of the following connector types is most likely in use?

Answer(s): D. SC

Explanation: SC connectors are commonly used in enterprise-grade fiber patch
panels because of their robust push-pull locking mechanism.

Question 94

A network administrator is connecting two Layer 2 switches in a network. These
switches must transfer data in multiple networks. Which of the following would
fulfill this requirement?

    A. Jumbo frames
    B. 802.1Q tagging
    C. Native VLAN
    D. Link aggregation

Answer(s): B. 802.1Q tagging

Explanation: To carry multiple VLANs between two Layer 2 switches, the link must
be configured as a trunk, which uses 802.1Q tagging. This tagging inserts a VLAN
ID into each Ethernet frame, allowing several networks (VLANs) to travel over
the same physical connection. Jumbo frames = increases MTU size, not related to
VLAN transport Native VLAN = designates untagged traffic, but does not carry
multiple VLANs by itself Link aggregation = increases bandwidth, but without
tagging it cannot transport multiple VLANs 802.1Q is the required technology to
allow multiple VLANs across a switch-to-switch link.

Question 95

A network administrator wants users to be able to authenticate to the corporate
network using a port-based authentication framework when accessing both wired
and wireless devices. Which of the following is the best security feature to
accomplish this task?

    A. 802.1X
    B. Access control list
    C. Port security
    D. MAC filtering

Answer(s): A. 802.1X

Explanation: 802.1X provides centralized port-based authentication using RADIUS
for both wired and wireless clients.

Question 96

Which of the following is most closely associated with a dedicated link to a
cloud environment and may not include encryption?

    A. Direct Connect
    B. Internet gateway
    C. Captive portal
    D. VPN

Answer(s): A. Direct Connect

Explanation: AWS Direct Connect (and similar private cloud links) provide
dedicated Layer 2 connectivity but do not encrypt traffic by default. Encryption
must be added separately.

Question 97

A systems administrator is investigating why users cannot reach a Linux web
server with a browser but can ping the server IP. The server is online, the web
server process is running, and the link to the switch is up. Which of the
following commands should the administrator run on the server first?

    A. traceroute
    B. netstat
    C. tcpdump
    D. arp

Answer(s): B. netstat

Explanation: netstat verifies whether the web server is listening on port 80/443
and whether inbound connection attempts are reaching the service.

Question 98

Which of the following devices can operate in multiple layers of the OSI model?

    A. Hub
    B. Switch
    C. Transceiver
    D. Modem

Answer(s): B. Switch

Explanation: Modern switches operate at Layer 2, and multilayer switches
additionally perform Layer 3 routing, making them multi-layer devices.

Question 99

Before using a guest network, an administrator requires users to accept the
terms of use. Which of the following is the best way to accomplish this goal?

    A. Pre-shared key
    B. Autonomous access point
    C. Captive portal
    D. WPA2 encryption

Answer(s): C. Captive portal

Explanation: A captive portal forces users to a web page where they must accept
terms or authenticate before being granted network access. This is standard for
guest networks.

Question 100

A network administrator for a small office is adding a passive IDS to its
network switch for the purpose of inspecting network traffic. Which of the
following should the administrator use?

    A. SNMP trap
    B. Port mirroring
    C. Syslog collection
    D. API integration

Answer(s): B. Port mirroring

Explanation: A passive IDS requires a copy of network traffic. Port mirroring
sends duplicated traffic from selected ports/VLANs to the IDS for analysis.

Question 101

Which of the following most likely requires the use of subinterfaces?

    A. A router with only one available LAN port
    B. A firewall performing deep packet inspection
    C. A hub utilizing jumbo frames
    D. A switch using Spanning Tree Protocol

Answer(s): A. A router with only one available LAN port

Explanation: Routers often use subinterfaces to handle multiple VLANs across a
single physical interface (router-on-a-stick). This is needed when LAN ports are
limited.

Question 102

A company receives a cease-and-desist order from its ISP regarding prohibited
torrent activity. Which of the following should be implemented to comply with
the cease-and-desist order?

    A. MAC security
    B. Content filtering
    C. Screened subnet
    D. Perimeter network

Answer(s): B. Content filtering

Explanation: Content filtering blocks unauthorized application types (like
torrent traffic), preventing violations of ISP acceptable-use policies.

Question 103

Which of the following requires network devices to be managed using a different
set of IP addresses?

    A. Console
    B. Split tunnel
    C. Jump box
    D. Out of band

Answer(s): D. Out of band

Explanation: Out-of-band management uses a dedicated, isolated management
network with its own IP addressing, separate from production traffic.

Question 104

A network administrator wants to configure a backup route in case the primary
route fails. A dynamic routing protocol is not installed on the router. Which of
the following routing features should the administrator choose to accomplish
this task?

    A. Neighbor adjacency
    B. Link state flooding
    C. Administrative distance
    D. Hop count

Answer(s): C. Administrative distance

Explanation: Routers choose routes based on administrative distance. Adding a
static route with a higher distance creates a backup route that activates only
if the primary fails.

Question 105

Which of the following steps of the troubleshooting methodology should a
technician take to confirm a theory?

    A. Duplicate the problem.
    B. Identify the symptoms.
    C. Gather information.
    D. Determine any changes.

Answer(s): A. Duplicate the problem.

Explanation: To confirm a theory, you must reproduce the issue in a controlled
or repeated way. “Duplicate the problem” validates whether the suspected cause
aligns with observed behavior.

Question 106

A network administrator is deploying a new switch and wants to make sure that
the default priority value was set for a spanning tree. Which of the following
values would the network administrator expect to see?

    A. 4096
    B. 8192
    C. 32768
    D. 36684

Answer(s): C. 32768

Explanation: Default Spanning Tree Protocol bridge priority is 32768. Devices
with lower priority become preferred STP root bridges.

Question 107

A network administrator is configuring a wireless network with an ESSID. Which
of the following is a user benefit of ESSID compared to SSID?

    A. Stronger wireless connection
    B. Roaming between access points
    C. Advanced security
    D. Which of the following is a user benefit of ESSID compared to SSID?

Answer(s): B. Roaming between access points

Explanation: An ESSID spans multiple access points, allowing clients to roam
seamlessly between them while staying connected to the same wireless network
name.

Question 108

A network administrator needs to connect two routers in a point-to-point
configuration and conserve IP space. Which of the following subnets should the
administrator use?

    A. /24
    B. /26
    C. /28
    D. /30

Answer(s): D. /30

Explanation: A /30 network provides exactly 2 usable IPs—perfect for
point-to-point router links with minimal address wastage.

Question 109

An attacker follows an employee through a badge-secured door before the door
closes. Which of the following types of attacks is occurring?

    A. Shoulder surfing
    B. Tailgating
    C. Phishing
    D. On-path

Answer(s): B. Tailgating

Explanation: Tailgating (piggybacking) occurs when an unauthorized person gains
physical access by following someone through a secure entry point.

Question 110

A research facility is expecting to see an exponential increase in global
network traffic in the near future. The offices are equipped with 2.5Gbps fiber
connections from the ISP, but the facility is currently only utilizing 1Gbps
connections. Which of the following would need to be configured in order to use
the ISP's connection speed?

    A. 802.1Q tagging
    B. Network address translation
    C. Port duplex
    D. Link aggregation

Answer(s): D. Link aggregation

Explanation: To exceed 1Gbps per path, multiple switch ports must be combined
using link aggregation (LACP), allowing throughput beyond a single interface’s
capacity.

Question 111

A VoIP phone is plugged in to a port but cannot receive calls. Which of the
following needs to be done on the port to address the issue?

    A. Trunk all VLANs on the port.
    B. Configure the native VLAN.
    C. Tag the traffic to voice VLAN.
    D. Disable VLANs.

Answer(s): C. Tag the traffic to voice VLAN.

Explanation: VoIP phones often send traffic on a tagged voice VLAN. If tagging
is not correctly configured, signaling and call control traffic will fail.

Question 112

Which of the following can support a jumbo frame?

    A. Access point
    B. Bridge
    C. Hub
    D. Switch

Answer(s): D. Switch

Explanation: Switches commonly support jumbo frames (9000-byte MTU), especially
in data-intensive environments. Hubs and APs do not.

Question 113

A network manager wants to implement a SIEM system to correlate system events.
Which of the following protocols should the network manager verify?

    A. NTP
    B. DNS
    C. LDAP
    D. DHCP

Answer(s): A. NTP

Explanation: A SIEM requires accurate timestamps to correlate logs. NTP
synchronizes time across devices, making correct event ordering possible.

Question 114

A network engineer is designing a secure communication link between two sites.
The entire data stream needs to remain confidential. Which of the following will
achieve this goal?

    A. GRE
    B. IKE
    C. ESP
    D. AH

Answer(s): C. ESP

Explanation: IPSec ESP (Encapsulating Security Payload) provides encryption,
integrity, authentication, and anti-replay protection—ensuring confidentiality.

Question 115

Which of the following protocols has a default administrative distance value of
90?

    A. RIP
    B. EIGRP
    C. OSPF
    D. BGP

Answer(s): B. EIGRP

Explanation: EIGRP uses a default administrative distance of 90 for internal
routes, making it preferred over many other dynamic protocols when equal routing
paths exist.

Question 116

An office is experiencing intermittent connection issues. A network engineer
identifies that the issue occurs whenever someone uses the fax machine that is
connected to a switch. Which of the following should the engineer do first to
resolve the issue?

    A. Run a new Cat 5 line.
    B. Enable 802.1Q tagging.
    C. Change the MTU.
    D. Configure a VLAN.

Answer(s): D. Configure a VLAN.

Explanation: Fax machines using VoIP adapters or analog gateways can send
broadcast or disruptive traffic. Placing them in a separate VLAN isolates their
traffic and prevents interference.

Question 117

A network engineer receives a vendor alert regarding a vulnerability in a router
CPU. Which of the following should the engineer do to resolve the issue?

    A. Update the firmware.
    B. Replace the system board.
    C. Patch the OS.
    D. Isolate the system.

Answer(s): A. Update the firmware.

Explanation: Hardware-level vulnerabilities in routers are normally addressed
through firmware updates, which include vendor-supplied microcode fixes and
security patches. Updating the firmware is the manufacturer’s intended
remediation path and is the correct action.

Question 118

Which of the following fiber connector types is the most likely to be used on a
network interface card?

    A. LC
    B. SC
    C. ST
    D. MPO

Answer(s): A. LC

Explanation: LC connectors are the most common connectors used on modern NICs
and SFP/SFP+ modules because they are small-form-factor and designed for
high-density environments.

Question 119

Which of the following connectors provides console access to a switch?

    A. ST
    B. RJ45
    C. BNC
    D. SFP

Answer(s): B. RJ45

Explanation: Most switch console ports use an RJ45 console interface for serial
management access (often via rollover cable).

Question 120

A network administrator notices interference with industrial equipment in the
2.4GHz range. Which of the following technologies would most likely mitigate
this issue? (Choose two.)

    A. Mesh network
    B. 5GHz frequency
    C. Omnidirectional antenna
    D. Non-overlapping channel
    E. Captive portal
    F. Ad hoc network

Answer(s): B. 5GHz frequency, D. Non-overlapping channel

Explanation: Industrial equipment frequently interferes with the 2.4GHz band, so
moving clients to 5GHz avoids that interference entirely. Additionally,
configuring non-overlapping channels (1, 6, 11) minimizes co-channel
interference in 2.4GHz deployments.

Question 121

Which of the following network topologies contains a direct connection between
every node in the network?

    A. Mesh
    B. Star
    C. Hub-and-spoke
    D. Point-to-point

Answer(s): A. Mesh

Explanation: A full mesh topology provides a direct physical or logical link
between every pair of nodes, maximizing redundancy and fault tolerance.

Question 122

A network architect needs to create a wireless field network to provide reliable
service to public safety vehicles. Which of the following types of networks is
the best solution?

    A. Mesh
    B. Ad hoc
    C. Point-to-point
    D. Infrastructure

Answer(s): A. Mesh

Explanation: A wireless mesh network is ideal for mobile public-safety
operations because each node can route traffic dynamically, providing resilience
and wide-area coverage even if individual nodes move or fail.

Question 123

A manager is evaluating the environmental design of a data center. Which of the
following setups should the manager implement if the maximum thermal dissipation
is the highest concern?

    A. A blue-green
    B. A hot-cold
    C. An east-west
    D. An active-passive

Answer(s): B. A hot-cold

Explanation: A hot-aisle / cold-aisle design improves airflow efficiency and
maximizes heat dissipation by separating hot exhaust air from cold intake paths.

Question 124

A network administrator configured a router interface as 10.0.0.95
255.255.255.240. The administrator discovers that the router is not routing
packets to a web server with IP 10.0.0.81/28. Which of the following is the best
explanation?

    A. The web server is in a different subnet.
    B. The router interface is a broadcast address.
    C. The IP address space is a class A network.
    D. The subnet is in a private address space.

Answer(s): B. The router interface is a broadcast address.

Explanation: In the 10.0.0.80/28 subnet, the address 10.0.0.95 is the broadcast
address, so the router cannot use it as an interface IP. Because the router is
configured with an invalid (broadcast) address, it cannot route packets.

Question 125

A network administrator is notified that a user cannot access resources on the
network. The network administrator checks the physical connections to the
workstation labeled User 3 and sees the Ethernet is properly connected. However,
the network interface's indicator lights are not blinking on either the computer
or the switch. Which of the following is the most likely cause?

    A. The switch failed.
    B. The default gateway is wrong.
    C. The port is shut down.
    D. The VLAN assignment is incorrect.

Answer(s): C. The port is shut down.

Explanation: In the 10.0.0.80/28 subnet, the address 10.0.0.95 is the broadcast
address, so the router cannot use it as an interface IP. Because the router is
configured with an invalid (broadcast) address, it cannot route packets.

Question 126

Which of the following internal routing protocols is best characterized as
having fast convergence and being loop-free?

    A. BGP
    B. STP
    C. OSPF
    D. RIP

Answer(s): C. OSPF

Explanation: OSPF, a link-state protocol, converges rapidly and uses the
Dijkstra SPF algorithm, which builds loop-free routing trees.

Question 127

An administrator is setting up an SNMP server for use in the enterprise network
and needs to create device IDs within a MIB. Which of the following describes
the function of a MIB?

    A. DHCP relay device
    B. Which of the following describes the function of a MIB?
    C. Definition file for event translation
    D. Network access controller

Answer(s): C. Definition file for event translation

Explanation: In SNMP, the Management Information Base (MIB) acts as a definition
file that describes all managed objects, their OIDs, and how events/values
should be interpreted. It translates device data into a standardized structure
that SNMP managers can read.

Question 128

A critical infrastructure switch is identified as end-of-support. Which of the
following is the best next step to ensure security?

    A. Apply the latest patches and bug fixes.
    B. Decommission and replace the switch.
    C. Ensure the current firmware has no issues.
    D. Isolate the switch from the network.

Answer(s): B. Decommission and replace the switch.

Explanation: End-of-support hardware no longer receives security patches, making
it a long-term vulnerability. The only correct mitigation is to decommission and
replace the switch with supported hardware.

Question 129

A company's marketing team created a new application and would like to create a
DNS record for newapplication.comptia.org that always resolves to the same
address as wwww.comptia.org. Which of the following records should the
administrator use?

    A. SOA
    B. MX
    C. CNAME
    D. NS

Answer(s): C. CNAME

Explanation: A CNAME (canonical name) record maps one domain name to another. It
ensures that newapplication.comptia.org always resolves to the same address as
www.comptia.org , automatically inheriting any changes.

Question 130

A network administrator wants to implement security zones in the corporate
network to control access to only individuals inside of the corporation. Which
of the following security zones is the best solution?

    A. Extranet
    B. Trusted
    C. VPN
    D. Public

Answer(s): B. Trusted

Explanation: A Trusted zone contains internal systems accessible only by
internal or authenticated corporate users. It is specifically meant to restrict
access to authorized individuals within the organization. Exams QUESTION: 131
Which of the following network devices converts wireless signals to electronic
signals? A. Router B. Firewall C. Access point D. Load balancer Answer(s): C
Explanation: An access point performs radio-to-electrical signal conversion to
bridge wireless clients onto the wired Ethernet network.

Question 132

A network administrator deployed wireless networking in the office area. When
users visit the outdoor patio and try to download emails with large attachments
or stream training videos, they notice buffering issues. Which of the following
is the most likely cause?

    A. Network congestion
    B. Wireless interference
    C. Signal degradation
    D. Client disassociation

Answer(s): C. Signal degradation

Explanation: As users move farther from the AP and outdoors, RF signal strength
naturally drops. This signal degradation reduces throughput and causes buffering
during high-bandwidth activities.

Question 133

Which of the following activities would have groups from different departments
evaluate the disaster recovery process?

    A. Validation test
    B. SLA alignment
    C. Tabletop exercises
    D. Active-active approach

Answer(s): C. Tabletop exercises

Explanation: Tabletop exercises simulate disaster scenarios and bring together
multiple departments to walk through roles, responsibilities, and outcomes. This
is the collaborative evaluation method referenced in the question.

Question 134

Which of the following routing protocols uses an autonomous system number?

    A. IS-IS
    B. OSPF
    C. BGP
    D. EIGRP

Answer(s): C. BGP

Explanation: BGP (Border Gateway Protocol) is an exterior gateway protocol that
relies on Autonomous System Numbers (ASNs) to exchange routing information
between independent networks.

Question 135

Which of the following is a characteristic of the application layer?

    A. It relies upon other layers for packet delivery.
    B. It checks independently for packet loss.
    C. It encrypts data in transit.
    D. It performs address translation.

Answer(s): A. It relies upon other layers for packet delivery.

Explanation: The application layer provides network services to applications but
relies on lower layers (transport, network, data link) to handle delivery,
addressing, and transmission reliability.

Question 136

Which of the following IP transmission types encrypts all of the transmitted
data?

    A. ESP
    B. AH
    C. GRE
    D. UDP
    E. TCP

Answer(s): A. ESP

Explanation: IPsec ESP (Encapsulating Security Payload) provides full encryption
of packet contents. By contrast, AH provides no encryption, and GRE/TCP/UDP are
not encryption mechanisms.

Question 137

Which of the following should be configured so users can authenticate to a
wireless network using company credentials?

    A. SSO
    B. SAML
    C. MFA
    D. RADIUS

Answer(s): D. RADIUS

Explanation: Enterprise Wi-Fi uses 802.1X with a RADIUS server to authenticate
users with corporate credentials (e.g., Active Directory). SAML/SSO apply to web
authentication, not Wi-Fi.

Question 138

A network engineer performed a migration to a new mail server. The engineer
changed the MX record, verified the change was accurate, and confirmed the new
mail server was reachable via the IP address in the A record. However, users are
not receiving email. Which of the following should the engineer have done to
prevent the issue from occurring?

    A. Change the email client configuration to match the MX record.
    B. Reduce the TTL record prior to the MX record change.
    C. Perform a DNS zone transfer prior to the MX record change.
    D. Update the NS record to reflect the IP address change.

Answer(s): B. Reduce the TTL record prior to the MX record change.

Explanation: DNS records—especially MX records—may be cached for the full
duration of their TTL (Time To Live). If the TTL was high before the migration,
external mail servers may continue using the old MX record for hours or days.
Reducing the TTL before changing MX ensures the update propagates quickly.
Reference: https://perfectmail.com/kb/changing_dns_records

Question 139

Which of the following should a network administrator configure when adding OT
devices to an organization's architecture?

    A. Honeynet
    B. Data-at-rest encryption
    C. Time-based authentication
    D. Network segmentation

Answer(s): D. Network segmentation

Explanation: Operational Technology (OT) systems such as PLCs and SCADA
controllers are highly sensitive and must be isolated from corporate IT
networks. Network segmentation protects OT devices by minimizing attack surface,
preventing lateral movement, and enforcing strict control over communications
between IT and OT environments. Reference:
https://www.mckinsey.com/capabilities/risk-and-resilience/our-insights/cybersecurity/how-to-
enhance-the-cybersecurity-of-operational-technology-environments

Question 140

To reduce costs and increase mobility, a Chief Technology Officer (CTO) wants to
adopt cloud services for the organization and its affiliates. To reduce the
impact for users, the CTO wants key services to run from the on- site data
center and enterprise services to run in the cloud. Which of the following
deployment models is the best choice for the organization?

    A. Public
    B. Hybrid
    C. SaaS
    D. Private

Answer(s): B. Hybrid

Explanation: A hybrid cloud deployment blends on-premises resources with
cloud-based services, allowing the organization to keep essential workloads
local while moving enterprise services into the cloud for flexibility and
scalability. Reference: https://www.cloudwards.net/cloud-deployment-models/

Question 141

Which of the following is used to describe the average duration of an outage for
a specific service?

    A. RPO
    B. MTTR
    C. RTO
    D. MTBF

Answer(s): B. MTTR

Explanation: MTTR (Mean Time To Repair) measures the average time required to
restore a service after a failure. It reflects operational responsiveness and
recovery effectiveness.

Question 142

A network engineer is setting up a new VoIP network for a customer. The current
network is segmented only for computers and servers. No additional switch ports
can be used in the new network. Which of the following does the engineer need to
do to configure the network correctly? (Choose two.)

    A. Change network translation definitions.
    B. Enable 802.1Q.
    C. Implement a routing protocol.
    D. Set up voice VLANs.
    E. Reconfigure the DNS.
    F. Place devices in the perimeter network.

Answer(s): B. Enable 802.1Q., E. Reconfigure the DNS.

Explanation: 802.1Q is the standard for VLAN tagging in Ethernet frames, which
allows for the use of multiple VLANs on a single switch port. Enabling 802.1Q is
necessary to segment voice traffic and data traffic on the same physical
infrastructure. Setting up voice VLANs helps prioritize voice traffic over data
traffic to ensure better Quality of Service (QoS) for VoIP communications. This
creates a separate VLAN specifically for voice, improving performance and
reducing interference from data traffic.

Question 143

A network rack has four servers and four switches with dual power supplies. Only
one intelligent PDU is installed in the rack. Which of the following is the
reason to add a second PDU?

    A. Power redundancy
    B. Failed PSU monitoring
    C. Surge protection
    D. Electricity conservation

Answer(s): A. Power redundancy

Explanation: Adding a second Power Distribution Unit (PDU) provides power
redundancy, ensuring that if one PDU or power source fails, the other can
continue supplying power to critical devices like servers and switches. This is
important for maintaining uptime and preventing service outages in case of power
issues.

Question 144

Which of the following allows a user to connect to an isolated device on a
stand-alone network?

    A. Jump box
    B. API gateway
    C. Secure Shell
    D. Clientless VPN

Answer(s): A. Jump box

Explanation: A jump box (or jump server) is a secure device that allows a user
to access and connect to an isolated network or device that is otherwise
inaccessible. It serves as an intermediary between the user and the isolated
device, ensuring security and control when managing or troubleshooting devices
in a stand-alone or restricted network.

Question 145

Early in the morning, an administrator installs a new DHCP server. In the
afternoon, some users report they are experiencing network outages. Which of the
following is the most likely issue?

    A. The administrator did not provision enough IP addresses.
    B. The administrator configured an incorrect default gateway.
    C. The administrator did not provision enough routes.
    D. The administrator did not provision enough MAC addresses.

Answer(s): A. The administrator did not provision enough IP addresses.

Explanation: If a new DHCP server is installed and some users are experiencing
network outages later, it is most likely that the DHCP server did not have
enough IP addresses in its pool to assign to all devices. Once the available IP
addresses are exhausted, new devices cannot obtain an IP address, leading to
network connectivity issues.

Question 146

A company is implementing a policy that will not allow employees to bring
personal devices to the office and connect to the wireless network. Which of the
following is the best way to enforce this policy?

    A. MAC filtering
    B. 802.1X
    C. Port security
    D. ACL

Answer(s): B. 802.1X

Explanation: 802.1X is a network access control protocol that provides
authentication to devices trying to connect to the network. By using 802.1X, the
company can enforce a policy that requires only authorized devices (such as
company-provided devices) to authenticate before being granted access to the
network, effectively preventing personal devices from connecting. This is the
best way to enforce such a policy because it allows for strong security and
authentication at the network access level. Other methods like MAC filtering or
ACLs can be bypassed more easily, and port security is generally more applicable
to wired networks.

Question 147

A network engineer is troubleshooting an issue with a VoIP network. After
performing analysis, the engineer found that when users upload large files,
voice quality is severely degraded. When no other traffic is on the network,
voice quality is fine. Which of the following should the engineer do to most
likely resolve the issue?

    A. Enable MAC filtering.
    B. Reduce the VLAN database.
    C. Configure QoS on the router.
    D. Implement ACLs.

Answer(s): C. Configure QoS on the router.

Explanation: Quality of Service (QoS) prioritizes certain types of traffic over
others. In this case, configuring QoS on the router would prioritize voice
traffic over data traffic (such as large file uploads), ensuring that VoIP calls
maintain high quality even when the network is under heavy load. This prevents
the voice traffic from being affected by bandwidth-heavy activities like file
uploads.

Question 148

Which of the following disaster recovery metrics is used to describe the amount
of data that is lost since the last backup?

    A. MTTR
    B. RTO
    C. RPO
    D. MTBF

Answer(s): C. RPO

Explanation: RPO refers to the maximum acceptable amount of data loss measured
in time. It indicates the point in time to which data must be recovered after a
disaster (e.g., how much data can be lost since the last backup). It helps
organizations determine how frequently backups should occur to meet their
disaster recovery goals.

Question 149

A network administrator needs to improve network monitoring. Which of the
following should the administrator do first?

    A. Establish baseline metrics.
    B. Implement a SIEM.
    C. Perform regular packet captures.
    D. Conduct availability monitoring.

Answer(s): A. Establish baseline metrics.

Explanation: Before improving network monitoring, it is important to establish
baseline metrics. This involves measuring the normal performance and behavior of
the network, such as bandwidth usage, latency, packet loss, and other key
indicators. Having a baseline allows the administrator to detect anomalies,
identify performance issues, and measure the impact of any changes made to the
network.

Question 150

A network administrator is troubleshooting issues with a DHCP server at a
university. More students have recently arrived on campus, and the users are
unable to obtain an IP address. Which of the following should the administrator
do to address the issue?

    A. Enable IP helper.
    B. Change the subnet mask.
    C. Increase the scope size.
    D. Add address exclusions.

Answer(s): C. Increase the scope size.

Explanation: When more students have arrived and users are unable to obtain an
IP address, it typically means the DHCP server's available pool of IP addresses
has been exhausted. Increasing the scope size on the DHCP server will expand the
range of available IP addresses, allowing more devices to obtain an IP address
and connect to the network.

Question 151

Which of the following is designed to distribute network traffic among devices
based on the quantity of traffic?

    A. Load balancer
    B. Router
    C. Proxy
    D. Switch

Answer(s): A. Load balancer

Explanation: A load balancer is designed to distribute network traffic among
multiple devices (such as servers) based on factors like the quantity of traffic
or server load. This helps ensure efficient use of resources, prevents any one
device from being overwhelmed, and improves the overall performance and
reliability of the network.

Question 152

A user recently moved a workstation to a different part of the office. The user
is able to access the internet and print but is unable to access server
resources. Which of the following is the most likely cause of the issue?

    A. Incorrect default gateway
    B. Wrong VLAN assignment
    C. Error-disabled port
    D. Duplicate IP address

Answer(s): B. Wrong VLAN assignment

Explanation: If the user can access the internet and print but is unable to
access server resources, the most likely issue is that the workstation is
assigned to the wrong VLAN. VLANs are used to segment network traffic, and if
the workstation is in a different VLAN than the servers, it won't be able to
access those resources unless proper routing is configured between the VLANs.

Question 153

A technician is planning an equipment installation into a rack in a data center
that practices hot aisle/cold aisle ventilation. Which of the following
directions should the equipment exhaust face when installed in the rack?

    A. Sides
    B. Top
    C. Front
    D. Rear

Answer(s): D. Rear

Explanation: In a data center with hot aisle/cold aisle ventilation, equipment
is typically installed so that cool air is pulled in from the front (facing the
cold aisle) and warm air is exhausted out the rear (facing the hot aisle). This
arrangement helps maintain proper airflow and cooling efficiency in the data
center.

Question 154

A network administrator needs to add 255 useable IP addresses to the network. A
/24 is currently in use. Which of the following prefixes would fulfill this
need?

    A. /23
    B. /25
    C. /29
    D. /32

Answer(s): A. /23

Explanation: A /23 subnet provides 512 total IP addresses, with 510 usable IP
addresses (after accounting for the network and broadcast addresses). This would
satisfy the need for 255 usable IP addresses. The current /24 subnet provides
256 total IP addresses, with 254 usable addresses, so moving to a /23 subnet
will double the number of available IP addresses.

Question 155

Which of the following allows an organization to map multiple internal devices
to a single external-facing IP address?

    A. NAT
    B. BGP
    C. OSPF
    D. FHRP

Answer(s): A. NAT

Explanation: NAT allows an organization to map multiple internal devices, which
have private IP addresses, to a single external-facing public IP address. This
process helps conserve public IP addresses and enables devices on a private
network to communicate with external networks, such as the internet, using a
single IP address.

Question 156

Which of the following steps in the troubleshooting methodology includes
checking logs for recent changes?

    A. Identify the problem.
    B. Document the findings and outcomes.
    C. Test the theory to determine cause.
    D. Establish a plan of action.

Answer(s): A. Identify the problem.

Explanation: During the Identify the problem step of the troubleshooting
methodology, checking logs for recent changes is a key part of gathering
information to help understand the issue. This helps determine if any recent
configurations, updates, or changes could be related to the problem.

Question 157

Which of the following configurations exempts traffic to the internet from
traversing a VPN?

    A. Client-to-site
    B. Active-passive
    C. Split-tunnel
    D. Out-of-band

Answer(s): C. Split-tunnel

Explanation: A split-tunnel configuration allows certain traffic, such as
traffic destined for the internet, to bypass the VPN and go directly to its
destination without traversing the VPN tunnel. This helps reduce the load on the
VPN by only routing traffic that is meant for the internal network through the
tunnel, while internet traffic goes directly to the internet.

Question 158

Which of the following ports creates a secure connection to a directory service?

    A. 22
    B. 389
    C. 445
    D. 636

Answer(s): D. 636

Explanation: Port 636 is used for LDAPS (LDAP Secure), which creates a secure,
encrypted connection to a directory service using SSL/TLS. This is the secure
version of the LDAP protocol, which typically operates on port 389 without
encryption.

Question 159

A network engineer configures a new switch and connects it to an existing switch
for expansion and redundancy. Users immediately lose connectivity to the
network. The network engineer notes the following spanning tree information from
both switches.
![img for question 159](https://free-braindumps.com/images/exam-dumps/N10-009/05f51fcf-3b81-43a9-86e7-7aee49a9b74a.jpg)
Which of the following best describes the issue?

    A. The port cost should not be equal.
    B. The ports should use link aggregation.
    C. A root bridge needs to be identified.
    D. The switch should be configured for RSTP.

Answer(s): D. The switch should be configured for RSTP.

Explanation: RSTP (802.1w) would provide faster convergence and help prevent
loops in the network. With traditional STP, both switches may be incorrectly
forwarding on all ports due to slow convergence or misconfiguration, which leads
to a broadcast storm or looping issue. RSTP can quickly resolve this by
identifying which port should block traffic to prevent loops.

Question 160

A network administrator is implementing security zones for each department.
Which of the following should the administrator use to accomplish this task?

    A. ACLs
    B. Port security
    C. Content filtering
    D. NAC

Answer(s): A. ACLs

Explanation: Access Control Lists (ACLs) are used to define rules that allow or
deny traffic between different network zones. By implementing ACLs on network
devices such as routers or firewalls, a network administrator can control the
traffic flow between departments or zones, enforcing security policies and
isolating departments as needed.

Question 161

Which of the following protocols is used to route traffic on the public
internet?

    A. BGP
    B. OSPF
    C. EIGRP
    D. RIP

Answer(s): A. BGP

Explanation: Border Gateway Protocol (BGP) is the protocol used to route traffic
between different autonomous systems (AS) on the public internet. It determines
the best path for data packets across multiple networks based on various
attributes such as path length, policies, and network reliability. BGP is the
backbone of internet routing and ensures that data can traverse between
different networks globally.

Question 162

Which of the following protocols provides remote access utilizing port 22?

    A. SSH
    B. Telnet
    C. TLS
    D. RDP

Answer(s): A. SSH

Explanation: SSH (Secure Shell) is a protocol that provides secure remote access
to devices over a network. It uses port 22 by default and encrypts the
connection, ensuring secure data transmission. SSH is commonly used by network
administrators for securely managing servers and other network devices remotely.

Question 163

After changes were made to a firewall, users are no longer able to access a web
server. A network administrator wants to ensure that ports 80 and 443 on the web
server are still accessible from the user IP space. Which of the following
commands is best suited to perform this testing?

    A. dig
    B. ifconfig
    C. ping
    D. nmap

Answer(s): D. nmap

Explanation: nmap (Network Mapper) is the best tool for testing whether specific
ports (e.g., 80 for HTTP and 443 for HTTPS) are open and accessible on a web
server. It is commonly used for network discovery and security auditing and
allows the network administrator to scan a target system to determine the status
of specific ports. For example, the administrator can run the following command:
nmap -p 80,443 <web_server_IP> This command will check whether ports 80 and 443
are open on the specified web server.

Question 164

Which of the following attacks would most likely cause duplicate IP addresses in
a network?

    A. Rogue DHCP server
    B. DNS poisoning
    C. Social engineering
    D. Denial-of-service

Answer(s): A. Rogue DHCP server

Explanation: A rogue DHCP server can cause duplicate IP addresses on a network
by assigning conflicting IP addresses to devices. When an unauthorized DHCP
server operates in a network, it may offer IP configurations that overlap with
those assigned by the legitimate DHCP server. This results in duplicate IP
address assignments, leading to connectivity issues for affected devices.

Question 165

An organization wants better network visibility. The organization's requirements
include: Multivendor/OS-monitoring capabilities Real-time collection Data
correlation Which of the following meets these requirements?

    A. SNMP
    B. SIEM
    C. Nmap
    D. Syslog

Answer(s): B. SIEM

Explanation: SIEM (Security Information and Event Management) systems provide
the capabilities required for better network visibility, as described in the
organization's requirements. SIEM solutions: 1. Multivendor/OS Monitoring
Capabilities: Collect and process data from multiple sources, including diverse
vendors and operating systems. 2. Real-time Collection: Offer real-time
monitoring and logging of events across the network. 3. Data Correlation:
Analyze and correlate data from various devices and systems to identify
patterns, anomalies, or security events. 32 33 34 35 36

Question 166

An administrator is evaluating the use of authentication within SNMP. Which of
the following is the most secure way of authenticating devices using only SNMP?

    A. Use version 1 of SNMP and use a community string to serve as a PSK
    B. Use version 3 of SNMP and set up trap messages for critical events on the network
    C. Use version 2c of SNMP and use informs to validate device authentication
    D. Use version 2u of SNMP to authenticate devices for network monitoring

Answer(s): B. Use version 3 of SNMP and set up trap messages for critical events
on the network

Explanation: SNMP version 3 (SNMPv3) provides the most secure way to
authenticate devices and manage network monitoring. Unlike earlier versions
(SNMPv1 and SNMPv2c), SNMPv3 includes robust security features such as: 1.
Authentication: Supports authentication using user-based security models (USM),
ensuring only authorized users can access SNMP data. 2. Encryption: Provides
encryption for SNMP messages, preventing data from being intercepted or tampered
with. 3. Trap Messages: Allows configuring trap messages for critical events,
enabling real-time alerts for network administrators.

Question 167

A company has observed increased user traffic to gambling websites and would
like to limit this behavior on work computers. Which of the following should the
company most likely implement?

    A. ACLS
    B. Content filter
    C. Port security
    D. Screened subnet

Answer(s): B. Content filter

Explanation: A content filter is the most appropriate solution for restricting
access to gambling websites and other unwanted online content. Content filtering
works by analyzing and blocking access to specific websites or categories of
content based on predefined rules or policies. It can be implemented at the
firewall, proxy server, or through specialized filtering software.

Question 168

Following a fire in a data center, the cabling was replaced. Soon after an
administrator notices network issues. Which of the following are the most likely
causes of the network issues? (Choose two.)

    A. The switches are not the correct voltage
    B. The HVAC system was not verified as fully functional after the fire
    C. The VLAN database was not deleted before the equipment was brought back online
    D. The RJ45 cables were replaced with unshielded cables
    E. The wrong transceiver type was used for the new termination
    F. The new RJ45 cables are a higher category than the old ones

Answer(s): D. The RJ45 cables were replaced with unshielded cables, E. The wrong
transceiver type was used for the new termination

Explanation: The RJ45 cables were replaced with unshielded cables Unshielded
cables (e.g., UTP) can cause network issues in environments with high
electromagnetic interference (EMI), such as data centers. Shielded cables (e.g.,
STP or FTP) are typically used in such environments to minimize interference and
ensure reliable communication. The wrong transceiver type was used for the new
termination Using the wrong transceiver (e.g., mismatched single-mode vs.
multimode fiber, or incorrect connector type) can cause connectivity issues,
such as failure to establish a link or poor signal quality. This is especially
common when cables are replaced without verifying compatibility with the
transceivers and switches.

Question 169

Cloud computing has the capability to meet increased and decreased demands for
computing infrastructure for a short period of time. Which of the following best
describes this characteristic?

    A. Efficiency
    B. Elasticity
    C. Multitenancy
    D. Scalability

Answer(s): B. Elasticity

Explanation: Elasticity in cloud computing refers to the ability of the system
to automatically scale resources up or down based on demand. This capability
allows organizations to handle short-term fluctuations in workload without
over-provisioning or underutilizing resources. For example, during a
high-traffic event, the cloud can add resources temporarily, and once the demand
decreases, it scales them back down.

Question 170

Which of the following can also provide a security feature when implemented?

    A. NAT
    B. BGP
    C. FHRP
    D. EIGRP

Answer(s): A. NAT

Explanation: Network Address Translation (NAT) can provide a security feature by
hiding the internal IP addresses of a network from external entities. NAT
translates private IP addresses into a public IP address (or a smaller pool of
public IPs) for internet access. This makes it harder for external attackers to
directly target internal devices since their private IPs are not exposed.

Question 171

Which of the following best describes the transmission format that occurs at the
transport layer over connectionless communication?

    A. Datagram
    B. Segment
    C. Frames
    D. Packets

Answer(s): A. Datagram

Explanation: At the transport layer, connectionless communication (as used by
protocols like UDP - User Datagram Protocol) operates with data units called
datagrams. Datagrams are self-contained, independent packets that carry enough
information for routing from the source to the destination without the need for
an established connection.

Question 172

Which of the following is most likely to work with an FC connection and offers
more scalability?

    A. DAS
    B. SAN
    C. SSE
    D. NAS

Answer(s): B. SAN

Explanation: SAN (Storage Area Network) is most likely to work with an FC (Fibre
Channel) connection and offers greater scalability. SANs use high-speed
networks, often employing Fibre Channel, to provide block-level storage to
servers. This setup is highly scalable, allowing organizations to add more
storage capacity or devices as needed while maintaining performance and
flexibility.

Question 173

A company is moving to a hybrid cloud model. As part of this move the mail
server will be moved to the cloud. The systems administrator needs to ensure the
mail server continues to receive email. Which of the following types of DNS
records should the systems administrator update?

    A. NS
    B. PTR
    C. MX
    D. A

Answer(s): C. MX

Explanation: MX (Mail Exchange) records in DNS specify the mail servers
responsible for receiving emails for a domain. When moving the mail server to
the cloud, the systems administrator must update the MX record to point to the
new mail server's hostname or IP address in the cloud. This ensures that email
traffic is routed correctly to the new server.

Question 174

A network engineer is configuring network ports in a public office. To increase
security, the engineer wants the ports to allow network connections only after
authentication. Which of the following security features should the engineer
use?

    A. Port security
    B. 802.1X
    C. MAC filtering
    D. Access control list

Answer(s): B. 802.1X

Explanation: 802.1X is a network access control protocol that provides
port-based authentication. It ensures that only authenticated devices can
connect to the network through a switch or access point. When implemented,
802.1X requires devices to authenticate using credentials, such as usernames and
passwords, or certificates before granting access to the network.

Question 175

A network administrator is expanding a network and wants to ensure no
unauthorized redundant links are present. Which of the following should the
administrator use to identify and block redundant links?

    A. SDN
    B. STP
    C. LLDP
    D. OSPF

Answer(s): B. STP

Explanation: Spanning Tree Protocol (STP) is specifically designed to prevent
loops in a network with redundant links. It identifies redundant paths and
places them into a blocking state, ensuring only one active path is used at a
time. This prevents network issues such as broadcast storms caused by loops.

Question 176

A network administrator notices uncommon communication between VMs on ephemeral
ports on the same subnet. The administrator is concerned about that traffic
moving laterally within the network. Which of the following describes the type
of traffic flow the administrator is analyzing?

    A. East-west
    B. Point-to-point
    C. Horizontal-scaling
    D. Hub-and-spoke

Answer(s): A. East-west

Explanation: East-west traffic refers to the communication that occurs between
devices or systems within the same data center or subnet, such as virtual
machines (VMs) communicating with each other. This type of traffic is distinct
from north-south traffic, which involves communication between internal systems
and external networks or clients. The administrator's concern about traffic
moving laterally aligns with the concept of east-west traffic, as it involves
internal, intra-network communication.

Question 177

Which of the following would be violated if an employee accidentally deleted a
customer's data?

    A. Integrity
    B. Confidentiality
    C. Vulnerability
    D. Availability

Answer(s): A. Integrity

Explanation: The integrity of data ensures that the information remains
accurate, complete, and unaltered unless explicitly modified by authorized
personnel. If an employee accidentally deletes customer data, the data's
integrity is violated because the original data is no longer accurate or
complete. This type of incident directly impacts the trustworthiness of the data
within the system.

Question 178

A network engineer is now in charge of all SNMP management in the organization.
The engineer must use a SNMP version that does not utilize plaintext data. Which
of the following is the minimum version of SNMP that supports this requirement?

    A. v1
    B. v2c
    C. v2u
    D. v3

Answer(s): D. v3

Explanation: SNMPv3 is the minimum version of SNMP that provides enhanced
security features, including support for authentication and encryption. Unlike
SNMPv1 and SNMPv2c, which transmit data (including community strings) in
plaintext, SNMPv3 allows for the use of encrypted communication, ensuring data
confidentiality and protection against interception. This makes it the suitable
choice for environments requiring secure SNMP management.

Question 179

A company recently acquired a number of sites and no documentation was provided.
A network administrator needs to identify and document all of the digital assets
in use. Which of the following is the best method for the administrator to use?

    A. Availability monitoring
    B. Packet capture
    C. Physical inventory
    D. Network discovery

Answer(s): D. Network discovery

Explanation: Network discovery is the best method for identifying and
documenting all digital assets in use. It involves using tools and techniques to
scan and identify devices, services, and resources connected to the network.
These tools can detect IP addresses, open ports, operating systems, and other
network details, helping the administrator to create an inventory of digital
assets efficiently and accurately. Other options like physical inventory may
miss devices or services not physically visible, and packet capture is more
focused on analyzing traffic rather than discovering assets.

Question 180

A network administrator recently upgraded a wireless infrastructure with new
APs. Users are reporting that, when stationary, the wireless connection drops
and reconnects after 20 to 30 seconds. While reviewing the logs, the
administrator notices that the APs are changing channels. Which of the following
is the most likely reason for the service interruptions?

    A. Channel interference
    B. Roaming misconfiguration
    C. Network congestion
    D. Insufficient wireless coverage

Answer(s): A. Channel interference

Explanation: The most likely reason for the service interruptions is channel
interference. Wireless Access Points (APs) use a feature called Dynamic
Frequency Selection (DFS) or automatic channel selection to switch to less
congested channels when interference is detected. However, when the APs change
channels, there is a brief service disruption for connected devices. This is
often noticed when the devices are stationary, as they remain connected to the
same AP, but the channel change interrupts the connection temporarily.
Addressing channel interference, such as using non-overlapping channels and
optimizing AP placement, can reduce these disruptions.

Question 181

A network administrator needs to set up a multicast network for audio and video
broadcasting. Which of the following networks would be the most appropriate for
this application?

    A. 172.16.0.0/24
    B. 192.168.0.0/24
    C. 224.0.0.0/24
    D. 240.0.0.0/24

Answer(s): C. 224.0.0.0/24

Explanation: The IP address range 224.0.0.0 to 239.255.255.255 is reserved for
multicast traffic. Multicast is used for applications such as audio and video
broadcasting, where data is sent from one source to multiple recipients
efficiently. The 224.0.0.0/24 range is specifically reserved for local network
multicast (e.g., routing protocol updates). For broader multicast applications,
addresses in the 224.0.1.0 to 239.255.255.255 range would be used. This makes
the 224.0.0.0/24 network the most appropriate choice for setting up a multicast
network.

Question 182

A user connects to a corporate VPN via a web browser and is able to use TLS to
access the internal financial system to input a time card. Which of the
following best describes how the VPN is being used?

    A. Clientless
    B. Client-to-site
    C. Full tunnel
    D. Site-to-site

Answer(s): A. Clientless

Explanation: The term "clientless" VPN refers to a VPN connection that does not
require the user to install specialized software or a VPN client. Instead, the
user connects through a web browser, typically using SSL/TLS protocols (often
referred to as SSL VPN). In this case, the user accesses the corporate VPN and
is able to use TLS to access internal resources, which indicates a clientless
VPN solution. Other options like client-to-site and full tunnel would require
dedicated VPN client software, and site-to-site refers to VPN connections
between two network locations, not individual users.

Question 183

A network administrator needs to fail over services to an off-site environment.
This process will take four weeks to become fully operational. Which of the
following DR concepts does this describe?

    A. Hot site
    B. Warm site
    C. Cold site
    D. Active-active approach

Answer(s): B. Warm site

Explanation: A warm site is a disaster recovery (DR) concept where the off-site
environment is partially configured and can be brought online within a
relatively short time (typically a few days to a few weeks). In this scenario,
the process will take four weeks to become fully operational, which aligns with
the characteristics of a warm site. A hot site would be fully operational and
ready to use immediately, while a cold site would require the longest recovery
time, as it would need to be completely set up from scratch. An active-active
approach involves running services in multiple locations simultaneously, which
is not the case here.

Question 184

A security analyst wants to control internet access based on site reputation and
categorization. The analyst needs a solution that does not require traffic flow
changes. Which of the following solutions would most likely meet these
requirements?

    A. Proxy
    B. DNS filtering
    C. Router ACL
    D. Load balancer

Answer(s): B. DNS filtering

Explanation: DNS filtering allows for the control of internet access based on
site reputation and categorization by filtering DNS requests. This approach does
not require any changes to traffic flow, as it works by intercepting and
blocking or allowing DNS requests based on predefined rules for site reputation
and categorization. The user's requests to access websites are filtered at the
DNS level before any traffic flows to the site.

Question 185

A wireless technician wants to implement a technology that will allow user
devices to automatically navigate to the best available frequency standard.
Which of the following technologies should the technician use?

    A. Band steering
    B. Wireless LAN controller
    C. Directional antenna
    D. Autonomous access point

Answer(s): A. Band steering

Explanation: Band steering is a technology used in wireless networks to
automatically guide devices to the most appropriate frequency band, typically
2.4 GHz or 5 GHz. This ensures that devices are directed to the best available
band based on factors like network congestion and signal strength, thereby
optimizing the user experience. The other options do not directly relate to
automatic navigation to the best frequency band: a wireless LAN controller
manages network configuration but does not directly steer devices, a directional
antenna focuses signal direction but does not manage frequency bands, and an
autonomous access point operates independently but does not perform band
steering.

Question 186

A user called the help desk after business hours to complain that files on a
device are inaccessible and the wallpaper was changed. The network administrator
thinks that this issue is an isolated incident, but the security analyst thinks
the issue might be a ransomware attack. Which of the following troubleshooting
steps should be taken first?

    A. Identify the problem.
    B. Establish a theory.
    C. Document findings.
    D. Create a plan of action.

Answer(s): A. Identify the problem.

Explanation: The first step in troubleshooting is to identify the problem.
Before jumping to conclusions or forming theories, it's essential to gather all
available information about the issue. In this case, understanding whether the
issue is indeed related to a ransomware attack or if it's an isolated incident
requires careful investigation. This step will help clarify the symptoms and
lead to a more informed diagnosis. Once the problem is identified, the next
steps (like establishing a theory or creating a plan of action) can be
undertaken based on the findings.

Question 187

A data center interconnect using a VXLAN was recently implemented. A network
engineer observes slow performance and fragmentation on the interconnect. Which
of the following technologies will resolve the issue?

    A. 802.1Q tagging
    B. Spanning tree
    C. Link aggregation
    D. Jumbo frames

Answer(s): D. Jumbo frames

Explanation: VXLAN (Virtual Extensible LAN) encapsulates Ethernet frames in UDP
packets, which can lead to fragmentation if the maximum transmission unit (MTU)
size is not properly configured. Jumbo frames are Ethernet frames that exceed
the standard MTU of 1500 bytes, allowing larger payloads to be transmitted
without fragmentation. Enabling jumbo frames on the interconnect will allow the
VXLAN traffic to pass without fragmentation, improving performance. The other
options are not directly related to resolving fragmentation issues with VXLAN:
802.1Q tagging is used for VLAN tagging, spanning tree manages network loops,
and link aggregation increases bandwidth but does not address fragmentation.

Question 188

A new server is deployed in a trusted zone and is validated to be online with
all appropriate services running. However, users in a perimeter network cannot
access the server. Which of the following should a network administrator do to
resolve the reported issue?

    A. Create a TXT record on the DNS server for the new server.
    B. Update the firewall ACL to allow access to the new server.
    C. Configure a static route for the user VLAN to the new server.
    D. Insert a static ARP entry for the new server on the Layer 3 switch.

Answer(s): B. Update the firewall ACL to allow access to the new server.

Explanation: Since the server is deployed in a trusted zone and is running
properly, the most likely cause of the issue is a firewall or access control
list (ACL) blocking traffic from the perimeter network to the server. Updating
the firewall ACL to allow access from the perimeter network to the server will
resolve the issue and ensure that the appropriate traffic can flow through the
firewall.

Question 189

Network administrators are using the Telnet protocol to administer network
devices that are on the 192.168.1.0/24 subnet. Which of the following tools
should the administrator use to best identify the devices?

    A. dig
    B. nmap
    C. tracert
    D. telnet

Answer(s): B. nmap

Explanation: nmap is a powerful network scanning tool that can be used to
discover devices on a network, identify open ports, and gather information about
the devices, including which services are running. This makes it ideal for
identifying devices on the 192.168.1.0/24 subnet, which is the goal in this
scenario.

Question 190

A network administrator recently updated configurations on a Layer 3 switch.
Following the updates, users report being unable to reach a specific file
server. Which of the following is the most likely cause?

    A. Incorrect ACLs
    B. Switching loop
    C. Duplicate IP addresses
    D. Wrong default route

Answer(s): A. Incorrect ACLs

Explanation: The most likely cause of the issue is incorrect ACLs (Access
Control Lists). ACLs control the traffic that is allowed or denied between
devices on a network, and if they were misconfigured during the update to the
Layer 3 switch, they could block access to the file server. This is a common
issue when ACLs are not properly adjusted after configuration changes, leading
to connectivity problems.

Question 191

A network engineer wants to implement a solution where all web servers will send
event data over port 514. Which of the following services will accomplish this
task?

    A. Syslog
    B. SMTP
    C. DNS
    D. DHCP

Answer(s): A. Syslog

Explanation: Syslog is a standard protocol used for sending log or event data
from devices, including web servers, to a centralized logging server. Port 514
is the default port used for Syslog communication. This protocol is commonly
used for collecting and managing log data, which fits the requirement for the
web servers to send event data over this specific port.

Question 192

A security administrator wants to discover zero-day attacks before they can be
used on the company's network. Which of the following can the administrator use
to accomplish this task?

    A. Central repository
    B. Honeypot
    C. Next-generation firewall
    D. Evil twin

Answer(s): B. Honeypot

Explanation: A honeypot is a security mechanism designed to attract and trap
potential attackers by simulating vulnerable systems or services. By deploying a
honeypot, a security administrator can observe attack techniques and behaviors,
including zero-day attacks, in a controlled environment. This allows the
administrator to discover and analyze new threats before they can be used on the
company's actual network.

Question 193

Users at a satellite office are experiencing issues when using
videoconferencing. Which of the following should a technician focus on first to
rectify these issues?

    A. Quality of service
    B. Network signal
    C. Time to live
    D. Load balancing

Answer(s): A. Quality of service

Explanation: Quality of Service (QoS) should be the focus first because it is
specifically designed to prioritize certain types of traffic, such as
videoconferencing, over other types of traffic on the network. Videoconferencing
requires consistent bandwidth and low latency for smooth performance. If QoS is
not properly configured, video and audio packets might be delayed or dropped,
leading to poor videoconferencing experiences.

Question 194

A network administrator is trying to locate the switch interface a PC is
connected to. The administrator accesses the local switch, pings the PC IP
address, and then uses the command show arp. Which of the following commands
should the administrator use next?

    A. show route
    B. show mac-address-table
    C. show vlan
    D. show interface

Answer(s): B. show mac-address-table

Explanation: After using the show arp command to identify the IP address-to-MAC
address mapping, the next step is to find which switch interface the PC is
connected to. The show mac-address-table command will display the MAC address
table of the switch, which contains the MAC addresses of devices connected to
each interface. The administrator can then locate the MAC address of the PC in
the table and identify the corresponding switch interface.

Question 195

A user attempts to log in to a corporate website by utilizing a shortcut. The
shortcut has been used many times before. The user then notices some
discrepancies on the company website. Which of the following is most likely the
reason for this issue?

    A. VLAN hopping
    B. ARP spoofing
    C. DNS poisoning
    D. MAC flooding

Answer(s): C. DNS poisoning

Explanation: DNS poisoning occurs when a malicious actor manipulates the DNS
cache to redirect a user's traffic to a fraudulent website, often one that
appears similar to the legitimate site. In this case, the user is trying to log
in using a shortcut, and the discrepancies on the company website suggest that
the traffic might have been redirected to a malicious site. DNS poisoning can
result in the user being unknowingly directed to a fake website, where they may
encounter altered content or be vulnerable to phishing attacks.

Question 196

Which of the following is the correct order of components in a bottom-up
approach for the three-tier hierarchical model?

    A. Access, distribution, and core
    B. Core, root, and distribution
    C. Core, spine, and leaf
    D. Access, core, and root

Answer(s): A. Access, distribution, and core

Explanation: In the bottom-up approach of the three-tier hierarchical model, the
components are ordered as follows: 1. Access layer ­ This is the layer where end
devices (like computers, printers, etc.) connect to the network. 2. Distribution
layer ­ This layer aggregates the traffic from the access layer and provides
policy-based connectivity and routing between different segments of the
network. 3. Core layer ­ The core layer is responsible for high-speed,
high-performance routing between different distribution layers and networks.
This model ensures scalability, redundancy, and efficient traffic management in
large networks.

Question 197

A client with a 2.4GHz wireless network has stated that the entire office is
experiencing intermittent issues with laptops after the WAP was moved. Which of
the following is the most likely reason for these issues?

    A. The network uses a non-overlapping channel.
    B. The signal is reflecting too much.
    C. The network has excessive noise.
    D. A microwave is in the office.

Answer(s): C. The network has excessive noise.

Explanation: The most likely reason for the intermittent wireless issues in this
scenario is excessive noise on the 2.4GHz band. The 2.4GHz frequency range is
commonly used by various devices like microwaves, Bluetooth devices, and other
electronics, which can cause interference and disrupt the wireless signal. When
the wireless access point (WAP) was moved, it could have been positioned closer
to sources of interference, leading to noise and signal degradation, which
causes connectivity issues.

Question 198

Which of the following SD-WAN features allows a router to be shipped directly to
the installation site and does not require site-level configuration?

    A. Zero-touch provisioning
    B. Application aware
    C. Transport agnostic
    D. Central policy management

Answer(s): A. Zero-touch provisioning

Explanation: Zero-touch provisioning (ZTP) is a feature that allows a router or
device to be shipped directly to the installation site, where it automatically
configures itself without requiring manual site-level configuration. The device
will retrieve its configuration from a centralized server or management system
as soon as it connects to the network, simplifying deployment and reducing the
need for on-site IT resources.

Question 199

A network technician is troubleshooting network latency and has determined the
issue to be occurring between two network switches (Switch10 and Switch11).
Symptoms reported include poor video performance and slow file copying. Given
the following information:
![img for question 199](https://free-braindumps.com/images/exam-dumps/N10-009/0dab2f51-cd36-4dae-be59-65aa0bfca215.jpg)
Which of the following should the technician most likely do to resolve the
issue?

    A. Disable automatic negotiation on Switch11.
    B. Modify Switch10 MTU value to 1500.
    C. Configure STP on both switches.
    D. Change the native VLAN on the ports.

Answer(s): B. Modify Switch10 MTU value to 1500.

Explanation: Based on the output from the switches, we can see that Switch10 has
an MTU value of 1600 bytes, while Switch11 has an MTU value of 1500 bytes. A
mismatch in the MTU value between the two switches can cause fragmentation,
which leads to performance issues, such as slow file transfers and poor video
performance. To resolve this issue, the MTU value on Switch10 should be modified
to match the 1500-byte MTU setting on Switch11. Ensuring the MTU values match
across the network will prevent fragmentation and improve performance.

Question 200

Which of the following types of routes will take precedence when building a
routing table for a given subnet?

    A. Static
    B. BGP
    C. OSPF
    D. Default

Answer(s): A. Static

Explanation: When building a routing table, static routes take precedence over
dynamic routing protocols like BGP (Border Gateway Protocol), OSPF (Open
Shortest Path First), and default routes. Static routes are manually configured
by a network administrator and have a higher administrative distance than
dynamic routes, meaning they will be preferred when both static and dynamic
routes exist for the same destination.

Question 201

Which of the following steps in the troubleshooting methodology comes after
using a top-to-bottom examination of the OSI model to determine cause?

    A. Test the theory.
    B. Establish a plan of action.
    C. Verify full system functionality.
    D. Identify the problem.

Answer(s): A. Test the theory.

Explanation: After using a top-to-bottom examination of the OSI model to
determine the cause of a network issue, the next step in the troubleshooting
methodology is to test the theory. This involves validating the hypothesis made
about the problem's cause and verifying if the identified issue is indeed the
root cause.

Question 202

Which of the following would an adversary do while conducting an evil twin
attack?

    A. Trick users into using an AP with an SSID that is identical to a legitimate network.
    B. Manipulate address resolution to point devices to a malicious endpoint.
    C. Present an identical MAC to gain unauthorized access to network resources.
    D. Capture data in transit between two legitimate endpoints to steal data.

Answer(s): A. Trick users into using an AP with an SSID that is identical to a
legitimate network.

Explanation: An evil twin attack involves an adversary setting up a rogue access
point (AP) with the same SSID as a legitimate wireless network. The goal is to
trick users into connecting to the malicious AP, thereby intercepting and
potentially manipulating the data transmitted between the users and the network.
Once connected to the rogue AP, the attacker may capture sensitive data or
launch additional attacks, such as man-in-the-middle attacks.

Question 203

An ISP provided a company with an IP range of 98.174.235.142/28. A network
technician configured a router with a subnet mask of 255.255.255.224 and default
gateway of 98.174.235.129. After the configuration was set up. the company is
unable to connect to the ISP. Which of the following would resolve this issue?

    A. Change the subnet mask to .240.
    B. Change the Ethernet cable from the external interface to the modem.
    C. Change the CIDR to /29.
    D. Change the static IP to 98.174.235.128/28.

Answer(s): D. Change the static IP to 98.174.235.128/28.

Explanation: The IP range provided by the ISP is 98.174.235.142/28, which gives
a subnet with the network address of 98.174.235.128 and a range of IPs from
98.174.235.128 to 98.174.235.143 (usable IPs: 98.174.235.129 to 98.174.235.142).
The router should be configured with an IP address in this range. The issue in
this case is that the static IP address on the router is set to 98.174.235.129,
which is the default gateway in the configuration, but this IP should not be
used as the router's own IP. The router should have an IP address from the valid
range of 98.174.235.128/28 that isn't used for the gateway (which is
98.174.235.129), so the correct IP would be 98.174.235.130 or any other
available address in the range.

Question 204

A network administrator is troubleshooting a connection between two switches
that is experiencing intermittent errors. The administrator needs to determine
which port on the remote switch the faulty cable is connected to. Which of the
following is the best tool to use to identify the error?

    A. tracert
    B. LLDP run
    C. nmap
    D. ping

Answer(s): B. LLDP run

Explanation: LLDP (Link Layer Discovery Protocol) is the best tool for
identifying which port on the remote switch the faulty cable is connected to.
LLDP is a Layer 2 protocol used by network devices to advertise their identity,
capabilities, and neighbors. By using LLDP, a network administrator can discover
information about the devices connected to a switch port, including the port
number on the remote switch.

Question 205

Which of the following is a difference between EOL and EOS?

    A. EOL discontinues the product but may offer support.
    B. EOS replaces free support with a subscription model.
    C. EOS only applies to physical products.
    D. EOL still guarantees warranty service.

Answer(s): A. EOL discontinues the product but may offer support.

Explanation: EOL (End of Life) and EOS (End of Support) are terms used in the
lifecycle of a product, and they represent different stages: EOL (End of Life)
refers to when a product is officially discontinued, meaning the manufacturer
will no longer produce or sell the product. However, it may still offer support
services such as software updates or security patches for a limited time. EOS
(End of Support) refers to when the manufacturer stops offering any support for
the product, including technical support, updates, or bug fixes. This typically
happens after EOL.

Question 206

A network architect is implementing an off-premises computing facility and needs
to ensure that operation will not be impacted by major outages. Which of the
following should the architect consider?

    A. Hot site
    B. DCI
    C. Direct Connect
    D. Active-passive approach

Answer(s): A. Hot site

Explanation: A hot site is an off-premises computing facility that is fully
equipped and can take over operations immediately in the event of a disaster or
major outage. It typically includes all necessary hardware, software, and data
to ensure business continuity without any downtime. This option would ensure
that operations are not impacted by major outages, as the hot site can provide
immediate failover.

Question 207

A network engineer is testing a website to ensure it is compatible with IPv6.
After attempting to ping the website by its IPv6 address, the engineer
determines that the DNS has not been set up properly. Which of the following
should the network engineer complete to resolve this issue?

    A. Enable a PTR record.
    B. Update the existing TXT record.
    C. Add a new AAA record.
    D. Configure a secondary NS record.

Answer(s): C. Add a new AAA record.

Explanation: In IPv6, the AAAA record is used to map a domain name to its
corresponding IPv6 address. If the network engineer is unable to ping the
website by its IPv6 address and determines that the DNS is not set up properly,
it is likely because the AAAA record, which links the domain to the IPv6
address, is missing or incorrectly configured.

Question 208

A small coffee shop wants to set up multiple 2.4GHz wireless access points. The
access points will support a large number of users, and the network technician
wants to mitigate interference as much as possible. Which of the following is
the number of 22MHz channels that the equipment can support?

    A. 1
    B. 2
    C. 3
    D. 4

Answer(s): C. 3

Explanation: In the 2.4GHz frequency band, there are 11 or 13 channels
available, depending on the country. However, these channels overlap
significantly, especially when using standard 20MHz channel widths. To minimize
interference and maximize the number of non-overlapping channels, the 2.4GHz
band can only support 3 non- overlapping channels when using 22MHz channel
width. The non-overlapping channels in the 2.4GHz band are typically: Channel 1
(center frequency at 2412 MHz) Channel 6 (center frequency at 2437 MHz) Channel
11 (center frequency at 2462 MHz) Using these three channels (1, 6, and 11)
allows you to avoid interference between channels. Increasing the number of
channels or overlapping channels would result in interference and poor
performance for wireless clients. Thus, 3 non-overlapping 22MHz channels are
available in the 2.4GHz band.

Question 209

A company is purchasing a 40Gbps broadband connection service from an ISP. Which
of the following should most likely be configured on the 10G switch to take
advantage of the new service?

    A. 802.11Q tagging
    B. Jumbo frames
    C. Half duplex
    D. Link aggregation

Answer(s): D. Link aggregation

Explanation: To take full advantage of a 40Gbps broadband connection, the 10G
switch will need to combine multiple 10Gbps links into a single logical
connection, which can be achieved by link aggregation. Link aggregation allows
multiple physical links to act as a single logical link, increasing bandwidth
and providing redundancy. With a 40Gbps connection, the 10G switch would
aggregate multiple 10Gbps links (e.g., 4x10Gbps) to meet the required speed.

Question 210

Which of the following are the main differences between ESP and AH? (Choose
two.)

    A. AH provides confidentiality through the use of encryption.
    B. ESP provides authentication for IP headers and their payloads.
    C. ESP provides confidentiality through the use of encryption.
    D. AH provides authentication for IP headers and their payloads.
    E. AH provides data origin authorization over shared secret.
    F. ESP provides data origin authorization over shared secret.

Answer(s): C. ESP provides confidentiality through the use of encryption., E. AH
provides data origin authorization over shared secret.

Explanation: ESP provides confidentiality through the use of encryption: ESP
(Encapsulating Security Payload) provides confidentiality by encrypting the
payload (the data being transmitted). It ensures that the data cannot be read by
unauthorized parties. AH provides authentication for IP headers and their
payloads: AH (Authentication Header) provides data integrity and authentication
for the IP headers and the payload. It ensures that the data hasn't been
tampered with, but it does not provide confidentiality (encryption).

Question 211

An organization wants to ensure that incoming emails were sent from a trusted
source. Which of the following DNS records is used to verify the source?

    A. TXT
    B. AAA
    C. CNAME
    D. MX

Answer(s): A. TXT

Explanation: To verify that incoming emails were sent from a trusted source,
organizations typically use TXT records in DNS. Specifically, SPF (Sender Policy
Framework) records are stored as TXT records and are used to specify which mail
servers are allowed to send emails on behalf of the domain. This helps verify
that the source of the email is authorized and trusted.

Question 212

Which of the following is the most closely associated with segmenting compute
resources within a single cloud account?

    A. Network security group
    B. IaaS
    C. VPC
    D. Hybrid cloud

Answer(s): C. VPC

Explanation: A VPC (Virtual Private Cloud) is the most closely associated with
segmenting compute resources within a single cloud account. A VPC allows you to
create isolated network environments within a cloud provider's infrastructure,
enabling you to segment resources, control traffic, and apply network security
rules. You can define subnets, set up routing, and configure security groups to
segment compute resources within that isolated environment.

Question 213

Which of the following is the most likely function to be decremented when a tool
is used to measure the distance between two locations on the internet?

    A. GRE
    B. TTL
    C. VPN
    D. QoS

Answer(s): B. TTL

Explanation: TTL (Time to Live) is the most likely function to be decremented
when a tool is used to measure the distance between two locations on the
internet. TTL is a field in the IP header that is used to limit the lifetime of
a packet to prevent it from circulating indefinitely in case of routing loops.
Each time the packet is forwarded by a router, the TTL value is decremented by
one. When tools like traceroute are used to measure the path and distance
between two locations, they rely on the TTL value to determine how many hops
(routers) the packet takes to reach its destination.

Question 214

A user's home mesh wireless network is experiencing latency issues. A technician
has: Performed a speed test. Rebooted the devices. Performed a site survey.
Performed a wireless packet capture. The technician reviews the following
information:
![img for question 214](https://free-braindumps.com/images/exam-dumps/N10-009/d45836b2-37d1-4e48-a029-fa1dc5b15125.jpg)
The technician notices in the packet capture that frames were retransmitted.
Which of the following is the most likely cause of the user's network issue?

    A. The SSIDs should not be the same.
    B. The network has too much overlap.
    C. The devices are incompatible with the mesh network.
    D. The nodes are underpowered.

Answer(s): B. The network has too much overlap.

Explanation: From the information provided, we can see that the same SSID (Home)
is being used by multiple devices with very close MAC addresses and the same
channel (channel 11). This suggests that multiple wireless access points or
nodes are operating on the same channel, and the signal coverage may overlap
significantly. Reasons for the issue: Overlapping Channels: When multiple access
points or mesh network nodes are using the same channel and are physically close
to each other, they can interfere with one another, leading to packet collisions
and retransmissions. The RSSI values indicate that the devices are fairly close
to each other but still experiencing interference due to channel overlap.
Retransmissions: The issue of frames being retransmitted, as noted in the packet
capture, is a strong indicator of interference, which is often caused by
overlapping networks or devices sharing the same frequency (channel 11).

Question 215

A network engineer implements a 192.168.100.0/25 subnet for a building without
obtaining sizing requirements. It is later determined that the building will
house 700 people. Which of the following subnet masks will most efficiently
support that number of people?

    A. 255.255.252.0
    B. 255.255.254.0
    C. 255.255.255.0
    D. 255.255.255.128

Answer(s): A. 255.255.252.0

Explanation: To determine the most efficient subnet mask for supporting 700
people, we need to ensure that the subnet has enough host addresses. Subnet
Requirements: Each person requires one unique IP address. A subnet needs to have
at least 700 usable IP addresses. The subnet mask determines the number of
usable host addresses in the network. Let's examine each option: 1.
255.255.252.0 (Subnet mask: /22) A /22 subnet provides 1024 IP addresses (2^10).
1024 IP addresses minus 2 for network and broadcast addresses gives 1022 usable
IP addresses, which is sufficient to support 700 people. 2. 255.255.254.0
(Subnet mask: /23) A /23 subnet provides 512 IP addresses (2^9). 512 IP
addresses minus 2 for network and broadcast addresses gives 510 usable IP
addresses, which is not sufficient for 700 people. 3. 255.255.255.0 (Subnet
mask: /24) A /24 subnet provides 256 IP addresses (2^8). 256 IP addresses minus
2 for network and broadcast addresses gives 254 usable IP addresses, which is
far too few for 700 people. 4. 255.255.255.128 (Subnet mask: /25) A /25 subnet
provides 128 IP addresses (2^7). 128 IP addresses minus 2 for network and
broadcast addresses gives 126 usable IP addresses, which is not nearly enough
for 700 people. Therefore, the /22 subnet (255.255.252.0) is the most efficient
choice, providing enough usable IP addresses to accommodate 700 people.

Question 216

A company is building a new campus that will have wired and wireless devices.
The network will be designed to support casual internet usage for guests and
break rooms for employees. Which of the following authentication methods is best
suited for guests given the requirements of this scenario?

    A. ESP
    B. PSK
    C. WPA
    D. IKE

Answer(s): B. PSK

Explanation: For the given scenario, where a company is building a new campus
with a network designed to support casual internet usage for guests and break
rooms for employees, PSK (Pre-Shared Key) is the most suitable authentication
method for guests. PSK (Pre-Shared Key) is commonly used for wireless networks
where the network administrator shares a single, simple password or key with
users. It's ideal for guest networks in a scenario where there is no need for
individual user authentication but rather a simple way for guests to access the
network. WPA (Wi-Fi Protected Access) is a wireless security protocol that PSK
can work under, such as WPA2-PSK. It provides security through encryption but is
easier to set up for guest access by providing a shared password. WPA itself is
a protocol for securing wireless networks, but it does not specifically refer to
the method for authenticating users, which in this case would be PSK.

Question 217

Following the troubleshooting methodology, a technician implements a solution
that resolves the reported issue. Which of the following should the technician
do next?

    A. Document the findings.
    B. Create a plan of action.
    C. Establish a theory.
    D. Identify the problem.

Answer(s): A. Document the findings.

Explanation: After implementing a solution that resolves the reported issue, the
next step in the troubleshooting methodology is to document the findings. This
includes recording the steps taken, the solution implemented, and any relevant
details about the issue and its resolution. Proper documentation ensures that
future troubleshooting efforts can refer to past solutions and help track
recurring problems.

Question 218

A network administrator needs to divide 192.168.1.0/24 into two equal halves.
Which of the following subnet masks should the administrator use?

    A. 255.255.0.0
    B. 255.255.254.0
    C. 255.255.255.0
    D. 255.255.255.128

Answer(s): D. 255.255.255.128

Explanation: To divide the 192.168.1.0/24 network into two equal halves, the
network administrator needs to borrow 1 bit from the host portion of the IP
address, which is 8 bits for a /24 subnet. This will create two subnets with 128
usable IP addresses each. 255.255.255.128 subnet mask corresponds to a /25
subnet, which splits the 192.168.1.0/24 network into two equal subnets, each
with 128 IP addresses (126 usable addresses). This is the correct choice for
dividing the network into two equal halves.

Question 219

Which of the following protocols uses the Dijkstra's Link State Algorithm to
establish routes inside its routing table?

    A. OSPF
    B. EIGRP
    C. BGP
    D. RIP

Answer(s): A. OSPF

Explanation: OSPF (Open Shortest Path First) uses Dijkstra's Link State
Algorithm to calculate the shortest path first (SPF) to each network in its
routing table. OSPF is a link-state routing protocol, meaning that it maintains
a database of the entire network topology and uses the Dijkstra algorithm to
compute the best path.

Question 220

Which of the following traffic types does a DHCP Discover request from a PC use?

    A. Broadcast
    B. Anycast
    C. Unicast
    D. Multicast

Answer(s): A. Broadcast

Explanation: When a PC sends a DHCP Discover request, it uses a broadcast. This
is because the PC does not yet have an IP address and therefore cannot send the
request to a specific destination IP address. Instead, it broadcasts the DHCP
Discover packet to all devices on the local network (to the broadcast address
255.255.255.255) to locate a DHCP server.

Question 221

A user's VoIP phone and workstation are connected through an inline cable. The
user reports that the VoIP phone intermittently reboots, but the workstation is
not having any network-related issues. Which of the following is the most likely
cause?

    A. The PoE power budget is exceeded.
    B. Port security is violated.
    C. The signal is degraded.
    D. The Ethernet cable is not working.

Answer(s): A. The PoE power budget is exceeded.

Explanation: The most likely cause of the VoIP phone intermittently rebooting
while the workstation does not have any network-related issues is that the PoE
(Power over Ethernet) power budget is exceeded. PoE provides both power and data
over the same Ethernet cable to devices such as VoIP phones. If the power budget
on the switch port that is supplying PoE is exceeded, the VoIP phone might not
get enough power to function properly, leading to intermittent reboots.

Question 222

A network administrator is installing a network for a small company. The
switches will be installed in parallel to provide redundancy in case a specific
device fails. Which of the following should be configured to prevent loops?

    A. Spanning tree
    B. CRC
    C. Jumbo frames
    D. Link aggregation

Answer(s): A. Spanning tree

Explanation: To prevent loops in a network with multiple switches providing
redundancy, Spanning Tree Protocol (STP) should be configured. STP is a network
protocol used to detect and prevent loops in Ethernet networks. When there are
redundant paths between switches, STP ensures that only one active path exists
at any given time and blocks the other redundant paths to avoid broadcast storms
and network loops.

Question 223

A company's network is experiencing high latency and packet loss during peak
hours. Network monitoring tools show increased traffic on a switch. Which of the
following should a network technician implement to reduce the network congestion
and improve performance?

    A. Load balancing
    B. Port mirroring
    C. Quality of service
    D. Spanning Tree Protocol

Answer(s): A. Load balancing

Explanation: To reduce network congestion and improve performance, especially
when high latency and packet loss occur during peak hours, load balancing should
be implemented. Load balancing helps distribute the traffic more evenly across
the network, preventing any single device or link from becoming overloaded. This
ensures more efficient use of the available bandwidth and reduces congestion.

Question 224

Which of the following VPN types provides secure remote access to the network
resources through a web portal?

    A. Proxy
    B. Clientless
    C. Site-to-site
    D. Direct connect

Answer(s): B. Clientless

Explanation: A clientless VPN provides secure remote access to network resources
via a web portal without requiring the user to install a dedicated VPN client on
their device. This type of VPN allows users to access resources by simply using
a standard web browser. The web portal handles the authentication and secure
access to the internal network.

Question 225

Which of the following best explains the role of confidentiality with regard to
data at rest?

    A. Data can be accessed by anyone on the administrative network.
    B. Data can be accessed remotely with proper training.
    C. Data can be accessed after privileged access is granted.
    D. Data can be accessed after verifying the hash.

Answer(s): C. Data can be accessed after privileged access is granted.

Explanation: Confidentiality with regard to data at rest refers to ensuring that
sensitive information stored on a device or network is protected from
unauthorized access. This means that data can only be accessed by individuals
who have been granted the appropriate privileges or permissions. Access control
mechanisms such as encryption, password protection, and authentication are
typically used to maintain the confidentiality of data at rest.

Question 226

Several users in an organization report connectivity issues and lag during a
video meeting. The network administrator performs a tcpdump and observes
increased retransmissions for other non-video applications on the network. Which
of the following symptoms describes the users' reported issues?

    A. Latency
    B. Packet loss
    C. Bottlenecking
    D. Jitter

Answer(s): B. Packet loss

Explanation: In the scenario described, the increased retransmissions observed
for non-video applications suggest that there is packet loss on the network.
When packets are lost during transmission, they must be retransmitted, which
leads to increased latency, delays, and issues like connectivity and lag. This
is especially noticeable in time-sensitive applications like video meetings,
where dropped packets can cause significant disruptions.

Question 227

An administrator enables DNS filtering on the firewall to block users from
visiting malicious websites. Which of the following should the administrator
also do? (Choose two.)

    A. Disable DoH in users' internet browsers.
    B. Update NS record to point to DNS filter servers.
    C. Block port 443 to the malicious websites.
    D. Block port 53 to servers on the internet.
    E. Disable TLS v1.3 in users' internet browsers.
    F. Implement DNSSEC for corporate records.

Answer(s): A. Disable DoH in users' internet browsers., D. Block port 53 to
servers on the internet.

Explanation: Disable DoH in users' internet browsers: DNS over HTTPS (DoH)
encrypts DNS queries, which can bypass DNS filtering. By disabling DoH in the
users' internet browsers, the administrator ensures that DNS queries are sent to
the designated DNS filter server, where they can be inspected and potentially
blocked for malicious sites. Implement DNSSEC for corporate records: DNS
Security Extensions (DNSSEC) adds security to the DNS protocol by ensuring the
integrity and authenticity of DNS data. By implementing DNSSEC for corporate
records, the administrator ensures that the DNS responses are not tampered with,
preventing DNS spoofing attacks which could allow malicious sites to bypass the
DNS filtering.

Question 228

Which of the following is concerned with guaranteed availably of a cloud
resource?

    A. IPAM
    B. SLA
    C. MTBF
    D. EOL

Answer(s): B. SLA

Explanation: SLA (Service Level Agreement): An SLA is a formal agreement between
a cloud service provider and the customer that specifies the level of service
the provider will deliver. It typically includes details about the guaranteed
availability (uptime), response times, and other service metrics. The SLA
guarantees the availability of cloud resources by setting expectations on
service uptime and what compensations or actions will be taken if the service
level is not met.

Question 229

A network consultant needs to decide between running an Ethernet uplink or using
the built-in 5GHz point-to- point functionality on a WAP. Which of the following
documents provides the best information to assist the consultant with this
decision?

    A. Site survey results
    B. Physical diagram
    C. Service-level agreement
    D. Logical diagram

Answer(s): A. Site survey results

Explanation: Site survey results: A site survey provides critical information
about the physical environment where the network will be deployed, including
signal strength, interference, and the best possible locations for access points
(WAPs). This information is essential for making decisions about network design,
including whether to use an Ethernet uplink or the 5GHz point-to-point
functionality. The site survey results will highlight factors such as coverage
areas, potential obstacles, and interference, which will inform the choice
between these two options.

Question 230

While troubleshooting connectivity issues, a junior network administrator is
given explicit instructions to test the host's TCP/IP stack first. Which of the
following commands should the network administrator run?

    A. ping 127.0.0.1
    B. ping 169.254.1.1
    C. ping 172.16.1.1
    D. ping 192.168.1.1

Answer(s): A. ping 127.0.0.1

Explanation: ping 127.0.0.1: This command tests the local host's TCP/IP stack by
sending a ping to the loopback address (127.0.0.1). The loopback address is used
to test if the host's networking software and TCP/IP stack are functioning
properly without relying on any physical network connections. If this ping is
successful, it confirms that the host's TCP/IP stack is working correctly.

Question 231

Users at an organization report that the wireless network is not working in some
areas of the building. Users report that other wireless network SSIDs are
visible when searching for the network, but the organization's network is not
displayed. Which of the following is the most likely cause?

    A. Interference or channel overlap
    B. Insufficient wireless coverage
    C. Roaming misconfiguration
    D. Client disassociation issues

Answer(s): B. Insufficient wireless coverage

Explanation: Insufficient wireless coverage: If the organization's wireless
network is not visible in some areas of the building, the most likely cause is
insufficient wireless coverage in those areas. This could be due to the distance
from the wireless access points (WAPs), obstacles like walls or furniture, or
the placement of the WAPs. In areas with poor coverage, the signal may not be
strong enough for the SSID to be detected by devices, even though other SSIDs
are visible.

Question 232

Which of the following panels would be best to facilitate a central termination
point for all network cables on the floor of a company building?

    A. Patch
    B. UPS
    C. MDF
    D. Rack

Answer(s): C. MDF

Explanation: MDF (Main Distribution Frame): The MDF is the best choice for a
central termination point for all network cables in a building. It serves as the
primary hub for connecting network cables, both from within the building and
from external sources. The MDF is typically located in a centralized area where
all the cables from various parts of the building are brought together and then
routed to other areas like the IDF (Intermediate Distribution Frame) or directly
to network equipment. It is the main point for managing and distributing network
connections.

Question 233

Which of the following is most commonly associated with many systems sharing one
IP address in the public IP-addressing space?

    A. PAT
    B. NAT
    C. VIP
    D. NAT64

Answer(s): A. PAT

Explanation: PAT (Port Address Translation): PAT is a type of NAT (Network
Address Translation) where multiple devices within a private network share a
single public IP address. This is done by assigning different port numbers to
each connection, allowing the devices to appear as a single entity to the
outside world while still being able to maintain unique communication sessions.
PAT is commonly used in home networks and organizations to allow multiple
devices to access the internet using one public IP address.

Question 234

A network administrator is reviewing a production web server and observes the
following output from the netstat command:
![img for question 234](https://free-braindumps.com/images/exam-dumps/N10-009/f4a8eb17-4d04-4c4c-b472-849f3aa5cc51.jpg)
Which of the following actions should the network administrator take to harden
the security of the web server?

    A. Disable the unused ports.
    B. Enforce access control lists.
    C. Perform content filtering.
    D. Set up a screened subnet.

Answer(s): A. Disable the unused ports.

Explanation: The netstat output shows multiple ports in the LISTENING state,
indicating that services are actively accepting connections. While ports 80
(HTTP) and 443 (HTTPS) are expected for a web server, other open ports such as
20 (FTP Data), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), and 69 (TFTP) might
not be necessary for web server functionality. To harden security, the network
administrator should disable or close the unused ports to reduce the attack
surface. Unused ports provide potential entry points for attackers if not
properly secured. This can be done through: Stopping unnecessary services
Configuring firewall rules to block unwanted traffic Using server hardening
techniques

Question 235

A network technician is examining the configuration on an access port and
notices more than one VLAN has been set. Which of the following best describes
how the port is configured?

    A. With a voice VLAN
    B. With too many VLAN
    C. With a default VLAN
    D. With a native VLAN

Answer(s): A. With a voice VLAN

Explanation: An access port is typically associated with a single VLAN, but it
is possible to configure it with more than one VLAN if a voice VLAN is also set.
A voice VLAN is commonly used to separate voice traffic (e.g., from IP phones)
from data traffic on the same port, ensuring that voice traffic receives the
appropriate priority and QoS (Quality of Service). This configuration allows
both voice and data to be carried over the same physical connection but into
separate logical VLANs.

Question 236

A small company has the following IP addressing strategy: User subnet:
192.168.1.0/24 Voice subnet: 192.168.2.0/24 Server subnet: 192 168.10.0/24 A
user is unable to connect to the company fileshare server located at
192.168.10.1. The user's networking configuration is:
![img for question 236](https://free-braindumps.com/images/exam-dumps/N10-009/5c9d90e7-c763-4ade-b73d-797f176a70d8.jpg)
Which of the following will most likely correct the issue?

    A. Changing the IPv4 address to 192.168.10.1
    B. Changing the subnet mask to 255.255.255.0
    C. Changing the DNS servers to internet IPs
    D. Changing the physical address to 7A-01-7A-21-01-50

Answer(s): B. Changing the subnet mask to 255.255.255.0

Explanation: The user's current subnet mask is 255.255.0.0, which means they are
part of a /16 subnet (192.168.0.0/16). However, the company's subnetting
strategy assigns the user subnet as 192.168.1.0/24 and the server subnet as
192.168.10.0/24. With 255.255.0.0, the user's device assumes it is in the same
subnet as 192.168.10.1, so it does not send traffic to the default gateway
(192.168.1.200) for routing. The actual network segmentation follows /24
subnetting, meaning that 192.168.1.50 (user) and 192.168.10.1 (server) are in
different subnets and must communicate through a router. Changing the subnet
mask to 255.255.255.0 (/24) correctly aligns the user's device with the
company's subnetting scheme, ensuring that traffic is properly routed through
the gateway.

Question 237

A network administrator needs to connect a department to a new network segment.
They need to use a DHCP server located on another network. Which of the
following can the administrator use to complete this task?

    A. IP Helper
    B. Reservation
    C. Exclusion
    D. Scope

Answer(s): A. IP Helper

Explanation: IP Helper An IP Helper (or DHCP relay agent) is used to forward
DHCP requests from clients in one subnet to a DHCP server in another subnet.
Since DHCP is a broadcast-based service, routers typically do not forward DHCP
requests across different subnets. By configuring an IP Helper address on the
router or Layer 3 switch, the DHCP broadcast is converted into a unicast message
and sent to the DHCP server on another network. This ensures that clients in the
new network segment can obtain IP addresses from the remote DHCP server.

Question 238

A network engineer is implementing a solution by which on-premises servers are
migrated to a cloud service provider. Which of the following service models will
provide a lift and shift solution to meet this requirement?

    A. Infrastructure as a service
    B. Infrastructure as code
    C. Software as a service
    D. Software-defined network

Answer(s): A. Infrastructure as a service

Explanation: Infrastructure as a Service (IaaS) provides virtualized computing
resources over the internet, allowing organizations to "lift and shift" their
on-premises servers to the cloud without significant changes. In a
lift-and-shift migration, existing applications and workloads are moved to
cloud-based virtual machines with minimal modifications. IaaS providers (such as
AWS, Azure, or Google Cloud) offer compute, storage, and networking resources,
enabling organizations to run their servers and applications in the cloud
similarly to how they operate on- premises.

Question 239

A network administrator is conducting an assessment and found network devices
that do not meet standards. Which of the following configurations is considered
a set of rules that devices should adhere to?

    A. Production
    B. Backup
    C. Candidate
    D. Golden

Answer(s): D. Golden

Explanation: Golden A golden configuration is a standardized and approved set of
configurations that network devices should adhere to in order to meet
organizational policies and security standards. This serves as a baseline for
maintaining network security, performance, and compliance. If a device does not
meet the golden configuration, it may need to be updated or reconfigured to
align with best practices.

Question 240

An IT department asks a newly hired employee to use a personal laptop until the
company can provide one. Which of the following policies is most applicable to
this situation?

    A. IAM
    B. BYOD
    C. DLP
    D. AUP

Answer(s): B. BYOD

Explanation: BYOD (Bring Your Own Device) refers to policies that allow
employees to use their personal devices (such as laptops, smartphones, and
tablets) for work-related tasks. Since the IT department is asking the employee
to temporarily use a personal laptop, the BYOD policy would outline security
measures, acceptable use, network access restrictions, and data protection
requirements to ensure company security while using a personal device.

Question 241

Which of the following offers the ability to manage access at the cloud VM
instance?

    A. Security group
    B. Internet gateway
    C. Direct Connect
    D. Network ACL

Answer(s): A. Security group

Explanation: Security group is a cloud-based firewall that controls inbound and
outbound traffic at the instance level (e.g., AWS EC2 instances, Azure VMs).
Security groups define allow/deny rules based on IP addresses, protocols, and
ports to manage access to a cloud-based virtual machine (VM).

Question 242

In an environment with one router, which of the following will allow a network
engineer to communicate between VLANs without purchasing additional hardware?

    A. Subinterfaces
    B. VXLAN
    C. Layer 3 switch
    D. VIP

Answer(s): A. Subinterfaces

Explanation: A subinterface allows inter-VLAN communication on a single router
using the Router-on-a-Stick method. This approach configures multiple logical
(sub)interfaces on a single physical interface of the router, each assigned to a
different VLAN. The router handles VLAN tagging (802.1Q) and routes traffic
between VLANs, enabling communication without additional hardware.

Question 243

A network administrator is concerned with on-path attacks and wants to provide
encryption of fully qualified domain names in outbound communications. Which of
the following best describes the protocol that provides the proper security
layer for internet communication?

    A. SSL
    B. DoH
    C. TLS
    D. DNSSEC

Answer(s): B. DoH

Explanation: DoH (DNS over HTTPS) encrypts fully qualified domain name (FQDN)
queries by encapsulating them within HTTPS traffic. This prevents on-path
attacks (such as Man-in-the-Middle attacks) from intercepting or tampering with
DNS queries. DoH enhances privacy and security by ensuring that DNS requests are
encrypted, making it harder for attackers to manipulate or eavesdrop on domain
name resolutions.

Question 244

A network administrator wants to restrict inbound traffic to allow only HTTPS to
the company website, denying all other inbound traffic from the internet. Which
of the following would best accomplish this goal?

    A. ACL on the edge firewall
    B. Port security on an access switch
    C. Content filtering on a web gateway
    D. URL filtering on an outbound proxy

Answer(s): A. ACL on the edge firewall

Explanation: An Access Control List (ACL) on the edge firewall is the best way
to restrict inbound traffic and allow only HTTPS (port 443) to the company
website while blocking all other inbound traffic from the internet. Firewalls
use ACLs to filter network traffic based on IP addresses, protocols, and ports,
ensuring that only authorized traffic is permitted.

Question 245

A network engineer is deploying switches at a new remote office. The switches
have been preconfigured with hostnames and STP priority values. Based on the
following table:
![img for question 245](https://free-braindumps.com/images/exam-dumps/N10-009/2e392472-a4a6-4892-bc0c-c9a4f60ffa7c.jpg)
Which of the following switches will become the root bridge?

    A. core-sw01
    B. access-sw01
    C. distribution-sw01
    D. access-sw02

Answer(s): B. access-sw01

Explanation: The root bridge in STP is determined first by the lowest priority
value. In this case, both core-sw01 and access- sw01 have a priority of 4096,
which is lower than the other switches (32768). When there is a tie in priority,
the switch with the lower MAC address is selected as the root bridge. Comparing
the MAC addresses: core-sw01: 0000.0000.005f access-sw01: 0000.0000.005e Since
0000.0000.005e is lower than 0000.0000.005f, access-sw01 will become the root
bridge.

Question 246

Which of following must be implemented to securely connect a company's
headquarters with a branch location?

    A. Split-tunnel VPN
    B. Clientless VPN
    C. Full-tunnel VPN
    D. Site-to-site VPN

Answer(s): D. Site-to-site VPN

Explanation: A site-to-site VPN is the best solution for securely connecting a
company's headquarters with a branch location. This type of VPN establishes a
permanent, encrypted tunnel between two networks, allowing seamless and secure
communication between them. It is typically configured on firewalls or routers
at each site, ensuring data security over the internet.

Question 247

A network engineer needs to virtualize network services, including a router, at
a remote branch location. Which of the following solutions meets the
requirements?

    A. NFV
    B. VRF
    C. VLAN
    D. VPC

Answer(s): A. NFV

Explanation: NFV (Network Functions Virtualization) allows network services,
such as routers, firewalls, and load balancers, to be virtualized and run on
standard hardware instead of dedicated network appliances. This meets the
requirement of virtualizing network services, including a router, at a remote
branch location. NFV enables flexibility, cost savings, and scalability by
replacing physical network devices with software-based solutions running on
virtual machines or cloud environments.

Question 248

A group of users cannot connect to network resources. The technician runs
ipconfig from one user's device and is able to ping the gateway shown from the
command. Which of the following is most likely preventing the users from
accessing network resources?

    A. VLAN hopping
    B. Rogue DHCP
    C. Distributed DoS
    D. Evil twin

Answer(s): B. Rogue DHCP

Explanation: If users cannot connect to network resources but can ping the
gateway, this suggests they have an IP address assigned but might have incorrect
network settings, such as a wrong DNS server or incorrect subnet information.
This issue often occurs when a rogue DHCP server (an unauthorized DHCP server on
the network) assigns incorrect or malicious IP configurations, preventing users
from accessing network resources correctly.

Question 249

Which of the following disaster recovery concepts is calculated by dividing the
total hours of operation by the total number of units?

    A. MTTR
    B. MTBF
    C. RPO
    D. RTO

Answer(s): B. MTBF

Explanation: MTBF (Mean Time Between Failures) is calculated by dividing the
total hours of operation by the total number of failures in a system. It is a
key disaster recovery and reliability metric used to measure the average time a
system operates before experiencing a failure. Formula: MTBF = total hours of
operation / total number of failures

Question 250

A network administrator has been monitoring the company's servers to ensure that
they are available. Which of the following should the administrator use for this
task?

    A. Packet capture
    B. Data usage reports
    C. SNMP traps
    D. Configuration monitoring

Answer(s): C. SNMP traps

Explanation: SNMP (Simple Network Management Protocol) traps allow a network
administrator to monitor server availability by receiving real-time alerts when
a server goes down or experiences issues. Traps are asynchronous notifications
sent by network devices to an SNMP management system when predefined events
occur, such as high CPU usage, link failures, or server unavailability.

Question 251

A network engineer is completing a wireless installation in a new building. A
requirement is that all clients be able to automatically connect to the fastest
supported network. Which of the following best supports this requirement?

    A. Enabling band steering
    B. Disabling the 5GHz SSID
    C. Adding a captive portal
    D. Configuring MAC filtering

Answer(s): A. Enabling band steering

Explanation: Band steering helps clients automatically connect to the fastest
supported network by encouraging devices to use the 5GHz band instead of the
2.4GHz band when they support both. The 5GHz band offers higher speeds and less
interference compared to 2.4GHz. Band steering detects dual-band capable devices
and directs them to 5GHz, ensuring optimal performance.

Question 252

A network technician notices a device is at EOL. For which of the following
should the technician plan?

    A. Retrofitting
    B. Decommissioning
    C. Restarting
    D. Upgrading

Answer(s): B. Decommissioning

Explanation: When a device reaches EOL (End of Life), it means the manufacturer
no longer provides support, updates, or security patches for it. The proper
action is to decommission the device, which involves removing it from
production, securely erasing data, and disposing of or recycling it properly.

Question 253

A company implements a video streaming solution that will play on all computers
that have joined a particular group, but router ACLs are blocking the traffic.
Which of the following is the most appropriate IP address that will be allowed
in the ACL?

    A. 127.0.0.1
    B. 172.17.1.1
    C. 224.0.0.1
    D. 240.0.0.1

Answer(s): C. 224.0.0.1

Explanation: The 224.0.0.1 IP address belongs to the multicast address range
(224.0.0.0 - 239.255.255.255), specifically the all-hosts multicast group. This
means that any device on the network subscribed to the multicast group will
receive the video stream. Multicast is commonly used for streaming video and
other content to multiple devices efficiently without sending multiple unicast
copies.

Question 254

Which of the following are the best device-hardening techniques for network
security? (Choose two.)

    A. Disabling unused ports
    B. Performing regular scanning of unauthorized devices
    C. Monitoring system logs for irregularities
    D. Enabling logical security such as SSO
    E. Changing default passwords
    F. Ensuring least privilege concepts are in place

Answer(s): A. Disabling unused ports, D. Enabling logical security such as SSO

Explanation: Device hardening is the process of securing network devices to
reduce vulnerabilities and minimize attack surfaces. The two best techniques for
network security are: Disabling unused ports Prevents unauthorized access by
closing physical and logical network ports that are not in use, reducing the
risk of exploitation. Changing default passwords Default passwords are
well-known to attackers. Changing them to strong, unique passwords is essential
to prevent unauthorized access.

Question 255

Which of the following allows for the interception of traffic between the source
and destination?

    A. Self-signed certificate
    B. VLAN hopping
    C. On-path attack
    D. Phishing

Answer(s): C. On-path attack

Explanation: An on-path attack (formerly known as Man-in-the-Middle (MitM)
attack) occurs when an attacker intercepts and potentially alters communication
between a source and destination without their knowledge. This allows attackers
to eavesdrop, capture sensitive data, inject malicious content, or manipulate
communication.

Question 256

A company discovers on video surveillance recordings that an unauthorized person
installed a rogue access point in its secure facility. Which of the following
allowed the unauthorized person to do this?

    A. Evil twin
    B. Honeytrap
    C. Wardriving
    D. Tailgating

Answer(s): D. Tailgating

Explanation: Tailgating occurs when an unauthorized person gains physical access
to a secure area by following an authorized individual without proper
authentication. This social engineering attack allows attackers to enter
restricted areas where they can install rogue access points or other malicious
devices without being detected.

Question 257

A secure communication link needs to be configured between data centers via the
internet. The data centers are located in different regions. Which of the
following is the best protocol for the network administrator to use?

    A. DCI
    B. GRE
    C. VXLAN
    D. IPSec

Answer(s): D. IPSec

Explanation: IPSec (Internet Protocol Security) is the best protocol for
securing communication between data centers over the internet. It provides
encryption, integrity, and authentication for data-in-transit, ensuring that
sensitive information is protected from interception and tampering. IPSec is
commonly used in VPNs (Virtual Private Networks) and site-to-site VPNs for
secure, encrypted connections between remote locations.

Question 258

Which of the following can be implemented to add an additional layer of security
between a corporate network and network management interfaces?

    A. Jump box
    B. Console server
    C. API interface
    D. In-band management

Answer(s): A. Jump box

Explanation: A jump box (jump server) is a hardened, controlled-access device
that acts as an intermediary between a corporate network and network management
interfaces. It provides an additional layer of security by requiring
administrators to log in to the jump box first before accessing critical
infrastructure devices, such as routers, switches, or servers. This helps
isolate and protect management interfaces from direct exposure to the corporate
network, reducing the risk of unauthorized access and attacks.

Question 259

A network administrator performed upgrades on a server and installed a new NIC
to improve performance. Following the upgrades, users are unable to reach the
server. Which of the following is the most likely reason?

    A. The PoE power budget was exceeded.
    B. TX/RX was transposed.
    C. A port security violation occurred.
    D. An incorrect cable type was installed.

Answer(s): C. A port security violation occurred.

Explanation: Many network switches enforce port security, which restricts access
to specific MAC addresses on a given port. When the network administrator
installed a new NIC, the MAC address changed, potentially triggering a port
security violation. As a result, the switch may have disabled the port,
preventing users from accessing the server. To resolve this, the administrator
should: Check the switch logs for security violations. Clear the port security
settings or update the allowed MAC address list. Ensure the switch port is not
in an error-disabled state.

Question 260

A junior network technician at a large company needs to create networks from a
Class C address with 14 hosts per subnet. Which of the following numbers of host
bits is required?

    A. One
    B. Two
    C. Three
    D. Four

Answer(s): D. Four

Explanation: To determine the number of host bits required for a subnet that
supports 14 hosts, we use the host formula: 2h ­ 2 = Number of usable hosts where
h is the number of host bits, and we subtract 2 (one for the network address and
one for the broadcast address). Let's check for 14 hosts: 24 - 2 = 16 - 2 = 14
This satisfies the requirement.

Question 261

Which of the following is a company most likely enacting if an accountant for
the company can only see the financial department's shared folders?

    A. General Data Protection Regulation
    B. Least privilege network access
    C. Acceptable use policy
    D. End user license agreement

Answer(s): B. Least privilege network access

Explanation: Least privilege network access is a security principle that ensures
users only have access to the data and resources necessary for their job role.
In this case, the accountant is restricted to the financial department's shared
folders, meaning access controls are in place to enforce the principle of least
privilege, limiting exposure to sensitive or unnecessary data.

Question 262

Which of the following connector types would most likely be used to connect to
an external antenna?

    A. BNC
    B. ST
    C. LC
    D. MPO

Answer(s): A. BNC

Explanation: A BNC (Bayonet Neill-Concelman) connector is commonly used for
coaxial cables, which are frequently used in RF (radio frequency) applications
such as external antennas, CCTV systems, and radio communications. BNC
connectors provide a secure, quick-connect/disconnect mechanism, making them
ideal for wireless networking and antenna connections.

Question 263

A company recently converted most of the office laptops to connect wirelessly to
the corporate network. After a recent high-traffic malware attack, narrowing the
event to a specific user was difficult because of the wireless configuration.
Which of the following actions should the company take?

    A. Restrict users to the 5GHz frequency.
    B. Upgrade to a mesh network.
    C. Migrate from PSK to Enterprise.
    D. Implement WPA2 encryption.

Answer(s): C. Migrate from PSK to Enterprise.

Explanation: Migrating from PSK (Pre-Shared Key) to Enterprise mode (also known
as WPA2/WPA3-Enterprise) will allow the company to authenticate users
individually using unique credentials via 802.1X authentication and a RADIUS
server. This approach enables better tracking of user activity and enhances
security by associating each device with a specific user, making it easier to
trace potential security incidents like high- traffic malware attacks.

Question 264

Which of the following cloud service models most likely requires the greatest
up-front expense by the customer when migrating a data center to the cloud?

    A. Infrastructure as a service
    B. Software as a service
    C. Platform as a service
    D. Network as a service

Answer(s): A. Infrastructure as a service

Explanation: Infrastructure as a Service (IaaS) requires the greatest up-front
expense when migrating a data center to the cloud because the customer is
responsible for purchasing and managing virtualized computing resources such as
virtual machines (VMs), storage, networking, and security configurations. The
company must design, configure, and migrate applications, data, and services
from the on-premises data center to the cloud.

Question 265

After providing a username and password, a user must input a passcode from a
phone application. Which of the following authentication technologies is used in
this example?

    A. SSO
    B. LDAP
    C. MFA
    D. SAML

Answer(s): C. MFA

Explanation: Multi-Factor Authentication (MFA) requires users to provide two or
more authentication factors to verify their identity. In this case, the user
enters: 1. Username and password (Something they know) 2. Passcode from a phone
application (Something they have) This combination ensures stronger security by
requiring an additional authentication factor beyond just a password. 52 53 54
55 56

Question 266

Which of the following facilities is the best example of a warm site in the
event of information system disruption?

    A. A combination of public and private loud services to restore data
    B. A partial infrastructure, software, and data on site
    C. A full electrical infrastructure in place, but no customer devices on site
    D. A full infrastructure in place, but no current data on site

Answer(s): B. A partial infrastructure, software, and data on site

Explanation: A warm site is a backup facility that has some infrastructure,
pre-installed software, and partial data replication, but it still requires some
configuration and updates before becoming fully operational after a disaster.
This balances cost and recovery speed, making it more prepared than a cold site
but not as fully operational as a hot site.

Question 267

Which of the following services runs on port 636?

    A. SMTP
    B. Syslog
    C. TFTP
    D. LDAPS

Answer(s): D. LDAPS

Explanation: LDAPS (Lightweight Directory Access Protocol Secure) is the secure,
encrypted version of LDAP that runs over port 636 using SSL/TLS encryption to
protect directory authentication and queries. It is commonly used for secure
user authentication and directory access in Active Directory and other directory
services.

Question 268

A company wants to implement data loss prevention by restricting user access to
social media platforms and personal cloud storage on workstations. Which of the
following types of filtering should the company deploy to achieve these goals?

    A. Port
    B. DNS
    C. MAC
    D. Content

Answer(s): D. Content

Explanation: Content filtering is used to restrict access to specific types of
websites, applications, or online services, such as social media platforms and
personal cloud storage. This is commonly done through firewalls, web proxies, or
security appliances that analyze and block content based on predefined rules.
Content filtering helps enforce data loss prevention (DLP) policies by
preventing users from uploading or sharing sensitive data on unauthorized
platforms.

Question 269

An organization is struggling to get effective coverage using the wireless
network. The organization wants to implement a solution that will allow for
continuous connectivity anywhere in the facility. Which of the following should
the network administrator suggest to ensure the best coverage?

    A. Implementing additional ad hoc access points
    B. Providing more Ethernet drops for user connections
    C. Deploying a mesh network in the building
    D. Changing the current frequency of the Wi-Fi

Answer(s): C. Deploying a mesh network in the building

Explanation: A mesh network is the best solution for ensuring continuous Wi-Fi
coverage throughout a facility. Mesh networking uses multiple interconnected
access points (nodes) to extend coverage, improve reliability, and allow devices
to seamlessly roam between access points without disconnection. This solution is
ideal for large buildings where a single router or traditional access point
deployment does not provide full coverage.

Question 270

Which of the following protocols allows automatic routing failover for an
active-passive firewall pair?

    A. EIGRP
    B. OSPF
    C. VRRP
    D. BGP

Answer(s): C. VRRP

Explanation: VRRP (Virtual Router Redundancy Protocol) enables automatic routing
failover for an active-passive firewall pair by allowing multiple routers (or
firewalls) to share a virtual IP address. The active firewall handles traffic
while the passive firewall remains on standby. If the active firewall fails,
VRRP automatically fails over to the passive firewall, ensuring continuous
network availability.

Question 271

Which of the following is a major difference between an IPS and IDS?

    A. An IPS needs to be installed in line with traffic and an IDS does not.
    B. An IPS is signature-based and an IDS is not.
    C. An IPS is less susceptible to false positives than an IDS.
    D. An IPS requires less administrative overhead than an IDS.

Answer(s): A. An IPS needs to be installed in line with traffic and an IDS does
not.

Explanation: The major difference between Intrusion Prevention Systems (IPS) and
Intrusion Detection Systems (IDS) is how they operate within the network: IPS
(Intrusion Prevention System) is installed in-line with network traffic, meaning
it can actively block threats in real time before they reach their target. IDS
(Intrusion Detection System) is not in-line, meaning it monitors and alerts on
suspicious activity but does not actively block threats. Instead, it relies on
administrators or other security systems to take action.

Question 272

Which of the following describes the best reason for using BGP?

    A. Preventing a loop within a LAN
    B. Improving reconvergence times
    C. Exchanging router updates with a different ISP
    D. Sharing routes with a Layer 3 switch

Answer(s): C. Exchanging router updates with a different ISP

Explanation: BGP (Border Gateway Protocol) is primarily used for routing between
different autonomous systems (ASes), such as when an organization connects to
multiple ISPs or exchanges routing information across different networks. It is
the protocol of the internet, ensuring that networks can communicate globally by
exchanging routing updates between ISPs and large-scale enterprises.

Question 273

Which of the following steps of the troubleshooting methodology comes after
testing the theory to determine cause?

    A. Verity full system functionality.
    B. Document the findings and outcomes.
    C. Establish a plan of action.
    D. Identify the problem.

Answer(s): C. Establish a plan of action.

Explanation: The CompTIA troubleshooting methodology follows a structured
approach. After testing the theory to determine the cause, the next step is to
"Establish a plan of action" to resolve the issue and implement the solution.
This step ensures that the fix is planned properly and minimizes any potential
impact on the system. CompTIA Troubleshooting Methodology: 1. Identify the
problem (gather information, ask questions, and observe symptoms). 2. Establish
a theory of probable cause (analyze the issue and make an educated guess). 3.
Test the theory to determine the cause (confirm if the theory is correct). 4.
Establish a plan of action and implement the solution (Correct Answer). 5.
Verify full system functionality and implement preventive measures. 6. Document
findings, actions, and outcomes for future reference.

Question 274

A network administrator installed a new VLAN to the network after a company
added an additional floor to the office. Users are unable to obtain an IP
address on the new VLAN, but ports on existing VLANs are working properly. Which
of the following configurations should the administrator update?

    A. Scope size
    B. Address reservations
    C. Lease time
    D. IP helper

Answer(s): D. IP helper

Explanation: If users on the new VLAN are unable to obtain an IP address, it is
likely that their DHCP requests are not reaching the DHCP server. This typically
happens when the DHCP server is on a different VLAN and there is no IP Helper
address configured on the Layer 3 device (router or Layer 3 switch). An IP
Helper address (also known as a DHCP relay agent) is configured on the router to
forward DHCP requests from clients on different VLANs to the central DHCP
server, allowing them to receive an IP address.

Question 275

A network engineer needs to add a boundary network to isolate and separate the
internal network from the public-facing internet. Which of the following
security defense solutions would best accomplish this task?

    A. Trusted zones
    B. URL filtering
    C. ACLs
    D. Screened subnet

Answer(s): D. Screened subnet

Explanation: A screened subnet (also known as a demilitarized zone (DMZ)) is a
security architecture that isolates and separates the internal network from the
public-facing internet by placing public-facing services (such as web servers,
email servers, and VPN gateways) in an intermediate security zone. This prevents
direct access to the internal network, reducing the risk of attacks. A screened
subnet typically involves firewalls on both sides, with: One firewall facing the
public internet Another firewall protecting the internal network

Question 276

Which of the following can help prevent unauthorized modifications to hardware
when designing an MDF closet?

    A. Lockable cabinets
    B. Uninterruptable power supply
    C. Port security
    D. Microsegmentation

Answer(s): A. Lockable cabinets

Explanation: Lockable cabinets are an effective physical security measure to
prevent unauthorized access or modifications to hardware in an MDF (Main
Distribution Frame) closet. By securing the equipment inside a locked cabinet,
only authorized personnel can make changes to the hardware, which helps
safeguard against tampering or unauthorized modifications.

Question 277

After installing a new 6E wireless router in a small office, a technician
notices that some wireless devices are not able to achieve the rated speeds.
Which of the following should the technician check to troubleshoot the issue?
(Choose two.)

    A. Client device compatibility
    B. Back-end cabling
    C. Weather phenomena
    D. Voltage source requirements
    E. Interference levels
    F. Processing power

Answer(s): A. Client device compatibility, C. Weather phenomena

Explanation: Client device compatibility: If some wireless devices are unable to
achieve the rated speeds, the issue could be due to the client devices not
supporting the higher speeds of the 6E router (such as the 6 GHz band). The
technician should check whether the devices are compatible with Wi-Fi 6E and
support the speeds offered by the router. Interference levels: Wireless signals
can be affected by interference from other devices, networks, or physical
obstructions. The technician should assess whether interference is impacting the
performance of the wireless network, particularly on the 6 GHz band, which may
be more susceptible to interference in some environments.

Question 278

Which of the following routing protocols needs to have an autonomous system set
in order to establish communication with neighbor devices?

    A. OSPF
    B. EIGRP
    C. FHRP
    D. RIP

Answer(s): B. EIGRP

Explanation: EIGRP (Enhanced Interior Gateway Routing Protocol) requires an
autonomous system (AS) number to be configured in order to establish
communication with neighboring routers. The AS number helps to identify and
group routers that are using the same routing protocol within a specific domain,
enabling them to share routing information effectively.

Question 279

An investment bank is seeking a DR backup solution. Which of the following
provides the most cost-effective backup site?

    A. Hot
    B. Cold
    C. Cluster
    D. Warm

Answer(s): B. Cold

Explanation: A cold backup site is the most cost-effective disaster recovery
(DR) solution because it involves a location that has the necessary
infrastructure (like power and cooling) but no active hardware or systems in
place until needed. It typically requires the least investment because it
doesn't require maintaining servers and other systems running at all times,
unlike hot or warm sites. When a disaster occurs, hardware and systems are then
set up and restored as needed.

Question 280

A firewall administrator is mapping a server's internal IP address to an
external IP address for public use. Which of the following is the name of this
function?

    A. NAT
    B. VIP
    C. PAT
    D. BGP

Answer(s): A. NAT

Explanation: NAT (Network Address Translation) is the function that maps a
server's internal IP address to an external IP address for public use. This
allows internal devices to communicate with external networks (such as the
internet) using a single or a few external IP addresses, while hiding the
internal network structure.

Question 281

A network engineer is completing a new VoIP installation, but the phones cannot
find the TFTP server to download the configuration files. Which of the following
DHCP features would help the phone reach the TFTP server?

    A. Exclusions
    B. Lease time
    C. Options
    D. Scope

Answer(s): C. Options

Explanation: In DHCP, Options can be configured to provide additional
information to the client devices, such as the IP address of the TFTP server.
Specifically, Option 150 is commonly used to specify the TFTP server's IP
address in VoIP installations. This allows the VoIP phones to reach the TFTP
server and download their configuration files.

Question 282

Which of the following best represents north-south traffic?

    A. A connection between a computer and a public web server
    B. Data moving between a data center and a DR site
    C. Traffic between a production server and a backup server
    D. Routing updates between OSPF routers

Answer(s): A. A connection between a computer and a public web server

Explanation: In networking, north–south traffic refers to data flowing into and
out of a data center, typically between client devices (users) and servers.
Option A—a connection between a computer (client) and a public web server—is the
classic example of north–south traffic: The user (north) accesses services
hosted in the data center (south). This is inbound/outbound traffic relative to
the data center. The other options describe east–west traffic, which is internal
or lateral: B: Between a data center and a DR site → intersite data replication
= east–west C: Between production and backup servers → internal server-to-server
traffic = east–west D: Routing updates between OSPF routers → lateral
communication = east–west Therefore, A is the only correct representation of
north–south traffic. Reference: North-south traffic refers to the data flow
between internal network resources (such as servers or devices within a data
center) and external resources, typically going from the internal network to the
outside world or vice versa. A connection between a computer and a public web
server represents this type of traffic, where data moves from an internal
network (the computer) to an external network (the web server on the internet).

Question 283

Which of the following provides an opportunity for an on-path attack?

    A. Phishing
    B. Dumpster diving
    C. Evil twin
    D. Tailgating

Answer(s): C. Evil twin

Explanation: An evil twin attack is a type of on-path attack where an attacker
sets up a rogue Wi-Fi access point that mimics a legitimate network, tricking
users into connecting to it. Once connected, the attacker can intercept and
manipulate the data traffic between the victim and the intended destination,
making it an on-path (man-in-the- middle) attack.

Question 284

A network administrator is configuring a network for a new site that will have
150 users. Within the next year, the site is expected to grow by ten uses. Each
user will have two IP addresses, one computer, and one phone connected to the
network. Which of the following classful IPv4 address ranges will be best-suited
for the network?

    A. Class D
    B. Class B
    C. Class A
    D. Class C

Answer(s): D. Class C

Explanation: A Class C IPv4 address range provides a subnet with up to 254
usable host addresses, which is suitable for networks with around 150 users.
Since each user requires two IP addresses (one for a computer and one for a
phone), the network will need 300 addresses (150 users × 2 IPs per user), which
can easily be accommodated within the 254 usable addresses of a Class C network
with proper subnetting (e.g., using a /24 subnet mask). Therefore, a Class C
network is the best fit for the requirements.

Question 285

A network administrator needs to assign IP addresses to a newly installed
network. They choose 192.168.1.0/24 as their network address and need to create
three subnets with 30 hosts on each subnet. Which of the following is a valid
subnet mask that will meet the requirements?

    A. 255.255.255.128
    B. 255.255.255.192
    C. 255.255.255.224
    D. 255.255.255.240

Answer(s): B. 255.255.255.192

Explanation: To accommodate 30 hosts per subnet, you need a subnet mask that
allows for at least 32 IP addresses per subnet, considering that two addresses
in each subnet are reserved (one for the network address and one for the
broadcast address). The subnet mask 255.255.255.192 provides 64 IP addresses per
subnet, which includes the 30 hosts and the reserved addresses, meeting the
requirement. With a subnet mask of 255.255.255.192, there are 6 bits for the
host portion (2^6 = 64), allowing for 62 usable addresses for hosts (after
excluding the network and broadcast addresses). This is sufficient for 30 hosts
per subnet.

Question 286

The network engineering team needs to implement a wireless network within two
separate buildings. Once the network is set up, users will need to authenticate
using RADIUS in order to access internal resources. Which of the following
wireless technologies should the team implement?

    A. Mesh
    B. Enterprise
    C. Ad hoc
    D. Point to point

Answer(s): B. Enterprise

Explanation: Enterprise wireless networks support robust security features such
as RADIUS (Remote Authentication Dial-In User Service) for user authentication,
making them ideal for environments where secure access to internal resources is
required. This technology allows for centralized authentication and policy
enforcement, ensuring that users can securely connect to the network.
Additionally, enterprise wireless networks support more complex configurations,
such as multiple access points spanning multiple buildings, which is needed in
this case.

Question 287

A network engineer discovers network traffic that is sending confidential
information to an unauthorized and unknown destination. Which of the following
best describes the cause of this network traffic?

    A. Ransomware
    B. Darkware
    C. Malware
    D. Adware

Answer(s): C. Malware

Explanation: Malware is a broad term that encompasses malicious software
designed to damage or disrupt systems, and it can be responsible for sending
confidential information to unauthorized destinations. This could include
spyware, Trojans, or other types of malicious programs that secretly exfiltrate
data. Since the network traffic is sending confidential information to an
unknown destination, it is most likely the result of malware infection on the
network.

Question 288

A security administrator is looking for rogue servers on the network and would
also like to determine which services are running on those servers. Which of the
following software tools should the administrator use?

    A. tracert
    B. nmap
    C. netstat
    D. ping

Answer(s): B. nmap

Explanation: nmap (Network Mapper) is a powerful tool used for network discovery
and security auditing. It can be used to identify rogue servers on the network
by scanning IP ranges and detecting which systems are active. Additionally, nmap
can determine which services (such as HTTP, SSH, etc.) are running on those
servers by performing service detection. This makes it the most suitable tool
for the administrator's need to find rogue servers and determine their services.

Question 289

A network administrator needs to secure SNMP access with authentication and
encryption. Which of the following should the administrator use?

    A. SNMPv3
    B. SNMP community string
    C. SNMP ACL access group
    D. SNMPv2c

Answer(s): A. SNMPv3

Explanation: SNMPv3 (Simple Network Management Protocol version 3) is the
version that provides enhanced security features, including authentication and
encryption. Unlike SNMPv1 and SNMPv2c, which use clear-text community strings
and do not offer encryption, SNMPv3 ensures that SNMP traffic is encrypted and
that access is authenticated using username and passwords, protecting the
integrity and confidentiality of management data.

Question 290

A user's desk has a workstation and an IP phone. The user is unable to browse
the internet on the workstation, but the phone works. Which of the following
configurations is required?

    A. Voice VLAN
    B. Native VLAN
    C. Data VLAN
    D. Trunk port

Answer(s): C. Data VLAN

Explanation: The scenario describes a common enterprise setup where a single
switch port connects both a VoIP phone and a workstation (PC) daisy-chained
through the phone. This configuration requires the switch port to carry traffic
for two separate VLANs: 1.A Voice VLAN (typically tagged, assigned to the phone,
and prioritized). 2.A Data VLAN (typically untagged/native, assigned to the
workstation). Since the IP phone works, the Voice VLAN (A) configuration is
likely already successful and is not the required fix. The workstation is unable
to access the internet, meaning its data traffic is failing. The traffic from
the workstation must be assigned to the Data VLAN to successfully reach the
corporate network and the internet. Therefore, the Data VLAN is the required
configuration that is either missing or incorrectly applied to the workstation
or the switch port. -A Trunk port (D) describes the type of port that carries
multiple VLANs, but Data VLAN (C) is the specific network segment required to
fix the workstation's connectivity problem.

Question 291

A network technician is configuring the company's network 100Mbps port Layer 2
switches. The technician wants increased throughput for the uplinks between
switches. The technician connects multiple redundant links between the switches.
Which of the following should the technician configure?

    A. Spanning Tree Protocol
    B. Switch Virtual Interfaces
    C. Native VLAN
    D. First Hop Redundancy Protocol

Answer(s): A. Spanning Tree Protocol

Explanation: Spanning Tree Protocol (STP) prevents Layer 2 loops when multiple
redundant links exist between switches. STP detects redundant paths and places
one or more ports into a blocking state to maintain a loop-free topology. It
ensures network stability and prevents broadcast storms. Important: STP does not
increase throughput; it only prevents loops. To increase throughput, link
aggregation (LACP) would be required.

Question 292

Which of the following would most likely be utilized to implement encryption in
transit when using HTTPS?

    A. SSH
    B. TLS
    C. SCADA
    D. RADIUS

Answer(s): B. TLS

Explanation: TLS (Transport Layer Security) is the protocol used to implement
encryption in transit for HTTPS (Hypertext Transfer Protocol Secure). It ensures
that data transmitted between a web browser and a server is encrypted, providing
confidentiality and security. TLS is the successor to SSL (Secure Sockets Layer)
and is the standard cryptographic protocol used for securing communications over
a computer network, including HTTPS.

Question 293

Some of the 20 employees who use the wireless network report they are unable to
access network resources even though the wireless network is available. An
administrator recently made the following configuration changes to the wireless
DHCP server: Network: 192.168.100.0 Mask: 255.255.255.240 Gateway: 192.168.100.1
Which of the following is the cause of this issue?

    A. Incorrect VLAN assignment
    B. Incorrect ACL configuration
    C. Incorrect subnet mask
    D. Incorrect default gateway

Answer(s): C. Incorrect subnet mask

Explanation: The subnet mask 255.255.255.240 allows for only 14 usable host IP
addresses per subnet (since 2 IP addresses are reserved for network and
broadcast addresses), but the administrator has 20 employees using the wireless
network. This means that there are not enough IP addresses available within the
subnet for all users to get a valid address. To accommodate 20 devices, a subnet
mask of 255.255.255.224 (which provides 30 usable IP addresses) would be needed
instead.

Question 294

Which of the following typically uses compromised systems that become part of a
bot network?

    A. Evil twin attack
    B. DDoS attack
    C. XML injection
    D. Brute-force password attack

Answer(s): B. DDoS attack

Explanation: A DDoS (Distributed Denial of Service) attack typically uses
compromised systems that are part of a botnet. In a DDoS attack, the attacker
takes control of multiple machines (often through malware) and uses them to
flood a target server or network with excessive traffic, overwhelming it and
causing it to become unavailable to legitimate users. These compromised machines
are part of a botnet, which is a network of infected systems that can be
remotely controlled by the attacker.

Question 295

Which of the following network ports is used when a client accesses an SFTP
server?

    A. 22
    B. 80
    C. 443
    D. 3389

Answer(s): A. 22

Explanation: SFTP (Secure File Transfer Protocol) uses port 22, which is the
same port used by SSH (Secure Shell). SFTP is a secure method for transferring
files over a network, and it operates over SSH to provide encrypted
communication for file transfers.

Question 296

Two companies successfully merged. Following the merger, a network administrator
identified a connection bottleneck. The newly formed company plans to acquire a
high-end 40GB switch and redesign the network from a three-tier model to a
collapsed core. Which of the following should the administrator do until the new
devices are acquired?

    A. Implement the FHRP.
    B. Configure a route selection metric change.
    C. Install a load balancer.
    D. Enable link aggregation.

Answer(s): D. Enable link aggregation.

Explanation: Link aggregation (LACP) bundles multiple physical links into one
logical interface to increase total bandwidth. This alleviates bottlenecks until
the new 40Gb switch is deployed.

Question 297

Which of the following is the step that a troubleshooter should take immediately
after implementing a solution?

    A. Review lessons learned during the process.
    B. Establish a plan of action.
    C. Verify full system functionality.
    D. Document actions and outcomes.

Answer(s): C. Verify full system functionality.

Explanation: After implementing a solution, the next immediate step is to verify
full system functionality. This involves testing the system to ensure that the
solution has resolved the issue and that all components are working as expected.
This step ensures that the solution has addressed the problem effectively before
moving on to documenting actions or reviewing lessons learned.

Question 298

Users can usually use RDP to connect to a terminal server with hostname TS19
that points to 10.0.100.19. However, users recently have been unable to connect
to TS19. The technician pings 10.0.100.19 and gets an unreachable error. Which
of the following is the most likely cause?

    A. The users are on the wrong subnet.
    B. The DHCP server renewed the lease.
    C. The IP address was not reserved.
    D. The hostname was changed.

Answer(s): C. The IP address was not reserved.

Explanation: If the terminal server's IP (10.0.100.19) was not reserved, the
DHCP server may assign that address to another device. The terminal server then
receives a different IP, making the original address unreachable. Reserving or
statically assigning the server’s IP prevents this issue.

Question 299

Which of the following is the OSI model layer that uses a connectionless
protocol for packet delivery?

    A. Physical
    B. Network
    C. Transport
    D. Application

Answer(s): B. Network

Explanation: The Network layer (Layer 3) of the OSI model uses a connectionless
protocol for packet delivery. The most common protocol at this layer is IP
(Internet Protocol), which is connectionless. It sends packets without
establishing a dedicated connection between the sender and receiver, meaning
there is no guaranteed delivery or error recovery at this layer - those
responsibilities are handled by higher layers, such as the Transport layer.

Question 300

A company experiences an incident involving a user who connects an unmanaged
switch to the network. Which of the following technologies should the company
implement to help avoid similar incidents without conducting an asset inventory?

    A. Screened subnet
    B. 802.1X
    C. MAC filtering
    D. Port security

Answer(s): D. Port security

Explanation: Port security restricts how many MAC addresses can be learned on a
switch port. When an unmanaged switch is connected, multiple new MAC addresses
appear on the port, causing a violation. The port can then shut down or block
traffic. This prevents unauthorized devices from expanding the network without
requiring an asset inventory.
