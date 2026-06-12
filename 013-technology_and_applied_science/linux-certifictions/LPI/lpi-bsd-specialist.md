---
title: LPI BSD Specialist
author: Justin Bealer
date_created: 2024-08-30, 02-08-06
date_modified: 2024-09-17, 09-30-00
reference: 
description: 
aliases: 
tags: 
---
# LPI BSD Specialist

## Links

## Books

## Objectives

        7.1 Topic 711: BSD Installation and Software Management
            7.1.1 711.1 BSD Operating System Installation (weight: 3)
            7.1.2 711.2 BSD Software and Package Management (weight: 4)
            7.1.3 711.3 BSD System Startup Configuration (weight: 3)
            7.1.4 711.4 Hardware Configuration (weight: 2)
            7.1.5 711.5 BSD Kernel Parameters and System Security Level (weight: 2)
        7.2 Topic 712: Storage Devices and BSD Filesystems
            7.2.1 712.1 BSD Partitioning and Disk Labels (weight: 2)
            7.2.2 712.2 Create File Systems and Maintain their Integrity (weight: 1)
            7.2.3 712.3 Control Mounting and Unmounting of File Systems (weight: 2)
            7.2.4 712.4 Manage File Permissions and Ownership (weight: 3)
            7.2.5 712.5 Create and Change Hard and Symbolic Links (weight: 1)
            7.2.6 712.6 Find Files and BSD Directory Layout (weight: 2)
        7.3 Topic 713: Basic BSD System Administration
            7.3.1 713.1 Manage User Accounts and Groups (weight: 3)
            7.3.2 713.2 Automate System Administration Tasks by Scheduling Jobs (weight: 2)
            7.3.3 713.3 Maintain System Time (weight: 1)
            7.3.4 713.4 System Logging (weight: 2)
            7.3.5 713.5 Mail Transfer Agents (MTA) Basics (weight: 1)
            7.3.6 713.6 Manage Printing and Print Jobs (weight: 1)
            7.3.7 713.7 Manage User Sessions (weight: 1)
        7.4 Topic 714: Basic BSD Network Administration
            7.4.1 714.1 Fundamentals of Internet Protocols (weight: 2)
            7.4.2 714.2 Basic network configuration (weight: 3)
            7.4.3 714.3 Basic network troubleshooting (weight: 3)
            7.4.4 714.4 Configure Client Side DNS (weight: 2)
        7.5 Topic 715: Basic Unix Skills
            7.5.1 715.1 Use the Shell and Work on the Command Line (weight: 2)
            7.5.2 715.2 Perform basic file management (weight: 3)
            7.5.3 715.3 Create, Monitor and Kill Processes (weight: 3)
            7.5.4 715.4 Use Simple Regular Expressions (weight: 2)
            7.5.5 715.5 Perform basic file editing operations (weight: 2)
            7.5.6 715.6 Customize or write simple scripts (weight: 2)
    8 Future Change Considerations

Introduction

This is a required exam for the Linux Professional Institute BSD Specialist certification. It covers basic skills in installing and administering a BSD system.

This page IS A DRAFT for for the Linux Professional Institute BSD Specialist certification.

Candidate Description

The certification holder is a BSD system administrator. The certification holder has a solid understanding of the architecture of the BSD operating systems. This includes the ability to manage various aspects of a BSD installation, including user accounts and groups, processes, file systems, installed software and client networking configuration. Furthermore, the candidate is experienced in using standard BSD and Unix tools on the command line. The certification holder is able to apply these skills on FreeBSD, OpenBSD and NetBSD.

Version Information

These objectives are for version 1.0.0.

Translations of Objectives

The following translations of the objectives are available on this wiki:

    English
    Japanese

Exams and Requirements

The Linux Professional Institute BSD Specialist certification is awarded after passing this exam. There is no requirement to posses another certifications.

Hint on BSD Operating Systems

These objectives contain command and file names which might be relevant within the exam. Candidates should be aware that the exam covers three different BSD operating systems. Commands and files with the same name might exist on all or some of these systems and still differ in their behavior or content. This might be the case even when the command or file name is listed in the ‘common’ section of the objectives. Candidates are expected to be able to use the files and commands on all BSD operating systems mentioned in the objectives. Where appropriate, the exam will be specific which BSD operating system is covered.

Objectives
Topic 711: BSD Installation and Software Management
711.1 BSD Operating System Installation (weight: 3)

Weight
 3

Description
 
