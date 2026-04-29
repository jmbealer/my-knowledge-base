# networkplus

## 1.0 Networking Concepts 23%

### 1.1 Explain concepts related to the Open Systems Interconnection (OSI) reference model.

OSI (Open Systems Interconnection):<7-layer theoretical model for network
communications.

- PDU (Protocol Data Unit):<Data block exchanged at specific protocol layer.
- Layer 1 - Physical:↔Transmits raw bits over physical medium.
- Layer 2 - Data link:↔Node-to-node data transfer and error handling.
- Layer 3 - Network:↔Routing data packets between different networks.
- Layer 4 - Transport:↔Reliable end-to-end data delivery and flow control.
- Layer 5 - Session:↔Managing communication sessions between applications.
- Layer 6 - Presentation:↔Data translation, encryption, and compression
  formatting.
- Layer 7 - Application:↔Interface for end-user network processes.

### 1.2 Compare and contrast networking appliances, applications, and functions.

Physical and virtual appliances

- Router:<Forwards data packets between computer networks.
- Switch:<Connects devices within a single network segment.
- Firewall:<Security device filtering network traffic rules.
- Intrusion detection system (IDS):<Monitors network traffic for suspicious
  activity.
- Intrusion prevention system (IPS):<Detects and blocks malicious network
  activity.
- Load balancer:<Distributes network traffic across multiple servers.
- Proxy:<Intermediary server handling client requests.
- Network-attached storage (NAS):<File-level storage connected to a network.
- Storage area network (SAN):<High-speed network for block-level storage access.
- Wireless
  - Access point (AP):<Bridges wireless clients to wired network.
  - Wireless Controller:<Central management device for multiple access points.

Applications

- Content delivery network (CDN):<Distributed servers speeding up content
  delivery.

Functions

- Virtual private network (VPN):<Encrypted tunnel over a public network.
- Quality of service (QoS):<Prioritizing specific traffic types over others.
- Time to live (TTL):<Packet lifespan limit to prevent looping.

### 1.3 Summarize cloud concepts and connectivity options.

- Network functions virtualization (NFV): Virtualizing network services instead
  of hardware.
  - NFV (Network Functions Virtualization): Virtualizing network services
    instead of hardware.
- Virtual private cloud (VPC): Isolated private network within a public cloud.
  - VPC (Virtual Private Cloud): Isolated private network within a public cloud.
- Network security groups: Virtual firewall rules for cloud resources.
- network security lists
- Cloud gateways
  - Internet gateway: Connects VPC instances to the internet.
  - Network address translation NAT gateway: Enables private instances to access
    internet.
- Cloud Connectivity Options
  - VPN
  - Direct Connect: Dedicated physical connection to cloud provider.
- Deployment models
  - Public cloud: Cloud resources shared by general public.
  - Private cloud: Cloud infrastructure dedicated to single organization.
  - Hybrid cloud: Environment combining public and private clouds.
- Service models
  - Software as a service (SaaS): Software delivered over internet via
    subscription.
  - Infrastructure as a service (IaaS): Virtualized computing resources over the
    internet.
  - Platform as a service (PaaS): Platform for developing and deploying
    applications.
  - IaaS (Infrastructure as a Service): Virtualized computing resources over the
    internet.
  - PaaS (Platform as a Service): Platform for developing and deploying
    applications.
  - SaaS (Software as a Service): Software delivered over internet via
    subscription.
- Scalability: Ability to handle increasing workload growth.
- Elasticity: Automatically scaling resources up and down.
- Multitenancy: Single instance serving multiple distinct customers.

### 1.4 Explain common networking ports, protocols, services, and traffic types.

