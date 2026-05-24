Linux+
CERTIFICATION

Plus Series

CompTIA Linux+
Certification
Exam Objectives
EXAM NUMBER: XK0-006 V8

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

About the Exam
The CompTIA Linux+ certification exam will certify the successful candidate has the knowledge and skills required
to configure, manage, operate, and troubleshoot Linux server environments while using security best practices,
scripting, containerization, virtualization, and automation.
This is equivalent to 12 months of hands-on experience working with Linux servers. Certifications in and/or
knowledge about A+, Network+, Server+ are recommended.
These content examples are meant to clarify the test objectives and should not be construed as a comprehensive
listing of all the content of this examination.
EXAM ACCREDITATION
The CompTIA Linux+ exam is accredited by ANSI to show compliance with the ISO 17024 standard and, as such,
undergoes regular reviews and updates to the exam objectives.
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
exam. Candidates will be required to abide by the CompTIA Candidate Agreement. If a candidate has a question as
to whether study materials are considered unauthorized (aka “brain dumps”), he/she should contact CompTIA at
examsecurity@comptia.org to confirm.
PLEASE NOTE
The lists of examples provided in bulleted format are not exhaustive lists. Other examples of technologies, processes,
or tasks pertaining to each objective may also be included on the exam, although not listed or covered in this
objectives document. CompTIA is constantly reviewing the content of our exams and updating test questions to be
sure our exams are current, and the security of the questions is protected. When necessary, we will publish updated
exams based on existing exam objectives. Please know that all related exam preparation materials will still be valid.

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

TEST DETAILS
Required exam

XK0-006

Number of questions

Maximum of 90

Types of questions

Multiple-choice and performance-based

Length of test

90 minutes

Recommended experience

12 months of hands-on experience working with Linux servers; A+, Network+,
Server+, or similar certifications and/or knowledge recommended

EXAM OBJECTIVES (DOMAINS)
The table below lists the domains measured by this examination and the extent to which they are represented.
DOMAIN
1.0
2.0
3.0
4.0
5.0

PERCENTAGE OF EXAMINATION

System Management					
Services and User Management				
Security							
Automation, Orchestration, and Scripting 			
Troubleshooting						

Total

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

23%
20%
18%
17%
22%
100%

1.0 System Management
1.1

Explain basic Linux concepts.
• Basic boot process
− Bootloader
գ Configuration files
− Kernel
գ Parameters
− Initial RAM [random-access memory] disk (initrd)
− Preboot Execution Environment (PXE)
• Filesystem Hierarchy Standard (FHS)
−/
− /bin
− /boot
− /dev
− /etc
− /home
− /lib
− /proc
− /sbin
− /tmp
− /usr
− /var
• Server architectures
− AArch64
− Reduced instruction set computer, version five (RISC-V)
− x86
− x86_64/AMD64
• Distributions
− RPM Package Manager (RPM)-based
− Debian packet manager (dpkg)-based
• Graphical User Interface (GUI)
− Display managers
− Window managers
− X Server
− Wayland
• Software licensing
− Opensource software
− Free software
− Proprietary software
− Copyleft

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

1.0 | System Management

1.2

1.3

Summarize Linux device management concepts and tools.
• Kernel modules
− depmod
− insmod
− lsmod
− modinfo
− modprobe
− rmmod

− ipmitool
− lm_sensors
− lscpu
− lshw
− lsmem
− lspci
− lsusb

• Device management
− dmesg
− dmidecode

• initrd management
− dracut
− mkinitrd

• Custom hardware
− Embedded systems
− Graphics Processing Unit
(GPU) use cases
գ nvtop

Given a scenario, manage storage in a Linux system.
• Logical Volume Manager (LVM)
− Logical volume
գ lvchange
գ lvcreate
գ lvdisplay
գ lvremove
գ lvresize/lvextend
գ lvs
• Volume group
− vgchange
− vgcreate
− vgdisplay
− vgexport
− vgextend
− vgimport
− vgremove
− vgs
− vgscan
• Physical volume
− pvcreate
− pvdisplay
− pvmove
− pvremove
− pvresize
− pvs
− pvscan
• Partitions
− blkid
− fdisk/gdisk
− growpart
− lsblk
− parted

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

