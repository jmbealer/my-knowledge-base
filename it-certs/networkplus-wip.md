# networkplus

## 1.0 Networking Concepts 23%

### 1.1 Explain concepts related to the Open Systems Interconnection (OSI) reference model.

Open Systems Interconnection (OSI): Standardized seven-layer framework for
network communication.

- Key Concepts: <!-- newly added -->
  - OSI Model - 7 Layers: Application, Presentation, Session, Transport, Network, Data Link, Physical. <!-- newly added -->
  - Encapsulation: Wrapping data with protocol headers (Down the stack). <!-- newly added -->
  - Decapsulation: Removing protocol headers (Up the stack). <!-- newly added -->
  - Mnemonics: "All People Seem To Need Data Processing" (App to Phy) / "Please Do Not Throw Sausage Pizza Away" (Phy to App). <!-- newly added -->

- Protocol Data Unit (PDU): Data block exchanged at specific protocol layers.
  - Segment: PDU at Transport layer (Layer 4). <!-- newly added -->
  - Packet: PDU at Network layer (Layer 3). <!-- newly added -->
  - Frame: PDU at Data Link layer (Layer 2). <!-- newly added -->
  - Bits: PDU at Physical layer (Layer 1). <!-- newly added -->
  - Data: PDU at Application, Presentation, Session layers (Layers 5-7). <!-- newly added -->

- Encapsulation: Packaging data with headers for transmission. <!-- newly added -->
- Decapsulation: Removing headers to extract data payload. <!-- newly added -->
  - Process: Layer 1 (Bits) -> Layer 2 (Frames) -> Layer 3 (Packets) -> Layer 4 (Segments) -> Layer 7 (Data). <!-- newly added -->
- Layer 1 - Physical: Transmits raw bits over physical medium.
  - Functions: Signaling, cabling, connectors, bit rate. <!-- newly added -->
  - Devices: Hubs, repeaters, network cables, modems. <!-- newly added -->
  - Troubleshooting: Fix cabling, punch-downs, loopback tests. <!-- newly added -->
- Layer 2 - Data Link: Node-to-node data transfer and error handling.
  - Sublayers: <!-- newly added -->
    - LLC (Logical Link Control): Flow control, error checking, protocols. <!-- newly added -->
    - MAC (Media Access Control): Hardware addressing, media access. <!-- newly added -->
  - Addressing: MAC Addresses (Physical, 48-bit hex). <!-- newly added -->
  - Devices: Switches, Bridges, NICs. <!-- newly added -->
  - Protocols: Ethernet, PPP, HDLC, Frame Relay. <!-- newly added -->
- Layer 3 - Network: Routing data packets between different networks.
  - Functions: Logical addressing (IP), Path selection (Routing), Packet forwarding. <!-- newly added -->
  - Devices: Routers, Layer 3 Switches. <!-- newly added -->
  - Protocols: IP (v4/v6), ICMP, OSPF, BGP, RIP. <!-- newly added -->
  - Switching Methods: Packet Switching, Circuit Switching. <!-- newly added -->
  - Connection Services: Flow control, Packet reordering. <!-- newly added -->
- Layer 4 - Transport: Reliable end-to-end data delivery and flow control.
  - Protocols: TCP (Reliable, Connection-oriented), UDP (Unreliable, Connectionless). <!-- newly added -->
  - Functions: Segmentation, Flow Control, Error Correction, Multiplexing. <!-- newly added -->
  - Mechanisms: Three-way handshake (SYN, SYN-ACK, ACK), Windowing, Buffering. <!-- newly added -->
  - Devices: Load Balancers, Firewalls (can operate here), WAN Accelerators. <!-- newly added -->
- Layer 5 - Session: Managing communication sessions between applications.
  - Functions: Connection establishment, maintenance, and teardown. <!-- newly added -->
  - Concepts: Dialog control (Simplex, Half-duplex, Full-duplex). <!-- newly added -->
  - Protocols: NetBIOS, RPC, H.323, RTP. <!-- newly added -->
- Layer 6 - Presentation: Data translation, encryption, and compression
  formatting.
  - Functions: Data formatting, Encryption/Decryption, Compression/Decompression. <!-- newly added -->
  - Standards: ASCII, Unicode, JPEG, MPEG, TLS, SSL. <!-- newly added -->
  - Concepts: Character encoding, Syntax negotiation. <!-- newly added -->
- Layer 7 - Application: Interface for end-user network processes.
  - Services: File transfers, Email, Web browsing, Network Management, Remote Access. <!-- newly added -->
  - Protocols: HTTP, FTP, SMTP, DNS, SNMP, Telnet, SSH, POP3, IMAP. <!-- newly added -->
  - Functions: Service advertisement, Application services, API access. <!-- newly added -->

