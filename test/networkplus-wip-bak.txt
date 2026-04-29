# networkplus

## 1.0 Networking Concepts 23%

### 1.1 Explain concepts related to the Open Systems Interconnection (OSI) reference model

**Open Systems Interconnection (OSI)**: *Standardized seven-layer framework* for network communication.

**Fundamental Concepts**:

- **Interoperability**: Ability of *different systems and organizations* to work together.
- **Abstraction**: *Hiding implementation details* to simplify complex systems.
- **Standardization**: Establishing *technical criteria* to ensure uniformity (ISO, IEEE).
- **Protocol**: Set of *rules governing data exchange* (Syntax, Semantics, Timing).
- **Transmission Modes**: *Direction of signal flow* (Simplex, Half-Duplex, Full-Duplex).
- **Connection Services**: *Reliability of data transfer* (Connection-Oriented vs Connectionless).

- **Protocol Data Unit (PDU)**: *Data block exchanged* at specific protocol layers.
- **Encapsulation**: Process of *adding headers and trailers* to data at each layer.
  - **Header**: *Control information* added to beginning of data payload.
  - **Trailer**: *Control information* added to end of data payload.
  - **Payload**: *Actual data* being transmitted within a packet/frame.
- **Decapsulation**: Process of *removing headers and trailers* from data at each layer.
- **Addressing**: Mechanism for *identifying nodes and routing messages* (MAC, IP, Port).
- **Multiplexing**: *Combining multiple signals* into one transmission channel.

- **Layer 1 - Physical**: Transmits *raw bits* over physical medium.
  - **PDU**: *Bit*.
  - **Sub-concepts**: Signaling (Sync/Async), Modulation, Multiplexing (TDM/FDM), Physical Topologies.
    - **Attenuation**: *Loss of signal strength* over distance.
    - **Latency**: *Time delay* for data to travel from source to destination.
    - **Bandwidth**: *Maximum rate* of data transfer across a given path.
  - **Devices**: Hubs, Repeaters, Cables, Transceivers, Modems.
  - **Protocols/Standards**: Ethernet (IEEE 802.3 Physical), Wi-Fi (IEEE 802.11 Physical), Bluetooth, USB.
- **Layer 2 - Data Link**: *Node-to-node data transfer* and error handling.
  - **PDU**: *Frame*.
  - **Sublayers**:
    - **Media Access Control (MAC)**: *Addressing and channel access control*.
    - **Logical Link Control (LLC)**: *Flow control, error checking*, and protocol multiplexing.
  - **Sub-concepts**: MAC Addressing, Switching, Bridging, Error Detection (CRC/FCS).
    - **Collision Domain**: Network segment where *data collisions can occur*.
    - **Broadcast Domain**: Logical division where *all nodes* can reach each other by broadcast.
    - **CSMA/CD**: *Carrier Sense Multiple Access/Collision Detection* (Ethernet access method).
  - **Devices**: Switches, Bridges, Network Interface Cards (NICs), Wireless Access Points (WAPs).
  - **Protocols**: Ethernet, PPP, ARP, STP, VLAN (802.1Q), L2TP.
- **Layer 3 - Network**: *Routing data packets* between different networks.
  - **PDU**: *Packet*.
  - **Sub-concepts**: IP Addressing (Logical), Routing, Path Selection, Packet Switching/Circuit Switching.
    - **Fragmentation**: *Breaking packets into smaller units* to fit MTU.
    - **Time to Live (TTL)**: Field *limiting packet lifespan* to prevent looping.
    - **Route Table**: *Database* used by routers to determine where to forward packets.
  - **Devices**: Routers, Layer 3 Switches, Firewalls.
  - **Protocols**: IP (IPv4/IPv6), ICMP, IPSec, GRE, RIP, OSPF, BGP.
- **Layer 4 - Transport**: *Reliable end-to-end data delivery* and flow control.
  - **PDU**: *Segment (TCP) / Datagram (UDP)*.
  - **Sub-concepts**: Port Numbers, Segmentation, Flow Control, Error Recovery, Multiplexing.
    - **Windowing**: Controlling data flow by *limiting unacknowledged segments*.
    - **Acknowledgement (ACK)**: *Confirmation of receipt* of data packets.
    - **Three-Way Handshake**: Process to *establish a reliable TCP connection* (SYN, SYN-ACK, ACK).
  - **Devices**: Load Balancers, Firewalls (Stateful).
  - **Protocols**: TCP, UDP.
- **Layer 5 - Session**: *Managing communication sessions* between applications.
  - **Sub-concepts**: Dialog Control, Session ID, Setup/Teardown.
    - **Synchronization**: *Checkpointing data stream* to allow recovery from interruption.
    - **Remote Procedure Calls (RPC)**: *Executing code on a remote system* as if local.
  - **Protocols**: SIP, RTP, RPC, NetBIOS, SMB.
- **Layer 6 - Presentation**: *Data translation, encryption, and compression* formatting.
  - **Sub-concepts**: Data Formatting (ASCII/Unicode), Encryption/Decryption, Compression/Decompression.
    - **Character Sets**: *Encoding standards* for text (ASCII, Unicode, EBCDIC).
    - **Serialization**: *Converting data structures* into a format for storage or transmission.
  - **Protocols**: SSL/TLS, JPEG, GIF, MPEG.
- **Layer 7 - Application**: *Interface for end-user* network processes.
  - **Sub-concepts**: Network Services, User Interface.
    - **Application Programming Interface (API)**: Set of *definitions for building and integrating* application software.
    - **User Agent**: *Software acting on behalf of a user* (e.g., Web Browser).
  - **Devices**: Application Gateways, Proxy Servers.
  - **Protocols**: HTTP, HTTPS, FTP, DNS, SMTP, DHCP, SSH, Telnet, SNMP.

**Network Nodes**: Devices that *send, receive, and forward data*.

- **Intermediate Nodes**: Devices that *forward traffic* between other nodes (routers, switches).
- **End Systems (Hosts)**: Devices that *send and receive data* (computers, servers, phones).

### 1.2 Compare and contrast networking appliances, applications, and functions.

**Physical**: *Hardware-based* network components and devices. **Virtual Appliances**: *Software-based* network functions running on hypervisors.

**Network Architecture Planes**:

- **Control Plane**: Part of the network that *makes routing decisions* (Routing Tables, OSPF, BGP).
- **Data Plane (Forwarding Plane)**: Part of the network that *forwards data packets* based on Control Plane decisions.

- **Router**: *Forwards data packets* between computer networks (Layer 3).
  - Uses **Routing Tables** to determine best path.
  - Can perform **NAT, DHCP, and ACL filtering**.
  - Connects *diverse network types* (LAN, WAN, Copper, Fiber).
- **Switch**: *Connects devices* within a single network segment (Layer 2/Layer 3).
  - **Layer 2 Switch**: Forwards frames based on **MAC addresses**.
  - **Layer 3 Switch (Multilayer)**: Adds *routing functionality* (IP-based forwarding).
  - Creates *separate collision domains* per port (unlike Hubs).
  - Supports **VLANs and Power over Ethernet (PoE)**.
- **Firewall**: *Security device* filtering network traffic rules (Layer 3/4/7).
  - Filters traffic based on **IP, Port, and Application (NGFW)**.
  - **Statefulness**: Tracks active connections (Stateful vs Stateless).
  - Can be *physical appliance or virtual software*.
- **Intrusion Detection System (IDS)**: *Monitors network traffic* for suspicious activity.
- **Intrusion Prevention System (IPS)**: *Detects and blocks* malicious network activity.
- **Load Balancer**: *Distributes network traffic* across multiple servers.
- **Proxy**: *Intermediary server* handling client requests.
- **Network-Attached Storage (NAS)**: *File-level storage* connected to a network.
- **Storage Area Network (SAN)**: Dedicated *high-speed network* for block-level storage access.
  - *Offloads storage traffic* from LAN to improve performance.
  - **Protocols**: Fibre Channel (FC), iSCSI, FCoE.
- **Wireless**: *Communication using radio waves* instead of cables.
  - **Access Point (AP)**: *Bridges wireless clients* to wired network (Layer 2).
  - **Wireless Controller**: *Central management device* for multiple access points.
    - Centralizes configuration, security policies, and firmware updates.
- **Modem**: Device *modulating and demodulating* signals for transmission (Layer 1/2).
  - Converts *digital signals to analog* (and vice versa) for DSL/Cable/Fiber.
- **Network Interface Controller (NIC)**: *Hardware connecting computer* to network media.

**Functions and Applications**:

- **Client**: Device *users access the network* with (Workstation, Phone, Laptop).
- **Server**: Device *providing resources* to the network (File, Web, Email).
- **Quality of Service (QoS)**: *Prioritizing specific traffic types* over others.
- **Time to Live (TTL)**: *Packet lifespan limit* to prevent looping.
- **Content Delivery Network (CDN)**: *Distributed servers* speeding up content delivery.

**Standards Organizations**:

- **Internet Assigned Numbers Authority (IANA)**: Manages *global IP allocation* and DNS root.
- **Internet Engineering Task Force (IETF)**: Develops *Internet standards and protocols* (RFCs).

### 1.3 Summarize cloud concepts and connectivity options.



**Cloud Models**:

- **Infrastructure as a Service (IaaS)**: *Virtualized computing resources* over the internet.

- **Platform as a Service (PaaS)**: *Platform for developing and deploying* applications.

- **Software as a Service (SaaS)**: *Software delivered over internet* via subscription.



**Deployment Models**:

- **Public Cloud**: Cloud resources *shared by general public*.

- **Private Cloud**: Cloud infrastructure *dedicated to single organization*.

- **Hybrid Cloud**: Environment *combining public and private* clouds.



**Cloud Connectivity**:

- **Virtual Private Network (VPN)**: *Encrypted tunnel* over a public network.

- **Direct Connect**: *Dedicated physical connection* to cloud provider.



**Cloud Infrastructure Concepts**:

