# networkplus

## 1.0 Networking Concepts 23%

### 1.1 Explain concepts related to the Open Systems Interconnection (OSI) reference model.



Open Systems Interconnection (OSI): Standardized seven-layer framework for network communication.



- Mnemonic: All People Seem To Need Data Processing. <!-- newly added -->







OSI Interactions <!-- newly added -->



- ...



- Decapsulation: Removing headers to extract payload data. <!-- newly added -->







Communication Synchronization <!-- newly added -->



- Asynchronous Communication: Uses start and stop bits for timing. <!-- newly added -->



- Synchronous Communication: Uses common clock source for real-time timing. <!-- newly added -->







Bandwidth Utilization <!-- newly added -->



- Baseband: Uses entire medium frequency for one signal. <!-- newly added -->



- Broadband: Divides medium bandwidth into multiple separate channels. <!-- newly added -->







- Protocol Data Unit (PDU): Data block exchanged at specific protocol layers.



- ...

  - PDU: Bits. <!-- newly added -->

- Layer 2 - Data Link: Node-to-node data transfer and error handling.

  - PDU: Frames. <!-- newly added -->

  - Logical Link Control (LLC): Manages multiplexing, flow, and error control. <!-- newly added -->

  - Media Access Control (MAC): Handles physical addressing and medium access. <!-- newly added -->

- Layer 3 - Network: Routing data packets between different networks.

  - PDU: Packets. <!-- newly added -->

- Layer 4 - Transport: Reliable end-to-end data delivery and flow control.

  - PDU: Segments (TCP) or Datagrams (UDP). <!-- newly added -->

- Layer 5 - Session: Managing communication sessions between applications.

  - PDU: Data. <!-- newly added -->

- Layer 6 - Presentation: Data translation, encryption, and compression formatting.

  - PDU: Data. <!-- newly added -->

- Layer 7 - Application: Interface for end-user network processes.

  - PDU: Data. <!-- newly added -->

### 1.2 Compare and contrast networking appliances, applications, and functions.



Nodes: Devices that send, receive, or forward data. <!-- newly added -->

- Intermediate Nodes: Perform data forwarding functions between other nodes. <!-- newly added -->

- End Systems: Devices that send or receive data traffic. <!-- newly added -->

- Hosts: Another term for end system network devices. <!-- newly added -->



Network Models <!-- newly added -->

- Client-Server: Powerful servers centrally provision resources for clients. <!-- newly added -->

- Peer-to-Peer: Decentralized model where hosts share all roles. <!-- newly added -->



Physical: Hardware-based network components and devices.

Virtual Appliances: Software-based network functions running on hypervisors.

- Router: Forwards data packets between computer networks.
- Switch: Connects devices within a single network segment.
- Bridge: Connects and filters traffic between network segments. <!-- newly added -->
- Hub: Multi-port repeater for connecting network devices. <!-- newly added -->
- Repeater: Regenerates network signals to extend transmission distance. <!-- newly added -->
- Modem: Modulates and demodulates signals for data transmission. <!-- newly added -->
- Firewall: Security device filtering network traffic rules.
- Intrusion Detection System (IDS): Monitors network traffic for suspicious
  activity.
- Intrusion Prevention System (IPS): Detects and blocks malicious network
  activity.
- Load Balancer: Distributes network traffic across multiple servers.
- Proxy: Intermediary server handling client requests.
- Network-Attached Storage (NAS): File-level storage connected to a network.
- Storage Area Network (SAN): High-speed network for block-level storage access.
- Wireless: Communication using radio waves instead of cables.
  - Access Point (AP): Bridges wireless clients to wired network.
  - Wireless Controller: Central management device for multiple access points.

Applications: Software programs performing specific network-related tasks.

- Content Delivery Network (CDN): Distributed servers speeding up content
  delivery.

Functions: Specific operations or roles within network architecture.

- Virtual Private Network (VPN): Encrypted tunnel over a public network.
- Quality of Service (QoS): Prioritizing specific traffic types over others.
- Time to Live (TTL): Packet lifespan limit to prevent looping.

### 1.3 Summarize cloud concepts and connectivity options.

- Network Functions Virtualization (NFV): Virtualizing network services by
  decoupling from hardware.
- Virtual Private Cloud (VPC): Isolated private network within a public cloud.
- Network Security Groups (NSG): Virtual firewall rules for cloud resources.
- Network Security Lists: Cloud-based access control lists for subnets.
- Cloud Gateways: Entry points connecting local networks to cloud.
  - Internet Gateway (IGW): Connects VPC instances to the internet.
  - Network Address Translation (NAT) Gateway: Enables private instances to
    access internet.
- Cloud Connectivity Options: Methods for establishing connections to cloud
  providers.
  - Virtual Private Network (VPN): Encrypted tunnel over a public network.
  - Direct Connect: Dedicated physical connection to cloud provider.
- Deployment Models: Different ways cloud services are hosted.
  - Public Cloud: Cloud resources shared by general public.
  - Private Cloud: Cloud infrastructure dedicated to single organization.
  - Hybrid Cloud: Environment combining public and private clouds.
  - Community Cloud: Infrastructure shared by specific organizations with common goals. <!-- newly added -->
- Service Models: Categories of services provided by cloud vendors.
  - Software as a Service (SaaS): Software delivered over internet via subscription.
  - Infrastructure as a Service (IaaS): Virtualized computing resources over the internet.
  - Platform as a Service (PaaS): Platform for developing and deploying applications.
  - Desktop as a Service (DaaS): Cloud-hosted virtual desktops accessible via internet. <!-- newly added -->
- Cloud Characteristics <!-- newly added -->
  - Measured Service: Resource usage is tracked and billed accordingly. <!-- newly added -->
  - Resource Pooling: Provider resources serve multiple consumers dynamically. <!-- newly added -->
  - Shared Responsibility: Security duties split between provider and user. <!-- newly added -->
- Scalability: Ability to handle increasing workload growth.
- Elasticity: Automatically scaling resources up and down.
- Multitenancy: Single instance serving multiple distinct customers.

### 1.4 Explain common networking ports, protocols, services, and traffic types.