### 1.2 Compare and contrast networking appliances, applications, and functions.

Physical: Hardware-based network components and devices. Virtual Appliances:
Software-based network functions running on hypervisors.

- Router: Forwards data packets between computer networks.
- Switch: Connects devices within a single network segment.
  - Layer 2 Switch: Forwards frames based on MAC addresses (creates collision domains). <!-- newly added -->
  - Layer 3 Switch: Performs routing functions using IP addresses (inter-VLAN routing). <!-- newly added -->
- Firewall: Security device filtering network traffic rules.
  - Packet Filtering: Inspects packet headers (stateless). <!-- newly added -->
  - Stateful Inspection: Tracks active connections and sessions. <!-- newly added -->
  - Next-Generation Firewall (NGFW): Deep packet inspection, application awareness. <!-- newly added -->
  - Web Application Firewall (WAF): Protects web apps from specific attacks (XSS, SQLi). <!-- newly added -->
  - Unified Threat Management (UTM): Combines multiple security features (AV, IDS/IPS, etc). <!-- newly added -->
- Intrusion Detection System (IDS): Monitors network traffic for suspicious
  activity.
  - Passive monitoring: Logs and alerts (signature or anomaly based). <!-- newly added -->
- Intrusion Prevention System (IPS): Detects and blocks malicious network
  activity.
  - Active protection: Drops packets or resets connections inline. <!-- newly added -->
- Load Balancer: Distributes network traffic across multiple servers.
  - Functions: SSL offloading, Caching, Compression, Health monitoring. <!-- newly added -->
  - Benefits: Scalability, Availability, Fault Tolerance. <!-- newly added -->
- Proxy: Intermediary server handling client requests.
  - Forward Proxy: Acting on behalf of internal clients accessing the internet (caching, filtering). <!-- newly added -->
  - Reverse Proxy: Acting on behalf of servers to handle external requests (load balancing, security). <!-- newly added -->
  - Transparent Proxy: Intercepts traffic without client configuration. <!-- newly added -->
- Network-Attached Storage (NAS): File-level storage connected to a network.
  - Protocols: SMB, NFS. <!-- newly added -->
- Storage Area Network (SAN): High-speed network for block-level storage access.
  - Protocols: Fibre Channel (FC), iSCSI, FCoE. <!-- newly added -->
  - Access: Block-level (appears as local disk). <!-- newly added -->
- Wireless: Communication using radio waves instead of cables.
  - Access Point (AP): Bridges wireless clients to wired network.
- Wireless Controller: Central management device for multiple access points.
- Hub: Layer 1 device repeating signals to all ports (creates single collision domain). <!-- newly added -->
- Repeater: Device amplifying signal to extend transmission distance.
- Media Converter: Device converting one media signaling type to another.
- Bridge: Device joining physical segments while minimizing collisions. <!-- newly added -->
- Customer Premises Equipment (CPE): Equipment at customer site connecting to WAN. <!-- newly added -->
- Demarcation Point (Demarc): Point where service provider responsibility ends. <!-- newly added -->

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
    - Private-Direct Connection: Dedicated line for secure, high-performance access. <!-- newly added -->
- Deployment Models: Different ways cloud services are hosted.
  - Public Cloud: Cloud resources shared by general public.
  - Private Cloud: Cloud infrastructure dedicated to single organization.
  - Hybrid Cloud: Environment combining public and private clouds.
  - Community Cloud: Shared infrastructure for specific community with common concerns. <!-- newly added -->
- Service Models: Categories of services provided by cloud vendors.
  - Software as a Service (SaaS): Software delivered over internet via
    subscription.
  - Infrastructure as a Service (IaaS): Virtualized computing resources over the
    internet.
  - Platform as a Service (PaaS): Platform for developing and deploying
    applications.
- Scalability: Ability to handle increasing workload growth.
- Elasticity: Automatically scaling resources up and down.
- Multitenancy: Single instance serving multiple distinct customers.
- Metered Utilization: Pay-per-use model for cloud services. <!-- newly added -->

### 1.4 Explain common networking ports, protocols, services, and traffic types.

