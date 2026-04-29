CERTIFICATION

Xpert Series

CompTIA CloudNetX
Certification Exam
Objectives
EXAM NUMBER: CNX-001 V1

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

About the Exam
The CompTIA CloudNetX CNX-001 V1 certification exam will certify the successful candidate has the knowledge
and skills required to:
• Analyze business requirements to design and configure secure network architecture for on-premises and
cloud environments.
• Analyze requirements to design for network security, availability, Zero Trust, and identity and access
management technologies.
• Apply and configure concepts and tools related to network monitoring and performance, automation,
and scripting.
• Troubleshoot network issues related to connectivity, performance, access, and security.
• Perform network operation and maintenance.
EXAM ACCREDITATION
The CompTIA CloudNetX CNX-001 V1 exam is accredited by the ANSI National Accreditation Board (ANAB) to show
compliance with the International Organization for Standardization (ISO) 17024 standard and, as such, undergoes
regular reviews and updates to the exam objectives..
EXAM DEVELOPMENT
CompTIA exams result from subject matter expert workshops and industry-wide survey results regarding the skills
and knowledge required of an IT professional.
COMPTIA AUTHORIZED MATERIALS USE POLICY
CompTIA Certifications, LLC is not affiliated with and does not authorize, endorse, or condone utilizing any content
provided by unauthorized third-party training sites (aka “brain dumps”). Individuals who utilize such materials in
preparation for any CompTIA examination will have their certifications revoked and be suspended from future
testing in accordance with the CompTIA Candidate Agreement. In an effort to more clearly communicate CompTIA’s
exam policies on use of unauthorized study materials, CompTIA directs all certification candidates to the CompTIA
Certification Exam Policies. Please review all CompTIA policies before beginning the study process for any CompTIA
exam. Candidates will be required to abide by the CompTIA Candidate Agreement. If a candidate has a question
as to whether study materials are considered unauthorized (aka “brain dumps”), they should contact CompTIA at
examsecurity@comptia.org to confirm.
PLEASE NOTE
The lists of examples provided in bulleted format are not exhaustive lists. Other examples of technologies, processes,
or tasks pertaining to each objective may also be included on the exam, although not listed or covered in this
objectives document. CompTIA is constantly reviewing the content of our exams and updating test questions to be
sure our exams are current, and the security of the questions is protected. When necessary, we will publish updated
exams based on existing exam objectives. Please know that all related exam preparation materials will still be valid.

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

TEST DETAILS
Required exam

CloudNetX CNX-001 V1

Number of questions

Maximum of 90

Types of questions

Multiple-choice and performance-based

Length of test
Recommended experience

A minimum of ten years of experience in the IT field and five years of
experience in a network architect role, with experience in the hybrid cloud
environment. Network+, Security+, and Cloud+ or equivalent experience.

Passing Score

Pass/fail only; no scaled score

EXAM OBJECTIVES (DOMAINS)
The table below lists the domains measured by this examination and the extent to which they are represented.
DOMAIN

PERCENTAGE OF EXAMINATION

1.0
2.0
3.0
4.0

Network Architecture Design				
Network Security					
Network Operations, Monitoring, and Performance		
Network Troubleshooting					

31%
28%
16%
25%

Total

							

100%

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

				

1.0 Network Architecture Design
1.1

Given a scenario, analyze business requirements to apply core networking concepts to a
network design.
• Open Systems Interconnection (OSI) model
• Internet Protocol (IP) addressing
− IPv4
− IPv6
− IP subnetting
− Classless Inter-domain Routing (CIDR) notation
− Variable Length Subnet Mask (VLSM)
− Public vs. private
− Static vs. dynamic
• Network address translation (NAT)
− Port forwarding
− Port address translation (PAT)
− NAT64
• Networking protocols
− Transmission Control Protocol (TCP)/
User Datagram Protocol (UDP)
− Authentication protocols
◦ Power and cooling
◦ 802.1X
◦ Remote Authentication Dial-in User Service (RADIUS)

1.2