• Filesystems
− Formats
գ xfs
գ ext4
գ btrfs
գ tmpfs
• Utilities
− df
− du
− fio
− fsck
− mkfs
− resize2fs
− xfs_growfs
− xfs_repair
• Redundant Array of
Independent Disks (RAID)
− /proc/mdstat
− mdadm
• Mounted storage
− Mounting
գ /etc/fstab
գ /etc/mtab
գ /proc/mounts
գ autofs
գ mount
գ umount
− Mount options
գ noatime
գ nodev
գ nodiratime
գ noexec

գ nofail
գ nosuid
գ remount
գ ro
գ rw
− Network mounts
գ Network file system (NFS)
գ Server Message Block
(SMB) Samba
• Inodes

1.0 | System Management

1.4

Given a scenario, manage network services and configurations on a Linux server.
• Common network tools
− arp
− curl
− dig
− ethtool
− hostname
− ip
գ ip address
գ ip link
գ ip route
− iperf3
− mtr
− nc
− nmap
− nslookup
− ping/ping6
− ss
− tcpdump
− tracepath
− traceroute

• Network configuration
− /etc/hosts
− /etc/resolv.conf
− /etc/nsswitch.conf
• NetworkManager
− nmcli
− nmconnect
• Netplan
− netplan apply
− netplan status
− netplan try
գ Configuration files
ը /etc/netplan

1.5

Given a scenario, manage a Linux system using common shell operations.
• Common environmental variables
− DISPLAY
− HOME
− PATH
− PS1
− SHELL
− USER
• Paths
− Absolute
գ ~
գ /
• Relative
−.
− ..
−• Shell environment configurations
− .bashrc
− .bash_profile
− .profile

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

• Channel redirection
−<
−>
− <<
− >>
−|
− Standard output
− Standard error
− Standard input
− Here docs
գ <<<
• Basic shell utilities
−!
− !!
− alias
− awk
− bc
− cat
− cut
− echo
− grep

− head
− history
− less
− more
− printf
− sed
− sort
− source
− tail
− tee
− tr
− uname
− uniq
− wc
− xargs
• Text editors
− vi/vim
− nano

1.0 | System Management

1.6

Given a scenario, perform backup and restore operations for a Linux server.
• Archiving
− cpio
− tar
• Compression tools
− 7-Zip
− bzip2
− gzip
− unzip
− xz

1.7

• Other tools
− dd
− ddrescue
− rsync
− zcat
− zgrep
− zless

Summarize virtualization on Linux systems.
• Linux hypervisors
− Quick Emulator (QEMU)
− Kernel-based Virtual Machine (KVM)
• Virtual machines (VMs)
− Paravirtualized drivers
− VirtIO
− Disk image operations
գ Convert
գ Resize
գ Image properties
− VM states
− Nested virtualization
• VM operations
− Resources
գ Storage
գ RAM
գ Central processing unit (CPU)
գ Network
− Baseline image templates
− Cloning
− Migrations
− Snapshots
• Bare metal vs. virtual machines
• Network types
− Bridged
− Network address translation (NAT)
− Host-only/isolated
− Routed
− Open
• Virtual machine tools
− libvirt
− virsh
− vit-manager

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

2.0 Services and User Management
2.1

Given a scenario, manage files and directories on a Linux system.
• Utilities
− cd
− cp
− diff
− file
− find
− ln
− locate
− ls
− lsof
− mkdir
− mv
− pwd
− rm
− rmdir
− sdiff
− stat
− touch

2.2

• Links
− Symbolic link
− Hard link
• Device types in /dev
− Block devices
− Character devices
− Special character devices

Given a scenario, perform local account management in a Linux environment.
• Add
− adduser
− groupadd
− useradd
• Delete
− deluser
− groupdel
− userdel
• Modify
− chsh
− groupmod
− passwd
− usermod
• Lock
− chage
− passwd
− usermod
• Expiration
− Configuration files
− chage

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