- Protocols: Rules governing data exchange between network devices.
- Ports: Logical endpoints for identifying specific processes.
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
  - Post Office Protocol v3 (POP3): Retrieves emails from server (port 110). <!-- newly added -->
  - Internet Message Access Protocol (IMAP): Retrieves emails from server (port 143). <!-- newly added -->
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
  - IMAP over SSL (IMAPS): Secure email retrieval (port 993). <!-- newly added -->
  - POP3 over SSL (POP3S): Secure email retrieval (port 995). <!-- newly added -->
  - SQL Server: Microsoft database communication using port 1433.
  - MySQL: Database communication using port 3306. <!-- newly added -->
  - Remote Desktop Protocol (RDP): GUI-based remote access on port 3389.
  - Session Initiation Protocol (SIP): Manages multimedia communication sessions
    (ports 5060/5061).
- Internet Protocol (IP) types
  - Internet Protocol (IP): Principal protocol for routing and addressing
    packets.
  - Internet Control Message Protocol (ICMP): Reports network errors and
    diagnostic information.
  - Transmission Control Protocol (TCP): Reliable, connection-oriented data
    delivery protocol.
  - User Datagram Protocol (UDP): Fast, connectionless, best-effort data
    transmission protocol.
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

### 1.5 Compare and contrast transmission media and transceivers.

- Wireless: Data transmission via electromagnetic radio frequencies.
  - 802.11 Standards: Wireless networking standards utilizing radio
    transmission.
  - Cellular: Wireless data transmission via mobile phone networks.
  - Satellite: Internet access via orbiting relay stations.
- Wired: Data transmission through physical cables and wires.
  - 802.3 Standards: IEEE standards defining wired Ethernet specifications.
  - Single-Mode Fiber (SMF): Fiber carrying single light path long distance.
  - Multimode Fiber (MMF): Fiber cable carrying multiple light paths.
  - Direct Attach Copper (DAC): Copper cable with integrated transceivers.
  - Twinaxial Cable: Copper cable with two inner conductors.
  - Coaxial Cable: Cable with inner conductor and outer shield.
  - Plenum Cable: Fire-resistant cable for air handling spaces.
- Transceivers: Devices that both transmit and receive signals.
  - Protocol: Rules for physical data encoding and transmission.
    - Fiber Channel (FC): High-speed network technology for storage networking.
  - Form Factors: Standardized physical dimensions and module shapes.
    - Small Form-Factor Pluggable (SFP): Compact optical transceiver module
      supporting 1Gbps.
    - Enhanced Small Form-Factor Pluggable (SFP+): Supports 10Gbps. <!-- newly added -->
    - SFP28: Supports 25Gbps. <!-- newly added -->
    - Quad Small Form-Factor Pluggable (QSFP): High-speed fiber transceiver
      supporting 4 channels (up to 40Gbps). <!-- newly added -->
    - Enhanced Quad Small Form-Factor Pluggable (QSFP+): Supports 40Gbps or more. <!-- newly added -->
    - QSFP28: Supports 100Gbps. <!-- newly added -->
    - QSFP56: Supports 200Gbps. <!-- newly added -->
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
  - Ultra Physical Contact (UPC): Fiber connector polish with rounded surface (Low back reflection). <!-- newly added -->
  - Angled Physical Contact (APC): Fiber connector polish with angled surface (Lowest back reflection, 8-degree angle). <!-- newly added -->
  - Physical Contact (PC): Fiber connector polish with slight curvature (Least effective reduction in back reflection). <!-- newly added -->

### 1.6 Compare and contrast network topologies, architectures, and types.

- Mesh Topology: Network where nodes connect to multiple others.
  - Partial Mesh: Topology with only key devices interconnected for redundancy. <!-- newly added -->
- Hybrid Topology: Network mixing multiple topology types.
- Bus Topology: All nodes connect to a single backbone cable.
- Ring Topology: Nodes connected in a circular loop data path.
- Star/Hub and Spoke: Nodes connecting to a central device.
- Tree Topology: Nodes arranged hierarchically (star-of-stars). <!-- newly added -->
- Physical Topology: Physical layout of nodes and links. <!-- newly added -->
- Logical Topology: Flow of data paths through the network. <!-- newly added -->
- Overlay Network: Virtual network built on top of another network. <!-- newly added -->
- Spine and Leaf: Datacenter topology reducing latency between servers.
- Point-to-Point: Direct connection between two nodes.
- Three-Tier Hierarchical Model: Design separating Core, Distribution, and
  Access.
  - Core Layer: High-speed backbone of network hierarchy.
  - Distribution Layer: Layer connecting access switches to core.
  - Access Layer: Network hierarchy tier connecting end-user devices.