The candidate should be able to install FreeBSD, NetBSD, and OpenBSD. Furthermore, candidates should be able to upgrade an existing BSD installation.

**Key Knowledge Areas:**

    Install the FreeBSD, NetBSD, and OpenBSD operating systems using default options.
    Upgrade an existing FreeBSD, NetBSD or OpenBSD operating system installation.
    Determine the type and version of the operating system installed.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        uname
    FreeBSD:
        bsdinstall
        freebsd-update
    NetBSD:
        sysinst
    OpenBSD:
        bsd.rd

711.2 BSD Software and Package Management (weight: 4)

Weight
 4

Description
 
Candidates should be able to install, manage, and update software on a BSD system. This includes using pre-compiled binary software using a package manager as well as compiling software from source code and using ports.

**Key Knowledge Areas:**

    Candidates should understand software management mechanisms on BSD systems.
    Install, query, and uninstall pre-compiled binary packages.
    Use ports to compile software.
    Determine which installed software has pending upgrades or outstanding security vulnerabilities and install available upgrades.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        make
    FreeBSD:
        pkg install
        pkg delete
        pkg info
        pkg upgrade
    NetBSD:
        pkg_admin
        pkg_add
        pkg_delete
        pkg_info
    OpenBSD:
        pkg_add
        pkg_delete
        pkg_info

711.3 BSD System Startup Configuration (weight: 3)

Weight
 3

Description
 
Candidates should understand the BSD boot process and be able to manage services, including configuring which services are started at boot time. Furthermore, candidates should be able to start and restart a BSD system.

**Key Knowledge Areas:**

    Understand the boot process of each BSD operating system.
    Understand the role and principles of a bootloader, including BSD bootloader stages.
    Use rc startup scripts to start, stop, restart, and check the status of services.
    Configure services to be started at boot time.
    Start and restart a BSD system.
    Put a BSD system in single-user mode.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        boot(8)
        rc
        /etc/rc.conf
        /etc/rc.d/
        inetd
        shutdown
    FreeBSD:
        service
    NetBSD:
        service
    OpenBSD:
        rcctl

711.4 Hardware Configuration (weight: 2)

Weight
 2

Description
 
Candidates should be able to investigate a system’s hardware and configure how BSD handles hardware devices. This includes understanding the role of kernel modules and loading and managing existing kernel modules.

**Key Knowledge Areas:**

    Determine what hardware is installed on a system.
    Determine which hardware was probed at boot time.
    BSD-specific utilities which can be used to troubleshoot and manipulate PCI, ATA, and SCSI devices.
    View, load, and unload kernel modules.
    Availability of kernel modules in different BSD operating systems.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        dmesg
        /boot/loader.conf
    FreeBSD:
        camcontrol
        devinfo
        pciconf
        kldstat
        kldload
        kldunload
    NetBSD:
        atactl
        pcictl
        scsictl
        modstat
        modload
        modunload
    OpenBSD:
        atactl
        scsi

711.5 BSD Kernel Parameters and System Security Level (weight: 2)

Weight
 2

Description
 
Candidate should understand configurable kernel parameters (MIBs) and should be able to view and set kernel parameters. This includes understanding and setting BSD securelevels.

**Key Knowledge Areas:**

    Understand the concept of kernel MIBs.
    View MIBs and modify MIBs at run-time and permanently.
    Understand the concept and restrictions of BSD securelevels.
    Understand under which circumstances a securelevel can be raised or lowered.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        init
        sysctl
        /etc/sysctl.conf
    OpenBSD:
        config
        /etc/boot.conf

Topic 712: Storage Devices and BSD Filesystems
712.1 BSD Partitioning and Disk Labels (weight: 2)

Weight
 2

Description
 
Candidates should understand the concepts of disk slice tables and disk labels and be able to view, create, and modify the layout of a hard disk.

**Key Knowledge Areas:**

    Understand the concepts of disk slice tables and disk labels.
    View, create, or edit the disk slice table, master boot record, or disk label.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        fdisk
        disklabel
    OpenBSD:
        installboot

712.2 Create File Systems and Maintain their Integrity (weight: 1)

Weight
 1

Description
 
Candidates should be able to create file systems and check their integrity. This includes identifying files which consume the most disk space.

**Key Knowledge Areas:**

    Create UFS and ZFS file systems.
    Determine disk space usage and available space.
    Check the consistency of a UFS filesystem or health of a ZFS pool.
    Awareness of ZFS snapshots.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        newfs
        fsck
        du
        df
    FreeBSD:
        zpool
    NetBSD:
        zpool