- Protocols: Rules governing data exchange between network devices.
- Ports: Logical endpoints for identifying specific processes.
  - Well-Known Ports: Reserved for core services (0–1023). <!-- newly added -->
  - Registered Ports: Used by applications and vendors (1024–49151). <!-- newly added -->
  - Dynamic Ports: Temporary ports for client-side use (49152–65535). <!-- newly added -->
  - File Transfer Protocol (FTP): Transfers files between systems using ports
    20/21.
  - Secure File Transfer Protocol (SFTP): Secure file transfer using SSH on
    port 22.
  - Secure Shell (SSH): Encrypted remote command-line access on port 22.
  - Telnet: Unencrypted remote command-line communication on port 23.
  - Simple Mail Transfer Protocol (SMTP): Sends email messages using port 25.
  - Domain Name System (DNS): Resolves domain names to IP addresses (port 53).
  - Dynamic Host Configuration Protocol (DHCP): Automates IP address assignment
    (ports 67/68).
  - Trivial File Transfer Protocol (TFTP): Simple file transfer without
    authentication (port 69).
  - Hypertext Transfer Protocol (HTTP): Transmits unencrypted web data on
    port 80.
  - Hypertext Transfer Protocol Secure (HTTPS): Secure, encrypted web browsing
    on port 443.
  - Network Time Protocol (NTP): Synchronizes clocks on network devices (port
    123).
  - Simple Network Management Protocol (SNMP): Monitors and manages network
    devices (ports 161/162).
  - Lightweight Directory Access Protocol (LDAP): Queries and manages
    distributed directory information (port 389).
  - Server Message Block (SMB): Network file and printer sharing (port 445).
  - Syslog: Standard protocol for system log messages (port 514).
  - Simple Mail Transfer Protocol Secure (SMTPS): Secure email submission using
    port 587.
  - Lightweight Directory Access Protocol over SSL (LDAPS): Secure directory
    access on port 636.
  - SQL Server: Microsoft database communication using port 1433.
  - MySQL: Open-source database communication on port 3306. <!-- newly added -->
  - Remote Desktop Protocol (RDP): GUI-based remote access on port 3389.
  - Kerberos: Secure network authentication protocol on port 88. <!-- newly added -->
  - Post Office Protocol 3 (POP3): Retrieves email from server on port 110. <!-- newly added -->
  - Internet Message Access Protocol (IMAP): Manages email on remote server (port 143). <!-- newly added -->
  - File Transfer Protocol Secure (FTPS): Secure file transfer using TLS (ports 989/990). <!-- newly added -->
  - Internet Message Access Protocol Secure (IMAPS): Secure email management using TLS (port 993). <!-- newly added -->
  - Post Office Protocol 3 Secure (POP3S): Secure email retrieval using TLS (port 995). <!-- newly added -->
  - Remote Authentication Dial-In User Service (RADIUS): Centralized authentication and accounting (ports 1812/1813). <!-- newly added -->
  - Diameter: Modern successor to RADIUS authentication protocol. <!-- newly added -->
  - Secure Real-Time Transport Protocol (SRTP): Secure streaming of audio and video. <!-- newly added -->
  - Layer 2 Tunneling Protocol (L2TP): VPN tunneling protocol on port 1701. <!-- newly added -->
  - Point-to-Point Tunneling Protocol (PPTP): Legacy, deprecated VPN tunneling protocol (port 1723). <!-- newly added -->
  - Session Initiation Protocol (SIP): Manages multimedia communication sessions (ports 5060/5061).
- Internet Protocol (IP) types
  - Internet Protocol (IP): Principal protocol for routing and addressing
    packets.
  - Internet Control Message Protocol (ICMP): Reports network errors and
    diagnostic information.
- Transmission Control Protocol (TCP): Reliable, connection-oriented data delivery protocol.
  - Three-Way Handshake: SYN, SYN-ACK, ACK process establishing connections. <!-- newly added -->
  - TCP Flags: Control bits identifying segment purpose and state. <!-- newly added -->
    - SYN: Synchronizes sequence numbers to initiate connections. <!-- newly added -->
    - ACK: Acknowledges successful receipt of data packets. <!-- newly added -->
    - FIN: Gracefully terminates an established virtual connection. <!-- newly added -->
    - RST: Abruptly resets a connection due to errors. <!-- newly added -->
    - PSH: Forces buffer data to be sent immediately. <!-- newly added -->
    - URG: Identifies segment data as requiring urgent processing. <!-- newly added -->
- User Datagram Protocol (UDP): Fast, connectionless, best-effort data transmission protocol.
- ...
  - Generic Routing Encapsulation (GRE): Encapsulates various network protocols
    within virtual tunnels.
  - Internet Protocol Security (IPsec): Suite ensuring IP packet confidentiality
    and integrity.
    - Authentication Header (AH): Verifies sender identity and data integrity.
    - Encapsulating Security Payload (ESP): Provides encryption, authentication,
      and data integrity.
    - Internet Key Exchange (IKE): Negotiates security keys and associations
      automatically.
  - Address Resolution Protocol (ARP): Resolves IP addresses to MAC hardware
    addresses.
- Traffic Types: Categories of data flow across a network.
  - Unicast: One-to-one communication between single sender and receiver.
  - Multicast: One-to-many communication to a subscribed group.
- Anycast: One-to-nearest communication within a group of nodes.
  - Broadcast: One-to-all communication on a network segment.
  - Unknown Unicast: Sent to unknown MAC address; treated like broadcast. <!-- newly added -->

Header Fields <!-- newly added -->
- IP Header: Contains version, length, and source/destination addresses. <!-- newly added -->
- Ethernet Header: Contains MAC addresses and EtherType field. <!-- newly added -->
- EtherType: Indicates the protocol encapsulated in frame payload. <!-- newly added -->

### 1.5 Compare and contrast transmission media and transceivers.

- Wireless: Data transmission via electromagnetic radio frequencies.
  - 802.11 Standards: Wireless networking standards utilizing radio
    transmission.
  - Cellular: Wireless data transmission via mobile phone networks.
  - Satellite: Internet access via orbiting relay stations.
- Wired: Data transmission through physical cables and wires.
  - Bit Representation <!-- newly added -->
    - Voltage: Electrical levels representing bits on copper wire. <!-- newly added -->
    - Light: Pulses representing bits on fiber optic cable. <!-- newly added -->
  - 802.3 Standards: IEEE standards defining wired Ethernet specifications.
  - Wiring Standards <!-- newly added -->
    - T568A: Legacy wiring standard for RJ45 connectors. <!-- newly added -->
    - T568B: Modern, common wiring standard for network cables. <!-- newly added -->
    - Straight-Through: Both cable ends use the same standard. <!-- newly added -->
    - Crossover: Cable ends use different standards (A and B). <!-- newly added -->
  - Single-Mode Fiber (SMF): Fiber carrying single light path long distance.
- ...
    - Uses lasers for high-speed, long-distance communication. <!-- newly added -->
  - Multimode Fiber (MMF): Fiber cable carrying multiple light paths.
    - Cheaper termination for shorter distances and high bandwidth. <!-- newly added -->
  - Direct Attach Copper (DAC): Copper cable with integrated transceivers.
  - Twinaxial Cable: Copper cable with two inner conductors.
- Coaxial Cable: Cable with inner conductor and outer shield.
    - Widely used for cable television and LANs. <!-- newly added -->
- Copper Cabling Categories <!-- newly added -->
  - Cat 5e: Supports speeds up to 1 Gbps. <!-- newly added -->
  - Cat 6: Supports 10 Gbps for short distances. <!-- newly added -->
  - Cat 6a: Improved for 10 Gbps over longer distances. <!-- newly added -->
  - Cat 7/8: Highly shielded cables for high-speed data centers. <!-- newly added -->
- Twisted Pair: Copper wires twisted to reduce electromagnetic interference. <!-- newly added -->
- ...
- Transceivers: Devices that both transmit and receive signals.
  - Protocol: Rules for physical data encoding and transmission.
    - Fiber Channel (FC): High-speed network technology for storage networking.
  - Form Factors: Standardized physical dimensions and module shapes.
    - Gigabit Interface Converter (GBIC): Original hot-swappable gigabit interface module. <!-- newly added -->
    - Small Form-Factor Pluggable (SFP): Compact optical transceiver module supporting 1Gbps.
    - SFP+: Enhanced SFP supporting data rates up to 10Gbps. <!-- newly added -->
    - Quad Small Form-Factor Pluggable (QSFP): High-speed fiber transceiver supporting 4 channels.
    - QSFP+: Enhanced QSFP supporting 40Gbps and higher. <!-- newly added -->
    - Bi-Directional (BiDi) Transceiver: Sends and receives over single fiber strand. <!-- newly added -->