- **Network Functions Virtualization (NFV)**: *Virtualizing network services* by decoupling from hardware.

  - **Decoupling**: *Separating network functions* from proprietary hardware.

- **Virtual Private Cloud (VPC)**: *Isolated private network* within a public cloud.

  - **Isolation**: *Segmenting resources* for security and control.

- **Cloud Gateways**: *Entry points* connecting local networks to cloud.

  - **Internet Gateway (IGW)**: *Connects VPC instances* to the internet.

  - **Network Address Translation (NAT) Gateway**: *Enables private instances* to access internet.



**Security and Management**:

- **Network Security Groups (NSG)**: *Virtual firewall rules* for cloud resources (Instance-level).

- **Network Security Lists**: Firewall rules *applied at the subnet level*.

- **Multitenancy**: *Single instance* serving multiple distinct customers.

- **Scalability**: Ability to *handle increasing workload* growth.

- **Elasticity**: *Automatically scaling* resources up and down.

### 1.4 Explain common networking ports, protocols, services, and traffic types.

- **Protocols**: *Rules governing data exchange* between network devices.
  - **Connection-Oriented**: *Establishes session* before data transfer (Reliable).
  - **Connectionless**: *Sends data without* established session (Unreliable/Fast).
  - **Stateful**: *Retains information* about session status (e.g., TCP).
  - **Stateless**: *No session information* retained between requests (e.g., UDP, HTTP).

- **Ports**: *Logical endpoints* for identifying specific processes.
  - **Well-known Ports (0-1023)**: *Reserved for system services* (HTTP, FTP).
  - **Registered Ports (1024-49151)**: *Assigned to user processes*/applications.
  - **Dynamic/Private Ports (49152-65535)**: *Ephemeral ports* for client sessions.

  - **File Transfer Protocol (FTP)**: *Transfers files* between systems using ports 20/21.
  - **Secure File Transfer Protocol (SFTP)**: *Secure file transfer* using SSH on port 22.
  - **Secure Shell (SSH)**: *Encrypted remote* command-line access on port 22.
  - **Telnet**: *Unencrypted remote* command-line communication on port 23.
  - **Simple Mail Transfer Protocol (SMTP)**: *Sends email* messages using port 25.
  - **Domain Name System (DNS)**: *Resolves domain names* to IP addresses (port 53).
  - **Dynamic Host Configuration Protocol (DHCP)**: *Automates IP address* assignment (ports 67/68).
  - **Trivial File Transfer Protocol (TFTP)**: *Simple file transfer* without authentication (port 69).
  - **Hypertext Transfer Protocol (HTTP)**: *Transmits unencrypted* web data on port 80.
  - **Hypertext Transfer Protocol Secure (HTTPS)**: *Secure, encrypted* web browsing on port 443.
  - **Network Time Protocol (NTP)**: *Synchronizes clocks* on network devices (port 123).
  - **Simple Network Management Protocol (SNMP)**: *Monitors and manages* network devices (ports 161/162).
  - **Lightweight Directory Access Protocol (LDAP)**: *Queries and manages* distributed directory information (port 389).
  - **Server Message Block (SMB)**: Network *file and printer sharing* (port 445).
  - **Syslog**: Standard protocol for *system log messages* (port 514).
  - **Simple Mail Transfer Protocol Secure (SMTPS)**: *Secure email submission* using port 587.
  - **Lightweight Directory Access Protocol over SSL (LDAPS)**: *Secure directory access* on port 636.
  - **Structured Query Language (SQL Server)**: *Microsoft database* communication using port 1433.
  - **Remote Desktop Protocol (RDP)**: *GUI-based remote* access on port 3389.
  - **Session Initiation Protocol (SIP)**: *Manages multimedia* communication sessions (ports 5060/5061).
    - **Session Management**: *Setup, modification, and teardown* of calls.

- **Internet Protocol (IP) types**
  - **Internet Protocol (IP)**: *Principal protocol* for routing and addressing packets.
  - **Internet Control Message Protocol (ICMP)**: *Reports network errors* and diagnostic information.
  - **Transmission Control Protocol (TCP)**: *Reliable, connection-oriented* data delivery protocol.
    - **Three-Way Handshake**: *SYN, SYN-ACK, ACK* process establishing connection.
    - **Flow Control**: *Managing data rate* to prevent overwhelming receiver.
    - **Sequence Numbers**: *Ordering packets* to reconstruct stream at destination.
    - **Acknowledgments**: *Confirming receipt* of data packets.
  - **User Datagram Protocol (UDP)**: *Fast, connectionless*, best-effort data transmission protocol.
  - **Generic Routing Encapsulation (GRE)**: *Encapsulates* various network protocols within virtual tunnels.
  - **Internet Protocol Security (IPsec)**: Suite *ensuring IP packet* confidentiality and integrity.
    - **Authentication Header (AH)**: *Verifies sender identity* and data integrity.
    - **Encapsulating Security Payload (ESP)**: Provides *encryption, authentication*, and data integrity.
    - **Internet Key Exchange (IKE)**: *Negotiates security keys* and associations automatically.
  - **Address Resolution Protocol (ARP)**: *Resolves IP addresses* to MAC hardware addresses.
- **Traffic Types**: *Categories of data flow* across a network.
  - **Unicast**: *One-to-one* communication between single sender and receiver.
  - **Multicast**: *One-to-many* communication to a subscribed group.
    - Uses 224.0.0.0/4 IPv4 range
  - **Anycast**: *One-to-nearest* communication within a group of nodes.
    - Used in IPv6 and DNS
  - **Broadcast**: *One-to-all* communication on a network segment.
    - Used for ARP, DHCP Discover

### 1.5 Compare and contrast transmission media and transceivers.

- **Wireless**: *Data transmission* via electromagnetic radio frequencies.
  - **802.11 Standards**: Wireless networking standards *utilizing radio transmission*.
    - **802.11a**: 54 Mbps on **5 GHz band** (Legacy).
    - **802.11b**: 11 Mbps on **2.4 GHz band** (Legacy).
    - **802.11g**: 54 Mbps on **2.4 GHz band** (Legacy).
    - **802.11n (Wi-Fi 4)**: 600 Mbps on **2.4/5 GHz** (MIMO).
    - **802.11ac (Wi-Fi 5)**: 1 Gbps+ on **5 GHz** (MU-MIMO).
    - **802.11ax (Wi-Fi 6)**: 10 Gbps on **2.4/5/6 GHz** (OFDMA).
  - **Cellular**: Wireless data transmission via *mobile phone networks*.
  - **Satellite**: Internet access via *orbiting relay stations*.

- **Wired**: *Data transmission* through physical cables and wires.
  - **Twisted Pair Categories**: *Copper cabling standards* for Ethernet.
    - **Cat 5e**: 1 Gbps up to **100 meters**.
    - **Cat 6**: 10 Gbps up to **55 meters**.
    - **Cat 6a**: 10 Gbps up to **100 meters**.
    - **Cat 8**: 40 Gbps up to **30 meters** (Datacenter).
  - **Fire Ratings**: *Cable jacket types* for safety compliance.
    - **Plenum**: *Fire-resistant, low-smoke* for air handling spaces.
    - **Riser (Non-Plenum)**: *Vertical runs* between floors, less fire-resistant.
  - **Fiber Optic Types**: *Glass cabling* using light for transmission.
    - **Single-Mode Fiber (SMF)**: *Small core (9um)*, laser-based, long distance (km).
    - **Multimode Fiber (MMF)**: *Larger core (50um)*, LED-based, short distance (m).
  - **Coaxial Cable**: *Copper core with shielding* for broadband/TV.
    - **RG-6**: Standard for *modern cable TV/internet*.
    - **RG-59**: Older standard, *higher loss*, short runs.
  - **Direct Attach Copper (DAC)**: *Twinax copper cable* with integrated transceivers.

- **Transceivers**: Devices that *both transmit and receive signals*.
  - **Form Factors**: *Standardized physical dimensions* and module shapes.
    - **Small Form-Factor Pluggable (SFP)**: 1 Gbps *hot-swappable module*.
    - **Enhanced SFP (SFP+)**: 10 Gbps version of SFP.
    - **Quad SFP (QSFP)**: 40 Gbps module (4 channels).
    - **QSFP28**: 100 Gbps module for *high-speed backbones*.
  - **Protocol**: *Rules for physical data encoding* and transmission.
    - **Fiber Channel (FC)**: *High-speed network technology* for storage networking.

- **Connector Types**: *Physical interfaces* used for joining network cables.
  - **Subscriber Connector (SC)**: *Square push-pull* fiber connector (Datacenter/Telecom).
  - **Local Connector (LC)**: *Small form-factor push-pull* fiber connector (High-density).
  - **Straight Tip (ST)**: *Bayonet twist-lock* fiber connector (Legacy/Campus).
  - **Multi-Fiber Push On (MPO)**: *High-density connector* for 12-24 fibers.
  - **Registered Jack (RJ)**: *Standard connector interface* for telecommunications.
    - **RJ11**: 6-position, 2-4 conductor for *telephone/DSL*.
    - **RJ45**: 8-position, 8-conductor for *Ethernet networking*.
  - **F-Type Connector**: *Screw-on connector* for coaxial cable (TV/Modem).
  - **Bayonet Neill-Concelman (BNC)**: *Twist-lock connector* for coaxial cables.
  - **Ultra Physical Contact (UPC)**: Fiber connector polish with *rounded surface*.
  - **Angled Physical Contact (APC)**: Fiber connector polish with *angled surface*.

### 1.6 Compare and contrast network topologies, architectures, and types.

- **Physical Topology**: *Actual layout* of hardware, cables, and devices.
- **Logical Topology**: *Path data flows* through the network.
- **Mesh Topology**: Network where nodes connect to *multiple others*.
  - **Full Mesh**: Every node connects *directly to every other* node.
    - **Fault Tolerance**: System *continues operating* after component failure.
  - **Partial Mesh**: Selected nodes connect to multiple others for *redundancy*.
    - **Redundancy**: *Duplicate components or paths* preventing system failure.
