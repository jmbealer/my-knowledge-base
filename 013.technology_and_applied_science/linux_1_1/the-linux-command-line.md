---
title: The Linux Command Line
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 11-01-03
reference: 
description: 
aliases: 
tags: 
---
# The Linux Command Line

## Learning the Shell

what is the shell
  the shell is program that take keyboard command and passe them to the
  operating system to carry out.
  Bash is acronym for "Bourne Again SHell"
    bash is an enhanced replacement for sh
  sh the original unix shell program written by Steve Bourne.

terminal emulators interact with the shell; when using GUI
  give us access to the shell.
  also called terminal

GUI is an acronym for graphical user interface

` [me@linuxbox ~] $` is called a shell prompt
  shell prompt appear whenever the shell is ready to accept input
  
pound sign # the terminal session has superuser privileges.
  logged in as the root user or terminal provides superuser
  (administrative) privileges.
  
virtual terminal or virtual consoles
  are terminal sessions running behind the graphical desktop.
  access by pressing C-A-F1 through C-A-F6
  switch from one virtual console to another; A-F1 through F-F6
  
## Navigation

pwd - print name of current working directory
cd - change directory
ls - list director contents

Linux organizes its files in what is called a hierarchical directory
structure.
  this means they are organized in a tree-like pattern of directories
  (sometimes called folders in other systems)
    which may contain files and other directories.
root directory is the first directory in the file system.
  contains files and subdirectories, which contain more files and
  subdirectories and so on.

parent directory is the directory above current working directory
  current working directory is the directory your in now
    subdirectory is the directories below current working directory.