- Media Converter: Changes signals from one media to another. <!-- newly added -->
- Connector Types: Physical interfaces used for joining network cables.
  - Subscriber Connector (SC): Push-pull square fiber optic connector.
  - Local Connector (LC): Small form-factor fiber optic connector.
  - Straight Tip (ST): Bayonet-style twist-and-lock fiber connector.
  - Multi-Fiber Push On (MPO): Fiber connector terminating multiple strands.
  - Registered Jack (RJ): Standard connector interface for telecommunications.
  - RJ11: Six-conductor connector primarily used for telephones.
  - RJ45: Standard eight-pin connector for twisted pair Ethernet.
  - F-Type Connector: Screw-on connector for coaxial cable.
  - Bayonet Neill-Concelman (BNC): Twist-lock connector for coaxial cables.
  - Ultra Physical Contact (UPC): Fiber connector polish with rounded surface.
  - Angled Physical Contact (APC): Fiber connector polish with angled surface.

### 1.6 Compare and contrast network topologies, architectures, and types.

- Mesh Topology: Network where nodes connect to multiple others.
  - Formula: n(n-1)/2 links for full mesh connectivity. <!-- newly added -->
- Hybrid Topology: Network mixing multiple topology types.
- Star/Hub and Spoke: Nodes connecting to a central device.
  - Advantage: Central point allows easy fault isolation. <!-- newly added -->
- Spine and Leaf: Datacenter topology reducing latency between servers.
- Point-to-Point: Direct connection between two nodes.
  - Bandwidth: Guaranteed level as only two devices share. <!-- newly added -->
- Bus Topology: All nodes connected to a common medium. <!-- newly added -->
- Ring Topology: Each node connected to exactly two others. <!-- newly added -->
- Tree Topology: Nodes arranged hierarchically like a branching structure. <!-- newly added -->

Topology Definitions <!-- newly added -->
- Physical Topology: Actual physical placement of nodes and cables. <!-- newly added -->
- Logical Topology: How data flows through the network layout. <!-- newly added -->

Three-Tier Hierarchical Model: Design separating Core, Distribution, and Access.
- ...
- Network Types: Categorization of networks based on geographic scale.
  - Local Area Network (LAN): Network within a limited geographic area.
    - SOHO: Small office or home office network. <!-- newly added -->
    - SME: Network supporting dozens of organizational users. <!-- newly added -->
    - Enterprise LAN: Hundreds or thousands of connected user devices. <!-- newly added -->
  - Wide Area Network (WAN): Network spanning large geographic distances.
  - Metropolitan Area Network (MAN): Network spanning a city or campus.
  - Campus Area Network (CAN): Network connecting multiple buildings in an organization. <!-- newly added -->
  - Personal Area Network (PAN): Very short range network (Bluetooth).
- WAN Technologies <!-- newly added -->
- ...

### 1.7 Given a scenario, use appropriate IPv4 network addressing.

IPv6 Differences <!-- newly added -->
- Address Size: 128-bit format allowing vast unique addresses. <!-- newly added -->
- Address Format: Written in hexadecimal and colon-separated notation. <!-- newly added -->
- Built-in Security: Mandatory support for IPsec protocol suite. <!-- newly added -->
- No NAT Needed: Sufficient addresses for all global devices. <!-- newly added -->
- SLAAC: Built-in autoconfiguration for IPv6 network hosts. <!-- newly added -->

- Public vs. Private: Globally routable versus internal-only IP addresses.
  - Automatic Private IP Addressing (APIPA): Self-assigned fallback IP when DHCP
    fails.
  - RFC 1918: Standard defining private, non-routable IP ranges.
    - 10.0.0.0 - 10.255.255.255: Private Class A network range. <!-- newly added -->
    - 172.16.0.0 - 172.31.255.255: Private Class B network range. <!-- newly added -->
    - 192.168.0.0 - 192.168.255.255: Private Class C network range. <!-- newly added -->
  - Loopback: IP directing traffic to the local host.
    - 127.0.0.0 - 127.255.255.255: Loopback address range for testing. <!-- newly added -->
  - Localhost: Standard hostname referring to the local computer.
- Subnetting: Dividing a network into smaller logical segments.
  - Variable Length Subnet Mask (VLSM): Subnetting using different mask lengths
    efficiently.
  - Classless Inter-Domain Routing (CIDR): Flexible IP addressing using prefix
    notation.
    - /XX Notation: Representing subnet masks using bit counts. <!-- newly added -->
  - Decimal to Binary: Reference for converting subnet masks. <!-- newly added -->
    - 255 - 1111 1111: All bits set to one. <!-- newly added -->
    - 254 - 1111 1110: Seven ones followed by zero. <!-- newly added -->
    - 252 - 1111 1100: Six ones followed by zeros. <!-- newly added -->
    - 248 - 1111 1000: Five ones followed by zeros. <!-- newly added -->
    - 240 - 1111 0000: Four ones followed by zeros. <!-- newly added -->
    - 224 - 1110 0000: Three ones followed by zeros. <!-- newly added -->
    - 192 - 1100 0000: Two ones followed by zeros. <!-- newly added -->
    - 128 - 1000 0000: One one followed by zeros. <!-- newly added -->
    - 0 - 0000 0000: All bits set to zero. <!-- newly added -->
  - Subnets: List of CIDR notations and counts. <!-- newly added --> <!-- should delete -->
    - /32: 1 IP (Single Host). <!-- newly added -->
    - /31: 2 IPs (Point-to-Point). <!-- newly added -->
    - /30: 4 IPs (2 Usable). <!-- newly added -->
    - /29: 8 IPs (6 Usable). <!-- newly added -->
    - /28: 16 IPs (14 Usable). <!-- newly added -->
    - /27: 32 IPs (30 Usable). <!-- newly added -->
    - /26: 64 IPs (62 Usable). <!-- newly added -->
    - /25: 128 IPs (126 Usable). <!-- newly added -->
    - /24: 256 IPs (254 Usable). <!-- newly added -->
    - /23: 512 IPs. <!-- newly added -->
    - /22: 1,024 IPs. <!-- newly added -->
    - /21: 2,048 IPs. <!-- newly added -->
    - /20: 4,096 IPs. <!-- newly added -->
    - /19: 8,192 IPs. <!-- newly added -->
    - /18: 16,384 IPs. <!-- newly added -->
    - /17: 32,768 IPs. <!-- newly added -->
    - /16: 65,536 IPs. <!-- newly added -->
    - /8: 16,777,216 IPs. <!-- newly added -->
- IPv4 Address Classes: Hierarchical system for IP address allocation.
  - Class A: Large network block (1.0.0.0 to 126.x.x.x).
    - Range: 0.0.0.0 - 127.255.255.255. <!-- newly added -->
  - Class B: Medium network block (128.0.0.0 to 191.x.x.x).
    - Range: 128.0.0.0 - 191.255.255.255. <!-- newly added -->
  - Class C: Small network block (192.0.0.0 to 223.x.x.x).
    - Range: 192.0.0.0 - 223.255.255.255. <!-- newly added -->
  - Class D: Address range reserved for multicast traffic.
    - Range: 224.0.0.0 - 239.255.255.255. <!-- newly added -->
  - Class E: IP address range reserved for experimental use.
    - Range: 240.0.0.0 - 255.255.255.255. <!-- newly added -->

### 1.8 Summarize evolving use cases for modern network environments.