- **Hybrid Topology**: Network *mixing multiple* topology types.
- **Star Topology / Hub-and-Spoke**: *Central device* connects all nodes (LAN) or sites (WAN).
  - **Single Point of Failure**: *Critical component* whose failure stops entire system.
  - **Scalability**: Ability to *handle increasing workload* growth.
- **Spine and Leaf**: Datacenter topology *reducing latency* between servers.
  - **Two-Layer Design**: Architecture *minimizing hops* between any two servers.
  - **Minimizing Latency**: *Reducing time delay* for data packet transmission.
- **Point-to-Point**: *Direct connection* between two nodes.
  - **Dedicated Connection**: Communication channel *reserved for specific users*.
  - **Leased Lines**: *Rented dedicated circuit* between two points (T1/E1).
- **Bus Topology**: Single *cable backbone* connecting all network devices sequentially.
- **Ring Topology**: Network nodes connected in a *closed loop*.
- **Three-Tier Hierarchical Model**: Design separating **Core, Distribution, and Access**.
  - **Core Layer**: *High-speed backbone* of network hierarchy.
    - **Redundancy**: *High availability* through duplicate hardware and paths.
  - **Distribution Layer**: Layer *connecting access switches* to core.
    - **Policy Enforcement**: *Applying security, QoS, and routing* rules.
  - **Access Layer**: Network hierarchy tier connecting *end-user devices*.
    - **Power over Ethernet (PoE)**: *Delivering power* via Ethernet cabling.
- **Collapsed Core**: Topology *merging core and distribution* layers.
  - **Simplified Management**: *Reducing complexity* by combining network layers.
  - **Cost Reduction**: *Lowering expenses* by using fewer physical devices.
- **Traffic Flows**: *Patterns of data movement* through a network.
  - **North-South Traffic**: Data flow *entering or leaving* datacenter (Client-to-Server).
  - **East-West Traffic**: Data flow *between servers* in datacenter (Server-to-Server).
- **Network Types**: Categorization of networks based on *geographic scale*.
  - **Local Area Network (LAN)**: Network within a *limited geographic area*.
    - **Residential Network**: SOHO LAN for *home use* with consumer-grade equipment.
    - **SME Network**: LAN for small/medium enterprises with *structured cabling*.
    - **Enterprise LAN**: Large-scale LAN with *high-performance equipment* and redundancy.
    - **Datacenter Network**: *High-speed network* connecting servers and storage.
  - **Wide Area Network (WAN)**: Network spanning *large geographic distances*.
  - **Personal Area Network (PAN)**: *Very short range* network (Bluetooth).
  - **Metropolitan Area Network (MAN)**: Network spanning a *city or campus*.
    - **Campus Area Network (CAN)**: Network connecting *multiple buildings* in limited geographic area.
    - **Small Office/Home Office (SOHO)**: Small LAN using a *single multifunction appliance* for connectivity.
    - **Client-Server Network**: Network where *dedicated servers* provide resources to client devices.
      - **Server**: Device that *provides resources* or services to other hosts.
      - **Client**: Device that *requests and consumes* resources from servers.
    - **Peer-to-Peer Network (P2P)**: Network where hosts act as both *clients and servers* sharing resources.
    - **Intranet**: *Private network* accessible only to organization's internal users.
    - **Extranet**: Intranet allowing *controlled access* to external business partners.
    - **Darknet**: *Overlay network* accessible only with specific software.
  - **WAN Techologies**
  - **Multiprotocol Label Switching (MPLS)**: *Label-based routing* for faster, efficient network traffic flow.
  - **Metro Ethernet (Metro-E)**: High-speed Ethernet *extension across a metropolitan area*.
  - **Leased Line (T1/E1)**: *Dedicated point-to-point* connection with guaranteed bandwidth.
  - **Digital Subscriber Line (DSL)/Cable**: *Internet access* via telephone lines or coaxial cables.

### 1.7 Given a scenario, use appropriate IPv4 network addressing.



- **Public vs. Private**: *Globally routable* versus internal-only IP addresses.

  - **Public Addresses**: *Globally unique* addresses assigned by **IANA**.

    - **Globally Unique**: IP addresses that are *distinctive across the internet*.

  - **Private Addresses (RFC 1918)**: *Non-routable* addresses reserved for internal networks.

    - **Non-Routable**: Traffic *not forwarded* by public internet routers.

    - **Network Address Translation (NAT)**: Mechanism *mapping private IPs* to public IPs.

  - **Automatic Private IP Addressing (APIPA)**: *Self-assigned fallback IP* when DHCP fails.

    - **Self-Assignment**: *Automatic IP configuration* without a DHCP server.

    - **Link-Local**: Communication *limited to the local network* segment.

  - **Loopback**: IP *directing traffic* to the local host.

  - **Localhost (127.0.0.1)**: Standard *hostname referring* to the local computer.



- **Subnetting**: *Dividing a network* into smaller logical segments.

  - **Broadcast Control**: *Limiting unnecessary* network traffic to specific subnets.

  - **Network vs Host Portion**: *Dividing bits* between network ID and device ID.

  - **Variable Length Subnet Mask (VLSM)**: Subnetting using *different mask lengths* efficiently.

    - **Arbitrary Length**: Masks using *non-standard bit lengths* (0-32).

  - **Classless Inter-Domain Routing (CIDR)**: *Flexible IP addressing* using prefix notation.

    - **Prefix Notation (CIDR)**: *Representing subnet masks* using bit-count (/XX).



    | CIDR | Subnet Mask     | Total IPs  |

    | ---- | --------------- | ---------- |

    | /32  | 255.255.255.255 | 1          |

    | /31  | 255.255.255.254 | 2          |

    | /30  | 255.255.255.252 | 4          |

    | /29  | 255.255.255.248 | 8          |

    | /28  | 255.255.255.240 | 16         |

    | /27  | 255.255.255.224 | 32         |

    | /26  | 255.255.255.192 | 64         |

    | /25  | 255.255.255.128 | 128        |

    | /24  | 255.255.255.0   | 256        |

    | /23  | 255.255.254.0   | 512        |

    | /22  | 255.255.252.0   | 1,024      |

    | /21  | 255.255.248.0   | 2,048      |

    | /20  | 255.255.240.0   | 4,096      |

    | /19  | 255.255.224.0   | 8,192      |

    | /18  | 255.255.192.0   | 16,384     |

    | /17  | 255.255.128.0   | 32,768     |

    | /16  | 255.255.0.0     | 65,536     |

    | /15  | 255.254.0.0     | 131,072    |

    | /14  | 255.252.0.0     | 262,144    |

    | /13  | 255.248.0.0     | 524,288    |

    | /12  | 255.240.0.0     | 1,048,576  |

    | /11  | 255.224.0.0     | 2,097,152  |

    | /10  | 255.192.0.0     | 4,194,304  |

    | /9   | 255.128.0.0     | 8,388,608  |

    | /8   | 255.0.0.0       | 16,777,216 |

  - **Decimal to Binary**



    | Subnet Mask (Decimal) | Subnet Mask (Binary) | Wildcard (Decimal) | Wildcard (Binary) |

    | --------------------- | -------------------- | ------------------ | ----------------- |

    | 255                   | 1111 1111            | 0                  | 0000 0000         |

    | 254                   | 1111 1110            | 1                  | 0000 0001         |

    | 252                   | 1111 1100            | 3                  | 0000 0011         |

    | 248                   | 1111 1000            | 7                  | 0000 0111         |

    | 240                   | 1111 0000            | 15                 | 0000 1111         |

    | 224                   | 1110 0000            | 31                 | 0001 1111         |

    | 192                   | 1100 0000            | 63                 | 0011 1111         |

    | 128                   | 1000 0000            | 127                | 0111 1111         |

    | 0                     | 0000 0000            | 255                | 1111 1111         |

- **IPv4 Address Classes**: *Hierarchical system* for IP address allocation.

  - **Default Masks**: Standard *subnet masks assigned* to each class.

  - **Host Capacity**: *Maximum number of devices* supported per subnet.

  - **Class A**: *Large networks* (1.0.0.0 - 126.255.255.255) /8.

  - **Class B**: *Medium networks* (128.0.0.0 - 191.255.255.255) /16.

  - **Class C**: *Small networks* (192.0.0.0 - 223.255.255.255) /24.

  - **Class D**: *Reserved for Multicast* traffic (224.0.0.0 - 239.255.255.255).

  - **Class E**: *Reserved for Experimental* use (240.0.0.0 - 255.255.255.255).

### 1.8 Summarize evolving use cases for modern network environments.

- **Software-Defined Network (SDN)** and **Software-Defined Wide Area Network (SD-WAN)**
  - **Software-Defined Network (SDN)**: *Centralized software control* of network hardware.
    - **Decoupling**: Separating *control plane from forwarding* data plane.
  - **Software-Defined Wide Area Network (SD-WAN)**: *Software-based management* of WAN connections.
    - **Application-Aware**: Prioritizing traffic based on *specific application type*.
    - **Zero-Touch Provisioning (ZTP)**: *Automated device configuration* upon network connection.
    - **Transport Agnostic**: Operating across *any underlying* communication medium.
    - **Central Policy Management**: *Unified control* of network rules from one interface.
- **Virtual Extensible LAN (VXLAN)**: Tunneling protocol *extending VLANs over Layer 3*.
  - **Data Center Interconnect (DCI)**: *Stretching Layer 2 segments* across dispersed datacenters.
  - **Layer 2 Encapsulation**: *Wrapping Ethernet frames* within UDP packets.
- **Overlay Network**: *Virtual network built* on top of physical network.
- **Zero Trust Architecture (ZTA)**: Security model *verifying every access request*.
  - **Policy-based Authentication**: Access granted via *strict identity and context* verification.
  - **Authorization**: *Dynamic, context-aware enforcement* of resource access rights.
  - **Least Privilege Access**: Granting *minimum permissions necessary* for specific tasks.
