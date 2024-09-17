---
title: Vimrc
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-50
reference: 
description: 
aliases: 
tags: 
---
# Vimrc
== Initialization

- First, initialize (if defined) the system vimrc (see :version)
- :h vimrc
- $VIMINIT (this is an environment variable)
- $HOME/ .vimrc
- $HOME/ .vim/vimrc
- $EXINIT (this is  an environment variable)
- $HOME/ .exrc
- $VIMRUNTIME/defaults.vim

:h  runtimepath
  a list of directories which will be searched for runtime files
  search order:
    User Home .vim
    Sysadmin folder
    $VIMRUNTIME
    Sysadmin "after" folder
    User Home "after" folder