- Protocols and Ports
  - File Transfer Protocol (FTP): Unencrypted file transfer using ports 20/21.
  - FTP (File Transfer Protocol): Unencrypted file transfer using ports 20/21.
  - Secure File Transfer Protocol (SFTP): Secure file transfer tunneling over
    SSH. 22

  - SFTP (Secure File Transfer Protocol): Secure file transfer tunneling over
    SSH.
  - Secure Shell (SSH): Encrypted remote command-line access and administration.
    22

  - SSH (Secure Shell): Encrypted remote command-line access.
  - Telnet: Unencrypted, insecure remote command-line communication. 23

  - Simple Mail Transfer Protocol (SMTP): Protocol used for sending email
    messages. 25

  - SMTP (Simple Mail Transfer Protocol): Protocol used for sending email
    messages.
  - Domain Name System (DNS): Resolves domain names to IP addresses. 53

  - DNS (Domain Name System): Resolves domain names to IP addresses.
  - Dynamic Host Configuration Protocol (DHCP): Automates IP address assignment
    to network clients. 67/68
  - DHCP (Dynamic Host Configuration Protocol): Automates IP address assignment
    to network clients.
  - Trivial File Transfer Protocol (TFTP): Simple, connectionless file transfer
    without authentication. 69
  - TFTP (Trivial File Transfer Protocol): Simple, connectionless file transfer
    without authentication.
  - Hypertext Transfer Protocol (HTTP): Transmits web pages and data
    unencrypted. 80
  - HTTPS (Hypertext Transfer Protocol Secure): Secure, encrypted web browsing
    over SSL/TLS.
  - Network Time Protocol (NTP): Synchronizes time clocks across network
    devices. 123

  - NTP (Network Time Protocol): Synchronizes clocks on network devices.
  - Simple Network Management Protocol (SNMP): Monitors and manages network
    device statistics. 161/162

  - SNMP (Simple Network Management Protocol): Protocol monitoring and managing
    network devices.
  - Lightweight Directory Access Protocol (LDAP): Accesses/maintains distributed
    directory info services. 389

  - LDAP (Lightweight Directory Access Protocol): Protocol for querying
    directory services.
  - Hypertext Transfer Protocol Secure (HTTPS): Secure, encrypted web browsing
    over SSL/TLS. 433

  - HTTP (Hypertext Transfer Protocol): Transmits web pages and data
    unencrypted.
  - Server Message Block (SMB): Network file, printer, and serial port sharing.
    445

  - SMB (Server Message Block): Network file, printer, and serial port sharing.
  - Syslog: Standard protocol for sending system log messages. 514

  - Simple Mail Transfer Protocol Secure (SMTPS): Secure email submission using
    encryption. 587

  - Lightweight Directory Access Protocol over SSL (LDAPS): Secure directory
    service access over SSL/TLS. 636
  - Structured Query Language (SQL) Server 1433
  - Remote Desktop Protocol (RDP) 3389
  - Session Initiation Protocol (SIP) 5060/5061
- Internet Protocol (IP) types
  - IP (Internet Protocol): Principal communications protocol in internet
    protocol suite.
  - ICMP: Reports network errors and diagnostics (e.g., ping).
    - ICMP (Internet Control Message Protocol): Reports network errors and
      diagnostics.
  - TCP: Reliable, connection-oriented, guaranteed data delivery.
    - TCP (Transmission Control Protocol): Reliable, connection-oriented,
      guaranteed data delivery.
  - UDP: Fast, connectionless, best-effort data transmission.
    - UDP (User Datagram Protocol): Fast, connectionless, best-effort data
      transmission.
  - GRE: Tunneling protocol encapsulating arbitrary network protocols.
    - GRE (Generic Routing Encapsulation): Tunneling protocol encapsulating
      arbitrary network protocols.
  - Internet Protocol Security IPSec: Suite ensuring IP packet confidentiality
    and integrity.
  - IPSec (Internet Protocol Security): Suite ensuring IP packet confidentiality
    and integrity.
    - Authentication Header (AH): Verifies sender identity and data integrity.
      - AH (Authentication Header): Verifies sender identity and data integrity.
    - Encapsulating Security Payload (ESP): Provides encryption, authentication,
      and integrity for data.
      - ESP (Encapsulating Security Payload): Provides encryption,
        authentication, and integrity for data.
    - Internet Key Exchange (IKE): Negotiates security keys and associations
      automatically.
      - IKE (Internet Key Exchange): Negotiates security keys and associations
        automatically.
- Traffic types
  - Unicast: One-to-one communication between single sender and receiver.
  - Multicast: One-to-many communication to subscribed group members.
  - Anycast
  - Broadcast: One-to-all communication to every node on segment.