- **Secure Access Service Edge (SASE)** / **Security Service Edge (SSE)**
  - **Secure Access Service Edge (SASE)**: *Converging WAN and security* into cloud services.
  - **Security Service Edge (SSE)**: *Security-only subset* of the SASE architecture.
- **Infrastructure as Code (IaC)**: Managing infrastructure via *machine-readable definition files*.
  - **Automation**: *Scripting infrastructure tasks* to reduce human error.
    - **Playbooks**: *Automated scripts* for orchestrating configuration tasks.
    - **Templates**: *Standardized files* for consistent device deployment.
    - **Configuration Drift**: Detecting *deviations from the intended* baseline state.
    - **Dynamic Inventories**: *Real-time discovery* and management of network resources.
  - **Source Control**: System for *tracking and managing* code changes.
    - **Version Control**: *Tracking every modification* to the infrastructure code.
    - **Branching**: Developing features *independently in parallel* code lines.
- **IPv6 Addressing**: *128-bit addressing system* replacing IPv4.
  - **Mitigating Address Exhaustion**: Solving *limited IP supply* with massive space.
  - **Compatibility Requirements**: *Bridging communications* between IPv4 and IPv6.
    - **Tunneling**: *Encapsulating IPv6 packets* inside IPv4 packets.
    - **Dual Stack**: Running *IPv4 and IPv6 protocols* simultaneously.
    - **NAT64**: *Translating traffic* between IPv6 and IPv4 devices.

## 2.0 Network Implementation 20%

Goal of Domain 2:

- This domain covers the actual deployment and configuration of networking
  devices and technologies including routing, switching, wireless, and physical
  installations.
- It emphasizes practical implementation skills and is foundational for most
  real-world IT tasks.

Things You Must Memorize:

- Differences between RIP, OSPF, BGP, EIGRP
- VLAN and trunk configurations
- 802.11 standards and wireless security types
- DHCP relay and DNS record types
- Topology definitions and diagrams

### 2.1 Explain characteristics of routing technologies.



**Static Routing**: *Manually configured* routing entries by an administrator.

- **Use Cases**: Small networks, stub networks, stable environments.

- **Benefits**: Simplicity, *low overhead*, predictability, security.

- **Drawbacks**: *No auto-failover*, poor scalability, high maintenance.



**Dynamic Routing**: Routers *automatically exchanging* path information.

- **Use Cases**: Large networks, *changing topologies*, internet.

- **Benefits**: Scalability, adaptability, *automatic failover*.

- **Drawbacks**: Complexity, *resource usage*, security risks.



  - **Border Gateway Protocol (BGP)**: Protocol routing between *internet autonomous systems*.

    - **Autonomous Systems (AS)**: *Independent networks* under single administrative control.

  - **Enhanced Interior Gateway Routing Protocol (EIGRP)**: *Advanced distance-vector* protocol using multiple metrics.

    - **Rapid Convergence**: *Speed* at which routers agree on topology.

  - **Open Shortest Path First (OSPF)**: *Link-state routing* protocol using Dijkstra algorithm.

    - **Area**: *Logical grouping* of routers to optimize routing.



**Route Selection**: Process of *determining the best* network path.

- **Administrative Distance (AD)**: Metric ranking *trustworthiness* of routing sources.

- **Prefix Length**: Number of bits *identifying the network* portion.

- **Metric**: Value used to *evaluate cost* of path.



**Address Translation**: *Mapping one IP address space* into another.

- **Network Address Translation (NAT)**: *Remapping private IP* space to public IP.

- **Port Address Translation (PAT)**: *Many-to-one mapping* using unique port numbers.



**First Hop Redundancy Protocol (FHRP)**: Provides *failover* for default gateways.

- **Virtual IP (VIP)**: *Shared IP address* for cluster failover.

- **Virtual Router Redundancy Protocol (VRRP)**: *Open standard* for default gateway redundancy.



**Subinterfaces**: *Logical interfaces* created on a single physical interface.

- **Traffic Segregation**: *Isolating data flows* for security or management.



**Routing Information Protocol (RIP)**: *Distance-vector* routing protocol using hop count.

### 2.2 Given a scenario, configure switching technologies and features



**Virtual Local Area Network (VLAN)**: *Logical network segment* on physical switch.

- **Broadcast Domain Isolation**: *Segmenting network* to limit broadcast traffic spread.

- **VLAN Database**: Storage file containing *VLAN configuration information*.

  - **VLAN ID**: *Numerical identifier* for specific virtual networks.

- **Switch Virtual Interface (SVI)**: *Logical Layer 3* interface on a switch.

  - **Layer 3 Processing**: *Enabling routing* between different virtual networks.



**Interface Configuration**: *Settings applied* to individual physical or logical ports.

- **Native VLAN**: *Default VLAN* carrying untagged traffic on trunks.

  - **Untagged Traffic**: Frames *lacking 802.1Q* VLAN identifier tags.

- **Voice VLAN**: VLAN *prioritized for real-time* voice traffic.

  - **VoIP Prioritization**: *Ensuring QoS* for critical voice communications.

- **802.1Q Tagging (DOT1Q)**: Protocol *inserting VLAN identifiers* into frames.

  - **Frame Tagging**: *Marking Ethernet frames* with specific VLAN IDs.

- **Link Aggregation (LAG)**: *Combining physical ports* into one logical link.

  - **Fault Tolerance**: System *remains operational* during link failure.

  - **Increased Throughput**: *Aggregating bandwidth* from multiple physical connections.

  - **Link Aggregation Control Protocol (LACP)**: *Dynamic negotiation* protocol for bundling ports.

- **Speed**: *Data transfer rate* setting for interface.

- **Duplex**: *Communication mode* setting (Half or Full).

  - **Full-Duplex**: *Simultaneous two-way* communication without collisions.



**Spanning Tree Protocol (STP)**: Protocol *preventing Layer 2* network loops.

- **Loop Prevention**: *Blocking redundant paths* to avoid broadcast storms.

- **Rapid Spanning Tree Protocol (RSTP)**: *Faster convergence* version of Spanning Tree.



**Maximum Transmission Unit (MTU)**: *Largest data packet* size supported by interface.

- **Fragmentation**: *Breaking packets* to fit smaller MTU sizes.

- **Jumbo Frames**: Ethernet frames *exceeding standard 1500 byte* size.

  - **Overhead Reduction**: *Increasing efficiency* by sending more data per-header.



**Inter-VLAN Routing**: *Enabling traffic flow* between different VLANs.



**Power over Ethernet (PoE)**: Delivers *electrical power* via Ethernet cabling.

- **802.3af (PoE)**: Standard providing up to **15.4 watts**.

- **802.3at (PoE+)**: Standard providing up to **25.5 watts**.

- **802.3bt (PoE++)**: Standard providing up to **90 watts**.



**Switch Stacking**: *Managing multiple physical* switches as one logical unit.

### 2.3 Given a scenario, select and configure wireless devices and technologies



**Wireless Standards**: *Specifications defining* Wi-Fi speed and frequency.

- **802.11a**: 54 Mbps on **5 GHz band** (Legacy).

- **802.11b**: 11 Mbps on **2.4 GHz band** (Legacy).

- **802.11g**: 54 Mbps on **2.4 GHz band** (Legacy).

- **802.11n (Wi-Fi 4)**: 600 Mbps on **2.4/5 GHz** (MIMO).

  - **Multiple-Input Multiple-Output (MIMO)**: Using *multiple antennas* to increase throughput.

- **802.11ac (Wi-Fi 5)**: 1 Gbps+ on **5 GHz** (MU-MIMO).

  - **Multi-User MIMO (MU-MIMO)**: Supporting *simultaneous transmission* to multiple clients.

- **802.11ax (Wi-Fi 6)**: 10 Gbps on **2.4/5/6 GHz** (OFDMA).

  - **Orthogonal Frequency-Division Multiple Access (OFDMA)**: Dividing channels into *sub-carriers* for efficiency.



**Channels**: Specific *frequency ranges* for wireless communication.

- **Channel Width**: *Frequency span* used for data transmission (MHz).

- **Non-Overlapping Channels**: *Adjacent channels* that do not interfere (1,6,11).

- **Regulatory Impacts**: *Legal restrictions* on wireless frequency and power.

- **802.11h**: Standard for *dynamic frequency selection* and power.

  - **Dynamic Frequency Selection (DFS)**: Automatically *switching channels* to avoid radar interference.



**Frequency Options**: *Radio bands* available for wireless data transmission.

- **2.4GHz**: *Low-frequency* band with high penetration and range.

- **5GHz**: *High-frequency* band with high speed and capacity.

- **6GHz**: *Ultra-high* frequency band for Wi-Fi 6E devices.

- **Band Steering**: *Directing dual-band clients* to optimal frequency bands.



**Service Set Identifier (SSID)**: *Name identifying* a wireless network.

- **Basic Service Set Identifier (BSSID)**: Unique *MAC address identifying* a specific radio.

- **Extended Service Set Identifier (ESSID)**: Shared *network name across* multiple access points.



**Network Types**: Different *configurations* for wireless network connectivity.

- **Mesh Networks**: *Decentralized nodes* providing self-healing redundant pathways.

- **Ad Hoc**: *Peer-to-peer* connection without central infrastructure (IBSS).

- **Point-to-Point**: *Direct wireless link* between two specific locations.

- **Infrastructure**: Network *managed by* central access points (BSS).



**Encryption**: *Scrambling* wireless data to ensure privacy.

- **Wi-Fi Protected Access 2 (WPA2)**: *Security standard* using **AES-CCMP** for strong encryption.

- **Wi-Fi Protected Access 3 (WPA3)**: *Latest security* using **SAE** for individualized encryption.

- **Wi-Fi Protected Access (WPA)**: *Legacy security* replacing vulnerable WEP standard.

- **Wi-Fi Protected Setup (WPS)**: Simplified but *insecure* device connection method.



**Guest Networks**: *Isolated wireless segments* for temporary users.

