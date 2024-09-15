# Vim Quick Reference Guide

N is used to indicate an optional count that can be given before the
command.

## motions

### left-right motions

[N]h left
  [N]<Ctrl-h> left
[N]l right
0 to first character in the line
^ to first non-blank character in the line
[N]$ to last character in the line
  N-1 lines lower
g0 to first character in the screen line
  differs from 0 when lines wraps
g^ to first non-blank character in the screen line
  differs from ^ when lines wraps
g$ to last character in the screen line
  differs from $ when lines wraps
gm
  to middle of the screen line
gM
  to middle of the line
[N]|
  to column N; default 1
[N]f{char}
  to the Nth occurrence of {char} to the right
[N]F{char}
  to the Nth occurrence of {char} to the left
[N]t{char}
  till before the Nth occurrence of {char} to the right
[N]T{char}
  till before the Nth occurrence of {char} to the left
[N];
  repeat the last "f", "F", "t", or "T" N times
[N],
  repeat the last "f", "F", "t", or "T" N times in opposite direction
<!--ID: 1639612872570-->


### up-down motions

[N]k
  up N lines
[N]j
  down N lines
[N]-
  up N lines, on the first non-blank character
[N]+
  down N lines, on the first non-blank character
[N]_
  down N-1 lines, on the first non-blank character
[N]G
  goto line N, on the first non-blank character; default last line
[N]gg
  goto line N, on the first non-blank character; default first line
[N]%
  goto line N percentage down in the file;
  N must be given, otherwise it is the % command
[N]gk
  up N screen line
  differs from k when line wraps
[N]gj
  down N screen lines
  differs from j when line wraps


### text objects motions

w 
  N words forward
W
  N blank-separated WORDs forward
e
  forward to the end of the Nth word
E
  forward to the end of the Nth blank-separated WORD
b
  N words backward
B
  N blank-separated WORDs backward
ge
  backward to the end of the Nth word
gE
  backward to the end of the Nth blank-separated WORD

)
(

### pattern searches
### mark and motions

scrolling

## insert

### inserting text

a
  append text after the cursor; N times
A
  append text at the end of the line; N times
i
  insert text before the cursor; N times
I
  insert text before the first non-blank in the line; N times
gI
  insert text in column 1; N times
o
O
`:star[tinsert][!]`
`:startr[eplace][!]`

### Keys
### Special keys
### Digraphs
### Special inserts

change
visual
text objects
repeating command
ky mapping
abbreviations
options
undo/redo commands