- -- Integrated Acronyms --
- ACL (Access Control List): Rules determining access rights to network
  resources.
- API (Application Programming Interface): Code allowing software applications
  to communicate.
- ARP (Address Resolution Protocol): Resolves IP addresses to MAC hardware
  addresses.

### 1.5 Compare and contrast transmission media and transceivers.

- Wireless
  - 802.11 standards: Wireless networking standards utilizing radio
    transmission.
  - Cellular: Wireless data transmission via mobile phone networks.
  - Satellite: Internet access via orbiting relay stations.
- Wired
  - 802.3 standards: IEEE standards defining wired Ethernet specifications.
  - Single-mode fiber (SMF): Fiber carrying single light path long distance.
  - Multimode fiber (MMF): Fiber cable carrying multiple light paths.
  - Direct attach copper (DAC): Copper cable with integrated transceivers.
    - DAC (Direct Attach Copper): Copper cable with integrated transceivers.
    - Twinaxial cable: Copper cable with two inner conductors.
  - Coaxial cable: Cable with inner conductor and outer shield.
  - Cable speeds
  - Plenum cable: Fire-resistant cable for air handling spaces.
  - Non-Plenum Cable
- Transceivers
  - Protocol
    - Ethernet
    - Fibre Channel (FC)
  - Form factors
    - Small form-factor pluggable (SFP): Compact optical transceiver module
      supporting 1Gbps.
      - SFP (Small Form-factor Pluggable): Compact optical transceiver module.
    - Quad small form-factor pluggable (QSFP): High-speed fiber transceiver
      supporting 4 channels.
      - QSFP (Quad Small Form-factor Pluggable): High-speed fiber transceiver
        supporting 4 channels.
- Connector types
  - Subscriber connector (SC): Push-pull square fiber optic connector.
    - SC (Subscriber Connector): Push-pull square fiber optic connector.
  - Local connector (LC): Small form-factor fiber optic connector.
    - LC (Local Connector): Small form-factor fiber optic connector.
  - Straight tip (ST): Bayonet-style twist-and-lock fiber connector.
    - ST (Straight Tip): Bayonet-style twist-and-lock fiber connector.
  - Multi-fiber push on (MPO): Fiber connector terminating multiple strands.
    - MPO (Multifiber Push On): Fiber connector terminating multiple strands.
  - RJ11:
    - RJ (Registered Jack): Standard connector interface (e.g., RJ45).
  - RJ45: Standard connector for twisted pair Ethernet.
  - F-type connector: Screw-on connector for coaxial cable.
  - Bayonet Neill–Concelman (BNC): Twist-lock connector for coaxial cables.
    - BNC (Bayonet Neill–Concelman): Twist-lock connector for coaxial cables.
- -- Integrated Acronyms --
- UPC/APC (Ultra/Angled Physical Contact): Fiber connector polish types.

### 1.6 Compare and contrast network topologies, architectures, and types.

- Mesh topology: Network where nodes connect to multiple others.
- Hybrid topology: Network mixing multiple topology types.
- Star/hub and spoke: Nodes connecting to central device.
- Spine and leaf: Datacenter topology reducing latency between servers.
- Point to point: Direct connection between two nodes.
- Three-tier hierarchical model: Design separating Core, Distribution, and
  Access.
  - Core layer: High-speed backbone of network hierarchy.
  - Distribution layer: Layer connecting access switches to core.
  - Access layer: Network hierarchy tier connecting end-user devices.
- Collapsed core: Topology merging core and distribution layers.
- Traffic flows
  - North-south traffic: Data flow entering or leaving datacenter.
  - East-west traffic: Data flow between servers in datacenter.
- -- Integrated Acronyms --
- LAN (Local Area Network): Network within a limited geographic area.
- WAN (Wide Area Network): Network spanning large geographic distances.
- PAN (Personal Area Network): Very short range network (Bluetooth).
- MAN (Metropolitan Area Network): Network spanning a city or campus.
- MDF (Main Distribution Frame): Central point for network cabling termination.
- IDF (Intermediate Distribution Frame): Cable rack connecting end devices to
  MDF.

### 1.7 Given a scenario, use appropriate IPv4 network addressing.