- **Captive Portal**: *Webpage requiring interaction* before granting network access.



**Authentication**: *Verifying identity* of wireless clients before access.

- **Pre-Shared Key (PSK)**: *Shared passphrase* used by all network users.

- **Enterprise (802.1X)**: *Centralized authentication* using individual user credentials.

  - **RADIUS**: Server managing *centralized authentication* and authorization.



**Antennas**: Devices for *transmitting and receiving* radio waves.

- **Omnidirectional Antenna**: Radiating radio signals in *all directions equally*.

- **Directional Antenna**: Focusing radio signals in a *specific direction*.



**Autonomous vs. Lightweight Access Point**: *Standalone* management versus *controller-based* management.

- **Autonomous**: *Standalone access point* managing all local functions.

- **Lightweight Access Point**: *Controller-managed device* offloading logic to WLC.

- **Wireless LAN Controller (WLC)**: *Centralized appliance* managing multiple lightweight access points.

- **Control and Provisioning of Wireless Access Points (CAPWAP)**: *Protocol for communication* between APs and controllers.

### 2.4 Explain important factors of physical installations



**Important Installation Implications**: *Physical considerations* for deploying network equipment.

- **Locations**: Physical sites where network hardware is installed.

  - **Intermediate Distribution Frame (IDF)**: *Secondary rack* connecting end devices to MDF.

  - **Main Distribution Frame (MDF)**: *Primary central hub* for incoming service lines.

- **Rack Size**: Standardized width and height units (**U**).

- **Port-Side Exhaust/Intake**: *Airflow management* strategy to prevent equipment overheating.

- **Cabling**: *Physical wiring* used to interconnect network devices.

  - **Patch Panel**: Hardware for *organizing and reconfiguring* copper cables.

  - **Fiber Distribution Panel**: Specialized enclosure for *terminating/routing* fiber optic cables.

- **Lockable**: *Physical security* feature preventing unauthorized equipment access.



**Power**: *Electrical requirements* for operating network infrastructure.

- **Uninterruptible Power Supply (UPS)**: *Battery backup* providing near-instantaneous emergency power.

- **Power Distribution Unit (PDU)**: Device *distributing electric power* to rack equipment.

- **Power Load**: *Total electrical demand* of all connected devices.

- **Voltage**: *Potential difference* required for device electrical compatibility.



**Environment Factors**: *Physical conditions* affecting network equipment performance.

- **Humidity**: *Moisture level management* to prevent corrosion/static buildup.

- **Fire Suppression**: *Non-damaging systems* (gas/clean agent) for extinguishing fires.

- **Temperature**: *Level of heat* maintained to avoid malfunctions.

## 3.0 Network Operations 19%

Goal of Domain 3:

- This domain covers the management, documentation, monitoring, and resilience
  of networks.
- It focuses on the daily processes that keep the network functional, secure,
  and recoverable.

Things You Must Memorize:

- SNMP vs Syslog vs NetFlow vs SIEM
- RPO vs RTO vs MTTR
- VPN protocols and remote access tools
- Change management and configuration baselines
- Disaster recovery site types

### 3.1 Explain the purpose of organizational processes and procedures

**Documentation**: *Records describing* network architecture and operational policies.
- **Physical Diagram**: *Visual representation* of physical connections and locations.
- **Logical Diagram**: *Visual representation* of data flow and architecture.
- **Rack Diagram**: *Detailed view* of equipment mounted in racks.
- **Cable Map**: *Tracking* of physical cable paths and terminations.
- **Network Diagrams**: *Visualizing structure* across different OSI layers.
  - **Layer 1 Diagram**: *Mapping physical components*, cabling, and locations.
  - **Layer 2 Diagram**: *Illustrating VLANs*, switches, and data link paths.
  - **Layer 3 Diagram**: *Detailing IP addresses*, subnets, and routing protocols.
- **Asset Inventory**: *Detailed list* of hardware, software, and licenses.
  - **Hardware Inventory**: *Tracking specifications*, locations, and asset conditions.
  - **Software Inventory**: *Documenting versions*, configurations, and security patches.
  - **Licensing Management**: *Tracking usage rights*, expirations, and compliance.
  - **Warranty Support**: *Records* of service agreements and support claims.
- **IP Address Management (IPAM)**: *Software tracking* IP address allocation network-wide.
  - **Conflict Prevention**: *Organizing IP space* to avoid duplicate assignments.
- **Service-Level Agreement (SLA)**: *Contract defining* expected service performance standards.
  - **Performance Metrics**: *Agreed standards* for uptime, latency, and response.
- **Wireless Survey**: *Assessing radio frequency* coverage and performance.
  - **Wireless Heat Map**: *Visualizing signal strength* and coverage intensity.

**Life-Cycle Management**: Process of *managing hardware and software stages*.
- **End-of-Life (EOL)**: Point when manufacturer *stops production and sales*.
- **End-of-Support (EOS)**: Date when manufacturer *stops providing technical assistance*.
- **Software Management**: *Overseeing updates*, versions, and optimization.
  - **Patch Management**: *Systematic application* of bug fixes and vulnerabilities.
  - **Operating System (OS) Management**: *Regular maintenance* of device software environments.
  - **Firmware Management**: *Updating low-level code* controlling hardware functions.
- **Decommissioning**: *Safe removal and disposal* of network assets.

**Change Management**: *Formal process* for approving system modifications.
- **Service Request**: *Logging and analyzing* requests for configuration changes.

**Configuration Management**: Maintaining *consistent settings* across all network devices.
- **Production Configuration**: *Active settings* used in live operational environment.
- **Backup Configuration**: *Stored copy* of settings for disaster recovery.
- **Baseline/Golden Configuration**: *Standardized template* for consistent device deployment.
- **Version Control**: *Tracking and managing* configuration changes over time.

### 3.2 Given a scenario, use network monitoring technologies

**Methods**: *Techniques used* to collect network performance data.
- **Simple Network Management Protocol (SNMP)**: Protocol *monitoring and managing* network devices.
  - **Trap (SNMP)**: *Unsolicited alert message* sent by managed devices.
  - **Management Information Base (MIB)**: *Hierarchical database* defining properties of managed objects.
  - **SNMP v2c**: Version using *plain-text community strings* for authentication.
  - **SNMP v3**: *Secure version* providing strong encryption and authentication.
- **Flow Data**: *Statistics* on network traffic patterns (**NetFlow**).
  - **Metadata Analysis**: *Examining IP headers* without capturing full payloads.
- **Packet Capture (PCAP)**: *Intercepting and logging* data for deep inspection.
- **Baseline Metrics**: *Historical data* representing normal network performance levels.
  - **Anomaly Detection**: *Triggering warnings* when traffic deviates from baseline.
- **Log Aggregation**: *Consolidating log data* from multiple network sources.
  - **Syslog Collector**: *Server gathering* log messages from distributed devices.
  - **Security Information and Event Management (SIEM)**: *Real-time correlation* and analysis of security alerts.
- **Application Programming Interface (API)**: *Facilitating automated configuration* and data synchronization.
- **Port Mirroring (SPAN)**: *Copying traffic* to a designated monitoring port.

**Solutions**: *Specific tools or software* for network monitoring.
- **Network Discovery**: *Identifying devices* and mapping the network structure.
  - **Ad Hoc Discovery**: *Manual network scanning* performed on-demand.
  - **Scheduled Discovery**: *Automated scans* occurring at regular intervals.
- **Traffic Analysis**: *Examining data flow* to identify bandwidth bottlenecks.
- **Performance Monitoring**: *Tracking response times* and throughput for health.
- **Availability Monitoring**: *Checking uptime status* of critical network components.
- **Configuration Monitoring**: *Detecting setting changes* to ensure security compliance.

### 3.3 Explain disaster recovery (DR) concepts

**DR Metrics**: *Measurements used* to evaluate disaster recovery readiness.
- **Recovery Point Objective (RPO)**: *Maximum tolerable data loss* following a disaster.
  - **Data Age**: *Maximum acceptable age* of recovered backup files.
- **Recovery Time Objective (RTO)**: *Maximum time allowed* to restore services.
  - **Downtime Limit**: *Targeted duration* to resume business continuity.
- **Mean Time to Repair (MTTR)**: *Average time to fix* a failed device.
  - **Repair Efficiency**: *Measure of speed* returning system to normal.
- **Mean Time Between Failures (MTBF)**: *Average time before* a component fails.
  - **System Reliability**: *Calculated lifespan* of component between failure events.

**Backup Types**: *Different methods* for creating data copies.
- **Full Backup**: *Complete backup* of all data.
- **Incremental Backup**: *Backup of data changed* since last backup.
- **Differential Backup**: *Backup of data changed* since last full backup.
- **Offsite Backup**: *Storing backups* at a geographically separate location.

**DR Sites**: *Locations used* for recovering data and operations.
- **Disaster Recovery (DR)**: *Procedures for restoring* systems after failure.
- **Cold Site**: *Empty backup facility* requiring equipment setup.
  - **Infrastructure Only**: *Basic power and networking* without server hardware.
- **Warm Site**: *Partially equipped* backup site, not fully active.
  - **Partial Configuration**: *Pre-configured services* with delayed operational readiness.
- **Hot Site**: *Fully operational* backup site ready immediately.
  - **Mirror Site**: *Real-time synchronization* for immediate failover capability.

**High-Availability Approaches**: *Strategies for maintaining* continuous network service availability.
- **Active-Active**: *Redundant systems* simultaneously handling network traffic.
  - **Load Distribution**: *Simultaneous operation* maximizing throughput and performance.
- **Active-Passive**: *Backup system waiting* until primary system fails.
  - **Standby Mode**: *Ready system taking over* primary roles immediately.
- **Hardware Redundancy**: *Duplicate physical components* preventing single point failure.
- **Link Redundancy**: *Multiple network connections* providing failover paths.
- **Server Clustering**: *Group of servers* working together as single system.

