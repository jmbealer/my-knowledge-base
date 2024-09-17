---
title: Vim Cheatsheet
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 11-01-01
reference: 
description: 
aliases: 
tags: 
---
# Vim Cheatsheet

h[elp] {subject}
sav[eas] {file} save the current buffer under the name {file}
{count}clo[se][!] without {count}: Close the current window. If given close the
{count} window.
[count]K run a program to lookup the keyword under the cursor.
:o file
<!--ID: 1619722547688-->


:help keyword # open help for keyword
:o file       # open file
:saveas file  # save file as
:close        # close current pane

## Insert Mode Commands

Insert
i :: insert before cursor
<!--ID: 1619722547268-->

a :: insert after cursor
<!--ID: 1619722547478-->

I
A
gI
gi
o
O
[count]

i        # insert before the cursor
I        # insert at the beginning of the line
a        # insert (append) after the cursor
A        # insert (append) at the end of the line
o        # append (open) a new line below the current line
O        # append (open) a new line above the current line
ea       # insert (append) at the end of the word
Esc      # exit insert mode

## Cursor Movement

### Motion and Operators

c change
d delete
y yank into register (does not change the text)
g~ swap case
gu make lowercase
gU make uppercase

### Left-right Motions

h [count] characters to the left. exclusive motion.
l [count] characters to the right. exclusive motion.
0 To the first character of the line. exclusive motion.
^ To the first non-blank character of the line. exclusive motion.
$ To the end of the line. When a count is given also go [count -1] lines
downward. inclusive motion.