- Software-Defined Network (SDN) and Software-Defined Wide Area Network (SD-WAN)
  - Software-Defined Network (SDN): Centralized software control of network
    hardware.
    - OpenFlow: Protocol for communication between SDN controller and plane. <!-- newly added -->
  - Software-Defined Wide Area Network (SD-WAN): Software-based management of
    WAN connections.
  - Applications aware: Traffic routing based on application type.
  - Zero-Touch Provisioning (ZTP): Automated device setup without manual
    intervention.
  - Transport agnostic: Operating across any underlying communication medium.
  - Central policy management: Unified control of network configurations and
    rules.
- Virtual Extensible LAN (VXLAN): Tunneling protocol extending VLANs over
  Layer 3.
  - Data Center Interconnect (DCI): Technologies connecting two or more
    datacenters.
  - Layer 2 Encapsulation: Wrapping Layer 2 frames within another protocol.
- Zero Trust Architecture (ZTA): Security model verifying every access request.
  - Policy-based authentication: Access granted based on defined security
    policies.
  - Authorization: Process of granting specific permissions to users.
  - Least Privilege Access: Granting minimum necessary access rights for tasks.
- Secure Access Service Edge (SASE)/Security Service Edge (SSE)
  - Secure Access Service Edge (SASE): Converging WAN and security into cloud
    services.
  - Security Service Edge (SSE): Security component of SASE architecture.
    - Cloud Access Security Broker (CASB): Enforcing security policies for cloud applications. <!-- newly added -->
    - Secure Web Gateway (SWG): Filtering web traffic to protect against threats. <!-- newly added -->
    - Zero Trust Network Access (ZTNA): Secure access to applications based on identity. <!-- newly added -->
- Infrastructure as Code (IaC): Managing infrastructure via machine-readable
  definition files.
  - Automation: Scripting tasks to reduce manual intervention.
    - Terraform: Tool for building, changing, and versioning infrastructure. <!-- newly added -->
    - Ansible: Tool for software provisioning and configuration management. <!-- newly added -->
    - Playbooks: Automated scripts for orchestrating configuration tasks.
    - Templates: Standardized files used for consistent device deployment.
    - Reusable Tasks: Modular automation components used across multiple playbooks.
    - Upgrades: Installing newer software or firmware versions.
    - Configuration Drift: Systems deviating from baseline settings over time.
    - Dynamic Inventories: Automatically updated lists of managed network hosts.
  - Source Control: System for tracking and managing code changes.
    - Version Control: Management of multiple iterations of configuration files.
    - Central Repository: Master storage location for all project files.
    - Conflict Identification: Detecting overlapping changes in shared files.
    - Branching: Creating parallel versions of code for development.
- IPv6 Addressing: 128-bit addressing system replacing IPv4.
  - Mitigating address exhaustion: Solving the limited supply of IP addresses.
  - Compatibility requirements
    - Tunneling: Encapsulating one protocol within another for transmission.
    - Dual Stack: Running IPv4 and IPv6 simultaneously on devices.
    - NAT64: Protocol allowing IPv6-only clients to access IPv4.

## 2.0 Network Implementation 20%

### 2.1 Explain characteristics of routing technologies.

Static Routing: Manually configured routing entries by an administrator.

Dynamic Routing: Routers automatically exchanging path information.

    - Border Gateway Protocol (BGP): Protocol routing between internet autonomous systems.
      - Path-Vector: Routing protocol maintaining path information to destination. <!-- newly added -->
    - Enhanced Interior Gateway Routing Protocol (EIGRP): Cisco protocol using bandwidth and delay metrics.
      - Hybrid: Combining distance-vector and link-state routing features. <!-- newly added -->
    - Open Shortest Path First (OSPF): Link-state routing protocol using Dijkstra's algorithm.
      - Link-State: Building complete topology map for routing decisions. <!-- newly added -->
    - Distance-Vector: Sharing entire routing table with neighbors. <!-- newly added -->

Route Selection: Process of determining the best network path.

    - Administrative Distance: Metric rating trustworthiness of routing sources.
    - Prefix Length: Number of bits set in subnet mask.
    - Metric: Value used by routing protocols to determine best path.

Address Translation: Mapping one IP address space into another.

    - Network Address Translation (NAT): Modifying IP addresses in packet headers.
    - Port Address Translation (PAT): Sharing one public IP via multiple ports.

First Hop Redundancy Protocol (FHRP): Provides failover for default gateways.

Virtual IP (VIP): Shared IP address for cluster failover.

Subinterfaces: Logical interfaces created on a single physical interface.

Routing Information Protocol (RIP): Distance-vector routing protocol using hop
count.

### 2.2 Given a scenario, configure switching technologies and features

Virtual Local Area Network (VLAN): Logical network segment on physical switch.

    - VLAN Database: Storage file containing VLAN configuration information.
    - Switch Virtual Interface (SVI): Logical Layer 3 interface on a switch.

Interface Configuration: Settings applied to individual physical or logical ports.

    - Native VLAN: VLAN for untagged traffic on trunk ports.
    - Voice VLAN: VLAN dedicated to carrying real-time voice traffic.
    - 802.1Q Tagging: Protocol tagging frames for VLAN identification.
    - Link Aggregation: Combining ports to increase bandwidth.
        - Link Aggregation Control Protocol (LACP): Protocol for bundling ports into single channels.
    - Speed: Data rate setting for a network interface.
    - Duplex: Communication mode setting (half or full) for port.

Spanning Tree Protocol (STP): Protocol preventing Layer 2 loops.

- Bridge Protocol Data Unit (BPDU): Messages exchanged by switches for STP. <!-- newly added -->

- BPDU Guard: Shuts down port on unexpected BPDU reception. <!-- newly added -->

- PortFast: Immediately transitions access port to forwarding state. <!-- newly added -->

- Rapid Spanning Tree Protocol (RSTP): Faster convergence version of Spanning Tree Protocol.



Switching Methods <!-- newly added -->

- Cut-Through: Starts forwarding before receiving full frame. <!-- newly added -->

- Store-and-Forward: Waits for full frame before forwarding. <!-- newly added -->



Maximum Transmission Unit (MTU): Largest data packet size supported by interface.



- Jumbo Frames: Ethernet frames larger than standard 1500 bytes.



Switch Stacking: Multiple physical switches acting as one unit. <!-- newly added -->

- 802.3af (PoE): Provides up to 15.4W per port. <!-- newly added -->

- 802.3at (PoE+): Provides up to 25.5W per port. <!-- newly added -->

- 802.3bt (PoE++): Provides up to 90W per port. <!-- newly added -->

### 2.3 Given a scenario, select and configure wireless devices and technologies

Channels: Specific frequency ranges for wireless communication.

- Channel Width: Frequency range used for data transmission.
- Non-Overlapping Channels: Adjacent channels that do not interfere.
- Regulatory Impacts: Legal restrictions on wireless frequency usage.
- 802.11h: Wi-Fi amendment preventing interference with radar.
  - Dynamic Frequency Selection (DFS): Automatically chooses less congested channels. <!-- newly added -->
  - Transmit Power Control (TPC): Reduces interference by limiting wireless power. <!-- newly added -->
- Wireless Technologies <!-- newly added -->
  - MIMO: Multiple input, multiple output for increased throughput. <!-- newly added -->
  - MU-MIMO: Serving multiple wireless users simultaneously. <!-- newly added -->
  - OFDMA: Efficient frequency allocation for multiple simultaneous users. <!-- newly added -->
  - BSS Coloring: Reducing interference in high-density wireless networks. <!-- newly added -->