**Testing**: *Assessing effectiveness* of disaster recovery and availability.
- **Tabletop Exercises**: *Theoretical drills* to test disaster response plans.
  - **Scenario Simulation**: *Discussion-based decision making* and gap identification.
- **Validation Tests**: *Practical assessments* confirming recovery procedures work.
  - **Process Execution**: *Actual restoration* to verify recovery objectives.

### 3.4 Given a scenario, implement IPv4 and IPv6 network services

**Dynamic Addressing**: *Automatic assignment* of IP addresses to devices.
- **Dynamic Host Configuration Protocol (DHCP)**: *Automates IP address assignment* to network clients.
  - **DORA Process**: *Discover, Offer, Request, Acknowledge* sequence for assignment.
  - **Reservations**: *Permanently assigning* specific IP to specific MAC.
  - **Scope**: *Defined range* of IP addresses for distribution.
  - **Lease Time**: *Duration* a client can use assigned IP.
  - **DHCP Options**: *Passing additional parameters* like DNS or NTP.
  - **Relay/IP Helper**: *Forwarding DHCP requests* across different subnets.
  - **Exclusions**: *Subsets of scope* not used for dynamic assignment.
- **Stateless Address Autoconfiguration (SLAAC)**: *IPv6 hosts generating* own addresses automatically.
  - **Neighbor Discovery (ND)**: *IPv6 mechanism* for finding local network information.

**Name Resolution**: *Process of translating* hostnames into IP addresses.
- **Domain Name System (DNS)**: *Resolves domain names* to IP addresses.
  - **DNSSEC**: *Digital signatures* verifying DNS data authenticity.
  - **DNS over HTTPS (DoH)**: *Encrypting DNS queries* via HTTPS protocol.
  - **DNS over TLS (DoT)**: *Encrypting DNS queries* via TLS protocol.
  - **Record Types**: *Different categories* of entries within DNS databases.
    - **Address Record (A)**: *Maps domain name* to IPv4 address.
    - **IPv6 Address Record (AAAA)**: *Maps domain name* to IPv6 address.
    - **Canonical Name (CNAME)**: *Alias mapping* one hostname to another.
    - **Mail Exchange (MX)**: *Specifies mail servers* for a domain.
    - **Text Record (TXT)**: *Holds arbitrary text* for external sources.
    - **Name Server (NS)**: *Identifies authoritative* DNS servers for domain.
    - **Pointer Record (PTR)**: *Maps IP address* to domain name.
  - **Zone Types**: *Classifications* of DNS database segments.
    - **Forward Zone**: *Resolving domain names* to IP addresses.
    - **Reverse Zone**: *Mapping IP addresses* back to hostnames.
    - **Primary Zone**: *Main read-write version* of a zone file.
    - **Secondary Zone**: *Read-only copy* used for backup/redundancy.
  - **Authoritative**: *Master source* containing the original DNS records.
  - **Recursive Query**: *Server retrieving* full answers from other servers.
- **Hosts File**: *Local text file* for manual DNS override.

**Time Protocols**: *Standards for synchronizing* clocks across network devices.
- **Network Time Protocol (NTP)**: *Synchronizes clocks* via hierarchical strata system.
  - **Hierarchical Strata**: *Levels of distance* from reference clock source.
- **Precision Time Protocol (PTP)**: *Nanosecond-level* clock synchronization for local networks.
- **Network Time Security (NTS)**: *Encryption and authentication* extension for NTP.

**Start of Authority (SOA)**: DNS record *identifying zone's authoritative* source.

### 3.5 Compare and contrast network access and management methods



**Site-to-Site VPN**: *Connecting two entire networks* securely.

- **Network Interconnection**: *Linking geographically dispersed* offices over public internet.

- **Virtual Private Network (VPN)**: *Encrypted tunnel* over a public network.



**Client-to-Site VPN**: *Remote user connecting* securely to corporate network.

- **Remote Access**: *Individual users accessing* internal resources via internet.

- **Clientless VPN**: *Secure resource access* through a web browser.

- **Split Tunnel**: *Routing only corporate* traffic through VPN tunnel.

  - **Path Efficiency**: *Local internet traffic bypasses* the VPN gateway.

- **Full Tunnel**: *Routing all user traffic* through VPN gateway.

  - **Complete Encryption**: *Ensuring all user traffic* is secured centrally.



**Connection Methods**: *Techniques used* to access and manage devices.

- **Secure Shell (SSH)**: *Encrypted remote login* replacing insecure Telnet protocol.

  - **Remote Management**: *Administrating network devices* from a distance securely.

- **Graphical User Interface (GUI)**: *Visual dashboard* for simplified device configuration.

- **Application Programming Interface (API)**: *Programmable interaction* for network automation and integration.

- **Console Connection**: *Direct physical access* for initial device setup.



**Jump Box/Host**: *Hardened intermediary* for accessing sensitive zones.

- **Security Gateway**: *Stepping stone* between different network trust levels.



**In-Band vs. Out-of-Band Management**: *Managing via primary* network or separate path.

- **In-Band Management**: *Administering devices* through the production data path.

- **Out-of-Band Management (OOB)**: *Dedicated management path* independent of data network.

  - **Outage Resilience**: *Ensuring device access* during primary network failure.

## 4.0 Network Security 14%

Goal of Domain 4:

- This domain focuses on identifying, preventing, and responding to security
  threats across networks.
- It covers foundational concepts, real-world threats, and best practices to
  harden devices and control access.

Things You Must Memorize:

- Definitions of CIA, AAA, and Zero Trust
- Malware and attack types (phishing, DoS, ARP spoofing)
- NAC technologies (802.1X, port security)
- Secure network protocols and their ports
- Authentication servers: RADIUS vs TACACS+

### 4.1 Explain the importance of basic network security concepts



**Logical Security**: *Software and procedural measures* protecting digital assets.



- **Encryption**: *Scrambling data* to prevent unauthorized access.

  - **Data in Transit**: Protecting data as it *travels across networks*.

    - **Interception Protection**: *Preventing eavesdropping* on active network communications.

  - **Data at Rest**: Protecting data *stored on physical storage* media.

    - **Theft Protection**: *Securing stored data* against unauthorized physical retrieval.

- **Certificates**: *Digital documents verifying identity* of network entities.

  - **Public Key Infrastructure (PKI)**: Framework *managing digital certificates* and keys.

    - **Trust Framework**: *System for issuing and validating* digital identities.

  - **Self-Signed**: Certificate *signed by its creator* rather than CA.

    - **Internal Trust**: *Establishing identity* within private, controlled environments.

- **Identity and Access Management (IAM)**: Framework of *policies and technologies* managing digital identities.

  - **Authentication**: *Verification of user identity* for network access.

    - **Multi-Factor Authentication (MFA)**: Verification requiring *two or more credential types*.

    - **Single Sign-On (SSO)**: *Single login granting access* to multiple systems.

    - **RADIUS**: *Centralized authentication* for users connecting to services.

    - **LDAP**: Protocol for *maintaining distributed directory* information services.

    - **SAML**: *XML-based standard* for exchanging authentication data.

    - **TACACS+**: Protocol for *AAA services separating core functions*.

    - **Time-based Authentication**: *Security tokens that change* at regular intervals.

  - **Authorization**: Process of *granting specific permissions* to users.

    - **Least Privilege**: Granting only *minimum necessary access rights*.

    - **Role-Based Access Control (RBAC)**: Access rights *based on user job function*.

  - **Accounting**: *Logging and auditing* user actions and resource usage.

- **Geofencing**: Creating *virtual boundaries* for geographic-based access control.



**Physical Security**: *Tangible barriers* protecting hardware and facility access.



- **Surveillance**: *Real-time monitoring* and recording of physical activities.

- **Entrance Control**: *Physical mechanisms preventing* unauthorized facility entry.



**Deception Technologies**: *Tools luring attackers* into decoy environments.



- **Honeypot**: *Decoy system luring attackers* to detect threats.

  - **Threat Intelligence**: *Gathering data* on attacker methods and behavior.

- **Honeynet**: *Network of decoys* simulating a real environment.



**Common Security Terminology**: *Standard vocabulary* describing security concepts.



- **Risk**: *Probability of threat exploiting* a vulnerability.

- **Vulnerability**: *Security weakness susceptible* to being exploited.

- **Exploit**: *Method or code used* to abuse vulnerability.

- **Threat**: *Potential cause* of an unwanted security incident.

- **Mitigation**: *Steps taken to reduce* risk or impact.

- **Defense in Depth**: *Layered security approach* using multiple controls.

- **Confidentiality, Integrity, and Availability (CIA) Triad**: *Core security model* for protecting information.



**Audits and Regulatory Compliance**: *Verifying adherence* to security policies and laws.



- **Data Locality**: Requirement for *data to stay in region*.

- **Payment Card Industry Data Security Standard (PCI DSS)**: Standards for *securing credit card transactions*.

- **General Data Protection Regulation (GDPR)**: *EU regulation protecting* personal data and privacy.



**Network Segmentation Enforcement**: Using *boundaries to isolate* network traffic segments.



- **Internet of Things (IoT)** and **Industrial Internet of Things (IIoT)**: *Networked physical objects* and industrial equipment.

- **SCADA / ICS / OT**: Systems *monitoring and controlling* industrial infrastructure.

- **Guest**: Isolated network segment for *temporary visitors*.

- **Bring Your Own Device (BYOD)**: Policy allowing *personal devices* on corporate networks.

### 4.2 Summarize various types of attacks and their impact to the network



**Denial-of-Service (DoS)** / **Distributed Denial-of-Service (DDoS)**

- **Denial-of-Service (DoS)**: Attack *preventing legitimate access* to resources.

  - **Traffic Overwhelming**: Rendering services unavailable via *excessive request volume*.

- **Distributed Denial-of-Service (DDoS)**: *DoS attack* from multiple sources simultaneously.

  - **Botnet**: Network of *compromised computers* performing coordinated attacks.



**VLAN Hopping**: Attacking by *moving between different VLANs* illegally.

