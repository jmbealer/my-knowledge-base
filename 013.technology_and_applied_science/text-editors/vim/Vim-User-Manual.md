---
title: Vim-User-Manual
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-01
reference: 
description: 
aliases: 
tags: 
---
# Vim-User-Manual
= Vim User Manual

user-manual: These files explain how to accomplish an editing task.

== Getting Started

* *Notation*
** *[]* - Characters in square brackets are optional.
** *[count]* - An optional number that may precede the command to multiply or
iterate the command.
*** If no number is given, a count of one is used, unless otherwise noted.
*** You can use <Del> to erase the last digit (N<Del>).
** *["x]* *[quotex]* - An optional register designation where text can be stored.
*** The x is a single character between 'a' and 'z' or 'A' and 'Z' or '"'
**** And in some cases (with the put command) between '0' and '9', '%', '#', or
others.
*** The uppercase and lowercase letter designate the same register,
**** but the lowercase letter is used to overwrite the pervious register contents,
**** while the uppercase letter is used append to the previous register contents.
*** Without the ""x" or with """" the stored text is put into the unnamed
register.
** *{}*
** *{char1-char2}*
** *{motion}*
** *{Visual}*
** *<character>*
** *'c'*
** *CTRL-{char}*
** *'option'*
** *"command"*
<!--ID: 1639528993499-->


* ctrl-] and ctrl-o
* normal, _italic_, *bold*, +mono+
* bold *constrained* & **un**constrained *con*
* x
* undo and redo

== Editing Effectively

== Tuning Vim

== Reference Manual