h        # move cursor left
j        # move cursor down
k        # move cursor up
l        # move cursor right
H        # move to top of screen
M        # move to middle of screen
L        # move to bottom of screen
w        # jump forwards to the start of a word
W        # jump forwards to the start of a word (words can contain punctuation)
e        # jump forwards to the end of a word
E        # jump forwards to the end of a word (words can contain punctuation)
b        # jump backwards to the start of a word
B        # jump backwards to the start of a word (words can contain punctuation)
0        # jump to the start of the line
^        # jump to the first non-blank character of the line
$        # jump to the end of the line
g_       # jump to the last non-blank character of the line
gg       # go to the first line of the document
G        # go to the last line of the document
5G       # go to line 5
fx       # jump to next occurrence of character x
tx       # jump to before next occurrence of character x
}        # jump to next paragraph (or function/block, when editing code)
{        # jump to previous paragraph (or function/block, when editing code)
zz       # center cursor on screen
Ctrl + b # move back one full screen
Ctrl + f # move forward one full screen
Ctrl + d # move forward 1/2 a screen
Ctrl + u # move back 1/2 a screen

## Up-down Motions

## Word Motions

## Unsorted

Editing

r        # replace a single character
J        # join line below to the current one
cc       # change (replace) entire line
cw       # change (replace) to the start of the next word
ce       # change (replace) to the end of the next word
cb       # change (replace) to the start of the previous word
c0       # change (replace) to the start of the line
c$       # change (replace) to the end of the line
s        # delete character and substitute text
S        # delete line and substitute text (same as cc)
xp       # transpose two letters (delete and paste)
.        # repeat last command
u        # undo
Ctrl + r # redo

Marking text (visual mode)

v        # start visual mode, mark lines, then do a command (like y-yank)
V        # start linewise visual mode
o        # move to other end of marked area
O        # move to other corner of block
aw       # mark a word
ab       # a block with ()
aB       # a block with {}
ib       # inner block with ()
iB       # inner block with {}
Esc      # exit visual mode
Ctrl + v # start visual block mode
<!--ID: 1619722547898-->


Visual commands

>       # shift text right
<       # shift text left
y       # yank (copy) marked text
d       # delete marked text
~       # switch case

Cut and paste

yy       # yank (copy) a line
2yy      # yank (copy) 2 lines
yw       # yank (copy) the characters of the word from the cursor position to the start of the next word
y$       # yank (copy) to end of line
p        # put (paste) the clipboard after cursor
P        # put (paste) before cursor
dd       # delete (cut) a line
2dd      # delete (cut) 2 lines
dw       # delete (cut) the characters of the word from the cursor position to the start of the next word
D        # delete (cut) to the end of the line
d$       # delete (cut) to the end of the line
d^       # delete (cut) to the first non-blank character of the line
d0       # delete (cut) to the begining of the line
x        # delete (cut) character

Search and replace

/pattern       # search for pattern
?pattern       # search backward for pattern
\vpattern      # 'very magic' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed)
n              # repeat search in same direction
N              # repeat search in opposite direction
:%s/old/new/g  # replace all old with new throughout file
:%s/old/new/gc # replace all old with new throughout file with confirmations
:noh           # remove highlighting of search matches

Search in multiple files

:vimgrep /pattern/ {file} # search for pattern in multiple files
:cn                       # jump to the next match
:cp                       # jump to the previous match
:copen                    # open a window containing the list of matches
<!--ID: 1619722548120-->


Exiting

:w              # write (save) the file, but don't exit
:w !sudo tee %  # write out the current file using sudo
:wq or :x or ZZ # write (save) and quit
:q              # quit (fails if there are unsaved changes)
:q! or ZQ       # quit and throw away unsaved changes

Working with multiple files

:e file       # edit a file in a new buffer
:bnext or :bn # go to the next buffer
:bprev or :bp # go to the previous buffer
:bd           # delete a buffer (close a file)
:ls           # list all open buffers
:sp file      # open a file in a new buffer and split window
:vsp file     # open a file in a new buffer and vertically split window
Ctrl + ws     # split window
Ctrl + ww     # switch windows
Ctrl + wq     # quit a window
Ctrl + wv     # split window vertically
Ctrl + wh     # move cursor to the left window (vertical split)
Ctrl + wl     # move cursor to the right window (vertical split)
Ctrl + wj     # move cursor to the window below (horizontal split)
Ctrl + wk     # move cursor to the window above (horizontal split)

Tabs

:tabnew or :tabnew file # open a file in a new tab
Ctrl + wT               # move the current split window into its own tab
gt or :tabnext or :tabn # move to the next tab
gT or :tabprev or :tabp # move to the previous tab
<number>gt              # move to tab <number>
:tabmove <number>       # move current tab to the <number>th position (indexed from 0)
:tabclose or :tabc      # close the current tab and all its windows
:tabonly or :tabo       # close all tabs except for the current one
:tabdo command



    :help keyword - open help for keyword
    :saveas file - save file as
    :close - close current pane
    K - open man page for word under the cursor

Cursor movement

    h - move cursor left
    j - move cursor down
    k - move cursor up
    l - move cursor right
    H - move to top of screen
    M - move to middle of screen
    L - move to bottom of screen
    w - jump forwards to the start of a word
    W - jump forwards to the start of a word (words can contain punctuation)
    e - jump forwards to the end of a word
    E - jump forwards to the end of a word (words can contain punctuation)
    b - jump backwards to the start of a word
    B - jump backwards to the start of a word (words can contain punctuation)
    % - move to matching character (default supported pairs: '()', '{}', '[]' - use :h matchpairs in vim for more info)
    0 - jump to the start of the line
    ^ - jump to the first non-blank character of the line
    $ - jump to the end of the line
    g_ - jump to the last non-blank character of the line
    gg - go to the first line of the document
    G - go to the last line of the document
    5G - go to line 5
    fx - jump to next occurrence of character x
    tx - jump to before next occurrence of character x
    Fx - jump to previous occurrence of character x
    Tx - jump to after previous occurrence of character x
    ; - repeat previous f, t, F or T movement
    , - repeat previous f, t, F or T movement, backwards
    } - jump to next paragraph (or function/block, when editing code)
    { - jump to previous paragraph (or function/block, when editing code)
    zz - center cursor on screen
    Ctrl + e - move screen down one line (without moving cursor)
    Ctrl + y - move screen up one line (without moving cursor)
    Ctrl + b - move back one full screen
    Ctrl + f - move forward one full screen
    Ctrl + d - move forward 1/2 a screen
    Ctrl + u - move back 1/2 a screen
    ]m - jump to beginning of next method
    ]M - end of next
    [m - beginning of previous
    [M - end of previous
    g; - position of last edit inside a buffer
<!--ID: 1619722548332-->


Insert mode - inserting/appending text

    Ctrl + o <command> - execute normal-mode command while in insert-mode
    i - insert before the cursor
    I - insert at the beginning of the line
    a - insert (append) after the cursor
    A - insert (append) at the end of the line
    o - append (open) a new line below the current line
    O - append (open) a new line above the current line
    ea - insert (append) at the end of the word
    Esc - exit insert mode

Working with multiple files

    :e file - edit a file in a new buffer
    :bnext or :bn - go to the next buffer
    :bprev or :bp - go to the previous buffer
    :bd - delete a buffer (close a file)
    :ls - list all open buffers
    :sp file - open a file in a new buffer and split window
    :vsp file - open a file in a new buffer and vertically split window
    Ctrl + ws - split window
    Ctrl + ww - switch windows
    Ctrl + wq - quit a window
    Ctrl + wv - split window vertically
    Ctrl + wh - move cursor to the left window (vertical split)
    Ctrl + wl - move cursor to the right window (vertical split)
    Ctrl + wj - move cursor to the window below (horizontal split)
    Ctrl + wk - move cursor to the window above (horizontal split)

Editing

    r - replace a single character
    J - join line below to the current one with one space in between
    gJ - join line below to the current one without space in between
    gwip - reflow paragraph
    cc - change (replace) entire line
    C - change (replace) to the end of the line
    c$ - change (replace) to the end of the line
    ciw - change (replace) entire word
    cw - change (replace) to the end of the word
    s - delete character and substitute text
    S - delete line and substitute text (same as cc)
    xp - transpose two letters (delete and paste)
    u - undo
    Ctrl + r - redo
    . - repeat last command
    :sort - sort all lines
    :sort! - sort in reverse
    :sort u - removes dupes and sort
    :sort i - ignore case
    :sort n - sort numerically

Marking text (visual mode)

    v - start visual mode, mark lines, then do a command (like y-yank)
    V - start line-wise visual mode
    o - move to other end of marked area
    Ctrl + v - start visual block mode
    O - move to other corner of block
    aw - mark a word
    ab - a block with ()
    aB - a block with {}
    ib - inner block with ()
    iB - inner block with {}
    Esc - exit visual mode
<!--ID: 1619722548554-->


Visual commands

    > - shift text right
    < - shift text left
    y - yank (copy) marked text
    d - delete marked text
    ~ - switch case

Registers

    :reg - show registers content
    "xy - yank into register x
    "xp - paste contents of register x

Marks

    :marks - list of marks
    ma - set current position for mark A
    `a - jump to position of mark A
    y`a - yank text to position of mark A

Macros

    **qa** - record macro a
    q - stop recording macro
    @a - run macro a
    @@ - rerun last run macro

Cut and paste

    yy - yank (copy) a line
    2yy - yank (copy) 2 lines
    yw - yank (copy) the characters of the word from the cursor position to the start of the next word
    y$ - yank (copy) to end of line
    p - put (paste) the clipboard after cursor
    P - put (paste) before cursor
    dd - delete (cut) a line
    2dd - delete (cut) 2 lines
    dw - delete (cut) the characters of the word from the cursor position to the start of the next word
    D - delete (cut) to the end of the line
    d$ - delete (cut) to the end of the line
    x - delete (cut) character

Exiting

    :w - write (save) the file, but don't exit
    :w !sudo tee % - write out the current file using sudo
    :wq or x or ZZ - write (save) and quit
    :q - quit (fails if there are unsaved changes)
    :q! or ZQ - quit and throw away unsaved changes
    :wqa - write (save) and quit on all tabs

Search and replace

    /pattern - search for pattern
    ?pattern - search backward for pattern
    \vpattern - 'very magic' pattern: non-alphanumeric characters are interpreted as special regex symbols (no escaping needed)
    n - repeat search in same direction
    N - repeat search in opposite direction
    :%s/bad/good/g - replace all bad with good throughout file
    :%s/bad/good/gc - replace all bad with good throughout file with confirmations
    :28s/bad/good/g - replace all bad with good on line 28
    :6,11s/bad/good/g - replace all bad with goo in lines 6 to 11, including 6 and 11
    :noh - remove highlighting of search matches

Search in multiple files

    :vimgrep /pattern/ {`{file}`}- search for pattern in multiple files
    :cn - jump to the next match
    :cp - jump to the previous match
    :copen - open a window containing the list of matches
<!--ID: 1619722548786-->


Folding

    zf#j - creates a fold from the cursor down # lines
    zf/string - creates a fold from the cursor to string
    zj - moves the cursor to the next fold
    zk - moves the cursor to the previous fold
    zo - opens a fold at the cursor
    zO - opens all folds at the cursor
    zm - increases the foldlevel by one
    zM - closes all open folds
    zr - decreases the foldlevel by one
    zR - decreases the foldlevel to zero — all folds will be open
    zd - deletes the fold at the cursor
    zE - deletes all folds
    [z - move to start of open fold
    ]z - move to end of open fold

Plugins
vim-bookmarks

    mm - add/remove bookmark at current line
    mi - add/edit/remove annotation at current line
    mn - jump to next bookmark in buffer
    mp - jump to previous bookmark in buffer
    ma - show all bookmarks (toggle)
    mc - clear bookmarks in current buffer only
    mx - clear bookmarks in all buffers
    [count]mkk - move up bookmark at current line
    [count]mjj - move down bookmark at current line
    [count]mg - move bookmark at current line to another line

fugitive

    \gs - to show a window that lists changes
    \gb - to show blame
    \gc - to commit staged changes
    \gd - to diff
    \gl - to show log
    cb<space> - after running \gs, allows list, create, or delete branches
    co<space> - after running \gs, allows for switching branches
    + - after running \gs, and the cursor over a file, this will toggle showing file changes
    - - after running \gs, and the cursor over a file, this will toggle staging/unstaging a file
    X - after running \gs, and the cursor over a file, this will discard changes of a file
    - - after running \gs, and the cursor over a commit, this will prompt to push changes to the remote

tmux general shortcut keys

    `k - to clear the terminal window

tmux window navigation

    `<window number> - to toggle between windows
    `w - to toggle between tmux sessions
    `, - to rename a window
    `h - split window horizontal
    `v - split window vertical
    `c - open a new window
    `t - open a new window
    `xy - close the current window
    `<right arrow> - move to the window to the right of the current window
    `<left arrow> - move to the window to the left of the current window
    `<up arrow> - move to the window above the current window
    `<down arrow> - move to the window below the current window

tmux pane navigation

    C-h - move to the pane to the left
    C-l - move to the pane to the right
    C-j - move to the pane above
    C-k - move to the pane below
    
    

normal mode. (typing a letter here doesn't insert text, but rather lets you navigate and manipulate text in various ways)
	gg - beginning of document
	H - beginning of document
	G - end of document
		4G - go to line 4
	b - beginning of previous word
	B - beginnging of previous WORD
	w - next word
	W - next WORD
	e - end of word
	E - end of WORD
	0 - beginning of line
	$ - end of line

	+ - move down by line beginnings
	- - move up by line beginnings

	^ - first non-blank character
	g_ - last non-blank character
	'. - go to last edited line
	'' - previous cursor position

	gi - go to insert mode on previous cursor position
	gx - go to the URL under the cursor
		g:netrw_browserx_viewer can be set to the desired browser
		ga - show info about character under cursor
	Ctrl-G - show line info

	. - repeat previous command

	f - find character on line
		; - repeat
		3fq - third occurrence of 'q'
	F - find character on line, looking backwards
	t - go till the specified character
	T - go till the specified character, looking backwards
	; - repeat last f, F, t or T command
	, - repeat last f, F, t or T command, backwards

	* - next occurrence of word under cursor
	# - previous occurrent of word under cursor

	4| - jump to column 4

	{ - previous empty line
	} - next empty line
	% - go to next matching parenthesis
	) - next sentence
	( - previous sentence
	]] - to next opening brace section
	][ - to next closing brace section
	[[ - backwards to opening brace section
	[] - backwards to closing brace section

	'. - jump to last modified line
	Ctrl-o - retrace movements in file backwards
	Ctrl-i - retract movement in file forwards
	Ctrl-u - up half a page
	Ctrl-d - down half a page

	zz - center screen on cursor
	zt - align top of screen with cursor
	zb - align bottom of screen with cursor

	inplace editing
		r - replace character
		J - join line below to current one

		~ - toggle case
		g~~ - toggle case of line
		g~$ - toggle case until end of line

		Ctrl-A - increment number beneath cursor
		Ctrl-X - decrement number beneath cursor

		== - autoindent
		=% - autoindent within braces

	entering insert mode
		i - insert mode
		I - insert at beginning of line
		s - substitute character (deletes the character under the cursor and goes into insert mode)
		S - subsitute line (same as doing cc)
		C - substitute from cursor to end of line
		a - append after cursor
		A - append at end of line
		o - open (append) new line below
		O - open (append) new line above		

	search
		/ - search
			/hello - search for the word 'hello'
			patterns
				non-greedy match - /http.\{-}
		? - search backwards
		n - repeat search
		N - repeat search in opposite direction
		/\v'.+' - search using 'very magic mode', to avoid having to escape common characters
		/\n\zs[a-z0-9] - use \zs flag to crop selection (in this case omitting the \n from the highlighted search result)	
	
	q/ - show and edit searches in a buffer
	q: - show and edit history of commands

	cc - change entire line
	dd - delete entire line
		4dk - delete 4 lines upwards
	yy - yank line
	yw - yank word
	"zyy - yank line to buffer z
	c - change
	p - paste
	P - paste before cursor
	gp - paste and go to end of text
	gP - paste before cursor and go to end of text
	x - cut
	X - cut before cursor
	D - delete till end of line

	undo and redo
		u - undo
		U - hard undo (back to states before any edits were made)
		Ctrl-r - redo
		g- - go backwards in history tree
		g+ - go forward in history tree
		:earlier 20s

	combining operators, movements and counts
		cw - change word
		ci' - change everything inside quotes
			ci"
			ci<
		cib - change everything inside brackets
		ciB - change everything inside braces
		ct_ - change till underscore
		cT_ - change till underscore (backwards)
		cit - change in tag (XML or HTML)

		dk - delete line above
		3dk - delete the 3 lines above

	switching windows
		Ctrl-ww - switch window
		Ctrl-wh - move cursor to left-hand window
		Ctrl-wj - move cursor to upper window
		Ctrl-wk - move cursor to upper window
		Ctrl-wl - move cursor to right-hand window
		Ctrl-wq - quit window

	switching tabs
		Cmd-shift [ - previous tab
		Cmd-shift ] - next tab

	q - record macro
		qa - record marcro in register 'a'
		do something special
		press q again to stop recording
		16@a - run the macro 16 times
		"ap - paste the contents of the 'a' macro
		:%normal @b - repeat until end of file

	registers (any time you delete or yank text it goes into a register)
		:reg - show contents of registers
		"1p - paste from register 1.

	marks
		:marks - show marks

		lowercase marks (mark positions and jump around in the current file)
			create
				ma
				mb
			jump to
				'a
				'b

		uppercase marks (mark positions and jump around between different files)
			create
				mA
				mB
			jump to
				'A
				'B

		:delm - delete a mark

		jumping to marks
			use ` to move position-wise and ' to move line-wise

			`[ - jump to beginning of last yanked or changed text
			`] - jump to end of last yanked or changed text
			`< - jump to beginning of last visual selection
			`> - jump to end of last visual selection

	tags
		vim will read a 'tags' file automatically

		Ctrl-] - jump to definition
		Ctrl-t - jump back from definition

		g] - list matching tags

		:tag _initInputField - jump the function definition of _initInputField
		:tag /placeholder - jump to tag matching the text 'placeholder'

		:ptag placeholderUrl - open tag in preview window
		:tselect afterSave - select from multiple matching tags
		:tjump url - jump to unique tag, or list non-unique ones

	spell checking
		:set spell
		]s - next spelling mistake
		[s - previous spelling mistake
		z= - bring up list of suggestions for word under cursor
		1z= - replace word with first suggested spelling
		zg - mark word as good in spell list
		zw - mark word as bad in spell list
		
		zug - undo adding as good
		zuw - undo addings as bad

		~/.vim/spell/en.utf-8.add	

	show indentation guides
		set list listchars=tab:»-,trail:·,extends:»,precedes:«
		or
		set listchars=tab:»-,trail:·,extends:»,precedes:«
		or
		set listchars=tab:▸\ ,eol:¬

		set nolist

	set numbers
	set nu
	set nu!

insert mode (lets you insert text into the document)
	:help ins-special-keys

	3iGo - insert "Go" 3 times
	Ctrl-P - autocomplete
	Ctrl-X, Ctrl-O - omnicomplete

	Ctrl-y - duplicate line above, character-by-character
	Ctrl-e - duplicate line below, character-by-character

	Ctrl-t - indent line
	Ctrl-d - unindent line

	Ctrl-r {reg} - insert from register
		Ctrl-r =2+2 - insert '4'
<!--ID: 1619722549016-->


	inserting special characters, digraphs
		Ctrl-K
			Type approximation of the character, e.g.
				a: for ä
				14 for ¼
			:dig to reference these
		Ctrl-V

	editing while in insert mode
		Ctrl-w - delete word before cursor
		Ctrl-u - delete line before cursor
		Ctrl-rx - insert contents of register x
		Ctrl-t - increase line indent
		Ctrl-d - decrease line indent
		
	leaving
		<Esc>
		Ctrl-[

visual mode
	v - start selecting
	V - visual line mode
	vib - select visually within brackets
	viB - select visually within braces
	viW - select visually within word (or URL or filename)
	v2ap - select 2 paragraphs visually
	gv - previous visual selection

	gv - reselect what was previously selected
	= - fix indentation
	
	search within visual selection
		make the selection
		hit escape
		/\%Vwhat_to_search

	visual block mode
		Ctrl-V
		move around to make a selection, e.g - j
		I to insert and type something
		esc to exit the mode and insert the characters

		c - change
		d - delete
		o - toggle to opposite
		I - prepend to each visual block line

command line mode (typing a colon gives you access to many commands)
	Ctrl-b - beginning of command line
	Ctrl-e - end of command line
	Ctrl-w - delete word
	Ctrl-r - insert a register
	Ctrl-r Ctrl-w - insert word from under cursor
	Ctrl-f - edit using normal mode
	@: - repeat previous ex command

	:cd ~/Projects/showstudio/site
		cd %:h - change to the directory of the current file
	:pwd
	:so ~/.vimrc
	:!ls
	:sp a.txt - split window and edit a.txt
	:vsp b.txt

	:enew - edit a new buffer in the current window

	:r - read in a file
		:185r read in line 185

	:w - write a file
		:w test.txt

	set wrap!
	set nowrap
	set wrap

	external command
		:%! markdown - filter buffer via the external 'markdown' command

	ranges
		:15,30d - delete lines 15 - 30
		:15,30m $ - move lines 15 - 30 to the end
		:15,30>> - indent lines 15 - 30

	command history
		: and the up key

	filename
		use a % sign on the command line to denote the current file
		:! echo %
		:so %

		:! markdown % > %:p:r.html
		:help filename-modifiers
	
	search and replace
		:%s/old/new - search and replace (first occurrence in each line)
		:%s/old/new/g - search and replace globally
		:%s/old/new/gc - search and replace with confirmations
		d/pattern - delete 'pattern'
		:5,12s/old/new/g - search and replace within range
		:%s/\s\+$//e - strip whitespace from ends of lines

		:g/test/d - delete all lines that match 'test'
		:g!/test/d - delete all lines that don't match 'test'

	move
		:m 12 - move current line to after line 12
		:m 0 - move current line to before first line
		:m $ - move current line to after last line 
		:m7 - move current line to line 7
		:4m7 - move line 4 to line 7
		:4m$ - move line 4 the end of document
	
	copy
		:3co7 - copy line 3 after line 7
		:3t7 - same as above
		:3t. - copy line 3 to after current line

		:sort - sort lines alphabetically
		:retab
		:changes
		:dig - digraphs
		:color - show current colorscheme

	:%TOhtml - generate HTML page that looks like the current view
	:w !sudo tee % - write current file with sudo, to avoid file permission error

	buffers
		:buffers
		:ls
		:files

		:b3 - display buffer 3
		:bn - next buffer
		:bp previous buffer
		Ctrl-6 - switch between recent buffers
	
		:bd
		:bdel
		:5,999bd

		:%bd - delete all buffers

		:bdel galleries <Ctrl-a> - complete all matches

		status column
			h is hidden
			+ means unsaved changes
	
	args
		:args
		:args ~/Dropbox/documents/unix.txt ~/Dropbox/documents/mac.txt
		:args *.txt
		:args `cat table_of_content.txt`
		:args `find  - -type f`

		argdo
			:args *.txt
			:argdo %s/\a/*/g
			:argdo update

	grep (search across multiple files)
		:vimgrep /pr( **/*.ctp
		:cw
		:cnext
		:cprev



