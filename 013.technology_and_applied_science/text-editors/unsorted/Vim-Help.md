---
title: Vim-Help
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-01
reference: 
description: 
aliases: 
tags: 
---
# Vim-Help
= Vim Help

.Get specific help
|===
|What |Prepend |Example
|Normal mode command |Prepend |:help x
|Visual mode command |v_ |:help v_u
|Insert mode command |i_ |:help i_<Esc>
|Command-line command |: |:help :quit
|Command-line editing |c_ |:help c_<Del>
|Vim command argument |- |:help -r
|Option |' |:help 'textwidth'
|Regular expression |/ |:help /[
|===

Search for help: type ":help word" the hit ctrl-D to see matching help entries
for "word". Or use ":helpgrep word"