- Service Set Identifier (SSID): Name identifying a wireless network.

- Basic Service Set Identifier (BSSID): MAC address of a wireless access point.
- Extended Service Set Identifier (ESSID): Network name across multiple access
  points.

Network Types: Different configurations for wireless network connectivity.

- Mesh Networks: Wireless nodes acting as repeaters.
- Ad Hoc: Peer-to-peer wireless network without central infrastructure.
- Point-to-Point: Direct wireless connection between two specific nodes.
- Infrastructure: Wireless network managed by central access points.

Encryption: Scrambling wireless data to ensure privacy.

- Wi-Fi Protected Access 2 (WPA2): Wi-Fi security standard using AES encryption.
- Wi-Fi Protected Access 3 (WPA3): Latest Wi-Fi security with improved
  encryption.
- Wi-Fi Protected Access (WPA): Security standard for wireless networks.
- Wi-Fi Protected Setup (WPS): Insecure simplified wireless connection method.

Guest Networks: Isolated wireless segments for temporary users.

- Captive Portal: Webpage requiring interaction before network access.

Authentication: Verifying identity of wireless clients before access.

- Pre-Shared vs. Enterprise: Personal password versus centralized server
  authentication.
- Pre-Shared Key (PSK): Password shared by all users for access.
- Enterprise: Centralized authentication using a RADIUS server.

Antennas: Devices for transmitting and receiving radio waves.

- Omnidirectional vs. Directional: Signal in all directions versus focused path.
- Omnidirectional Antenna: Antenna radiating signal in all directions equally.
- Directional: Antenna focusing radio signals in one direction.

Wireless Standards <!-- newly added -->
- 802.11a: 5GHz band, up to 54Mbps. <!-- newly added -->
- 802.11b: 2.4GHz band, up to 11Mbps. <!-- newly added -->
- 802.11g: 2.4GHz band, up to 54Mbps. <!-- newly added -->
- 802.11n: 2.4/5GHz bands, up to 600Mbps (MIMO). <!-- newly added -->
- 802.11ac: 5GHz band, up to 1+ Gbps (MU-MIMO). <!-- newly added -->
- 802.11ax: 2.4/5/6GHz bands, up to 10+ Gbps (Wi-Fi 6). <!-- newly added -->

Autonomous vs. Lightweight Access Point: Standalone management versus
controller-based management. 
- Autonomous: Standalone access point managing its own configuration. 
- Lightweight Access Point: Controller-managed access point with minimal local logic.

### 2.4 Explain important factors of physical installations

Important Installation Implications: Physical considerations for deploying network equipment.

- Customer Premises Equipment (CPE): Equipment located at the subscriber's physical site. <!-- newly added -->
- Local Loop: Cabling from customer site to local exchange. <!-- newly added -->
- Demarcation Point (Demarc): Where service provider cabling enters customer premises. <!-- newly added -->
- Locations: Physical sites where network hardware is installed.
  - Intermediate Distribution Frame (IDF): Cable rack connecting end devices to
    MDF.
  - Main Distribution Frame (MDF): Central point for network cabling
    termination.
- Rack Size: Standardized width and height units (U).
- Port-Side Exhaust/Intake: Managing airflow direction through rack equipment.
- Cabling: Physical wiring used to interconnect network devices.
  - Patch Panel: Hardware assembly for organizing cable connections.
  - Fiber Distribution Panel: Specialized enclosure for terminating fiber optic
    cables.
- Lockable: Physical security feature for equipment racks.

Power: Electrical requirements for operating network infrastructure.

- Uninterruptible Power Supply (UPS): Battery backup for power outages.
- Power Distribution Unit (PDU): Device distributing electric power to rack
  equipment.
- Power Load: Total electrical demand of connected network devices.
- Voltage: Potential difference measured between two points.

Environment Factors: Physical conditions affecting network equipment performance.

- Humidity: Amount of water vapor present in air.
- Fire Suppression: Automated systems for extinguishing data center fires.
- Temperature: Level of heat maintained in server rooms.

## 3.0 Network Operations 19%

### 3.1 Explain the purpose of organizational processes and procedures

Documentation: Records describing network architecture and operational policies.

- Physical vs. Logical Diagrams: Hardware layout versus data flow
  representation.
- Physical Diagrams: Visual representation of hardware and cable locations.
- Logical Diagrams: Visual representation of data flow and addressing.
- Rack Diagrams: Visual layout of equipment within server racks.
- Cable Maps and Diagrams: Schematic of physical cable paths and terminations.
- Network Diagrams: Visual representations of network infrastructure and connectivity.
  - Layer 1: Physical connectivity and hardware components diagram.
  - Layer 2: Data link layer and VLAN structure diagram.
  - Layer 3: Logical addressing and IP routing path diagram.
- Asset Inventory: Detailed list of hardware, software, and licenses.
  - Hardware: Physical components and devices in the network.
  - Software: Operating systems and applications used on devices.
  - Licensing: Legal permissions required to use software products.
  - Warranty Support: Manufacturer service coverage for hardware failures.
  - Acceptable Use Policy (AUP): Policy defining acceptable use of organization
    resources.
- IP Address Management (IPAM): Software tracking IP address allocation
  network-wide.
- Service-Level Agreement (SLA): Contract defining expected service performance
  standards.
- Wireless Survey: Assessing radio frequency coverage and performance.
  - Wireless Heat Map: Visualizing wireless signal strength and coverage.

Life-Cycle Management: Process of managing hardware and software stages.

- End-of-Life (EOL): Vendor stops selling or marketing a product.
- End-of-Support (EOS): Vendor stops providing updates or technical assistance.
- Software Management: Overseeing software updates, versions, and configurations.
  - Patches and Bug Fixes: Small updates addressing specific software issues.
  - Operating System (OS): Primary software managing hardware and other
    applications.
  - Firmware: Low-level software controlling specific hardware components.
- Decommissioning: Removing assets from service and secure disposal.

Change Management: Formal process for approving system modifications.

- Request Process Tracking/Service Request: Method for documenting and managing
  change requests.

Configuration Management: Maintaining consistent settings across all network devices.

- Production Configuration: Current settings used on active network devices.
- Backup Configuration: Saved settings for restoring devices after failure.
- Baseline/Golden Configuration: Standardized template for consistent device
  deployment.

### 3.2 Given a scenario, use network monitoring technologies

Methods: Techniques used to collect network performance data.

- Simple Network Management Protocol (SNMP): Protocol monitoring and managing
  network devices.
  - Trap (SNMP): Unsolicited alert sent by device to manager.
    - Management Information Base (MIB): Database of variables managed by SNMP.
      - Versions: Different iterations of the SNMP protocol.
        - v2c: Version using community strings for authentication.
        - v3: Version adding encryption and robust authentication.
    - Community Strings: Passwords used for authenticating SNMP v1/v2c.
    - Authentication: Verification of device identity for secure management.
- Flow Data: Statistics on network traffic patterns (NetFlow).
- Packet Capture: Intercepting and logging data packets for analysis.
- Baseline Metrics: Historical data representing normal network performance
  levels.
  - Anomaly Alerting/Notification: Triggering warnings when traffic deviates
    from baseline.
- Log Aggregation: Consolidating log data from multiple network sources.
  - Syslog Collector: Server gathering log messages from network devices.
  - Security Information and Event Management (SIEM): Real-time analysis of
    security logs and alerts.
- Port Mirroring: Copying switch traffic to a monitoring port.

Solutions: Specific tools or software for network monitoring.

