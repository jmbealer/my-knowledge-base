---
title: Vim-wip
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 11-01-01
reference: 
description: 
aliases: 
tags: 
---
# Vim-wip
general subjects

## Intro Wip

vim stands for Vi IMproved.

### Notation Wip

[] characters in square brackets are optional.
[count] an optional number that may precede the command to multiply or
iterate the command.
["x] [quotex] an optional register designation  where text can be
stored.
{} curly braces denote part of the command which must appear, but which
can take a number of different values.
{char1-char2} a single character from the range  char1 to char2
  {a-z} is a lowercase letter.
  multiple ranges may be concatenated.
    {a-zA-Z0-9} is any alphanumeric character.
{motion} a command that moves the cursor.
{Visual} a selected text area.
CTRL-{char}
'option' an option, or parameter, that can be set to a value, is enclosed
in single quotes.
"command" a reference to a command that you can type is enclosed in
double quotes.
<!--ID: 1639612872499-->


### Mode Intro Wip

Vim has seven BASIC modes:

Normal mode
  In Normal mode you can enter all the normal editor commands.
  Vim start in Normal mode.
  Normal mode is also called Command mode.
Visual mode
  Similar to Normal mode, but the motion commands extend a highlighted
  area.
  When a non-motion command is used, it is executed on the highlighted
  area.
Select mode
  Typing a printable character delete the selection and starts Insert
  mode.
Insert mode
  In Insert mode the text you type is inserted into the buffer.
Command-line mode
  In Command-line mode you can enter one line of text at the bottom of
  the window.
  Command-line mode is also called Cmdline mode
Ex mode
  Like Command-line mode, but after entering a command you remain in Ex
  mode.
  Very limited editing of the command line.
Terminal-Job mode
  Interacting with a job in a terminal window.
  Type key go to the job and the job output is displayed in the
  terminal window.

There are seven ADDITIONAL modes. These are  variants of the BASIC
modes:

### Mode Switching
### Definitions

basic editing
  starting vim
    vim filename
    vim [option | filename] ..

editing files


vim is modal editor.
  normal mode
  insert mode
  visual mode
  command line mode

vim basic
opening a file
- vim <file>
- :e <file>
saving a file
- :w :write save working file
  :w <file>
  :w! <file> overwrite options
- :up :update save working file
  :up <file>
  :up! <file> overwrite options
closing a file
- :x save working file and exit
- :wq save working file and exit
- ZZ save working file and exit
- :q! exit without saving working file
- :qa exit all open files in the current vim session
vim modes
- normal execute all editor commands
- insert inserting text
- command line executing ex commands
- visual select text and execute vim commands
- select
- ex like command line mode; stay in ex mode
help
:h
:helpgrep
:h 'option'
  :h 'list'

invocation
vim file1 file2
vim +linenumber file

exiting
:q quit
:qa quit all files
:wq write and quit
:q! quit without saving


insert mode
  ctrl-w delete the current word
  ctrl-p auto complete previous word
  ctrl-n auto complete next word
  ctrl-x, ctrl-l auto complete line
  ctrl-t  indent current line
  ctrl-d unindent current line

normal mode; default mode, also called command mode
visual mode
  v enter visual mode
  V visually select current line
  ctrl-v visually select columns



## Cursor Motions Wip

word consist of a sequence of letters, digits and underscores.
WORD consist of a sequence of non-blank character, separated with white
space.

i insert
a append
I insert at first non-blank character
gI insert at first column of line
gi insert at previous position
A append to end of line
o insert at the line below current line
O insert at the line above current line
s delete character under the cursor and enter insert mode
S delete line and enter insert mode
: enter command line mode
/ enter command line mode and search forward
? enter command line mode and search backward



I insert begin of the line
A append end of the line
o new line below
O new line above
w jump to next word
  3w jump 3 words
b jump to previous word
r replace letter
R replace mode
cw change word
  c3w delete next 3 words and enter insert mode
C change line
dw delete word
  d3w delete 3 words
D delete line
3dd delete three lines
3cc change three lines
ciw change inner word
ci( or ci) change inner parentheses
ci[ or ci] change inner brackets
ci{ or ci} change inner brackets
diw delete inner word
ctrl-r redo
% jump to matched bracket
c% change until bracket
10G go to 10th line
  :10 go to 10th line
$ end of line
0 begin of the line
v visual mode
V visual line
ctrl-v visual block
p paste after
P paste before
yi) yank in bracket
yiw yank inner word
. repeat last operation
zz center the screen
> shift right
< shift left
= indent
gg=G indent whole file
ggdG delete whole file




[[vim-anki-wip]]

s b
t j
n k
b w

S B
T }
N {
B W

c-s left
c-t down
c-n up
c-b right

motion: left-right, up-down, text object, pattern searches, marks,
various, using tags, scrolling

N is used to indicate an optional count that can be given before the
command.

left-right motions
these commands move the cursor to the specified column in the current
line.


`h or <Left> or <Ctrl-h> or <Bs>`
  [count] character to the left. exclusive motion.
`l or <Right> or <Ctrl-l> or <Space>`
  [count] character to the right. exclusive motion.
`0`
  To the first character of the line. exclusive motion.
  differs for <Home>
<Home>
  To the first character of the line. exclusive motion.
  differs for 0
^
  To the first non-blank character of the line. exclusive motion.
  Any count is ignored.
$ or <End>
  To the end of the line. inclusive motion.
g_
  To the last non-blank character of the line.
  [count - 1] lines downward inclusive.
g0
g^
gn
g$
|
f{char}
F{char}
t{char}
T{char}
;
.
<!--ID: 1639612872511-->


up-down
these command move to the specified line.

k
j
gk
gj
-


word-motions

`w or b or <S-Right>`
  [count] words forward; exclusive motion.
  remap w to s

`W or B or <C-Right>`
  [count] WORDS forward; exclusive motion.
  remap W to S
`e`
  forward to the end of word; [count] inclusive
`E`
  forward to the end of WORD; [count] inclusive
`s or <S-Left>`
  [count] words backward; exclusive motion.
  remap b to s
`S or <C-Left>`
  [count] WORDS backward; exclusive motion.
  remap B to S
`ge`
  backward to the end of word; [count] inclusive
`gE`
  backward to the end of WORD; [count] inclusive

object-motions



## Scrolling
## Insert
## Change
## Undo
## Repeat
## Visual
## Various
## Recover