712.3 Control Mounting and Unmounting of File Systems (weight: 2)

Weight
 2

Description
 
Candidates should be able to view mounted file systems, mount or unmount file systems, and determine which file systems will mount at boot.

**Key Knowledge Areas:**

    Determine which local file systems are currently mounted.
    Mount and unmount UFS or ZFS file systems.
    Configure which file systems are mounted at boot time.
    Resolve mount errors.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        mount
        umount
        /etc/fstab
        df
    FreeBSD
        zfs
    NetBSD
        zfs

712.4 Manage File Permissions and Ownership (weight: 3)

Weight
 3

Description
 
Candidates should understand and be able to manage file ownership and permissions.

**Key Knowledge Areas:**

    Understand traditional Unix permissions.
    View and modify permissions using both symbolic and octal mode.
    Understand and use the SUID bit, SGID bit, and sticky bit.
    Set the default file and directory permissions.
    View and modify ownership of files and directories.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        chown
        chgrp
        ls
        chmod
        umask

712.5 Create and Change Hard and Symbolic Links (weight: 1)

Weight
 1

Description
 
Candidates should be able to manage symbolic and hard links.

**Key Knowledge Areas:**

    Understand the difference between symbolic and hard links.
    Create, view, and remove both types of links.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        ln
        ls
        rm(1)

712.6 Find Files and BSD Directory Layout (weight: 2)

Weight
 2

Description
 
Candidates should understand the BSD directory layout and be able to find files according to different search criteria.

**Key Knowledge Areas:**

    Understand the directory layout used by BSD systems.
    Know which utilities can be used to find binaries, source, manpages, and files.
    Update the locate database.
    Use find to locate files, including using search criteria such as last modification time, size, type, file flags, UID or GID, permissions, or by a text pattern.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        whatis
        whereis
        which
        locate
        locate.updatedb
        find
        hier(7)

Topic 713: Basic BSD System Administration
713.1 Manage User Accounts and Groups (weight: 3)

Weight
 3

Description
 
Candidates should be able to create and manage user and system accounts as well as groups and group membership.

**Key Knowledge Areas:**

    Create, modify, and remove user and system accounts as well as groups.
    Manage group membership.
    Lock and unlock accounts.
    Change user passwords.
    Change a user's properties, such as the default shell.
    Control which files are copied to a new user's home directory during account creation.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        adduser
        passwd
        chpass
        chfn
        chsh
        vipw
        nologin
        id
        groups
        who
        whoami
        su(1)
        /usr/share/skel/
    FreeBSD:
        pw
        rmuser
    NetBSD:
        user
        useradd
        userinfo
        usermod
        userdel
    OpenBSD:
        user
        useradd
        userinfo
        usermod
        userdel
        rmuser

713.2 Automate System Administration Tasks by Scheduling Jobs (weight: 2)

Weight
 2

Description
 
Candidates should understand the location of the periodic system scripts and be able to schedule automated execution of their own commands using cron.

**Key Knowledge Areas:**

    Understand the periodic system scripts.
    Configure which periodic system scripts are run daily, weekly and monthly.
    Manually run a periodic system script.
    Understand the difference between the system crontab and user crontabs, including all available fields.
    Use the crontab editor to create or edit a user crontab.
    Control which users can create their own crontabs.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        crontab
        cron
        crontab
        /var/cron/allow
        /var/cron/deny
    FreeBSD:
        /etc/defaults/periodic.conf
        periodic
    NetBSD:
        /etc/daily.conf
        /etc/weekly.conf
        /etc/monthly.conf
        /etc/security.conf
    OpenBSD:
        daily
        weekly
        monthly

713.3 Maintain System Time (weight: 1)

Weight
 1

Description
 
Candidates should be able to set the system time and use NTP for time synchronization.

**Key Knowledge Areas:**

    Understand the concepts of NTP.
    Configure NTP and manually synchronize with a time server.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        ntpd
        /etc/rc.conf
        date
    FreeBSD:
        /etc/ntp.conf
        ntpq
    NetBSD:
        /etc/ntp.conf
        ntpq
    OpenBSD:
        /etc/ntpd.conf

713.4 System Logging (weight: 2)

Weight
 2

Description
 
Candidates should be able to review system log files and configure log file rotation.

**Key Knowledge Areas:**

    Understand system logging and location of log files.
    View log files, including ongoing and compressed logs.
    Configure log rotation by either time or size.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        newsyslog
        /etc/newsyslog.conf
        /etc/syslog.conf
        tail
        grep
        zgrep
        zless
        zmore
        dmesg
    FreeBSD:
        bzcat
    NetBSD:
        bzcat