◦ Terminal Access Controller Access
Control System Plus (TACACS+)
◦ Lightweight Directory Access Protocol (LDAP)
− Routing protocols
◦ Dynamic
▪ Open Shortest Path First (OSPF)
▪ Border Gateway Protocol (BGP)
◦ Static
▪ Routing tables
− Dynamic Host Configuration Protocol (DHCP)
− Network Time Protocol (NTP)
− Domain Name System (DNS)
◦ Domain Name System Security Extensions (DNSSEC)
◦ DNS over Transport Layer Security (TLS) (DoT)
◦ DNS over Hypertext Transfer Protocol
Secure (HTTPS) (DoH)
• Container networking
• Network virtual interfaces

Given a scenario, analyze business requirements to select and implement the appropriate
network architectures and topologies.
• Topology types
− Mesh
− Star
− Hub-and-spoke
− Spine-and-leaf
− Point-to-point

• Segmentation
− Virtual local area network (VLAN)
− Virtual extensible LAN
(VXLAN)
− Generic Network Virtualization
Encapsulation (GENEVE)

• Zones
− Trusted
− Untrusted
− Screened subnet

• Environments
− Production
− Non-production

• Traffic flows
− North/south
− East/west

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

1.0 | Network Architecture Design

1.3

Given a scenario, analyze requirements to select appropriate connectivity solutions in a
hybrid environment.
• Multiprotocol Label
Switching (MPLS)
• Software-defined wide area
network (SD-WAN)
• Cellular
• Satellite
• Dark fiber
• Direct internet access
• Metro network
• Public cloud connectivity
− ExpressRoute
− Direct Connect

1.4

• Remote access
− Bastion host
− Secure Shell (SSH)
− Remote Desktop Protocol
(RDP)
• Application gateways
• Private Platform as a Service
(PaaS) connectivity
− Service endpoints

− Transit gateways
− Virtual private cloud
(VPC) peering
− Private link
• Virtual private network (VPN)
− Site-to-site
− Point-to-site
− Remote access
− Split tunneling
− WireGuard

Given a scenario, analyze availability requirements to recommend technologies that meet
business needs.
• Load balancing
− Global
− Local
− Virtual IP (VIP)
− Methods
◦ Round robin
◦ Load-based
◦ Least connections
◦ Weighted

1.5

− Software-defined cloud
interconnect (SDCI)

• High availability
− Active-active
− Active-passive
• Link aggregation
• Autoscaling
• Regions and availability zones
• Content delivery network (CDN)
• Fault domains

• Update domains
• Redundancy
− Devices
− Paths

Given a scenario, evaluate business requirements to make recommendations for physical
campus installations.
• Power considerations
− Voltage
− Wattage
− Amperage
− Power distribution unit (PDU)
− Uninterruptible power supply (UPS)
− Utility power
− Emergency power off (EPO)
− Backup power generators

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

• Power disruption
− Blackout
− Brownout
− Surge
− Spike
• Environmental factors
− Temperature
− Humidity
− British thermal units (BTUs)

• Fire suppression
• Physical access controls
− Video surveillance
− Biometrics
− Proximity readers
− Locks and keys
− Near-field communication
(NFC)
− Door sensors

1.0 | Network Architecture Design

1.6

Given a scenario, analyze business requirements to select the appropriate campus wired
network components.
• Layer 2 vs. Layer 3
− Switch
− Router
• Power over Ethernet (PoE)
• Three-tier hierarchy
− Core
− Distribution
− Access
• Collapsed core
• Intermediate distribution frame
(IDF)/Main distribution frame (MDF)
− Cable management

1.7

• Customer premises
equipment (CPE)
− Media converters

Given a scenario, analyze business requirements to select the appropriate campus wireless
network components.
• Wi-Fi
− Wireless access points
◦ Antenna types
▪ Omni-directional
▪ Directional
◦ Placement
◦ Enclosure
◦ Power considerations
− Controllers
− Standards and protocols

1.8

• Spanning Tree Protocol (STP)
• Tagging/trunking
• Bonding
• Voice and video
− Session Initiation Protocol (SIP)
− WebRTC
− Real-time Streaming
Protocol (RTSP)
− H.323