- Public vs. Private
  - APIPA: Self-assigned fallback IP when DHCP fails.
    - APIPA (Automatic Private Internet Protocol Addressing): Self-assigned
      fallback IP when DHCP fails.
  - RFC1918: Standard defining private, non-routable IP ranges.
  - Loopback: IP directing traffic to the local host.
  - localhost
- Subnetting
  - Variable Length Subnet Mask (VLSM): Subnetting using different mask lengths
    efficiently.
    - VLSM (Variable Length Subnet Mask): Subnetting using different mask
      lengths efficiently.
  - Classless Inter-domain Routing (CIDR): Flexible IP addressing using prefix
    notation.
    - CIDR (Classless Inter-domain Routing): Flexible IP addressing using prefix
      notation.
- IPv4 address classes
  - Class A: Large network block (1.0.0.0 to 126.x.x.x).
  - Class B: Medium network block (128.0.0.0 to 191.x.x.x).
  - Class C: Small network block (192.0.0.0 to 223.x.x.x).
  - Class D: Address range reserved for multicast traffic.
  - Class E:

### 1.8 Summarize evolving use cases for modern network environments.

- Software-defined network (SDN) and Software-defined Wide Area Network (SD-WAN)
  - Software-defined network (SDN): Centralized software control of network
    hardware.
  - SD-WAN: Software-based management of WAN connections.
  - SDN (Software-defined Network): Centralized software control of network
    hardware.
  - SD-WAN (Software-defined Wide Area Network): Software-based management of
    WAN connections.
  - Applications aware
  - Zero-touch provisioning: Automated device setup without manual intervention.
  - Transport agnostic
  - Central policy management
- VXLAN: Tunneling protocol extending VLANs over Layer 3.
  - VXLAN (Virtual Extensible LAN): Tunneling protocol extending VLANs over
    Layer 3.
  - Data center interconnect (DCI)
  - Layer 2 encapsualtion
- Zero trust architecture (ZTA): Security model verifying every access request.
  - ZTA (Zero Trust Architecture): Security model verifying every access
    request.
  - Policy-based authentication
  - Authorization
  - Least privilege access
- Secure Access Secure Edge (SASE)/Security Security Edge (SSE)
  - Secure Access Secure Edge (SASE): Converging WAN and security into cloud
    service.
  - SASE (Secure Access Service Edge): Converging WAN and security into cloud
    service.
- Infrastructure as code (IaC): Managing infrastructure via definition files.
  - IaC (Infrastructure as Code): Managing infrastructure via definition files.
  - Automation: Scripting tasks to reduce manual intervention.
    - Playbooks/templates/reusable tasks
    - Upgrades
    - Configuration drift: Systems deviating from baseline settings over time.
      - configuration drift/compliance
    - Dynamic inventories
  - Source control
    - Version control
    - Central repository
    - Conflict identification
    - Branching
- IPv6 addressing: 128-bit addressing system replacing IPv4.
  - Mitigating address exhaustion
  - Compatibility requirements
    - Tunneling
    - Dual stack: Running IPv4 and IPv6 simultaneously.
    - NAT64

## 2.0 Network Implementation 20%

### 2.1 Explain characteristics of routing technologies.

Static routing: Manually configured routing entries by an administrator.

Dynamic routing: Routers automatically exchanging path information.

    - BGP (Border Gateway Protocol): Protocol routing between internet autonomous systems.
    - EIGRP (Enhanced Interior Gateway Routing Protocol): Cisco routing protocol using bandwidth and delay.
    - OSPF (Open Shortest Path First): Link-state routing protocol using Dijkstra's algorithm.

Route Selection

    - Administrative distance: Metric rating the trustworthiness of routing sources.
    - Prefix length
    - Metric

Address Translation

    - NAT (Network Address Translation): Modifying IP addresses in packet headers.
    - PAT (Port Address Translation): Sharing one public IP via multiple ports.

FHRP (First Hop Redundancy Protocol): Provides failover for default gateways.

Virtual IP (VIP): Shared IP address for cluster failover.

Subinterfaces

RIP (Routing Information Protocol): Distance-vector routing protocol using hop
count.

### 2.2 Given a scenario, configure switching technologies and features

