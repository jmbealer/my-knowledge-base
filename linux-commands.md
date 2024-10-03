---
author: Justin Bealer
date_created: 2024-10-03, 04-27-27
date_modified: 2024-10-03, 04-27-38
reference: 
description: 
aliases: 
tags: 
---
# Linux-commands

## help

commands that give help about a given command
look at tldr

NAME: man [man options] [[section] page ..] .. - an inteface to the system reference manuals
DESCRIPTION: man - is the system's manual pager
EXAMPLES: man ls - display the manual page for the item (program) ls.

NAME: **apropos** - search the manual page names and descriptions
DESCRIPTION: **apropos** - searches the descriptions for instances of keyword.

NAME: **info** [OPTION]... [MENU-ITEM...] - read Info documents
DESCRIPTION: **info** - Read documentation in Info format.

NAME
       which - shows the full path of (shell) commands.

SYNOPSIS
       which [options] [--] programname [...]

DESCRIPTION
       Which takes one or more arguments. For each of its arguments it prints to stdout the full path of the executables that
       would have been executed when this argument had been entered at the shell prompt. It does this by searching for an exe‐
       cutable or script in the directories listed in the environment variable PATH using the same algorithm as bash(1).

       This man page is generated from the file which.texinfo.

NAME
       whereis - locate the binary, source, and manual page files for a command

SYNOPSIS
       whereis [options] [-BMS directory... -f] name...

DESCRIPTION
       whereis locates the binary, source and manual files for the specified command names. The supplied names are first
       stripped of leading pathname components. Prefixes of s. resulting from use of source code control are also dealt with.
       whereis then attempts to locate the desired program in the standard Linux places, and in the places specified by $PATH
       and $MANPATH.

       The search restrictions (options -b, -m and -s) are cumulative and apply to the subsequent name patterns on the command
       line. Any new search restriction resets the search mask. For example,

          whereis -bm ls tr -m gcc

       searches for "ls" and "tr" binaries and man pages, and for "gcc" man pages only.

       The options -B, -M and -S reset search paths for the subsequent name patterns. For example,

          whereis -m ls -M /usr/share/man/man1 -f cal

       searches for "ls" man pages in all default paths, but for "cal" in the /usr/share/man/man1 directory only.

WHATIS(1)                                             Manual pager utils                                             WHATIS(1)

NAME
       whatis - display one-line manual page descriptions

SYNOPSIS
       whatis [-dlv?V] [-r|-w] [-s list] [-m system[,...]] [-M path] [-L locale] [-C file] name ...

DESCRIPTION
       Each  manual  page has a short description available within it.  whatis searches the manual page names and displays the
       manual page descriptions of any name matched.

       name may contain wildcards (-w) or be a regular expression (-r).  Using these options, it may be necessary to quote the
       name or escape (\) the special characters to stop the shell from interpreting them.

       index databases are used during the search, and are updated by the mandb program.  Depending on your installation, this
       may be run by a periodic cron job, or may need to be run manually after new manual pages have been installed.  To  pro‐
       duce an old style text whatis database from the relative index database, issue the command:

       whatis -M manpath -w '*' | sort > manpath/whatis

       where manpath is a manual page hierarchy such as /usr/man.

help
(command) -h | --help | help : to display a brief summary of the cli command
whereis
whatis
which
info