◦ 802.11
− Frequencies
◦ 2.4GHz
◦ 5GHz
◦ 6GHz
− Channels
− Service set identifier (SSID)
◦ Hidden vs. advertised
− Wireless roaming

• Bluetooth Low Energy (BLE)
• NFC
• Long-range wide area
network (LoRaWAN)

Given a scenario, analyze requirements to select the appropriate artifacts for architecture
documentation.
• Requirements analysis
− Business
− Technical
− Regulatory compliance
− Statement of work (SOW)
• Network diagramming
− Physical vs. logical
− High-level vs. low-level designs
− Flow diagrams

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

• Verification and validation
• Runbooks
• Work breakdown structure (WBS)
• Knowledge base articles
• Baselines
• Reference architectures
− External
− Internal
• Configuration management
database (CMDB)

2.0 Network Security
2.1

Explain common cloud and network threats, vulnerabilities, and mitigations.
• Threats
− Distributed denial-ofservice (DDoS) attack
− Data exfiltration
− On-path attack
− Credential reuse
− Brute-force attack
− Out-of-band (OOB) attack
− IP spoofing
− Buffer overflow
− Privilege escalation
− Insider threat
− Evil twin
− Rogue access point

2.2

• Vulnerabilities
− Zero-day
− Open Worldwide Application
Security Project (OWASP) top 10
− Overly permissive rules
− IP reuse
− Legacy access control lists (ACLs)
− Insecure protocols
− Unpatched devices
− Misconfigurations

• Mitigations
− Input sanitization
− Data loss prevention (DLP) controls
− IP address management (IPAM)
− MITRE ATT&CK Framework
− Cyber Kill Chain
− Cloud Controls Matrix (CCM)
− Patch management
− Vulnerability management
− Center for Internet Security
(CIS) benchmarks
− Configuration reviews
− Null routing

Given a scenario, analyze requirements to select the appropriate technology to secure a
network.
• Firewalls
− Next-generation firewall (NGFW)
− Cloud-native firewall
− Web application firewall (WAF)
• Intrusion prevention system (IPS)/
intrusion detection system (IDS)
• Encryption

2.3

− Initialization vector attack
− BGP hijacking
− Social engineering attack

− Protocol types
− Secure sockets layer
(SSL)/TLS inspection
− Cipher suites
− Algorithms
− Asymmetric
− Symmetric

• Application gateway
• Secure web gateway
• Network access control (NAC)
− Posture assessment
• Dynamic list

Given a scenario, configure the appropriate access controls to secure a network.
• Firewall rules
− Decryption rules
− Application aware
− Source and destination
− Allow list
− Block list
• Network access control lists
(NACLs)
• Network security groups
− Inbound rules
− Outbound rules

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

• IPS/IDS signature rules
• Geolocation rules
• Content/Uniform Resource
Locator (URL) filtering
− Categories
− Applications
− File blocking
• DLP controls
• Port security

2.0 | Network Security

2.4

Given a scenario, analyze requirements to apply the appropriate Zero Trust architecture
(ZTA) principles to secure a network.
• Microsegmentation
• Secure Access Service Edge (SASE)
− Secure Service Edge (SSE)
• Cloud Access Security
Broker (CASB)
• Identity as the perimeter
• Device trust
• Principle of least privilege
• Zero Trust network access

2.5

Given a scenario, apply identity and access management to secure a network environment.
• Single sign-on (SSO)
− Federation
− Security Assertion Markup
Language (SAML)
− OAuth 2.0
− OpenID Connect (OIDC)
− Passwordless
• Multifactor authentication (MFA)
• Conditional access
• Geofencing
• Privileged access

2.6

management (PAM)
• Risk-based authentication
• Role-based access control
• Attribute-based access
control (ABAC)
• Endpoint trust
• User and entity behavior
analytics (UEBA)
• Public key infrastructure (PKI)
− Certificate-based authentication
− Key management system (KMS)

• Session-based tokens
• Just-in-time (JIT) provisioning
• System for Cross-domain
Identity Management (SCIM)
• Cloud Infrastructure Entitlement
Management (CIEM)

Given a scenario, use the appropriate wireless security method or configuration.
• Encryption
− Advanced Encryption
Standard (AES)
− Wi-Fi Protected Access 2 (WPA2)
− Wi-Fi Protected Access 3 (WPA3)

