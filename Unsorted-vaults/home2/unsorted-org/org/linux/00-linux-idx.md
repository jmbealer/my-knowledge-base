# Linux Index

terminal multiplexer
 - tmux
  - automatically tmux package manager installation
    - if "test ! -d ~/.tmux/plugins/tpm" \
   "run 'git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm && ~/.tmux/plugins/tpm/bin/install_plugins'"
  - source-file '~/.tmux.conf'
    - :source-file
    - tmux source-file
  - do something about prefix key
    unbind C-b
    set -g prefix C-q
  - bind-key
 - gnu screen
- file naming
  - only use _ - .
  - Use all-lowercase, and separate words with hyphens.
  - Use only standard ASCII alphanumeric characters in file and directory names.
  - tmux plugins

maybe learn; rsync
- sudo -e {filename} to open file with $EDITOR
- sudoedit {filename}
- changed dpi to 406 in /etc/lightdm/lightdm.conf
[cli-apps](cli-apps.md)
<!--ID: 1639528998433-->


[Vim Index](00-vim-idx.md)
[Nix Commands](Nix-Commands.md)
[Linux test](Linux-test.md)
[Doom Emacs](Doom-Emacs.md)
[LPI Linux Essentials Exam Objectives](LPI-Linux-Essentials-Exam-Objectives.md)
[WIP Linux](WIP-Linux.md)
[LPIC 1 Certified Linux Administrator](LPIC-1-Certified-Linux-Administrator.md)
[LPIC 2 Certified Linux Engineer](LPIC-2-Certified-Linux-Engineer.md)
[LPIC 3 300 Linux Enterprise Professional Mixed Environment Objectives](LPIC-3-300-Linux-Enterprise-Professional-Mixed-Environment-Objectives.md)
[LPIC 3 303 Linux Enterprise Professional Security](LPIC-3-303-Linux-Enterprise-Professional-Security.md)
[LPIC 3 304 Linux Enterprise Professional Virtualization and High Availability](LPIC-3-304-Linux-Enterprise-Professional-Virtualization-and-High-Availability.md)
[[qtile| Qtile]]
replace ls with exa
[fish](fish.md)
pacman -Rs packagename

fc-list | grep -i iosveka

* Operating System
* Learn to live in Terminal
** Learn Bash Scripting
** Vim/Nano/PowerShell/Emacs
** Compiling apps from source (gcc, make and other related stuff)
** System Performance
*** nmon, iostat, sar, vmstat
** Others
*** strace, dtrace, systemtap, uname, df, history
** Text Manipulation Tools
*** awk, sed, grep, sort, uniq, cat, cut, echo, fmt, tr, nl, egrep, fgrep, wc
** Process Monitoring
*** ps, top, htop, atop, isof
** Network
*** nmap, tcpdump, ping mtr, traceroute, dig, airmon, airodump, dig, iptables,
    netstat
** terminal multiplexers
*** tmux
*** screen
W
xrandr --dpi
HiDPI arch wiki

nvim-lspconfig
starship

  #linux