- **Layer 2 Bypass**: *Circumventing network segmentation* to reach restricted zones.

- **Switch Spoofing**: Attacker *manipulates switch* into negotiating a trunk link.

- **Double Tagging**: Attacker *embeds second VLAN tag* to bypass security.



**Media Access Control (MAC) Flooding**: *Overwhelming switch MAC tables* with fake addresses.

- **Fail-Open Mode**: Switch *broadcasts all traffic* when table capacity exceeded.



**ARP Poisoning**: *Corrupting ARP cache* to map attacker's MAC.

- **MAC-to-IP Linking**: *Maliciously associating* attacker hardware address with legitimate IP.



**ARP Spoofing**: Sending *fake ARP messages* to intercept traffic.



**DNS Poisoning**: Injecting *fake DNS records* to redirect traffic.

- **Cache Corruption**: *Corrupting DNS resolver data* with fraudulent entries.



**DNS Spoofing**: *Redirecting users* to malicious sites via DNS.



**Rogue Devices and Services**: *Unauthorized hardware or software* on a network.

- **Rogue Devices**: *Unauthorized hardware* connected to a secure network.

- **Services**: *Unauthorized software-based functions* running on a network.

- **Rogue DHCP**: *Unauthorized server* distributing incorrect IP configurations.

- **Access Point (AP)**: Hardware device providing *wireless network connectivity*.

  - **Rogue Access Point**: *Unauthorized wireless access point* on a network.



**Evil Twin**: *Fake access point mimicking* a legitimate one.

- **SSID Masquerading**: *Deceiving users* via identical wireless network names.



**Man-in-the-Middle (MitM)**: Attacker *secretly intercepts and relays* communication.



**On-Path Attack**: *Intercepting communication* between two legitimate network nodes.

- **Eavesdropping**: *Secretly monitoring* private data exchange between parties.



**Social Engineering**: *Manipulating people* into divulging confidential information.

- **Human Manipulation**: Exploiting *psychology rather than technical hacking* methods.

- **Phishing**: *Fraudulent emails* tricking users into revealing info.

- **Spear Phishing**: *Targeted phishing attack* against specific individual/group.

- **Whaling**: Targeted phishing attack against *high-level executives*.

- **Vishing**: *Voice phishing* attacks conducted over phone.

- **Smishing**: Phishing attacks conducted via *SMS text messages*.

- **Pretexting**: *Fabricating a scenario* to steal information.

- **Dumpster Diving**: *Searching through trash* for sensitive information.

- **Shoulder Surfing**: *Watching someone enter* passwords or sensitive data.

- **Tailgating**: *Following authorized personnel* into restricted physical areas.



**Malware**: *Malicious software* designed to harm systems or data.

- **Virus**: *Malicious code requiring host* file to spread.

- **Worm**: *Self-replicates, spreads* across networks without host.

- **Trojan**: Malicious software *masquerading as legitimate* application.

- **Ransomware**: *Encrypts files, demands payment* for decryption.

- **Spyware**: Software *secretly recording* user activity and data.

- **Adware**: Software *automatically displaying* unwanted advertisements.

- **Keylogger**: Software *recording every keystroke* made by user.

- **Rootkit**: Malware *granting administrative control* while hiding presence.

### 4.3 Given a scenario, apply network security features, defense techniques, and solutions



**Device Hardening**: *Securing a system* by reducing attack surface.

- **Attack Surface Reduction**: *Minimizing vulnerability* by disabling unnecessary functions.

- **Disable Unused Ports and Services**: *Closing entry points* to minimize security risks.

- **Change Default Passwords**: Replacing *factory-set credentials* with secure ones.



**Network Access Control (NAC)**: *Controlling device admission* to the network.

- **Port-based Network Access Control (PNAC)**: *Authenticating devices* at the point of connection.

- **Port Security**: *Limiting network port access* by MAC address.

  - **MAC Limiting**: *Restricting number of devices* per physical port.

- **802.1X**: IEEE standard for *port-based network authentication*.

- **MAC Filtering**: *Allowing or denying* network access by MAC.



**Key Management**: *Secure handling and storage* of cryptographic keys.

- **Key Lifecycle**: Managing *creation, distribution, rotation*, and revocation.



**Security Rules**: *Definitions controlling traffic* flow through security devices.

- **Access Control List (ACL)**: Rules determining *access rights* to network resources.

  - **Traffic Filtering**: *Allowing or denying packets* via IP/Port/Protocol rules.

- **Uniform Resource Locator (URL) Filtering**: *Restricting website access* based on web addresses.

- **Content Filtering**: *Blocking access* to specific types of data.

- **Unified Threat Management (UTM)**: *All-in-one security appliance* for network protection.



**Firewall Types**: Hardware or software *monitoring and controlling* network traffic.

- **Packet Filtering Firewall**: Filters traffic based on *IP headers and ports*.

- **Stateful Firewall**: *Tracks active connections* to make filtering decisions.

- **Next-Generation Firewall (NGFW)**: *Deep packet inspection* and application-level control.

- **Host-based Firewall**: *Software firewall* running on a single device.



**Zones**: *Logical network areas* with distinct security requirements.

- **Trust Segmentation**: *Isolating resources* based on varying trust levels.

- **Trusted vs. Untrusted**: *Internal secure network* versus external insecure network.

- **Screened Subnet (DMZ)**: *Buffer zone hosting* public-facing services securely.

  - **Perimeter Defense**: *Isolating public services* from the internal network.

## 5.0 Network Troubleshooting 24%

Goal of Domain 5:

- This domain covers how to approach, diagnose, and resolve a wide variety of
  network issues using structured methodologies and tools. It represents the
  largest percentage of the exam and is vital for real-world technical
  troubleshooting.

Things You Must Memorize:

- The 6-step troubleshooting process
- Common errors: CRC, colisions, flapping, duplex mismatch
- DHCP/DNS/NAT failure symptoms and fixes
- Wireless performance problems (interference, signal loss)
- CLI tools and when to use them: ping, tracert, ipconfig, netstat, nslookup

### 5.1 Explain the troubleshooting methodology



1. **Identify the Problem**: *Gather information*, symptoms, and recent changes.

- **Gather Information**: *Collecting issue details* from logs and performance data.

  - **Scope/Impact**: Determining the *number of systems affected* by issue.

- **Question Users**: Interviewing individuals to get *firsthand problem descriptions*.

  - **Symptom Fact-finding**: Gathering clues *not evident in automated* system logs.

- **Identify Symptoms**: Noting *specific signs and behavior* of network failure.

- **Determine if Anything Has Changed**: Investigating *recent updates* or hardware modifications.

- **Duplicate the Problem**, if possible: *Recreating issue* in a controlled environment for testing.

- **Approach Multiple Problems Individually**: Resolving *each separate issue* one at a time.

- **Define Scope**: Establishing *boundaries* of the troubleshooting effort.



2. **Establish a Theory of Probable Cause**: *Brainstorm probable causes* starting with the obvious.

- **Question the Obvious**: Checking for *simple, frequent oversights* like disconnected cables.

  - **Obvious Failures**: Eliminating *straightforward issues* before complex diagnostic steps.

- **Consider Multiple Approaches**: Keeping an *open mind* to various potential solutions.

  - **Top-to-Bottom/Bottom-to-Top OSI Model**: *Systematic verification* of network layers in sequence.

    - **Systematic Verification**: Ensuring *no individual layer* is overlooked during testing.

    - **Top-to-Bottom**: Troubleshooting starting from **Application layer down to Physical**.

    - **Bottom-to-Top**: Troubleshooting starting from **Physical layer up to Application**.

  - **Divide and Conquer**: *Narrowing down* problem location by bisecting system.

    - **Section Isolation**: *Isolating specific segments* to identify the failure point.



3. **Test the Theory to Determine the Cause**: *Confirm the cause* or escalate if incorrect.

- **Theory Validation**: Applying *practical methods* to verify hypothesized root cause.

- **Escalation**: Referral of a problem to a *senior technician* or third party.

  - **Escalation Criteria**: Identifying when problem *exceeds current knowledge* or resources.

- If theory is confirmed, determine next steps to resolve problem

- If theory is not confirmed, establish a new theory or escalate



4. **Establish a Plan of Action**: to resolve the problem and identify potential effects: *Determine steps to fix* and assess impact.

- **Impact Assessment**: Evaluating how *proposed fixes affect* the wider network.

- Implement fix with *minimal disruption*

- Schedule *downtime* if needed.



5. **Implement the Solution** or escalate as necessary: *Execute the fix* or escalate if needed.

- **Disruption Mitigation**: *Minimizing network downtime* during solution execution.



6. **Verify Full System Functionality** and implement preventive measures if applicable: *Confirm system works* and prevent recurrence.

- **User Acceptance**: *Confirming with affected users* that problem is resolved.

- Test full services and related systems

- Confirm with user



7. **Document Findings, Actions, Outcomes, and Lessons Learned** throughout the process: *Record actions, outcomes*, and lessons learned.

- **Knowledge Base**: Creating *visual and textual records* for future reference.

- Record the problem, resolution, and timeline

- Useful for *audits training*, and trend tracking



**Best Practices**:

- Follow **change control** if required

- Use **rollback plan** in case the fix fails

- Maintain **communication** with stakeholders

### 5.2 Given a scenario, troubleshoot common cabling and physical interface issues



**Cable Issues**: *Physical layer failures* related to network wiring.

- **Incorrect Cable**: Using the *wrong type* of network cabling.

  - **Category Mismatch**: Using cabling *unsupported* for required network speeds.

  - **Single-Mode vs. Multimode**: *Long-distance laser* vs *short-distance LED* fiber.

    - **Signal Dispersion**: *Light spreading* in multimode fiber over distance.

  - **STP vs. UTP**: *Shielded* versus *unshielded* copper network cabling.

    - **EMI Protection**: *Shielding required* in high electromagnetic interference environments.