• List
− getent passwd
− groups
− id
− last
− lastlog
−w
− who
− whoami
• User profile templates
− /etc/profile
− /etc/skel
• Account files
− /etc/group
− /etc/passwd
− /etc/shadow
• Attributes
− Unique Identifier (UID)
− Group Identifier (GID)
− Effective User Identifier (EUID)
− Effective Group Identifier (EGID)

• User accounts vs. system
accounts vs. service accounts
− UID range

2.0 | Services and User Management

2.3

Given a scenario, manage processes and jobs in a Linux environment.
• Process verification
− /proc/<PID>
− atop
− htop
− lsof
− mpstat
− pidstat
− ps
− pstree
− strace
− top
• Process ID
− Parent Process Identification
Number (PPID)
− Process Identification Number (PID)

2.4

• Priority
− nice
− renice
• Process limits
• Job and process management
−&
− bg
− Ctrl + c
− Ctrl + d

− Ctrl + z
− exec
− fg
− jobs
− kill
− killall
− nohup
− pkill
− Signals
գ 1 HUP
գ 9 KILL
գ 15 TERM
• Scheduling
− anacron
− at
− crontab

Given a scenario, configure and manage software in a Linux environment.
• Installation, update, and removal
− Repository
− Source
− Package dependencies and conflicts
− Package managers
− Language-specific
գ pip
գ cargo
գ npm
• Repository management
− Enabling/disabling
− Third party

2.5

• Process states
− Running
− Blocked
− Sleeping
− Stopped
− Zombie

− Gnu’s Not Unix (GNU) Privacy
Guard (GPG) signatures
• Package and repository exclusions
• Update alternatives
• Software configuration
• Sandboxed applications
• Basic configurations of
common services
− Domain Name System
(DNS) protocol
− Network Time Protocol (NTP)/
Precision Time Protocol (PTP)

Given a scenario, manage Linux using systemd.
• Systemd units
− Services
− Timers
− Mounts
− Targets
• Utilities
− hostnamectl
− resolvectl
− sysctl
− systemctl
− systemd-analyze
− systemd-blame
− systemd-resolved
− timedatectl

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

• Managing unit states
− daemon-reload
− disable
− edit
− enable
− mask
− reload
− restart
− start
− status
− stop
− unmask

− Dynamic Host Configuration
Protocol (DHCP)
− HyperText Transfer Protocol (HTTP)
գ Apache HTTP Server (httpd)
գ Nginx
− Simple Mail Transfer
Protocol (SMTP)
− Internet Messaging Access
Protocol (IMAP4)

2.0 | Services and User Management

2.6

Given a scenario, manage applications in a container on a Linux server.
• Runtimes
− runC
− Podman
− containerd
− Docker
• Image operations
− Pulling images
− Build an image
գ Dockerfile
ը ENTRYPOINT
ը CMD
ը USER
ը FROM
− Pruning
− Tags
− Layers
• Container operations
− Read container logs
− Map container volumes
− Start/stop containers
− Inspect containers
− Delete a container
− Run
− Exec
− Pruning
− Tags
− Environmental variables
• Volume operations
− Create volume
− Mapping volume
− Pruning
− SELinux context
− Overlay
• Container networks
− Create network
− Port mapping
− Pruning
− Types
գ macvlan
գ ipvlan
գ Host
գ Bridge
գ Overlay
գ None
• Privileged vs. unprivileged

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

3.0 Security
3.1

Summarize authorization, authentication, and accounting methods.
• Polkit
• Pluggable Authentication
Modules (PAM)
• System Security
Services Daemon
(SSSD)/Winbind realm

3.2

• Lightweight Directory
Access Protocol (LDAP)
• Kerberos
• Samba

Given a scenario, configure and implement firewalls on a Linux system.
• firewalld
− firewall-cmd
− Runtime vs. permanent
− Rich rules
− Zones
− Ports vs. services
• Uncomplicated Firewall (ufw)
− Ports vs. services

3.3

• System audit
− audit.rules
− auditd

• Logging
− journalctl
− rsyslog
− logrotate
− /var/log

բ nftables
բ iptables
բ ipset

Translation (DNAT)
− Source Network Address
Translation (SNAT)

• Netfilter module
• Address translation
− NAT
− Port Address Translation (PAT)
− Destination Network Address

• Stateful vs. stateless
• Internet rotocol (IP) forwarding
− net.ipv4.ip_forward