• Guest access
• Captive portal
• Layer 2 client isolation
• Media access control (MAC)
address filtering

• Authentication
− Temporal Key Integrity
Protocol (TKIP)
− Preshared key (PSK)
− PSK enterprise

2.7

Given a scenario, implement the appropriate appliance-hardening technique.
• Patch management
− Delivery channels
− Verification

− Password complexity
− Password length
− Password rotation

• Default credential management
• Disabling unneeded services
• Local password management

• Protocol configuration
− Disabling insecure protocols

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

• Restricting access to
administrative interfaces
• Disabling unused physical ports
• Log management
− Log rotation
− Remote logging

3.0 Network Operations, Monitoring,
and Performance
3.1

Explain concepts related to operating and maintaining a network environment.
• Risk management
− Risk acceptance
◦ Waivers and exceptions
− Risk avoidance
− Risk transference
− Risk mitigation
− Risk register
• Business continuity
− Mean time to recovery (MTTR)
− Mean time between
failures (MTBF)
− Mean time to detect (MTTD)
− Mean time to investigate (MTTI)
− Recovery point objective (RPO)/
recovery time objective (RTO)
• Disaster recovery
• Service management

3.2

• Auditing
• Failure rate
• Contracts, agreements, and terms
− Interconnection Security
Agreement (ISA)
− Memorandum of
understanding (MOU)
− Master service agreement (MSA)
− Service-level indicator (SLI)/
key performance indicator (KPI)
− Service-level objective (SLO)
− Service-level agreement (SLA)
− Operational-level agreement (OLA)
− Non-disclosure agreement (NDA)
− Licensing agreements
− End-of-life (EOL)/endof-support (EOS)

virtualization (NFV)
− Firewall as a service
− Reverse proxy
− Forward proxy
− NAT gateways
• OOB management
• Network cost management
− Operating expenditure (OpEx)
− Capital expenditure (CapEx)
− Cost optimization
− Chargeback model
− Orphaned resources
• Service delivery
− Self-service
− Cross-connect
− Time to market

• Network function

Given a scenario, use tools and techniques related to monitoring and performance.
• Traffic analysis
− Traffic mirroring
− Throughput
− Latency
− Loss
− Jitter
− Network flows
− Reachability
• Log collection
− Centralized logging

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

− Security information and
event management (SIEM)
− Syslog
− JavaScript Object Notation (JSON)
− Data lake
• Simple Network Management
Protocol (SNMP)
• Quality of service (QoS)
• Alerting
• Telemetry

• Dashboards
− Status pages
• Metrics
• Continuous monitoring
− Resource utilization
− Bandwidth utilization
− Reactive vs. proactive monitoring

3.0 | Network Operations, Monitoring, and Performance

3.3

Given a scenario, apply automation and scripting to administer a hybrid cloud
environment.
• Infrastructure as code (IaC)
− Resource provisioning
− Resource configuration
− Yet Another Markup
Language (YAML)
− JSON
− Linters
• Life cycle management
− Mutable infrastructure
− Immutable infrastructure
− Patch management

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

• Version control
− Public vs. private repositories
− Secrets management
• DevOps
− Continuous integration and
continuous delivery (CI/CD)
pipeline management
− GitOps
• Generative artificial intelligence (AI)
• Application programming
interface (API)

• Software development kit (SDK)
• Command-line interface (CLI)
• Desired state
− Configuration reviews
− Baselines/benchmarks
− Configuration backup
and restore
• Change management

4.0 Network Troubleshooting
4.1

Explain the troubleshooting methodology.
• Identify the problem
− Gather information
− Question users
− Identify symptoms
− Determine if anything has changed
− Duplicate the problem, if possible
− Approach multiple
problems individually
• Establish a theory of probable cause
− Question the obvious
− Consider multiple approaches
◦ Top-to-bottom/bottomto-top OSI model
◦ Divide and conquer

4.2

• Document findings, actions,
outcomes, and lessons learned
throughout the process

• Establish a plan of action
to resolve the problem and
identify potential effects
• Implement the solution or
escalate as necessary
• Verify full system functionality
and if applicable implement
preventive measures