- Network Discovery: Identifying devices present on a network.
  - Ad Hoc: Spontaneous network scanning for device identification.
  - Scheduled: Regularly timed scans for inventorying network devices.
- Traffic Analysis: Examining data flow to identify performance issues.
- Performance Monitoring: Tracking system health and resource utilization.
- Availability Monitoring: Checking uptime status of network devices.
- Configuration Monitoring: Detecting changes in device setting files.

Simple Network Management Protocol (SNMP): Protocol monitoring and managing
network devices.

### 3.3 Explain disaster recovery (DR) concepts

DR Metrics: Measurements used to evaluate disaster recovery readiness.

- Recovery Point Objective (RPO): Maximum tolerable data loss following a
  disaster.
- Recovery Time Objective (RTO): Maximum time allowed to restore services.
- Mean Time to Repair (MTTR): Average time to fix a failed device.
- Mean Time Between Failures (MTBF): Average time before a component fails.

DR Sites: Locations used for recovering data and operations.

- Disaster Recovery (DR): Procedures for restoring systems after failure.
- Cold Site: Empty backup facility requiring equipment setup.
- Warm Site: Partially equipped backup site, not fully active.
- Hot Site: Fully operational backup site ready immediately.

Backup Types <!-- newly added -->
- Full Backup: Backing up entire data set. <!-- newly added -->
- Incremental Backup: Saving changes since last backup. <!-- newly added -->
- Differential Backup: Saving changes since last full backup. <!-- newly added -->

High-Availability Approaches: Strategies for maintaining continuous network service availability.

- Active-Active: Redundant systems simultaneously handling network traffic.
- Active-Passive: Backup system waiting until primary system fails.

Testing: Assessing effectiveness of disaster recovery and availability.

- Tabletop Exercises: Theoretical drills to test disaster response plans.
- Validation Tests: Practical assessments confirming recovery procedures work.

### 3.4 Given a scenario, implement IPv4 and IPv6 network services

Dynamic Addressing: Automatic assignment of IP addresses to devices.

- Dynamic Host Configuration Protocol (DHCP): Automates IP address assignment to
  network clients.
  - Process: Discover, Offer, Request, Acknowledge (DORA). <!-- newly added -->
  - Reservations
    - DHCP Reservation: Permanently assigning specific IP to specific MAC.
  - Scope: Range of IP addresses available for distribution.
  - Lease Time: Duration a client can use assigned IP.
  - Options: Additional configuration data sent to DHCP clients.
  - Relay/IP Helper: Forwarding DHCP requests across different subnets.
  - Exclusions: Specific IP addresses within scope not distributed.
- Stateless Address Autoconfiguration (SLAAC): IPv6 hosts generating own
  addresses automatically.

Name Resolution: Process of translating hostnames into IP addresses.

- Domain Name System (DNS): Resolves domain names to IP addresses.
  - Domain Name System Security Extensions (DNSSEC): Cryptographic
    authentication for DNS records.
  - DNS over HTTPS (DoH) and DNS over TLS (DoT)
    - DNS over HTTPS (DoH): Encrypting DNS queries via HTTPS protocol.
    - DNS over TLS (DoT): Encrypting DNS queries via TLS protocol.
  - Record Types: Different categories of entries within DNS databases.
    - Address Record (A): DNS record mapping hostname to IPv4 address.
    - IPv6 Address Record (AAAA): DNS record mapping hostname to IPv6 address.
    - Canonical Name (CNAME): Alias mapping one hostname to another.
    - Mail Exchange (MX): Directs email to domain's mail server.
    - Text Record (TXT): DNS record holding arbitrary text information.
    - Name Server (NS): Designates authoritative name servers for domain.
    - Pointer Record (PTR): Maps IP address to hostname.
    - Zone Types: Classifications of DNS database segments and management.
      - Zone Transfer: Replicating DNS records between DNS servers.
      - Forward: Resolving hostnames to IP addresses.
      - Reverse: Resolving IP addresses to hostnames.
    - Authoritative: Master source containing the original DNS records.
    - Non-Authoritative: Cached DNS information obtained from other servers.
    - Primary: Original, read-write version of a zone file.
    - Secondary: Read-only copy of a zone file.
    - Recursive
      - Recursive Lookup: DNS server querying others to resolve name.
- Hosts File: Local text file mapping hostnames to IPs.

Time Protocols: Standards for synchronizing clocks across network devices.

- Network Time Protocol (NTP): Synchronizes clocks on network devices (port
  123).
- Precision Time Protocol (PTP): High-precision clock synchronization for local
  networks.
- Network Time Security (NTS): Secure mechanism for NTP time synchronization.

Start of Authority (SOA): DNS record identifying zone's authoritative source.

### 3.5 Compare and contrast network access and management methods

Site-to-Site VPN: Connecting two entire networks securely.

    - Virtual Private Network (VPN): Encrypted tunnel over a public network.
      - IPsec: Layer 3 protocol for secure site-to-site VPNs. <!-- newly added -->
      - SSL/TLS: Browser-based encryption for remote access. <!-- newly added -->
      - L2TP: Layer 2 tunneling protocol often combined with IPsec. <!-- newly added -->
      - GRE: Tunneling protocol encapsulating non-IP traffic. <!-- newly added -->

Client-to-Site VPN: Remote user connecting securely to corporate network.

- Clientless: VPN access without dedicated client software installation.
- Split Tunnel vs. Full Tunnel
  - Split Tunnel: Routing only specific traffic through VPN.
  - Full Tunnel: Routing all traffic through VPN gateway.

Connection Methods: Techniques used to access and manage devices.

- Secure Shell (SSH): Encrypted remote command-line access.
  - Remote Desktop Protocol (RDP): GUI-based remote access protocol for Windows.
- Graphical User Interface (GUI): Visual interface for interacting with
  electronic devices.
- Application Programming Interface (API): Code allowing software applications
  to communicate. <!-- Objective 1.4 -->
- Console: Physical port for direct local device management.

Jump Box/Host: Hardened intermediary for accessing sensitive zones.

In-Band vs. Out-of-Band Management: Managing via primary network or separate path.

- In-Band: Managing network devices through the production network.
- Out-of-Band Management: Admin traffic using dedicated, separate network path.
- Intranet: Private network accessible only to authorized users. <!-- newly added -->
- Extranet: Private network allowing limited access to partners. <!-- newly added -->
- Internet: Global system of interconnected computer networks. <!-- newly added -->
- Darknet: Anonymous overlay network accessible via specialized software. <!-- newly added -->

## 4.0 Network Security 14%

### 4.1 Explain the importance of basic network security concepts

Logical Security: Software and procedural measures protecting digital assets.

- Encryption: Scrambling data to prevent unauthorized access.
  - Data in Transit: Protecting data as it travels across networks.
  - Data at Rest: Protecting data stored on physical storage media.
  - End-to-End Encryption (E2EE): Continuous protection between communicating parties only. <!-- newly added -->
- Certificates: Digital documents verifying identity of network entities.
  - Public Key Infrastructure (PKI): Framework managing digital certificates and
    keys.
  - Self-Signed: Certificate signed by its creator rather than CA.
  - SSL/TLS: Protocols for secure authentication and encrypted sessions. <!-- newly added -->