Given a scenario, apply operating system (OS) hardening techniques on a Linux system.
• Privilege escalation
− sudo
գ /etc/sudoers
ը NOEXEC
ը NOPASSWD
implications
գ /etc/sudoers.d
գ visudo
գ sudo -i
գ wheel group
գ sudo group
− su • File attributes
− chattr
− lsattr
գ immutable
գ append only
• Permissions
− File permissions
գ chgrp

գ chmod
ը Octal
ը Symbolic
գ chown
− Special permissions
գ Sticky bit
գ setuid
գ setgid
− Default user file-creation
mode mask (umask)
• Access control
− Access control
lists (ACLs)
գ setfacl
գ getfacl
− SELinux
գ restorecon
գ semanage
գ chcon
գ ls -Z
գ getenforce
գ setenforce

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

գ getsebool
գ setsebool
գ audit2allow
գ sealert
գ States
ը Enforcing
ը Permissive
ը Disabled
• Secure remote access
− Secure Shell
daemon (SSHD)
գ Key vs. password
authentication
գ Secure Shell
(SSH) tunneling
գ PermitRootLogin
գ Disabling X forwarding
գ AllowUsers
գ AllowGroups
− SSH agent
− Secure File Transfer
Protocol (SFTP)

գ chroot
− fail2ban
• Avoid the use of
unsecure access services
− Telnet
− File Transfer
Protocol (FTP)
− Trivial File Transfer
Protocol (TFTP)
• Disabling unused
file systems
• Removal of unnecessary
Set User ID (SUID)
permissions
• Secure boot
− Unified Extensible
Firmware Interface (UEFI)

3.0 | Security

3.4

Explain account hardening techniques and best practices.
• Passwords
− Complexity
− Length
− Expiration
− Reuse
− History

3.5

• pam_tally2
• Avoid running as root

Explain cryptographic concepts and technologies in a Linux environment.
• Data at rest
− File encryption
գ GPG
− Filesystem encryption
գ Linux Unified Key
Setup 2 (LUKS2)
գ Argon2
• Data in transit
− Open Secure Sockets
Layer (OpenSSL)
− WireGuard
− LibreSSL
− Transport Layer Security
(TLS) protocol versions

3.6

• Multifactor authentication (MFA)
• Checking existing breach lists
• Restricted shells
− /sbin/nologin
− /bin/rbash

• Hashing
− SHA-256
− Hashed message authentication
code (HMAC)
• Removal of weak algorithms
• Certificate management
− Trusted root certificates
գ No-cost
գ Commercial
• Avoiding self-signed certificates

Explain the importance of compliance and audit procedures.
• Detection and response
− Anti-malware
− Indicators of compromise (IOC)
• Vulnerability scanning
− Common Vulnerabilities
and Exposures (CVEs)
− Common Vulnerability
Scoring System (CVSS)
− Backporting patches
− Service misconfigurations
− Tools
գ Port scanners
գ Protocol analyzer
• Standards and audit
− Open Security Content Automation
Protocol (OpenSCAP)
− Center for Internet Security
(CIS) Benchmarks

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

• File integrity
− Advanced Intrusion Detection
Environment (AIDE)
− Rootkit hunter (rkhunter)
− Signed package verification
− Installed file verification
• Secure data destruction
− shred
− badblocks -w
− dd if=/dev/urandom
− Cryptographic destruction
• Software supply chain
• Security banners
− /etc/issue
− /etc/issue.net
− /etc/motd

4.0 Automation, Orchestration, and Scripting
4.1

Summarize the use cases and techniques of automation and orchestration in a Linux
environment.
• Infrastructure as code
− Ansible
գ Playbooks
գ Inventory
գ Modules
գ Ad hoc
գ Collections
գ Facts
գ Agentless
− Puppet
գ Classes
գ Certificates
գ Modules
գ Facts
գ Agent/Agentless
− OpenTofu
գ Provider
գ Resource

4.2

գ State
գ Application programming
interface (API)
• Unattended deployment
− Kickstart
− Cloud-init
• Continuous integration/
Continuous deployment (CI/CD)
− Version control
− Shift left testing
− GitOps
− Pipelines
− DevSecOps
• Deployment orchestration
− Kubernetes
գ ConfigMaps

