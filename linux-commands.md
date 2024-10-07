---
author: Justin Bealer
date_created: 2024-10-03, 04-27-27
date_modified: 2024-10-04, 03-21-22
reference: 
description: 
aliases: 
tags: 
---
# Linux-commands

## Help

commands that give help about a given command
look at tldr

*man* - an interface to the system reference manuals
*man* ls - display the manual page for the item (program) ls.

*apropos* - search the manual page names and descriptions

*info* - read Info documents

*which* - shows the full path of (shell) commands.

*whereis* - locate the binary, source, and manual page files for a command

*whatis* - display one-line manual page descriptions

help
(command) -h | --help | help : to display a brief summary of the cli command

*ls* - list directory contents
*cd* - change the working directory
*mv* - move (rename) files
*pwd* - print name of current/working directory
*mkdir* - make directories
*rmdir* - remove empty directories
*touch* - change (create) file timestamps
*rm* - remove files or directories
*locate* - find files by name, quickly
*clear* - clear the terminal screen

*who* - show who is logged on
*whoami* - print effective user name
*date* - print or set the system date and time
*cal* - display a calendar
*exit* - cause the shell to exit
*time* - time a simple command or give resource usage
*sudo* - execute a command as another user

*cp* - copy files and directories
*find* - search for files in a directory hierarchy
*du* - estimate file space usage
*grep* - print lines that match a patterns
*awk* - pattern scanning and processing language
*sed* - stream editor for filtering and transforming text
*sort* - sort lines of text files
*uniq* - report or omit repeated lines
*diff* - compare files line by line
*wc* - print newline, word, and byte counts for each file

*>* - redirect standard output
*>>* - append standard output
*<* - redirect standard input
*|* - pipe output to another command
*tee* - read from standard input and write to standard output
*tar* - an archiving utility
*gzip* - compress or expand files
*gunzip* - decompress(expand) files

*zip* - package and compress (archive) files
*unzip* - list, test and extract compressed files from ZIP archive
*scp* - OpenSSH secure file copy
*rsync* - a fast, versatile, remote (and local) file-copying tool
*sftp* - OpenSSH secure file transfer

*wget* - the non-interactive network downloader
*curl* - transfer a URL
*chmod* - change file mode bits
*chown* - change file owner and group
*umask* - get or set the file mode creation mask
*ps* - report a snapshot of the current processes
*top* - display linux processes
*htop* - interactive process viewer
*kill* - terminate a process
*pkill* - look up, signal, or wait for processes based on name and other attributes

*nohup* - run a command immune to hangups, with output to a non-tty
*vmstat* - report virtual memory statistics
*iostat* - report cpu and i/o statistics for devices and partitions
*free* - display amount of free and used memory in the system
*df* - report file system space usage
*sar* - collect, report, or save system activity information
*useradd* - create a new user or update default new user information
*usermod* - modify a user account
*userdel* - delete a user account and related files
*groupadd* - create a new group

*passwd* - change user password
*ping* - send ICMP ECHO_REQUEST to network hosts
*ifconfig* - configure a network interfaces
*netstat* - print network connections, routing tables, interface statistics, masquerade connections, and multicast memberships
*ss* - another utility to investigate sockets
*traceroute* - print the route packets trace to network host
*dig* - DNS lookup utility
*nslookup* - query Internet name servers interactively
*iptables* - administration tool for IPv4/IPv6 packet filtering and NAT
*ip* - linux IPv4 protocol implementation

*apt* - package manager utility (Debian/Ubuntu)
*pacman* - package manager utility (Arch Linux)
*dnf* - package manager utility (Fedora, CentOS, RHEL: replaces yum)
*yum* - package manager utility (Fedora, CentOS, RHEL: older versions)
*zypper* - package manager utility (openSUSE, SUSE)
*flatpak* - build, install and run  flatpak applications and runtimes
*uname* - print system information
*hostname* - show or set the system’s host name

*uptime* - tell how long the system has been running
*id* - print real and effective user and group IDs
*lscpu* - display information about the CPU architecture
*lsblk* - list block devices
*lsmod* - show the status of modules in the linux kernel
*dmesg* - print or control the kernel ring buffer
*su* - run a command with substitute user and group ID
*shutdown* - halt, power off or reboot the machine
*reboot* - power off, reboot, or halt the machine
*systemctl* - control the systemd system and service manager

*mount* - mount a filesystem
*umount* - unmount filesystems
*xargs* - build and execute command lines from standard input
*alias* - define or display aliases
*jobs* - display status of jobs in the current session
*bg* - run jobs in the background
*killall* - kill processes by name
*history* - manipulate the history list
*ssh* - OpenSSH remote login client
*tcpdump* - dump traffic on a network
*watch* - execute a program periodically, showing output fullscreen
*tmux* - terminal multiplexer
*nmap* - network exploration tool and security/port scanner
*strace* - trace system calls and signals

## Other

*appimage* - appimage application package manager
*snap* - snappy application package manager
*service* - run a system v init script
*screen* - Manage multiple terminal sessions from a single window.
*nc* - Open TCP or UDP connections for testing and data transfer.

.deb - debian package
.rpm - redhat package manager
.tgz - compressed tarball
  the "universal" package format for linux

apt - package manager for debian based systems
yum - package manager for redhat based systems
pacman - package manager for arch based systems

shell command
starts with command name - what to do
followed by options - how to do it
followed by arguments - what to do it to

kernel run one process /sbin/init

what is the symbol for directory file type? d
what is the file type for d? directory
what is a directory? a file used to store other files.

what is the symbol for regular file type? -
what is the file type for -? regular file
what is a regular file? includes readable files, images files, binary files, and compressed files.

what is the symbol for symbolic link file type? l
what is the file type for l? symbolic link
what is a symbolic link? points to another files.

what is the symbol for socket file type? s
what is the file type for s? socket
what is a socket? allows for communication between processes.

what is the symbol for pipe file type? p
what is the file type for p? pipe
what is a pipe? allows for communication between processes.

what is the symbol for block file type? b
what is the file type for b? block file
what is a block file? used to communicate with hardware.

what is the symbol for character file type? c
what is the file type for c? character file
what is a character file? used to communicate with hardware.

file type-permissions-hard link count-user owner-group owner-file size-timestamp-filename