Given a scenario, use the appropriate tool or command.
• Tools
− Wireshark
− Netcat
− Nmap
− Iperf
− radclient
− OpenSSL
− Postman
• Commands
− tcpdump

4.3

• Test the theory to determine cause
− If the theory is confirmed,
determine the next steps
to resolve the problem
− If the theory is not confirmed, reestablish a new theory or escalate

− dig
− mtr
− arp
− netstat
− curl
− ping
− nslookup
− traceroute
− ip
− ipconfig
◦ flushdns

− ifconfig
− route
− ss
− dhclient
− top
− snmpwalk
− nfdump

Given a scenario, analyze output from network tools and commands to resolve issues.
• Tools
− Wireshark
− Netcat
− Nmap
− Iperf
− radclient
− OpenSSL
− Postman
− Spectrum analyzer
− Heat map
− SIEM

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

• Commands
− tcpdump
− dig
− mtr
− arp
− netstat
− curl
− ping
− nslookup
− traceroute
− ip
− ipconfig

− ifconfig
− route
− ss
− dhclient
− top
− snmpwalk
− nfdump
• Performance issues
• Connectivity issues
• Access and security issues

4.0 | Network Troubleshooting

4.4

Given a scenario, troubleshoot connectivity issues.
• Intermittent connectivity
• DNS issues
• Asymmetric routing
• Port exhaustion
• Port misconfiguration
− VLAN assignment
• Duplicated IP addresses
• Duplicated MAC addresses
• IP address exhaustion
• NAT table exhaustion

4.5

4.6

Given a scenario, troubleshoot network performance issues.
• Latency issues
• Packet loss
• Maximum transmission unit
(MTU) issues
− Misconfigured jumbo frames
− Fragmentation

• Broadcast storm
• Resource exhaustion
• Bandwidth issues
− Overutilization
− Bottleneck
− Throttling

• Hairpinning

• Network scanning issues

Given a scenario, troubleshoot Wi-Fi performance issues.
• Signal interference
• Signal loss
• Signal degradation
• Low signal strength
• Band steering issues
• Channel overlap

4.7

• DHCP issues
• Request timeouts
• IPv6 router advertisements
• Physical layer disruptions
• Stale cache
• Internet Protocol Security
(IPSec) issues
• BGP issues
• Routing loops
• Single point of failure

• Incorrect channel width
• Client disassociation
• Roaming issues
− Sticky clients
• Transmitter/receiver incompatibility

Given a scenario, troubleshoot access and security issues.
• Rule and policy issues
− Incorrect security group
− Missing rules
− Misconfigured rules
− Overly permissive rules
− URL/web content filtering
− Geo-restriction
− ACL issues
• Denial of service (DoS) issues
− DDoS
− SYN floods
• Authentication and
authorization failures
− Password issues

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

− Incorrect group membership
− Mismatched secrets
• Certificate issues
− Mismatch
− Expired certificates
− Revoked certificates
− Trust issues
− Hash incompatibility
− TLS issues
• Blocked or dropped traffic

CompTIA CloudNetX CNX-001 Acronym List
The following is a list of acronyms that appears on the CompTIA CloudNetX
CNX-001 V1 exam. Candidates are encouraged to review the complete list and
attain a working knowledge of all listed acronyms as part of a comprehensive
exam preparation program.
ACRONYM		
AAA		
ABAC		
ACL		
ACME		
AES		
AI		
AP		
API		
ATT&CK		
BGP		
BIA		
BLE		
BPDU		
BPF		
BTU		
BYOD		
CASB		
CCM		
CCTV		
CDN		
CI/CD		
CIDR 		
CIEM		
CIS		
CLI		
CMDB		
CPE		
CPU		
CSP		
DAC		
DDoS		
DHCP		
DLP		
DNS		
DNSSEC		
DoH		
DoS		
DoT		
EDR		
EOL		
EOS		
EPO		