713.5 Mail Transfer Agents (MTA) Basics (weight: 1)

Weight
 1

Description
 
Candidates should understand the role of a Mail Transfer Agent and configure aliases and mail forwarding on their local MTA as well as outgoing email using a relay.

**Key Knowledge Areas:**

    Understand the role of a Mail Transfer Agent (MTA).
    Determine which MTA is used on the system.
    Create an email alias for both Sendmail and Postfix.
    Configure Sendmail and Postfix to use a relay for outgoing mail.
    View and flush the mail queue.
    Understand the difference between the mbox and maildir mail destination file format type.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        /etc/mail/aliases
        newaliases
    FreeBSD:
        /etc/mail/mailer.conf
        mailq
    NetBSD:
        /etc/mailer.conf
        postalias
        mailq
        postqueue
    OpenBSD:
        /etc/mailer.conf
        smtpctl

713.6 Manage Printing and Print Jobs (weight: 1)

Weight
 1

Description
 
Candidates should understand how printing on a BSD system works and should be able to review the printing queue and manipulate print jobs.

**Key Knowledge Areas:**

    Understand the BSD lpr printing system.
    Understand the meaning of /etc/printcap entries.
    View the print queue and manipulate the jobs within the queue.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        lpc
        lpq
        lprm
        printcap

713.7 Manage User Sessions (weight: 1)

Weight
 1

Description
 
Candidates should be able to identify which users are currently logged in to a system and review the history of user logins.

**Key Knowledge Areas:**

    Determine who is currently on the system.
    Determine the last time a user was on the system.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        w
        who
        last
        users
    FreeBSD:
        lastlogin
    NetBSD:
        lastlogin
        /var/log/lastlog
    OpenBSD:
        /var/log/lastlog

Topic 714: Basic BSD Network Administration
714.1 Fundamentals of Internet Protocols (weight: 2)

Weight
 2

Description
 
Candidates should understand important network protocols as well as basic IPv4 and IPv6 addressing and subnetting.

**Key Knowledge Areas:**

    Understand IPv4 addressing and subnetting.
    Understand basic IPv6 addressing and subnetting.
    Convert a subnet mask between dotted decimal, hexadecimal, or CIDR notation.
    Determine valid host addresses as well as the subnet address and, for IPv4, the broadcast address of a given network.
    Understand the key features of TCP, UDP and ICMP.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        CIDR
        Prefix and Interface Identifier

714.2 Basic network configuration (weight: 3)

Weight
 3

Description
 
Candidates should be able to configure the IP settings of network interfaces.

**Key Knowledge Areas:**

    Configure IP settings both temporarily and permanently.
    Demonstrate a basic understanding of DHCP leases.
    View the current DHCP lease, release it, and renew a lease.
    Configure a DHCP client to override the settings received from a DHCP server.
    Understand and configure interface aliases.
    Understand IPv6 auto configuration using SLAAC and DHCPv6.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        ifconfig
        route
        hostname
        /etc/hosts
        dhclient
        /etc/dhclient.conf
        /var/db/dhclient.leases
        /etc/rc.conf
    NetBSD:
        /etc/ifconfig.if
        /etc/ifaliases
    OpenBSD:
        netstart
        /etc/hostname.if
        /etc/myname
        /etc/mygate

714.3 Basic network troubleshooting (weight: 3)

Weight
 3

Description
 
Candidates should be able to analyze and resolve simple network connectivity problems.

**Key Knowledge Areas:**

    Determine the current IP configuration of a system.
    Troubleshoot IPv4 and IPv6 connectivity.
    Determine which TCP or UDP ports are open on a system.
    Verify the availability of a TCP/IP service.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        ifconfig
        netstat
        route
        ping
        ping6
        traceroute
        /etc/services
        telnet
        nmap
        nc
    FreeBSD:
        sockstat
        rtsol
    NetBSD:
        sockstat
        rtsol
    OpenBSD:
        /etc/hostname.if

714.4 Configure Client Side DNS (weight: 2)

Weight
 2

Description
 
Candidates should understand the basics of DNS and be able to configure host name resolution.

**Key Knowledge Areas:**

    Understand basic DNS theory, including types of resource records, reverse lookups, and types of DNS servers.
    Query a DNS server for a particular type of resource record.
    Configure name resolution, including the order of host name resolution and recursive DNS server.
    Troubleshoot DNS problems.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        host
        hostname
        /etc/resolv.conf
    FreeBSD:
        drill
        /etc/nsswitch.conf
    NetBSD:
        dig
        nslookup
        /etc/nsswitch.conf
    OpenBSD:
        dig
        nslookup

