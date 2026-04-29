AF

T

CompTIA CySA+
Certification Exam
Objectives

D

R

EXAM NUMBER: CS0-004 V4

CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

About the Exam

The CompTIA CySA+ CS0-004 V4 certification exam will certify the successful candidate has the knowledge
and skills required to:
•
•
•
•

Understand and perform incident response and vulnerability management processes.
Detect and analyze indicators of malicious activity in support of security operations.
Use appropriate tools, methods, and frameworks to prioritize and manage vulnerabilities and respond
to incidents.
Understand reporting and communication concepts related to vulnerability management and incident
response activities.

This is the equivalent of approximately 4 years of IT experience in a SOC analyst (level 2) or a vulnerability
analyst role. These content examples are meant to clarify the test objectives and should not be construed as
a comprehensive listing of all the content of this examination.

AF

T

EXAM ACCREDITATION
The CompTIA CySA+ exam is accredited by the ANSI National Accreditation Board (ANAB) to show
compliance with the International Organization for Standardization (ISO) 17024 standard and, as such,
undergoes regular reviews and updates to the exam objectives.
EXAM DEVELOPMENT
CompTIA exams result from subject matter expert workshops and industry-wide survey results regarding the
skills and knowledge required of an IT professional.

D

R

CompTIA AUTHORIZED MATERIALS USE POLICY
CompTIA Certifications, LLC is not affiliated with and does not authorize, endorse, or condone utilizing any
content provided by unauthorized third-party training sites (aka “brain dumps”). Individuals who utilize such
materials in preparation for any CompTIA examination will have their certifications revoked and be suspended
from future testing in accordance with the CompTIA Candidate Agreement. In an effort to more clearly
communicate CompTIA’s exam policies on use of unauthorized study materials, CompTIA directs all
certification candidates to the CompTIA Certification Exam Policies. Please review all CompTIA policies before
beginning the study process for any CompTIA exam. Candidates will be required to abide by the CompTIA
Candidate Agreement. If a candidate has a question as to whether study materials are considered
unauthorized (aka “brain dumps”), they should contact CompTIA at examsecurity@comptia.org to confirm.
PLEASE NOTE
The lists of examples provided in bulleted format are not exhaustive lists. Other examples of technologies,
processes, or tasks pertaining to each objective may also be included on the exam, although not listed or
covered in this objectives document. CompTIA is constantly reviewing the content of our exams and updating
test questions to be sure our exams are current and the security of the questions is protected. When
necessary, we will publish updated exams based on existing exam objectives. Please know that all related
exam preparation materials will still be valid.

CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

TEST DETAILS
Required exam
Number of questions
Types of questions
Length of test
Recommended experience

CySA+ CS0-004 V4
Multiple-choice and performance-based
4 years of hands-on experience in a SOC analyst
(level 2) or vulnerability analyst role

EXAM OBJECTIVES (DOMAINS)
The table below lists the domains measured by this examination and the extent to which they are
represented.
DOMAIN

PERCENTAGE OF EXAMINATION

1.0

Security Operations

34%

2.0

Vulnerability Management

26%

3.0

Incident Response and Management

24%

4.0

Reporting and Communication

16%

D

R

AF

T

Total

CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

100%

1.0

Security Operations

1.1 Explain concepts related to system and network architecture in security
operations.













Network architecture concepts
•
Zero Trust Network Architecture
(ZTNA)
•
Secure access service edge
(SASE)
•
Hybrid cloud
Identity and access management
(IAM)
•
Privileged access management
(PAM)
•
Authentication and authorization
methods
•
Secrets management
Encryption techniques
Data protection concepts
Critical infrastructure concepts
•
Operational technology (OT)
•
Industrial control system (ICS)
•
Supervisory control and data
acquisition (SCADA)

T



Logging concepts
•
Ingestion
•
Configuration
•
Integrity and security
•
Time synchronization
•
Retention
Operating system concepts
•
System hardening
•
File structure
♦ Critical files
•
System processes
Infrastructure/system architecture
concepts
•
Cloud native
•
Virtualization
•
Containerization
•
Application programming
interfaces (APIs)
Device management concepts
•
Mobile
•
Endpoint

AF



1.2 Given a scenario, analyze indicators of potential malicious activity.

D



Network-related indicators
•
Rogue devices
•
Enumeration
•
Anomalous activity
•
Activity on unexpected ports
Host-related indicators
•
Resource consumption
•
Unauthorized software
•
Anomalous activity
♦ Suspicious or rogue
processes
♦ Living Off the Land Binaries
(LOLBins) and Scripts
♦ File system changes
♦ Data exfiltration
Unauthorized configuration