DEFINITION
Authentication, Authorization, and Accounting
Attribute-based Access Control
Access Control List
Automated Certificate Management Environment Protocol
Advanced Encryption Standard
Artificial Intelligence
Access Point
Application Programming Interface
Adversarial Tactics, Techniques, and Common Knowledge
Border Gateway Protocol
Business Impact Analysis
Bluetooth Low Energy
Bridge Protocol Data Units
Berkeley Packet Filter
British Thermal Unit
Bring Your Own Device
Cloud Access Security Broker
Cloud Controls Matrix
Closed-circuit TV
Content Delivery Network
Continuous Integration and Continuous Deployment
Classless Inter-domain Routing
Cloud Infrastructure Entitlement Management
Center for Internet Security
Command-line Interface
Configuration Management Database
Customer Premises Equipment
Central Processing Unit
Cloud Service Provider
Discretionary Access Control
Distributed Denial of Service
Dynamic Host Configuration Protocol
Data Loss Prevention
Domain Name System
Domain Name System Security Extensions
DNS over HTTPS
Denial of Service
DNS over TLS
Endpoint Detection and Response
End-of-life
End-of-support
Emergency Power Off

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

ACRONYM
FCoE		
FTP		
GDPR		
GENEVE		
HCL		
HSM		
HTTP		
HTTPS		
IaaS		
IaC		
IAM		
IDF		
IDS		
IoT		
IP		
IPAM		
IPS		
IPSec		
ISA		
ISO		
ISP 		
JIT		
JSON		
KMS		
KPI		
LAN		
LDAP		
LoRaWAN		
MAC 		
MDF		
MDM		
MFA		
MIB		
MOU		
MPLS		
MSA		
MSP		
MTBF		
MTTD		
MTTI		
MTTR		
MTU 		
MX		
NAC		
NACL		
NAS		
NAT		
NDA		
NFC		
NFS		
NFV		
NGFW		
NIC		
NOC		

DEFINITION
Fibre Channel Over Ethernet
File Transfer Protocol
General Data Protection Regulation
Generic Network Virtualization Encapsulation
HashiCorp Configuration Language
Hardware Security Module
Hypertext Transfer Protocol
Hypertext Transfer Protocol Secure
Infrastructure as a Service
Infrastructure as Code
Identity and Access Management
Intermediate Distribution Frame
Intrusion Detection System
Internet of Things
Internet Protocol
IP Address Management
Intrusion Prevention System
Internet Protocol Security
Interconnection Security Agreement
Industry Standards Organization
Internet Service Provider
Just-in-time
JavaScript Object Notation
Key Management System
Key Performance Indicator
Local Area Network
Lightweight Directory Access Protocol
Long-range Wide Area Network
Media Access Control
Main Distribution Frame
Mobile Device Management
Multifactor Authentication
Management Information Base
Memorandum of Understanding
Multiprotocol Label Switching
Master Service Agreement
Managed Service Provider
Mean Time Between Failures
Mean Time To Detect
Mean Time To Investigate
Mean Time To Recovery
Maximum Transmission Unit
Mail Exchange
Network Access Control
Network Access Control List
Network-attached Storage
Network Address Translation
Non-disclosure Agreement
Near-field Communication
Network File System
Network Function Virtualization
Next-generation Firewall
Network Interface Card
Network Operations Center

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

ACRONYM
NSG		
NTP		
OIDC		
OLA		
OOB		
OS		
OSI		
OSPF		
OTP		
OWASP		
PaaS		
PAM		
PAT		
PCAP		
PDU		
PII		
PKI		
PoE		
PSK		
QoS		
QR		
RADIUS		
RAID		
RDP		
REST		
RPO		
RTMP		
RTO		
RTSP		
S/MIME		
SaaS		
SAE		
SAML		
SASE		
SCIM		
SDCI		
SDK		
SD-WAN		
SFP		
SIEM		
SIP		
SLA		
SLI		
SLO		
SNMP		
SOAR		
SOW		
SQL		
SSE		
SSH		
SSID		
SSL		
SSO		
STP		