- Identity and Access Management (IAM): Managing user identities and resource
  access.
  - Authentication: Verification of user identity for network access.
    - Multi-Factor Authentication (MFA): Authentication requiring two or more
      credential types.
    - Single Sign-On (SSO): Logging in once to access multiple systems.
    - Remote Authentication Dial-In User Service (RADIUS): Server handling
      authentication for network access.
    - Lightweight Directory Access Protocol (LDAP): Protocol for querying and
      managing directory services.
    - Security Assertion Markup Language (SAML): XML format exchanging
      authentication data.
    - Terminal Access Controller Access Control System Plus (TACACS+): Protocol
      for AAA services, typically device admin.
    - Time-based Authentication: Security tokens that change at regular
      intervals.
  - Authorization: Process of granting specific permissions to users.
    - Least Privilege: Granting only minimum necessary access rights.
    - Role-Based Access Control (RBAC): Access rights based on user job
      function.
- Geofencing: Creating virtual boundaries for geographic-based access control.

Physical Security: Tangible barriers protecting hardware and facility access.

- Camera: Visual surveillance device for monitoring physical areas.
- Locks: Physical mechanisms preventing unauthorized entry to facilities.

Deception Technologies: Tools luring attackers into decoy environments.

- Honeypot: Decoy system luring attackers to detect threats.
- Honeynet: Network of decoys simulating a real environment.

Common Security Terminology: Standard vocabulary used to describe security concepts.

- Risk: Probability of threat exploiting a vulnerability.
- Vulnerability: Security weakness susceptible to being exploited.
- Exploit: Method or code used to abuse vulnerability.
- Threat: Potential cause of an unwanted security incident.
- Confidentiality, Integrity, and Availability (CIA) Triad: Core security model
  for protecting information.

Audits and Regulatory Compliance: Verifying adherence to security policies and laws.

- Audits: Systematic evaluations of an organization's security posture.
- Regulatory Compliance: Meeting legal requirements for data protection.
- Data Locality: Requirement for data to stay in region.
- Payment Card Industry Data Security Standard (PCI DSS): Standards for securing
  credit card transactions.
- General Data Protection Regulation (GDPR): EU regulation protecting personal
  data and privacy.

Network Segmentation Enforcement: Using boundaries to isolate network traffic segments.

- Internet of Things (IoT) and Industrial Internet of Things (IIoT): Networked
  physical objects and industrial equipment.
- Supervisory Control and Data Acquisition (SCADA), Industrial Control System
  (ICS), Operational Technology (OT): Systems monitoring and controlling
  industrial infrastructure.
- Guest: Isolated network segment for temporary visitors.
- Bring Your Own Device (BYOD): Policy allowing personal devices on corporate
  networks.

### 4.2 Summarize various types of attacks and their impact to the network

Denial-of-Service (DoS)/Distributed Denial-of-Service (DDoS)

- Denial-of-Service (DoS): Attack preventing legitimate access to resources.
- Distributed Denial-of-Service (DDoS): DoS attack from multiple sources
  simultaneously.

VLAN Hopping: Attacking by moving between different VLANs illegally.

Media Access Control (MAC) Flooding: Overwhelming switch MAC tables with fake
addresses.

ARP Poisoning: Corrupting ARP cache to map attacker's MAC.

ARP Spoofing: Sending fake ARP messages to intercept traffic.

DNS Poisoning: Injecting fake DNS records to redirect traffic.

DNS Spoofing: Redirecting users to malicious sites via DNS.

Rogue Devices and Services: Unauthorized hardware or software on a network.

- Rogue Devices: Unauthorized hardware connected to a secure network.
- Services: Unauthorized software-based functions running on a network.
- DHCP: Unauthorized server distributing incorrect IP configurations.
- Access Point (AP): Hardware device providing wireless network connectivity.
  - Rogue Access Point: Unauthorized wireless access point on a network.

Evil Twin: Fake access point mimicking a legitimate one.

On-Path Attack: Intercepting communication between two legitimate network nodes.

Social Engineering Phishing: Fraudulent emails tricking users into revealing
info.

- Phishing: Deceptive emails aiming to steal sensitive information. <!-- newly added -->
- Spear Phishing: Targeted phishing attacks against specific individuals. <!-- newly added -->
- Whaling: Phishing attacks targeting high-profile executives. <!-- newly added -->
- Vishing: Phishing attacks conducted over voice calls. <!-- newly added -->
- Smishing: Phishing attacks using SMS text messages. <!-- newly added -->
- Pretexting: Creating a fabricated scenario to gain victim's trust. <!-- newly added -->
- Dumpster Diving: Searching through trash for sensitive information.
- Shoulder Surfing: Watching someone enter passwords or sensitive data.
- Tailgating: Following authorized personnel into restricted physical areas.

Malware: Malicious software designed to harm systems or data.
- Virus: Malware requiring a host file to spread. <!-- newly added -->
- Worm: Self-replicating malware spreading across networks independently. <!-- newly added -->
- Trojan: Malicious software disguised as a legitimate application. <!-- newly added -->
- Ransomware: Malware encrypting files and demanding payment. <!-- newly added -->
- Spyware: Software secretly collecting user information. <!-- newly added -->
- Rootkit: Malware designed to hide its presence on a system. <!-- newly added -->

### 4.3 Given a scenario, apply network security features, defense techniques, and solutions

Device Hardening: Securing a system by reducing attack surface.

- Disable Unused Ports and Services: Closing entry points to minimize security
  risks.
- Change Default Passwords: Replacing factory-set credentials with secure ones.

Network Access Control (NAC): Controlling device admission to the network.

- Port Security: Limiting network port access by MAC address.
- 802.1X: Port-based network access control and authentication.
- MAC Filtering: Allowing or denying network access by MAC.

Key Management: Secure handling and storage of cryptographic keys.

Security Rules: Definitions controlling traffic flow through security devices.

- Access Control List (ACL): Rules determining access rights to network
  resources. <!-- Objective 1.4 -->
- Uniform Resource Locator (URL) Filtering: Restricting website access based on
  web addresses.
- Content Filtering: Blocking access to specific types of data.
- Unified Threat Management (UTM): All-in-one security appliance for network
  protection.

Zones: Logical network areas with distinct security requirements.

- Trusted vs. Untrusted: Internal secure network versus external insecure
  network.
- Screened Subnet: Semi-public zone separating internet and internal LAN.

## 5.0 Network Troubleshooting 24%

### 5.1 Explain the troubleshooting methodology

Identify the Problem: Gather information, symptoms, and recent changes.

- Gather Information: Collecting all relevant data about the issue.
  - From users, logs, and alerts. <!-- newly added -->
- Question Users: Interviewing affected individuals to understand symptoms.
  - Ask: What changed? When did it start? <!-- newly added -->
  - Open Questions: Invite users to explain in their words. <!-- newly added -->
  - Closed Questions: Invite fixed responses like yes or no. <!-- newly added -->
  - Did it ever work? Establish if original setup worked. <!-- newly added -->
- Identify Symptoms: Determining specific signs of the network problem.
  - Define scope: one user, department, or entire network. <!-- newly added -->
- Determine if Anything Has Changed: Checking for recent configuration or
  hardware modifications.
- Duplicate the Problem, if possible: Replicating the issue in a controlled
  environment.
- Approach Multiple Problems Individually: Resolving each separate issue one at
  a time.

Establish a Theory of Probable Cause: Brainstorm probable causes starting with
the obvious.

- Question the Obvious: Checking for simple failures like disconnected cables.
- Consider Multiple Approaches: Evaluating different potential solutions to the
  problem.
  - Top-to-Bottom/Bottom-to-Top OSI Model: Systematically checking layers for
    potential points of failure.
  - Divide and Conquer: Narrowing down problem location by bisecting system.

