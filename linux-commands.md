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
  chmod [<set><action><permissions>]... file
  set
    u - user: the user who owns the file.
    g - group: the group who owns the file.
    o - others: anyone other than the user owner or member of the group owner.
    a - all: refer to the user, group and others.
  action
    + - add the permission, if necessary.
    = - specify the exact permission.
    - - remove the permission, if necessary.
  permissions
    r - read
    w - write
    x - execute
  add execute permission for the user owner: chmod u+x file
*chown* - change file owner and group
  change ownership to root: chown root file
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
  shutdown now
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

cat
more
less
head
tail
dd

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

what are ls information fields? file type-permissions-hard link count-user owner-group owner-file size-timestamp-filename

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

what is permissions? access control for files and directories
what is the permissions order? user-group-others
what is the permission symbol for read? r
what is the permission symbol for write? w
what is the permission symbol for execute? x
read (r) allows for file contents to be read or copied
write (w) allows for file contents to be modified or overwritten.  allows for
files to be added or removed from a directory.
execute (x) allows for a file to be run as a process, although script file
require read permission as well

regular expressions
basic regex characters:
. - any one single character
[ ] - any one specified character
[^ ] - not the one specified character
* - zero or more of the previous character
^ - if first character in the pattern, then pattern must be at beginning of
the line to match, otherwise just a literal ^
$ - if last character in the pattern, then pattern must be at the end of the
line to match, otherwise just a literal $
extended regex characters:
* - one or more of the previous pattern
? - the preceding pattern is optional
{ } - specify minimum, maximum or exact matches of the previous pattern
| - alternation - a logical "or"
( ) used to create groups

passwd field order: username:password status:change date:minimum:maximum:warn:inactive
field: example: meaning
user name: sysadmin: the name of the user
password status: P: P indicates a usable password, L indicates a locked password, NP indicates no password
change date: 03/01/2015: the date when the password was last changed
minimum: 0: the minimum number of days that must pass before the current
password can be changed by the user.
maximum: 99999: the maximum number of days remaining for the password to expire.
warn: 7: the number of days prior to password expiry that the user is warned.
inactive: -1: the number of days after password expiry that the user account remain active.

standard input (stdin) - is the information the command receives and processes
when it is executed, essentially what a user types on the keyboard.
standard output (stdout) - is the information that the command displays, the
output of the command
standard error (stderr) - is the error messages generated by commands that are
not correctly executed.

### NDG Linux Essentials - Chapter 2

Android
    A Linux distribution that provides a platform for mobile users but lacks the traditional GNU/Linux packages to make it compatible with desktop Linux distributions.
    Section 2.4.1
CentOS
    A Linux distribution that is compatible with Red Hat Enterprise Linux but does not offer the paid support that Red Hat does.
    Section 2.4.1
Debian
    An operating system that uses the Linux kernel. It that promotes the use of open source software and adherence to standards.
    Section 2.4.1
Linux Mint
    A Linux distribution that is a derivative of Ubuntu and still relies upon the Ubuntu repositories.
    Section 2.4.1
Raspberry Pi
    A hardware platform used in training for programmers and hardware designers at all levels. Its low cost and ease of use have made it popular with educators.
    Section 2.4.1
Raspbian
    A specialized Linux distribution optimized to run on Raspberry Pi hardware.
    Section 2.4.1
Red Hat
    A Linux distribution that introduced Red Hat Package Manager (RPM). The developer formed a company by the same name which specializes in open source software.
    Section 2.4.1
SUSE
    One of the first comprehensive Linux distributions. It is derived from Slackware which offers many similarities with Red Hat Enterprise Linux.
    Section 2.4.1
Scientific Linux
    A specific use distribution based on Red Hat. It was designed to enable scientific computing.
    Section 2.4.1
Ubuntu
    The most popular Debian derived distribution. It has several different variants for desktop, server, and various specialized applications as well as an LTS version.
    Section 2.4.1
beta
    A software release that has many new features that haven’t been tested.
    Section 2.1.1
command line interface (CLI)
    A text based interface in which the user enters commands. Feedback, output and programs are presented in text format only.
    Section 2.1.1
desktop configuration
    Desktop are preferred if the user interacts with the system directly. Desktop system primarily run a GUI for the ease of use of its user.2.1.1
    Section 2.1.1
graphical user interface (GUI)
    A visual user interface that allows the user to interact with the system using windows, icons, a cursor, etc.
    Section 2.1.1
long-term support (LTS)
    Associated with the life cycle of distributions, this feature states that software is supported for 5 years or more.
    Section 2.4
maintenance cycles
    The period of time vendors support older versions of software before not offering any updates.
    Section 2.1.1
openSUSE
    A Linux distribution that is a completely open, free version of SUSE Linux Enterprise with multiple desktop packages similar to CentOS and Linux Mint.
    Section 2.4.1
stable
    A software release whose updates have been tested in the field.
    Section 2.1.1

### NDG Linux Essentials - Chapter 3 - Working in Linux

Apache HTTPD
    Apache HTTPD is a server application program, or daemon, that manages web page requests on an Apache web server.
    Section 3.2.2.1