R





CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.











Application-related indicators
•
Service disruption
•
Anomalous activity
Cloud-related indicators
•
Anomalous activity
•
Resource compromise
Social engineering attacks
•
Typosquatting
•
URL shorteners
Identity-based indicators
•
IAM account compromise
•
Unauthorized access
•
Impossible travel
Email-related attacks
•
Business email compromise
(BEC)

1.3 Given a scenario, use tools to determine malicious activity.
Tools
•
Decoding/parsing
♦ CyberChef
•
Packet analysis
♦ Wireshark
♦ tcpdump
♦ Snort
♦ Suricata
♦ Zeek
•
Log analysis
♦ Security information and event management (SIEM)
•
Threat-intelligence platforms
♦ Open Threat Exchange (OTX)
♦ Malware Information Sharing Platform (MISP)
♦ Open Cyber Threat Intelligence (OpenCTI)
•
Endpoint security
♦
Endpoint detection and response (EDR) and extended detection and response (XDR)
♦ Mobile device management (MDM)
•
Domain and IP reputation
♦ WHOIS
♦ AbuseIPDB
♦ Geolocation by IP Address (GEO-IP)
•
File analysis
♦ Strings
♦ VirusTotal
♦ Yet another recursive acronym (YARA)
•
Sandboxing
♦ Joe Sandbox
♦ Cuckoo Sandbox
•
Pattern recognition
♦ Regular expressions
♦ Interpreting suspicious commands
•
Email analysis
♦ MXToolbox
•
User and entity behavior analysis (UEBA)
♦ Open User and Entity Behavior Analytics (OpenUBA)
File formats
•
JSON
•
XML
•
YAML
•
EVTX
Programming/scripting languages
•
Python
•
PowerShell
•
Shell script

D



R

AF

T





CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

1.4 Explain threat intelligence and threat-hunting concepts.












T



Threat actors
•
Advanced persistent threat (APT)
•
Insider threat
Tactics, techniques, and procedures (TTPs)
•
Heat maps
•
Pyramid of pain
•
MITRE ATT&CK
•
Attribution
Confidence-level impacts
•
Timeliness
•
Relevance
•
Accuracy
Collection methods and sources
•
Open-source intelligence (OSINT)
•
Closed-source intelligence
•
Threat intelligence sharing
Indicator of compromise (IoC)
•
Collection
•
Analysis
•
Application/usage
•
Types
♦ Atomic
♦ Behavioral
Threat modeling
•
Spoofing, tampering, repudiation, information disclosure, denial of service, elevation of
privilege (STRIDE)
Threat mapping
Cyber deception

AF





Standardize processes
•
Manage and facilitate team coordination
•
Playbook/runbook creation
Streamline operations
•
Automation and orchestration
♦ Security orchestration, automation, and Response (SOAR)
♦ Infrastructure as code (IaC)
•
Data enrichment
♦ Rule/alert tuning
♦ Dashboard creation
Technology and tool integration
•
APIs
•
Webhooks
•
Plug-ins

D



R

1.5 Explain the importance of efficiency and process improvement in security
operations.



CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

1.6 Summarize concepts related to the use of AI in security operations.




D

R

AF

T



AI risks
•
Hallucinations
•
Data exposure
•
Model poisoning
•
Malicious prompts
Governance
•
Legal or regulatory compliance
•
AI usage policies
Use cases
•
Comparing artifacts
•
Analyzing log files
•
Document creation
•
Incident investigation
•
Event correlation
•
Automation and orchestration

CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

2.0 Vulnerability Management
2.1 Given a scenario, implement the appropriate vulnerability scanning method.



T



Asset inventory
Planning considerations
•
Scheduling
•
Operations
•
Performance
•
Sensitivity levels
•
Segmentation
•
Regulatory requirements
Scan types
•
Internal vs. external
•
Agent vs. agentless
•
Credentialed vs. non-credentialed
•
Passive vs. active
•
Discovery
♦ Mapping scans
♦ Device fingerprinting
•
Security baseline scanning
♦ Payment Card Industry Data Security Standard (PCI DSS)
♦ Center for Internet Security (CIS) benchmarks
♦ International Organization for Standardization (ISO) 27000 series





D