Test the Theory to Determine the Cause: Confirm the cause or escalate if
incorrect.

- If theory is confirmed, determine next steps to resolve problem
  - Isolate variables to confirm root cause. <!-- newly added -->
- if theory is not confirmed, establish a new theory or escalate
  - Go back to establishing a theory. <!-- newly added -->

Establish a Plan of Action to resolve the problem and identify potential
effects: Determine steps to fix and assess impact.
- Implement fix with minimal disruption. <!-- newly added -->
- Schedule downtime if needed. <!-- newly added -->

Implement the Solution or escalate as necessary: Execute the fix or escalate if
needed.
- Follow change control procedures if required. <!-- newly added -->
- Use rollback plan if fix fails. <!-- newly added -->
- Escalation: Referring problems to senior staff or manufacturers. <!-- newly added -->

Verify Full System Functionality and implement preventive measures if
applicable: Confirm system works and prevent recurrence.
- Test full services and related systems. <!-- newly added -->
- Confirm resolution with the user. <!-- newly added -->

Document Findings, Actions, Outcomes, and Lessons Learned throughout the
process: Record actions, outcomes, and lessons learned.
- Record problem, resolution, and timeline. <!-- newly added -->
- Useful for audits, training, and trend tracking. <!-- newly added -->

### 5.2 Given a scenario, troubleshoot common cabling and physical interface issues

Cable Issues: Physical layer failures related to network wiring.

- Incorrect Cable: Using the wrong type of network cabling.
  - Single-Mode vs. Multimode: Long-distance fiber versus short-distance
    high-bandwidth fiber.
  - Category 5/6/7/8: Various Ethernet cabling standards for different speeds.
  - Shielded Twisted Pair (STP) vs. Unshielded Twisted Pair (UTP): Protected
    versus standard copper network cabling.
- Signal Degradation: Reduction in signal quality during transmission.
  - Crosstalk: Signal bleeding between adjacent copper wires.
  - Interference: External signals disrupting network transmission (EMI/RFI).
  - Attenuation: Loss of signal strength over distance.
- Improper Termination: Poorly attached connectors causing physical layer
  failures.
- Transmitter (TX)/Receiver (RX) Transposed: Sending and receiving wires swapped
  incorrectly.

Interface Issues: Failures occurring at the device connection point.

- Increasing Interface Counters: Statistics tracking errors on a specific port.
  - Cyclic Redundancy Check (CRC): Error-detecting code indicating corrupted
    data frames.
  - Runts: Ethernet frames smaller than permitted minimum size.
  - Drops: Packets discarded due to congestion or errors.
- Port Status: The operational state of a network interface.
  - Error Disabled: Port shut down by switch due to errors.
  - Administratively Down: Port manually disabled by network administrator.
  - Suspended: Port inactive due to protocol negotiation failure.

Hardware Issues: Physical component failures within network devices.

- Power over Ethernet (PoE): Transmitting power over standard Ethernet cabling.
  - Power Budget Exceeded: Demanding more power than switch can provide.
  - Incorrect Standard: Mismatch between PoE device and switch requirements.
- Transceivers: Modular components for connecting to fiber networks.
  - Mismatch: Incompatible transceiver type or speed on link.
  - Signal Strength: Optical or electrical power level issues.

### 5.3 Given a scenario, troubleshoot common issues with network services

Switching Issues: Failures related to Layer 2 network operations.

- Spanning Tree Protocol (STP): Protocol preventing Layer 2 loops.
  - Network Loops: Traffic circulating endlessly between switches.
  - Root Bridge Selection: Electing the main switch in Spanning Tree.
  - Port Roles/States: Specific functional modes assigned to switch ports.
- Incorrect VLAN Assignment: Assigning a port to the wrong VLAN.
- Access Control List (ACL): Rules determining access rights to network
  resources.

Route Selection: Problems related to determining data packet paths.

- Routing Table: Database used for determining data packet paths.
- Default Routes: Path used when no specific destination exists.

Address Pool Exhaustion: No available IP addresses in DHCP scope.

Incorrect Default Gateway: Wrong IP address configured for local exit.

Incorrect IP Address: Invalid or misconfigured IP on a device.

- Duplicate IP Address: Two devices assigned same IP, causing conflict.

Incorrect Subnet Mask: Misconfigured mask leading to communication errors.

### 5.4 Given a scenario, troubleshoot common performance issues

Congestion/Contention: Network slowing due to high traffic volume.

Bottlenecking: Point of congestion limiting overall performance.

Bandwidth: Maximum data transfer rate of a network.

- Throughput: Actual data transfer rate supported by link.

Latency: Time delay for data to reach destination.
- Processing Delay: Time taken by routers to process headers. <!-- newly added -->
- Queuing Delay: Time spent waiting in network routing queues. <!-- newly added -->
- Transmission Delay: Time needed to push bits onto medium. <!-- newly added -->
- Propagation Delay: Time for signal to travel through medium. <!-- newly added -->

Packet Loss: Data units failing to reach their destination.
- Network Congestion: Deterioration of quality due to excessive load. <!-- newly added -->

Jitter: Variation in packet arrival time.

Wireless

- Interference: External signals disrupting wireless network communication.
  - Channel Overlap: Wireless frequencies interfering with each other.
- Signal Degradation or Loss: Reduction in wireless signal quality or strength.
- Insufficient Wireless Coverage: Dead zones where wireless signal is missing.
- Client Disassociation Issues: Devices repeatedly losing connection to access
  points.
- Roaming Misconfiguration: Failure of clients to switch between APs smoothly.

### 5.5 Given a scenario, use the appropriate tool or protocol to solve networking issues

Software Tools: Applications used for network analysis and troubleshooting.

- Protocol Analyzer: Tool decoding and displaying network traffic (Wireshark).
- Command Line
  - Ping: Tool checking network reachability via ICMP.
  - Traceroute: Tool showing path packets take to host.
  - Nslookup: Tool for querying DNS records to resolve names.
  - Tcpdump: Command-line packet analyzer for network traffic monitoring.
  - Dig: Domain Information Groper for querying DNS servers.
  - Netstat: Tool displaying active network connections and statistics.
  - IP/Ifconfig/Ipconfig: Tools displaying network interface configuration and
    addressing.
  - ARP: Tool for viewing and managing ARP cache.
- Nmap: Tool for network discovery and security scanning.
- Link Layer Discovery Protocol (LLDP)/Cisco Discovery Protocol (CDP): Protocols
  for discovering neighboring network devices.
- Speed Tester: Application measuring network bandwidth and latency.

Hardware Tools: Physical devices used for network testing and maintenance.

- Toner: Tool for tracing cables through walls and ceilings.
- Cable Tester: Device verifying continuity and wiring of cabling.
- Taps: Hardware used to intercept network traffic for monitoring.
- Wi-Fi Analyzer: Tool visualizing wireless signal strength and channels.
- Visual Fault Locator (VFL): Laser tool for finding breaks in fiber.

Basic Networking Device Commands

- Show MAC-Address-Table: Displays the switch's MAC address learning table.
- Show Route: Displays the current IP routing table entries.
- Show Interface: Displays status and statistics for network ports.
- Show Config: Displays the current running configuration of device.
- Show ARP: Displays the local address resolution protocol cache.
- Show VLAN: Displays configured virtual local area network information.
- Show Power: Displays power supply status and PoE usage.