C
    A compiled computer programming language. C is the language in which Linux is written.
    Section 3.5
Firefox
    An open source, cross-platform web browser developed by the Mozilla Foundation.
    Section 3.2.3.4
GIMP
    An open source application which handles 2D image manipulation.
    Section 3.2.3.2
Java
    A compiled, object-oriented programming language owned by Oracle.
    Section 3.5
JavaScript
    A cross-platform scripting language for adding interactive elements to web pages, that is in wide use across the internet.
    Section 3.5
LibreOffice
    An open source office suite forked from Open Office. It includes tools that strive for compatibility with Microsoft Office in both features and file formats.
    Section 3.2.3.3
MariaDB
    An open source database application forked from MySQL. It records data written to it by dynamic web applications.
    Section 3.2.2.3
MySQL
    A relational database management system used for web development.
    Section 3.2.2.3
NFS
    The native file sharing protocol for Unix and Linux. Short for Network File System.
    Section 3.2.2.5
NGINX
    An open source web server based out of Russia focused on the use of more modern UNIX kernels.
    Section 3.2.2.1
Nextcloud
    An open source private cloud server software forked from ownCloud. It is provided under a GNU AGPLv3 that can be deployed and administered internally by an organization.
    Section 3.2.2.2
OpenOffice.org
    An open source office suite which has been discontinued.
    Section 3.2.3.3
PHP
    A scripting language designed to create dynamic web pages.
    Section 3.5
Perl
    An interpreted programming language popular with system adminsitrators. It was orginally developed to perform text manipulation.
    Section 3.5
Python
    A scripting language which simplifies complex tasks, has excellent statistical processing, and it popular in academia.
    Section 3.5
Samba
    A file sharing application ideal for use with Windows systems.
    Section 3.2.2.5
Thunderbird
    A full-featured, open source desktop email client developed by the Mozilla Foundation.
    Section 3.2.3.1
apt-get
    A front-end program for Debian package management.
    Section 3.4.1
console
    Traditionally used to refer to a physical terminal.
    Section 3.1.1
dpkg
    The package management system used on Debian derived Linux distributions.
    Section 3.4.1
ownCloud
    An open source file hosting service. The project was launched in 2010 by Frank Karlitschek to provide software to store, sync and share data from private cloud servers.
    Section 3.2.2.2
password issues

    Section 3.6.1 
privacy issues and tools

    Section 3.6.2 
rpm
    The package management system used on Red Hat derived Linux distributions. According to the Linux Standards Base, the standard package management system is RPM.
    Section 3.4.2
shell
    The user interface of a Linux system. It interacts with the user by accepting commands, passes them to the kernel for execution, and displays any output to the terminal.
    Section 3.3.1
terminal
    The environment or device in which the user interacts with the software. It can also refer to a graphical program which emulates a console.
    Section 3.1.1
use of common open source applications in presentations and projects

    Section 3.2.3.3 
using a browser, privacy concerns, configuration options, searching the web and saving content

    Section 3.6.2 
yum
    A front-end tool for RPM package management.
    Section 3.4.2

### NDG Linux Essentials - Chapter 4 - Open Source Software and Licensing

BSD
    An open source license which states that you may redistribute the source software and binaries as long as copyright notices are maintained and there is no implication that the original creator endorses your version. Short for Berkley Software Distribution.
    Section 4.2.2
Creative Commons
    An organization created to address the intentions behind FOSS licenses for non-software entities.
    Section 4.2.3
FLOSS
    Free/Libre/Open Source Software (FLOSS) is a collective term for the open source community which uses the term libre to define the difference between free from restrictions on software usage (libre) and free from cost (free).
    Section 4.2.2
FOSS
    An open source body called Free Open Source Software (FOSS) which consists of both Free Software and Open Source as a collective in order to downplay the differences between the two organizations.
    Section 4.2.2
Free Software
    The freedom to share, study and modify the underlying source code of the software.
    Section 4.2.1
GPL
    Licenses developed by FSF that are meant to be included in the source code to ensure that all future variants and modifications of the original program continue to have the same freedom of use as the original. Short for GNU General Public Licenses.
    Section 4.2.1
Open Source Software
    Software that meets the OSI Open Source software guidelines where no restrictions are placed on the use of the software regardless of the intended use.
    Section 4.2.2
copyleft
    A philosophy held by the Free Software Foundation (FSF) that someone who modifies free software should be required to share any changes they have made.
    Section 4.2.1
open source business models

    Section 4.3 
permissive
    Open source licenses that do not contain copyleft provisions and therefore are more permissive in how they allow software to be redistributed.
    Section 4.2.2

### NDG Linux Essentials - Chapter 5 - Command Line Skills

Bash
    The most commonly used shell for Linux distributions.
    Section 5.2
PATH environment variable
    Variable containing a list that defines which directories the shell looks in for commands.
    Section 5.4.3
echo
    Command that displays output in the terminal.
    Section 5.4.1
export
    Command that turns a local variable into an environment variable.
    Section 5.4.2
history
    Command that outputs a list of previously executed commands.
    Section 5.3.3
type
    Command that determines information about command type.
    Section 5.5