- Backbone Network: Infrastructure connecting different LANs or subnetworks. <!-- newly added -->
- Collapsed Core: Topology merging core and distribution layers.
- Traffic Flows: Patterns of data movement through a network.
  - North-South Traffic: Data flow entering or leaving datacenter.
    - Ingress: Inbound traffic entering a network. <!-- newly added -->
    - Egress: Outbound traffic leaving a network. <!-- newly added -->
  - East-West Traffic: Data flow between servers in datacenter.
- Network Types: Categorization of networks based on geographic scale.
  - Local Area Network (LAN): Network within a limited geographic area.
  - Home Area Network (HAN): Residential LAN for digital devices. <!-- newly added -->
  - Wide Area Network (WAN): Network spanning large geographic distances.
  - Campus Area Network (CAN): Network connecting multiple buildings in single organization. <!-- newly added -->
  - Personal Area Network (PAN): Very short range network (Bluetooth).
  - Metropolitan Area Network (MAN): Network spanning a city or campus.
  - Global Area Network (GAN): Network supporting mobile users across arbitrary areas. <!-- newly added -->
  - Intranet: Private network under control of single administrative entity. <!-- newly added -->
  - Extranet: Network allowing limited access to external users. <!-- newly added -->
  - Darknet: Overlay network accessible only via specialized software. <!-- newly added -->
### 1.7 Given a scenario, use appropriate IPv4 network addressing.

- Public vs. Private: Globally routable versus internal-only IP addresses.
  - Automatic Private IP Addressing (APIPA): Self-assigned fallback IP when DHCP
    fails.
  - RFC 1918: Standard defining private, non-routable IP ranges.
    - 10.0.0.0 - 10.255.255.255 <!-- newly added -->
    - 172.16.0.0 - 172.31.255.255 <!-- newly added -->
    - 192.168.0.0 - 192.168.255.255 <!-- newly added -->
  - Loopback: IP directing traffic to the local host.
  - Localhost: Standard hostname referring to the local computer.
    - 127.0.0.0 - 127.255.255.255 <!-- newly added -->
- Subnetting: Dividing a network into smaller logical segments.
  - Variable Length Subnet Mask (VLSM): Subnetting using different mask lengths
    efficiently.
  - Classless Inter-Domain Routing (CIDR): Flexible IP addressing using prefix
    notation.
- IPv4 Address Classes: Hierarchical system for IP address allocation.
  - Class A: Large network block (1.0.0.0 to 126.x.x.x).
  - Class B: Medium network block (128.0.0.0 to 191.x.x.x).
  - Class C: Small network block (192.0.0.0 to 223.x.x.x).
  - Class D: Address range reserved for multicast traffic.
  - Class E: IP address range reserved for experimental use.
- Subnet Mask Binary Values <!-- newly added -->
  - 255: 1111 1111 (Wildcard: 0) <!-- newly added -->
  - 254: 1111 1110 (Wildcard: 1) <!-- newly added -->
  - 252: 1111 1100 (Wildcard: 3) <!-- newly added -->
  - 248: 1111 1000 (Wildcard: 7) <!-- newly added -->
  - 240: 1111 0000 (Wildcard: 15) <!-- newly added -->
  - 224: 1110 0000 (Wildcard: 31) <!-- newly added -->
  - 192: 1100 0000 (Wildcard: 63) <!-- newly added -->
  - 128: 1000 0000 (Wildcard: 127) <!-- newly added -->
  - 0: 0000 0000 (Wildcard: 255) <!-- newly added -->
- CIDR Reference Table <!-- newly added -->
  - /32: 255.255.255.255 (1 Address) <!-- newly added -->
  - /31: 255.255.255.254 (2 Addresses) <!-- newly added -->
  - /30: 255.255.255.252 (4 Addresses) <!-- newly added -->
  - /29: 255.255.255.248 (8 Addresses) <!-- newly added -->
  - /28: 255.255.255.240 (16 Addresses) <!-- newly added -->
  - /27: 255.255.255.224 (32 Addresses) <!-- newly added -->
  - /26: 255.255.255.192 (64 Addresses) <!-- newly added -->
  - /25: 255.255.255.128 (128 Addresses) <!-- newly added -->
  - /24: 255.255.255.0 (256 Addresses) <!-- newly added -->
  - /23: 255.255.254.0 (512 Addresses) <!-- newly added -->
  - /22: 255.255.252.0 (1,024 Addresses) <!-- newly added -->
  - /21: 255.255.248.0 (2,048 Addresses) <!-- newly added -->
  - /20: 255.255.240.0 (4,096 Addresses) <!-- newly added -->
  - /19: 255.255.224.0 (8,192 Addresses) <!-- newly added -->
  - /18: 255.255.192.0 (16,384 Addresses) <!-- newly added -->
  - /17: 255.255.128.0 (32,768 Addresses) <!-- newly added -->
  - /16: 255.255.0.0 (65,536 Addresses) <!-- newly added -->
  - /15: 255.254.0.0 <!-- newly added -->
  - /14: 255.252.0.0 <!-- newly added -->
  - /13: 255.248.0.0 <!-- newly added -->
  - /12: 255.240.0.0 <!-- newly added -->
  - /11: 255.224.0.0 <!-- newly added -->
  - /10: 255.192.0.0 <!-- newly added -->
  - /9: 255.128.0.0 <!-- newly added -->
  - /8: 255.0.0.0 <!-- newly added -->
  - /7: 254.0.0.0 <!-- newly added -->
  - /6: 252.0.0.0 <!-- newly added -->
  - /5: 248.0.0.0 <!-- newly added -->
  - /4: 240.0.0.0 <!-- newly added -->
  - /3: 224.0.0.0 <!-- newly added -->