VLAN (Virtual Local Area Network): Logical network segment on physical switch.

    - VLAN database:
    - SVI (Switch Virtual Interface): Logical layer 3 interface on switch.

Interface Configuration

    - Native VLAN: VLAN for untagged traffic on trunk ports.
    - Voice VLAN
    - 802.1Q tagging: Trunking protocol tagging frames for VLAN identification.
    - Link aggregation: Combining ports to increase bandwidth.
        - LACP (Link Aggregation Control Protocol): Protocol for bundling ports into single channel.
    - Speed
    - Duplex

STP (Spanning Tree Protocol): Protocol preventing layer 2 loops.

    - RSTP (Rapid Spanning Tree Protocol): Faster convergence version of Spanning Tree Protocol.

MTU (Maximum Transmission Unit): Largest data packet size supported by
interface.

    - Jumbo frames: Ethernet frame larger than standard 1500 bytes.

### 2.3 Given a scenario, select and configure wireless devices and technologies

Channels - Channel width: Frequency range used for data transmission. -
Non-overlapping channels - Regulatory Impacts - 802.11h: Wi-Fi amendment
preventing interference with radar.

Frequency Options

- 2.4GHz
- 5GHz
- 6GHz
- Band steering

SSID (Service Set Identifier): Name identifying a wireless network.

- BSSID (Basic Service Set Identifier): MAC address of a wireless access point.
- ESSID (Extended Service Set Identifier): Network name across multiple access
  points. Network types

- Mesh networks: Wireless nodes acting as repeaters.
- Ad hoc
- Point to point
- Infrastructure

Encryption

- WPA2: Standard Wi-Fi security using AES encryption.
- WPA3: Latest Wi-Fi security with improved encryption.
- WPA (Wi-Fi Protected Access): Security standard for wireless networks.
- WPS (Wi-Fi Protected Setup): Insecure simplified wireless connection method.

Guest Networks

- Captive portals: Webpage requiring interaction before network access.

Authentication

- Pre-shared vs. enterprise
- Pre-shared key (PSK): Password shared by all users for access.

Antennas

- Omnidirectional vs. directional
- Omnidirectional antenna: Antenna radiating signal in all directions equally.

Autonomous vs. Lightweight access point

### 2.4 Explain important factors of physical installations

Important Installation Implications

- Locations
  - IDF (Intermediate Distribution Frame): Cable rack connecting end devices to
    MDF.
  - MDF (Main Distribution Frame): Central point for network cabling
    termination.
- Rack size: Standardized width and height units (U).
- Port-side exhaust/intake
- Cabling
  - Patch panel: Hardware assembly for organizing cable connections.
  - Fiber distribution panel
- Lockable

Power

- UPS (Uninterruptible Power Supply): Battery backup for power outages.
- PDU (Power Distribution Unit): Device distributing electric power to rack
  equipment.
- Power load
- Voltage

Environment Factors

- Humidity
- Fire Suppression
- Temperature

## 3.0 Network Operations 19%

### 3.1 Explain the purpose of organizational processes and procedures

Documentation

- Physical vs. logical diagrams
- Rack diagrams
- Cable maps and diagrams
- Network diagrams
  - Layer 1
  - Layer 2
  - Layer 3
- Asset inventory: Detailed list of hardware, software, and licenses.
  - Hardware
  - Software
  - Licensing
  - Warranty support
  - AUP (Acceptable Use Policy): Policy defining acceptable use of resources.
- IP address management (IPAM): Software tracking IP address allocation
  network-wide.
  - IPAM (Internet Protocol Address Management): Software tracking IP address
    allocation network-wide.
- Service-level agreement (SLA): Contract defining expected service performance
  standards.
  - SLA (Service-level Agreement): Contract defining expected service
    performance standards.
- Wireless survey/heat map
  - Wireless heat map: Visualizing wireless signal strength and coverage.

Life-cycle management

- End-of-life (EOL): Vendor stops selling or marketing a product.
- End-of-support (EOS): Vendor stops providing updates or technical assistance.
- Software management
  - Patches and bug fixes
  - Operating system (OS)
  - Firmware
- Decommissioning: Removing assets from service and secure disposal.

