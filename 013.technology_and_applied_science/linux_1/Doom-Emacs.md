---
title: Doom-Emacs
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 11-01-03
reference: 
description: 
aliases: 
tags: 
---
# Doom-Emacs

;(unmap! 'normal "s")
;(general-auto-unbind-keys)
(map! ;general-override-auto-enable :nveomr "s"  #'evil-forward-char
      :n "t" 'evil-next-line
      :n "n" 'evil-previous-line
      :n "b" 'evil-forward-char
      :n "s"  'evil-backward-char
      )

Doom Emacs Keymaps

<Space> global leader key

- Ret jump to bookmark
- spc find file in project
- ' resume last search
- * search for symbol in project
- , switch workspace buffer
- . find file
- : M-x
- ; Eval expression
- < switch buffer
- ` switch to last buffer
- u universal argument
- x pop up scratch buffer
- ~ toggle last popup
- X org capture
- <Tab> +workspace
- b +buffer
- c +code
- f +file
- g +git
- h +help
- i +insert
- m +<localleader>
- n +notes
- o +open
- p +project
- q +quit/session
- s +search
- t +toggle
- w +window