Network scanning and mapping
•
Angry IP Scanner
•
Masscan
Multipurpose tools
•
Nmap
•
Metasploit Framework (MSF)
•
Maltego
•
Recon-ng
Web application scanners
•
Burp Suite
•
Zed Attack Proxy (ZAP)
•
Nikto
Vulnerability scanners
•
Nessus
•
Nuclei
•
Open Vulnerability Assessment Scanner (OpenVAS)
Cloud infrastructure assessment tools
•
ScoutSuite
•
Prowler
•
Trivy
•
Checkov
Breach attack simulation (BAS) tools
•
Atomic Red Team
•
Caldera

R



AF

2.2 Given a scenario, analyze output from vulnerability assessment tools.





CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

2.3 Given a scenario, analyze data to prioritize and mitigate vulnerabilities.








T



Criteria
•
Exploitability
•
Active exploitation/threat intelligence
•
Asset value
•
Impact
•
Patch/remediation availability
•
True/false positives
•
True/false negatives
Scoring methods
•
Common Vulnerability Scoring System (CVSS) metrics
•
First Exploitability Prediction Scoring System (EPSS)
Context awareness
•
Internal
•
External
•
Isolated
Mitigation strategies
•
Attack surface management
•
Secure coding best practices
•
Patching and configuration management
•
Exceptions
•
Compensating controls
Validation of remediation



D



Control types
•
Administrative
•
Technical
•
Physical
Control functions
•
Preventative
•
Detective
•
Responsive
•
Corrective
Risk concepts
•
Risk appetite
•
Residual risk
•
Inherent risk
Risk management strategies
•
Accept
•
Transfer
•
Avoid
•
Mitigate
Policies, governance, and service-level objectives (SLOs)
Application security
•
Static application security testing (SAST)
•
Dynamic application security testing (DAST)
•
Software Assurance Maturity Model (SAMM)
Third-party risk
•
Supply chain
•
Software composition analysis (SCA)
•
Software bill of materials (SBOM)

R



AF

2.4 Explain concepts related to control types, risks, and vulnerability
management.








CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

3.0 Incident Response and Management
3.1 Summarize concepts related to attack methodology frameworks.




Cyber Kill Chain
Diamond Model of Intrusion Analysis
MITRE ATT&CK

3.2 Summarize the incident response process.








Preparation
Detection
Analysis
Containment
Eradication
Recovery
Post-incident



D





AF



Analysis
•
Triage
•
Establishment of a timeline
Evidence acquisition
•
Chain of custody
•
Data integrity validation
•
Preservation
•
Legal hold
Containment
•
Scope
•
Impact
•
Isolation
Escalation
Eradication techniques
Continuous monitoring

R



T

3.3 Given a scenario, implement incident response techniques.

CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

4.0 Reporting and Communication
4.1 Explain the importance of vulnerability management reporting and
communication.




T



Vulnerability scan reports
Compliance findings
Risk scorecards
Action plans
•
Escalation
•
Dependencies
Inhibitors to remediation
•
Contractual agreements
•
Organizational governance
•
Business process interruption
•
Degrading functionality
•
Legacy systems
•
Proprietary systems
•
Patch availability
Stakeholder identification and communication
Metrics and key performance indicators (KPIs)
•
Trends
•
Top risks
•
Service-level agreement (SLA)

AF






4.2 Explain the importance of security operations and incident response reporting
and communication.
Incident declaration and escalation
Executive summary
Communication plan
•
Stakeholder identification
•
Legal team
•
Public relations
•
Regulatory reporting agencies
•
Law enforcement
•
Customers
Operational security awareness
•
Communication channels
Post-incident reporting
•
After-action report
•
Lessons learned
•
Root cause analysis

D

R








CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.






Shift/incident handover
Internal threat intelligence report
•
Tailored to
organization/environment
Metrics and KPIs
•
Alert volume
•
False-positive rate
•
True-positive rate
•
Mean time to close
•
Mean time to detect
•
Mean time to respond
•
Mean time to remediate
•
Phishing campaign click rate

CompTIA CySA+ Acronym List
The following is a list of acronyms that appear on the CompTIA CySA+ CS0-004 V4
certification exam. Candidates are encouraged to review the complete list and attain a
working knowledge of all listed acronyms as part of a comprehensive exam preparation
program.

T

AF

D

DNS
DR
EDR
EPSS
GCP
GDB
GeoIP
IaC
IAM
ICS
IDS
IoC
IP
IPS
ISO
JSON

