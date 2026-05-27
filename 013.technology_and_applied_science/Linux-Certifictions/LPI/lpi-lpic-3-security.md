---
title: LPI LPIC-3 Security
author: Justin Bealer
date_created: 2024-08-30, 02-06-34
date_modified: 2024-09-17, 09-29-59
reference: 
description: 
aliases: 
tags: 
---
# LPI LPIC-3 Security

## Links

[LPIC-3 Security](https://www.lpi.org/our-certifications/lpic-3-303-overview/)
[LPIC-3 Security Exam 303 Objectives](<https://www.lpi.org/our-certifications/exam-303-objectives/>)

## Books

## Objectives

        4.1 Topic 325: Cryptography
            4.1.1 325.1 X.509 Certificates and Public Key Infrastructures (weight: 5)
            4.1.2 325.2 X.509 Certificates for Encryption, Signing and Authentication (weight: 4)
            4.1.3 325.3 Encrypted File Systems (weight: 3)
            4.1.4 325.4 DNS and Cryptography (weight: 5)
        4.2 Topic 326: Host Security
            4.2.1 326.1 Host Hardening (weight: 3)
            4.2.2 326.2 Host Intrusion Detection (weight: 4)
            4.2.3 326.3 User Management and Authentication (weight: 5)
            4.2.4 326.4 FreeIPA Installation and Samba Integration (weight: 4)
        4.3 Topic 327: Access Control
            4.3.1 327.1 Discretionary Access Control (weight: 3)
            4.3.2 327.2 Mandatory Access Control (weight: 4)
            4.3.3 327.3 Network File Systems (weight: 3)
        4.4 Topic 328: Network Security
            4.4.1 328.1 Network Hardening (weight: 4)
            4.4.2 328.2 Network Intrusion Detection (weight: 4)
            4.4.3 328.3 Packet Filtering (weight: 5)
            4.4.4 328.4 Virtual Private Networks (weight: 4)
    5 Other Comments for consideration
    6 Changes since version 1
        6.1 321.3
            6.1.1 320.3 Advanced GPG
            6.1.2 320.6 OpenSSH

Introduction

The description of the entire LPIC-3 program is listed here.

Version Information

These objectives are version 2.0.0.

The version 1.x objectives can be found here.

Translations of Objectives

The following translations of the objectives are available on this wiki:

    English
    Spanish

Objectives
Topic 325: Cryptography
325.1 X.509 Certificates and Public Key Infrastructures (weight: 5)
Weight  5
Description  Candidates should understand X.509 certificates and public key infrastructures. They should know how to configure and use OpenSSL to implement certification authorities and issue SSL certificates for various purposes.

**Key Knowledge Areas:**

    Understand X.509 certificates, X.509 certificate lifecycle, X.509 certificate fields and X.509v3 certificate extensions.
    Understand trust chains and public key infrastructures.
    Generate and manage public and private keys.
    Create, operate and secure a certification authority.
    Request, sign and manage server and client certificates.
    Revoke certificates and certification authorities.

**The following is a partial list of the used files, terms and utilities:**

    openssl, including relevant subcommands
    OpenSSL configuration
    PEM, DER, PKCS
    CSR
    CRL
    OCSP

325.2 X.509 Certificates for Encryption, Signing and Authentication (weight: 4)
Weight  4
Description  Candidates should know how to use X.509 certificates for both server and client authentication. Candidates should be able to implement user and server authentication for Apache HTTPD. The version of Apache HTTPD covered is 2.4 or higher.

**Key Knowledge Areas:**

    Understand of SSL, TLS and protocol versions.
    Understand common transport layer security threats, for example Man-in-the-Middle.
    Configure Apache HTTPD with mod_ssl to provide HTTPS service, including SNI and HSTS.
    Configure Apache HTTPD with mod_ssl to authenticate users using certificates.
    Configure Apache HTTPD with mod_ssl to provide OCSP stapling.
    Use OpenSSL for SSL/TLS client and server tests. 

**The following is a partial list of the used files, terms and utilities:**

    Intermediate certification authorities
    Cipher configuration (no cipher-specific knowledge)
    httpd.conf
    mod_ssl
    openssl

325.3 Encrypted File Systems (weight: 3)
Weight  3
Description  Candidates should be able to set up and configure encrypted file systems.

**Key Knowledge Areas:**

    Understand block device and file system encryption.
    Use dm-crypt with LUKS to encrypt block devices.
    Use eCryptfs to encrypt file systems, including home directories and PAM integration.
    Be aware of plain dm-crypt and EncFS.

**The following is a partial list of the used files, terms and utilities:**

    cryptsetup
    cryptmount
    /etc/crypttab
    ecryptfsd
    ecryptfs-* commands
    mount.ecryptfs, umount.ecryptfs
    pam_ecryptfs

325.4 DNS and Cryptography (weight: 5)
Weight  5
Description  Candidates should have experience and knowledge of cryptography in the context of DNS and its implementation using BIND. The version of BIND covered is 9.7 or higher.

**Key Knowledge Areas:**

    Understanding of DNSSEC and DANE.
    Configure and troubleshoot BIND as an authoritative name server serving DNSSEC secured zones.
    Configure BIND as an recursive name server that performs DNSSEC validation on behalf of its clients.
    Key Signing Key, Zone Signing Key, Key Tag
    Key generation, key storage, key management and key rollover
    Maintenance and re-signing of zones
    Use DANE to publish X.509 certificate information in DNS.
    Use TSIG for secure communication with BIND.

**The following is a partial list of the used files, terms and utilities:**

    DNS, EDNS, Zones, Resource Records
    DNS resource records: DS, DNSKEY, RRSIG, NSEC, NSEC3, NSEC3PARAM, TLSA
    DO-Bit, AD-Bit
    TSIG
    named.conf
    dnssec-keygen
    dnssec-signzone
    dnssec-settime
    dnssec-dsfromkey
    rndc
    dig
    delv
    openssl

Topic 326: Host Security
326.1 Host Hardening (weight: 3)
Weight  3
Description  Candidates should be able to secure computers running Linux against common threats. This includes kernel and software configuration.

**Key Knowledge Areas:**

    Configure BIOS and boot loader (GRUB 2) security.
    Disable useless software and services.
    Use sysctl for security related kernel configuration, particularly ASLR, Exec-Shield and IP / ICMP configuration.
    Limit resource usage.
    Work with chroot environments.
    Drop unnecessary capabilities.
    Be aware of the security advantages of virtualization.

**The following is a partial list of the used files, terms and utilities:**

    grub.cfg
    chkconfig, systemctl
    ulimit
    /etc/security/limits.conf
    pam_limits.so
    chroot
    sysctl
    /etc/sysctl.conf

326.2 Host Intrusion Detection (weight: 4)
Weight  4
Description  Candidates should be familiar with the use and configuration of common host intrusion detection software. This includes updates and maintenance as well as automated host scans.

**Key Knowledge Areas:**

    Use and configure the Linux Audit system.
    Use chkrootkit.
    Use and configure rkhunter, including updates.
    Use Linux Malware Detect.
    Automate host scans using cron.
    Configure and use AIDE, including rule management.
    Be aware of OpenSCAP.

**The following is a partial list of the used files, terms and utilities:**

    auditd
    auditctl
    ausearch, aureport
    auditd.conf
    audit.rules
    pam_tty_audit.so
    chkrootkit
    rkhunter
    /etc/rkhunter.conf
    maldet
    conf.maldet
    aide
    /etc/aide/aide.conf

326.3 User Management and Authentication (weight: 5)
Weight  5
Description  Candidates should be familiar with management and authentication of user accounts. This includes configuration and use of NSS, PAM, SSSD and Kerberos for both local and remote directories and authentication mechanisms as well as enforcing a password policy.

**Key Knowledge Areas:**

    Understand and configure NSS.
    Understand and configure PAM.
    Enforce password complexity policies and periodic password changes.
    Lock accounts automatically after failed login attempts.
    Configure and use SSSD.
    Configure NSS and PAM for use with SSSD.
    Configure SSSD authentication against Active Directory, IPA, LDAP, Kerberos and local domains.
    Obtain and manage Kerberos tickets.

**The following is a partial list of the used files, terms and utilities:**

    nsswitch.conf
    /etc/login.defs
    pam_cracklib.so
    chage
    pam_tally.so, pam_tally2.so
    faillog
    pam_sss.so
    sssd
    sssd.conf
    sss_* commands
    krb5.conf
    kinit, klist, kdestroy

326.4 FreeIPA Installation and Samba Integration (weight: 4)
Weight  4
Description  Candidates should be familiar with FreeIPA v4.x. This includes installation and maintenance of a server instance with a FreeIPA domain as well as integration of FreeIPA with Active Directory.

**Key Knowledge Areas:**

    Understand FreeIPA, including its architecture and components.
    Understand system and configuration prerequisites for installing FreeIPA.
    Install and manage a FreeIPA server and domain.
    Understand and configure Active Directory replication and Kerberos cross-realm trusts.
    Be aware of sudo, autofs, SSH and SELinux integration in FreeIPA.

**The following is a partial list of the used files, terms and utilities:**

    389 Directory Server, MIT Kerberos, Dogtag Certificate System, NTP, DNS, SSSD, certmonger
    ipa, including relevant subcommands
    ipa-server-install, ipa-client-install, ipa-replica-install
    ipa-replica-prepare, ipa-replica-manage

Topic 327: Access Control
327.1 Discretionary Access Control (weight: 3)
Weight  3
Description  Candidates are required to understand Discretionary Access Control and know how to implement it using Access Control Lists. Additionally, candidates are required to understand and know how to use Extended Attributes.

**Key Knowledge Areas:**

    Understand and manage file ownership and permissions, including SUID and SGID.
    Understand and manage access control lists.
    Understand and manage extended attributes and attribute classes.

**The following is a partial list of the used files, terms and utilities:**

    getfacl
    setfacl
    getfattr
    setfattr 

327.2 Mandatory Access Control (weight: 4)
Weight  4
Description  Candidates should be familiar with Mandatory Access Control systems for Linux. Specifically, candidates should have a thorough knowledge of SELinux. Also, candidates should be aware of other Mandatory Access Control systems for Linux. This includes major features of these systems but not configuration and use.

**Key Knowledge Areas:**

    Understand the concepts of TE, RBAC, MAC and DAC.
    Configure, manage and use SELinux.
    Be aware of AppArmor and Smack.

**The following is a partial list of the used files, terms and utilities:**

    getenforce, setenforce, selinuxenabled
    getsebool, setsebool, togglesebool
    fixfiles, restorecon, setfiles
    newrole, runcon
    semanage
    sestatus, seinfo
    apol
    seaudit, seaudit-report, audit2why, audit2allow
    /etc/selinux/*

327.3 Network File Systems (weight: 3)
Weight  3
Description  Candidates should have experience and knowledge of security issues in use and configuration of NFSv4 clients and servers as well as CIFS client services. Earlier versions of NFS are not required knowledge.

**Key Knowledge Areas:**

    Understand NFSv4 security issues and improvements.
    Configure NFSv4 server and clients.
    Understand and configure NFSv4 authentication mechanisms (LIPKEY, SPKM, Kerberos).
    Understand and use NFSv4 pseudo file system.
    Understand and use NFSv4 ACLs.
    Configure CIFS clients.
    Understand and use CIFS Unix Extensions.
    Understand and configure CIFS security modes (NTLM, Kerberos).
    Understand and manage mapping and handling of CIFS ACLs and SIDs in a Linux system.

**The following is a partial list of the used files, terms and utilities:**

    /etc/exports
    /etc/idmapd.conf
    nfs4acl
    mount.cifs parameters related to ownership, permissions and security modes
    winbind
    getcifsacl, setcifsacl

Topic 328: Network Security
328.1 Network Hardening (weight: 4)
Weight  4
Description  Candidates should be able to secure networks against common threats. This includes verification of the effectiveness of security measures.

**Key Knowledge Areas:**

    Configure FreeRADIUS to authenticate network nodes.
    Use nmap to scan networks and hosts, including different scan methods.
    Use Wireshark to analyze network traffic, including filters and statistics.
    Identify and deal with rogue router advertisements and DHCP messages.

**The following is a partial list of the used files, terms and utilities:**

    radiusd
    radmin
    radtest, radclient
    radlast, radwho
    radiusd.conf
    /etc/raddb/*
    nmap
    wireshark
    tshark
    tcpdump
    ndpmon

328.2 Network Intrusion Detection (weight: 4)
Weight  4
Description  Candidates should be familiar with the use and configuration of network security scanning, network monitoring and network intrusion detection software. This includes updating and maintaining the security scanners.

**Key Knowledge Areas:**

    Implement bandwidth usage monitoring.
    Configure and use Snort, including rule management.
    Configure and use OpenVAS, including NASL.

**The following is a partial list of the used files, terms and utilities:**

    ntop
    Cacti
    snort
    snort-stat
    /etc/snort/*
    openvas-adduser, openvas-rmuser
    openvas-nvt-sync
    openvassd
    openvas-mkcert
    /etc/openvas/*

328.3 Packet Filtering (weight: 5)
Weight  5
Description  Candidates should be familiar with the use and configuration of packet filters. This includes netfilter, iptables and ip6tables as well as basic knowledge of nftables, nft and ebtables.

**Key Knowledge Areas:**

    Understand common firewall architectures, including DMZ.
    Understand and use netfilter, iptables and ip6tables, including standard modules, tests and targets.
    Implement packet filtering for both IPv4 and IPv6.
    Implement connection tracking and network address translation.
    Define IP sets and use them in netfilter rules.
    Have basic knowledge of nftables and nft.
    Have basic knowledge of ebtables.
    Be aware of conntrackd.

**The following is a partial list of the used files, terms and utilities:**

    iptables
    ip6tables
    iptables-save, iptables-restore
    ip6tables-save, ip6tables-restore
    ipset
    nft
    ebtables

328.4 Virtual Private Networks (weight: 4)
Weight  4
Description  Candidates should be familiar with the use of OpenVPN and IPsec.

**Key Knowledge Areas:**

    Configure and operate OpenVPN server and clients for both bridged and routed VPN networks.
    Configure and operate IPsec server and clients for routed VPN networks using IPsec-Tools / racoon.
    Awareness of L2TP.

**The following is a partial list of the used files, terms and utilities:**

    /etc/openvpn/*
    openvpn server and client
    setkey
    /etc/ipsec-tools.conf
    /etc/racoon/racoon.conf

Other Comments for consideration

As examples, following items are not in the current objectives:

1) Related to Wireless LAN: (Note: It’s not only for Linux though, it is necessary to consider because there are many points to be taken care for configuration in terms of security measure.)

Some aspects (i.e. Radius) are implemented in V2 (fth)

2) Related to IPv6: Not only IPv4, but also IPv6 should be considered.

Implemented in V2 wherever applicable (fth)

3) Security features in Linux: For example, ASLR and Exec-Shield (ASCII Armor) should be considered, because it causes security level lower if those are disabled.

Implemented in host hardening in V2 (fth)

4) Related to Forensics: In the survey of malware’s behavior, Sleuth Kit would be used to analyze the hard disk on Linux machine. Also in some cases, LVM commands would be used to restore the disk which became un-mountable. So that this area should be learned.

This is an interesting topic, but it goes beyond basic security in the sense it "prevention and defending". This is postmortal analysis. As the exam already contains a lot of topic this is postponed but up to discussion (fth)

5) Database (RDB, NoSQL) security: Because Application Security (bind, apache, etc.) is covered now, this item would be nice to cover. And this item is listed in the CIF, security contest almost every time. Also the counter-measure in server side is necessary.

As the other software / service aspects beyond Linux system security have been dropped this is considered out of scope for now too (fth)

6) Related to OpenFlow: There are several points to be considered in terms of security measure about the configuration of OpenFlow.

This is considered as an application aspect which seems to be beyond the scope for not (fth).

7) RADIUS: This was covered in 301 though, this is not covered now. This should be covered.

Implemented in V2 (fth)

8) DNS: More DNSSEC and DANE.

Implemented in V2 (fth)

9) Secure development, hardening

Hardening has been implemented for both hosts and networks in V2 (fth), Secure development is considered out of scope for now (fth)

10) Certificate Transparency

11) polkit
Changes since version 1
321.3

The following aspects have been removed from objective 321.3 User Management and Authentication:

**Key Knowledge Areas:**

    Kerberos Key Distribution Centre
    Kerberos Principals
    Kerberos Tickets
    password cracking 

**The following is a partial list of the used files, terms and utilities:**

    krb5.conf
    krb5kdc/kdc.conf
    kdb5_util
    rb5kdc/kadm5.acl
    kadmin, kadmin.local
    john

320.3 Advanced GPG
Weight  To be determined
Description  Candidates should know how to use GPG. This includes key generation, signing and publishing to key servers. Managing multiple private keys and IDs is also included.

**Key Knowledge Areas:**

    Use GPG for encryption and signing.
    Configure GPG.
    Manage private and public keys.
    Interact with GPG key servers to publish and retrieve public keys. 

**The following is a partial list of the used files, terms and utilities:**

    gpg
    gpgv
    gpg-agent
    ~/.gnupg/*

320.6 OpenSSH
Weight  To be determined
Description  Candidates should have experience and knowledge of security issues in use and configuration of OpenSSH SSH services.

**Key Knowledge Areas:**

    Configure and use OpenSSH.
    Manage OpenSSH keys and access control.
    Be aware of SSH protocol v1 and v2 security issues.

**The following is a partial list of the used files, terms and utilities:**

    /etc/ssh/*
    ~/.ssh/*
    ssh-keygen
    ssh-agent
    ssh-vulnkey 

Navigation menu

    Page Discussion View source History 

    Log in 

Exam Objectives

    Linux Essentials v1.6
    Security Essentials v1.0
    Web Development Essentials v1.0
    Open Source Essentials v1.0
    LPIC-1 v5.0
    LPIC-2 v4.5
    300 Objectives v3.0
    303 Objectives v3.0
    305 Objectives v3.0
    306 Objectives v3.0
    DevOps Tools Engineer Objectives v1.0
    BSD Specialist Objectives v1.0

Search

Navigation

    Main page
    Recent changes
    LPI Website

Tools

    What links here
    Related changes
    Special pages
    Printable version
    Permanent link
    Page information

Powered by MediaWiki

    This page was last modified on 3 May 2019, at 05:35. About LPI Wiki 