գ Secrets
գ Pods
գ Deployments
գ Volumes
գ Services
գ Variables
− Docker Swarm
գ Service
գ Nodes
գ Tasks
գ Networks
գ Scale
− Docker/Podman Compose
գ Compose file
գ Up/down
գ Logs

Given a scenario, perform automated tasks using shell scripting.
• Expansion
− Parameter expansion
գ ${var}
− Command substitution
գ $(foo)
գ `foo`
− Subshell
գ (foo)
• Functions
• Internal Field Separator/Output
Field Separator (IFS/OFS)
• Conditional statements
− if
− case
• Looping statements
− until
− for
− while
• Interpreter directive
− #!

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

• Comparisons
− Numerical
գ -eq
գ -ge
գ -gt
գ -le
գ -lt
գ -ne
− String
գ >
գ <
գ ==
գ =
գ = ~
գ ! =
գ <=
գ >=
• Regular expressions
− [[ $foo =~ regex ]]
• Test
−!
− -d

− -f
− -n
− -z
• Variables
− Environmental
− Arguments
− Assignments
գ alias
գ export
գ local
գ set
գ unalias
գ unset
− Return codes
գ $?

4.0 | Automation, Orchestration, and Scripting

4.3

Summarize Python basics used for Linux system administration.
• Setting up a virtual environment
• Built-in modules
• Installing dependencies
• Python fundamentals
− Indentations
− Current versions
− Data types and structures
գ Boolean
գ Dictionary
գ Floating point

4.4

գ Integer
գ List
գ String
− Extensible using modules
and packages
• Python Enhancement Proposal
(PEP) 8 best practices

Given a scenario, implement version control using Git.
• .gitignore
• add
• branch
• checkout
• clone
• commit
• config
• diff
• fetch
• init

4.5

• log
• merge
− squash
բ pull
բ push
բ rebase
բ reset
բ stash
բ tag

Summarize best practices and responsible uses of artificial intelligence (AI).
• Common use cases
− Generation of code
− Generation of regular expressions
− Generation of infrastructure as code
− Document code/create documentation
− Recommendations for how to improve compliance
− Security review
− Code optimization
− Code linting
• Best practices
− Avoid copy/paste without review/quality assurance
− Verify output

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

− Data governance
գ Security of data
ը Large language model (LLM) training
ը Human review
գ Local models
ը Private vs. public
− Adhere to corporate policy
• Prompt engineering

5.0 Troubleshooting
5.1

Summarize monitoring concepts and configurations in a Linux system.
• Service monitoring
− Service-level agreement (SLA)
− Service-level indicator (SLI)
− Service-level objective (SLO)
• Data acquisition methods
− Simple Network Management
Protocol (SNMP)
գ Traps
գ Management information
bases (MIBs)
− Agent/agentless

5.2

• Configurations
− Thresholds
− Alerts
− Events
− Notifications
− Logging

Given a scenario, analyze and troubleshoot hardware, storage, and Linux OS issues.
• Common issues
− Kernel panic
− Data corruption issues
− Kernel corruption issues
− Package dependency issues
− Filesystem will not mount
− Server not turning on
− OS filesystem full
− Server inaccessible
− Device failure
− Inode exhaustion

5.3

− Webhooks
− Health checks
− Log aggregation

− Partition not writable
− Segmentation fault
− Grand Unified Bootloader
(GRUB) misconfiguration
− Killed processes
− PATH misconfiguration issues
− Systemd unit failures
− Missing or disabled drivers
− Unresponsive process
− Quota issues
− Memory leaks

Given a scenario, analyze and troubleshoot networking issues on a Linux system.
• Common issues
− Misconfigured firewalls
− DHCP issues
− DNS issues
− Interface misconfiguration
գ Maximum transmission
unit (MTU) mismatch
գ Bonding
գ Media access control
(MAC) spoofing

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

գ Subnet
գ Cannot ping server
− Routing issues
գ Gateway
− Server unreachable
− IP conflicts
− Dual stack issues (IPv4 and IPv6)
− Link down
− Link negotiation issues