Change management: Formal process for approving system modifications.

- Request process tracking/service request

Configuration management

- Production configuration
- Backup configuration
- Baseline/golden configuration

### 3.2 Given a scenario, use network monitoring technologies

Methods

- SNMP: Protocol monitoring and managing network devices.
  - Trap (SNMP): Unsolicited alert sent by device to manager.
    - Management information base (MIB): Database of variables managed by SNMP.
      - Versions
        - v2c
        - v3
    - Community strings
    - Authentication
- Flow data: Statistics on network traffic patterns (NetFlow).
- Packet capture
- Baseline metrics
  - Anomaly alerting/notification
- Log aggregation
  - Syslog collector: Server gathering log messages from network devices.
  - Security information and event management (SIEM): Real-time analysis of
    security logs/alerts.
- Application programming interface (API) integration
- Port mirroring: Copying switch traffic to monitor port.

Solutions

- Network discovery: Identifying devices present on a network.
  - Ad hoc
  - Scheduled
- Traffic analysis
- Performance monitoring
- Availability monitoring
- Configuration monitoring

SNMP (Simple Network Management Protocol): Protocol monitoring and managing
network devices.

### 3.3 Explain disaster recovery (DR) concepts

DR metrics

- Recovery point objective (RPO): Max data loss tolerable after disaster.
- Recovery time objective (RTO): Max time allowed to restore services.
- Mean time to repair (MTTR): Average time to fix a failed device.
- Mean time between failures (MTBF): Average time before a component fails.

DR sites

- DR (Disaster Recovery): Procedures for restoring systems after failure.
- Cold site: Empty backup facility needing equipment setup.
- Warm site: Partially equipped backup site, not fully active.
- Hot site: Fully operational backup site ready immediately.

High-availability approaches

- Active-active
- Active-passive

Testing

- Tabletop exercises
- Validation tests

### 3.4 Given a scenario, implement IPv4 and IPv6 network services

Dynamic addressing

- DHCP (Dynamic Host Configuration Protocol): Automates IP address assignment to
  network clients.
  - Reservations
    - DHCP Reservation: Assigning specific IP to specific MAC permanently.
  - Scope: Range of IPs available for DHCP distribution.
  - Lease time
  - Options
  - Relay/IP helper: Forwarding DHCP requests across subnets.
  - Exclusions
- Stateless address autoconfiguration (SLAAC): IPv6 hosts generating own
  addresses automatically.

Name resolution

- DNS (Domain Name System): Resolves domain names to IP addresses.
  - Domain Name System Security Extensions (DNSSEC): Cryptographic
    authentication for DNS records.
  - DNS over HTTPS (DoH) and DNS over TLS (DoT) - DoH (DNS over HTTPS):
    Encrypting DNS queries via HTTPS protocol. - DoT (DNS over TLS): Encrypting
    DNS queries via TLS protocol.
  - Record types
    - Address (A) record: Maps hostname to IPv4 address.
      - A (Address): DNS record mapping hostname to IPv4 address.
    - AAAA record: Maps hostname to IPv6 address.
    - CNAME record: Alias mapping one hostname to another.
      - CNAME (Canonical Name): Alias mapping one hostname to another.
    - Mail exchange (MX) record: Directs email to domain's mail server.
      - MX (Mail Exchange): Directs email to domain's mail server.
    - Text (TXT): DNS record holding arbitrary text information.
    - Nameserver (NS): Designates authoritative name servers for domain.
    - Pointer (PTR) record: Maps IP address to hostname (reverse DNS).
    - Zone types
      - Zone transfer: Replicating DNS records between servers.
      - Forward
      - Reverse
    - Authoritative vs. non-authoritative
    - Primary vs. secondary
    - Recursive
      - Recursive lookup: DNS server querying others to resolve name.
- Hosts file

Time protocols

- NTP
- Precision Time Protocol (PTP)
- Network Time Security (NTS)

SOA (Start of Authority): DNS record identifying zone's authoritative source.

### 3.5 Compare and contrast network access and management methods

Site-to-site VPN: Connecting two entire networks securely.

    - VPN (Virtual Private Network): Encrypted tunnel over a public network.