- Subnet Proportion <!-- newly added -->
  - ![](https://remnote-user-data.s3.amazonaws.com/5cObcolK37nPoJISPGQF50Gk6ismraDJaX7YCGibhxUPY_GJ5gQirHjKt8q3jKHOWoZBfZyz16a3C5e8nks3oxrJB2GVetACKIiXd-2KIYNZw1fInUDgzSa1I3bnMFP2.png) <!-- newly added -->


### 1.8 Summarize evolving use cases for modern network environments.

- Software-Defined Network (SDN) and Software-Defined Wide Area Network (SD-WAN)
  - Software-Defined Network (SDN): Centralized software control of network
    hardware.
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
  - "Never trust, always verify" <!-- newly added -->
  - Policy-based authentication: Access granted based on defined security
    policies.
  - Authorization: Process of granting specific permissions to users.
  - Least Privilege Access: Granting minimum necessary access rights for tasks.
- Secure Access Service Edge (SASE)/Security Service Edge (SSE)
  - Secure Access Service Edge (SASE): Converging WAN and security into cloud
    services.
    - Combines SD-WAN + cloud security <!-- newly added -->
  - Security Service Edge (SSE): Security component of SASE architecture.
    - Includes CASB, SWG, ZTNA <!-- newly added -->
- Infrastructure as Code (IaC): Managing infrastructure via machine-readable
  definition files.
  - Networks and infrastructure defined in version-controlled code <!-- newly added -->
  - Automation: Scripting tasks to reduce manual intervention.
    - Tools: Terraform, Ansible <!-- newly added -->
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
    - EUI-64: Method generating IPv6 interface ID from MAC address. <!-- newly added -->

## 2.0 Network Implementation 20%

### 2.1 Explain characteristics of routing technologies.

Static Routing: Manually configured routing entries by an administrator.

Dynamic Routing: Routers automatically exchanging path information.
  - Distance-Vector: Protocol sharing entire routing table (e.g., RIP). <!-- newly added -->
  - Link-State: Protocol building complete network topology map (e.g., OSPF). <!-- newly added -->
  - Hybrid: Protocol combining distance-vector and link-state features (e.g., EIGRP). <!-- newly added -->
  - Path-Vector: Protocol maintaining path information to destination (e.g., BGP). <!-- newly added -->
  - Convergence: Time taken for routers to agree on topology. <!-- newly added -->

    - Border Gateway Protocol (BGP): Protocol routing between internet autonomous systems.
    - Enhanced Interior Gateway Routing Protocol (EIGRP): Cisco protocol using bandwidth and delay metrics.
    - Open Shortest Path First (OSPF): Link-state routing protocol using Dijkstra's algorithm.

Route Selection: Process of determining the best network path.

    - Administrative Distance: Metric rating trustworthiness of routing sources.
    - Prefix Length: Number of bits set in subnet mask.
    - Metric: Value used by routing protocols to determine best path.
    - Split Horizon: Prevents router from sending updates back to source interface. <!-- newly added -->
    - Route Poisoning: Advertising a failed route with an infinite metric. <!-- newly added -->
    - Hold-Down Timer: Period to ignore route updates after failure to prevent flapping. <!-- newly added -->
    - Floating Static Route: Backup static route with higher administrative distance. <!-- newly added -->
    - Equal-Cost Multi-Path (ECMP): Routing traffic across multiple best paths simultaneously. <!-- newly added -->

Address Translation: Mapping one IP address space into another.

    - Network Address Translation (NAT): Modifying IP addresses in packet headers.
    - Port Address Translation (PAT): Sharing one public IP via multiple ports.

First Hop Redundancy Protocol (FHRP): Provides failover for default gateways.
  - Hot Standby Router Protocol (HSRP): Cisco proprietary active/standby failover. <!-- newly added -->
  - Virtual Router Redundancy Protocol (VRRP): Open standard active/standby failover. <!-- newly added -->
  - Gateway Load Balancing Protocol (GLBP): Cisco proprietary load balancing and failover. <!-- newly added -->

Virtual IP (VIP): Shared IP address for cluster failover.

Subinterfaces: Logical interfaces created on a single physical interface.

Routing Information Protocol (RIP): Distance-vector routing protocol using hop
count.

### 2.2 Given a scenario, configure switching technologies and features

Virtual Local Area Network (VLAN): Logical network segment on physical switch.
    - Access Port: Switch port carrying traffic for only one VLAN. <!-- newly added -->
    - Trunk Port: Switch port carrying traffic for multiple VLANs. <!-- newly added -->
    - Inter-VLAN Routing: Routing traffic between different VLANs. <!-- newly added -->
    - VLAN Database: Storage file containing VLAN configuration information.
    - Switch Virtual Interface (SVI): Logical Layer 3 interface on a switch.

Interface Configuration: Settings applied to individual physical or logical ports.

    - Native VLAN: VLAN for untagged traffic on trunk ports.
    - Voice VLAN: VLAN dedicated to carrying real-time voice traffic.
    - 802.1Q Tagging: Protocol tagging frames for VLAN identification.
    - Flooding: Forwarding frame out all ports except source when destination unknown. <!-- newly added -->
    - Storm Control: Prevents network outages by limiting broadcast/multicast traffic. <!-- newly added -->
    - Switch Stacking: Linking multiple switches to manage them as a single unit. <!-- newly added -->
    - Auto-MDIX: Automatic detection and configuration of cable connection type. <!-- newly added -->
    - Wake-on-LAN (WoL): Powering on a device remotely via network signal. <!-- newly added -->
    - Link Aggregation: Combining ports to increase bandwidth.
        - Link Aggregation Control Protocol (LACP): Protocol for bundling ports into single channels.
    - Speed: Data rate setting for a network interface.
    - Duplex: Communication mode setting (half or full) for port.

Spanning Tree Protocol (STP): Protocol preventing Layer 2 loops.
  - Root Bridge: Central reference point (lowest Bridge ID). <!-- newly added -->
  - Port Roles: <!-- newly added -->
    - Root Port: Best path to root bridge. <!-- newly added -->
    - Designated Port: Best path to segment. <!-- newly added -->
    - Blocked Port: Prevents loops by not forwarding. <!-- newly added -->
  - Port States: <!-- newly added -->
    - Blocking: Prevents traffic to avoid loops. <!-- newly added -->
    - Listening: Prepares to forward, doesn't learn MACs. <!-- newly added -->
    - Learning: Adds MACs to table, doesn't forward. <!-- newly added -->
    - Forwarding: Actively forwards traffic. <!-- newly added -->

    - Rapid Spanning Tree Protocol (RSTP): Faster convergence version of Spanning Tree Protocol.

Maximum Transmission Unit (MTU): Largest data packet size supported by
interface.

    - Jumbo Frames: Ethernet frames larger than standard 1500 bytes.

### 2.3 Given a scenario, select and configure wireless devices and technologies

Channels: Specific frequency ranges for wireless communication.

- 802.11 Standards: Wireless networking specifications. <!-- newly added -->
  - 802.11a: 5GHz band, 54Mbps speed (Legacy). <!-- newly added -->
  - 802.11b: 2.4GHz band, 11Mbps speed (Legacy). <!-- newly added -->
  - 802.11g: 2.4GHz band, 54Mbps speed (Legacy). <!-- newly added -->
  - 802.11n: 2.4/5GHz bands, 600Mbps (MIMO). <!-- newly added -->
  - 802.11ac: 5GHz band, >1Gbps (MU-MIMO). <!-- newly added -->
  - 802.11ax: 2.4/5/6GHz bands, >10Gbps (Wi-Fi 6, OFDMA). <!-- newly added -->
- Channel Width: Frequency range used for data transmission.
- Non-Overlapping Channels: Adjacent channels that do not interfere.
- Regulatory Impacts: Legal restrictions on wireless frequency usage.
- 802.11h: Wi-Fi amendment preventing interference with radar.

Frequency Options: Radio bands available for wireless data transmission.

- 2.4GHz: Common wireless band with long range and penetration.
- 5GHz: High-speed wireless band with less interference.
- 6GHz: Ultra-fast band for Wi-Fi 6E devices.
- Band Steering: Directing dual-band clients to the 5GHz frequency.

Service Set Identifier (SSID): Name identifying a wireless network.

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
- Multiple Input Multiple Output (MIMO): Using multiple antennas to increase performance. <!-- newly added -->
- Multi-User MIMO (MU-MIMO): Allowing router to communicate with multiple devices simultaneously. <!-- newly added -->
- Beamforming: Directing wireless signal towards specific receiving device. <!-- newly added -->

Autonomous vs. Lightweight Access Point: Standalone management versus
controller-based management. 
- Autonomous: Standalone access point managing its own configuration. 
- Lightweight Access Point: Controller-managed access point with minimal local logic.

### 2.4 Explain important factors of physical installations

Important Installation Implications: Physical considerations for deploying network equipment.

- Locations: Physical sites where network hardware is installed.
  - Intermediate Distribution Frame (IDF): Cable rack connecting end devices to
    MDF.
  - Main Distribution Frame (MDF): Central point for network cabling
    termination.
  - Wiring Closet: Room where network cables terminate and equipment is housed. <!-- newly added -->
- Rack Size: Standardized width and height units (U).
- Port-Side Exhaust/Intake: Managing airflow direction through rack equipment.
- Cabling: Physical wiring used to interconnect network devices.
  - Horizontal Cabling: Cabling running from work area to wiring closet. <!-- newly added -->
  - Backbone Cabling: High-capacity cabling connecting wiring closets or floors. <!-- newly added -->
  - Cable Tray: Support system for managing and protecting cable runs. <!-- newly added -->
  - Patch Cable: Short cable connecting devices to wall ports or patch panels. <!-- newly added -->
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
  - Wet Pipe: Pipes contain water, fast response (risk of leak). <!-- newly added -->
  - Dry Pipe: Water released into pipes only when alarm triggered. <!-- newly added -->
  - Pre-action: Requires detection and sprinkler activation (double check). <!-- newly added -->
  - Deluge: Releases large volume of water (not common for electronics). <!-- newly added -->
  - Clean Agents: Gas-based, leaves no residue (Halon alternatives). <!-- newly added -->
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
  - NetFlow: Protocol collecting IP traffic flow statistics. <!-- newly added -->
- Packet Capture: Intercepting and logging data packets for analysis.
- Baseline Metrics: Historical data representing normal network performance
  levels.
  - Baselining: Establishing normal performance metrics for comparison. <!-- newly added -->
  - Anomaly Alerting/Notification: Triggering warnings when traffic deviates
    from baseline.
- Log Aggregation: Consolidating log data from multiple network sources.
  - Syslog Collector: Server gathering log messages from network devices.
    - Severity Levels (0-7): Emergency (0), Alert (1), Critical (2), Error (3), Warning (4), Notice (5), Info (6), Debug (7). <!-- newly added -->
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
- Backup Types: Strategies for data preservation. <!-- newly added -->
  - Full Backup: Copying entire data set (slowest backup, fastest restore). <!-- newly added -->
  - Incremental Backup: Copying only changes since last backup (fastest backup, slowest restore). <!-- newly added -->
  - Differential Backup: Copying changes since last full backup (moderate backup/restore). <!-- newly added -->

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

## 4.0 Network Security 14%

### 4.1 Explain the importance of basic network security concepts

Logical Security: Software and procedural measures protecting digital assets.

- Encryption: Scrambling data to prevent unauthorized access.
  - Data in Transit: Protecting data as it travels across networks.
  - Data at Rest: Protecting data stored on physical storage media.
- Certificates: Digital documents verifying identity of network entities.
  - Public Key Infrastructure (PKI): Framework managing digital certificates and
    keys.
  - Self-Signed: Certificate signed by its creator rather than CA.
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
  - Defense in Depth: Layered security approach (Physical -> Firewall -> Endpoint). <!-- newly added -->
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
  - SYN Flood: Initiating many TCP connections without completing handshake. <!-- newly added -->
  - ICMP Flood (Smurf Attack): Overwhelming target with ping requests. <!-- newly added -->
- Distributed Denial-of-Service (DDoS): DoS attack from multiple sources
  simultaneously.

VLAN Hopping: Attacking by moving between different VLANs illegally.

Media Access Control (MAC) Flooding: Overwhelming switch MAC tables with fake
addresses.

ARP Poisoning: Corrupting ARP cache to map attacker's MAC.

ARP Spoofing: Sending fake ARP messages to intercept traffic.

DNS Poisoning: Injecting fake DNS records to redirect traffic.
  - DNS Cache Poisoning: Corrupting DNS resolver cache. <!-- newly added -->
  - DNS Amplification: Overwhelming target with large DNS responses. <!-- newly added -->
  - DNS Tunneling: Encapsulating non-DNS traffic in DNS queries. <!-- newly added -->
  - DNS Hijacking: Diverting queries to malicious DNS server. <!-- newly added -->

DNS Spoofing: Redirecting users to malicious sites via DNS.

Rogue Devices and Services: Unauthorized hardware or software on a network.

- Rogue Devices: Unauthorized hardware connected to a secure network.
- Services: Unauthorized software-based functions running on a network.
- DHCP: Unauthorized server distributing incorrect IP configurations.
- Access Point (AP): Hardware device providing wireless network connectivity.
  - Rogue Access Point: Unauthorized wireless access point on a network.

Evil Twin: Fake access point mimicking a legitimate one.

On-Path Attack: Intercepting communication between two legitimate network nodes.
  - Replay Attack: Capturing and retransmitting valid data. <!-- newly added -->
  - Relay Attack: Proxying communication between two hosts. <!-- newly added -->
  - SSL Stripping: Downgrading HTTPS to HTTP. <!-- newly added -->

Social Engineering Phishing: Fraudulent emails tricking users into revealing
info.
  - Spear Phishing: Targeted phishing attack against specific individuals. <!-- newly added -->
  - Whaling: Targeted phishing attack against high-level executives. <!-- newly added -->
  - Vishing: Voice phishing attacks via phone calls. <!-- newly added -->
  - Smishing: SMS phishing attacks via text messages. <!-- newly added -->
  - Pretexting: Creating a fabricated scenario to gain trust. <!-- newly added -->
- Dumpster Diving: Searching through trash for sensitive information.
- Shoulder Surfing: Watching someone enter passwords or sensitive data.
- Tailgating: Following authorized personnel into restricted physical areas.

Malware: Malicious software designed to harm systems or data.
  - Virus: Malware requiring host file to spread. <!-- newly added -->
  - Worm: Self-replicating malware spreading across networks. <!-- newly added -->
  - Trojan: Malware masquerading as legitimate software. <!-- newly added -->
  - Ransomware: Malware encrypting files and demanding payment. <!-- newly added -->
  - Spyware: Malware collecting information without consent. <!-- newly added -->
  - Rootkit: Malware hiding malicious presence and processes. <!-- newly added -->
  - Logic Bomb: Malicious code triggering on specific event/condition. <!-- newly added -->

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
  - Demilitarized Zone (DMZ): Semi-trusted network segment hosting public servers. <!-- newly added -->

## 5.0 Network Troubleshooting 24%

### 5.1 Explain the troubleshooting methodology

Identify the Problem: Gather information, symptoms, and recent changes.

- Gather Information: Collecting all relevant data about the issue.
- Question Users: Interviewing affected individuals to understand symptoms.
- Identify Symptoms: Determining specific signs of the network problem.
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
- if theory is not confirmed, establish a new theory or escalate

Establish a Plan of Action to resolve the problem and identify potential
effects: Determine steps to fix and assess impact.

Implement the Solution or escalate as necessary: Execute the fix or escalate if
needed.

Verify Full System Functionality and implement preventive measures if
applicable: Confirm system works and prevent recurrence.

Document Findings, Actions, Outcomes, and Lessons Learned throughout the
process: Record actions, outcomes, and lessons learned.

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
    - Near-End Crosstalk (NEXT): Interference measured at the source end. <!-- newly added -->
    - Far-End Crosstalk (FEXT): Interference measured at the receiving end. <!-- newly added -->
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
  - Giants: Ethernet frames larger than permitted maximum size (>1518 bytes). <!-- newly added -->
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
  - Throughput Capacity: Rate at which data is successfully transmitted. <!-- newly added -->
- Goodput: Average rate of successful data transfer. <!-- newly added -->

Latency: Time delay for data to reach destination.
  - Processing Delay: Time to process packet header. <!-- newly added -->
  - Queuing Delay: Time packet spends in routing queues. <!-- newly added -->
  - Transmission Delay: Time to push packet bits onto link. <!-- newly added -->
  - Propagation Delay: Time for signal to travel through media. <!-- newly added -->

Packet Loss: Data units failing to reach their destination.

Jitter: Variation in packet arrival time.

Wireless

- Interference: External signals disrupting wireless network communication.
  - Channel Overlap: Wireless frequencies interfering with each other.
  - Hidden Node: Client unable to detect other clients, causing collisions. <!-- newly added -->
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