5.0 | Troubleshooting

5.4

Given a scenario, analyze and troubleshoot security issues on a Linux system.
• Common issues
− SELinux issues
գ Policy
գ Context
գ Booleans
− File and directory permission issues
գ ACLs
գ Attributes
− Account access
− Unpatched vulnerable systems

5.5

− Exposed or misconfigured services
− Remote access issues
− Certificate issues
− Misconfigured package repository
− Use of obsolete or insecure
protocols and ciphers
− Cipher negotiation issues

Given a scenario, analyze and troubleshoot performance issues.
• Common symptoms
− Swapping
− Out of memory
− Slow application response
− System unresponsiveness
− High CPU usage
− High load average
− High context switching
− High failed log-in attempts
− Slow startup
− High input/output (I/O) wait time
− Packet drops
− Jitter
− Random disconnects
− Random timeouts
− High latency
− Slow response times
− High disk latency
− Low throughput
− Blocked processes
− Hardware errors
− Sluggish terminal behavior
− Exceeding baselines
− Slow remote storage response
− CPU bottleneck

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

CompTIA Linux+ Acronym List
The following acronyms appear on the CompTIA Linux+ exam. Candidates are
encouraged to review the complete list and attain a working knowledge of all
listed acronyms as part of a comprehensive exam preparation program.
ACRONYM
ACL		
ACME		
AI		
AIDE		
API		
ARM		
BIOS		
CA		
CI/CD		
CIFS		
CIS		
CMS		
CPU		
CSV		
CUPS		
CVE		
CVSS		
DHCP		
DNAT		
DNS		
EGID		
EPEL		
EUID		
FEC		
FHS		
FQDN		
FTP		
FUSE		
GDPR		
GID		
GNU		
GPG2		
GPG		
GPT		
GPU		
GRUB		
GUI		
GUID		
HMAC		
HTTP		
HTTPD		
IaC		

DEFINITION
Access Control List
Automated Certificate Management Environment
Artificial Intelligence
Advanced Intrusion Detection Environment
Application Programming Interface
Advanced Reduced Instruction Set Computer (RISC) Machine
Basic Input/Output System
Certificate Authority
Continuous Integration/Continuous Deployment
Common Internet File System
Center for Internet Security
Content Management System
Central Processing Unit
Comma-seperated Value
Common UNIX Printing System
Common Vulnerabilities and Exposures
Common Vulnerability Scoring System
Dynamic Host Configuration Protocol
Destination Network Address Translation
Domain Name System
Effective Group Identifier
Extra Packages for Enterprise Linux
Effective User Identifier
Forward Error Correction
Filesystem Hierarchy Standard
Fully Qualified Domain Name
File Transfer Protocol
Filesystem in Userspace
General Data Protection Regulation
Group Identifier
Gnu’s Not Unix
GNU Privacy Guard 2
GNU Privacy Guard
GUID (Globally Unique Identifier) Partition Table
Graphics Processing Unit
Grand Unified Bootloader
Graphical User Interface
Globally Unique Identifier
Hashed Message Authentication Code
HyperText Transfer Protocol
HyperText Transfer Protocol Daemon
Infrastructure as Code

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

ACRONYM
ICMP		
IFS/OFS		
IMAP4		
initrd		
I/O		
IoC		
IOPS		
IP		
ISO		
JSON		
KRB 5		
KVM		
LAN		
LDAP		
LLM		
LUKS		
LUKS2		
LVM		
MAC		
MBR		
MFA		
MIB		
MTU		
NAS		
NAT		
NFS		
NIC		
NTP		
NVMe		
OOM		
OpenSCAP
OpenSSL
OS		
PAM		
PAT		
PEP		
PHP		
PID		
PKI		
PPID		
PTP		
PV		
PXE		
qcrow		
QEMU		
RAID		
RAM		
RISC		
RPM		
SAN		
SELinux		
setGID		
setUID		
SFTP		