- **Signal Degradation**: *Reduction in signal quality* during transmission.

  - **Crosstalk**: *Signal bleeding* between adjacent copper wires.

    - **NEXT / FEXT**: *Near-End or Far-End interference* between pairs.

  - **Interference (EMI/RFI)**: *External signals disrupting* network transmission.

  - **Attenuation**: *Gradual loss of signal strength* over distance.

- **Improper Termination**: *Poorly attached connectors* causing physical layer failures.

  - **Signal Reflection**: *Impedance mismatch* causing signal to bounce back.

- **Transmitter (TX)/Receiver (RX) Transposed**: Sending and receiving *wires swapped* incorrectly.

- **Open Circuit**: *Break in the connection* preventing signal flow.

- **Short Circuit**: *Accidental connection* between two distinct electrical paths.

- **Incorrect Pinout**: Wires *connected to wrong pins* in connector.

- **Distance Limitation**: *Exceeding maximum cable length* causes signal loss.

- **Bend Radius**: *Minimum curve allowed* before damaging fiber cable.



**Interface Issues**: *Failures occurring* at the device connection point.

- **Increasing Interface Counters**: Statistics tracking *errors on a specific port*.

  - **Cyclic Redundancy Check (CRC)**: Error-detecting code indicating *corrupted data frames*.

    - **Checksum Mismatch**: *Frame data changed* during network transit.

  - **Runts**: Ethernet frames *smaller than permitted* 64 bytes.

  - **Giants**: Ethernet frames *exceeding standard* 1518 byte size.

  - **Drops**: Packets *discarded* due to congestion or errors.

    - **Buffer Overflow**: Data discarded when *switch memory capacity exceeded*.

- **Port Status**: The *operational state* of a network interface.

  - **Error Disabled**: Port *shut down by switch* due to errors.

  - **Administratively Down**: Port *manually disabled* by network administrator.

  - **Suspended**: Port *inactive* due to protocol negotiation failure.



**Hardware Issues**: *Physical component failures* within network devices.

- **Power over Ethernet (PoE)**: *Transmitting power* over standard Ethernet cabling.

  - **Power Budget Exceeded**: Connected device demand *exceeding switch power capacity*.

  - **Incorrect Standard**: *Mismatch* between PoE device and switch requirements.

- **Transceivers**: *Modular components* for connecting to fiber networks.

  - **Mismatch**: *Incompatible transceiver type* or speed on link.

  - **Signal Strength**: *Optical or electrical power level* issues.

- **Dirty Connector**: *Contaminants* on fiber interface blocking light signal.

### 5.3 Given a scenario, troubleshoot common issues with network services



**Switching Issues**: *Failures related* to Layer 2 network operations.

- **Spanning Tree Protocol (STP)**: Protocol *preventing Layer 2 loops*.

  - **Network Loops**: *Broadcast storms* caused by multiple active paths.

  - **Root Bridge Selection**: *Electing central reference point* via Bridge ID.

    - **Bridge Priority**: *Configurable value* determining the root bridge switch.

  - **Port Roles**: Specific *functional assignments* (Root, Designated, Blocked).

  - **Port States**: *Transition sequence* ensuring network stability (Listening, Learning).

- **Incorrect VLAN Assignment**: *Misconfiguring ports* into wrong broadcast domains.

  - **VLAN Mismatch**: *Inconsistent VLAN configurations* across connected switch ports.

- **Access Control List (ACL)**: Rules *determining access rights* to network resources.

  - **Policy Conflict**: *Misconfigured rules blocking* legitimate network traffic.



**Route Selection**: Problems related to *determining data packet paths*.

- **Routing Table**: *Database used* for determining data packet paths.

  - **Stale Routes**: *Invalid routing entries* causing packet misdirection.

- **Default Routes**: Path used when *no specific destination* exists.

  - **Missing Default Route**: *Dropped packets* due to unknown destination path.



**Address Pool Exhaustion**: *Depletion* of available IP addresses in scope.

- **Over-subscription**: *Device count exceeding* available DHCP pool addresses.

- **Lease Release**: *Mechanism* for returning expired IPs to pool.



**Incorrect Default Gateway**: *Wrong IP address* configured for local exit.

- **Subnet Exit Error**: *Gateway IP residing* outside local subnet range.



**Incorrect IP Address**: *Invalid or misconfigured* IP on a device.

- **Manual Configuration Errors**: *Typographical mistakes* during static IP assignment.

- **Duplicate IP Address**: *Two devices assigned* same IP, causing conflict.



**Incorrect Subnet Mask**: *Misconfigured mask* leading to communication errors.

- **Subnet Incompatibility**: *Devices failing communication* due to mask mismatch.



- **Automatic Private IP Addressing (APIPA)**: *Self-assigned IP* indicating DHCP failure.

- **Maximum Transmission Unit (MTU) Mismatch**: *Packet size mismatch* causing fragmentation or drops.

### 5.4 Given a scenario, troubleshoot common performance issues



**Congestion/Contention**: Network slowing due to *high traffic volume*.

- **Capacity Overload**: *Demand exceeding* the available network resource bandwidth.



**Bottlenecking**: Point of congestion *limiting overall performance*.

- **Device Oversubscription**: *Single component restricting* the entire network flow.



**Bandwidth**: *Maximum data transfer rate* of a network.

- **Throughput**: Actual rate of *successful data packet delivery*.

  - **Successful Delivery Rate**: *Measuring effective data transfer* after protocol overhead.



**Latency**: *Time delay* for data to reach destination.

- **Propagation Delay**: *Time required* for signal to traverse medium.



**Packet Loss**: Data units *failing to reach* their destination.

- **Retransmission Overhead**: *Increased traffic caused* by repeating lost packets.



**Jitter**: *Variation* in packet arrival time.

- **Arrival Variation**: *Inconsistent timing* between packets in a stream.



**Wireless performance issues** *disrupting connectivity* and data flow.

- **Interference**: *External signals disrupting* wireless network communication.

  - **Channel Overlap**: Multiple access points *using identical frequency ranges*.

- **Signal Degradation or Loss**: *Reduction* in wireless signal quality or strength.

- **Insufficient Wireless Coverage**: Areas with *weak or absent signal*.

  - **Dead Zones**: *Geographic locations* where wireless connectivity is unavailable.

- **Client Disassociation Issues**: Devices *repeatedly losing connection* to access points.

- **Roaming Misconfiguration**: Failure of clients to *switch between APs smoothly*.

  - **Handoff Failure**: *Interruption* when client moves between access points.

- **Access Point (AP) Overload**: *Too many clients* degrading wireless performance.

### 5.5 Given a scenario, use the appropriate tool or protocol to solve networking issues

**Software Tools**: *Applications used* for network analysis and troubleshooting.
- **Protocol Analyzer**: *Captures and decodes* network traffic for analysis.
  - **Packet Capture (PCAP)**: *Intercepting and logging data* for deep inspection.
- **Command Line**: *Text-based interface* for precise device management.
  - **Ping**: Tests connectivity and measures *round-trip time* (ICMP).
  - **Traceroute**: Maps *path to destination* showing every hop.
  - **Nslookup**: *Queries DNS servers* to resolve hostnames.
  - **Tcpdump**: Command-line utility for *capturing and filtering* packets.
  - **Domain Information Groper (DIG)**: Retrieves *detailed DNS record* information and diagnostics.
  - **Netstat**: Displays *active connections*, routing tables, and statistics.
  - **IPConfig/Ifconfig/IP**: *Displays and configures* network interface settings.
  - **Address Resolution Protocol (ARP)**: Manages *IP-to-MAC address translation* tables.
- **Nmap**: Discovers *devices and services* via network scanning.
  - **Network Scanning**: *Sending packets* to identify active network nodes.
- **Link Layer Discovery Protocol (LLDP)**: *Vendor-neutral protocol* for discovering neighboring devices.
- **Cisco Discovery Protocol (CDP)**: Cisco-proprietary protocol for *identifying directly connected* devices.
  - **Neighbor Discovery**: *Exchanging identity and capability* information between devices.
- **Speed Tester**: Measures network connection *bandwidth and throughput*.
  - **Performance Evaluation**: Identifying *bandwidth bottlenecks*, latency, and jitter.

**Hardware Tools**: *Physical devices* used for network testing and maintenance.
- **Toner**: *Traces and identifies* wires within a bundle.
  - **Tone Generator**: *Sends signal* through cable for probe detection.
- **Cable Tester**: Verifies *physical integrity* and performance of cables.
  - **Continuity Testing**: Checking for *shorts, opens, and cross-connections*.
- **Network Tap (TAP)**: Provides *passive access* to network data flow.
  - **Packet Mirroring**: *Copying traffic* for monitoring without service interruption.
- **Wi-Fi Analyzer**: *Scans and analyzes* wireless network signals.
  - **Signal Analysis**: Measuring *strength, channel usage*, and interference sources.
- **Visual Fault Locator (VFL)**: Laser tool for *finding fiber optic breaks*.
- **Time Domain Reflectometer (TDR)**: *Locates breaks or faults* in copper cables.
- **Optical Time Domain Reflectometer (OTDR)**: Locates *breaks or faults* in fiber cables.
  - **Fault Localization**: *Pinpointing cable damage* locations via signal reflection.
- **Multimeter**: Measures *electrical properties* like voltage and resistance.
- **Loopback Plug**: Tests *physical port transmit* and receive functionality.
- **Spectrum Analyzer**: Visualizes *signal strength* across frequency bands.

**Basic Networking Device Commands**:
- **Show MAC-Address-Table**: Displays *associated MAC addresses* and switch ports.
- **Show Route**: Displays *routing table entries* and next-hop addresses.
- **Show Interface**: Provides *detailed interface status* and traffic statistics.
- **Show Config**: Displays device *running configuration* and security settings.
- **Show ARP**: *Maps IP addresses* to MAC addresses (Resolution).
- **Show VLAN**: Displays *virtual network IDs* and port assignments.
- **Show Power**: Monitors *PoE allocation* and device power consumption.
