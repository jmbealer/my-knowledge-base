---
title: LPI LPIC-2
author: Justin Bealer
date_created: 2024-08-30, 04-14-43
date_modified: 2024-09-17, 09-29-59
reference: 
description: 
aliases: 
tags: 
---
# LPI LPIC-2

These are required exams for LPI certification Level 2.
It covers advanced skills for the Linux professional that are common across all
distributions of Linux.

To pass LPIC-2, the candidate should be able to:

- Administer a small to medium-sized site.
- Plan, implement, maintain, keep consistent, secure, and troubleshoot a small
mixed (MS, Linux) network, including a:
  - LAN server (Samba, NFS, DNS, DHCP, client management).
  - Internet Gateway (firewall, VPN, SSH, web cache/proxy, mail).
  - Internet Server (web server and reverse proxy, FTP server).
- Supervise assistants.
- Advise management on automation and purchases.

## Links

[LPIC-2 Overview](https://www.lpi.org/our-certifications/lpic-2-overview/)
[LPIC-2 Exam 201 Objectives](https://www.lpi.org/our-certifications/exam-201-objectives/)
[LPIC-2 Exam 202 Objectives](https://www.lpi.org/our-certifications/exam-202-objectives/)

## Books

## Objectives: Exam 201 1-7

### Topic 200: Capacity Planning 1-2

#### 200.1 Measure and Troubleshoot Resource Usage Weight: 6

**Description:** Candidates should be able to measure hardware resource and
network bandwidth, identify and troubleshoot resource problems.

**Key Knowledge Areas:**

- Measure CPU usage.
- Measure memory usage.
- Measure disk I/O.
- Measure network I/O.
- Measure firewalling and routing throughput.
- Map client bandwidth usage.
- Match / correlate system symptoms with likely problems.
- Estimate throughput and identify bottlenecks in a system including networking.

**The following is a partial list of the used files, terms and utilities:**

- iostat
- iotop
- vmstat
- netstat
- ss
- iptraf
- pstree, ps
- w
- lsof
- top
- htop
- uptime
- sar
- swap
- processes blocked on I/O
- blocks in
- blocks out

#### 200.2 Predict Future Resource Needs Weight: 2

**Description:** Candidates should be able to monitor resource usage to predict
future resource needs.

**Key Knowledge Areas:**

- Use monitoring and measurement tools to monitor IT infrastructure usage.
- Predict capacity break point of a configuration.
- Observe growth rate of capacity usage.
- Graph the trend of capacity usage.
- Awareness of monitoring solutions such as Icinga2, Nagios, collectd, MRTG and Cacti

**The following is a partial list of the used files, terms and utilities:**

- diagnose
- predict growth
- resource exhaustion

### Topic 201: Linux Kernel 1-3

#### 201.1 Kernel Components Weight: 2

**Description:** Candidates should be able to utilise kernel components that are
necessary to specific hardware, hardware drivers, system resources and
requirements. This objective includes implementing different types of kernel
images, understanding stable and longterm kernels and patches, as well as using
kernel modules.

**Key Knowledge Areas:**

- Kernel 2.6.x, 3.x and 4.x documentation

**The following is a partial list of the used files, terms and utilities:**

- /usr/src/linux/
- /usr/src/linux/Documentation/
- zImage
- bzImage
- xz compression

#### 201.2 Compiling a Linux Kernel Weight: 3

**Description:** Candidates should be able to properly configure a kernel to
include or disable specific features of the Linux kernel as necessary. This
objective includes compiling and recompiling the Linux kernel as needed,
updating and noting changes in a new kernel, creating an initrd image and
installing new kernels.

**Key Knowledge Areas:**

- /usr/src/linux/
- Kernel Makefiles
- Kernel 2.6.x, 3.x and 4.x make targets
- Customize the current kernel configuration.
- Build a new kernel and appropriate kernel modules.
- Install a new kernel and any modules.
- Ensure that the boot manager can locate the new kernel and associated files.
- Module configuration files
- Use DKMS to compile kernel modules.
- Awareness of dracut

**The following is a partial list of the used files, terms and utilities:**

- mkinitrd
- mkinitramfs
- make
- make targets (all, config, xconfig, menuconfig, gconfig, oldconfig,
mrproper, zImage, bzImage, modules, modules_install, rpm-pkg, binrpm-pkg,
deb-pkg)
- gzip
- bzip2
- module tools
- /usr/src/linux/.config
- /lib/modules/kernel-version/
- depmod
- dkms

#### 201.3 Kernel Runtime Management and Troubleshooting Weight: 4

**Description:** Candidates should be able to manage and/or query a 2.6.x, 3.x
or 4.x kernel and its loadable modules. Candidates should be able to identify
and correct common boot and run time issues. Candidates should understand device
detection and management using udev. This objective includes troubleshooting
udev rules.

**Key Knowledge Areas:**

- Use command-line utilities to get information about the currently running
kernel and kernel modules.
- Manually load and unload kernel modules.
- Determine when modules can be unloaded.
- Determine what parameters a module accepts.
- Configure the system to load modules by names other than their file name.
- /proc filesystem
- Content of /, /boot/ , and /lib/modules/
- Tools and utilities to analyse information about the available hardware
- udev rules

**The following is a partial list of the used files, terms and utilities:**

- /lib/modules/kernel-version/modules.dep
- module configuration files in /etc/
- /proc/sys/kernel/
- /sbin/depmod
- /sbin/rmmod
- /sbin/modinfo
- /bin/dmesg
- /sbin/lspci
- /usr/bin/lsdev
- /sbin/lsmod
- /sbin/modprobe
- /sbin/insmod
- /bin/uname
- /usr/bin/lsusb
- /etc/sysctl.conf, /etc/sysctl.d/
- /sbin/sysctl
- udevmonitor
- udevadm monitor
- /etc/udev/

### Topic 202: System Startup 1-3

#### 202.1 Customizing System Startup Weight: 3

**Description:** Candidates should be able to query and modify the behaviour of
system services at various targets / run levels. A thorough understanding of the
systemd, SysV Init and the Linux boot process is required. This objective
includes interacting with systemd targets and SysV init run levels.

**Key Knowledge Areas:**

- Systemd
- SysV init
- Linux Standard Base Specification (LSB)

**The following is a partial list of the used files, terms and utilities:**

- /usr/lib/systemd/
- /etc/systemd/
- /run/systemd/
- systemctl
- systemd-delta
- /etc/inittab
- /etc/init.d/
- /etc/rc.d/
- chkconfig
- update-rc.d
- init and telinit

#### 202.2 System Recovery Weight: 4

**Description:** Candidates should be able to properly manipulate a Linux system
during both the boot process and during recovery mode. This objective includes
using both the init utility and init-related kernel options. Candidates should
be able to determine the cause of errors in loading and usage of bootloaders.
GRUB version 2 and GRUB Legacy are the bootloaders of interest. Both BIOS and
UEFI systems are covered.

**Key Knowledge Areas:**

- BIOS and UEFI
- NVMe booting
- GRUB version 2 and Legacy
- grub shell
- boot loader start and hand off to kernel
- kernel loading
- hardware initialisation and setup
- daemon/service initialisation and setup
- Know the different boot loader install locations on a hard disk or removable device.
- Overwrite standard boot loader options and using boot loader shells.
- Use systemd rescue and emergency modes.

**The following is a partial list of the used files, terms and utilities:**

- mount
- fsck
- inittab, telinit and init with SysV init
- The contents of /boot/, /boot/grub/ and /boot/efi/
- EFI System Partition (ESP)
- GRUB
- grub-install
- efibootmgr
- UEFI shell
- initrd, initramfs
- Master boot record
- systemctl

#### 202.3 Alternate Bootloaders Weight: 2

**Description:** Candidates should be aware of other bootloaders and their major
features.

**Key Knowledge Areas:**

- SYSLINUX, ISOLINUX, PXELINUX
- Understanding of PXE for both BIOS and UEFI
- Awareness of systemd-boot and U-Boot

**The following is a partial list of the used files, terms and utilities:**

- syslinux
- extlinux
- isolinux.bin
- isolinux.cfg
- isohdpfx.bin
- efiboot.img
- pxelinux.0
- pxelinux.cfg/
- uefi/shim.efi
- uefi/grubx64.efi

### Topic 203: Filesystem and Devices 1-3

#### 203.1 Operating the Linux Filesystem Weight: 4

**Description:** Candidates should be able to properly configure and navigate
the standard Linux filesystem. This objective includes configuring and mounting
various filesystem types.

**Key Knowledge Areas:**

- The concept of the fstab configuration
- Tools and utilities for handling swap partitions and files
- Use of UUIDs for identifying and mounting file systems
- Understanding of systemd mount units

**The following is a partial list of the used files, terms and utilities:**

- /etc/fstab
- /etc/mtab
- /proc/mounts
- mount and umount
- blkid
- sync
- swapon
- swapoff

#### 203.2 Maintaining a Linux Filesystem Weight: 3

**Description:** Candidates should be able to properly maintain a Linux
filesystem using system utilities. This objective includes manipulating standard
filesystems and monitoring SMART devices.

**Key Knowledge Areas:**

- Tools and utilities to manipulate and ext2, ext3 and ext4
- Tools and utilities to perform basic Btrfs operations, including subvolumes
and snapshots
- Tools and utilities to manipulate XFS
- Awareness of ZFS

**The following is a partial list of the used files, terms and utilities:**

- mkfs (mkfs.*)
- mkswap
- fsck (fsck.*)
- tune2fs, dumpe2fs and debugfs
- btrfs, btrfs-convert
- xfs_info, xfs_check, xfs_repair, xfsdump and xfsrestore
- smartd, smartctl

#### 203.3 Creating and Configuring Filesystem Options Weight: 2

**Description:** Candidates should be able to configure automount filesystems
using AutoFS. This objective includes configuring automount for network and
device filesystems. Also included is creating filesystems for devices such as
CD-ROMs and a basic feature knowledge of encrypted filesystems.

**Key Knowledge Areas:**

- autofs configuration files
- Understanding of automount units
- UDF and ISO9660 tools and utilities
- Awareness of other CD-ROM filesystems (HFS)
- Awareness of CD-ROM filesystem extensions (Joliet, Rock Ridge, El Torito)
- Basic feature knowledge of data encryption (dm-crypt / LUKS)

**The following is a partial list of the used files, terms and utilities:**

- /etc/auto.master
- /etc/auto.[dir]
- mkisofs
- cryptsetup

### Topic 204: Advanced Storage Device Administration 1-3

#### 204.1 Configuring RAID Weight: 3

**Description:** Candidates should be able to configure and implement software
RAID. This objective includes using and configuring RAID 0, 1 and 5.

**Key Knowledge Areas:**

- Software RAID configuration files and utilities

**The following is a partial list of the used files, terms and utilities:**

- mdadm.conf
- mdadm
- /proc/mdstat
- partition type 0xFD

#### 204.2 Adjusting Storage Device Access Weight: 2

**Description:** Candidates should be able to configure kernel options to
support various drives. This objective includes software tools to view & modify
hard disk settings including iSCSI devices.

**Key Knowledge Areas:**

- Tools and utilities to configure DMA for IDE devices including ATAPI and SATA
- Tools and utilities to configure Solid State Drives including AHCI and NVMe
- Tools and utilities to manipulate or analyse system resources (e.g.
interrupts)
- Awareness of sdparm command and its uses
- Tools and utilities for iSCSI
- Awareness of SAN, including relevant protocols (AoE, FCoE)

**The following is a partial list of the used files, terms and utilities:**

- hdparm, sdparm
- nvme
- tune2fs
- fstrim
- sysctl
- /dev/hd*, /dev/sd*, /dev/nvme*
- iscsiadm, scsi_id, iscsid and iscsid.conf
- WWID, WWN, LUN numbers

#### 204.3 Logical Volume Manager Weight: 3

**Description:** Candidates should be able to create and remove logical volumes,
volume groups, and physical volumes. This objective includes snapshots and
resizing logical volumes.

**Key Knowledge Areas:**

- Tools in the LVM suite
- Resizing, renaming, creating, and removing logical volumes, volume groups, and
physical volumes
- Creating and maintaining snapshots
- Activating volume groups

**The following is a partial list of the used files, terms and utilities:**

- /sbin/pv*
- /sbin/lv*
- /sbin/vg*
- mount
- /dev/mapper/
- lvm.conf

### Topic 205: Networking Configuration 1-3

#### 205.1 Basic Networking Configuration Weight: 3

**Description:** Candidates should be able to configure a network device to be
able to connect to a local, wired or wireless, and a wide-area network. This
objective includes being able to communicate between various subnets within a
single network including both IPv4 and IPv6 networks.

**Key Knowledge Areas:**

- Utilities to configure and manipulate ethernet network interfaces
- Configuring basic access to wireless networks

**The following is a partial list of the used files, terms and utilities:**

- ip
- ifconfig
- route
- arp
- iw
- iwconfig
- iwlist

#### 205.2 Advanced Network Configuration Weight: 4

**Description:** Candidates should be able to configure a network device to
implement various network authentication schemes. This objective includes
configuring a multi-homed network device and resolving communication problems.

**Key Knowledge Areas:**

- Utilities to manipulate routing tables
- Utilities to configure and manipulate ethernet network interfaces
- Utilities to analyse the status of the network devices
- Utilities to monitor and analyse the TCP/IP traffic

**The following is a partial list of the used files, terms and utilities:**

- ip
- ifconfig
- route
- arp
- ss
- netstat
- lsof
- ping, ping6
- nc
- tcpdump
- nmap

#### 205.3 Troubleshooting Network Issues Weight: 4

**Description:** Candidates should be able to identify and correct common
network setup issues, to include knowledge of locations for basic configuration
files and commands.

**Key Knowledge Areas:**

- Location and content of access restriction files
- Utilities to configure and manipulate ethernet network interfaces
- Utilities to manage routing tables
- Utilities to list network states.
- Utilities to gain information about the network configuration
- Methods of information about the recognised and used hardware devices
- System initialisation files and their contents (Systemd and SysV init)
- Awareness of NetworkManager and its impact on network configuration

**The following is a partial list of the used files, terms and utilities:**

- ip
- ifconfig
- route
- ss
- netstat
- /etc/network/, /etc/sysconfig/network-scripts/
- ping, ping6
- traceroute, traceroute6
- mtr
- hostname
- System log files such as /var/log/syslog, /var/log/messages and the systemd
journal
- dmesg
- /etc/resolv.conf
- /etc/hosts
- /etc/hostname, /etc/HOSTNAME
- /etc/hosts.allow, /etc/hosts.deny

### Topic 206: System Maintenance 1-3

#### 206.1 Make and Install Programs from Source Weight: 2

**Description:** Candidates should be able to build and install an executable
program from source. This objective includes being able to unpack a file of
sources.

**Key Knowledge Areas:**

- Unpack source code using common compression and archive utilities.
- Understand basics of invoking make to compile programs.
- Apply parameters to a configure script.
- Know where sources are stored by default.

**The following is a partial list of the used files, terms and utilities:**

- /usr/src/
- gunzip
- gzip
- bzip2
- xz
- tar
- configure
- make
- uname
- install
- patch

#### 206.2 Backup Operations Weight: 3

**Description:** Candidates should be able to use system tools to back up
important system data.

**Key Knowledge Areas:**

- Knowledge about directories that have to be included in backups
- Awareness of network backup solutions such as Amanda, Bacula, Bareos and
BackupPC
- Knowledge of the benefits and drawbacks of tapes, CDR, disk or other backup
media
- Perform partial and manual backups.
- Verify the integrity of backup files.
- Partially or fully restore backups.

**The following is a partial list of the used files, terms and utilities:**

- /bin/sh
- dd
- tar
- /dev/st*and /dev/nst*
- mt
- rsync

#### 206.3 Notify Users on System-related Issues Weight: 1

**Description:** Candidates should be able to notify the users about current
issues related to the system.

**Key Knowledge Areas:**

- Automate communication with users through logon messages.
- Inform active users of system maintenance

**The following is a partial list of the used files, terms and utilities:**

- /etc/issue
- /etc/issue.net
- /etc/motd
- wall
- shutdown
- systemctl

## Objectives: Exam 202 1-6

        7.1 ### Topic 207: Domain Name Server
            7.1.1 207.1 Basic DNS server configuration (weight: 3)
            7.1.2 207.2 Create and maintain DNS zones (weight: 3)
            7.1.3 207.3 Securing a DNS server (weight: 2)
        7.2 ### Topic 208: HTTP Services
            7.2.1 208.1 Basic Apache configuration (weight: 4)
            7.2.2 208.2 Apache configuration for HTTPS (weight: 3)
            7.2.3 208.3 Implementing Squid as a caching proxy (weight: 2)
            7.2.4 208.4 Implementing Nginx as a web server and a reverse proxy (weight: 2)
        7.3 ### Topic 209: File Sharing
            7.3.1 209.1 Samba Server Configuration (weight: 5)
            7.3.2 209.2 NFS Server Configuration (weight: 3)
        7.4 ### Topic 210: Network Client Management
            7.4.1 210.1 DHCP configuration (weight: 2)
            7.4.2 210.2 PAM authentication (weight: 3)
            7.4.3 210.3 LDAP client usage (weight: 2)
            7.4.4 210.4 Configuring an OpenLDAP server (weight: 4)
        7.5 ### Topic 211: E-Mail Services
            7.5.1 211.1 Using e-mail servers (weight: 4)
            7.5.2 211.2 Managing E-Mail Delivery (weight: 2)
            7.5.3 211.3 Managing Mailbox Access (weight: 2)
        7.6 ### Topic 212: System Security
            7.6.1 212.1 Configuring a router (weight: 3)
            7.6.2 212.2 Managing FTP servers (weight: 2)
            7.6.3 212.3 Secure shell (SSH) (weight: 4)
            7.6.4 212.4 Security tasks (weight: 3)
            7.6.5 212.5 OpenVPN (weight: 2)
    8 Future Change Considerations

### Topic 207: Domain Name Server 1-3

#### 207.1 Basic DNS Server Configuration Weight: 3

**Description:** Candidates should be able to configure BIND to function as an
authoritative and as a recursive, caching-only DNS server. This objective
includes the ability to manage a running server and configuring logging.

**Key Knowledge Areas:**

- BIND 9.x configuration files, terms and utilities
- Defining the location of the BIND zone files in BIND configuration files
- Reloading modified configuration and zone files
- Awareness of dnsmasq, djbdns and PowerDNS as alternate name servers

**The following is a partial list of the used files, terms and utilities:**

- /etc/named.conf
- /var/named/
- rndc
- named-checkconf
- kill
- host
- dig

#### 207.2 Create and Maintain DNS Zones Weight: 3

**Description:** Candidates should be able to create a zone file for a forward
or reverse zone and hints for root level servers. This objective includes
setting appropriate values for records, adding hosts in zones and adding zones
to the DNS. A candidate should also be able to delegate zones to another DNS
server.

**Key Knowledge Areas:**

- BIND 9 configuration files, terms and utilities
- Utilities to request information from the DNS server
- Layout, content and file location of the BIND zone files
- Various methods to add a new host in the zone files, including reverse zones

**The following is a partial list of the used files, terms and utilities:**

- /var/named/
- zone file syntax
- resource record formats
- named-checkzone
- named-compilezone
- masterfile-format
- dig
- nslookup
- host

#### 207.3 Securing a DNS Server Weight: 2

**Description:** Candidates should be able to configure a DNS server to run as a
non-root user and run in a chroot jail. This objective includes secure exchange
of data between DNS servers.

**Key Knowledge Areas:**

- BIND 9 configuration files
- Configuring BIND to run in a chroot jail
- Split configuration of BIND using the forwarders statement
- Configuring and using transaction signatures (TSIG)
- Awareness of DNSSEC and basic tools
- Awareness of DANE and related records

**The following is a partial list of the used files, terms and utilities:**

- /etc/named.conf
- /etc/passwd
- DNSSEC
- dnssec-keygen
- dnssec-signzone

### Topic 208: HTTP Services 1-4

#### 208.1 Basic Apache Configuration Weight: 4

**Description:** Candidates should be able to install and configure a web
server. This objective includes monitoring the server's load and performance,
restricting client user access, configuring support for scripting languages as
modules and setting up client user authentication. Also included is configuring
server options to restrict usage of resources. Candidates should be able to
configure a web server to use virtual hosts and customize file access.

**Key Knowledge Areas:**

- Apache 2.4 configuration files, terms and utilities
- Apache log files configuration and content
- Access restriction methods and files
- mod_perl and PHP configuration
- Client user authentication files and utilities
- Configuration of maximum requests, minimum and maximum servers and clients
- Apache 2.4 virtual host implementation (with and without dedicated IP addresses)
- Using redirect statements in Apache's configuration files to customize file access

**The following is a partial list of the used files, terms and utilities:**

- access logs and error logs
- .htaccess
- httpd.conf
- mod_auth_basic, mod_authz_host and mod_access_compat
- htpasswd
- AuthUserFile, AuthGroupFile
- apachectl, apache2ctl
- httpd, apache2

#### 208.2 Apache Configuration for HTTPS Weight: 3

**Description:** Candidates should be able to configure a web server to provide
HTTPS.

**Key Knowledge Areas:**

- SSL configuration files, tools and utilities
- Generate a server private key and CSR for a commercial CA
- Generate a self-signed Certificate
- Install the key and certificate, including intermediate CAs
- Configure Virtual Hosting using SNI
- Awareness of the issues with Virtual Hosting and use of SSL
- Security issues in SSL use, disable insecure protocols and ciphers

**The following is a partial list of the used files, terms and utilities:**

- Apache2 configuration files
- /etc/ssl/, /etc/pki/
- openssl, CA.pl
- SSLEngine, SSLCertificateKeyFile, SSLCertificateFile
- SSLCACertificateFile, SSLCACertificatePath
- SSLProtocol, SSLCipherSuite, ServerTokens, ServerSignature, TraceEnable

#### 208.3 Implementing Squid as a Caching Proxy Weight: 2

**Description:** Candidates should be able to install and configure a proxy
server, including access policies, authentication and resource usage.

**Key Knowledge Areas:**

- Squid 3.x configuration files, terms and utilities
- Access restriction methods
- Client user authentication methods
- Layout and content of ACL in the Squid configuration files

**The following is a partial list of the used files, terms and utilities:**

- squid.conf
- acl
- http_access

#### 208.4 Implementing Nginx as a Web Server and a Reverse Proxy Weight: 2

**Description:** Candidates should be able to install and configure a reverse
proxy server, Nginx. Basic configuration of Nginx as a HTTP server is included.

**Key Knowledge Areas:**

- Nginx
- Reverse Proxy
- Basic Web Server

**The following is a partial list of the used files, terms and utilities:**

- /etc/nginx/
- nginx

### Topic 209: File Sharing 1-2

#### 209.1 Samba Server Configuration Weight: 5

**Description:** Candidates should be able to set up a Samba server for various
clients. This objective includes setting up Samba as a standalone server as well
as integrating Samba as a member in an Active Directory. Furthermore, the
configuration of simple CIFS and printer shares is covered. Also covered is a
configuring a Linux client to use a Samba server. Troubleshooting installations
is also tested.

**Key Knowledge Areas:**

- Samba 4 documentation
- Samba 4 configuration files
- Samba 4 tools and utilities and daemons
- Mounting CIFS shares on Linux
- Mapping Windows user names to Linux user names
- User-Level, Share-Level and AD security

**The following is a partial list of the used files, terms and utilities:**

- smbd, nmbd, winbindd
- smbcontrol, smbstatus, testparm, smbpasswd, nmblookup
- samba-tool
- net
- smbclient
- mount.cifs
- /etc/samba/
- /var/log/samba/

#### 209.2 NFS Server Configuration Weight: 3

**Description:** Candidates should be able to export filesystems using NFS. This
objective includes access restrictions, mounting an NFS filesystem on a client
and securing NFS.

**Key Knowledge Areas:**

- NFS version 3 configuration files
- NFS tools and utilities
- Access restrictions to certain hosts and/or subnets
- Mount options on server and client
- TCP Wrappers
- Awareness of NFSv4

**The following is a partial list of the used files, terms and utilities:**

- /etc/exports
- exportfs
- showmount
- nfsstat
- /proc/mounts
- /etc/fstab
- rpcinfo
- mountd
- portmapper

### Topic 210: Network Client Management 1-4

#### 210.1 DHCP Configuration Weight: 2

**Description:** Candidates should be able to configure a DHCP server. This
objective includes setting default and per client options, adding static hosts
and BOOTP hosts. Also included is configuring a DHCP relay agent and maintaining
the DHCP server.

**Key Knowledge Areas:**

- DHCP configuration files, terms and utilities
- Subnet and dynamically-allocated range setup
- Awareness of DHCPv6 and IPv6 Router Advertisements

**The following is a partial list of the used files, terms and utilities:**

- dhcpd.conf
- dhcpd.leases
- DHCP Log messages in syslog or systemd journal
- arp
- dhcpd
- radvd
- radvd.conf

#### 210.2 PAM Authentication Weight: 3

**Description:** The candidate should be able to configure PAM to support
authentication using various available methods. This includes basic SSSD
functionality.

**Key Knowledge Areas:**

- PAM configuration files, terms and utilities
- passwd and shadow passwords
- Use sssd for LDAP authentication

**The following is a partial list of the used files, terms and utilities:**

- /etc/pam.d/
- pam.conf
- nsswitch.conf
- pam_unix, pam_cracklib, pam_limits, pam_listfile, pam_sss
- sssd.conf

#### 210.3 LDAP Client Usage Weight: 2

**Description:** Candidates should be able to perform queries and updates to an
LDAP server. Also included is importing and adding items, as well as adding and
managing users.

**Key Knowledge Areas:**

- LDAP utilities for data management and queries
- Change user passwords
- Querying the LDAP directory

**The following is a partial list of the used files, terms and utilities:**

- ldapsearch
- ldappasswd
- ldapadd
- ldapdelete

#### 210.4 Configuring an OpenLDAP Server Weight: 4

**Description:** Candidates should be able to configure a basic OpenLDAP server
including knowledge of LDIF format and essential access controls.

**Key Knowledge Areas:**

- OpenLDAP
- Directory based configuration
- Access Control
- Distinguished Names
- Changetype Operations
- Schemas and Whitepages
- Directories
- Object IDs, Attributes and Classes

**The following is a partial list of the used files, terms and utilities:**

- slapd
- slapd-config
- LDIF
- slapadd
- slapcat
- slapindex
- /var/lib/ldap/
- loglevel

### Topic 211: E-Mail Services 1-3

#### 211.1 Using E-mail Servers Weight: 4

**Description:** Candidates should be able to manage an e-mail server, including
the configuration of e-mail aliases, e-mail quotas and virtual e-mail domains.
This objective includes configuring internal e-mail relays and monitoring e-mail
servers.

**Key Knowledge Areas:**

- Configuration files for postfix
- Basic TLS configuration for postfix
- Basic knowledge of the SMTP protocol
- Awareness of sendmail and exim

**The following is a partial list of the used files, terms and utilities:**

- Configuration files and commands for postfix
- /etc/postfix/
- /var/spool/postfix/
- sendmail emulation layer commands
- /etc/aliases
- mail-related logs in /var/log/

#### 211.2 Managing E-Mail Delivery Weight: 2

**Description:** Candidates should be able to implement client e-mail management
software to filter, sort and monitor incoming user e-mail.

**Key Knowledge Areas:**

- Understanding of Sieve functionality, syntax and operators
- Use Sieve to filter and sort mail with respect to sender, recipient(s),
headers and size
- Awareness of procmail

**The following is a partial list of the used files, terms and utilities:**

- Conditions and comparison operators
- keep, fileinto, redirect, reject, discard, stop
- Dovecot vacation extension

#### 211.3 Managing Mailbox Access Weight: 2

**Description:** Candidates should be able to install and configure POP and IMAP
daemons.

**Key Knowledge Areas:**

- Dovecot IMAP and POP3 configuration and administration
- Basic TLS configuration for Dovecot
- Awareness of Courier

**The following is a partial list of the used files, terms and utilities:**

- /etc/dovecot/
- dovecot.conf
- doveconf
- doveadm

### Topic 212: System Security 1-5

#### 212.1 Configuring a Router Weight: 3

**Description:** Candidates should be able to configure a system to forward IP
packet and perform network address translation (NAT, IP masquerading) and state
its significance in protecting a network. This objective includes configuring
port redirection, managing filter rules and averting attacks.

**Key Knowledge Areas:**

- iptables and ip6tables configuration files, tools and utilities
- Tools, commands and utilities to manage routing tables.
- Private address ranges (IPv4) and Unique Local Addresses as well as Link Local Addresses (IPv6)
- Port redirection and IP forwarding
- List and write filtering and rules that accept or block IP packets based on
source or destination protocol, port and address
- Save and reload filtering configurations

**The following is a partial list of the used files, terms and utilities:**

- /proc/sys/net/ipv4/
- /proc/sys/net/ipv6/
- /etc/services
- iptables
- ip6tables

#### 212.2 Managing FTP Servers Weight: 2

**Description:** Candidates should be able to configure an FTP server for
anonymous downloads and uploads. This objective includes precautions to be taken
if anonymous uploads are permitted and configuring user access.

**Key Knowledge Areas:**

- Configuration files, tools and utilities for Pure-FTPd and vsftpd
- Awareness of ProFTPd
- Understanding of passive vs. active FTP connections

**The following is a partial list of the used files, terms and utilities:**

- vsftpd.conf
- important Pure-FTPd command line options

#### 212.3 Secure Shell (SSH) Weight: 4

**Description:** Candidates should be able to configure and secure an SSH
daemon. This objective includes managing keys and configuring SSH for users.
Candidates should also be able to forward an application protocol over SSH and
manage the SSH login.

**Key Knowledge Areas:**

- OpenSSH configuration files, tools and utilities

- Login restrictions for the superuser and the normal users

- Managing and using server and client keys to login with and without password

- Usage of multiple connections from multiple hosts to guard against loss of
connection to remote host following configuration changes

**The following is a partial list of the used files, terms and utilities:**

- ssh
- sshd
- /etc/ssh/sshd_config
- /etc/ssh/
- Private and public key files
- PermitRootLogin, PubKeyAuthentication, AllowUsers, PasswordAuthentication,
Protocol

#### 212.4 Security Tasks Weight: 3

**Description:** Candidates should be able to receive security alerts from
various sources, install, configure and run intrusion detection systems and
apply security patches and bugfixes.

**Key Knowledge Areas:**

- Tools and utilities to scan and test ports on a server
- Locations and organisations that report security alerts as Bugtraq, CERT or
other sources
- Tools and utilities to implement an intrusion detection system (IDS)
- Awareness of OpenVAS and Snort

**The following is a partial list of the used files, terms and utilities:**

- telnet
- nmap
- fail2ban
- nc
- iptables

#### 212.5 OpenVPN Weight: 2

**Description:** Candidates should be able to configure a VPN (Virtual Private
Network) and create secure point-to-point or site-to-site connections.

**Key Knowledge Areas:**

- OpenVPN

**The following is a partial list of the used files, terms and utilities:**

- /etc/openvpn/
- openvpn

### Future Change Considerations

Future changes to the objective will/may include:

- Extend the amount of NetworkManager covered, i.e. including the CLI
- lighttpd would have been too much coverage of web services. Perhaps reduce
Apache next revision to make room.
- host level IDS (tripwire, AIDE, etc) to be covered in future LPIC-1.
- introduction (or more) to FreeIPA
- add coverage of mod_security and mod_evasive to Apache HTTP (maybe as a
separate topic: Web Application Firewall)
- add coverage of a higher-level firewall package like firewalld or ufw
- Reconsider mod_perl
- Add firewall-cmd and /etc/firewalld/firewalld.conf related to firewalld to LPIC-2
- Awareness of firewalld
- Add nmcli and nmtui to LPIC-2
- Full coverage of IPv6 auto configuration
- Remove djbdns
- Advanced shell scripting (sed -e, set -x, set -o, pipefail, PIPESTATUS, declare)
- Filesystem quota (similar to the topic removed from LPIC-1)
- Understanding of consistency in backups, e.g. for databases
- Let's Encrypt for certification procurement
- 202.2: Reconsider NVMe booting
- 207.1: Consider dropping djbdns and consider unbound
- 207.1: /var/named/ is distro-specific
- 207.2: Remove creation of root.hints
- 207.2: Reconsider nslookup
- 207.3: Reconsider chroot
- 208.2: Remove CA.pl
- 208.2: Remove SNI specialties
- 208.2: Remove client certificate options
- 208.3: Reconsider the relevance of Squid
- 209.1: Remove Samba Share-Level security
- 209.1: Remove nmblookup
- 210.1: Remove arp
- 210.4: Aggregate Whitepages, schemas, classes etc.
- 212.2: Remove FTP
- 212.3: Remove Protocol
- 212.4: Remove bugtraq etc.
- Remove paths to commands and configuration files wherever possible