DEFINITION
Internet Control Message Protocol
Internal Field Separator/Output Field Separator
Internet Messaging Access Protocol 4
Initial RAM Disk
Input/Output
Indicators of Compromise
Input/Output Operations Per Second
Internet Protocol
International Standards Organization
JavaScript Object Notation
Kerberos 5
Kernel-based Virtual Machine
Local Area Network
Lightweight Directory Access Protocol
Large Language Model
Linux Unified Key Setup
Linux Unified Key Setup 2
Logical Volume Manager
Media Access Control
Master Boot Record
Multifactor Authentication
Management Information Base
Maximum Transmission Unit
Network-attached Storage
Network Address Translation
Network File System
Network Interface Card
Network Time Protocol
Non-Volatile Memory Express
Out of Memory
Open Security Content Automation Protocol
Open Secure Sockets Layer
Operating System
Pluggable Authentication Modules
Port Addresss Translation
Python Enhancement Proposal
PHP: Hypertext Preprocessor
Process Identification Number
Public Key Infrastructure
Parent Process Identification Number
Precision Time Protocol
Physical Volume
Preboot Execution Environment
QEMU Copy on Write
Quick Emulator
Redundant Array of Independent Disks
Random Access Memory
Reduced Instruction Set Computer
Red Hat Package Manager
Storage Area Network
Security Enhanced Linux
Set Group Identity
Set User Identity
Secure File Transfer Protocol

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

ACRONYM
SLA		
SLES		
SLI		
SLO		
SMB		
SMTP		
SNAT		
SNMP		
SR-IOV		
SSD		
SSH		
SSHD		
SSL		
SSO		
SSSD		
TCP		
TFTP		
TLS		
TOTP		
TTL		
UDP		
UEFI		
UFW		
UID		
USB		
UUID		
Vim		
VM		
WAN		
XML		
YAML		

DEFINITION
Service-level Agreement
SUSE Linux Enterprise Server
Service-level Indicator
Service-level Objective
Server Message Block
Simple Mail Transfer Protocol
Source Network Address Translation
Simple Network Management Protocol
Single Root Input/Output Virtualization
Solid-state Drive
Secure Shell
Secure Shell Daemon
Secure Sockets Layer
Single Sign-On
System Security Services Daemon
Transmission Control Protocol
Trivial File Transfer Protocol
Transport Layer Security
Time-based One-time Password
Time to Live
User Datagram Protocol
Unified Extensible Firmware Interface
Uncomplicated Firewall
Unique Identifier
Universal Serial Bus
Univerally Unique Identifier
Vi Improved
Virtual Machine
Wide Area Network
Extensible Markup Langage
YAML Ain't Markup Language

CompTIA Linux+ XK0-006 V8 Certification Exam
Exam Objectives Document Version 5.0
Copyright © 2024 CompTIA, Inc. All rights reserved.

CompTIA Linux+ Hardware and Software List
CompTIA has included this sample list of hardware and software to
assist candidates as they prepare for the Linux+ certification exam.
This list may also be helpful for training companies that wish to create
a lab component for their training offering. The bulleted lists below
each topic are sample lists and are not exhaustive.
EQUIPMENT
• Internet access
• Laptop or desktop that supports
virtualization or access to a
cloud service provider
• Network
• Router
• Spare parts/hardware
• Solid-state drive (SSD)
• Switch
• Universal Serial Bus (USB) media
• Wireless access point

SOFTWARE
• Automation tools
− Ansible
− Puppet
• Containerization software
− Docker
− Kubernetes
գ Minikube
− Podman

RECOMMENDED DISTRIBUTIONS
• Alma Linux
• Debian
• Fedora Linux
• OpenSUSE/SUSE Linux
Enterprise Server (SLES)
• Red Hat Enterprise Linux
• Rocky Linux
• Ubuntu

• Git
• Git repository
• LLM access
• Package repository
• PuTTY or SSH client
• Python 3
• Virtualization software

© 2024 CompTIA, Inc., used under license by CompTIA, Inc. All rights reserved. All certification programs and education related to such
programs are operated exclusively by CompTIA, Inc. CompTIA is a registered trademark of CompTIA, Inc. in the U.S. and internationally.
Other brands and company names mentioned herein may be trademarks or service marks of CompTIA, Inc. or of their respective owners.
Reproduction or dissemination prohibited without the written consent of CompTIA, Inc. Printed in the U.S. 11409-Aug2024