Client-to-site VPN: Remote user connecting securely to corporate network.

- Clientless
- Split tunnel vs. full tunnel
  - Split tunnel: Routing only specific traffic through VPN.
  - Full tunnel: Routing all traffic through VPN gateway.

Connection methods

- SSH (Secure Shell): Encrypted remote command-line access.
  - RDP (Remote Desktop Protocol): GUI remote access protocol for Windows.
- Graphical user interface (GUI)
- API
- Console

Jump box/host: Hardened intermediary for accessing sensitive zones.

In-band vs. out-of-band management

    - Out-of-band management: Admin traffic using dedicated, separate network path.

## 4.0 Network Security 14%

### 4.1 Explain the importance of basic network security concepts

Logical security

- Encryption: Scrambling data to prevent unauthorized access.
  - Data in transit
  - Data at rest
- Certificates
  - Public key infrastructure (PKI)
  - PKI: Framework managing digital certificates and keys.
  - Self-signed
- Identity and access management (IAM): Managing user identities and resource
  access.
  - Authentication
    - Multifactor authentication (MFA): Authentication requiring two or more
      credential types.
    - Single sign-on (SSO): Logging in once to access multiple systems.
    - Remote Authentication Dial- in User Service (RADIUS): Server handling
      authentication for network access.
    - LDAP
    - Security Assertion Markup Language (SAML): XML format exchanging
      authentication data.
    - Terminal Access Controller Access Control System Plus (TACACS+): Protocol
      for AAA services, typically device admin.
    - Time-based authentication
  - Authorization
    - Least privilege: Granting only minimum necessary access rights.
    - Role-based access control RBAC: Access rights based on user job function.
- Geofencing

Physical security

- Camera
- Locks

Deception technologies

- Honeypot: Decoy system luring attackers to detect threats.
- Honeynet

Common security terminology

- Risk: Probability of threat exploiting vulnerability.
- Vulnerability: Security weakness susceptible to exploit.
- Exploit
- Threat
- Confidentiality, Integrity, and Availability (CIA) triad
  - CIA (Confidentiality, Integrity, and Availability): Security model.

Audits and regulatory compliance

- Data locality
- Payment Card Industry Data Security Standards (PCI DSS)
- General Data Protection Regulation (GDPR)

Network segmentation enforcement

- Internet of Things (IoT) and Industrial Internet of Things (IIoT)
- Supervisory control and data acquisition (SCADA), industrial control System
  (ICS), operational technology (OT)
- Guest
- Bring your own device (BYOD)

### 4.2 Summarize various types of attacks and their impact to the network

Denial-of-service (DoS)/distributed denial-of-service (DDoS)

- DoS: Attack preventing legitimate access to resources.
- DDoS: DoS attack from multiple sources simultaneously.

VLAN hopping: Attacking by moving between VLANs.

Media Access Control (MAC) flooding ARP poisoning: Corrupting ARP cache to map
attacker's MAC.

ARP spoofing

DNS poisoning: Injecting fake DNS records to redirect traffic.

DNS spoofing

Rogue devices and services

- DHCP
- AP
  - Rogue access point: Unauthorized wireless access point on network.

Evil twin: Fake access point mimicking a legitimate one.

On-path attack

Social engineering Phishing: Fraudulent emails tricking users into revealing
info.

- Dumpster diving
- Shoulder surfing
- Tailgating

Malware: Malicious software harming systems or data.

### 4.3 Given a scenario, apply network security features, defense techniques, and solutions

Device hardening: Securing a system by reducing attack surface.

- Disable unused ports and services
- Change default passwords

Network access control (NAC): Controlling device admission to the network.

- Port security: Limiting port access by MAC address.
- 802.1X: Port-based network access control and authentication.
- MAC filtering

Key management

Security rules

- Access control list (ACL): Rules determining access rights to network
  resources.
- Uniform Resource Locator (URL) filtering
- Content filtering

Zones

- Trusted vs. untrusted
- Screened subnet: Semi-public zone separating internet and LAN.

Integrated Acronyms

- UTM (Unified Threat Management): All-in-one security appliance.

## 5.0 Network Troubleshooting 24%

### 5.1 Explain the troubleshooting methodology

