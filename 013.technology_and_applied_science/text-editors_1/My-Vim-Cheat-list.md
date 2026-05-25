
### Insert Mode Commands <inserting>

The following commands can be used to insert new text into the buffer. They can
all be undone and repeated with the "." command.

- a - [N] a
  - Append text after the cursor [N times]
    - Append text after the cursor [count] times.
  - If the cursor is in the first column of an empty line Insert starts there.
  - But not when 'virtualedit' is set!
- A - [N] A
  - Append text at the end of the line [N times].
    - Append text at the end of the line [count] times.
- i - [N] A or \<insert>
  - Insert text before the cursor [N times]. (also: \<Insert>)
    - Insert text before the cursor [count] times.
  - When using CTRL-O IN Insert mode i CTRL-O the count is not supported.
- I - [N] A
  - Insert text before the first non-blank in the line [N times].
    - Insert text before the first non-blank in the line [count] time.
  - When the 'H' flag is present in 'cpoptions' and the line only contains
      blank, insert start just before the last blank.
- gI - [N] gI
  - Insert text in column 1 [N times].
    - Insert text in column 1 [count] times.
- gi - [N] gi
  - Insert text in the same position as where Insert mode was stopped last time
      in the current buffer.
  - This uses the '^ mark.
  - It's different from "\`^i" when the mark is past the end of the line.
  - The position is corrected for inserted/deleted lines, but not for
      inserted/deleted characters.
  - When the :keepjumps command modifier is used the '^ mark won't be changed.
- o - [N] o
  - open a new line below the current line, append text [N times]
    - Begin a new line below the cursor and insert text, repeat [count] times.
  - When '#' flag is in 'cpoptions' the count is ignored.
- O - [N] O
  - open a new line above the current line, append text [N times]
    - Begin a new line above the cursor and insert text, repeat [count] times.
  - When '#' flag is in 'cpoptions' the count is ignored.

### Motion and Operators