DEFINITION
Artificial Intelligence
Application Programming Interface
Advanced Persistent Threat
Anonymous System Number
Amazon Web Services
Breach Attack Simulation
Business Continuity
Business Email Compromise
Cloud Access Security Broker
Computer Emergency Response Team
Cardholder Data
Center for Internet Security
Cybersecurity Incident Response Team
Common Vulnerability Scoring System
Dynamic Application Security Testing
Domain Keys Identified Mail
Data Loss Prevention
Domain-based Message Authentication, Reporting, and
Conformance
Domain Name Service
Disaster Recovery
Endpoint Detection and Response
Exploitability Predication Scoring System
Google Cloud Platform
GNU Debugger
Geolocation by IP
Infrastructure as Code
Identity and Access Management
Industrial Control Systems
Intrusion Detection System
Indicator of Compromise
Internet Protocol
Intrusion Prevention System
International Organization for Standardization
JavaScript Object Notation

R

ACRONYM
AI
API
APT
ASN
AWS
BAS
BC
BEC
CASB
CERT
CHD
CIS
CSIRT
CVSS
DAST
DKIM
DLP
DMARC

CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

AF

T

DEFINITION
Key Performance Indicator
Local File Inclusion
Mobile Device Management
Multifactor Authentication
Malware Information Sharing Platform
Memorandum of Understanding
Metasploit Framework
Open Cyber Threat Intelligence
Open User Behavior Analytics
Open Vulnerability Assessment Scanner
Open-Source Intelligence
Open Source Security Testing Methodology Manual
Operational Technology
Open Threat Exchange
Open Web Application Security Project
Privileged Access Management
Payment Card Industry Data Security Standard
Personally Identifiable Information
Public Key Infrastructure
Remote File Inclusion
Software Assurance Maturity Model
Secure Access Service Edge
Static Application Security Testing
Software Bill of Materials
Software Composition Analysis
Supervisory Control and Data Acquisition
Software Development Life Cycle
Software-Defined Networking
Security Information and Event Management
Service-level Agreement
Service-level Objective
Security Orchestration, Automation, and Response
Sender Policy Framework
Secure Sockets Layer
Single Sign-on
Spoofing, Tampering, Repudiation, Information disclosure,
Denial of service, and Elevation of privilege
Transmission Control Protocol
Tactics, Techniques, and Procedures
User and Entity Behavior Analysis
Unified Threat Management
Virtual Machine
Extended Detection and Response

D

R

ACRONYM
KPI
LFI
MDM
MFA
MISP
MOU
MSF
OpenCTI
OpenUBA
OpenVAS
OSINT
OSSTMM
OT
OTX
OWASP
PAM
PCI DSS
PII
PKI
RFI
SAMM
SASE
SAST
SBOM
SCA
SCADA
SDLC
SDN
SIEM
SLA
SLO
SOAR
SPF
SSL
SSO
STRIDE
TCP
TTPs
UEBA
UTM
VM
XDR

CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

DEFINITION
Extensible Markup Language
Yet Another Markup Language
Yet Another Recursive Acronym
Zed Attack Proxy
Zero Trust Network Access

D

R

AF

T

ACRONYM
XML
YAML
YARA
ZAP
ZTNA

CompTIA CySA+ CS0-001 V4 Certification Exam
Exam Objectives Document Version 1.1
Copyright © 2025 CompTIA, Inc. All rights reserved.

CompTIA CySA+
Hardware and Software List
CompTIA has included this sample list of hardware and software to assist candidates as
they prepare for the CySA+ CS0-004 V4 certification exam. This list may also be helpful
for training companies that wish to create a lab component for their training offering. The
Bulleted lists below each topic are sample lists and are not exhaustive.
EQUIPMENT
• Workstations (or laptops) with ability to run a virtual machine (VM)
• Firewall
• Intrusion detection system/intrusion prevention system (IDS/IPS)
• Servers

D

R

AF

T

SOFTWARE
• Windows operating systems
o Commando VM
• Linux operating systems
o Kali
• Open-source unified thread management (UTM) appliance
• Metasploitable
• SIEM
o Greylog
o Elasticsearch, Logstash, and Kibana (ELK)
o Splunk
• tcpdump
• Wireshark
• Vulnerability scanner
o OpenVAS
o Nessus
• Access to cloud instances
o Azure
o Amazon Web Services (AWS)
o Google Cloud Platform (GCP)

© 2025 CompTIA, Inc., used under license by CompTIA, Inc. All rights reserved. All certification programs and education related to such
programs are operated exclusively by CompTIA, Inc. CompTIA is a registered trademark of CompTIA, Inc. in the U.S. and internationally.
Other brands and company names mentioned herein may be trademarks or service marks of CompTIA, Inc. or of their respective owners.
Reproduction or dissemination prohibited without the written consent of CompTIA, Inc.