Identify the problem: Gather information, symptoms, and changes.

- Gather Information:
- question users:
- identify symptoms:
- determine if anything has changed:
- duplicate the problem, if possible:
- approach multiple problems individually:

Establish a Theory of Probable Cause: Brainstorm probable causes starting with
the obvious.

- Question the Obvious:
- consider multiple approaches:
  - top-to-bottom/bottom-to-top OSI model:
  - divide and conquer:

Test the theory to Determine the Cause: Confirm the cause or escalate if
incorrect.

- If theory is confirmed, determine next steps to resolve problem
- if theory is not confirmed, establish a new theory or escalate

Establish a Plan of action to resolve the problem and identify potential
effects: Determine steps to fix and assess impact.

Implement the solution or escalate as necessary: Execute the fix or escalate if
needed.

Verify full system functionality and implement preventive measures if
applicable: Confirm system works and prevent recurrence.

Document findings, actions, outcomes, and lessons learned throughout the
process: Record actions, outcomes, and lessons learned.

### 5.2 Given a scenario, troubleshoot common cabling and physical interface issues

Cable issues

- Incorrect cable
  - Single mode vs. multimode
  - Category 5/6/7/8
  - Shielded twisted pair (STP) vs. unshielded twisted pair (UTP)
- Signal degradation
  - Crosstalk: Signal bleeding between adjacent wires.
  - Interference: External signals disrupting network transmission (EMI/RFI).
  - Attenuation: Loss of signal strength over distance.
- Improper termination
- Transmitter (TX)/Receiver(RX) transposed

Interface issues

- Increasing interface counters
  - CRC: Error-detecting code indicating corrupted frames.
  - Runts: Ethernet frame smaller than permitted minimum.
  - Drops: Packets discarded due to congestion or errors.
- Port status
  - Error disabled: Port disabled by switch due to error condition.
  - Administratively down
  - Suspended

Hardware issues

- Power over Ethernet (PoE)
  - Power budget exceeded
  - Incorrect standard
- Transceivers
  - Mismatch
  - Signal strength

### 5.3 Given a scenario, troubleshoot common issues with network services

Switching issues

- STP
  - Network loops: Traffic circulating endlessly between switches.
  - Root bridge selection: Electing main switch in Spanning Tree.
  - Port roles Port states
- Incorrect VLAN assignment
- ACLs

Route selection

- Routing table
- Default routes

Address pool exhaustion: No available IP addresses in DHCP scope.

Incorrect default gateway

Incorrect IP address

- Duplicate IP address: Two devices assigned same IP, causing conflict.

Incorrect subnet mask

### 5.4 Given a scenario, troubleshoot common performance issues

Congestion/contention

Bottlenecking: Point of congestion limiting overall performance.

Bandwidth

- Throughput capacity: Actual data transfer rate supported by link.

Latency: Time delay for data to reach destination.

Packet loss

Jitter: Variation in packet arrival time.

Wireless

- Interference
  - Channel overlap: Wireless frequencies interfering with each other.
- Signal degradation or loss
- Insufficient wireless coverage
- Client disassociation issues
- Roaming misconfiguration

### 5.5 Given a scenario, use the appropriate tool or protocol to solve networking issues

Software tools

- Protocol analyzer: Tool decoding and displaying network traffic (Wireshark).
- Command line
  - ping: Tool checking network reachability via ICMP.
  - traceroute/tracert
    - traceroute: Tool showing path packets take to host.
  - nslookup: Tool for querying DNS records.
  - tcpdump
  - dig
  - netstat: Tool displaying active network connections.
  - ip/ifconfig/ipconfig
    - ip/ifconfig: Tool displaying network interface configuration.
  - arp
- nmap: Tool for network discovery and vulnerability scanning.
- Link Layer Discovery Protocol (LLDP)/Cisco Discovery Protocol (CDP)
- Speed tester

Hardware tools

- Toner
- Cable tester: Device verifying continuity of copper cabling.
- Taps
- Wi-Fi analyzer: Tool visualizing wireless signal strength and channels.
- Visual fault locator

Basic networking device commands

- show mac-address-table
- show route
- show interface
- show config
- show arp
- show vlan
- show power
