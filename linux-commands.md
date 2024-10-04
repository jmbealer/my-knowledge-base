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

*man* - an inteface to the system reference manuals
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

## Other

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