DEFINITION
Network Security Group
Network Time Protocol
OpenID Connect
Operational-level Agreement
Out-of-band
Operating System
Open Systems Interconnection
Open Shortest Path First
One-time Password
Open Worldwide Application Security Project
Platform as a Service
Privileged Access Management
Port Address Translation
Packet Capture
Power Distribution Unit
Personally Identifiable Information
Public Key Infrastructure
Power over Ethernet
Pre-shared Key
Quality of Service
Quick Response
Remote Authentication Dial-in User Services
Redundant Array of Independent Disks
Remote Desktop Protocol
Representational State Transfer
Recovery Point Objective
Real-time Messaging Protocol
Real Time Objective
Real-time Streaming Protocol
Secure/multipurpose Internet Mail Extensions
Software as a Service
Simultaneous Authentication of Equals
Security Assertion Markup Language
Secure Access Service Edge
System for Cross-interdomain Identity Management
Software-defined Cloud Interconnect
Software Development Kit
Software-defined Wide Area Network
Small Form-factor Pluggable
Security Information and Event Management
Session Initiation Protocol
Service-level Agreement
Service-level Indicator
Service-level Objective
Simple Network Management Protocol
Security Orchestration, Automation, and Response
Statement of Work
Structured Query Language
Secure Service Edge
Secure Shell
Service Set Identifier
Secure Sockets Layer
Single Sign-on
Spanning Tree Protocol

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

ACRONYM
TACACS+		
TCP		
TKIP		
TLS		
TTL		
UDP		
UEBA		
UPS		
URL		
VDI		
VIP		
VLAN		
VLSM		
VM		
VoIP		
VPC		
VPN		
VXLAN		
WAF		
WAN		
WAP		
WBS		
WLAN		
WPA2		
WPA3		
XML		
XXS		
YAML		
ZTA		
ZTNA		

DEFINITION
Terminal Access Controller Access Control System Plus
Transmission Control Protocol
Temporal Key Integrity Protocol
Transport Layer Security
Time to Live
User Datagram Protocol
User and Entity Behavior Analytics
Uninterruptible Power Supply
Uniform Resource Locator
Virtual Desktop Infrastructure
Virtual IP
Virtual Local Area Network
Variable Length Subnet Mask
Virtual Machine
Voice Over Internet Protocol
Virtual Private Cloud
Virtual Private Network
Virtual Extensible LAN
Web Application Firewall
Wide Area Network
Wireless Access Point
Work Breakdown Structure
Wireless Local Area Network
Wi-Fi Protected Access 2
Wi-Fi Protected Access 3
Extensible Markup Language
Cross-site Scripting
Yet Another Markup Language
Zero Trust Architecture
Zero Trust Network Access

CompTIA CloudNetX CNX-001 V1 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2023 CompTIA, Inc. All rights reserved.

CloudNetX Proposed Hardware and Software List
CompTIA has included this sample list of hardware and software to
assist candidates as they prepare for the CloudNetX CNX-001 V1 exam.
This list may also be helpful for training companies who wish to create
a lab component to their training offering. The bulleted lists below each
topic are a sample list and not exhaustive.
HARDWARE
• NGFWs
• Routers
• Switches
• Wireless access points
• Wireless controllers
• Cables
• Spectrum analyzer
• Cable tester

OTHER
• Whiteboard
• Access to a cloud provider
• OWASP Top Ten
• MITRE ATT&CK Framework
• Cloud Security Alliance Cloud
Controls Matrix (CCM)
• CIS benchmarks

SOFTWARE
• Device enumeration software
• Protocol analyzer
• Cisco packet tracer
• Load balancer
• CLI
• Wireshark
• Nmap
• Sample packet capture (pcap) files
• Diagramming software
• Access to Linux and Windows
operating systems
• Postman
• Terraform
• IPS/IDS
• Git client
• Python/Bash/PowerShell
• Log samples
• Integrated development environment

© 2023 CompTIA, Inc., used under license by CompTIA, Inc. All rights reserved. All certification programs and education related to such
programs are operated exclusively by CompTIA, Inc. CompTIA is a registered trademark of CompTIA, Inc. in the U.S. and internationally.
Other brands and company names mentioned herein may be trademarks or service marks of CompTIA, Inc. or of their respective owners.
Reproduction or dissemination prohibited without the written consent of CompTIA, Inc. Printed in the U.S. 11563-Nov2024

