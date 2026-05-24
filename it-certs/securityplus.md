# CompTIA Security+ SYO-701 V7 Objectives

## 1.0 General Security Concepts 12%

### 1.1 Compare and contrast various types of security controls

- **Categories**
  - **{{Technical Control}}**: Implemented via _software, hardware, or firmware_
    systems.
  - **{{Managerial Control}}**: Strategic risk governance through _policies and
    procedures_.
  - **{{Operational Control}}**: Processes executed by _people during daily
    operations_.
  - **{{Physical Control}}**: _Tangible measures_ protecting assets and safety.
- **Control types**
  - **{{Preventive}}**: Stops a security incident _before it occurs_.
  - **{{Deterrent}}**: Discourages intrusion by _warning of negative
    consequences_.
  - **{{Detective}}**: _Identifies and records_ events during or after
    occurrence.
  - **{{Corrective}}**: _Mitigates damage_ and restores systems after incidents.
  - **{{Compensating}}**: _Alternative substitute_ when primary control is not
    feasible.
  - **{{Directive}}**: Mandates _compliance_ through administrative rules and
    regulations.

### 1.2 Summarize fundamental security concepts

- **{{CIA Triad}}**: Core model for _information security policy_.
  - **{{Confidentiality}}**: Preventing _unauthorized access or disclosure_ of
    data.
  - **{{Integrity}}**: Ensuring data remains _accurate and unaltered_.
  - **{{Availability}}**: Ensuring data and systems are _accessible when
    needed_.
- **{{Non-repudiation}}**: Proving a subject _performed an action undeniably_.
- **{{AAA Framework}}**: Model for _controlling access to computer resources_.
  - **{{Authentication}}**: Verifying a _user or system's claimed identity_.
  - **{{Authorization}}**: Determining _access rights and permissions_ after
    authentication.
  - **{{Accounting}}**: _Tracking and recording_ user activity for auditing.
- **{{Gap Analysis}}**: Comparing _current security_ against the _desired
  state_.
- **{{Zero Trust}}**: "Never trust, always verify" _security model_.
  - **{{Least Privilege}}**: Granting only the _minimum necessary access_.
  - **{{Assume Breach}}**: Operating as if _attackers are already present_.
  - **{{Control Plane}}**: Orchestrates _access decisions and policy
    management_.
    - **{{Adaptive Identity}}**: Authentication requirements _adjust based on
      risk context_.
    - **{{Policy Engine}}**: Component _making the decision_ to grant access.
    - **{{Policy Administrator}}**: Component _establishing the connection_
      based on decisions.
  - **{{Data Plane}}**: Where _actual application data flow_ occurs.
    - **{{Policy Enforcement Point (PEP)}}**: _Intercepts traffic_ to enforce
      access decisions.
    - **{{Implicit Trust Zone}}**: Area where _trust is assumed_ (Eliminated in
      ZT).
- **{{Physical Security}}**: Protecting assets from _tangible, real-world
  threats_.
  - **{{Bollard}}**: Sturdy post _preventing vehicle ramming attacks_.
  - **{{Access Control Vestibule}}**: Double-door system _restricting entry_ to
    prevent tailgating.
  - **{{Fencing}}**: Perimeter barrier _defining boundaries and deterring
    entry_.
  - **{{Video Surveillance (CCTV)}}**: Monitoring and _recording visual
    activity_.
  - **{{Sensors}}**: Devices detecting _physical environmental changes_.
    - **{{Infrared}}**: Detects motion via _heat signature changes_.
    - **{{Pressure}}**: Detects _weight application_ on a surface.
    - **{{Microwave}}**: Detects movement via _radio wave reflection_.
    - **{{Ultrasonic}}**: Detects motion via _high-frequency sound waves_.
- **{{Deception and Disruption}}**: Techniques to _confuse, trap, or slow_
  attackers.
  - **{{Honeypot}}**: Single decoy system _luring attackers away_.
  - **{{Honeynet}}**: _Network of decoys_ simulating a real environment.
  - **{{Honeyfile}}**: Decoy file _triggering alerts when accessed_.
  - **{{Honeytoken}}**: Fake data element _tracking attacker activity_.

### 1.3 Explain the importance of change management processes and the impact to security

- **{{Change Management}}**: Process to _control lifecycle of system changes_.
  - **{{Separation of Duties}}**: Dividing tasks to _prevent error or fraud_.
  - **{{Rollback}}**: Ability to _revert to previous state_ upon failure.
- **Business processes impacting security operation**
  - **{{Approval Process}}**: Formal authorization _required before
    implementing_ changes.
  - **{{Ownership}}**: Individual or entity _accountable for a specific asset_.
  - **{{Stakeholder}}**: Individual _interested in or affected_ by the change.
  - **{{Impact Analysis}}**: Assessing _potential consequences_ before
    implementing a change.
  - **{{Backout Plan}}**: Procedure to _revert changes_ if implementation fails.
  - **{{Maintenance Window}}**: Scheduled timeframe _authorized for performing
    system changes_.
  - **{{Standard Operating Procedure (SOP)}}**: Step-by-step instructions for
    _routine tasks_.
- **Technical implications**
  - **{{Allow List / Deny List}}**: Explicitly _permitting or blocking_ specific
    traffic.
  - **{{Restricted Activities}}**: High-risk actions _prohibited during specific
    times_.
  - **{{Downtime}}**: Period when a _system or service is unavailable_.
  - **{{Legacy Application}}**: _Outdated software_ still used for business
    needs.
  - **{{Dependency}}**: Component _requiring other components_ to function
    correctly.
- **Documentation**
  - **{{Network Diagram}}**: Visual representation of _network topology and
    connections_.
  - **{{Version Control}}**: System _tracking and managing_ changes to files.

### 1.4 Explain the importance of using appropriate cryptographic solutions

- **{{Public Key Infrastructure (PKI)}}**: Framework managing _digital keys and
  certificates_.
  - **{{Trust Chain}}**: Path of trust from _root CA to end-entity_.
  - **{{Public Key}}**: Sharable key used for _encryption or verification_.
  - **{{Private Key}}**: Secret key used for _decryption or signing_.
  - **{{Key Escrow}}**: Storing keys with a _third party for recovery_.
- **Encryption**
  - **{{Full-disk Encryption (FDE)}}**: Encrypts the _entire physical drive_ and
    OS.
  - **{{Data-in-Transit}}**: Encrypting data _moving across a network_.
  - **{{Asymmetric Encryption}}**: Uses _key pairs_: one public, one private.
  - **{{Symmetric Encryption}}**: Uses the _same key_ for encryption and
    decryption.
  - **{{Key Exchange}}**: Secure method for _parties to swap keys_.
    - **{{Diffie-Hellman (DH)}}**: Protocol to _exchange keys over insecure
      channels_.
    - **{{Perfect Forward Secrecy (PFS)}}**: Past sessions remain secure _even
      if key is compromised_.
  - **{{Algorithm}}**: Mathematical formula _performing the encryption process_.
  - **{{Key Length}}**: Number of bits _determining the key's strength_.
    - **{{Entropy}}**: Measure of _randomness_ in cryptographic material.
- **Tools**
  - **{{Trusted Platform Module (TPM)}}**: Motherboard chip _storing keys and
    ensuring integrity_.
  - **{{Hardware Security Module (HSM)}}**: Dedicated physical appliance for
    _secure key management_.
  - **{{Secure Enclave}}**: CPU-isolated area _protecting sensitive memory and
    code_.
- **{{Obfuscation}}**: Making code or data _difficult to understand_.
  - **{{Steganography}}**: _Hiding secret data_ within innocent-looking files.
  - **{{Tokenization}}**: Replacing sensitive data with _non-sensitive unique
    symbols_.
  - **{{Data Masking}}**: _Hiding specific characters_ of data for display.
- **{{Hashing}}**: One-way conversion of _data to fixed string_.
  - **{{Collision}}**: distinct inputs _producing the same hash_.
- **{{Salting}}**: Adding _random data_ to passwords before hashing.
- **{{Digital Signature}}**: Cryptographic proof of _message origin and
  integrity_.
- **{{Key Stretching}}**: _Slowing down processing_ to strengthen weak keys.
- **{{Blockchain}}**: Decentralized, _immutable chain_ of transaction blocks.
- **{{Certificate}}**: Digital document _binding a key to identity_.
  - **{{Certificate Authority (CA)}}**: Trusted entity that _issues and
    verifies_ certificates.
  - **{{Certificate Revocation List (CRL)}}**: List of _invalid certificates_
    published by CA.
  - **{{Online Certificate Status Protocol (OCSP)}}**: Real-time protocol
    _checking if certificate is valid_.
    - **{{OCSP Stapling}}**: Server caches OCSP response to _reduce CA load_.
  - **{{Root of Trust}}**: The _ultimate, foundational trust anchor_ in PKI.
  - **{{Certificate Signing Request (CSR)}}**: Request sent to CA to _apply for
    certificate_.

## 2.0 Threats, Vulnerabilities, and Mitigations 22%

### 2.1 Compare and contrast common threat actors and motivations

- **Threat actors**
  - **{{Nation-State}}**: Government-backed actors targeting _national security
    interests_.
  - **{{Unskilled Attacker (Script Kiddie)}}**: Low-skill individuals using
    _pre-made tools or scripts_.
  - **{{Hacktivist}}**: Attackers motivated by _social or political ideology_.
  - **{{Insider Threat}}**: Trusted users _exploiting authorized access_ to
    harm.
  - **{{Organized Crime}}**: Professional criminal groups focused on _financial
    gain_.
  - **{{Shadow IT}}**: Unapproved technology used _without IT department
    knowledge_.
- **Attributes of actors**
  - **{{Internal / External}}**: Originates from _inside or outside_ the
    organization.
  - **{{Resources / Funding}}**: _Financial and material backing_ available to
    attacker.
  - **{{Sophistication / Capability}}**: The _technical skill and complexity_ of
    the attacker.