- ["x]**c**{motion}
  - change; delete {motion} text [into register x] and start insert.
- ["x]**d**{motion}
  - delete; delete text that {motion} moves over [into register x].
- ["x]**y**{motion}
  - yank; yank {motion} text [into register x]
  - (does not change the text)
- **~**{motion}
  - Switch case of {motion} text.
    - 'tildeop' option
    - Switch case of Nmove text.
  - 'notildeop' option: switch case of the character under the cursor
    - move the cursor to the right.
- **g~**{motion}
  - switch case of {motion} text.
- **gu**{motion}
  - make {motion} text lowercase.
- **gU**{motion}
  - make {motion} text uppercase.
- **!**{motion}{filter} filter {motion} text lines through an external program
    {filter}.
- **=**{motion} filter {motion} lines through an external program give with the
    'equalprg' option.
- **gq**{motion} format the lines that {motion} moves over.
- **gw**{motion} format the lines that {motion} moves over with no cursor movement
- **g?**{motion} ROT13 encode {motion} text.
- **>**{motion} shift {motion} lines one 'shiftwidth' rightwards.
- **<**{motion} shift {motion} lines ones 'shiftwidth' leftwards.
- **zf**{motion} define a fold
- **g@**{motion} call the function set by the 'operatorfunc' option.
-
### Left-Right Motions

- h or `<Left>` or CTRL-H or `<BS>`
  - [count] character to the left. exclusive motion.
- l or `<Right>` `<Space>`
  - [count] character to the right. exclusive motion.
- 0 to the first character of the line. exclusive motion.
- `<Home>` to the first character of the line. exclusive motion.
- ^ to the first non-blank character of the line. exclusive motion.
- $ or `End`
  - to the end of the line. inclusive motion.
  - when a count is given also go [count - 1] lines downward.
- g_ to the last non-blank character of the line and [count - 1] lines downward
    inclusive.
- g0 or g`<Home>`
  - to the first character of the screen line. exclusive motion.
  - when lines wrap ('wrap' on)
- g^ to the first non-blank character of the screen line. exclusive motion.
  - when lines wrap ('wrap' on)
- gm 
  - like "g0", but half a screenwidth to the right (or as much as possible).
- g$ or g`<End>`
  - to the last character of the screen line and [count - 1] screen lines
      downward inclusive.
  - when lines wrap ('wrap' on)
- |
  - to screen column [count] in the current line. exclusive motion.
- f{char}
  - to [count]'th occurrence of {char} to the right.
  - the cursor is placed on {char} inclusive.
- F{char}
  - to the [count]'th occurrence of {char} to the left.
  - the cursor is placed on {char} exclusive.
- t{char}
  - till before [count]'th occurrence of {char} to the right.
  - the cursor is placed on the character left of {char} inclusive.
  - {char} can be entered like with the f command.
- T{char}
  - till before [count]'th occurrence of {char} to the left.
  - The cursor is placed on the character right of {char} exclusive.
  - {char} can be entered like with the f command.
- ;
  - repeat latest f, t, F or T [count] times.
  - cpo-;
- ,
  - repeat latest f, t, F or T in opposite direction [count] times.
  - cpo-;
<!--ID: 1639528993535-->


### Up-Down Motions

- k or `<Up>` or CTRL-P
  - [count] lines upward linewise.
- j or `<Down>` or CTRL-J or `<NL>` or CTRL-N
  - [count] lines downward linewise.
- gk or g`<Up>`
- gj or g`<Down>`
- - (`<minus>`)
- + or CTRL-M or `<CR>`
- _ (`<underscore`)
- G
- `<C-End>`
- `<C-Home>` or gg
- :[range]
- {count}%
- :[range]go[to] [count] [count go] - :go :goto go
<!--ID: 1639528993562-->


### Word Motions <word-motions>

- b (w or `S-Right`)
  - [count] words forward. exclusive motion.
  - cursor N words forward.
- B (W or `C-Right`)
  - [count] WORDS forward. exclusive motion.
  - cursor N WORDS forward.
- e
  - Forward to the end of word [count] inclusive.
  - Does not stop in an empty line.
  - cursor forward to the end of word N.
- E
  - Forward to the end of WORD [count] inclusive.
  - Does not stop in an empty line.
  - cursor forward to the end of WORD N.
- s (b or `S-Left`)
  - [count] words backward. exclusive motion.
  - cursor N words backward.
- S (B or `C-Left`)
  - [count] WORDS backward. exclusive motion.
  - cursor N WORDS backward.
- ge
  - Backward to the end of word [count] inclusive.
  - go backwards to the end of the previous word.
- gE
  - Backward to the end of WORD [count] inclusive.
  - go backwards to the end of the previous WORD.

### Unsorted Commands 

i insert mode
I insert mode line
a append
A append line
Esc exit insert mode and return to normal mode
:w write
:q quit
:wq write and quit
:q! quit without saving
v enter visual mode (from normal mode)
p paste after the cursor
P paste before the cursor
u undo
`<CTRL-r>` redo
; go to next occurrence of the character searched for with f
, go to previous occurrence of the character searched for with f
vi (v)iew (i)nside go into visual mode and highlight everything in the current
target
va (v)iew (a)round same as above but also highlights the specified target
yi (y)ank (i)nside yank everything inside the current target
ya (y)ank (a)round yank as above, but also yanks the target
targets:
  (or) - parentheses
  {or} - curly braces
  [or] - square brackets
  w - (w)ord
  W - (W)ORD
  " - double quotes
  ' - single quotes
di (d)elete (i)nside delete everything inside the current target
da (d)elete (a)round delete everything inside and including the current target
ci (c)hange (i)nside like [di] the enter insert mode
ca (c)hange (a)round like [da] the enter insert mode
dt{character} delete from the cursor up until (but not including) the next
occurrence of {character}
df{character} same as dt, but also includes the character
ct{character} same as dt, but also enter insert mode
cf{character} same as df, but also enter insert mode
/ search (forward) in the file for the next
n find the next occurrence
N find the previous occurrence
? search (backwards) in the file for the next
^ go to first non-blank character in the line
$ go to the last character in the line
0 go to first character in the line, includes blank space
gg go to top file
G go to bottom file
`>>` indent
`<<` outdent, unindent, dedent
x delete character at cursor
dw delete word
d$ or D delete to end of line
$ go to end of text on current line
^ go to beginning of text on current line
0 go to beginning of current line
d2w delete two words
dd delete entire line
2dd delete entire line
U undo changes on entire line
r replace character under cursor
cw changes word 
c$ or C changes to end of line
c2w change two words
50G or :50 go to line 50
/waldo search for "waldo"
n go to next search result
N go to previous search result
?carmen search backwards for "carmen"
ctrl-o jump to previous location (jump back)
ctrl-i jump to next location (jump forward)
% go the matching parentheses or brackets
:%s/bad/good replace bad with good in current line
:%s/hi/bye/g replace hi with bye in entire file
:%s/x/y/gc replace x with y in entire file, prompt for changes
:!ls run shell command ls
v enter visual mode
vw visual select word
vwd or vwx visual select word, then delete word
:w play.rb save current file as "play.rb"
:r hat.rb read in file "hat.rb"
o open new line below
O open new line above
e go to end of word
2e go the end of two words
R enter replace mode
yw yank word
vwy visual select word, the yank
y$ yank to end of current line
set ignorecase or set ic change search settings to ignore case
set noignorecase or set noic change search settings to use case
:e sun.rb open file "sun.rb"
:help w get help for "w" command
:help e get help for "e" command
ge end of previous word
} next paragraph
( previous sentence
) next sentence
yy yank line
:reg or :register show yank register
"0p paste from "0" register
"ap paste from "a" register
ctrl-r " paste from default register in insert mode
ctrl-r 0 paste from 0 register in insert mode
ctrl-r u paste from "a" register in insert mode
:s/cat/dog search for cat replace it with dog
:s/cat/dog/g search for cat replace it with dog whole file
3iYes Yes Yes Yes
* and # find word under cursor
H move to first line of screen
M move to middle line of screen
L move to middle line of screen
ce change rest of current word
<!--ID: 1639528993580-->


### `[Operator][Count][Motion]`

- Operators are actions. These are like verbs of a sentence when "speaking Vim"
  - verbs: the operation you want to take on the text
- Motions provide context to your Operators. These execute the action in a
    particular way.
  - nouns 
- Counts are optional and simply let you put a multiplier to your command and
    motion.

- text objects
  - iw "inner word" (works from anywhere in a word)
  - it "inner tag" (the contents of an HTML tag)
  - i" "inner quotes"
  - ip "inner paragraph"
  - as "a sentence"

- **s** [count] words backwards. exclusive motion.
- **t**
- **n**
- **b** [count] words forward. exclusive motion.

### Notation <notation>

- [] - Characters in square brackets are optional.
- [count] - An optional number that may precede the command to multiply or
    iterate the command.
  - If no number is given, a count of one is used, unless otherwise noted.
  - You can use \<Del> to erase the last digit (N\<Del>).
- ["x] <[quotex]> - An optional register designation where text can be stored.
  - The x is a single character between:
    - 'a' and 'z' or 'A' and 'Z' or '"'
    - Some cases (with the put command) between '0' and '9', '%', '#' or others.
  - The uppercase and lowercase letter designate the same register
  - But the lowercase letter is used to overwrite the previous register contents
  - While the uppercase letter is used to append the previous register contents.
  - Without the ""x" or with """" the stored text is put into the unnamed
      register.
- {}
  - Curly braces denote parts of the command which must appear, but which can
      take a number of different values.
  - The differences between Vim and Vi are also given in curly braces.
- {char1-char2}
  - A single character from the range char1 to char2.
  - For example: {a-z} is a lowercase letter.
  - Multiple ranges may be concatenated.
  - For example: {a-zA-Z0-9} is any alphanumeric character.
- {motion} <movement>
  - A command that moves the cursor.
  - This is used after an operator command to move over the text that is to be
      operated upon.
  - If the motion includes a count and the operator also has a count, the two
      counts are multiplied.
    - For example: "2d3w" deletes six words.
  - The motion can be backwards.
    - For example: "db" to delete to the start of the word.
  - The motion can also be a mouse click.
    - The mouse is not supported in every terminal though.
  - The ":omap" command can be used to map characters while an operator is
      pending.
  - Ex commands can be used to move the cursor.
    - This can be
- {Visual}
- \<character>
- 'c'
- CTRL-{char}
- 'option'
- "command"
<!--ID: 1639528993599-->


### Modes

Vim has seven BASIC modes:

- Normal mode
- Visual mode
- Select mode
- Insert mode
- Command-line mode
- Ex mode
- Terminal-Job mode

There are seven ADDITIONAL modes. These are variants of the BASIC modes:

- Operator-pending mode
- Replace mode
- Virtual Replace mode
- Insert Normal mode
- Terminal-Normal mode
- Insert Visual mode
- Insert Select mode