Topic 715: Basic Unix Skills
715.1 Use the Shell and Work on the Command Line (weight: 2)

Weight
 2

Description
 
Candidates should be able to use and customize a shell and understand the differences between the different shells offered on a BSD system. Candidates should also be able to use manpages.

**Key Knowledge Areas:**

    Understand the differences between the standard shells on BSD systems.
    Be comfortable using the sh, csh, or tcsh shells.
    View and modify environmental variables, both temporarily and permanently.
    Redirect input and output to/from files and commands.
    Use simple and advanced wildcard specifications in commands.
    Understand the manpage sections and use manpages.
    Modify shell behavior both temporarily and permanently, including preventing the shell from clobbering existing files and using history substitution.
    Set command aliases and temporarily bypass a command alias.
    Run a command multiple times with different arguments for each call.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        sh
        csh
        tcsh
        <
        >
        |
        >&
        |&
        tee
        env
        file globbing
         ?
        *
        man
        intro
        less
         !
         !!
        $
        xargs

715.2 Perform basic file management (weight: 3)

Weight
 3

Description
 
Candidates should be able to handle files on a BSD system. This includes identifying the type of files and creating archives of files.

**Key Knowledge Areas:**

    Copy, move, and remove files and directories.
    Recursively copy multiple files and directories.
    Remove files and directories recursively.
    Determine if a file is a binary, text, or data file.
    Using common Unix command line backup utilities.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        cp
        mkdir
        mv
        ls
        rm
        rmdir
        touch
        dd
        tar
        cpio
        pax
        cp
        file

715.3 Create, Monitor and Kill Processes (weight: 3)

Weight
 
Description
 
Candidates should be able to manage processes, including identifying processes with extensive resource usage, prioritizing, and terminating processes.

**Key Knowledge Areas:**

    Monitor the system's workload over the last 1, 5 and 15 minutes.
    Monitor the virtual memory system, including monitoring swapping and paging activity.
    View active processes and recognize inordinate CPU usage.
    Understand the most commonly used Unix signals, including their names.
    Understand the difference between SIGTERM and SIGKILL.
    Send a signal to an active process.
    End a process or change its priority.
    Start a process in the background, place an existing process into the background, verify if any jobs are currently running in the background, and return a background process to the foreground.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        top
        ps
        pgrep
        pstat
        systat
        nice
        renice
        kill
        pkill
        swapctl
        uptime
        w
        vmstat
        Shell built-in commands: &, ^Z, jobs, bg, fg, and kill
    FreeBSD:
        killall

715.4 Use Simple Regular Expressions (weight: 2)

Weight
 2

Description
 
Candidates should be able to use simple regular expressions and wildcards to search text in files and streams.

**Key Knowledge Areas:**

    Match text patterns when analyzing program output or searching through files.
    Specify a range of characters within [], specify a literal, use a repetition operator, recognize a metacharacter, and create an inverse filter.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        grep
        egrep
        fgrep
        re_format(7)

715.5 Perform basic file editing operations (weight: 2)

Weight
 2

Description
 
Candidates should be able to use the vi editor for basic file editing.

**Key Knowledge Areas:**

    Edit files using the vi editor.
    Modify a read-only file or exit vi without saving any edits to the file.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        vi
         :w
         :wq
         :wq!
         :q!
        Dd
        Y
        P
        X
        I
        A
        /
        ZZ
         :set number
         :set list

715.6 Customize or write simple scripts (weight: 2)

Weight
 2

Description
 
Candidate should understand the concept of shell scripting and be able to write simple Bourne shell scripts.

**Key Knowledge Areas:**

    Understand the advantages and disadvantages of using a Bourne shell script rather than a csh or bash shell script.
    Understand the shebang, comments, and script permissions.
    Use positional parameters, special parameters, and wildcards.
    Use quotes and backslashes.
    Use conditions and loops.
    Troubleshoot a script.

**The following is a partial list of the used files, terms and utilities:**

    Common:
        chmod
        stdin
        stdout
        stderr
        for
        while
        if
        case
        exec

Future Change Considerations

Future changes to the objective may include:

    712.1: Add gdisk and reconsider fdisk, disklabel and installboot

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

    This page was last modified on 16 February 2021, at 16:22. About LPI Wiki 