- **Motivations**
  - **{{Data Exfiltration}}**: Unauthorized _transfer of data_ out of a network.
  - **{{Espionage}}**: Spying to obtain _secret government or trade
    information_.
  - **{{Service Disruption}}**: Intentionally _interrupting availability_ of
    systems or networks.
  - **{{Blackmail}}**: Coercing victims by _threatening to reveal_ compromising
    information.
  - **{{Financial Gain}}**: Attacking primarily to _generate monetary profit_.
  - **{{Philosophical / Political Beliefs}}**: Actions driven by _ideology or
    personal convictions_.
  - **{{Ethical}}**: Actions intended to _help or improve security_ ("White
    Hat").
  - **{{Revenge}}**: Retaliatory attacks seeking _payback for perceived wrongs_.
  - **{{Disruption / Chaos}}**: Causing _confusion or disorder_ for its own
    sake.
  - **{{War}}**: Cyber operations conducting _military strategy or sabotage_.

### 2.2 Explain common threat vectors and attack surfaces

- **{{Threat Vector}}**: The _path or means_ an attacker uses.
- **{{Attack Surface}}**: Total sum of _vulnerabilities accessible to an
  attacker_.
- **Message-based**
  - **{{Email}}**: Attack delivery via _electronic mail messages_.
  - **{{Short Message Service (SMS)}}**: Attack delivery via _mobile text
    messages_.
  - **{{Instant Messaging (IM)}}**: Attack delivery via _real-time chat
    applications_.
- **{{Image-based}}**: Malware embedded within _digital image files_.
  - **{{Steganography}}**: _Hiding malicious code_ within innocent-looking
    files.
- **{{File-based}}**: Malware delivered via _downloadable files or attachments_.
- **{{Voice Call}}**: Attacks conducted over _phone or VoIP systems_.
- **{{Removable Device}}**: Malware introduced via _USBs or external drives_.
  - **{{USB Drop}}**: Leaving infected drives to be _found and plugged in_.
- **Vulnerable software**
  - **{{Client-based}}**: Vulnerabilities within _specific installed software
    agents_.
  - **{{Agentless}}**: Vulnerabilities exploited _without installing local
    software_.
- **Unsupported systems and applications**
  - **{{Unsupported Systems}}**: Software _no longer receiving_ manufacturer
    security updates.
- **Unsecure networks**
  - **{{Wireless}}**: Attacks exploiting _Wi-Fi radio signals_.
    - **{{Evil Twin}}**: Fake access point _mimicking a legitimate network_.
  - **{{Wired}}**: Attacks requiring _physical connection_ to cables.
  - **{{Bluetooth}}**: Attacks exploiting _short-range wireless device pairing_.
    - **{{Bluejacking}}**: Sending _unsolicited messages_ to Bluetooth devices.
    - **{{Bluesnarfing}}**: Unauthorized _access of information_ from Bluetooth
      devices.
- **{{Open Service Ports}}**: Network endpoints _accepting traffic_ without
  restriction.
  - **{{Port Scanning}}**: Probing a server to _identify open ports_.
- **{{Default Credentials}}**: Standard usernames/passwords _left unchanged by
  administrators_.
- **Supply chain**
  - **{{Managed Service Provider (MSP)}}**: Third-party company _managing IT
    services_ for clients.
  - **{{Vendor}}**: Seller providing _finished hardware or software products_.
  - **{{Supplier}}**: Entity providing _raw materials or components_.
- **Human vectors / Social Engineering**
  - **{{Social Engineering}}**: Manipulating people into _performing actions or
    divulging info_.
  - **{{Phishing}}**: Deceptive emails _inducing users to reveal information_.
  - **{{Vishing}}**: Phishing attempts conducted via _voice phone calls_.
  - **{{Smishing}}**: Phishing attempts conducted via _SMS text messages_.
  - **{{Misinformation / Disinformation}}**: Spreading _false info_ to deceive
    or confuse.
  - **{{Impersonation}}**: Pretending to be _another person or entity_.
  - **{{Business Email Compromise (BEC)}}**: Compromising legitimate email
    accounts to _conduct fraud_.
  - **{{Pretexting}}**: Fabricating a _scenario to gain victim's trust_.
  - **{{Watering Hole}}**: Infecting _websites frequently visited_ by targets.
  - **{{Brand Impersonation}}**: Mimicking a _trusted company_ to trick users.
  - **{{Typosquatting}}**: Registering domains _visually similar_ to popular
    sites.

### 2.3 Explain various types of vulnerabilities

- **{{Vulnerability}}**: Weakness in an asset _exploitable by threat actors_.
- **Application**
  - **{{Memory Injection}}**: Inserting _malicious code_ into running
    application memory.
  - **{{Buffer Overflow}}**: Writing _more data_ than a memory block holds.
    - **{{Bounds Checking}}**: Verifying input _fits within allocated memory_.
  - **{{Race Condition}}**: Outcome depends on _uncontrollable event timing
    sequence_.
    - **{{Time-of-Check (TOC)}}**: The moment the system _validates a request_.
    - **{{Time-of-Use (TOU)}}**: The moment the system _acts on resources_.
  - **{{Malicious Update}}**: Legitimate-looking software patch _containing
    hidden malware_.
- **{{Operating System (OS)-based}}**: Flaws specific to the _underlying system
  software_.
  - **{{Kernel Panic}}**: Critical error causing _OS to stop functioning_.
- **Web-based**
  - **{{Structured Query Language Injection (SQLi)}}**: Injecting queries to
    _manipulate databases via input_.
  - **{{Cross-Site Scripting (XSS)}}**: Injecting _malicious scripts_ into
    trusted websites.
    - **{{Reflected XSS}}**: Malicious script comes from _current HTTP request_.
    - **{{Stored XSS}}**: Malicious script is _saved on the server_.
- **Hardware**
  - **{{Firmware}}**: Software _permanently programmed_ into hardware read-only
    memory.
  - **{{End-of-Life (EOL)}}**: Vendor stops _supporting or updating_ the
    product.
  - **{{Legacy}}**: Outdated technology still in use, _often insecure_.
- **Virtualization**
  - **{{Virtual Machine (VM) Escape}}**: Breaking out of VM to _access host
    system_.
  - **{{Resource Reuse}}**: Data _persisting after memory_ is supposedly freed.
- **Cloud-specific**
  - **{{Misconfiguration}}**: Incorrectly set _security settings_ (e.g., public
    S3 buckets).
- **Supply Chain**
  - **{{Service Provider}}**: External entity _delivering IT or business
    services_.
  - **{{Hardware Provider}}**: Manufacturer supplying _physical components or
    devices_.
    - **{{Hardware Tampering}}**: Physical modification of devices _during
      manufacturing or shipping_.
  - **{{Software Provider}}**: Developer supplying _applications or code
    libraries_.
- **{{Cryptographic}}**: Flaws in _encryption algorithms or implementation_.
  - **{{Weak Algorithm}}**: Using encryption with _known vulnerabilities_ (e.g.,
    DES, MD5).
- **{{Misconfiguration}}**: Incorrectly set _security settings leaving gaps_.
- **Mobile Device**
  - **{{Side Loading}}**: Installing apps from _unofficial sources_.
  - **{{Jailbreaking / Rooting}}**: Removing _manufacturer restrictions_ on
    mobile devices.
- **{{Zero-Day}}**: Vulnerability _unknown to the vendor_ or developer.

### 2.4 Given a scenario, analyze indicators of malicious activity

- **Malware Attacks**
  - **{{Ransomware}}**: Malware _demanding payment_ to restore data access.
  - **{{Trojan}}**: Malware _disguised as legitimate_, harmless software.
  - **{{Worm}}**: Self-replicating malware _spreading independently_ across
    networks.
  - **{{Spyware}}**: Malware _secretly recording_ user activity and data.
  - **{{Bloatware}}**: Unwanted software _consuming system resources_.
  - **{{Virus}}**: Malicious code _attaching to host files_ to replicate.
  - **{{Keylogger}}**: Software _recording keystrokes_ to steal credentials.
  - **{{Logic Bomb}}**: Malicious code _triggered by specific conditions_.
  - **{{Rootkit}}**: Malware providing _privileged access_ while hiding itself.
  - **{{Payload}}**: Component of malware _performing the malicious action_.
  - **{{Command and Control (C2)}}**: Infrastructure used to _remotely manage
    compromised systems_.
- **Physical Attacks**
  - **{{Brute Force (Physical)}}**: Forcing entry through _physical barriers or
    locks_.
  - **{{Radio Frequency Identification (RFID) Cloning}}**: Copying data from
    _radio frequency identification chips_.
  - **{{Environmental}}**: Manipulating _temperature, power, or humidity_ to
    damage.
- **Network Attacks**
  - **{{Distributed Denial-of-Service (DDoS)}}**: Overwhelming a target with
    _traffic from many sources_.
    - **{{Botnet}}**: Network of compromised computers _controlled as a unit_.
    - **{{Amplified DDoS}}**: Increasing traffic volume via _response-heavy
      protocols_.
    - **{{Reflected DDoS}}**: Spoofing victim IP to _solicit floods of
      responses_.
  - **{{Domain Name System (DNS) Poisoning}}**: Manipulating domain resolution
    to _redirect traffic_.
  - **{{Wireless Attack}}**: Exploiting vulnerabilities in _radio-based
    communications_.
  - **{{On-Path (Man-in-the-Middle)}}**: _Intercepting and altering_
    communications between two parties.
  - **{{Credential Replay}}**: Capturing and _reusing valid login data_.
  - **{{Malicious Code}}**: Scripts designed to _harm or disrupt systems_.
- **Application Attacks**
  - **{{Injection}}**: Inserting _malicious input_ to manipulate application
    execution.
  - **{{Buffer Overflow}}**: Overwriting memory bounds to _crash or control
    execution_.
  - **{{Replay Attack}}**: Resending captured data to _impersonate a legitimate
    user_.
  - **{{Privilege Escalation}}**: Gaining _higher access rights_ than originally
    authorized.
    - **{{Vertical Escalation}}**: User gains _administrative privileges_.
    - **{{Horizontal Escalation}}**: User accesses _another user's data_.
  - **{{Forgery}}**: Falsifying _data or signatures_ to deceive systems.
    - **{{Cross-Site Request Forgery (CSRF)}}**: Tricking user into _executing
      unwanted actions_.
  - **{{Directory Traversal}}**: Accessing unauthorized files by _climbing
    directory trees_.
- **Cryptographic Attacks**
  - **{{Downgrade Attack}}**: Forcing system to use _weaker security protocols_.
  - **{{Collision Attack}}**: Finding two distinct inputs _producing the same
    hash_.
  - **{{Birthday Attack}}**: Exploiting probability to _find hash collisions
    faster_.
- **Password Attacks**
  - **{{Spraying}}**: Trying _one common password_ against many accounts.
  - **{{Brute Force (Digital)}}**: Trying _all possible combinations_ to guess
    passwords.
    - **{{Dictionary Attack}}**: Using a _list of common words_.
    - **{{Rainbow Table}}**: Using _pre-computed hashes_ to reverse passwords.
- **Indicators of Compromise (IoC)**
  - **{{Account Lockout}}**: Access disabled after _multiple failed login
    attempts_.
  - **{{Concurrent Session Usage}}**: Multiple _simultaneous logins_ using the
    same credentials.
  - **{{Blocked Content}}**: Security controls _preventing access_ to specific
    data.
  - **{{Impossible Travel}}**: Logins from _distant locations_ too quickly.
  - **{{Resource Consumption}}**: Abnormal usage of _CPU, memory, or bandwidth_.
  - **{{Resource Inaccessibility}}**: Data becoming _unavailable to authorized
    users_.
  - **{{Out-of-Cycle Logging}}**: Events recorded _outside normal operational
    hours_.
  - **{{Published/Documented Indicators}}**: Threat markers listed in _public
    intelligence feeds_.
  - **{{Missing Logs}}**: Gaps indicating potential _tampering or unauthorized
    deletion_.
  - **{{Beaconing}}**: Regular signals sent to _establish C2 communication_.

### 2.5 Explain the purpose of mitigation techniques used to secure the enterprise

- **{{Segmentation}}**: Dividing networks to _isolate traffic and limit spread_.
- **Access Control**
  - **{{Access Control List (ACL)}}**: Table of _rules defining rights_ for
    users.
  - **{{Permissions}}**: Specific _actions a user is allowed_ to perform.
  - **{{Least Privilege}}**: Granting only _minimum necessary access rights_.
- **{{Application Allow List}}**: Only _pre-approved software_ can run on
  systems.
- **{{Isolation}}**: Separating systems entirely to _contain potential
  compromises_.
  - **{{Sandboxing}}**: Running programs in _isolated, restricted environments_.
- **{{Patching}}**: Applying updates to _fix security vulnerabilities_.
  - **{{Regression Testing}}**: Ensuring updates _do not break existing
    functionality_.
- **{{Encryption}}**: Encoding data so _only authorized parties can read_.
- **{{Monitoring}}**: Continuous _observation of systems_ for suspicious
  activity.
  - **{{Log Management}}**: _Collecting and analyzing_ system-generated event
    records.
- **{{Configuration Enforcement}}**: Automating settings to _ensure compliance
  with standards_.
- **{{Decommissioning}}**: Securely _removing and destroying_ old systems or
  data.
- **Hardening Techniques**
  - **{{Hardening}}**: Reducing attack surface by _securing system
    configurations_.
    - **{{Attack Surface Reduction}}**: _Removing unnecessary features_ to
      minimize entry points.
  - **{{Endpoint Protection (EPP)}}**: Deploying _antivirus/antimalware_
    directly on host devices.
  - **{{Host-based Firewall}}**: Software _controlling traffic_ entering/leaving
    a single device.
  - **{{Host-based Intrusion Prevention System (HIPS)}}**: Detects and _blocks
    malicious activity_ on a host.
  - **{{Disabling Services}}**: Turning off _unused ports/protocols_ to reduce
    risk.
- **{{Vulnerability Management}}**: Cyclical process of _identifying and
  remediating risks_.

## 3.0 Security Architecture 18%

### 3.1 Compare and contrast security implications of different architecture models

- **Architecture and infrastructure concepts**
  - **{{Cloud Computing}}**: On-demand delivery of _computing services over the
    internet_.
    - **{{Shared Responsibility Model}}**: Defines security duties _shared
      between provider and customer_.
    - **{{Deployment Models}}**:
      - **{{Public Cloud}}**: Services available to _general public via
        internet_.
      - **{{Private Cloud}}**: Services dedicated to _a single organization_.
      - **{{Hybrid Cloud}}**: Combining _on-premises and cloud environments_.
      - **{{Community Cloud}}**: Infrastructure shared by _organizations with
        common concerns_.
    - **{{Service Models}}**:
      - **{{Software as a Service (SaaS)}}**: Provider manages _entire
        application stack_.
      - **{{Platform as a Service (PaaS)}}**: Provider manages _hardware and OS
        tools_.
      - **{{Infrastructure as a Service (IaaS)}}**: Provider manages
        _virtualized hardware resources_.
    - **{{Third-Party Vendors}}**: External partners supplying services,
      _increasing supply chain risk_.
  - **{{Infrastructure as Code (IaC)}}**: Managing infrastructure using
    _machine-readable definition files_.
    - **{{Idempotency}}**: Applying same code repeatedly produces _same result
      every time_.
  - **{{Serverless}}**: Executing code _without managing underlying servers_.
    - **{{Function as a Service (FaaS)}}**: Event-driven execution of _small
      code snippets_.
  - **{{Microservices}}**: Applications built as _collections of small,
    independent services_.
    - **{{API Gateway}}**: Single entry point _managing requests to
      microservices_.
  - **Network infrastructure**
    - **{{Physical Isolation}}**: Physically _disconnecting a system_ from all
      other networks.
      - **{{Air Gap}}**: Extreme isolation measure for _high-security systems_.
    - **{{Logical Segmentation}}**: Separating network traffic _virtually using
      software or VLANs_.
    - **{{Software-Defined Networking (SDN)}}**: Managing network control _via
      software, distinct from hardware_.
      - **{{Control Plane}}**: Centralized decision-making logic _for network
        traffic_.
  - **{{On-Premises}}**: Infrastructure located _physically within the
    organization's facilities_.
  - **Centralized vs. Decentralized**
    - **{{Centralized}}**: Management and security _controlled from a single
      point_.
    - **{{Decentralized}}**: Management _distributed across multiple points_ or
      sites.
  - **{{Containerization}}**: Packaging code and dependencies to _run reliably
    anywhere_.
    - **{{Container Orchestration}}**: Automating deployment and _management of
      containers_ (e.g., K8s).
  - **{{Virtualization}}**: Creating _virtual versions of hardware_ to run
    multiple OSs.
    - **{{Hypervisor}}**: Software creating and _running virtual machines_.
      - **{{Type 1 (Bare Metal)}}**: Hypervisor runs _directly on hardware_.
      - **{{Type 2 (Hosted)}}**: Hypervisor runs _as an application on an OS_.
    - **{{VM Sprawl}}**: Uncontrolled creation of _virtual machines without
      management_.
    - **{{VM Escape}}**: Attacker breaks out of VM to _access host system_.
  - **Specialized Systems**
    - **{{Internet of Things (IoT)}}**: Network of physical objects _embedded
      with sensors/software_.
    - **{{Industrial Control Systems (ICS)}}**: Systems _monitoring and
      controlling_ industrial processes.
      - **{{SCADA}}**: System for _high-level process supervisory management_.
    - **{{Real-Time Operating System (RTOS)}}**: OS processing data with
      _strict, immediate timing requirements_.
    - **{{Embedded Systems}}**: Specialized computing systems _dedicated to
      specific tasks_.
  - **{{High Availability (HA)}}**: Systems designed to _operate continuously
    without failure_.
- **Considerations**
  - **{{Availability}}**: Ensuring systems are _up and accessible when needed_.
  - **{{Resilience}}**: Ability to _withstand and recover_ from adverse
    conditions.
  - **{{Cost}}**: Financial resources required for _implementation and
    maintenance_.
  - **{{Responsiveness}}**: Speed at which a _system reacts to inputs_.
  - **{{Scalability}}**: Ability to handle _increased workloads_ by adding
    resources.
  - **{{Ease of Deployment}}**: Effort required to _install, configure, and
    launch systems_.
  - **{{Risk Transference}}**: Shifting financial impact of _risk to third
    parties_.
  - **{{Ease of Recovery}}**: Speed and simplicity of _restoring operations
    after failure_.
  - **{{Patch Availability}}**: Existence of _vendor updates_ to fix
    vulnerabilities.
  - **{{Inability to Patch}}**: Systems that _cannot be updated_ (e.g.,
    legacy/embedded).
  - **{{Power}}**: Energy supply _required to run infrastructure hardware_.
  - **{{Compute}}**: Processing resources (CPU/RAM) _required for workload
    execution_.

### 3.2 Given a scenario, apply security principles to secure enterprise infrastructure

- **Infrastructure considerations**
  - **{{Device Placement}}**: Strategic location of security devices to
    _maximize visibility_.
  - **{{Security Zones}}**: Logical areas of a network with _specific trust
    levels_.
    - **{{Demilitarized Zone (DMZ)}}**: Buffer zone between _trusted and
      untrusted networks_.
    - **{{Intranet}}**: Private network _internal to an organization_.
    - **{{Extranet}}**: Private network _accessible to authorized outsiders_.
  - **{{Attack Surface}}**: Sum of _all potential entry points_ for attackers.
  - **{{Connectivity}}**: Physical or logical path _enabling data exchange_.
  - **Failure modes**
    - **{{Fail-Open}}**: System _allows all traffic_ upon failure.
    - **{{Fail-Closed}}**: System _blocks all traffic_ upon failure.
  - **Device attribute**
    - **{{Active vs. Passive}}**: Active _intervenes_ in traffic; Passive only
      _observes_.
    - **{{Inline vs. Tap/Monitor}}**: Inline _sits in traffic path_; Tap _copies
      traffic_.
  - **Network appliances**
    - **{{Jump Server}}**: Hardened host used to _access separate security
      zones_.
    - **{{Proxy Server}}**: Intermediate server _acting on behalf of clients_.
    - **{{Intrusion Prevention System (IPS)}}**: Detects and _actively blocks
      malicious traffic_.
    - **{{Intrusion Detection System (IDS)}}**: Monitors and _alerts on
      suspicious activity_.
    - **{{Load Balancer}}**: Distributes traffic across _multiple servers for
      efficiency_.
    - **{{Sensors}}**: Devices or software _collecting data for monitoring_.
  - **Port security**
    - **{{802.1X}}**: IEEE standard for _port-based network access control_.
    - **{{Extensible Authentication Protocol (EAP)}}**: Framework for _multiple
      authentication methods_.
  - **Firewall types**
    - **{{Web Application Firewall (WAF)}}**: Filters and monitors _HTTP traffic
      to applications_.
    - **{{Unified Threat Management (UTM)}}**: Single appliance providing
      _multiple security functions_.
    - **{{Next-Generation Firewall (NGFW)}}**: Firewall with _deep packet
      inspection_ capabilities.
    - **{{Layer 4 / Layer 7}}**: Filtering by _port numbers_ vs. _application
      data_.
- **Secure communication/access**
  - **{{Virtual Private Network (VPN)}}**: Encrypted tunnel providing _secure
    remote access_.
  - **{{Remote Access}}**: Connecting to internal resources from _outside the
    perimeter_.
  - **{{Tunneling}}**: Encapsulating one protocol _within another for
    transport_.
    - **{{Transport Layer Security (TLS)}}**: Protocol providing _encryption for
      web traffic_.
    - **{{Internet Protocol Security (IPSec)}}**: Suite of protocols _securing
      IP communications_.
  - **{{Software-Defined Wide Area Network (SD-WAN)}}**: Managing WAN
    connections _via software control_.
  - **{{Secure Access Service Edge (SASE)}}**: Convergence of _network and
    security services_ in cloud.
- **{{Selection of Effective Controls}}**: Choosing measures based on _risk and
  requirements_.

### 3.3 Compare and contrast concepts and strategies to protect data

- **Data types**
  - **{{Regulated Data}}**: Information subject to _laws and compliance
    regulations_.
    - **{{Personally Identifiable Information (PII)}}**: Any data that can
      _uniquely identify an individual_.
    - **{{Protected Health Information (PHI)}}**: Medical records and
      _health-related personal data_.
    - **{{Payment Card Industry (PCI)}}**: Data related to _credit and debit
      cards_.
  - **{{Trade Secret}}**: Proprietary information providing a _competitive
    business advantage_.
  - **{{Intellectual Property (IP)}}**: Creations of the mind _protected by
    law_.
  - **{{Legal Information}}**: Data related to _litigation, contracts, and
    compliance_.
  - **{{Financial Information}}**: Records of _monetary transactions and
    assets_.
  - **{{Human-Readable vs. Non-Human-Readable}}**: Plain text vs. _binary or
    encrypted data_.
- **Data classifications**
  - **{{Sensitive}}**: General term for data _requiring protection from
    disclosure_.
  - **{{Confidential}}**: Highly sensitive data _restricted to specific
    individuals_.
  - **{{Public}}**: Information with _no restriction on disclosure_.
  - **{{Restricted}}**: Data available only to _authorized internal users_.
  - **{{Private}}**: Personal data _related to specific individuals_.
  - **{{Critical}}**: Information essential for _continued business operations_.
- **General data considerations**
  - **Data states**
    - **{{Data at Rest}}**: Information stored _persistently on physical media_.
    - **{{Data in Transit (Data in Motion)}}**: Information _moving across a
      network_.
    - **{{Data in Use}}**: Information currently _loaded in system memory_.
  - **{{Data Sovereignty}}**: Data is subject to _laws of the country_ where it
    is located.
  - **{{Geolocation}}**: Physical _geographic location_ of data storage.
  - **{{Data Minimization}}**: Collecting only the _minimum data necessary_ for
    a task.
- **Methods to secure data**
  - **{{Geographic Restrictions (Geofencing)}}**: Restricting access based on
    _physical location_.
  - **{{Encryption}}**: Cryptographic protection for _confidentiality and
    integrity_.
  - **{{Hashing}}**: Ensuring _integrity via fixed-length strings_.
  - **{{Masking}}**: _Hiding specific data parts_ for display (e.g., partial
    SSN).
  - **{{Tokenization}}**: Replacing sensitive data with _non-sensitive
    placeholders_.
  - **{{Obfuscation}}**: Making data _difficult for humans to interpret_.
  - **{{Segmentation}}**: Separating data into _distinct security containers_.
  - **{{Permission Restrictions}}**: Controlling access via _authorization and
    ACLs_.
  - **{{Data Loss Prevention (DLP)}}**: Systems designed to _prevent
    unauthorized data transfer_.

### 3.4 Explain the importance of resilience and recovery in security architecture

- **{{Resilience}}**: Ability to _maintain operations during a disaster_.
- **High availability**
  - **{{Load Balancing}}**: Distributing workloads across _multiple computing
    resources_.
  - **{{Clustering}}**: Grouping multiple servers to _act as a single system_.
- **Site considerations**
  - **{{Hot Site}}**: Fully operational facility _ready for immediate failover_.
  - **{{Cold Site}}**: Empty facility _requiring equipment and data setup_.
  - **{{Warm Site}}**: Facility with _equipment but no current data_.
  - **{{Geographic Dispersion}}**: Locating resources in _different physical
    regions_.
- **{{Platform Diversity}}**: Using _different operating systems or vendors_ to
  reduce risk.
- **{{Multi-Cloud Systems}}**: Distributing workloads across _multiple cloud
  service providers_.
- **{{Continuity of Operations (COOP)}}**: Plan for _restoring critical business
  functions_.
- **Capacity planning**
  - **{{People}}**: Ensuring _adequate staff skills and availability_.
  - **{{Technology}}**: Planning for _hardware and software requirements_.
  - **{{Infrastructure}}**: Planning for _facility and network needs_.
- **Testing**
  - **{{Tabletop Exercise}}**: Discussion-based walk-through of _incident
    response plans_.
  - **{{Failover}}**: Automatically switching to a _redundant standby system_.
  - **{{Simulation}}**: Realistic test of _response procedures in controlled
    environment_.
  - **{{Parallel Processing}}**: Running new and old _systems simultaneously for
    verification_.
- **Backups**
  - **{{Onsite / Offsite}}**: Storing backups _locally vs. in remote location_.
  - **{{Frequency}}**: How often _data snapshots are taken_.
  - **{{Encryption}}**: Protecting backup data from _unauthorized access_.
  - **{{Snapshots}}**: Point-in-time _read-only copy of data_.
  - **{{Recovery}}**: Process of _restoring data from backups_.
  - **{{Replication}}**: Real-time _copying of data to another site_.
  - **{{Journaling}}**: Recording changes to _enable recovery from failure_.
- **Power**
  - **{{Generator}}**: Auxiliary power source for _long-term outages_.
  - **{{Uninterruptible Power Supply (UPS)}}**: Battery backup for _short-term
    power stability_.
  - **{{Managed Power Distribution Unit (PDU)}}**: Device for _monitoring and
    controlling power outlets_.

## 4.0 Security Operations 28%

### 4.1 Given a scenario, apply common security techniques to computing resources

- **Secure baselines**
  - **{{Establish}}**: Defining the _minimum security configuration_ for
    systems.
    - **{{Standard Operating Environment (SOE)}}**: Uniform implementation of
      _OS and applications_ across an organization.
    - **{{Gold Image}}**: Pre-configured _system template_ used for rapid,
      secure deployment.
  - **{{Deploy}}**: Implementing _baselines across the enterprise_
    infrastructure.
  - **{{Maintain}}**: Regularly _auditing and updating_ baselines to ensure
    compliance.
- **Hardening targets**
  - **{{Mobile Devices}}**: Securing _smartphones and tablets_ against
    unauthorized access.
  - **{{Workstations}}**: Hardening _desktop and laptop computers_ for
    end-users.
  - **{{Switches}}**: Securing _network infrastructure devices_ at Layer 2.
  - **{{Routers}}**: Hardening _gateways that route traffic_ between networks.
  - **{{Cloud Infrastructure}}**: Securing _virtualized resources and services_
    in the cloud.
  - **{{Servers}}**: Hardening _high-value systems_ providing network services.
  - **{{ICS / SCADA}}**: Securing _industrial control systems_ and supervisory
    hardware.
  - **{{Embedded Systems}}**: Hardening _dedicated-function computing devices_
    within larger systems.
  - **{{RTOS}}**: Securing _operating systems_ with strict timing requirements.
  - **{{IoT Devices}}**: Hardening _interconnected physical objects_ with
    limited resources.
- **Wireless devices**
  - **Installation considerations**
    - **{{Site Survey}}**: Process of _analyzing RF environment_ for optimal
      placement.
    - **{{Heat Map}}**: Visual representation of _wireless signal strength_ and
      coverage.
- **Mobile solutions**
  - **{{Mobile Device Management (MDM)}}**: Centralized software for _managing
    mobile device_ security.
  - **{{Unified Endpoint Management (UEM)}}**: Single tool for _managing all
    endpoint_ types.
  - **Deployment models**
    - **{{Bring Your Own Device (BYOD)}}**: Employees use _personal devices_ for
      work purposes.
    - **{{Corporate-Owned, Personally Enabled (COPE)}}**: Company _provides
      device_ for work and personal use.
    - **{{Choose Your Own Device (CYOD)}}**: Employees _choose from approved_
      company-owned devices.
  - **Connection methods**
    - **{{Cellular}}**: Long-range _mobile network_ data communication.
    - **{{Wi-Fi}}**: Local area _wireless networking_ based on 802.11.
    - **{{Bluetooth}}**: Short-range _wireless technology_ for device pairing.
- **Wireless security settings**
  - **{{Wi-Fi Protected Access 3 (WPA3)}}**: Latest _wireless security standard_
    with stronger encryption.
  - **{{RADIUS}}**: Protocol for _centralized authentication_ in wireless
    networks.
  - **{{Cryptographic Protocols}}**: Mathematical methods for _securing
    wireless_ data (e.g., AES).
  - **{{Authentication Protocols}}**: Methods for _verifying identity_ (e.g.,
    EAP-TLS).
- **Application security**
  - **{{Input Validation}}**: Sanitizing _user-provided data_ to prevent
    injection attacks.
  - **{{Secure Cookies}}**: Protecting _session data_ with attributes like
    Secure and HttpOnly.
  - **{{Static Code Analysis (SAST)}}**: Reviewing _source code_ without
    executing the program.
  - **{{Dynamic Code Analysis (DAST)}}**: Testing _running applications_ for
    security vulnerabilities.
  - **{{Code Signing}}**: Using _digital signatures_ to verify software
    integrity and origin.
- **{{Sandboxing}}**: Running programs in _isolated, restricted environments_
  for safety.
- **{{Monitoring}}**: Continuous _observation of resources_ to detect suspicious
  activity.

### 4.2 Explain the security implications of proper hardware, software, and data asset management

- **{{Acquisition / Procurement Process}}**: Securely _sourcing and purchasing_
  hardware and software.
  - **{{Supply Chain Security}}**: Ensuring _integrity and trust_ of components
    from vendors.
- **Assignment / Accounting**
  - **{{Ownership}}**: Assigning a specific individual _accountable for an
    asset_.
  - **{{Classification}}**: Categorizing assets based on _sensitivity and
    value_.
- **Monitoring / Asset Tracking**
  - **{{Inventory}}**: Maintaining an _up-to-date list_ of all organizational
    assets.
  - **{{Enumeration}}**: Detailed _discovery of software and services_ on
    systems.
- **Disposal / Decommissioning**
  - **{{Sanitization}}**: Process of _removing data_ from storage media
    securely.
    - **{{Clearing}}**: Overwriting data to _prevent standard recovery_ methods.
    - **{{Purging}}**: Removing data to _prevent laboratory recovery_ methods.
  - **{{Destruction}}**: Physically _destroying media_ to make data
    unrecoverable.
  - **{{Certification}}**: Formal documentation _confirming secure data
    destruction_.
  - **{{Data Retention}}**: Policy defining _how long data is kept_ before
    disposal.
- **{{Asset Lifecycle}}**: Managing an asset from _acquisition to final
  disposal_.

### 4.3 Explain various activities associated with vulnerability management

- **Identification methods**
  - **{{Vulnerability Scan}}**: Automated tool _identifying known security
    weaknesses_.
  - **Application security**
    - **{{Static Analysis (SAST)}}**: Reviewing _source code without execution_.
    - **{{Dynamic Analysis (DAST)}}**: Testing _running applications for flaws_.
    - **{{Package Monitoring}}**: Tracking _vulnerabilities in software
      dependencies_.
  - **Threat feed**
    - **{{Open-Source Intelligence (OSINT)}}**: Intelligence collected from
      _publicly available sources_.
    - **{{Proprietary / Third-Party}}**: Paid intelligence _provided by security
      vendors_.
    - **{{Information-Sharing Organization (ISAO)}}**: Entity for _sharing
      threat intelligence_ between peers.
    - **{{Dark Web}}**: Hidden network used for _illicit data exchange_.
  - **{{Penetration Testing}}**: Authorized _simulated attack_ to evaluate
    security.
  - **{{Responsible Disclosure Program}}**: Framework for _reporting
    vulnerabilities_ to vendors safely.
    - **{{Bug Bounty Program}}**: Offering _rewards for discovered
      vulnerabilities_.
  - **{{System / Process Audit}}**: Formal _evaluation of compliance_ and
    security controls.
- **Analysis**
  - **{{Confirmation}}**: Verifying a _vulnerability actually exists_.
    - **{{False Positive}}**: Incorrectly _identifying a non-existent
      vulnerability_.
    - **{{False Negative}}**: Failing to _identify an actual vulnerability_.
  - **{{Prioritize}}**: Ranking vulnerabilities based on _risk and impact_.
  - **{{Common Vulnerability Scoring System (CVSS)}}**: Standardized framework
    for _rating vulnerability severity_.
  - **{{Common Vulnerabilities and Exposures (CVE)}}**: Dictionary of _publicly
    disclosed security flaws_.
  - **{{Vulnerability Classification}}**: Grouping vulnerabilities by _type and
    origin_.
  - **{{Exposure Factor (EF)}}**: Percentage of _asset value lost_ from threat.
  - **{{Environmental Variables}}**: Context-specific _factors affecting
    vulnerability risk_.
  - **{{Industry / Organizational Impact}}**: Assessing how _vulnerabilities
    affect business goals_.
  - **{{Risk Tolerance}}**: Amount of _risk an organization accepts_.
- **Vulnerability response and remediation**
  - **{{Patching}}**: Applying software updates to _fix security flaws_.
  - **{{Insurance}}**: Transferring financial _risk to a third party_.
  - **{{Segmentation}}**: Isolating systems to _limit vulnerability exposure_.
  - **{{Compensating Controls}}**: Alternative measures when _primary controls
    fail_.
  - **{{Exceptions and Exemptions}}**: Formal _approval to bypass_ security
    requirements.
- **Validation of remediation**
  - **{{Rescanning}}**: Performing _new scans_ to verify fixes.
  - **{{Audit}}**: Independent _review of remediation_ actions.
  - **{{Verification}}**: Ensuring _fixes work as intended_ without issues.
- **{{Reporting}}**: Documenting _vulnerability status and remediation_
  progress.

### 4.4 Explain security alerting and monitoring concepts and tools

- **Monitoring computing resources**
  - **{{Systems}}**: Continuous observation of _operating systems and hardware_.
  - **{{Applications}}**: Tracking the _performance and security_ of software.
  - **{{Infrastructure}}**: Monitoring _network devices and communication_
    pathways.
- **Activities**
  - **{{Log Aggregation}}**: Centralizing _event records from multiple sources_.
  - **{{Alerting}}**: Real-time _notification of suspicious_ or critical events.
  - **{{Scanning}}**: Systematic _probing of resources_ for vulnerabilities.
  - **{{Reporting}}**: Generating _documentation of monitoring_ findings and
    trends.
  - **{{Archiving}}**: Long-term _storage of historical_ log data.
  - **Alert response and remediation / validation**
    - **{{Quarantine}}**: Isolating _compromised or suspicious_ systems from
      network.
    - **{{Alert Tuning}}**: Adjusting _thresholds to reduce_ false positives.
- **Tools**
  - **{{Security Content Automation Protocol (SCAP)}}**: Standardized _method
    for automating_ security management.
  - **{{Benchmarks}}**: Industry-standard _best practices for securing_
    configurations.
  - **{{Agents / Agentless}}**: Software _installed on host_ vs _remote
    monitoring_.
  - **{{Security Information and Event Management (SIEM)}}**: Centralized
    _analysis of security_ log data.
  - **{{Antivirus / Antimalware}}**: Software _detecting and removing_ malicious
    programs.
  - **{{Data Loss Prevention (DLP)}}**: Detecting and _preventing unauthorized
    data_ exfiltration.
  - **{{SNMP Traps}}**: Unsolicited _messages sent by devices_ to managers.
  - **{{NetFlow}}**: Protocol for _collecting IP traffic_ information.
  - **{{Vulnerability Scanners}}**: Tools that _scan for known_ security
    weaknesses.
- **{{False Positive / Negative Tuning}}**: Optimizing _detection accuracy to
  minimize_ errors.
- **{{Behavioral Monitoring}}**: Identifying _deviations from established_
  normal activity.

### 4.5 Given a scenario, modify enterprise capabilities to enhance security

- **{{Firewall}}**: Device _filtering traffic based on defined rules_.
  - **{{Rules}}**: Instructions defining _permitted or blocked traffic_.
  - **{{Access Control List (ACL)}}**: Table of rules _managing network access_.
  - **{{Implicit Deny}}**: Rule _blocking all traffic_ not explicitly allowed.
  - **{{Ports / Protocols}}**: Specific _communication channels and rules_
    filtered.
  - **{{Screened Subnet}}**: Network segment _isolated by firewalls_.
- **{{IDS / IPS}}**: Systems _detecting or preventing_ network intrusions.
  - **{{Trends}}**: Identifying _patterns of activity_ over time.
  - **{{Signatures}}**: Fixed patterns _matching known malicious activity_.
  - **{{Heuristics / Behavioral}}**: Detecting anomalies _based on baseline
    deviations_.
- **{{Web Filter}}**: Control mechanism _restricting access to websites_.
  - **{{Agent-Based}}**: Filtering software _installed on local host_.
  - **{{Centralized Proxy}}**: Single point _intercepting and filtering_ web
    requests.
  - **{{URL Scanning}}**: Analyzing _web addresses for malicious content_.
  - **{{Content Categorization}}**: Grouping websites _by topic for blocking_.
  - **{{Block Rules}}**: Specific settings _preventing access to resources_.
  - **{{Reputation}}**: Scoring systems _identifying untrustworthy web sources_.
- **Operating system security**
  - **{{Group Policy}}**: Windows feature _managing system configurations_
    centrally.
  - **{{SELinux / AppArmor}}**: Kernel modules _enforcing mandatory access
    controls_.
- **Implementation of secure protocols**
  - **{{Protocol Selection}}**: Choosing _encrypted versions_ of network
    services.
  - **{{Port Selection}}**: Assigning _secure communication endpoints_.
  - **{{Transport Method}}**: How _data is moved_ across the network.
- **{{DNS Filtering}}**: Blocking access _to malicious domains_ via DNS.
  - **{{Sinkholing}}**: Redirecting _malicious traffic to controlled_ IP.
- **Email security**
  - **{{Domain-based Message Authentication Reporting and Conformance
    (DMARC)}}**: Framework _authenticating email and preventing_ spoofing.
  - **{{DomainKeys Identified Mail (DKIM)}}**: Cryptographic _signature
    verifying email origin_.
  - **{{Sender Policy Framework (SPF)}}**: Record _listing authorized email
    sending_ hosts.
  - **{{Gateway}}**: Appliance _filtering incoming and outgoing_ mail.
- **{{File Integrity Monitoring (FIM)}}**: Detecting _unauthorized changes to
  critical_ files.
- **{{Data Loss Prevention (DLP)}}**: Preventing _unauthorized transfer of
  sensitive_ data.
- **{{Network Access Control (NAC)}}**: Enforcing _security policies on devices_
  connecting.
- **{{Endpoint Detection and Response (EDR)}}**: Monitoring _host activities to
  detect_ threats.
- **{{Extended Detection and Response (XDR)}}**: Integrating _security data
  across multiple_ layers.
- **{{User Behavior Analytics (UBA)}}**: Tracking _user actions to identify_
  anomalies.

### 4.6 Given a scenario, implement and maintain identity and access management

- **{{Provisioning / De-provisioning}}**: Managing the _lifecycle of user
  accounts_.
- **{{Permission Assignments}}**: Granting _specific rights to resources_.
- **{{Identity Proofing}}**: Verifying a _person is who they claim_.
- **{{Federation}}**: Linking _identities across multiple organizations_.
  - **{{Identity Provider (IdP)}}**: Entity _creating and managing_ user
    identities.
  - **{{Service Provider (SP)}}**: Entity _providing the resource_ to user.
- **{{Single Sign-On (SSO)}}**: One set of _credentials for multiple systems_.
  - **{{Lightweight Directory Access Protocol (LDAP)}}**: Protocol for
    _accessing directory information_.
  - **{{Open Authorization (OAuth)}}**: Framework for _token-based delegated
    authorization_.
  - **{{Security Assertions Markup Language (SAML)}}**: XML-based standard for
    _exchanging authentication data_.
- **{{Interoperability}}**: Ability of _different systems to work together_.
- **{{Attestation}}**: Formal _confirmation of system or identity_ state.
- **Access controls**
  - **{{Mandatory Access Control (MAC)}}**: OS _enforces policy via security
    labels_.
  - **{{Discretionary Access Control (DAC)}}**: Owner _manages permissions for
    their resources_.
  - **{{Role-Based Access Control (RBAC)}}**: Permissions _assigned based on
    organizational roles_.
  - **{{Rule-Based Access Control}}**: Access _granted based on system rules_.
  - **{{Attribute-Based Access Control (ABAC)}}**: Access _granted based on
    specific characteristics_.
  - **{{Time-of-Day Restrictions}}**: Limiting access _to specific hours_.
  - **{{Least Privilege}}**: Granting only _minimum necessary access_.
- **{{Multifactor Authentication (MFA)}}**: Requiring _multiple independent
  credentials_ for access.
  - **Implementations**
    - **{{Biometrics}}**: Authentication _based on physical characteristics_.
    - **{{Hard / Soft Tokens}}**: Physical devices vs _software-generated
      codes_.
    - **{{Security Keys}}**: Dedicated _hardware tokens for authentication_.
  - **Factors**
    - **{{Something You Know}}**: Knowledge-based factor _like a password_.
    - **{{Something You Have}}**: Possession-based factor _like a phone_.
    - **{{Something You Are}}**: Inherence-based factor _like a fingerprint_.
    - **{{Somewhere You Are}}**: Location-based factor _like IP address_.
    - **{{Something You Do}}**: Action-based factor _like typing patterns_.
- **Password concepts**
  - **Password best practices**
    - **{{Length}}**: Total _number of characters_ in password.
    - **{{Complexity}}**: Using _diverse character types_ in password.
    - **{{Reuse}}**: Prohibiting _using previous passwords_ again.
    - **{{Expiration}}**: Forcing _passwords to be changed_ periodically.
    - **{{Age}}**: Time _since password was last_ changed.
  - **{{Password Managers}}**: Software _securely storing and managing_
    credentials.
  - **{{Passwordless}}**: Authentication _without using static passwords_.
- **{{Privileged Access Management (PAM)}}**: Tools _securing high-level
  administrative_ accounts.
  - **{{Just-in-Time (JIT) Permissions}}**: Granting _temporary elevated access_
    when needed.
  - **{{Password Vaulting}}**: Storing _administrative credentials in secure_
    repository.
  - **{{Ephemeral Credentials}}**: Short-lived _secrets that expire_ after use.

### 4.7 Explain the importance of automation and orchestration related to secure operations

- **{{Security Orchestration, Automation, and Response (SOAR)}}**: Tools for
  _automating incident response_ and workflows.
- **Use cases of automation and scripting**
  - **{{User Provisioning}}**: Automating _creation and management_ of accounts.
  - **{{Resource Provisioning}}**: Automated _allocation of computing_
    resources.
  - **{{Guard Rails}}**: Automated _boundaries ensuring systems_ stay compliant.
  - **{{Security Groups}}**: Automating _assignment of firewall_ rules.
  - **{{Ticket Creation}}**: Generating _incident records automatically_ in
    systems.
  - **{{Escalation}}**: Automated _routing of high-priority_ events.
  - **{{Enabling / Disabling Services and Access}}**: Automated _control of
    system_ states.
  - **{{Continuous Integration / Continuous Deployment (CI/CD)}}**: Automating
    _software development and testing_ lifecycles.
  - **{{Integrations and APIs}}**: Connecting _different systems via automated_
    interfaces.
- **Benefits**
  - **{{Efficiency / Time Saving}}**: Reducing _manual effort and accelerating_
    tasks.
  - **{{Enforcing Baselines}}**: Ensuring _consistent configurations across_ the
    enterprise.
  - **{{Standard Infrastructure Configurations}}**: Maintaining _uniform
    implementations of_ systems.
  - **{{Scaling in a Secure Manner}}**: Growing _infrastructure without
    compromising_ security.
  - **{{Employee Retention}}**: Reducing _burnout by automating_ repetitive
    tasks.
  - **{{Reaction Time}}**: Faster _response to security_ events.
  - **{{Workforce Multiplier}}**: Enhancing _capability of existing_ security
    staff.
- **Other considerations**
  - **{{Complexity}}**: Challenge of _managing intricate automated_ workflows.
  - **{{Cost}}**: Investment _required for automation_ tools.
  - **{{Single Point of Failure}}**: Risk if _automation system itself_ fails.
  - **{{Technical Debt}}**: Accumulation of _unoptimized or outdated_ code.
  - **{{Ongoing Supportability}}**: Long-term _maintenance requirements for_
    scripts.
- **{{Playbooks}}**: Documented _procedures for specific_ security responses.
- **{{Runbooks}}**: Automated _execution of playbook_ steps.

### 4.8 Explain appropriate incident response activities

- **{{Incident Response Plan (IRP)}}**: Documented procedures for _responding to
  security incidents_.
- **Process**
  - **{{Preparation}}**: Establishing _plans, tools, and teams_ before
    incidents.
  - **{{Detection}}**: Identifying _potential security incidents_ from alerts.
  - **{{Analysis}}**: Investigating _scope, impact, and root cause_ of
    incidents.
  - **{{Containment}}**: Limiting _damage and preventing spread_ of the
    incident.
  - **{{Eradication}}**: Removing _malicious components and vulnerabilities_
    from systems.
  - **{{Recovery}}**: Restoring _systems to normal operation_ securely.
  - **{{Lessons Learned}}**: Reviewing incident to _improve future response_
    (Post-Incident Activity).
- **{{Training}}**: Educating staff on _incident response roles_ and procedures.
- **Testing**
  - **{{Tabletop Exercise}}**: Discussion-based _simulation of incident
    scenarios_.
  - **{{Simulation}}**: Realistic _practice of response procedures_ in
    controlled environment.
- **{{Root Cause Analysis}}**: Identifying the _fundamental reason_ an incident
  occurred.
- **{{Threat Hunting}}**: Proactively _searching for undetected threats_ in the
  network.
- **Digital Forensics**
  - **{{Legal Hold}}**: Preserving data _relevant to potential litigation_.
  - **{{Chain of Custody}}**: Documenting _handling of evidence_ to ensure
    integrity.
  - **{{Acquisition}}**: Securely _collecting evidence_ without alteration.
  - **{{Reporting}}**: Documenting _forensic findings_ for stakeholders.
  - **{{Preservation}}**: Protecting evidence _from modification or
    destruction_.
  - **{{E-Discovery}}**: Identifying and _collecting electronic evidence_ for
    legal cases.
  - **{{Order of Volatility}}**: Collecting evidence _from most to least_
    volatile.

### 4.9 Given a scenario, use data sources to support an investigation

- **Log data**
  - **{{Firewall Logs}}**: Records of _network traffic filtered by firewalls_.
  - **{{Application Logs}}**: Records of _events from specific software_
    programs.
  - **{{Endpoint Logs}}**: Records of _activities on individual host_ devices.
  - **{{OS-Specific Security Logs}}**: Records of _authentication and system
    access_ events.
  - **{{IPS / IDS Logs}}**: Records of _detected or prevented intrusion_
    attempts.
  - **{{Network Logs}}**: Records of _communication between devices_ on network.
  - **{{Metadata}}**: Contextual data _describing properties of other_ data.
- **Data sources**
  - **{{Vulnerability Scans}}**: Automated reports _identifying known system
    weaknesses_.
  - **{{Automated Reports}}**: Periodically generated _summaries of security
    status_.
  - **{{Dashboards}}**: Visual displays _summarizing real-time security_ data.
  - **{{Packet Captures (PCAP)}}**: Full recording of _network traffic for
    analysis_.
  - **{{NetFlow}}**: Protocol for _collecting IP traffic statistics_.
  - **{{Artifact}}**: Digital residue _left behind by system_ or user activity.
- **{{Timeline Analysis}}**: Chronological sequencing of _events to reconstruct_
  incidents.
- **{{Log Normalization}}**: Converting logs into _a common standardized
  format_.
- **{{Event Correlation}}**: Linking related _events from different data_
  sources.

## 5.0 Security Program Management and Oversight 20%

### 5.1 Summarize elements of effective security governance

- **{{Governance}}**: Framework for _directing and controlling_ security
  strategy.
- **{{Guidelines}}**: Non-mandatory _recommendations for achieving_ security
  goals.
- **{{Policies}}**: High-level _statements of management intent_ and direction.
  - **{{Acceptable Use Policy (AUP)}}**: Rules for _using organizational assets_
    responsibly.
  - **{{Information Security Policies}}**: Overarching rules _protecting data
    and systems_.
  - **{{Business Continuity}}**: Plans ensuring _operational availability
    during_ disruptions.
  - **{{Disaster Recovery (DR)}}**: Process of _restoring technology
    infrastructure_ after failure.
  - **{{Incident Response (IR)}}**: Structured approach for _managing security
    breaches_.
  - **{{Software Development Lifecycle (SDLC)}}**: Framework for _securely
    building and maintaining_ software.
  - **{{Change Management}}**: Process controlling _lifecycle of system
    updates_.
- **{{Standards}}**: Mandatory _requirements for hardware and software_
  configurations.
- **{{Procedures}}**: Detailed _step-by-step instructions_ for tasks.
  - **{{Onboarding / Offboarding}}**: Process of _managing user entry and exit_.
  - **{{Playbooks / Runbooks}}**: Operational guides for _responding to
    incidents_.
- **External considerations**
  - **{{Regulatory}}**: Requirements mandated by _government or industry laws_.
  - **{{Legal}}**: Compliance with _civil and criminal statutes_.
  - **{{Industry}}**: Standards set by _professional security organizations_.
  - **{{Local / Regional / National / Global}}**: Geographic levels of
    _compliance and regulation_.
- **{{Monitoring and Revision}}**: Continuously _reviewing and updating_
  security documents.
- **Types of governance structures**
  - **{{Boards / Committees}}**: Groups providing _strategic security
    oversight_.
  - **{{Government Entities}}**: Regulatory bodies _enforcing legal
    requirements_.
  - **{{Centralized / Decentralized}}**: Management from _one point_ vs
    _multiple units_.
- **Roles and responsibilities for systems and data**
  - **{{Owner}}**: Individual _accountable for an asset's_ security.
  - **{{Controller}}**: Entity _determining purpose of data_ processing.
  - **{{Processor}}**: Entity _handling data on behalf_ of controller.
  - **{{Custodian / Steward}}**: Individual _responsible for maintaining_ data
    quality.
- **{{Due Diligence}}**: Research performed to _identify security risks_.
- **{{Due Care}}**: Implementing _reasonable security measures_ for protection.

### 5.2 Explain elements of the risk management process

- **{{Risk Management}}**: Process of _identifying, assessing, and mitigating_
  risks.
- **{{Risk Identification}}**: Discovering and _documenting potential
  organizational threats_.
- **Risk assessment**
  - **{{Ad hoc}}**: Performed _as needed for specific_ events.
  - **{{Recurring}}**: Performed on _a regular periodic_ schedule.
  - **{{One-time}}**: Performed once for _a specific project_.
  - **{{Continuous}}**: Constant _monitoring of the risk_ landscape.
- **Risk analysis**
  - **{{Qualitative}}**: Analysis based on _subjective judgment and experience_.
  - **{{Quantitative}}**: Analysis based on _numerical data and metrics_.
  - **{{Single Loss Expectancy (SLE)}}**: Monetary loss from _a single event_.
  - **{{Annualized Loss Expectancy (ALE)}}**: Estimated _yearly loss from risk_.
  - **{{Annualized Rate of Occurrence (ARO)}}**: Frequency of _risk events per
    year_.
  - **{{Probability / Likelihood}}**: Chance that _a threat will occur_.
  - **{{Exposure Factor (EF)}}**: Percentage of _asset value lost_.
  - **{{Impact}}**: Severity of _damage from threat_ realization.
- **Risk register**
  - **{{Key Risk Indicators (KRI)}}**: Metrics used to _measure risk levels_.
  - **{{Risk Owner}}**: Individual _accountable for managing_ specific risk.
  - **{{Risk Threshold}}**: Level of _risk that triggers action_.
- **{{Risk Tolerance}}**: Maximum _risk an organization accepts_.
- **Risk appetite**
  - **{{Expansionary}}**: Willing to _accept higher risk_ for growth.
  - **{{Conservative}}**: Seeking to _minimize risk exposure_.
  - **{{Neutral}}**: Balanced approach to _risk and reward_.
- **Risk management strategies**
  - **{{Transfer}}**: Shifting _risk to another party_ (e.g., insurance).
  - **{{Accept}}**: Acknowledging _risk without taking action_.
    - **{{Exemption / Exception}}**: Documented _approval to bypass_ controls.
  - **{{Avoid}}**: Eliminating _risk by stopping_ activity.
  - **{{Mitigate}}**: Reducing _risk via security_ controls.
- **{{Risk Reporting}}**: Communicating _risk status to stakeholders_.
- **Business impact analysis (BIA)**
  - **{{Recovery Time Objective (RTO)}}**: Maximum _acceptable downtime for
    systems_.
  - **{{Recovery Point Objective (RPO)}}**: Maximum _acceptable data loss_
    measured in time.
  - **{{Mean Time to Repair (MTTR)}}**: Average _time to fix_ failed systems.
  - **{{Mean Time Between Failures (MTBF)}}**: Average _time between system
    failures_.
- **{{Inherent Risk}}**: Risk _before any security controls_ are applied.
- **{{Residual Risk}}**: Risk _remaining after security controls_ are applied.

### 5.3 Explain the processes associated with third-party risk assessment and management

- **Vendor assessment**
  - **{{Penetration Testing}}**: Assessing vendor security _via simulated
    cyberattacks_.
  - **{{Right-to-Audit Clause}}**: Contract term allowing _direct inspection of
    vendor_.
  - **{{Evidence of Internal Audits}}**: Proof vendor performs _own security
    assessments_.
  - **{{Independent Assessments}}**: Evaluation by an _unbiased third party_.
  - **{{Supply Chain Analysis}}**: Evaluating risks across the _entire
    production network_.
- **Vendor selection**
  - **{{Due Diligence}}**: Researching vendor _before signing contracts_.
  - **{{Conflict of Interest}}**: Situations where _personal gain compromises
    judgment_.
- **Agreement types**
  - **{{Service-Level Agreement (SLA)}}**: Contract defining _performance
    standards and uptime_.
  - **{{Memorandum of Agreement (MOA)}}**: Legal document _describing
    cooperative relationship_.
  - **{{Memorandum of Understanding (MOU)}}**: Formal agreement _outlining
    mutual goals_.
  - **{{Master Service Agreement (MSA)}}**: Overarching contract _governing
    long-term relationship_.
  - **{{Work Order (WO) / Statement of Work (SOW)}}**: Specific details of
    _deliverables and timelines_.
  - **{{Non-Disclosure Agreement (NDA)}}**: Contract protecting _confidential
    information from disclosure_.
  - **{{Business Partners Agreement (BPA)}}**: Contract defining _obligations of
    partnership_.
- **{{Vendor Monitoring}}**: Continuous _oversight of vendor performance_ and
  security.
- **{{Questionnaires}}**: Tools for _gathering security information_ from
  vendors.
- **{{Rules of Engagement (RoE)}}**: Guidelines for _conducting security tests_.
- **{{Interconnection Security Agreement (ISA)}}**: Agreement defining
  _technical requirements for connection_.
- **{{Offboarding}}**: Process of _terminating vendor relationship_ securely.

### 5.4 Summarize elements of effective security compliance

- **Compliance reporting**
  - **{{Internal}}**: Reports created for _management and stakeholders_.
  - **{{External}}**: Reports created for _regulators and auditors_.
- **Consequences of non-compliance**
  - **{{Fines}}**: Monetary penalties _levied by regulators_.
  - **{{Sanctions}}**: Official penalties or _restrictions on business
    operations_.
  - **{{Reputational Damage}}**: Loss of trust _harming brand value_.
  - **{{Loss of License}}**: Revocation of _legal permission to operate_.
  - **{{Contractual Impacts}}**: Breach of contract _leading to termination_.
- **Compliance monitoring**
  - **{{Due Diligence}}**: Research ensuring _risks are identified_.
  - **{{Due Care}}**: Actions taken to _mitigate identified risks_.
  - **{{Attestation / Acknowledgement}}**: Formal _verification of compliance_
    status.
  - **{{Internal / External}}**: Monitoring performed by _own staff vs third
    parties_.
  - **{{Automation}}**: Using tools to _continuously verify compliance_.
- **Privacy**
  - **{{Privacy Impact Assessment (PIA)}}**: Identifying risks to _personally
    identifiable information_.
  - **Legal implications**
    - **{{Local / Regional}}**: Laws specific to _state or province_.
    - **{{National}}**: Laws applying to _entire country_.
    - **{{Global}}**: Regulations affecting _international operations_ (e.g.,
      GDPR).
  - **{{Data Subject}}**: Individual _to whom the data belongs_.
  - **{{Controller vs. Processor}}**: Entity determining _purpose vs entity
    processing_ data.
  - **{{Ownership}}**: Rights and _responsibilities for data_.
  - **{{Data Inventory and Retention}}**: Cataloging data and _defining storage
    duration_.
  - **{{Right to be Forgotten}}**: User's right to _have data erased_.
  - **{{Data Breach Notification}}**: Mandated reporting of _compromised
    personal data_.

### 5.5 Explain types and purposes of audits and assessments

- **{{Attestation}}**: Formal _confirmation of compliance_ or status.
- **Internal**
  - **{{Compliance Audit}}**: Internal review verifying _adherence to rules_.
  - **{{Audit Committee}}**: Board group _overseeing financial and security_
    reporting.
  - **{{Self-Assessments}}**: Internal review _performed by department_ staff.
- **External**
  - **{{Regulatory Audit}}**: Assessment by _government or oversight_ body.
  - **{{Examinations}}**: Formal _evaluation of security_ controls.
  - **{{Assessment}}**: Systematic _review of security_ posture.
  - **{{Independent Third-Party Audit}}**: Verification by _unbiased external_
    entity.
- **{{Penetration Testing}}**: Authorized _simulated attack_ to find weaknesses.
  - **{{Physical Pen-Test}}**: Testing _access to tangible_ assets.
  - **{{Offensive vs. Defensive}}**: Attack-focused vs _protection-focused_
    strategies.
  - **{{Integrated (Purple Team)}}**: Combined _offensive and defensive_
    testing.
  - **{{Known Environment (White Box)}}**: Tester has _full knowledge_ of
    target.
  - **{{Partially Known (Gray Box)}}**: Tester has _limited knowledge_ of
    target.
  - **{{Unknown Environment (Black Box)}}**: Tester has _no knowledge_ of
    target.
  - **{{Reconnaissance}}**: Gathering _information about a target_ system.
    - **{{Passive Recon}}**: Gathering info _without direct interaction_.
    - **{{Active Recon}}**: Gathering info _via direct interaction_.
- **{{Vulnerability Assessment}}**: Identifying _known security weaknesses_ in
  systems.
- **{{Gap Analysis}}**: Comparing _current performance with_ desired state.

### 5.6 Given a scenario, implement security awareness practices

- **{{Phishing}}**: Deceptive attempts to _steal sensitive information_ via
  email.
  - **{{Campaigns}}**: Coordinated _series of phishing_ attacks.
  - **{{Recognizing a Phishing Attempt}}**: Identifying _indicators of
    malicious_ intent.
  - **{{Responding to Suspicious Messages}}**: Reporting and _deleting
    potentially harmful_ emails.
  - **{{Simulated Phishing}}**: Testing user _resilience to phishing_ attacks.
- **Anomalous behavior recognition**
  - **{{Risky}}**: Actions that _increase likelihood_ of security incidents.
  - **{{Unexpected}}**: Events _deviating from normal_ operational patterns.
  - **{{Unintentional}}**: Accidental _actions causing security_ issues.
- **User guidance and training**
  - **{{Policy / Handbooks}}**: Documents _outlining security rules_ and
    procedures.
  - **{{Situational Awareness}}**: Being _alert to potential security_ threats.
  - **{{Insider Threat}}**: Malicious or negligent _actions by authorized
    users_.
  - **{{Password Management}}**: Creating and _maintaining strong credentials_.
  - **{{Removable Media and Cables}}**: Risks associated with _external storage
    devices_.
  - **{{Social Engineering}}**: Manipulating _people into performing_ actions.
  - **{{Operational Security (OpSec)}}**: Protecting _critical information from_
    adversaries.
  - **{{Hybrid / Remote Work}}**: Securing _environments outside the office_.
  - **{{Clean Desk Policy}}**: Securing _sensitive documents when_ unattended.
  - **{{Tailgating / Piggybacking}}**: Unauthorized _physical entry following_
    authorized users.
- **Reporting and monitoring**
  - **{{Initial}}**: Baseline _measurement of security_ awareness.
  - **{{Recurring}}**: Ongoing _assessment of training_ effectiveness.
- **{{Development}}**: Creating _training content relevant_ to roles.
- **{{Execution}}**: delivering _training to target_ audiences.
- **{{Gamification}}**: Using _game elements to enhance_ learning engagement.
- **{{Role-Based Training}}**: Customizing content _specific to job functions_.

## CompTIA Security+ SY0-701 Acronym List

The following is a list of acronyms that appears on the CompTIA Security+
SY0-701 exam. Candidates are encouraged to review the complete list and attain a
working knowledge of all listed acronyms as part of a comprehensive exam
preparation program.

ACRONYM DEFINITION

- **{{Two-Factor Authentication (2FA)}}**: Authentication requiring *two distinct forms of verification*.
- **{{Triple Data Encryption Standard (3DES)}}**: Legacy encryption *applying DES cipher three times*.
- **{{Authentication, Authorization, and Accounting (AAA)}}**: Framework for *controlling and tracking user access*.
- **{{Access Control List (ACL)}}**: Rules determining *permissions for users or systems*.
- **{{Advanced Encryption Standard (AES)}}**: Strong *symmetric block cipher for encryption*.
- **{{Advanced Encryption Standard 256-bit (AES-256)}}**: AES encryption *using a 256-bit key length*.
- **{{Authentication Header (AH)}}**: IPSec protocol *providing integrity and origin authentication*.
- **{{Artificial Intelligence (AI)}}**: Systems simulating *human intelligence for complex tasks*.
- **{{Automated Indicator Sharing (AIS)}}**: Exchange of *threat intelligence between organizations*.
- **{{Annualized Loss Expectancy (ALE)}}**: Estimated *yearly financial loss from a risk*.
- **{{Access Point (AP)}}**: Device *bridging wireless devices to wired network*.
- **{{Application Programming Interface (API)}}**: Interface allowing *software components to communicate*.
- **{{Advanced Persistent Threat (APT)}}**: Sophisticated attacker *maintaining long-term network access*.
- **{{Annualized Rate of Occurrence (ARO)}}**: Estimated *frequency of a threat happening per year*.
- **{{Address Resolution Protocol (ARP)}}**: Protocol *mapping IP addresses to MAC addresses*.
- **{{Address Space Layout Randomization (ASLR)}}**: Memory protection *randomizing data locations to prevent exploits*.
- **{{Adversarial Tactics, Techniques, and Common Knowledge (ATT&CK)}}**: Framework *describing cyber adversary behavior*.
- **{{Acceptable Use Policy (AUP)}}**: Rules *defining proper usage of organizational assets*.
- **{{Antivirus (AV)}}**: Software *preventing, detecting, and removing malware*.
- **{{Bourne Again Shell (BASH)}}**: Command-line *interface and scripting language for Linux*.
- **{{Business Continuity Planning (BCP)}}**: Strategy for *maintaining operations during disruptions*.
- **{{Border Gateway Protocol (BGP)}}**: Routing protocol *managing data packets between autonomous systems*.
- **{{Business Impact Analysis (BIA)}}**: Assessment of *consequences from disruption of business functions*.
- **{{Basic Input/Output System (BIOS)}}**: Firmware *initializing hardware during system boot*.
- **{{Business Partners Agreement (BPA)}}**: Contract *outlining responsibilities between business partners*.
- **{{Bridge Protocol Data Unit (BPDU)}}**: Messages *exchanged by switches to prevent loops*.
- **{{Bring Your Own Device (BYOD)}}**: Policy *allowing personal devices for work use*.
- **{{Certificate Authority (CA)}}**: Entity *issuing and verifying digital certificates*.
- **{{CAPTCHA}}**: Challenge-response *test distinguishing humans from bots*.
- **{{Corrective Action Report (CAR)}}**: Documentation of *steps taken to fix a defect*.
- **{{Cloud Access Security Broker (CASB)}}**: Security policy *enforcement point between cloud users and providers*.
- **{{Cipher Block Chaining (CBC)}}**: Encryption mode *chaining blocks using XOR*.
- **{{Counter Mode/CBC-MAC Protocol (CCMP)}}**: Encryption protocol *used in WPA2 wireless security*.
- **{{Closed-Circuit Television (CCTV)}}**: Video surveillance *system transmitting to limited monitors*.
- **{{Computer Emergency Response Team (CERT)}}**: Group *handling computer security incidents*.
- **{{Cipher Feedback (CFB)}}**: Stream cipher *mode using feedback for encryption*.
- **{{Challenge Handshake Authentication Protocol (CHAP)}}**: Protocol *authenticating via three-way handshake*.
- **{{Confidentiality, Integrity, Availability (CIA)}}**: The *triad of core information security principles*.
- **{{Chief Information Officer (CIO)}}**: Executive *responsible for IT strategy and implementation*.
- **{{Computer Incident Response Team (CIRT)}}**: Specialized group *responding to security breaches*.
- **{{Content Management System (CMS)}}**: Software *managing digital content creation and modification*.
- **{{Corporate-Owned, Business-Only (COBO)}}**: Mobile policy *restricting device use to work tasks*.
- **{{Continuity of Operation Planning (COOP)}}**: Plan *ensuring essential functions continue during emergencies*.
- **{{Corporate Owned, Personally Enabled (COPE)}}**: Mobile policy *allowing personal use of company devices*.
- **{{Contingency Planning (CP)}}**: Developing *strategies to recover from potential events*.
- **{{Cyclical Redundancy Check (CRC)}}**: Error-detecting *code verifying data integrity*.
- **{{Certificate Revocation List (CRL)}}**: List of *digital certificates invalidated before expiration*.
- **{{Chief Security Officer (CSO)}}**: Executive *responsible for physical and digital security*.
- **{{Cloud Service Provider (CSP)}}**: Company *offering cloud computing resources*.
- **{{Certificate Signing Request (CSR)}}**: Message *sent to CA to apply for certificate*.
- **{{Cross-Site Request Forgery (CSRF)}}**: Attack *forcing user to execute unwanted actions*.
- **{{Channel Service Unit (CSU)}}**: Device *connecting digital lines to network equipment*.
- **{{Counter Mode (CTM)}}**: Encryption mode *turning block cipher into stream cipher*.
- **{{Chief Technology Officer (CTO)}}**: Executive *overseeing technological needs and R&D*.
- **{{Common Vulnerability Enumeration (CVE)}}**: List of *publicly known cybersecurity vulnerabilities*.
- **{{Common Vulnerability Scoring System (CVSS)}}**: Framework *rating severity of security vulnerabilities*.
- **{{Choose Your Own Device (CYOD)}}**: Mobile policy *allowing selection from approved devices*.
- **{{Discretionary Access Control (DAC)}}**: Access control *where owners determine permissions*.
- **{{Database Administrator (DBA)}}**: Role *managing and maintaining database systems*.
- **{{Distributed Denial of Service (DDoS)}}**: Attack *overwhelming target from multiple sources*.
- **{{Data Execution Prevention (DEP)}}**: Security feature *preventing code execution in memory*.
- **{{Digital Encryption Standard (DES)}}**: Legacy *symmetric-key algorithm for data encryption*.
- **{{Dynamic Host Configuration Protocol (DHCP)}}**: Protocol *automating IP address assignment*.
- **{{Diffie-Hellman Ephemeral (DHE)}}**: Key exchange *providing forward secrecy using temporary keys*.
- **{{DomainKeys Identified Mail (DKIM)}}**: Email authentication *verifying sender identity via signature*.
- **{{Dynamic Link Library (DLL)}}**: Shared *library code used by multiple programs*.
- **{{Data Loss Prevention (DLP)}}**: Strategy *preventing unauthorized data exfiltration*.
- **{{Domain Message Authentication Reporting and Conformance (DMARC)}}**: Protocol *using SPF and DKIM to prevent spoofing*.
- **{{Destination Network Address Translation (DNAT)}}**: Translating *destination IP address of packets*.
- **{{Domain Name System (DNS)}}**: System *resolving hostnames to IP addresses*.
- **{{Domain Name System Security Extensions (DNSSEC)}}**: Suite *securing DNS against spoofing attacks*.
- **{{Denial of Service (DoS)}}**: Attack *making a resource unavailable to users*.
- **{{Data Privacy Officer (DPO)}}**: Role *ensuring compliance with data protection laws*.
- **{{Disaster Recovery Plan (DRP)}}**: Documented *process for restoring IT infrastructure*.
- **{{Digital Signature Algorithm (DSA)}}**: Standard *for creating digital signatures*.
- **{{Digital Subscriber Line (DSL)}}**: Internet connection *using telephone lines*.
- **{{Extensible Authentication Protocol (EAP)}}**: Framework *providing common authentication functions*.
- **{{Electronic Code Book (ECB)}}**: Encryption mode *dividing message into blocks*.
- **{{Elliptic Curve Cryptography (ECC)}}**: Public-key encryption *based on elliptic curve theory*.
- **{{Elliptic Curve Diffie-Hellman Ephemeral (ECDHE)}}**: Key exchange *using ECC and ephemeral keys*.
- **{{Elliptic Curve Digital Signature Algorithm (ECDSA)}}**: DSA variant *using elliptic curve cryptography*.
- **{{Endpoint Detection and Response (EDR)}}**: Tool *monitoring endpoints for threat detection*.
- **{{Encrypted File System (EFS)}}**: Windows feature *encrypting individual files*.
- **{{Enterprise Resource Planning (ERP)}}**: Software *managing core business processes*.
- **{{Electronic Serial Number (ESN)}}**: Unique *identifier for mobile devices*.
- **{{Encapsulated Security Payload (ESP)}}**: IPSec protocol *providing encryption and authentication*.
- **{{End User License Agreement (EULA)}}**: Legal contract *between software author and user*.
- **{{File System Access Control List (FACL)}}**: List *controlling access to file system objects*.
- **{{Full Disk Encryption (FDE)}}**: Encryption *protecting entire storage drive*.
- **{{File Integrity Management (FIM)}}**: Monitoring *system files for unauthorized changes*.
- **{{Field Programmable Gate Array (FPGA)}}**: Integrated circuit *configurable after manufacturing*.
- **{{False Rejection Rate (FRR)}}**: Rate *biometric system rejects authorized users*.
- **{{File Transfer Protocol (FTP)}}**: Standard protocol *for transferring files*.
- **{{Secured File Transfer Protocol (FTPS)}}**: FTP *secured with SSL/TLS encryption*.
- **{{Galois Counter Mode (GCM)}}**: High-performance *encryption mode providing integrity*.
- **{{General Data Protection Regulation (GDPR)}}**: EU law *on data protection and privacy*.
- **{{Gnu Privacy Guard (GPG)}}**: Encryption tool *implementing OpenPGP standard*.
- **{{Group Policy Object (GPO)}}**: Collection of *settings for Windows systems*.
- **{{Global Positioning System (GPS)}}**: Satellite-based *navigation system providing location*.
- **{{Graphics Processing Unit (GPU)}}**: Electronic circuit *designed to manipulate memory*.
- **{{Generic Routing Encapsulation (GRE)}}**: Tunneling protocol *encapsulating wide variety of protocols*.
- **{{High Availability (HA)}}**: System design *ensuring continuous operation*.
- **{{Hard Disk Drive (HDD)}}**: Magnetic *storage device using rotating platters*.
- **{{Host-based Intrusion Detection System (HIDS)}}**: System *monitoring host for suspicious activity*.
- **{{Host-based Intrusion Prevention System (HIPS)}}**: System *blocking malicious activity on host*.
- **{{Hashed Message Authentication Code (HMAC)}}**: Message authentication *using hash function and key*.
- **{{HMAC-based One-time Password (HOTP)}}**: Algorithm *generating passwords from hash*.
- **{{Hardware Security Module (HSM)}}**: Physical device *managing digital keys*.
- **{{Hypertext Markup Language (HTML)}}**: Standard markup *language for web pages*.
- **{{Hypertext Transfer Protocol (HTTP)}}**: Protocol for *transmitting hypermedia documents*.
- **{{Hypertext Transfer Protocol Secure (HTTPS)}}**: HTTP *secured via SSL/TLS encryption*.
- **{{Heating, Ventilation Air Conditioning (HVAC)}}**: Systems *regulating environmental conditions*.
- **{{Infrastructure as a Service (IaaS)}}**: Cloud model *providing virtualized computing resources*.
- **{{Infrastructure as Code (IaC)}}**: Managing *infrastructure through machine-readable files*.
- **{{Identity and Access Management (IAM)}}**: Framework *managing digital identities and access*.
- **{{Internet Control Message Protocol (ICMP)}}**: Protocol *sending error messages and operational info*.
- **{{Industrial Control Systems (ICS)}}**: Systems *monitoring and controlling industrial processes*.
- **{{International Data Encryption Algorithm (IDEA)}}**: Symmetric-key *block cipher used in PGP*.
- **{{Intermediate Distribution Frame (IDF)}}**: Cable rack *connecting internal wiring to MDF*.
- **{{Identity Provider (IdP)}}**: System *creating and managing identity information*.
- **{{Intrusion Detection System (IDS)}}**: Device *monitoring network for malicious activity*.
- **{{Institute of Electrical and Electronics Engineers (IEEE)}}**: Organization *developing technical standards*.
- **{{Internet Key Exchange (IKE)}}**: Protocol *setting up IPSec security associations*.
- **{{Instant Messaging (IM)}}**: Real-time *text transmission over internet*.
- **{{Internet Message Access Protocol (IMAP)}}**: Protocol *retrieving email from server*.
- **{{Indicators of Compromise (IoC)}}**: Artifacts *indicating a security breach*.
- **{{Internet of Things (IoT)}}**: Network of *interconnected physical devices*.
- **{{Internet Protocol (IP)}}**: Principal *communications protocol in internet suite*.
- **{{Intrusion Prevention System (IPS)}}**: Device *actively blocking network threats*.
- **{{Internet Protocol Security (IPSec)}}**: Suite *securing IP communications*.
- **{{Incident Response (IR)}}**: Approach *to managing security breach aftermath*.
- **{{Internet Relay Chat (IRC)}}**: Application layer *protocol for text communication*.
- **{{Incident Response Plan (IRP)}}**: Documented *procedures for handling security incidents*.
- **{{International Standards Organization (ISO)}}**: International *standard-setting body*.
- **{{Internet Service Provider (ISP)}}**: Company *providing internet access*.
- **{{Information Systems Security Officer (ISSO)}}**: Role *responsible for system security compliance*.
- **{{Initialization Vector (IV)}}**: Random number *used with key in encryption*.
- **{{Key Distribution Center (KDC)}}**: Trusted server *providing keys in Kerberos*.
- **{{Key Encryption Key (KEK)}}**: Key *used to encrypt other keys*.
- **{{Layer 2 Tunneling Protocol (L2TP)}}**: Tunneling protocol *supporting VPNs*.
- **{{Local Area Network (LAN)}}**: Network *connecting computers in limited area*.
- **{{Lightweight Directory Access Protocol (LDAP)}}**: Protocol *accessing directory information services*.
- **{{Lightweight Extensible Authentication Protocol (LEAP)}}**: Cisco *proprietary wireless authentication protocol*.
- **{{Monitoring as a Service (MaaS)}}**: Outsourced *security monitoring service*.
- **{{Mandatory Access Control (MAC)}}**: Access control *enforced by system policy*.
- **{{Media Access Control (MAC)}}**: Unique *identifier assigned to network interface*.
- **{{Message Authentication Code (MAC)}}**: Code *verifying message integrity and authenticity*.
- **{{Metropolitan Area Network (MAN)}}**: Network *spanning a city or campus*.
- **{{Master Boot Record (MBR)}}**: First sector *of storage device containing boot code*.
- **{{Message Digest 5 (MD5)}}**: Widely used *cryptographic hash function*.
- **{{Main Distribution Frame (MDF)}}**: Primary *hub for network cabling*.
- **{{Mobile Device Management (MDM)}}**: Administration *of mobile devices*.
- **{{Multifactor Authentication (MFA)}}**: Authentication *using two or more factors*.
- **{{Multifunction Device (MFD)}}**: Office machine *combining printing, scanning, copying*.
- **{{Multifunction Printer (MFP)}}**: Printer *with additional capabilities like scanning*.
- **{{Machine Learning (ML)}}**: AI subset *learning from data*.
- **{{Multimedia Message Service (MMS)}}**: Standard *sending multimedia content via mobile*.
- **{{Memorandum of Agreement (MOA)}}**: Document *describing cooperative relationship*.
- **{{Memorandum of Understanding (MOU)}}**: Agreement *expressing convergence of will*.
- **{{Multi-protocol Label Switching (MPLS)}}**: Mechanism *directing data via short path labels*.
- **{{Master Service Agreement (MSA)}}**: Contract *establishing terms for future transactions*.
- **{{Microsoft Challenge Handshake Authentication Protocol (MSCHAP)}}**: Microsoft's *version of CHAP authentication*.
- **{{Managed Service Provider (MSP)}}**: Company *managing IT services for clients*.
- **{{Managed Security Service Provider (MSSP)}}**: Company *managing security services for clients*.
- **{{Mean Time Between Failures (MTBF)}}**: Average *time between system breakdowns*.
- **{{Mean Time to Failure (MTTF)}}**: Expected *time until non-repairable failure*.
- **{{Mean Time to Recover (MTTR)}}**: Average *time to repair a failed component*.
- **{{Maximum Transmission Unit (MTU)}}**: Size of *largest protocol data unit*.
- **{{Mail Exchange (MX)}}**: DNS record *identifying mail servers for domain*.
- **{{Network Access Control (NAC)}}**: Security *enforcing policy on devices accessing network*.
- **{{Network Address Translation (NAT)}}**: Mapping *IP addresses between different networks*.
- **{{Non-Disclosure Agreement (NDA)}}**: Contract *protecting confidential information from disclosure*.
- **{{Near Field Communication (NFC)}}**: Short-range *wireless communication technology*.
- **{{Next-Generation Firewall (NGFW)}}**: Firewall *combining traditional filtering with DPI*.
- **{{Network-based Intrusion Detection System (NIDS)}}**: System *monitoring network traffic for threats*.
- **{{Network-based Intrusion Prevention System (NIPS)}}**: Device *blocking malicious network traffic*.
- **{{National Institute of Standards & Technology (NIST)}}**: US agency *developing technology standards*.
- **{{New Technology File System (NTFS)}}**: Proprietary *file system developed by Microsoft*.
- **{{New Technology LAN Manager (NTLM)}}**: Suite of *Microsoft security protocols*.
- **{{Network Time Protocol (NTP)}}**: Protocol *synchronizing clocks over packet networks*.
- **{{Open Authorization (OAUTH)}}**: Standard *for access delegation*.
- **{{Online Certificate Status Protocol (OCSP)}}**: Protocol *checking digital certificate revocation status*.
- **{{Object Identifier (OID)}}**: Unique *identifier for object in hierarchy*.
- **{{Operating System (OS)}}**: System *software managing computer hardware*.
- **{{Open-source Intelligence (OSINT)}}**: Intelligence *gathered from publicly available sources*.
- **{{Open Shortest Path First (OSPF)}}**: Link-state *routing protocol for IP networks*.
- **{{Operational Technology (OT)}}**: Hardware/software *controlling industrial equipment*.
- **{{Over the Air (OTA)}}**: Wireless *transmission of data or software*.
- **{{Open Vulnerability Assessment Language (OVAL)}}**: Standard *for assessing system security state*.
- **{{Open Worldwide Application Security Project (OWASP)}}**: Community *focused on improving software security*.
- **{{PKCS #12 (P12)}}**: Archive file *format storing cryptography objects*.
- **{{Peer to Peer (P2P)}}**: Decentralized *network architecture sharing resources*.
- **{{Platform as a Service (PaaS)}}**: Cloud *providing development and deployment environments*.
- **{{Proxy Auto Configuration (PAC)}}**: File *defining how browsers choose proxy*.
- **{{Privileged Access Management (PAM)}}**: System *securing elevated access accounts*.
- **{{Pluggable Authentication Modules (PAM)}}**: Mechanism *integrating low-level authentication schemes*.
- **{{Password Authentication Protocol (PAP)}}**: Simple *authentication protocol sending cleartext passwords*.
- **{{Port Address Translation (PAT)}}**: NAT *mapping multiple private IPs to one public*.
- **{{Password-Based Key Derivation Function 2 (PBKDF2)}}**: Function *strengthening passwords against brute force*.
- **{{Private Branch Exchange (PBX)}}**: Telephone *system within an enterprise*.
- **{{Packet Capture (PCAP)}}**: File format *storing captured network traffic*.
- **{{Payment Card Industry Data Security Standard (PCI DSS)}}**: Standard *securing credit card transactions*.
- **{{Power Distribution Unit (PDU)}}**: Device *distributing electric power to racks*.
- **{{Protected Extensible Authentication Protocol (PEAP)}}**: EAP *encapsulated within TLS tunnel*.
- **{{Personal Electronic Device (PED)}}**: Consumer *device capable of communication*.
- **{{Privacy Enhanced Mail (PEM)}}**: File format *storing cryptographic keys/certificates*.
- **{{Perfect Forward Secrecy (PFS)}}**: Property *preventing compromise of past sessions*.
- **{{Pretty Good Privacy (PGP)}}**: Encryption *program providing privacy and authentication*.
- **{{Personal Health Information (PHI)}}**: Data *relating to health status or care*.
- **{{Personally Identifiable Information (PII)}}**: Data *identifying a specific individual*.
- **{{Personal Identity Verification (PIV)}}**: Standard *for federal employee identification*.
- **{{Public Key Cryptography Standards (PKCS)}}**: Standards *for public-key cryptography*.
- **{{Public Key Infrastructure (PKI)}}**: Framework *managing digital keys and certificates*.
- **{{Post Office Protocol (POP)}}**: Protocol *retrieving email from server*.
- **{{Plain Old Telephone Service (POTS)}}**: Traditional *analog voice transmission telephone system*.
- **{{Point-to-Point Protocol (PPP)}}**: Protocol *establishing direct connection between nodes*.
- **{{Point-to-Point Tunneling Protocol (PPTP)}}**: Obsolete *method for implementing VPNs*.
- **{{Pre-Shared Key (PSK)}}**: Secret *shared between parties before communication*.
- **{{Pan-Tilt-Zoom (PTZ)}}**: Camera *capable of remote directional control*.
- **{{Potentially Unwanted Program (PUP)}}**: Software *installed without clear user consent*.
- **{{Recovery Agent (RA)}}**: Entity *authorized to recover encrypted data*.
- **{{Registration Authority (RA)}}**: Entity *verifying identity for certificate issuance*.
- **{{Research and Development in Advanced Communications Technologies in Europe (RACE)}}**: Project *developing digital communication*.
- **{{Rapid Application Development (RAD)}}**: Methodology *prioritizing rapid prototyping*.
- **{{Remote Authentication Dial-in User Service (RADIUS)}}**: Protocol *providing centralized AAA management*.
- **{{Redundant Array of Inexpensive Disks (RAID)}}**: Data storage *virtualization technology*.
- **{{Remote Access Server (RAS)}}**: Server *enabling remote connection to network*.
- **{{Remote Access Trojan (RAT)}}**: Malware *allowing covert remote control*.
- **{{Role-Based Access Control (RBAC)}}**: Access *based on user roles*.
- **{{Rule-Based Access Control (RBAC)}}**: Access *determined by predefined rules*.
- **{{Rivest Cipher Version 4 (RC4)}}**: Legacy *stream cipher (now insecure)*.
- **{{Remote Desktop Protocol (RDP)}}**: Protocol *providing graphical remote access*.
- **{{Radio Frequency Identification (RFID)}}**: Technology *identifying objects via radio waves*.
- **{{RACE Integrity Primitives Evaluation Message Digest (RIPEMD)}}**: Family *of cryptographic hash functions*.
- **{{Return on Investment (ROI)}}**: Metric *evaluating profitability of investment*.
- **{{Recovery Point Objective (RPO)}}**: Maximum *acceptable data loss period*.
- **{{Rivest, Shamir, & Adleman (RSA)}}**: Public-key *cryptosystem for secure transmission*.
- **{{Remotely Triggered Black Hole (RTBH)}}**: Technique *dropping undesirable traffic at edge*.
- **{{Recovery Time Objective (RTO)}}**: Target *time to restore service after failure*.
- **{{Real-Time Operating System (RTOS)}}**: OS *processing data as it comes in*.
- **{{Real-Time Transport Protocol (RTP)}}**: Protocol *delivering audio and video over IP*.
- **{{Secure/Multipurpose Internet Mail Extensions (S/MIME)}}**: Standard *for public key encryption and signing* of MIME data.
- **{{Software as a Service (SaaS)}}**: Cloud *model hosting applications for customers*.
- **{{Simultaneous Authentication of Equals (SAE)}}**: Key exchange *protocol in WPA3 preventing offline* attacks.
- **{{Security Assertions Markup Language (SAML)}}**: XML-based *standard for exchanging authentication data*.
- **{{Storage Area Network (SAN)}}**: Dedicated *high-speed network connecting storage devices*.
- **{{Subject Alternative Name (SAN)}}**: Extension *allowing multiple hostnames in SSL* certificates.
- **{{Secure Access Service Edge (SASE)}}**: Framework *converging networking and security services*.
- **{{Supervisory Control and Data Acquisition (SCADA)}}**: Industrial *control systems monitoring infrastructure*.
- **{{Security Content Automation Protocol (SCAP)}}**: Standard *automating vulnerability management and compliance*.
- **{{Simple Certificate Enrollment Protocol (SCEP)}}**: Protocol *simplifying distribution of digital certificates*.
- **{{Software-Defined Wide Area Network (SD-WAN)}}**: Virtual *WAN architecture allowing diverse transport* usage.
- **{{Software Development Kit (SDK)}}**: Collection *of tools for building software applications*.
- **{{Software Development Lifecycle (SDLC)}}**: Process *planning, creating, testing, and deploying* software.
- **{{Software Development Lifecycle Methodology (SDLM)}}**: Framework *structuring steps in software creation*.
- **{{Software-Defined Networking (SDN)}}**: Architecture *separating network control and forwarding*.
- **{{Security-Enhanced Linux (SELinux)}}**: Linux *feature supporting access control policies*.
- **{{Self-Encrypting Drives (SED)}}**: Storage *device encrypting data via hardware*.
- **{{Structured Exception Handler (SEH)}}**: Mechanism *handling both hardware and software exceptions*.
- **{{Secured File Transfer Protocol (SFTP)}}**: Secure *version of FTP using SSH*.
- **{{Secure Hashing Algorithm (SHA)}}**: Family *of cryptographic hash functions*.
- **{{Secure Hypertext Transfer Protocol (SHTTP)}}**: Obsolete *protocol for encrypting web traffic*.
- **{{Security Information and Event Management (SIEM)}}**: Solution *aggregating and analyzing security data*.
- **{{Subscriber Identity Module (SIM)}}**: Smart *card storing subscriber information for mobile*.
- **{{Service-Level Agreement (SLA)}}**: Contract *defining expected service standards*.
- **{{Single Loss Expectancy (SLE)}}**: Monetary *value lost from a single risk* event.
- **{{Server Message Block (SMB)}}**: Protocol *sharing files and printers on networks*.
- **{{Short Message Service (SMS)}}**: Protocol *sending text messages over cellular* networks.
- **{{Simple Mail Transfer Protocol (SMTP)}}**: Standard *protocol for sending email*.
- **{{Simple Mail Transfer Protocol Secure (SMTPS)}}**: Secure *email transmission using TLS*.
- **{{Simple Network Management Protocol (SNMP)}}**: Protocol *monitoring and managing network devices*.
- **{{Simple Object Access Protocol (SOAP)}}**: Messaging *protocol for exchanging structured information*.
- **{{Security Orchestration, Automation, Response (SOAR)}}**: Stack *automating security operations and incident* response.
- **{{System on Chip (SoC)}}**: Integrated *circuit containing all computer components*.
- **{{Security Operations Center (SOC)}}**: Facility *housing teams monitoring security posture*.
- **{{Statement of Work (SOW)}}**: Document *defining project scope and deliverables*.
- **{{Sender Policy Framework (SPF)}}**: Email *authentication method detecting forged sender* addresses.
- **{{Spam over Internet Messaging (SPIM)}}**: Unsolicited *messages sent over instant messaging*.
- **{{Structured Query Language (SQL)}}**: Language *managing data in relational databases*.
- **{{SQL Injection (SQLi)}}**: Attack *inserting malicious code into database* queries.
- **{{Secure Real-Time Protocol (SRTP)}}**: Protocol *providing encryption and authentication for RTP*.
- **{{Solid State Drive (SSD)}}**: Storage *device using flash memory*.
- **{{Secure Shell (SSH)}}**: Protocol *for secure remote login*.
- **{{Secure Sockets Layer (SSL)}}**: Legacy *protocol for establishing encrypted links*.
- **{{Single Sign-On (SSO)}}**: Authentication *enabling one login for multiple* systems.
- **{{Structured Threat Information eXchange (STIX)}}**: Language *describing cyber threat information*.
- **{{Secure Web Gateway (SWG)}}**: Solution *filtering web traffic to block* threats.
- **{{Terminal Access Controller Access Control System (TACACS+)}}**: Protocol *handling remote authentication and services*.
- **{{Trusted Automated eXchange of Indicator Information (TAXII)}}**: Protocol *transporting threat information via HTTPS*.
- **{{Transmission Control Protocol / Internet Protocol (TCP/IP)}}**: Conceptual *model and protocols for internet*.
- **{{Ticket Granting Ticket (TGT)}}**: User *authentication token in Kerberos protocol*.
- **{{Temporal Key Integrity Protocol (TKIP)}}**: Legacy *encryption protocol for wireless networks*.
- **{{Transport Layer Security (TLS)}}**: Cryptographic *protocol securing internet communications*.
- **{{Time-of-Check (TOC)}}**: Moment *system verifies resource access rights*.
- **{{Time-Based One-Time Password (TOTP)}}**: Algorithm *generating passwords using current time*.
- **{{Time-of-Use (TOU)}}**: Moment *system resource is actually utilized*.
- **{{Trusted Platform Module (TPM)}}**: Chip *securing hardware via cryptographic keys*.
- **{{Tactics, Techniques, and Procedures (TTP)}}**: Patterns *of activities associated with threat* actors.
- **{{Transaction Signature (TSIG)}}**: Mechanism *authenticating DNS updates via shared* keys.
- **{{User Acceptance Testing (UAT)}}**: Phase *verifying solution meets user requirements*.
- **{{Unmanned Aerial Vehicle (UAV)}}**: Aircraft *operated without a human pilot*.
- **{{User Behavior Analytics (UBA)}}**: Process *detecting anomalies in user activity*.
- **{{User Datagram Protocol (UDP)}}**: Communication *protocol used for low-latency loss-tolerating* connections.
- **{{Unified Extensible Firmware Interface (UEFI)}}**: Standard *firmware interface for PCs*.
- **{{Unified Endpoint Management (UEM)}}**: Architecture *managing all endpoint devices centrally*.
- **{{Uninterruptible Power Supply (UPS)}}**: Battery *backup providing emergency power*.
- **{{Uniform Resource Identifier (URI)}}**: String *identifying a resource on internet*.
- **{{Uniform Resource Locator (URL)}}**: Reference *specifying resource location on network*.
- **{{Universal Serial Bus (USB)}}**: Interface *standard for connecting peripherals*.
- **{{USB On-The-Go (USB OTG)}}**: Standard *allowing devices to act as hosts*.
- **{{Unified Threat Management (UTM)}}**: Solution *consolidating multiple security functions*.
- **{{Unshielded Twisted Pair (UTP)}}**: Common *network cable without EMI shielding*.
- **{{Visual Basic (VBA)}}**: Programming *language for Office applications*.
- **{{Virtual Desktop Environment (VDE)}}**: Technology *hosting desktop environment on server*.
- **{{Virtual Desktop Infrastructure (VDI)}}**: Technology *hosting desktop OS on virtual machines*.
- **{{Virtual Local Area Network (VLAN)}}**: Logic *network partition at Layer 2*.
- **{{Variable Length Subnet Masking (VLSM)}}**: Technique *optimizing IP address allocation*.
- **{{Virtual Machine (VM)}}**: Emulation *of a computer system*.
- **{{Voice over IP (VoIP)}}**: Delivery *of voice communications over IP*.
- **{{Virtual Private Cloud (VPC)}}**: Isolated *cloud computing environment*.
- **{{Virtual Private Network (VPN)}}**: Encrypted *connection over a public network*.
- **{{Video Teleconferencing (VTC)}}**: Technology *facilitating video and audio communication*.
- **{{Web Application Firewall (WAF)}}**: Firewall *monitoring and blocking HTTP traffic*.
- **{{Wireless Access Point (WAP)}}**: Device *connecting wireless devices to wired* network.
- **{{Wired Equivalent Privacy (WEP)}}**: Deprecated *wireless security algorithm*.
- **{{Wireless Intrusion Detection System (WIDS)}}**: System *monitoring wireless spectrum for attacks*.
- **{{Wireless Intrusion Prevention System (WIPS)}}**: System *automatically mitigating wireless threats*.
- **{{Work Order (WO)}}**: Document *authorizing specific work tasks*.
- **{{Wi-Fi Protected Access (WPA)}}**: Security *certification program for wireless networks*.
- **{{Wi-Fi Protected Setup (WPS)}}**: Standard *for easy wireless network setup*.
- **{{Wireless TLS (WTLS)}}**: Security *layer for WAP applications*.
- **{{Extended Detection and Response (XDR)}}**: Solution *collecting and correlating data across* layers.
- **{{Extensible Markup Language (XML)}}**: Markup *language defining set of rules*.
- **{{Exclusive Or (XOR)}}**: Logical *operation used in cryptography*.
- **{{Cross-Site Request Forgery (XSRF)}}**: Attack *tricking user into executing actions*.
- **{{Cross-Site Scripting (XSS)}}**: Attack *injecting malicious scripts into websites*.

## CompTIA Security+ SY0-701 Hardware and Software List

CompTIA has included this sample list of hardware and software to assist
candidates as they prepare for the Security+ SY0-701 certification exam. This
list may also be helpful for training companies that wish to create a lab
component for their training offering. The bulleted lists below each topic are
sample lists and are not exhaustive.

EQUIPMENT

- Tablet
- Laptop
- Web server
- Firewall
- Router
- Switch
- IDS
- IPS
- Wireless access point
- Virtual machines
- Email system
- Internet access
- DNS server
- IoT devices
- Hardware tokens
- Smartphone

SPARE PARTS/HARDWARE

- NICs
- Power supplies
- GBICs
- SFPs
- Managed Switch
- Wireless access point
- UPS

TOOLS

- Wi-Fi analyzer
- Network mapper
- NetFlow analyzer

SOFTWARE

- Windows OS
- Linux OS
- Kali Linux
- Packet capture software
- Pen testing software
- Static and dynamic analysis tools
- Vulnerability scanner
- Network emulators
- Sample code
- Code editor
- SIEM
- Keyloggers
- MDM software
- VPN
- DHCP service
- DNS service

OTHER

- Access to cloud environments
- Sample network documentation/diagrams
- Sample logs
