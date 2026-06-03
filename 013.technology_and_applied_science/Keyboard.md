- essential shortcuts #Shortcuts
    - File Management
        - {{Open File...}}- {{control o}} 
        - {{Save}}- {{control s}} 
        - {{Save As...}}- {{control shift s}} 
    - General
        - {{Print}}- {{control p}} 
        - {{Select all}}- {{control a}} 
        - {{Search}}- {{control f}} 
    - Basic Editing
        - {{Cut selection}}- {{control x}} 
        - {{Copy selection}}- {{control c}} 
        - {{Paste}}- {{control v}} 
        - {{Replace}}- {{control h}} 
        - {{Paste without formatting}}- {{control shift v}} 
        - {{Undo}}- {{control z}} 
        - {{Redo}}- {{control y}} 
    - 
    - 
    - 
- terminal shortcuts #Shortcuts
    - 
    - terminal cursor
        - {{Go to beginning of command line}}- {{control  a }} 
        - {{Go to end of command line}}- {{control  e}} 
        - {{Move back one character}}- {{control  b}} 
        - {{Move forward one character}}- {{control  f}} 
        - {{Move cursor forward one word}}- {{alt f}} 
        - {{Move cursor back one word}}- {{alt b}} 
        - {{Toggle between current cursor position and beginning of the line (Bash)}}- {{control  x control x}} 
    - terminal control
        - {{Clears the Screen}}- {{control  l}} 
        - {{Pause terminal output}}- {{control  s }} 
        - {{Resume terminal output after it was paused}}- {{control  q }} 
    - terminal editing
        - {{Undo last action}}- {{control  shift -(}} 
        - {{Swap the last two characters before the cursor}}- {{control  t}} 
        - {{Swap current word with previous}}- {{alt t}} 
        - {{Delete backward to the beginning of the current word}}- {{control  w }} 
        - {{Delete the character after the current cursor position or exit shell}}- {{control  d}} 
        - {{Paste whatever was cut by the last cut command}}- {{control  y}} 
        - {{Delete to the beginning of the line}}- {{control  u}} 
        - {{Delete to the end of the line}}- {{control  k}} 
    - terminal history
        - {{Search command history}}- {{control  r}} 
        - {{View previous command in the history}}- {{control  p}} 
        - {{View next command in the history}}- {{control  n}} 
    - terminal processes
        - {{Puts current process into a suspended background process}}- {{control  z}} 
        - {{Kill the currently running process}}- {{control  c}} 
    - 
- vimium shortcuts #Shortcuts
    - "Description","Keys","Context","Category","Conf.","Actions"
    - Navigating the page
        - {{Scroll down}},{{j or ctrl+e}}
        - {{Scroll up}},{{k or ctrl+y}}
        - {{Scroll to the top of the page}},{{gg}}
        - {{Scroll to the bottom of the page}},{{shift+g}}
        - {{Scroll a half page down}},{{d}}
        - {{Scroll a half page up}},{{u}}
        - {{Scroll left}},{{h}}
        - {{Scroll right}},{{l}}
        - {{Scroll all the way to the left}},{{zH}}
        - {{Scroll all the way to the right}},{{zL}}
        - {{Reload the page}},{{r}}
        - {{Copy the current URL to the clipboard}},{{yy}}
        - {{Open the clipboard's URL in the current tab}},{{p}}
        - {{Open the clipboard's URL in a new tab}},{{shift+p}}
        - {{Go up the URL hierarchy}},{{gu}}
        - {{Go to root of current URL hierarchy}},{{gU}}
        - {{Enter insert mode}},{{i}}
        - {{Enter visual mode}},{{v}}
        - {{Enter visual line mode}},{{shift+v}}
        - {{Focus the first text input on the page}},{{gi}}
        - {{Open a link in the current tab}},{{f}}
        - {{Open a link in a new tab}},{{shift+f}}
        - {{Open multiple links in a new tab}},{{alt+f}}
        - {{Copy a link URL to the clipboard}},{{yf}}
        - {{Follow the link labeled previous or <}},{{[[}}
        - {{Follow the link labeled next or >}},{{]]}}
        - {{Select the next frame on the page}},{{gf}}
        - {{Select the page's main/top frame}},{{gF}}
        - {{Create a new mark}},{{m}}
        - {{Go to a mark}},{{`}}
    - Using the vomnibar
        - {{Open URL, bookmark or history entry}},{{o}}
        - {{Open URL, bookmark or history entry in a new tab}},{{shift+o}}
        - {{Open a bookmark}},{{b}}
        - {{Open a bookmark in a new tab}},{{shift+b}}
        - {{Search through your open tabs}},{{shift+t}}
        - {{Edit the current URL}},{{ge}}
        - {{Edit the current URL and open in a new tab}},{{gE}}
    - Using find
        - {{Enter find mode}},{{/}}
        - {{Cycle forward to the next find match}},{{n}}
        - {{Cycle backward to the previous find match}},{{shift+n}}
    - Navigating history
        - {{Go back in history}},{{shift+h}}
        - {{Go forward in history}},{{shift+l}}
    - Manipulating tabs
        - {{Create new tab}},{{t}}
        - {{Go one tab left}},{{shift+j}}
        - {{Go one tab right}},{{k}}
        - {{Go to previously-visited tab}},{{^}}
        - {{Go to the first tab}},{{g0}}
        - {{Go to the last tab}},{{g$}}
        - {{Duplicate current tab}},{{yt}}
        - {{Pin or unpin current tab}},{{alt+p}}
        - {{Mute or unmute current tab}},{{alt+m}}
        - {{Close current tab}},{{x}}
        - {{Restore closed tab}},{{shift+x}}
        - {{Move tab to new window}},{{shift+w}}
        - {{Move tab to the left}},→
        - {{Move tab to the right}},
        - "Move tab to the left","""←"""
        - "Move tab to the right","""→"""
    - Miscellaneous
        - {{Show help}},{{?}}
        - {{View page source}},{{gs}}
        - 
- vim shortcuts #Shortcuts
    - Vim Global
        - open help for keyword:::h keyword
        - save file as:::sav file
        - open a terminal window:::ter
        - close current pane:::clo
        - open man page for word under the cursor::K
    - Vim Cursor movement
        - jump to next occurrence of character x::fx
        - move to bottom of screen::L
        - jump to the first non-blank character of the line::^
        - jump to the end of the line::$
        - jump to next paragraph (or function/block, when editing code)::}
        - move cursor up::k
        - jump forwards to the start of a word::w
        - jump forwards to the end of a word::e
        - jump backwards to the start of a word::b
        - move cursor left::h
        - move cursor down::j
        - move to top of screen::H
        - move to middle of screen::M
        - move cursor right::l
        - move to matching character (default supported pairs: '()', '{}', '[]'  use :h matchpairs in vim for more info)::%
        - jump forwards to the start of a word (words can contain punctuation)::W
        - jump to the start of the line::0
        - go to the last line of the document::G
        - go to line 5::5gg
        - jump to before next occurrence of character x::tx
        - jump to previous occurence of character x::Fx
        - jump to after previous occurence of character x::Tx
        - repeat previous f, t, F or T movement, backwards::,
        - jump to previous paragraph (or function/block, when editing code)::{
        - jump forwards to the end of a word (words can contain punctuation)::E
        - jump backwards to the start of a word (words can contain punctuation)::B
        - jump to the last non-blank character of the line::g_
        - go to the first line of the document::gg
        - repeat previous f, t, F or T movement::;
        - center cursor on screen::zz
        - move screen down one line (without moving cursor)::control e
        - move screen up one line (without moving cursor)::control y
        - move back one full screen::control b
        - move forward one full screen::control f
        - move forward 1/2 a screen::control d
        - move back 1/2 a screen::control u
    - Vim Insert mode
        - insert before the cursor::i
        - insert at the beginning of the line::I
        - append after the cursor::a
        - append at the end of the line::A
        - open a new line below the current line::o
        - open a new line above the current line::O
        - append at the end of the word::ea
        - delete the character before the cursor during insert mode::control h
        - delete word before the cursor during insert mode::control w
        - begin new line during insert mode::control j
        - indent (move right) line one shiftwidth during insert mode::control t
        - de-indent (move left) line one shiftwidth during insert mode::control d
        - insert (auto-complete) next match before the cursor during insert mode::control n
        - insert (auto-complete) previous match before the cursor during insert mode::control p
        - exit insert mode::escape
    - Vim Editing
        - {{replace a single character}},{{r}}
        - {{join line below to the current one with one space in between}},{{J}}
        - {{join line below to the current one without space in between}},{{gJ}}
        - {{reflow paragraph}},{{gwip}}
        - {{switch case up to motion}},{{g~}}
        - {{change to lowercase up to motion}},{{gu}}
        - {{change to uppercase up to motion}},{{gU}}
        - {{change (replace) entire line}},{{cc}}
        - {{change (replace) to the end of the line}},{{C}}
        - {{change (replace) to the end of the line}},{{c$}}
        - {{change (replace) entire word}},{{ciw}}
        - {{change (replace) to the end of the word}},{{cw}}
        - {{delete character and substitute text}},{{s}}
        - {{delete line and substitute text (same as cc)}},{{S}}
        - {{transpose two letters (delete and paste)}},{{xp}}
        - {{undo}},{{u}}
        - {{restore (undo) last changed line}},{{U}}
        - {{redo}},control {{r}}
        - {{repeat last command}},{{.}}
    - Vim Marking text (visual mode)
        - {{start visual mode, mark lines, then do a command (like y-yank)}},{{v}}
        - {{start linewise visual mode}},{{V}}
        - {{move to other end of marked area}},{{o}}
        - {{start visual block mode}},control {{v}}
        - {{move to other corner of block}},{{O}}
        - {{mark a word}},{{aw}}
        - {{a block with ()}},{{ab}}
        - {{a block with {}}},{{aB}}
        - {{a block with}}―{{ tags}},{{at}}
        - {{inner block with ()}},{{ib}}
        - {{inner block with {}}},{{iB}}
        - {{inner block with}}―{{ tags}},{{it}}
        - {{exit visual mode}},{{esc}}
    - Vim Visual commands
        - {{shift text right}},{{>}}
        - {{shift text left}},{{<}}
        - {{yank (copy) marked text}},{{y}}
        - {{delete marked text}},{{d}}
        - {{switch case}},{{~}}
        - {{change marked text to lowercase}},{{u}}
        - {{change marked text to uppercase}},{{U}}
    - Vim Registers
        - {{show registers content}},{{:reg}}
        - {{yank into register x}},{{xy""}}
        - {{paste contents of register x}},{{xp""}}
        - {{yank into the system clipboard register}},{{+y""}}
        - {{paste from the system clipboard register}},{{+p""}}
    - Vim Marks and positions
        - {{list of marks}},{{:marks}}
        - {{set current position for mark A}},{{ma}}
        - {{jump to position of mark A}},{{`a}}
        - {{yank text to position of mark A}},{{y`a}}
        - {{go to the position where Vim was previously exited}},{{`0}}
        - {{go to the position when last editing this file}},{{`""}}
        - {{go to the position of the last change in this file}},{{`.}}
        - {{go to the position before the last jump}},{{`}}{{`}}
        - {{list of jumps}},{{:ju}}
        - {{go to newer position in jump list}},control {{i}}
        - {{go to older position in jump list}},control {{o}}
        - {{list of changes}},{{:changes}}
        - {{go to newer position in change list}},{{g,}}
        - {{go to older position in change list}},{{g;}}
        - {{jump to the tag under cursor}},control {{]}}
    - Vim Macros
        - {{record macro a}},{{qa}}
        - {{stop recording macro}},{{q}}
        - {{run macro a}},{{@a}}
        - {{rerun last run macro}},{{@@}}
    - Vim Cut and paste
        - {{yank (copy) a line}},{{yy}}
        - {{yank (copy) 2 lines}},{{2yy}}
        - {{yank (copy) the characters of the word from the cursor position to the start of the next word}},{{yw}}
        - {{yank (copy) to end of line}},{{y$}}
        - {{put (paste) the clipboard after cursor}},{{p}}
        - {{put (paste) before cursor}},{{P}}
        - {{delete (cut) a line}},{{dd}}
        - {{delete (cut) 2 lines}},{{2dd}}
        - {{delete (cut) the characters of the word from the cursor position to the start of the next word}},{{dw}}
        - {{delete (cut) to the end of the line}},{{D}}
        - {{delete (cut) to the end of the line}},{{d$}}
        - {{delete (cut) character}},{{x}}
    - Vim Indent text
        - {{indent (move right) line one shiftwidth}},―
        - {{de-indent (move left) line one shiftwidth}},―
        - {{indent a block with () or {} (cursor on brace)}},{{>%}}
        - {{indent inner block with ()}},{{>ib}}
        - {{indent a block with}}―{{ tags}},{{>at}}
        - {{re-indent 3 lines}},{{3}}―
        - {{re-indent a block with () or {} (cursor on brace)}},{{=%}}
        - {{re-indent inner block with {}}},{{=iB}}
        - {{re-indent entire buffer}},{{gg=G}}
        - {{paste and adjust indent to current line}},{{]p}}
    - Vim Exiting
        - {{write (save) the file, but don't exit}},{{:w}}
        - {{write out the current file using sudo}},{{:w !sudo tee %}}
        - {{write (save) and quit}},{{:wq}}
        - {{quit (fails if there are unsaved changes)}},{{:q}}
        - {{quit and throw away unsaved changes}},{{:q!}}
        - {{write (save) and quit on all tabs}},{{:wqa}}
    - Vim Search and replace
        - {{search for pattern}},{{/pattern}}
        - {{search backward for pattern}},{{?pattern}}
        - {{search for 'very magic' pattern (auto-interpret non-alphanumeric chars as special regex symbols)}},{{\vpattern}}
        - {{repeat search in same direction}},{{n}}
        - {{repeat search in opposite direction}},{{N}}
        - {{replace all old with new throughout file}},{{:%s/old/new/g}}
        - {{replace all old with new throughout file with confirmations}},{{:%s/old/new/gc}}
        - {{remove highlighting of search matches}},{{:noh}}
    - Vim Search in multiple files
        - {{search for pattern 'foo' in all .js files in every sub-directory (recursively)}},{{:vim /foo/ **/*.js}}
        - {{jump to the next match}},{{:cn}}
        - {{jump to the previous match}},{{:cp}}
        - {{open a window containing the list of matches}},{{:cope}}
    - Vim Working with multiple files
        - {{edit a file in a new buffer}},{{:e file}}
        - {{go to the next buffer}},{{:bn}}
        - {{go to the previous buffer}},{{:bp}}
        - {{delete a buffer (close a file)}},{{:bd}}
        - {{go to a buffer by #}},{{:b#}}
        - {{go to a buffer by file}},{{:b file}}
        - {{list all open buffers}},{{:ls}}
        - {{open a file in a new buffer and split window}},{{:sp file}}
        - {{open a file in a new buffer and vertically split window}},{{:vs file}}
        - {{edit all buffers as vertical windows}},{{:vert ba}}
        - {{edit all buffers as tabs}},{{:tab ba}}
        - {{split window}},control {{w s}}
        - {{split window vertically}},control {{w v}}
        - {{switch windows}},control {{w w}}
        - {{quit a window}},control {{w q}}
        - {{exchange current window with next one}},control {{w x}}
        - {{make all windows equal height & width}},control {{w =}}
        - {{move cursor to the left window (vertical split)}},control {{w h}}
        - {{move cursor to the right window (vertical split)}},control {{w l}}
        - {{move cursor to the window below (horizontal split)}},control {{w j}}
        - {{move cursor to the window above (horizontal split)}},control {{w k}}
    - Vim Tabs
        - {{open a file in a new tab}},{{:tabnew}}
        - {{move the current split window into its own tab}},control {{w t}}
        - {{move to the next tab}},{{gt}}
        - {{move to the previous tab}},{{gT}}
        - {{move to tab number #}},{{#gt}}
        - {{move current tab to the #th position (indexed from 0)}},{{:tabm #}}
        - {{close the current tab and all its windows}},{{:tabc}}
        - {{close all tabs except for the current one}},{{:tabo}}
        - {{run the command on all tabs (e.g. :tabdo q - closes all opened tabs)}},{{:tabdo command}}
    - Vim Diff
        - {{jump to start of next change}},{{]c}}
        - {{jump to start of previous change}},{{[c}}
        - {{obtain (get) difference (from other buffer)}},{{do}}
        - {{put difference (to other buffer)}},{{dp}}
        - {{make current window part of diff}},{{:diffthis}}
        - {{update differences}},{{:dif}}
        - {{switch off diff mode for current window}},{{:diffo}}
    - Vim Folding
        - {{manually define a fold up to motion}},{{zf}}
        - {{delete fold under the cursor}},{{zd}}
        - {{toggle fold under the cursor}},{{za}}
        - {{open fold under the cursor}},{{zo}}
        - {{open all folds at the cursor}},{{zO}}
        - {{close fold under the cursor}},{{zc}}
        - {{reduce (open) all folds by one level}},{{zr}}
        - {{open all folds}},{{zR}}
        - {{fold more (close) all folds by one level}},{{zm}}
        - {{close all open folds}},{{zM}}
        - {{delete all folds}},{{zE}}
        - {{toggle folding functionality}},{{zi}}
        - {{move to start of open fold.}},{{[z}}
        - {{move to end of open fold.}},{{]z}}
        - 
- nvim command
    - neovim commands index 
        - This file contains a list of all commands for each mode, with a tag and a short description.  
        - The lists are sorted on ASCII value.
        - Tip: When looking for certain functionality, use a search command.  E.g., to look for deleting something, use: "/delete".
        - For an overview of options see [option-list](https://neovim.io/doc/user/quickref.html#option-list). 
        - For an overview of built-in functions see [functions](https://neovim.io/doc/user/vimeval.html#functions). 
        - For a list of Vim variables see [vim-variable](https://neovim.io/doc/user/vimeval.html#vim-variable).
    -  **1. Insert Mode Index**** **
        - Tag		Char		Insert-mode action
        - 
        - [i_CTRL-@](https://neovim.io/doc/user/insert.html#i_CTRL-%40)  	`CTRL-@`		insert previously inserted text and stop 				insert 
        - {{`CTRL-A`}}		insert previously inserted text 
        - {{`CTRL-C`}}		quit insert mode, without checking for abbreviation 
        - {{`CTRL-D`}}		delete one shiftwidth of indent in the current line 
        - [i_CTRL-E](https://neovim.io/doc/user/insert.html#i_CTRL-E)  	`CTRL-E`		insert the character which is below the cursor 		
        - `CTRL-F`		not used (but by default it's in ['cinkeys'](https://neovim.io/doc/user/options.html#'cinkeys') to 	re-indent the current line) 
        - [i_CTRL-G_j](https://neovim.io/doc/user/insert.html#i_CTRL-G_j)  	`CTRL-G` `CTRL-J`	line down, to column where inserting started 
        - {{`CTRL-G`}}{{ j}}	line down, to column where inserting started 
        - [i_CTRL-G_j](https://neovim.io/doc/user/insert.html#i_CTRL-G_j)  	`CTRL-G` `<Down>`	line down, to column where inserting started 
        - [i_CTRL-G_k](https://neovim.io/doc/user/insert.html#i_CTRL-G_k)  	`CTRL-G` `CTRL-K`	line up, to column where inserting started 
        - {{`CTRL-G`}}{{ k}}	line up, to column where inserting started 
        - [i_CTRL-G_k](https://neovim.io/doc/user/insert.html#i_CTRL-G_k)  	`CTRL-G` `<Up>`	line up, to column where inserting started 
        - [i_CTRL-G_u](https://neovim.io/doc/user/insert.html#i_CTRL-G_u)  	`CTRL-G` u	start new undoable edit 
        - [i_CTRL-G_U](https://neovim.io/doc/user/insert.html#i_CTRL-G_U)  	`CTRL-G` U	don't break undo with next cursor movement 
        - {{`<BS>`}}		delete character before the cursor
        - [i_digraph](https://neovim.io/doc/user/digraph.html#i_digraph)  	`{char1}<BS>{char2}` 				enter digraph (only when ['digraph'](https://neovim.io/doc/user/options.html#'digraph') option set) 
        - {{`CTRL-H`}}		same as `<BS>` 
        - {{`<Tab>`}}		insert a `<Tab>` character 
        - {{`CTRL-I`}}		same as `<Tab>` 
        - [i_<NL>](https://neovim.io/doc/user/insert.html#i_%3CNL%3E)  	`<NL>`		same as `<CR>` 
        - {{`CTRL-J`}}		same as `<CR>` 
        - [i_CTRL-K](https://neovim.io/doc/user/insert.html#i_CTRL-K)  	`CTRL-K` `{char1}` `{char2}` 				enter digraph 
        - {{`<CR>`}}		begin new line 
        - {{`CTRL-M`}}		same as `<CR>` 
        - [i_CTRL-N](https://neovim.io/doc/user/insert.html#i_CTRL-N)  	`CTRL-N`		find next match for keyword in front of the 				cursor 
        - {{`CTRL-O`}}		execute a single command and return to insert 	mode 
        - [i_CTRL-P](https://neovim.io/doc/user/insert.html#i_CTRL-P)  	`CTRL-P`		find previous match for keyword in front of 				the cursor 
        - [i_CTRL-Q](https://neovim.io/doc/user/insert.html#i_CTRL-Q)  	`CTRL-Q`		same as `CTRL-V`, unless used for terminal 				control flow
        - [i_CTRL-SHIFT-Q](https://neovim.io/doc/user/insert.html#i_CTRL-SHIFT-Q)  `CTRL-SHIFT-Q` `{char}` 				like `CTRL-Q` unless [tui-modifyOtherKeys](https://neovim.io/doc/user/tui.html#tui-modifyOtherKeys) is active
        - [i_CTRL-R](https://neovim.io/doc/user/insert.html#i_CTRL-R)  	`CTRL-R` `{register}` 				insert the contents of a register 
        - [i_CTRL-R_CTRL-R](https://neovim.io/doc/user/insert.html#i_CTRL-R_CTRL-R) `CTRL-R` `CTRL-R` `{register}` 				insert the contents of a register literally
        - [i_CTRL-R_CTRL-O](https://neovim.io/doc/user/insert.html#i_CTRL-R_CTRL-O) `CTRL-R` `CTRL-O` `{register}` 				insert the contents of a register literally 				and don't auto-indent
        - [i_CTRL-R_CTRL-P](https://neovim.io/doc/user/insert.html#i_CTRL-R_CTRL-P) `CTRL-R` `CTRL-P` `{register}` 				insert the contents of a register literally 				and fix indent. 		
        - `CTRL-S`		not used or used for terminal control flow 
        - {{`CTRL-T`}}		insert one shiftwidth of indent in current line 
        - {{`CTRL-U`}}		delete all entered characters in the current line 
        - [i_CTRL-V](https://neovim.io/doc/user/insert.html#i_CTRL-V)  	`CTRL-V` `{char}`	insert next non-digit literally 
        - [i_CTRL-SHIFT-V](https://neovim.io/doc/user/insert.html#i_CTRL-SHIFT-V)  `CTRL-SHIFT-V` `{char}` 				like `CTRL-V` unless [tui-modifyOtherKeys](https://neovim.io/doc/user/tui.html#tui-modifyOtherKeys) is active 
        - [i_CTRL-V_digit](https://neovim.io/doc/user/insert.html#i_CTRL-V_digit) `CTRL-V` `{number}` insert three digit decimal number as a single 				byte.
        - {{`CTRL-W`}}		delete word before the cursor 
        - [i_CTRL-X](https://neovim.io/doc/user/insert.html#i_CTRL-X)  	`CTRL-X` `{mode}`	enter `CTRL-X` sub mode, see [i_CTRL-X_index](https://neovim.io/doc/user/vimindex.html#i_CTRL-X_index) 
        - [i_CTRL-Y](https://neovim.io/doc/user/insert.html#i_CTRL-Y)  	`CTRL-Y`		insert the character which is above the cursor 
        - {{`<Esc>`}}		end insert mode
        - [i_CTRL-[](https://neovim.io/doc/user/insert.html#i_CTRL-%5B)  	`CTRL-[`		same as `<Esc>`
        - [i_CTRL-\_CTRL-N](https://neovim.io/doc/user/intro.html#i_CTRL-%5C_CTRL-N) `CTRL-\` `CTRL-N`	go to Normal mode
        - [i_CTRL-\_CTRL-G](https://neovim.io/doc/user/intro.html#i_CTRL-%5C_CTRL-G) `CTRL-\` `CTRL-G`	go to Normal mode 		
        - `CTRL-\` a - z	reserved for extensions 		
        - `CTRL-\` others	not used 
        - [i_CTRL-]](https://neovim.io/doc/user/insert.html#i_CTRL-%5D)  	`CTRL-]`		trigger abbreviation 
        - [i_CTRL-^](https://neovim.io/doc/user/insert.html#i_CTRL-%5E)  	`CTRL-^`		toggle use of [:lmap](https://neovim.io/doc/user/map.html#%3Almap) mappings 
        - [i_CTRL-_](https://neovim.io/doc/user/insert.html#i_CTRL-_)  	`CTRL-_`		When ['allowrevins'](https://neovim.io/doc/user/options.html#'allowrevins') set: toggle ['revins'](https://neovim.io/doc/user/options.html#'revins')
            - `<Space>` to '~'	not used, except '0' and '^' followed by 				
        - `CTRL-D`
        - [i_0_CTRL-D](https://neovim.io/doc/user/insert.html#i_0_CTRL-D)  	0 `CTRL-D`	delete all indent in the current line 
        - [i_^_CTRL-D](https://neovim.io/doc/user/insert.html#i_%5E_CTRL-D)  	^ `CTRL-D`	delete all indent in the current line, restore 				it in the next line
        - {{`<Del>`}}		delete character under the cursor
        - 
        - Meta characters (0x80 to 0xff, 128 to 255) 				not used
        - [i_<Left>](https://neovim.io/doc/user/insert.html#i_%3CLeft%3E)  	`<Left>`		cursor one character left 
        - [i_<S-Left>](https://neovim.io/doc/user/insert.html#i_%3CS-Left%3E)  	`<S-Left>`	cursor one word left 
        - [i_<C-Left>](https://neovim.io/doc/user/insert.html#i_%3CC-Left%3E)  	`<C-Left>`	cursor one word left 
        - [i_<Right>](https://neovim.io/doc/user/insert.html#i_%3CRight%3E)  	`<Right>`		cursor one character right 
        - [i_<S-Right>](https://neovim.io/doc/user/insert.html#i_%3CS-Right%3E)  	`<S-Right>`	cursor one word right 
        - [i_<C-Right>](https://neovim.io/doc/user/insert.html#i_%3CC-Right%3E)  	`<C-Right>`	cursor one word right 
        - [i_<Up>](https://neovim.io/doc/user/insert.html#i_%3CUp%3E)  	`<Up>`		cursor one line up 
        - [i_<S-Up>](https://neovim.io/doc/user/insert.html#i_%3CS-Up%3E)  	`<S-Up>`		same as `<PageUp>` 
        - [i_<Down>](https://neovim.io/doc/user/insert.html#i_%3CDown%3E)  	`<Down>`		cursor one line down 
        - [i_<S-Down>](https://neovim.io/doc/user/insert.html#i_%3CS-Down%3E)  	`<S-Down>`	same as `<PageDown>` 
        - [i_<Home>](https://neovim.io/doc/user/insert.html#i_%3CHome%3E)  	`<Home>`		cursor to start of line 
        - [i_<C-Home>](https://neovim.io/doc/user/insert.html#i_%3CC-Home%3E)  	`<C-Home>`	cursor to start of file 
        - [i_<End>](https://neovim.io/doc/user/insert.html#i_%3CEnd%3E)  	`<End>`		cursor past end of line 
        - [i_<C-End>](https://neovim.io/doc/user/insert.html#i_%3CC-End%3E)  	`<C-End>`		cursor past end of file 
        - [i_<PageUp>](https://neovim.io/doc/user/insert.html#i_%3CPageUp%3E)  	`<PageUp>`	one screenful backward 
        - [i_<PageDown>](https://neovim.io/doc/user/insert.html#i_%3CPageDown%3E)  	`<PageDown>`	one screenful forward 
        - [i_<F1>](https://neovim.io/doc/user/helphelp.html#i_%3CF1%3E)  	`<F1>`		same as `<Help>` 
        - [i_<Help>](https://neovim.io/doc/user/helphelp.html#i_%3CHelp%3E)  	`<Help>`		stop insert mode and display help window 
        - [i_<Insert>](https://neovim.io/doc/user/insert.html#i_%3CInsert%3E)  	`<Insert>`	toggle Insert/Replace mode 
        - [i_<LeftMouse>](https://neovim.io/doc/user/insert.html#i_%3CLeftMouse%3E)  	`<LeftMouse>`	cursor at mouse click 
        - [i_<ScrollWheelDown>](https://neovim.io/doc/user/insert.html#i_%3CScrollWheelDown%3E)  	`<ScrollWheelDown>`	move window three lines down 
        - [i_<S-ScrollWheelDown>](https://neovim.io/doc/user/insert.html#i_%3CS-ScrollWheelDown%3E)  	`<S-ScrollWheelDown>`	move window one page down 
        - [i_<ScrollWheelUp>](https://neovim.io/doc/user/insert.html#i_%3CScrollWheelUp%3E)  	`<ScrollWheelUp>`		move window three lines up 
        - [i_<S-ScrollWheelUp>](https://neovim.io/doc/user/insert.html#i_%3CS-ScrollWheelUp%3E)  	`<S-ScrollWheelUp>`	move window one page up 
        - [i_<ScrollWheelLeft>](https://neovim.io/doc/user/insert.html#i_%3CScrollWheelLeft%3E)  	`<ScrollWheelLeft>`	move window six columns left 
        - [i_<S-ScrollWheelLeft>](https://neovim.io/doc/user/insert.html#i_%3CS-ScrollWheelLeft%3E)  	`<S-ScrollWheelLeft>`	move window one page left 
        - [i_<ScrollWheelRight>](https://neovim.io/doc/user/insert.html#i_%3CScrollWheelRight%3E)  	`<ScrollWheelRight>`	move window six columns right
        - [i_<S-ScrollWheelRight>](https://neovim.io/doc/user/insert.html#i_%3CS-ScrollWheelRight%3E) `<S-ScrollWheelRight>`	move window one page right
        - commands in `CTRL-X` submode				[i_CTRL-X_index](https://neovim.io/doc/user/vimindex.html#i_CTRL-X_index)
            - [i_CTRL-X_CTRL-D](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-D)  	`CTRL-X` `CTRL-D`	complete defined identifiers 
            - [i_CTRL-X_CTRL-E](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-E)  	`CTRL-X` `CTRL-E`	scroll up 
            - [i_CTRL-X_CTRL-F](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-F)  	`CTRL-X` `CTRL-F`	complete file names 
            - [i_CTRL-X_CTRL-I](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-I)  	`CTRL-X` `CTRL-I`	complete identifiers 
            - [i_CTRL-X_CTRL-K](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-K)  	`CTRL-X` `CTRL-K`	complete identifiers from dictionary 
            - [i_CTRL-X_CTRL-L](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-L)  	`CTRL-X` `CTRL-L`	complete whole lines 
            - [i_CTRL-X_CTRL-N](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-N)  	`CTRL-X` `CTRL-N`	next completion 
            - [i_CTRL-X_CTRL-O](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-O)  	`CTRL-X` `CTRL-O`	omni completion 
            - [i_CTRL-X_CTRL-P](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-P)  	`CTRL-X` `CTRL-P`	previous completion 
            - [i_CTRL-X_CTRL-R](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-R)  	`CTRL-X` `CTRL-R`	complete contents from registers 
            - [i_CTRL-X_CTRL-S](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-S)  	`CTRL-X` `CTRL-S`	spelling suggestions 
            - [i_CTRL-X_CTRL-T](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-T)  	`CTRL-X` `CTRL-T`	complete identifiers from thesaurus 
            - [i_CTRL-X_CTRL-Y](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-Y)  	`CTRL-X` `CTRL-Y`	scroll down
            - [i_CTRL-X_CTRL-U](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-U)  	`CTRL-X` `CTRL-U`	complete with
            - ['completefunc'](https://neovim.io/doc/user/options.html#'completefunc') [i_CTRL-X_CTRL-V](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-V)  	`CTRL-X` `CTRL-V`	complete like in : command line
            - [i_CTRL-X_CTRL-Z](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-Z)  	`CTRL-X` `CTRL-Z`	stop completion, keeping the text as-is
            - [i_CTRL-X_CTRL-]](https://neovim.io/doc/user/insert.html#i_CTRL-X_CTRL-%5D)  	`CTRL-X` `CTRL-]`	complete tags 
            - `CTRL-X` s	spelling suggestions 
        - commands in completion mode (see [popupmenu-keys](https://neovim.io/doc/user/insert.html#popupmenu-keys))
            - {{`CTRL-E`}}	stop completion and go back to original text  
            - {{`CTRL-Y`}}	accept selected match and stop completion 		
            - `CTRL-L`		insert one character from the current match 		
            - {{`<CR>`}}		insert currently selected match 		
            - {{`<BS>`}}		delete one character and redo search 		
            - {{`CTRL-H`}}		same as `<BS>` 		
            - `<Up>`		select the previous match 		
            - `<Down>`		select the next match 		
            - `<PageUp>`	select a match several entries back 		
            - `<PageDown>`	select a match several entries forward 		
            - other		stop completion and insert the typed character
    -  **2. Normal mode**** index**
        - CHAR	 any non-blank character WORD	 a sequence of non-blank characters N	 a number entered before the command `{motion}` a cursor movement command Nmove	 the text that is moved over with a `{motion}` SECTION	 a section that possibly starts with '}' instead of '{'
        - note: 1 = cursor movement command; 2 = can be undone/redone
        - Tag		Char	      Note Normal-mode action
        - ------------------------------------------------------------------------------
            - `CTRL-@`		   not used [CTRL-A](https://neovim.io/doc/user/change.html#CTRL-A)  	`CTRL-A`		2  add N to number at/after cursor [CTRL-B](https://neovim.io/doc/user/scroll.html#CTRL-B)  	`CTRL-B`		1  scroll N screens Backwards [CTRL-C](https://neovim.io/doc/user/pattern.html#CTRL-C)  	`CTRL-C`		   interrupt current (search) command [CTRL-D](https://neovim.io/doc/user/scroll.html#CTRL-D)  	`CTRL-D`		   scroll Down N lines (default: half a screen) [CTRL-E](https://neovim.io/doc/user/scroll.html#CTRL-E)  	`CTRL-E`		   scroll N lines upwards (N lines Extra) [CTRL-F](https://neovim.io/doc/user/scroll.html#CTRL-F)  	`CTRL-F`		1  scroll N screens Forward [CTRL-G](https://neovim.io/doc/user/editing.html#CTRL-G)  	`CTRL-G`		   display current file name and position [<BS>](https://neovim.io/doc/user/motion.html#%3CBS%3E)  		`<BS>`		1  same as "h" [CTRL-H](https://neovim.io/doc/user/motion.html#CTRL-H)  	`CTRL-H`		1  same as "h" [<Tab>](https://neovim.io/doc/user/motion.html#%3CTab%3E)  		`<Tab>`		1  go to N newer entry in jump list [CTRL-I](https://neovim.io/doc/user/motion.html#CTRL-I)  	`CTRL-I`		1  same as `<Tab>` [<NL>](https://neovim.io/doc/user/motion.html#%3CNL%3E)  		`<NL>`		1  same as "j" [<S-NL>](https://neovim.io/doc/user/scroll.html#%3CS-NL%3E)  	`<S-NL>`		1  same as `CTRL-F` [CTRL-J](https://neovim.io/doc/user/motion.html#CTRL-J)  	`CTRL-J`		1  same as "j" 		`CTRL-K`		   not used [CTRL-L](https://neovim.io/doc/user/various.html#CTRL-L)  	`CTRL-L`		   redraw screen [<CR>](https://neovim.io/doc/user/motion.html#%3CCR%3E)  		`<CR>`		1  cursor to the first CHAR N lines lower [<S-CR>](https://neovim.io/doc/user/scroll.html#%3CS-CR%3E)  	`<S-CR>`		1  same as `CTRL-F` [CTRL-M](https://neovim.io/doc/user/motion.html#CTRL-M)  	`CTRL-M`		1  same as `<CR>` [CTRL-N](https://neovim.io/doc/user/motion.html#CTRL-N)  	`CTRL-N`		1  same as "j" [CTRL-O](https://neovim.io/doc/user/motion.html#CTRL-O)  	`CTRL-O`		1  go to N older entry in jump list [CTRL-P](https://neovim.io/doc/user/motion.html#CTRL-P)  	`CTRL-P`		1  same as "k" 		`CTRL-Q`		   not used, or used for terminal control flow [CTRL-R](https://neovim.io/doc/user/undo.html#CTRL-R)  	`CTRL-R`		2  redo changes which were undone with 'u' 		`CTRL-S`		   not used, or used for terminal control flow [CTRL-T](https://neovim.io/doc/user/tagsrch.html#CTRL-T)  	`CTRL-T`		   jump to N older Tag in tag list [CTRL-U](https://neovim.io/doc/user/scroll.html#CTRL-U)  	`CTRL-U`		   scroll N lines Upwards (default: half a 				   screen) [CTRL-V](https://neovim.io/doc/user/visual.html#CTRL-V)  	`CTRL-V`		   start blockwise Visual mode [CTRL-W](https://neovim.io/doc/user/vimindex.html#CTRL-W)  	`CTRL-W` `{char}`	   window commands, see [CTRL-W](https://neovim.io/doc/user/vimindex.html#CTRL-W) [CTRL-X](https://neovim.io/doc/user/change.html#CTRL-X)  	`CTRL-X`		2  subtract N from number at/after cursor [CTRL-Y](https://neovim.io/doc/user/scroll.html#CTRL-Y)  	`CTRL-Y`		   scroll N lines downwards [CTRL-Z](https://neovim.io/doc/user/starting.html#CTRL-Z)  	`CTRL-Z`		   suspend program (or start new shell) 		`CTRL-[` `<Esc>`	   not used [CTRL-\_CTRL-N](https://neovim.io/doc/user/intro.html#CTRL-%5C_CTRL-N)  	`CTRL-\` `CTRL-N`	   go to Normal mode (no-op) [CTRL-\_CTRL-G](https://neovim.io/doc/user/intro.html#CTRL-%5C_CTRL-G)  	`CTRL-\` `CTRL-G`	   go to Normal mode (no-op) 		`CTRL-\` a - z	   reserved for extensions 		`CTRL-\` others	   not used [CTRL-]](https://neovim.io/doc/user/tagsrch.html#CTRL-%5D)  	`CTRL-]`		   :ta to ident under cursor [CTRL-^](https://neovim.io/doc/user/editing.html#CTRL-%5E)  	`CTRL-^`		   edit Nth alternate file (equivalent to 				   ":e #N") [CTRL-<Tab>](https://neovim.io/doc/user/tabpage.html#CTRL-%3CTab%3E)  	`CTRL-<`Tab>	   same as `g<Tab>` : go to last accessed tab 				   page 		`CTRL-_`		   not used
        - [<Space>](https://neovim.io/doc/user/motion.html#%3CSpace%3E)  	`<Space>`		1  same as "l" [!](https://neovim.io/doc/user/change.html#%21)  		!{motion}{filter} 				2  filter Nmove text through the `{filter}` 				   command [!!](https://neovim.io/doc/user/change.html#%21%21)  		!!{filter}	2  filter N lines through the `{filter}` command [quote](https://neovim.io/doc/user/change.html#quote)  		"{register}	   use `{register}` for next delete, yank or put 				   (`{.%#:}` only work with put) [#](https://neovim.io/doc/user/pattern.html#%23)  		#		1  search backward for the Nth occurrence of 				   the ident under the cursor [$](https://neovim.io/doc/user/motion.html#%24)$		1  cursor to the end of Nth next line [%](https://neovim.io/doc/user/motion.html#%25)  		%		1  find the next (curly/square) bracket on 				   this line and go to its match, or go to 				   matching comment bracket, or go to matching 				   preprocessor directive. [N%](https://neovim.io/doc/user/motion.html#N%25)  		`{count}`%	1  go to N percentage in the file [&](https://neovim.io/doc/user/change.html#%26)  		&		2  repeat last :s ['](https://neovim.io/doc/user/motion.html#')  		'{a-zA-Z0-9}	1  cursor to the first CHAR on the line with 				   mark `{a-zA-Z0-9}` [''](https://neovim.io/doc/user/motion.html#'')  		''		1  cursor to the first CHAR of the line where 				   the cursor was before the latest jump. ['(](https://neovim.io/doc/user/motion.html#'%28)  		'(		1  cursor to the first CHAR on the line of the 				   start of the current sentence [')](https://neovim.io/doc/user/motion.html#'%29)  		')		1  cursor to the first CHAR on the line of the 				   end of the current sentence ['<](https://neovim.io/doc/user/motion.html#'%3C)  		'<		1  cursor to the first CHAR of the line where 				   highlighted area starts/started in the 				   current buffer. ['>](https://neovim.io/doc/user/motion.html#'%3E)  		'>		1  cursor to the first CHAR of the line where 				   highlighted area ends/ended in the current 				   buffer. ['[](https://neovim.io/doc/user/motion.html#'%5B)  		'[1  cursor to the first CHAR on the line of the 				   start of last operated text or start of put 				   text [']](https://neovim.io/doc/user/motion.html#'%5D)  		']		1  cursor to the first CHAR on the line of the 				   end of last operated text or end of put 				   text ['{](https://neovim.io/doc/user/motion.html#'%7B)  		'{		1  cursor to the first CHAR on the line of the 				   start of the current paragraph ['}](https://neovim.io/doc/user/motion.html#'%7D)  		'}		1  cursor to the first CHAR on the line of the 				   end of the current paragraph [(](https://neovim.io/doc/user/motion.html#%28)  		(		1  cursor N sentences backward [)](https://neovim.io/doc/user/motion.html#%29)  		)		1  cursor N sentences forward [star](https://neovim.io/doc/user/pattern.html#star)  		*		1  search forward for the Nth occurrence of 				   the ident under the cursor [+](https://neovim.io/doc/user/motion.html#%2B)  		+		1  same as `<CR>` [<S-Plus>](https://neovim.io/doc/user/scroll.html#%3CS-Plus%3E)  	`<S-+>`		1  same as `CTRL-F` [,](https://neovim.io/doc/user/motion.html#%2C)  		,		1  repeat latest f, t, F or T in opposite 				   direction N times [-](https://neovim.io/doc/user/motion.html#-)  		-		1  cursor to the first CHAR N lines higher [<S-Minus>](https://neovim.io/doc/user/scroll.html#%3CS-Minus%3E)  	`<S-->`		1  same as `CTRL-B` [.](https://neovim.io/doc/user/repeat.html#.)  		.		2  repeat last change with count replaced with 				   N [/](https://neovim.io/doc/user/pattern.html#%2F)  		/{pattern}<CR>	1  search forward for the Nth occurrence of 				   `{pattern}` [/<CR>](https://neovim.io/doc/user/pattern.html#%2F%3CCR%3E)  		/<CR>		1  search forward for `{pattern}` of last search [0](https://neovim.io/doc/user/motion.html#0)  		0		1  cursor to the first char of the line [count](https://neovim.io/doc/user/intro.html#count)  		1		   prepend to command to give a count [count](https://neovim.io/doc/user/intro.html#count)  		2			" [count](https://neovim.io/doc/user/intro.html#count)  		3			" [count](https://neovim.io/doc/user/intro.html#count)  		4			" [count](https://neovim.io/doc/user/intro.html#count)  		5			" [count](https://neovim.io/doc/user/intro.html#count)  		6			" [count](https://neovim.io/doc/user/intro.html#count)  		7			" [count](https://neovim.io/doc/user/intro.html#count)  		8			" [count](https://neovim.io/doc/user/intro.html#count)  		9			" [:](https://neovim.io/doc/user/cmdline.html#%3A)  		:		1  start entering an Ex command [N:](https://neovim.io/doc/user/cmdline.html#N%3A)  		`{count}`:	   start entering an Ex command with range 				   from current line to N-1 lines down [;](https://neovim.io/doc/user/motion.html#%3B)  		;		1  repeat latest f, t, F or T N times [<](https://neovim.io/doc/user/change.html#%3C)  		<{motion}	2  shift Nmove lines one ['shiftwidth'](https://neovim.io/doc/user/options.html#'shiftwidth') 				   leftwards [<<](https://neovim.io/doc/user/change.html#%3C%3C)  		<<		2  shift N lines one ['shiftwidth'](https://neovim.io/doc/user/options.html#'shiftwidth') leftwards [=](https://neovim.io/doc/user/change.html#%3D)  		={motion}	2  filter Nmove lines through "indent"―↔		2  filter N lines through "indent" [>](https://neovim.io/doc/user/change.html#%3E)  		>`{motion}`	2  shift Nmove lines one ['shiftwidth'](https://neovim.io/doc/user/options.html#'shiftwidth') 				   rightwards [>>](https://neovim.io/doc/user/change.html#%3E%3E)  		>>		2  shift N lines one ['shiftwidth'](https://neovim.io/doc/user/options.html#'shiftwidth') rightwards [?](https://neovim.io/doc/user/pattern.html#%3F)  		?{pattern}<CR>	1  search backward for the Nth previous 				   occurrence of `{pattern}` [?<CR>](https://neovim.io/doc/user/pattern.html#%3F%3CCR%3E)  		?<CR>		1  search backward for `{pattern}` of last search [@](https://neovim.io/doc/user/repeat.html#%40)  		@{a-z}		2  execute the contents of register `{a-z}`
        - N times [@:](https://neovim.io/doc/user/repeat.html#%40%3A)  		@:		   repeat the previous ":" command N times [@@](https://neovim.io/doc/user/repeat.html#%40%40)  		@@		2  repeat the previous @{a-z} N times [A](https://neovim.io/doc/user/insert.html#A)  		A		2  append text after the end of the line N times [B](https://neovim.io/doc/user/motion.html#B)  		B		1  cursor N WORDS backward [C](https://neovim.io/doc/user/change.html#C)  		["x]C		2  change from the cursor position to the end 				   of the line, and N-1 more lines [into 				   register x]; synonym for "c$](https://neovim.io/doc/user/change.html#D)[" [D](https://neovim.io/doc/user/change.html#D)  		["x]D		2  delete the characters under the cursor 				   until the end of the line and N-1 more 				   lines [into register x]; synonym for "d$" [E](https://neovim.io/doc/user/motion.html#E)  		E		1  cursor forward to the end of WORD N [F](https://neovim.io/doc/user/motion.html#F)  		F{char}		1  cursor to the Nth occurrence of `{char}` to 				   the left [G](https://neovim.io/doc/user/motion.html#G)  		G		1  cursor to line N, default last line [H](https://neovim.io/doc/user/motion.html#H)  		H		1  cursor to line N from top of screen [I](https://neovim.io/doc/user/insert.html#I)  		I		2  insert text before the first CHAR on the 				   line N times [J](https://neovim.io/doc/user/change.html#J)  		J		2  Join N lines; default is 2 [K](https://neovim.io/doc/user/various.html#K)  		K		   lookup Keyword under the cursor with 				   ['keywordprg'](https://neovim.io/doc/user/options.html#'keywordprg') [L](https://neovim.io/doc/user/motion.html#L)  		L		1  cursor to line N from bottom of screen [M](https://neovim.io/doc/user/motion.html#M)  		M		1  cursor to middle line of screen [N](https://neovim.io/doc/user/pattern.html#N)  		N		1  repeat the latest '/' or '?' N times in 				   opposite direction [O](https://neovim.io/doc/user/insert.html#O)  		O		2  begin a new line above the cursor and 				   insert text, repeat N times [P](https://neovim.io/doc/user/change.html#P)  		["x]P		2  put the text [from register x] before the 				   cursor N times [R](https://neovim.io/doc/user/change.html#R)  		R		2  enter replace mode: overtype existing 				   characters, repeat the entered text N-1 				   times [S](https://neovim.io/doc/user/change.html#S)  		["x]S		2  delete N lines [into register x] and start 				   insert; synonym for "cc". [T](https://neovim.io/doc/user/motion.html#T)  		T{char}		1  cursor till after Nth occurrence of `{char}` 				   to the left [U](https://neovim.io/doc/user/undo.html#U)  		U		2  undo all latest changes on one line [V](https://neovim.io/doc/user/visual.html#V)  		V		   start linewise Visual mode [W](https://neovim.io/doc/user/motion.html#W)  		W		1  cursor N WORDS forward [X](https://neovim.io/doc/user/change.html#X)  		["x]X		2  delete N characters before the cursor [into 				   register x] [Y](https://neovim.io/doc/user/change.html#Y)  		["x]Y		   yank N lines [into register x]; synonym for 				   "yy" ](https://neovim.io/doc/user/vim_diff.html#default-mappings)[**				   Note:**](https://neovim.io/doc/user/vim_diff.html#default-mappings)[ Mapped to "y$" by default. [default-mappings](https://neovim.io/doc/user/vim_diff.html#default-mappings) [ZZ](https://neovim.io/doc/user/editing.html#ZZ)  		ZZ		   write if buffer changed and close window [ZQ](https://neovim.io/doc/user/editing.html#ZQ)  		ZQ		   close window without writing [[](https://neovim.io/doc/user/vimindex.html#%5B)  		[`{char}`		   square bracket command (see [ Index - Neovim docs](https://neovim.io/doc/user/vimindex.html#%5D)  		]{char}		   square bracket command (see []](https://neovim.io/doc/user/vimindex.html#%5D) below) [^](https://neovim.io/doc/user/motion.html#%5E)  		^		1  cursor to the first CHAR of the line [_](https://neovim.io/doc/user/motion.html#_)  		_		1  cursor to the first CHAR N - 1 lines lower [`](https://neovim.io/doc/user/motion.html#%60)  {a-zA-Z0-9}	1  cursor to the mark {a-zA-Z0-9} [`(](https://neovim.io/doc/user/motion.html#%60%28)  (		1  cursor to the start of the current sentence [`)](https://neovim.io/doc/user/motion.html#%60%29)  )		1  cursor to the end of the current sentence [`<](https://neovim.io/doc/user/motion.html#%60%3C)  <		1  cursor to the start of the highlighted area [`>](https://neovim.io/doc/user/motion.html#%60%3E)  >		1  cursor to the end of the highlighted area [`  [		1  cursor to the start of last operated text 				   or start of putted text [`]](https://neovim.io/doc/user/motion.html#%60%5D)  ]		1  cursor to the end of last operated text or 				   end of putted text [``](https://neovim.io/doc/user/motion.html#%60%60)  		"``"		1  cursor to the position before latest jump [`{](https://neovim.io/doc/user/motion.html#%60%7B)  {		1  cursor to the start of the current paragraph [`}](https://neovim.io/doc/user/motion.html#%60%7D)  }		1  cursor to the end of the current paragraph [a](https://neovim.io/doc/user/insert.html#a)  		a		2  append text after the cursor N times [b](https://neovim.io/doc/user/motion.html#b)`
        - `b		1  cursor N words backward [c](https://neovim.io/doc/user/change.html#c)  		["x]c{motion}	2  delete Nmove text [into register x] and 				   start insert [cc](https://neovim.io/doc/user/change.html#cc)  		["x]cc		2  delete N lines [into register x] and start 				   insert [d](https://neovim.io/doc/user/change.html#d)  		["x]d{motion}	2  delete Nmove text [into register x] [dd](https://neovim.io/doc/user/change.html#dd)  		["x]dd		2  delete N lines [into register x] [do](https://neovim.io/doc/user/diff.html#do)  		do		2  same as ":diffget" [dp](https://neovim.io/doc/user/diff.html#dp)  		dp		2  same as ":diffput" [e](https://neovim.io/doc/user/motion.html#e)  		e		1  cursor forward to the end of word N [f](https://neovim.io/doc/user/motion.html#f)  		f{char}		1  cursor to Nth occurrence of `{char}` to the 				   right [g](https://neovim.io/doc/user/vimindex.html#g)  		g{char}		   extended commands, see [g](https://neovim.io/doc/user/vimindex.html#g) below [h](https://neovim.io/doc/user/motion.html#h)  		h		1  cursor N chars to the left [i](https://neovim.io/doc/user/insert.html#i)  		i		2  insert text before the cursor N times [j](https://neovim.io/doc/user/motion.html#j)  		j		1  cursor N lines downward [k](https://neovim.io/doc/user/motion.html#k)  		k		1  cursor N lines upward [l](https://neovim.io/doc/user/motion.html#l)  		l		1  cursor N chars to the right [m](https://neovim.io/doc/user/motion.html#m)  		m{A-Za-z}	   set mark `{A-Za-z}` at cursor position [n](https://neovim.io/doc/user/pattern.html#n)  		n		1  repeat the latest '/' or '?' N times [o](https://neovim.io/doc/user/insert.html#o)  		o		2  begin a new line below the cursor and 				   insert text, repeat N times [p](https://neovim.io/doc/user/change.html#p)  		["x]p		2  put the text [from register x] after the 				   cursor N times [q](https://neovim.io/doc/user/repeat.html#q)  		q{0-9a-zA-Z"}	   record typed characters into named register 				   `{0-9a-zA-Z"}` (uppercase to append) [q](https://neovim.io/doc/user/repeat.html#q)  		q		   (while recording) stops recording [Q](https://neovim.io/doc/user/repeat.html#Q)  		Q		2  replay last recorded register [q:](https://neovim.io/doc/user/cmdline.html#q%3A)  		q:		   edit : command-line in command-line window [q/](https://neovim.io/doc/user/cmdline.html#q%2F)  		q/		   edit / command-line in command-line window [q?](https://neovim.io/doc/user/cmdline.html#q%3F)  		q?		   edit ? command-line in command-line window [r](https://neovim.io/doc/user/change.html#r)  		r{char}		2  replace N chars with `{char}` [s](https://neovim.io/doc/user/change.html#s)  		["x]s		2  (substitute) delete N characters [into 				   register x] and start insert [t](https://neovim.io/doc/user/motion.html#t)  		t{char}		1  cursor till before Nth occurrence of `{char}` 				   to the right [u](https://neovim.io/doc/user/undo.html#u)  		u		2  undo changes [v](https://neovim.io/doc/user/visual.html#v)  		v		   start charwise Visual mode [w](https://neovim.io/doc/user/motion.html#w)  		w		1  cursor N words forward [x](https://neovim.io/doc/user/change.html#x)  		["x]x		2  delete N characters under and after the 				   cursor [into register x] [y](https://neovim.io/doc/user/change.html#y)  		["x]y{motion}	   yank Nmove text [into register`
        - `x] [yy](https://neovim.io/doc/user/change.html#yy)  		["x]yy		   yank N lines [into register x] [z](https://neovim.io/doc/user/vimindex.html#z)  		z{char}		   commands starting with 'z', see [z](https://neovim.io/doc/user/vimindex.html#z) below [{](https://neovim.io/doc/user/motion.html#%7B)  		{		1  cursor N paragraphs backward [bar](https://neovim.io/doc/user/motion.html#bar)  		|		1  cursor to column N [}](https://neovim.io/doc/user/motion.html#%7D)  		}		1  cursor N paragraphs forward [~](https://neovim.io/doc/user/change.html#~)  		~		2  ['tildeop'](https://neovim.io/doc/user/options.html#'tildeop') off: switch case of N characters 				   under cursor and move the cursor N 				   characters to the right [~](https://neovim.io/doc/user/change.html#~)  		~`{motion}`	   ['tildeop'](https://neovim.io/doc/user/options.html#'tildeop') on: switch case of Nmove text [<C-End>](https://neovim.io/doc/user/motion.html#%3CC-End%3E)  	`<C-End>`		1  same as "G" [<C-Home>](https://neovim.io/doc/user/motion.html#%3CC-Home%3E)  	`<C-Home>`	1  same as "gg" [<C-Left>](https://neovim.io/doc/user/motion.html#%3CC-Left%3E)  	`<C-Left>`	1  same as "b" [<C-LeftMouse>](https://neovim.io/doc/user/tagsrch.html#%3CC-LeftMouse%3E)  	`<C-LeftMouse>`	   ":ta" to the keyword at the mouse click [<C-Right>](https://neovim.io/doc/user/motion.html#%3CC-Right%3E)  	`<C-Right>`	1  same as "w" [<C-RightMouse>](https://neovim.io/doc/user/tagsrch.html#%3CC-RightMouse%3E) `<C-RightMouse>`	   same as "CTRL-T" [<C-Tab>](https://neovim.io/doc/user/tabpage.html#%3CC-Tab%3E)  	`<C-Tab>`		   same as "g<Tab>" [<Del>](https://neovim.io/doc/user/change.html#%3CDel%3E)  		["x]<Del>	2  same as "x" [N<Del>](https://neovim.io/doc/user/various.html#N%3CDel%3E)  	`{count}``<Del>`	   remove the last digit from `{count}` [<Down>](https://neovim.io/doc/user/motion.html#%3CDown%3E)  	`<Down>`		1  same as "j" [<End>](https://neovim.io/doc/user/motion.html#%3CEnd%3E)  		`<End>`		1  same as "$" [<F1>](https://neovim.io/doc/user/helphelp.html#%3CF1%3E)  		`<F1>`		   same as `<Help>` [<Help>](https://neovim.io/doc/user/helphelp.html#%3CHelp%3E)  	`<Help>`		   open a help window [<Home>](https://neovim.io/doc/user/motion.html#%3CHome%3E)  	`<Home>`		1  same as "0" [<Insert>](https://neovim.io/doc/user/insert.html#%3CInsert%3E)  	`<Insert>`	2  same as "i" [<Left>](https://neovim.io/doc/user/motion.html#%3CLeft%3E)  	`<Left>`		1  same as "h" [<LeftMouse>](https://neovim.io/doc/user/visual.html#%3CLeftMouse%3E)  	`<LeftMouse>`	1  move cursor to the mouse click position [<MiddleMouse>](https://neovim.io/doc/user/change.html#%3CMiddleMouse%3E)  	`<MiddleMouse>`	2  same as "gP" at the mouse click position [<PageDown>](https://neovim.io/doc/user/scroll.html#%3CPageDown%3E)  	`<PageDown>`	   same as `CTRL-F` [<PageUp>](https://neovim.io/doc/user/scroll.html#%3CPageUp%3E)  	`<PageUp>`	   same as `CTRL-B` [<Right>](https://neovim.io/doc/user/motion.html#%3CRight%3E)  	`<Right>`		1  same as "l" [<RightMouse>](https://neovim.io/doc/user/visual.html#%3CRightMouse%3E)  	`<RightMouse>`	   start Visual mode, move cursor to the mouse 				   click position [<S-Down>](https://neovim.io/doc/user/scroll.html#%3CS-Down%3E)  	`<S-Down>`	1  same as `CTRL-F` [<S-Left>](https://neovim.io/doc/user/motion.html#%3CS-Left%3E)  	`<S-Left>`	1  same as "b" [<S-LeftMouse>](https://neovim.io/doc/user/gui.html#%3CS-LeftMouse%3E)  	`<S-LeftMouse>`	   same as "*" at the mouse click position [<S-Right>](https://neovim.io/doc/user/motion.html#%3CS-Right%3E)  	`<S-Right>`	1  same as "w" [<S-RightMouse>](https://neovim.io/doc/user/gui.html#%3CS-RightMouse%3E) `<S-RightMouse>`	   same as "#" at the mouse click position [<S-Up>](https://neovim.io/doc/user/scroll.html#%3CS-Up%3E)  	`<S-Up>`		1  same as `CTRL-B` [<Undo>](https://neovim.io/doc/user/undo.html#%3CUndo%3E)  	`<Undo>`		2  same as "u" [<Up>](https://neovim.io/doc/user/motion.html#%3CUp%3E)  		`<Up>`		1  same as "k" [<ScrollWheelDown>](https://neovim.io/doc/user/vimindex.html#%3CScrollWheelDown%3E)  	`<ScrollWheelDown>`	move window three lines down [<S-ScrollWheelDown>](https://neovim.io/doc/user/vimindex.html#%3CS-ScrollWheelDown%3E)  	`<S-ScrollWheelDown>`	move window one page down [<ScrollWheelUp>](https://neovim.io/doc/user/vimindex.html#%3CScrollWheelUp%3E)  	`<ScrollWheelUp>`		move window three lines up [<S-ScrollWheelUp>](https://neovim.io/doc/user/vimindex.html#%3CS-ScrollWheelUp%3E)  	`<S-ScrollWheelUp>`	move window one page up [<ScrollWheelLeft>](https://neovim.io/doc/user/vimindex.html#%3CScrollWheelLeft%3E)  	`<ScrollWheelLeft>`	move window six columns left [<S-ScrollWheelLeft>](https://neovim.io/doc/user/vimindex.html#%3CS-ScrollWheelLeft%3E)  	`<S-ScrollWheelLeft>`	move window one page left [<ScrollWheelRight>](https://neovim.io/doc/user/vimindex.html#%3CScrollWheelRight%3E)  	`<ScrollWheelRight>`	move window six columns right [<S-ScrollWheelRight>](https://neovim.io/doc/user/vimindex.html#%3CS-ScrollWheelRight%3E)  	`<S-ScrollWheelRight>`	move window one page right
    -  **2.1 Text objects**** index**
        - These can be used after an operator or in Visual mode to select an object.
        - Tag		Command		   Op-pending and Visual-mode action
        - ------------------------------------------------------------------------------
        - [v_aquote](https://neovim.io/doc/user/motion.html#v_aquote)  	a"		   double quoted string [v_a'](https://neovim.io/doc/user/motion.html#v_a')  		a'		   single quoted string [v_a(](https://neovim.io/doc/user/motion.html#v_a%28)  		a(		   same as ab [v_a)](https://neovim.io/doc/user/motion.html#v_a%29)  		a)		   same as ab [v_a<](https://neovim.io/doc/user/motion.html#v_a%3C)  		a<		   "a―" from '<' to the matching '>' [v_a>](https://neovim.io/doc/user/motion.html#v_a%3E)  		a>		   same as a< [v_aB](https://neovim.io/doc/user/motion.html#v_aB)  		aB		   "a Block" from `[{` to `]}` (with brackets) [v_aW](https://neovim.io/doc/user/motion.html#v_aW)  		aW		   "a WORD" (with white space) [v_a[](https://neovim.io/doc/user/motion.html#v_a%5B)  		a["a []" from '[' to the matching ']' [v_a]](https://neovim.io/doc/user/motion.html#v_a%5D)  		a]		   same as a[ [v_a`](https://neovim.io/doc/user/motion.html#v_a%60)  		a`		   string in backticks [v_ab](https://neovim.io/doc/user/motion.html#v_ab)  		ab		   "a block" from "[(" to "])" (with braces) [v_ap](https://neovim.io/doc/user/motion.html#v_ap)  		ap		   "a paragraph" (with white space) [v_as](https://neovim.io/doc/user/motion.html#v_as)  		as		   "a sentence" (with white space) [v_at](https://neovim.io/doc/user/motion.html#v_at)  		at		   "a tag block" (with white space) [v_aw](https://neovim.io/doc/user/motion.html#v_aw)  		aw		   "a word" (with white space) [v_a{](https://neovim.io/doc/user/motion.html#v_a%7B)  		a{		   same as aB [v_a}](https://neovim.io/doc/user/motion.html#v_a%7D)  		a}		   same as aB [v_iquote](https://neovim.io/doc/user/motion.html#v_iquote)  	i"		   double quoted string without the quotes [v_i'](https://neovim.io/doc/user/motion.html#v_i')  		i'		   single quoted string without the quotes [v_i(](https://neovim.io/doc/user/motion.html#v_i%28)  		i(		   same as ib [v_i)](https://neovim.io/doc/user/motion.html#v_i%29)  		i)		   same as ib [v_i<](https://neovim.io/doc/user/motion.html#v_i%3C)  		i<		   "inner ↔" from '<' to the matching '>' [v_i>](https://neovim.io/doc/user/motion.html#v_i%3E)  		i>		   same as i< [v_iB](https://neovim.io/doc/user/motion.html#v_iB)  		iB		   "inner Block" from `[{` and `]}` [v_iW](https://neovim.io/doc/user/motion.html#v_iW)  		iW		   "inner WORD" [v_i[](https://neovim.io/doc/user/motion.html#v_i%5B)  		i["inner []" from '[' to the matching ']' [v_i]](https://neovim.io/doc/user/motion.html#v_i%5D)  		i]		   same as i[ [v_i`](https://neovim.io/doc/user/motion.html#v_i%60)  		i`		   string in backticks without the backticks [v_ib](https://neovim.io/doc/user/motion.html#v_ib)  		ib		   "inner block" from "[(" to "])" [v_ip](https://neovim.io/doc/user/motion.html#v_ip)  		ip		   "inner paragraph" [v_is](https://neovim.io/doc/user/motion.html#v_is)  		is		   "inner sentence" [v_it](https://neovim.io/doc/user/motion.html#v_it)  		it		   "inner tag block" [v_iw](https://neovim.io/doc/user/motion.html#v_iw)  		iw		   "inner word" [v_i{](https://neovim.io/doc/user/motion.html#v_i%7B)  		i{		   same as iB [v_i}](https://neovim.io/doc/user/motion.html#v_i%7D)  		i}		   same as iB
    -  **2.2 Window commands index**** **
        - Tag		Command		   Normal-mode action
        - ------------------------------------------------------------------------------
        - [CTRL-W_CTRL-B](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-B)  	`CTRL-W` `CTRL-B`	   same as "CTRL-W b" [CTRL-W_CTRL-C](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-C)  	`CTRL-W` `CTRL-C`	   no-op [CTRL-W_CTRL-D](https://neovim.io/doc/user/tagsrch.html#CTRL-W_CTRL-D)  	`CTRL-W` `CTRL-D`	   same as "CTRL-W d" [CTRL-W_CTRL-F](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-F)  	`CTRL-W` `CTRL-F`	   same as "CTRL-W f" 		`CTRL-W` `CTRL-G`	   same as "CTRL-W g .." [CTRL-W_CTRL-H](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-H)  	`CTRL-W` `CTRL-H`	   same as "CTRL-W h" [CTRL-W_CTRL-I](https://neovim.io/doc/user/tagsrch.html#CTRL-W_CTRL-I)  	`CTRL-W` `CTRL-I`	   same as "CTRL-W i" [CTRL-W_CTRL-J](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-J)  	`CTRL-W` `CTRL-J`	   same as "CTRL-W j" [CTRL-W_CTRL-K](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-K)  	`CTRL-W` `CTRL-K`	   same as "CTRL-W k" [CTRL-W_CTRL-L](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-L)  	`CTRL-W` `CTRL-L`	   same as "CTRL-W l" [CTRL-W_CTRL-N](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-N)  	`CTRL-W` `CTRL-N`	   same as "CTRL-W n" [CTRL-W_CTRL-O](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-O)  	`CTRL-W` `CTRL-O`	   same as "CTRL-W o" [CTRL-W_CTRL-P](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-P)  	`CTRL-W` `CTRL-P`	   same as "CTRL-W p" [CTRL-W_CTRL-Q](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-Q)  	`CTRL-W` `CTRL-Q`	   same as "CTRL-W q" [CTRL-W_CTRL-R](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-R)  	`CTRL-W` `CTRL-R`	   same as "CTRL-W r" [CTRL-W_CTRL-S](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-S)  	`CTRL-W` `CTRL-S`	   same as "CTRL-W s" [CTRL-W_CTRL-T](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-T)  	`CTRL-W` `CTRL-T`	   same as "CTRL-W t" [CTRL-W_CTRL-V](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-V)  	`CTRL-W` `CTRL-V`	   same as "CTRL-W v" [CTRL-W_CTRL-W](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-W)  	`CTRL-W` `CTRL-W`	   same as "CTRL-W w" [CTRL-W_CTRL-X](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-X)  	`CTRL-W` `CTRL-X`	   same as "CTRL-W x" [CTRL-W_CTRL-Z](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-Z)  	`CTRL-W` `CTRL-Z`	   same as "CTRL-W z" [CTRL-W_CTRL-]](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-%5D)  	`CTRL-W` `CTRL-]`	   same as "CTRL-W ]" [CTRL-W_CTRL-^](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-%5E)  	`CTRL-W` `CTRL-^`	   same as "CTRL-W ^" [CTRL-W_CTRL-_](https://neovim.io/doc/user/windows.html#CTRL-W_CTRL-_)  	`CTRL-W` `CTRL-_`	   same as "CTRL-W _" [CTRL-W_+](https://neovim.io/doc/user/windows.html#CTRL-W_%2B)  	`CTRL-W` +	   increase current window height N lines [CTRL-W_-](https://neovim.io/doc/user/windows.html#CTRL-W_-)  	`CTRL-W` -	   decrease current window height N lines [CTRL-W_<](https://neovim.io/doc/user/windows.html#CTRL-W_%3C)  	`CTRL-W` <	   decrease current window width N columns [CTRL-W_=](https://neovim.io/doc/user/windows.html#CTRL-W_%3D)  	`CTRL-W` =	   make all windows the same height & width [CTRL-W_>](https://neovim.io/doc/user/windows.html#CTRL-W_%3E)  	`CTRL-W` >	   increase current window width N columns [CTRL-W_H](https://neovim.io/doc/user/windows.html#CTRL-W_H)  	`CTRL-W` H	   move current window to the far left [CTRL-W_J](https://neovim.io/doc/user/windows.html#CTRL-W_J)  	`CTRL-W` J	   move current window to the very bottom [CTRL-W_K](https://neovim.io/doc/user/windows.html#CTRL-W_K)  	`CTRL-W` K	   move current window to the very top [CTRL-W_L](https://neovim.io/doc/user/windows.html#CTRL-W_L)  	`CTRL-W` L	   move current window to the far right [CTRL-W_P](https://neovim.io/doc/user/windows.html#CTRL-W_P)  	`CTRL-W` P	   go to preview window [CTRL-W_R](https://neovim.io/doc/user/windows.html#CTRL-W_R)  	`CTRL-W` R	   rotate windows upwards N times [CTRL-W_S](https://neovim.io/doc/user/windows.html#CTRL-W_S)  	`CTRL-W` S	   same as "CTRL-W s" [CTRL-W_T](https://neovim.io/doc/user/windows.html#CTRL-W_T)  	`CTRL-W` T	   move current window to a new tab page [CTRL-W_W](https://neovim.io/doc/user/windows.html#CTRL-W_W)  	`CTRL-W` W	   go to N previous window (wrap around) [CTRL-W_]](https://neovim.io/doc/user/windows.html#CTRL-W_%5D)  	`CTRL-W` ]	   split window and jump to tag under cursor [CTRL-W_^](https://neovim.io/doc/user/windows.html#CTRL-W_%5E)  	`CTRL-W` ^	   split current window and edit alternate 				   file N [CTRL-W__](https://neovim.io/doc/user/windows.html#CTRL-W__)  	`CTRL-W` _	   set current window height to N (default: 				   very high) [CTRL-W_b](https://neovim.io/doc/user/windows.html#CTRL-W_b)  	`CTRL-W` b	   go to bottom window [CTRL-W_c](https://neovim.io/doc/user/windows.html#CTRL-W_c)  	`CTRL-W` c	   close current window (like [:close](https://neovim.io/doc/user/windows.html#%3Aclose)) [CTRL-W_d](https://neovim.io/doc/user/tagsrch.html#CTRL-W_d)  	`CTRL-W` d	   split window and jump to definition under 				   the cursor [CTRL-W_f](https://neovim.io/doc/user/windows.html#CTRL-W_f)  	`CTRL-W` f	   split window and edit file name under the 				   cursor [CTRL-W_F](https://neovim.io/doc/user/windows.html#CTRL-W_F)  	`CTRL-W` F	   split window and edit file name under the 				   cursor and jump to the line number 				   following the file name. [CTRL-W_g_CTRL-]](https://neovim.io/doc/user/windows.html#CTRL-W_g_CTRL-%5D) `CTRL-W` g `CTRL-]`  split window and do [:tjump](https://neovim.io/doc/user/tagsrch.html#%3Atjump) to tag under 				   cursor [CTRL-W_g]](https://neovim.io/doc/user/windows.html#CTRL-W_g%5D)  	`CTRL-W` g ]	   split window and do [:tselect](https://neovim.io/doc/user/tagsrch.html#%3Atselect) for tag 				   under cursor [CTRL-W_g}](https://neovim.io/doc/user/windows.html#CTRL-W_g%7D)  	`CTRL-W` g }	   do a [:ptjump](https://neovim.io/doc/user/tagsrch.html#%3Aptjump) to the tag under the cursor [CTRL-W_gf](https://neovim.io/doc/user/windows.html#CTRL-W_gf)  	`CTRL-W` g f	   edit file name under the cursor in a new 				   tab page [CTRL-W_gF](https://neovim.io/doc/user/windows.html#CTRL-W_gF)  	`CTRL-W` g F	   edit file name under the cursor in a new 				   tab page and jump to the line number 				   following the file name. [CTRL-W_gt](https://neovim.io/doc/user/windows.html#CTRL-W_gt)  	`CTRL-W` g t	   same as `gt`: go to next tab page [CTRL-W_gT](https://neovim.io/doc/user/windows.html#CTRL-W_gT)  	`CTRL-W` g T	   same as `gT`: go to previous tab page [CTRL-W_g<Tab>](https://neovim.io/doc/user/tabpage.html#CTRL-W_g%3CTab%3E)  	`CTRL-W` g `<Tab>`	   same as [g<Tab>](https://neovim.io/doc/user/tabpage.html#g%3CTab%3E): go to last accessed tab 				   page [CTRL-W_h](https://neovim.io/doc/user/windows.html#CTRL-W_h)  	`CTRL-W` h	   go to Nth left window (stop at first window) [CTRL-W_i](https://neovim.io/doc/user/tagsrch.html#CTRL-W_i)  	`CTRL-W` i	   split window and jump to declaration of 				   identifier under the cursor [CTRL-W_j](https://neovim.io/doc/user/windows.html#CTRL-W_j)  	`CTRL-W` j	   go N windows down (stop at last window) [CTRL-W_k](https://neovim.io/doc/user/windows.html#CTRL-W_k)  	`CTRL-W` k	   go N windows up (stop at first window) [CTRL-W_l](https://neovim.io/doc/user/windows.html#CTRL-W_l)  	`CTRL-W` l	   go to Nth right window (stop at last window) [CTRL-W_n](https://neovim.io/doc/user/windows.html#CTRL-W_n)  	`CTRL-W` n	   open new window, N lines high [CTRL-W_o](https://neovim.io/doc/user/windows.html#CTRL-W_o)  	`CTRL-W` o	   close all but current window (like [:only](https://neovim.io/doc/user/windows.html#%3Aonly)) [CTRL-W_p](https://neovim.io/doc/user/windows.html#CTRL-W_p)  	`CTRL-W` p	   go to previous (last accessed) window [CTRL-W_q](https://neovim.io/doc/user/windows.html#CTRL-W_q)  	`CTRL-W` q	   quit current window (like [:quit](https://neovim.io/doc/user/editing.html#%3Aquit)) [CTRL-W_r](https://neovim.io/doc/user/windows.html#CTRL-W_r)  	`CTRL-W` r	   rotate windows downwards N times [CTRL-W_s](https://neovim.io/doc/user/windows.html#CTRL-W_s)  	`CTRL-W` s	   split current window in two parts, new 				   window N lines high [CTRL-W_t](https://neovim.io/doc/user/windows.html#CTRL-W_t)  	`CTRL-W` t	   go to top window [CTRL-W_v](https://neovim.io/doc/user/windows.html#CTRL-W_v)  	`CTRL-W` v	   split current window vertically, new window 				   N columns wide [CTRL-W_w](https://neovim.io/doc/user/windows.html#CTRL-W_w)  	`CTRL-W` w	   go to N next window (wrap around) [CTRL-W_x](https://neovim.io/doc/user/windows.html#CTRL-W_x)  	`CTRL-W` x	   exchange current window with window N 				   (default: next window) [CTRL-W_z](https://neovim.io/doc/user/windows.html#CTRL-W_z)  	`CTRL-W` z	   close preview window [CTRL-W_bar](https://neovim.io/doc/user/windows.html#CTRL-W_bar)  	`CTRL-W` |	   set window width to N columns [CTRL-W_}](https://neovim.io/doc/user/windows.html#CTRL-W_%7D)  	`CTRL-W` }	   show tag under cursor in preview window [CTRL-W_<Down>](https://neovim.io/doc/user/windows.html#CTRL-W_%3CDown%3E)  	`CTRL-W` `<Down>`	   same as "CTRL-W j" [CTRL-W_<Up>](https://neovim.io/doc/user/windows.html#CTRL-W_%3CUp%3E)  	`CTRL-W` `<Up>`	   same as "CTRL-W k" [CTRL-W_<Left>](https://neovim.io/doc/user/windows.html#CTRL-W_%3CLeft%3E)  	`CTRL-W` `<Left>`	   same as "CTRL-W h" [CTRL-W_<Right>](https://neovim.io/doc/user/windows.html#CTRL-W_%3CRight%3E) `CTRL-W` `<Right>`	   same as "CTRL-W l"
    -  **2.3 Square bracket commands**** **
        - Tag		Char	      Note Normal-mode action
        - ------------------------------------------------------------------------------
        - [[_CTRL-D](https://neovim.io/doc/user/tagsrch.html#%5B_CTRL-D)  	[ `CTRL-D`	   jump to first #define found in current and 				   included files matching the word under the 				   cursor, start searching at beginning of 				   current file [[_CTRL-I](https://neovim.io/doc/user/tagsrch.html#%5B_CTRL-I)  	[ `CTRL-I`	   jump to first line in current and included 				   files that contains the word under the 				   cursor, start searching at beginning of 				   current file [[#](https://neovim.io/doc/user/motion.html#%5B%23)  		[#		1  cursor to N previous unmatched #if, #else 				   or #ifdef [['](https://neovim.io/doc/user/motion.html#%5B')  		['		1  cursor to previous lowercase mark, on first 				   non-blank [[(](https://neovim.io/doc/user/motion.html#%5B%28)  		[(		1  cursor N times back to unmatched '(' [[star](https://neovim.io/doc/user/motion.html#%5Bstar)  		[*		1  same as "[/" [[`](https://neovim.io/doc/user/motion.html#%5B%60)  		[		1  cursor to previous lowercase mark [[/](https://neovim.io/doc/user/motion.html#%5B%2F)  		[/		1  cursor to N previous start of a C comment [[D](https://neovim.io/doc/user/tagsrch.html#%5BD)  		[D		   list all defines found in current and 				   included files matching the word under the 				   cursor, start searching at beginning of 				   current file [[I](https://neovim.io/doc/user/tagsrch.html#%5BI)  		[I		   list all lines found in current and 				   included files that contain the word under 				   the cursor, start searching at beginning of 				   current file [[P](https://neovim.io/doc/user/change.html#%5BP)  		[P		2  same as "[p" [[[](https://neovim.io/doc/user/motion.html#%5B%5B)  		[[		1  cursor N sections backward [[]](https://neovim.io/doc/user/motion.html#%5B%5D)  		[]		1  cursor N SECTIONS backward [[c](https://neovim.io/doc/user/diff.html#%5Bc)  		[c		1  cursor N times backwards to start of change [[d](https://neovim.io/doc/user/tagsrch.html#%5Bd)  		[d		   show first #define found in current and 				   included files matching the word under the 				   cursor, start searching at beginning of 				   current file [[f](https://neovim.io/doc/user/deprecated.html#%5Bf)  		[f		   same as "gf" [[i](https://neovim.io/doc/user/tagsrch.html#%5Bi)  		[i		   show first line found in current and 				   included files that contains the word under 				   the cursor, start searching at beginning of 				   current file [[m](https://neovim.io/doc/user/motion.html#%5Bm)  		[m		1  cursor N times back to start of member 				   function [[p](https://neovim.io/doc/user/change.html#%5Bp)  		[p		2  like "P", but adjust indent to current line [[s](https://neovim.io/doc/user/spell.html#%5Bs)  		[s		1  move to the previous misspelled word [[z](https://neovim.io/doc/user/fold.html#%5Bz)  		[z		1  move to start of open fold [[{](https://neovim.io/doc/user/motion.html#%5B%7B)  		[{		1  cursor N times back to unmatched '{' [[<MiddleMouse>](https://neovim.io/doc/user/change.html#%5B%3CMiddleMouse%3E) [`<MiddleMouse>`	2  same as "[p"
        - [ ] _CTRL-D](https://neovim.io/doc/user/tagsrch.html#%5D_CTRL-D)  	] `CTRL-D`	   jump to first #define found in current and 				   included files matching the word under the 				   cursor, start searching at cursor position []_CTRL-I](https://neovim.io/doc/user/tagsrch.html#%5D_CTRL-I)  	] `CTRL-I`	   jump to first line in current and included 				   files that contains the word under the 				   cursor, start searching at cursor position []#](https://neovim.io/doc/user/motion.html#%5D%23)  		]#		1  cursor to N next unmatched #endif or #else []'](https://neovim.io/doc/user/motion.html#%5D')  		]'		1  cursor to next lowercase mark, on first 				   non-blank [])](https://neovim.io/doc/user/motion.html#%5D%29)  		])		1  cursor N times forward to unmatched ')' []star](https://neovim.io/doc/user/motion.html#%5Dstar)  		]*		1  same as "]/" []`](https://neovim.io/doc/user/motion.html#%5D%60)  		]`		1  cursor to next lowercase mark []/](https://neovim.io/doc/user/motion.html#%5D%2F)  		]/		1  cursor to N next end of a C comment []D](https://neovim.io/doc/user/tagsrch.html#%5DD)  		]D		   list all #defines found in current and 				   included files matching the word under the 				   cursor, start searching at cursor position []I](https://neovim.io/doc/user/tagsrch.html#%5DI)  		]I		   list all lines found in current and 				   included files that contain the word under 				   the cursor, start searching at cursor 				   position []P](https://neovim.io/doc/user/change.html#%5DP)  		]P		2  same as "[p" [][](https://neovim.io/doc/user/motion.html#%5D%5B)  		][1  cursor N SECTIONS forward []]](https://neovim.io/doc/user/motion.html#%5D%5D)  		]]		1  cursor N sections forward []c](https://neovim.io/doc/user/diff.html#%5Dc)  		]c		1  cursor N times forward to start of change []d](https://neovim.io/doc/user/tagsrch.html#%5Dd)  		]d		   show first #define found in current and 				   included files matching the word under the 				   cursor, start searching at cursor position []f](https://neovim.io/doc/user/deprecated.html#%5Df)  		]f		   same as "gf" []i](https://neovim.io/doc/user/tagsrch.html#%5Di)  		]i		   show first line found in current and 				   included files that contains the word under 				   the cursor, start searching at cursor 				   position []m](https://neovim.io/doc/user/motion.html#%5Dm)  		]m		1  cursor N times forward to end of member 				   function []p](https://neovim.io/doc/user/change.html#%5Dp)  		]p		2  like "p", but adjust indent to current line []s](https://neovim.io/doc/user/spell.html#%5Ds)  		]s		1  move to next misspelled word []z](https://neovim.io/doc/user/fold.html#%5Dz)  		]z		1  move to end of open fold []}](https://neovim.io/doc/user/motion.html#%5D%7D)  		]}		1  cursor N times forward to unmatched '}' []<MiddleMouse>](https://neovim.io/doc/user/change.html#%5D%3CMiddleMouse%3E) ]<MiddleMouse>	2  same as "]p"
    -  **2.4 Commands starting with 'g**** **
        - Tag		Char	      Note Normal-mode action
        - ------------------------------------------------------------------------------
        - [g_CTRL-G](https://neovim.io/doc/user/editing.html#g_CTRL-G)  	g `CTRL-G`	   show information about current cursor 				   position [g_CTRL-H](https://neovim.io/doc/user/visual.html#g_CTRL-H)  	g `CTRL-H`	   start Select block mode [g_CTRL-]](https://neovim.io/doc/user/tagsrch.html#g_CTRL-%5D)  	g `CTRL-]`	   [:tjump](https://neovim.io/doc/user/tagsrch.html#%3Atjump) to the tag under the cursor [g#](https://neovim.io/doc/user/pattern.html#g%23)  		g#		1  like "#", but without using "\<" and "\>" [g$](https://neovim.io/doc/user/motion.html#g%24)  		g$		1  when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off go to rightmost character of 				   the current line that is on the screen; 				   when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') on go to the rightmost character 				   of the current screen line [g&](https://neovim.io/doc/user/change.html#g%26)  		g&		2  repeat last ":s" on all lines [g'](https://neovim.io/doc/user/motion.html#g')  		g'{mark}	1  like ['](https://neovim.io/doc/user/motion.html#') but without changing the jumplist [g`](https://neovim.io/doc/user/motion.html#g%60)  		g`{mark}	1  like [`](https://neovim.io/doc/user/motion.html#%60) but without changing the jumplist [gstar](https://neovim.io/doc/user/pattern.html#gstar)  		g*		1  like "*", but without using "\<" and "\>" [g+](https://neovim.io/doc/user/undo.html#g%2B)  		g+		   go to newer text state N times [g,](https://neovim.io/doc/user/motion.html#g%2C)  		g,		1  go to N newer position in change list [g-](https://neovim.io/doc/user/undo.html#g-)  		g-		   go to older text state N times [g0](https://neovim.io/doc/user/motion.html#g0)  		g0		1  when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off go to leftmost character of 				   the current line that is on the screen; 				   when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') on go to the leftmost character 				   of the current screen line [g8](https://neovim.io/doc/user/various.html#g8)  		g8		   print hex value of bytes used in UTF-8 				   character under the cursor [g;](https://neovim.io/doc/user/motion.html#g%3B)  		g;		1  go to N older position in change list [g<](https://neovim.io/doc/user/message.html#g%3C)  		g<		   display previous command output [g?](https://neovim.io/doc/user/change.html#g%3F)  		g?		2  Rot13 encoding operator [g?g?](https://neovim.io/doc/user/change.html#g%3Fg%3F)  		g??		2  Rot13 encode current line [g?g?](https://neovim.io/doc/user/change.html#g%3Fg%3F)  		g?g?		2  Rot13 encode current line [gD](https://neovim.io/doc/user/pattern.html#gD)  		gD		1  go to definition of word under the cursor 				   in current file [gE](https://neovim.io/doc/user/motion.html#gE)  		gE		1  go backwards to the end of the previous 				   WORD [gH](https://neovim.io/doc/user/visual.html#gH)  		gH		   start Select line mode [gI](https://neovim.io/doc/user/insert.html#gI)  		gI		2  like "I", but always start in column 1 [gJ](https://neovim.io/doc/user/change.html#gJ)  		gJ		2  join lines without inserting space [gN](https://neovim.io/doc/user/visual.html#gN)  		gN	      1,2  find the previous match with the last used 				   search pattern and Visually select it [gP](https://neovim.io/doc/user/change.html#gP)  		["x]gP		2  put the text [from register x] before the 				   cursor N times, leave the cursor after it [gQ](https://neovim.io/doc/user/intro.html#gQ)  		gQ		   switch to "Ex" mode with Vim editing [gR](https://neovim.io/doc/user/change.html#gR)  		gR		2  enter Virtual Replace mode [gT](https://neovim.io/doc/user/tabpage.html#gT)  		gT		   go to the previous tab page [gU](https://neovim.io/doc/user/change.html#gU)  		gU{motion}	2  make Nmove text uppercase [gV](https://neovim.io/doc/user/visual.html#gV)  		gV		   don't reselect the previous Visual area 				   when executing a mapping or menu in Select 				   mode [g]](https://neovim.io/doc/user/tagsrch.html#g%5D)  		g]		   :tselect on the tag under the cursor [g^](https://neovim.io/doc/user/motion.html#g%5E)  		g^		1  when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off go to leftmost non-white 				   character of the current line that is on 				   the screen; when ['wrap'](https://neovim.io/doc/user/options.html#'wrap')`
        - `on go to the 				   leftmost non-white character of the current 				   screen line [g_](https://neovim.io/doc/user/motion.html#g_)  		g_		1  cursor to the last CHAR N - 1 lines lower [ga](https://neovim.io/doc/user/various.html#ga)  		ga		   print ascii value of character under the 				   cursor [gd](https://neovim.io/doc/user/pattern.html#gd)  		gd		1  go to definition of word under the cursor 				   in current function [ge](https://neovim.io/doc/user/motion.html#ge)  		ge		1  go backwards to the end of the previous 				   word [gf](https://neovim.io/doc/user/editing.html#gf)  		gf		   start editing the file whose name is under 				   the cursor [gF](https://neovim.io/doc/user/editing.html#gF)  		gF		   start editing the file whose name is under 				   the cursor and jump to the line number 				   following the filename. [gg](https://neovim.io/doc/user/motion.html#gg)  		gg		1  cursor to line N, default first line [gh](https://neovim.io/doc/user/visual.html#gh)  		gh		   start Select mode [gi](https://neovim.io/doc/user/insert.html#gi)  		gi		2  like "i", but first move to the ['^](https://neovim.io/doc/user/motion.html#'%5E) mark [gj](https://neovim.io/doc/user/motion.html#gj)  		gj		1  like "j", but when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') on go N screen 				   lines down [gk](https://neovim.io/doc/user/motion.html#gk)  		gk		1  like "k", but when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') on go N screen 				   lines up [gm](https://neovim.io/doc/user/motion.html#gm)  		gm		1  go to character at middle of the screenline [gM](https://neovim.io/doc/user/motion.html#gM)  		gM		1  go to character at middle of the text line [gn](https://neovim.io/doc/user/visual.html#gn)  		gn	      1,2  find the next match with the last used 				   search pattern and Visually select it [go](https://neovim.io/doc/user/motion.html#go)  		go		1  cursor to byte N in the buffer [gp](https://neovim.io/doc/user/change.html#gp)  		["x]gp		2  put the text [from register x] after the 				   cursor N times, leave the cursor after it [gq](https://neovim.io/doc/user/change.html#gq)  		gq{motion}	2  format Nmove text [gr](https://neovim.io/doc/user/change.html#gr)  		gr{char}	2  virtual replace N chars with `{char}` [gs](https://neovim.io/doc/user/various.html#gs)  		gs		   go to sleep for N seconds (default 1) [gt](https://neovim.io/doc/user/tabpage.html#gt)  		gt		   go to the next tab page [gu](https://neovim.io/doc/user/change.html#gu)  		gu{motion}	2  make Nmove text lowercase [gv](https://neovim.io/doc/user/visual.html#gv)  		gv		   reselect the previous Visual area [gw](https://neovim.io/doc/user/change.html#gw)  		gw{motion}	2  format Nmove text and keep cursor [gx](https://neovim.io/doc/user/various.html#gx)  		gx		   execute application for filepath at cursor [g@](https://neovim.io/doc/user/map.html#g%40)  		g@{motion}	   call ['operatorfunc'](https://neovim.io/doc/user/options.html#'operatorfunc') [g~](https://neovim.io/doc/user/change.html#g~)  		g~{motion}	2  swap case for Nmove text [g<Down>](https://neovim.io/doc/user/motion.html#g%3CDown%3E)  	g<Down>		1  same as "gj" [g<End>](https://neovim.io/doc/user/motion.html#g%3CEnd%3E)  	g<End>		1  same as "g$" [g<Home>](https://neovim.io/doc/user/motion.html#g%3CHome%3E)  	g<Home>		1  same as "g0" [g<LeftMouse>](https://neovim.io/doc/user/tagsrch.html#g%3CLeftMouse%3E)  	g<LeftMouse>	   same as `<C-LeftMouse>` 		g<MiddleMouse>	   same as `<C-MiddleMouse>` [g<RightMouse>](https://neovim.io/doc/user/tagsrch.html#g%3CRightMouse%3E)  	g<RightMouse>	   same as `<C-RightMouse>` [g<Tab>](https://neovim.io/doc/user/tabpage.html#g%3CTab%3E)  	g<Tab>		   go to last accessed tab page [g<Up>](https://neovim.io/doc/user/motion.html#g%3CUp%3E)  		g<Up>		1  same as "gk"
    -  **2.5 Commands starting with 'z**** **
        - Tag		Char	      Note Normal-mode action
        - ------------------------------------------------------------------------------
        - [z<CR>](https://neovim.io/doc/user/scroll.html#z%3CCR%3E)  		z<CR>		   redraw, cursor line to top of window, 				   cursor on first non-blank [zN<CR>](https://neovim.io/doc/user/scroll.html#zN%3CCR%3E)  	z{height}<CR>	   redraw, make window `{height}` lines high [z+](https://neovim.io/doc/user/scroll.html#z%2B)  		z+		   cursor on line N (default line below 				   window), otherwise like "z<CR>" [z-](https://neovim.io/doc/user/scroll.html#z-)  		z-		   redraw, cursor line at bottom of window, 				   cursor on first non-blank [z.](https://neovim.io/doc/user/scroll.html#z.)  		z.		   redraw, cursor line to center of window, 				   cursor on first non-blank [z=](https://neovim.io/doc/user/spell.html#z%3D)  		z=		   give spelling suggestions [zA](https://neovim.io/doc/user/fold.html#zA)  		zA		   open a closed fold or close an open fold 				   recursively [zC](https://neovim.io/doc/user/fold.html#zC)  		zC		   close folds recursively [zD](https://neovim.io/doc/user/fold.html#zD)  		zD		   delete folds recursively [zE](https://neovim.io/doc/user/fold.html#zE)  		zE		   eliminate all folds [zF](https://neovim.io/doc/user/fold.html#zF)  		zF		   create a fold for N lines [zG](https://neovim.io/doc/user/spell.html#zG)  		zG		   temporarily mark word as correctly spelled [zH](https://neovim.io/doc/user/scroll.html#zH)  		zH		   when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off scroll half a screenwidth 				   to the right [zL](https://neovim.io/doc/user/scroll.html#zL)  		zL		   when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off scroll half a screenwidth 				   to the left [zM](https://neovim.io/doc/user/fold.html#zM)  		zM		   set ['foldlevel'](https://neovim.io/doc/user/options.html#'foldlevel') to zero [zN](https://neovim.io/doc/user/fold.html#zN)  		zN		   set ['foldenable'](https://neovim.io/doc/user/options.html#'foldenable') [zO](https://neovim.io/doc/user/fold.html#zO)  		zO		   open folds recursively [zR](https://neovim.io/doc/user/fold.html#zR)  		zR		   set ['foldlevel'](https://neovim.io/doc/user/options.html#'foldlevel') to the deepest fold [zW](https://neovim.io/doc/user/spell.html#zW)  		zW		   temporarily mark word as incorrectly spelled [zX](https://neovim.io/doc/user/fold.html#zX)  		zX		   re-apply ['foldlevel'](https://neovim.io/doc/user/options.html#'foldlevel') [z^](https://neovim.io/doc/user/scroll.html#z%5E)  		z^		   cursor on line N (default line above 				   window), otherwise like "z-" [za](https://neovim.io/doc/user/fold.html#za)  		za		   open a closed fold, close an open fold [zb](https://neovim.io/doc/user/scroll.html#zb)  		zb		   redraw, cursor line at bottom of window [zc](https://neovim.io/doc/user/fold.html#zc)  		zc		   close a fold [zd](https://neovim.io/doc/user/fold.html#zd)  		zd		   delete a fold [ze](https://neovim.io/doc/user/scroll.html#ze)  		ze		   when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off scroll horizontally to 				   position the cursor at the end (right side) 				   of the screen [zf](https://neovim.io/doc/user/fold.html#zf)  		zf{motion}	   create a fold for Nmove text [zg](https://neovim.io/doc/user/spell.html#zg)  		zg		   permanently mark word as correctly spelled [zh](https://neovim.io/doc/user/scroll.html#zh)  		zh		   when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off scroll screen N characters 				   to the right [zi](https://neovim.io/doc/user/fold.html#zi)  		zi		   toggle ['foldenable'](https://neovim.io/doc/user/options.html#'foldenable') [zj](https://neovim.io/doc/user/fold.html#zj)  		zj		1  move to the start of the next fold [zk](https://neovim.io/doc/user/fold.html#zk)  		zk		1  move to the end of the previous fold [zl](https://neovim.io/doc/user/scroll.html#zl)  		zl		   when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off scroll screen N characters 				   to the left [zm](https://neovim.io/doc/user/fold.html#zm)  		zm		   subtract one from ['foldlevel'](https://neovim.io/doc/user/options.html#'foldlevel') [zn](https://neovim.io/doc/user/fold.html#zn)  		zn		   reset ['foldenable'](https://neovim.io/doc/user/options.html#'foldenable') [zo](https://neovim.io/doc/user/fold.html#zo)  		zo		   open fold [zp](https://neovim.io/doc/user/change.html#zp)  		zp		   paste in block-mode without trailing spaces [zP](https://neovim.io/doc/user/change.html#zP)  		zP		   paste in block-mode without trailing spaces [zr](https://neovim.io/doc/user/fold.html#zr)  		zr		   add one to ['foldlevel'](https://neovim.io/doc/user/options.html#'foldlevel') [zs](https://neovim.io/doc/user/scroll.html#zs)  		zs		   when ['wrap'](https://neovim.io/doc/user/options.html#'wrap') off scroll horizontally to 				   position the cursor at the start (left 				   side) of the screen [zt](https://neovim.io/doc/user/scroll.html#zt)  		zt		   redraw, cursor line at top of window [zuw](https://neovim.io/doc/user/spell.html#zuw)  		zuw		   undo [zw](https://neovim.io/doc/user/spell.html#zw) [zug](https://neovim.io/doc/user/spell.html#zug)  		zug		   undo [zg](https://neovim.io/doc/user/spell.html#zg) [zuW](https://neovim.io/doc/user/spell.html#zuW)  		zuW		   undo [zW](https://neovim.io/doc/user/spell.html#zW) [zuG](https://neovim.io/doc/user/spell.html#zuG)  		zuG		   undo [zG](https://neovim.io/doc/user/spell.html#zG) [zv](https://neovim.io/doc/user/fold.html#zv)  		zv		   open enough folds to view the cursor line [zw](https://neovim.io/doc/user/spell.html#zw)  		zw		   permanently mark word as incorrectly spelled [zx](https://neovim.io/doc/user/fold.html#zx)  		zx		   re-apply ['foldlevel'](https://neovim.io/doc/user/options.html#'foldlevel') and do "zv" [zy](https://neovim.io/doc/user/change.html#zy)  		zy		   yank without trailing spaces [zz](https://neovim.io/doc/user/scroll.html#zz)  		zz		   redraw, cursor line at center of window [z<Left>](https://neovim.io/doc/user/scroll.html#z%3CLeft%3E)  	z<Left>		   same as "zh" [z<Right>](https://neovim.io/doc/user/scroll.html#z%3CRight%3E)  	z<Right>	   same as "zl"
    -  **2.6 Operator-pending mode index**** **
        - These can be used after an operator, but before a `{motion}` has been entered.
        - Tag		Char		Operator-pending-mode action
        - ------------------------------------------------------------------------------
        - [o_v](https://neovim.io/doc/user/motion.html#o_v)  		v		force operator to work charwise [o_V](https://neovim.io/doc/user/motion.html#o_V)  		V		force operator to work linewise [o_CTRL-V](https://neovim.io/doc/user/motion.html#o_CTRL-V)  	`CTRL-V`		force operator to work blockwise
    -  **3. Visual mode indes**** **
        - Most commands in Visual mode are the same as in Normal mode.  The ones listed here are those that are different.
        - Tag		Command	      Note Visual-mode action
        - ------------------------------------------------------------------------------
        - [v_CTRL-\_CTRL-N](https://neovim.io/doc/user/intro.html#v_CTRL-%5C_CTRL-N) `CTRL-\` `CTRL-N`	   stop Visual mode [v_CTRL-\_CTRL-G](https://neovim.io/doc/user/intro.html#v_CTRL-%5C_CTRL-G) `CTRL-\` `CTRL-G`	   go to Normal mode [v_CTRL-A](https://neovim.io/doc/user/change.html#v_CTRL-A)  	`CTRL-A`		2  add N to number in highlighted text [v_CTRL-C](https://neovim.io/doc/user/visual.html#v_CTRL-C)  	`CTRL-C`		   stop Visual mode [v_CTRL-G](https://neovim.io/doc/user/visual.html#v_CTRL-G)  	`CTRL-G`		   toggle between Visual mode and Select mode [v_<BS>](https://neovim.io/doc/user/change.html#v_%3CBS%3E)  	`<BS>`		2  Select mode: delete highlighted area [v_CTRL-H](https://neovim.io/doc/user/change.html#v_CTRL-H)  	`CTRL-H`		2  same as `<BS>` [v_CTRL-O](https://neovim.io/doc/user/visual.html#v_CTRL-O)  	`CTRL-O`		   switch from Select to Visual mode for one 				   command [v_CTRL-V](https://neovim.io/doc/user/visual.html#v_CTRL-V)  	`CTRL-V`		   make Visual mode blockwise or stop Visual 				   mode [v_CTRL-X](https://neovim.io/doc/user/change.html#v_CTRL-X)  	`CTRL-X`		2  subtract N from number in highlighted text [v_<Esc>](https://neovim.io/doc/user/visual.html#v_%3CEsc%3E)  	`<Esc>`		   stop Visual mode [v_CTRL-]](https://neovim.io/doc/user/tagsrch.html#v_CTRL-%5D)  	`CTRL-]`		   jump to highlighted tag [v_!](https://neovim.io/doc/user/change.html#v_%21)  		!{filter}	2  filter the highlighted lines through the 				   external command `{filter}` [v_:](https://neovim.io/doc/user/cmdline.html#v_%3A)  		:		   start a command-line with the highlighted 				   lines as a range [v_<](https://neovim.io/doc/user/change.html#v_%3C)  		<		2  shift the highlighted lines one 				   ['shiftwidth'](https://neovim.io/doc/user/options.html#'shiftwidth') left [v_=](https://neovim.io/doc/user/change.html#v_%3D)  		=		2  filter the highlighted lines through the 				   external program given with the ['equalprg'](https://neovim.io/doc/user/options.html#'equalprg') 				   option [v_>](https://neovim.io/doc/user/change.html#v_%3E)  		>		2  shift the highlighted lines one 				   ['shiftwidth'](https://neovim.io/doc/user/options.html#'shiftwidth') right [v_b_A](https://neovim.io/doc/user/visual.html#v_b_A)  		A		2  block mode: append same text in all lines, 				   after the highlighted area [v_C](https://neovim.io/doc/user/change.html#v_C)  		C		2  delete the highlighted lines and start 				   insert [v_D](https://neovim.io/doc/user/change.html#v_D)  		D		2  delete the highlighted lines [v_b_I](https://neovim.io/doc/user/visual.html#v_b_I)  		I		2  block mode: insert same text in all lines, 				   before the highlighted area [v_J](https://neovim.io/doc/user/change.html#v_J)  		J		2  join the highlighted lines [v_K](https://neovim.io/doc/user/various.html#v_K)  		K		   run ['keywordprg'](https://neovim.io/doc/user/options.html#'keywordprg') on the highlighted area [v_O](https://neovim.io/doc/user/visual.html#v_O)  		O		   move horizontally to other corner of area [v_P](https://neovim.io/doc/user/change.html#v_P)  		P		   replace highlighted area with register 				   contents; registers are unchanged [v_R](https://neovim.io/doc/user/change.html#v_R)  		R		2  delete the highlighted lines and start 				   insert [v_S](https://neovim.io/doc/user/change.html#v_S)  		S		2  delete the highlighted lines and start 				   insert [v_U](https://neovim.io/doc/user/change.html#v_U)  		U		2  make highlighted area uppercase [v_V](https://neovim.io/doc/user/visual.html#v_V)  		V		   make Visual mode linewise or stop Visual 				   mode [v_X](https://neovim.io/doc/user/change.html#v_X)  		X		2  delete the highlighted lines [v_Y](https://neovim.io/doc/user/change.html#v_Y)  		Y		   yank the highlighted lines [v_aquote](https://neovim.io/doc/user/motion.html#v_aquote)  	a"		   extend highlighted area with a double 				   quoted string [v_a'](https://neovim.io/doc/user/motion.html#v_a')  		a'		   extend highlighted area with a single 				   quoted string [v_a(](https://neovim.io/doc/user/motion.html#v_a%28)  		a(		   same as ab [v_a)](https://neovim.io/doc/user/motion.html#v_a%29)  		a)		   same as ab [v_a<](https://neovim.io/doc/user/motion.html#v_a%3C)  		a<		   extend highlighted area with a―block [v_a>](https://neovim.io/doc/user/motion.html#v_a%3E)  		a>		   same as a< [v_aB](https://neovim.io/doc/user/motion.html#v_aB)  		aB		   extend highlighted area with a {} block [v_aW](https://neovim.io/doc/user/motion.html#v_aW)  		aW		   extend highlighted area with "a WORD" [v_a[](https://neovim.io/doc/user/motion.html#v_a%5B)  		a[extend highlighted area with a [] block [v_a]](https://neovim.io/doc/user/motion.html#v_a%5D)  		a]		   same as a[ [v_a`](https://neovim.io/doc/user/motion.html#v_a%60)  		a`		   extend highlighted area with a backtick 				   quoted string [v_ab](https://neovim.io/doc/user/motion.html#v_ab)  		ab		   extend highlighted area with a () block [v_ap](https://neovim.io/doc/user/motion.html#v_ap)  		ap		   extend highlighted area with a paragraph [v_as](https://neovim.io/doc/user/motion.html#v_as)  		as		   extend highlighted area with a sentence [v_at](https://neovim.io/doc/user/motion.html#v_at)  		at		   extend highlighted area with a tag block [v_aw](https://neovim.io/doc/user/motion.html#v_aw)  		aw		   extend highlighted area with "a word" [v_a{](https://neovim.io/doc/user/motion.html#v_a%7B)  		a{		   same as aB [v_a}](https://neovim.io/doc/user/motion.html#v_a%7D)  		a}		   same as aB [v_c](https://neovim.io/doc/user/change.html#v_c)  		c		2  delete highlighted area and start insert [v_d](https://neovim.io/doc/user/change.html#v_d)  		d		2  delete highlighted area [v_g_CTRL-A](https://neovim.io/doc/user/change.html#v_g_CTRL-A)  	g `CTRL-A`	2  add N to number in highlighted text [v_g_CTRL-X](https://neovim.io/doc/user/change.html#v_g_CTRL-X)  	g `CTRL-X`	2  subtract N from number in highlighted text [v_gJ](https://neovim.io/doc/user/change.html#v_gJ)  		gJ		2  join the highlighted lines without 				   inserting spaces [v_gq](https://neovim.io/doc/user/change.html#v_gq)  		gq		2  format the highlighted lines [v_gv](https://neovim.io/doc/user/visual.html#v_gv)  		gv		   exchange current and previous highlighted 				   area [v_iquote](https://neovim.io/doc/user/motion.html#v_iquote)  	i"		   extend highlighted area with a double 				   quoted string (without quotes) [v_i'](https://neovim.io/doc/user/motion.html#v_i')  		i'		   extend highlighted area with a single 				   quoted string (without quotes) [v_i(](https://neovim.io/doc/user/motion.html#v_i%28)  		i(		   same as ib [v_i)](https://neovim.io/doc/user/motion.html#v_i%29)  		i)		   same as ib [v_i<](https://neovim.io/doc/user/motion.html#v_i%3C)  		i<		   extend highlighted area with inner ↔ block [v_i>](https://neovim.io/doc/user/motion.html#v_i%3E)  		i>		   same as i< [v_iB](https://neovim.io/doc/user/motion.html#v_iB)  		iB		   extend highlighted area with inner {} block [v_iW](https://neovim.io/doc/user/motion.html#v_iW)  		iW		   extend highlighted area with "inner WORD" [v_i[](https://neovim.io/doc/user/motion.html#v_i%5B)  		i[extend highlighted area with inner [] block [v_i]](https://neovim.io/doc/user/motion.html#v_i%5D)  		i]		   same as i[ [v_i`](https://neovim.io/doc/user/motion.html#v_i%60)  		i`		   extend highlighted area with a backtick 				   quoted string (without the backticks) [v_ib](https://neovim.io/doc/user/motion.html#v_ib)  		ib		   extend highlighted area with inner () block [v_ip](https://neovim.io/doc/user/motion.html#v_ip)  		ip		   extend highlighted area with inner paragraph [v_is](https://neovim.io/doc/user/motion.html#v_is)  		is		   extend highlighted area with inner sentence [v_it](https://neovim.io/doc/user/motion.html#v_it)  		it		   extend highlighted area with inner tag block [v_iw](https://neovim.io/doc/user/motion.html#v_iw)  		iw		   extend highlighted area with "inner word" [v_i{](https://neovim.io/doc/user/motion.html#v_i%7B)  		i{		   same as iB [v_i}](https://neovim.io/doc/user/motion.html#v_i%7D)  		i}		   same as iB [v_o](https://neovim.io/doc/user/visual.html#v_o)  		o		   move cursor to other corner of area [v_p](https://neovim.io/doc/user/change.html#v_p)  		p		   replace highlighted area with register 				   contents; deleted text in unnamed register [v_r](https://neovim.io/doc/user/change.html#v_r)  		r		2  replace highlighted area with a character [v_s](https://neovim.io/doc/user/change.html#v_s)  		s		2  delete highlighted area and start insert [v_u](https://neovim.io/doc/user/change.html#v_u)  		u		2  make highlighted area lowercase [v_v](https://neovim.io/doc/user/visual.html#v_v)  		v		   make Visual mode charwise or stop 				   Visual mode [v_x](https://neovim.io/doc/user/change.html#v_x)  		x		2  delete the highlighted area [v_y](https://neovim.io/doc/user/change.html#v_y)  		y		   yank the highlighted area [v_~](https://neovim.io/doc/user/change.html#v_~)  		~		2  swap case for the highlighted area
    -  **4. Command-line editing**** **
        - Get to the command-line with the ':', '!', '/' or '?' commands. Normal characters are inserted at the current cursor position. "Completion" below refers to context-sensitive completion.  It will complete file names, tags, commands etc. as appropriate.
        - Tag		Command		Command-line editing-mode action
        - ------------------------------------------------------------------------------
            - `CTRL-@`		not used [c_CTRL-A](https://neovim.io/doc/user/cmdline.html#c_CTRL-A)  	`CTRL-A`		do completion on the pattern in front of the 				cursor and insert all matches [c_CTRL-B](https://neovim.io/doc/user/cmdline.html#c_CTRL-B)  	`CTRL-B`		cursor to begin of command-line [c_CTRL-C](https://neovim.io/doc/user/cmdline.html#c_CTRL-C)  	`CTRL-C`		same as `<Esc>` [c_CTRL-D](https://neovim.io/doc/user/cmdline.html#c_CTRL-D)  	`CTRL-D`		list completions that match the pattern in 				front of the cursor [c_CTRL-E](https://neovim.io/doc/user/cmdline.html#c_CTRL-E)  	`CTRL-E`		cursor to end of command-line ['cedit'](https://neovim.io/doc/user/options.html#'cedit')		`CTRL-F`		default value for ['cedit'](https://neovim.io/doc/user/options.html#'cedit'): opens the 				command-line window; otherwise not used [c_CTRL-G](https://neovim.io/doc/user/cmdline.html#c_CTRL-G)  	`CTRL-G`		next match when ['incsearch'](https://neovim.io/doc/user/options.html#'incsearch') is active [c_<BS>](https://neovim.io/doc/user/cmdline.html#c_%3CBS%3E)  	`<BS>`		delete the character in front of the cursor [c_digraph](https://neovim.io/doc/user/cmdline.html#c_digraph)  	`{char1}` `<BS>` `{char2}` 				enter digraph when ['digraph'](https://neovim.io/doc/user/options.html#'digraph') is on [c_CTRL-H](https://neovim.io/doc/user/cmdline.html#c_CTRL-H)  	`CTRL-H`		same as `<BS>` [c_<Tab>](https://neovim.io/doc/user/cmdline.html#c_%3CTab%3E)  	`<Tab>`		if ['wildchar'](https://neovim.io/doc/user/options.html#'wildchar') is `<Tab>`: Do completion on 				the pattern in front of the cursor [c_<S-Tab>](https://neovim.io/doc/user/cmdline.html#c_%3CS-Tab%3E)  	`<S-Tab>`		same as `CTRL-P` [c_wildchar](https://neovim.io/doc/user/cmdline.html#c_wildchar)  	['wildchar'](https://neovim.io/doc/user/options.html#'wildchar')	Do completion on the pattern in front of the 				cursor (default: `<Tab>`) [c_CTRL-I](https://neovim.io/doc/user/cmdline.html#c_CTRL-I)  	`CTRL-I`		same as `<Tab>` [c_<NL>](https://neovim.io/doc/user/cmdline.html#c_%3CNL%3E)  	`<NL>`		same as `<CR>` [c_CTRL-J](https://neovim.io/doc/user/cmdline.html#c_CTRL-J)  	`CTRL-J`		same as `<CR>` [c_CTRL-K](https://neovim.io/doc/user/cmdline.html#c_CTRL-K)  	`CTRL-K` `{char1}` `{char2}` 				enter digraph [c_CTRL-L](https://neovim.io/doc/user/cmdline.html#c_CTRL-L)  	`CTRL-L`		do completion on the pattern in front of the 				cursor and insert the longest common part [c_<CR>](https://neovim.io/doc/user/cmdline.html#c_%3CCR%3E)  	`<CR>`		execute entered command [c_CTRL-M](https://neovim.io/doc/user/cmdline.html#c_CTRL-M)  	`CTRL-M`		same as `<CR>` [c_CTRL-N](https://neovim.io/doc/user/cmdline.html#c_CTRL-N)  	`CTRL-N`		after using ['wildchar'](https://neovim.io/doc/user/options.html#'wildchar') with multiple matches: 				go to next match, otherwise: recall older 				command-line from history. 		`CTRL-O`		not used [c_CTRL-P](https://neovim.io/doc/user/cmdline.html#c_CTRL-P)  	`CTRL-P`		after using ['wildchar'](https://neovim.io/doc/user/options.html#'wildchar') with multiple matches: 				go to previous match, otherwise: recall older 				command-line from history. [c_CTRL-Q](https://neovim.io/doc/user/cmdline.html#c_CTRL-Q)  	`CTRL-Q`		same as `CTRL-V`, unless it's used for terminal 				control flow [c_CTRL-R](https://neovim.io/doc/user/cmdline.html#c_CTRL-R)  	`CTRL-R` `{regname}` 				insert the contents of a register or object 				under the cursor as if typed [c_CTRL-R_CTRL-R](https://neovim.io/doc/user/cmdline.html#c_CTRL-R_CTRL-R) `CTRL-R` `CTRL-R` `{regname}` [c_CTRL-R_CTRL-O](https://neovim.io/doc/user/cmdline.html#c_CTRL-R_CTRL-O) `CTRL-R` `CTRL-O` `{regname}` 				insert the contents of a register or object 				under the cursor literally 		`CTRL-S`		not used, or used for terminal control flow [c_CTRL-T](https://neovim.io/doc/user/cmdline.html#c_CTRL-T)  	`CTRL-T`		previous match when ['incsearch'](https://neovim.io/doc/user/options.html#'incsearch') is active [c_CTRL-U](https://neovim.io/doc/user/cmdline.html#c_CTRL-U)  	`CTRL-U`		remove all characters [c_CTRL-V](https://neovim.io/doc/user/cmdline.html#c_CTRL-V)  	`CTRL-V`		insert next non-digit literally, insert three 				digit decimal number as a single byte. [c_CTRL-W](https://neovim.io/doc/user/cmdline.html#c_CTRL-W)  	`CTRL-W`		delete the word in front of the cursor 		`CTRL-X`		not used (reserved for completion) 		`CTRL-Y`		copy (yank) modeless selection 		`CTRL-Z`		not used (reserved for suspend) [c_<Esc>](https://neovim.io/doc/user/cmdline.html#c_%3CEsc%3E)  	`<Esc>`		abandon command-line without executing it [c_CTRL-[](https://neovim.io/doc/user/cmdline.html#c_CTRL-%5B)  	`CTRL-[`		same as `<Esc>` [c_CTRL-\_CTRL-N](https://neovim.io/doc/user/intro.html#c_CTRL-%5C_CTRL-N) `CTRL-\` `CTRL-N`	go to Normal mode, abandon command-line [c_CTRL-\_CTRL-G](https://neovim.io/doc/user/intro.html#c_CTRL-%5C_CTRL-G) `CTRL-\` `CTRL-G`	go to Normal mode, abandon command-line 		`CTRL-\` a - d	reserved for extensions [c_CTRL-\_e](https://neovim.io/doc/user/cmdline.html#c_CTRL-%5C_e)  	`CTRL-\` e `{expr}` replace the command line with the result of 				`{expr}` 		`CTRL-\` f - z	reserved for extensions 		`CTRL-\` others	not used [c_CTRL-]](https://neovim.io/doc/user/cmdline.html#c_CTRL-%5D)  	`CTRL-]`		trigger abbreviation [c_CTRL-^](https://neovim.io/doc/user/cmdline.html#c_CTRL-%5E)  	`CTRL-^`		toggle use of [:lmap](https://neovim.io/doc/user/map.html#%3Almap) mappings [c_<Del>](https://neovim.io/doc/user/cmdline.html#c_%3CDel%3E)  	`<Del>`		delete the character under the cursor
        - [c_<Left>](https://neovim.io/doc/user/cmdline.html#c_%3CLeft%3E)  	`<Left>`		cursor left [c_<S-Left>](https://neovim.io/doc/user/cmdline.html#c_%3CS-Left%3E)  	`<S-Left>`	cursor one word left [c_<C-Left>](https://neovim.io/doc/user/cmdline.html#c_%3CC-Left%3E)  	`<C-Left>`	cursor one word left [c_<Right>](https://neovim.io/doc/user/cmdline.html#c_%3CRight%3E)  	`<Right>`		cursor right [c_<S-Right>](https://neovim.io/doc/user/cmdline.html#c_%3CS-Right%3E)  	`<S-Right>`	cursor one word right [c_<C-Right>](https://neovim.io/doc/user/cmdline.html#c_%3CC-Right%3E)  	`<C-Right>`	cursor one word right [c_<Up>](https://neovim.io/doc/user/cmdline.html#c_%3CUp%3E)  	`<Up>`		recall previous command-line from history that 				matches pattern in front of the cursor [c_<S-Up>](https://neovim.io/doc/user/cmdline.html#c_%3CS-Up%3E)  	`<S-Up>`		recall previous command-line from history [c_<Down>](https://neovim.io/doc/user/cmdline.html#c_%3CDown%3E)  	`<Down>`		recall next command-line from history that 				matches pattern in front of the cursor [c_<S-Down>](https://neovim.io/doc/user/cmdline.html#c_%3CS-Down%3E)  	`<S-Down>`	recall next command-line from history [c_<Home>](https://neovim.io/doc/user/cmdline.html#c_%3CHome%3E)  	`<Home>`		cursor to start of command-line [c_<End>](https://neovim.io/doc/user/cmdline.html#c_%3CEnd%3E)  	`<End>`		cursor to end of command-line [c_<PageDown>](https://neovim.io/doc/user/cmdline.html#c_%3CPageDown%3E)  	`<PageDown>`	same as `<S-Down>` [c_<PageUp>](https://neovim.io/doc/user/cmdline.html#c_%3CPageUp%3E)  	`<PageUp>`	same as `<S-Up>` [c_<Insert>](https://neovim.io/doc/user/cmdline.html#c_%3CInsert%3E)  	`<Insert>`	toggle insert/overstrike mode [c_<LeftMouse>](https://neovim.io/doc/user/cmdline.html#c_%3CLeftMouse%3E)  	`<LeftMouse>`	cursor at mouse click
        - commands in wildmenu mode (see ['wildmenu'](https://neovim.io/doc/user/options.html#'wildmenu'))
            - `<Up>`		move up to parent 		`<Down>`		move down to submenu 		`<Left>`		select the previous match 		`<Right>`		select the next match 		`<CR>`		move into submenu when doing menu completion 		`CTRL-E`		stop completion and go back to original text 		`CTRL-Y`		accept selected match and stop completion 		other		stop completion and insert the typed character
        - commands in wildmenu mode with ['wildoptions'](https://neovim.io/doc/user/options.html#'wildoptions') set to "pum"
            - `<PageUp>`	select a match several entries back 		`<PageDown>`	select a match several entries forward
    -  **5. Terminal mode**** **
        - In a [terminal](https://neovim.io/doc/user/terminal.html#terminal) buffer all keys except `CTRL-\` are forwarded to the terminal job.  If `CTRL-\` is pressed, the next key is forwarded unless it is `CTRL-N` or `CTRL-O`. Use [CTRL-\_CTRL-N](https://neovim.io/doc/user/intro.html#CTRL-%5C_CTRL-N) to go to Normal mode. Use [t_CTRL-\_CTRL-O](https://neovim.io/doc/user/terminal.html#t_CTRL-%5C_CTRL-O) to execute one normal mode command and then return to terminal mode.
        - You found it, Arthur!				[holy-grail](https://neovim.io/doc/user/vimindex.html#holy-grail)
    -  **6. EX commands**** **
        - This is a brief but complete listing of all the ":" commands, without mentioning any arguments.  The optional part of the command name is inside []. The commands are sorted on the non-optional part of their name.
        - Tag		Command		Action
        - ------------------------------------------------------------------------------
        - [:](https://neovim.io/doc/user/cmdline.html#%3A)  		:		nothing [:range](https://neovim.io/doc/user/cmdline.html#%3Arange)  	:{range}	go to last line in `{range}` [:!](https://neovim.io/doc/user/various.html#%3A%21)  		:!		filter lines or execute an external command [:!!](https://neovim.io/doc/user/various.html#%3A%21%21)  		:!!		repeat last ":!" command [:#](https://neovim.io/doc/user/various.html#%3A%23)  		:#		same as ":number" [:&](https://neovim.io/doc/user/change.html#%3A%26)  		:&		repeat last ":substitute" [:star](https://neovim.io/doc/user/cmdline.html#%3Astar)  		:*		use the last Visual area, like ":'<,'>" [:<](https://neovim.io/doc/user/change.html#%3A%3C)  		:<		shift lines one ['shiftwidth'](https://neovim.io/doc/user/options.html#'shiftwidth') left [:=](https://neovim.io/doc/user/various.html#%3A%3D)  		:=		print the last line number:-↔		shift lines one ['shiftwidth'](https://neovim.io/doc/user/options.html#'shiftwidth') right [:@](https://neovim.io/doc/user/repeat.html#%3A%40)  		:@		execute contents of a register [:@@](https://neovim.io/doc/user/repeat.html#%3A%40%40)  		:@@		repeat the previous ":@" [:2match](https://neovim.io/doc/user/pattern.html#%3A2match)  	:2mat[ch]	define a second match to highlight [:3match](https://neovim.io/doc/user/pattern.html#%3A3match)  	:3mat[ch]	define a third match to highlight [:Next](https://neovim.io/doc/user/editing.html#%3ANext)  		:N[ext]		go to previous file in the argument list [:append](https://neovim.io/doc/user/insert.html#%3Aappend)  	:a[ppend]	append text [:abbreviate](https://neovim.io/doc/user/map.html#%3Aabbreviate)  	:ab[breviate]	enter abbreviation [:abclear](https://neovim.io/doc/user/map.html#%3Aabclear)  	:abc[lear]	remove all abbreviations [:aboveleft](https://neovim.io/doc/user/windows.html#%3Aaboveleft)  	:abo[veleft]	make split window appear left or above [:all](https://neovim.io/doc/user/windows.html#%3Aall)  		:al[l]		open a window for each file in the argument 				list [:amenu](https://neovim.io/doc/user/gui.html#%3Aamenu)  	:am[enu]	enter new menu item for all modes [:anoremenu](https://neovim.io/doc/user/gui.html#%3Aanoremenu)  	:an[oremenu]	enter a new menu for all modes that will not 				be remapped [:args](https://neovim.io/doc/user/editing.html#%3Aargs)  		:ar[gs]		print the argument list [:argadd](https://neovim.io/doc/user/editing.html#%3Aargadd)  	:arga[dd]	add items to the argument list [:argdedupe](https://neovim.io/doc/user/editing.html#%3Aargdedupe)  	:argded[upe]	remove duplicates from the argument list [:argdelete](https://neovim.io/doc/user/editing.html#%3Aargdelete)  	:argd[elete]	delete items from the argument list [:argedit](https://neovim.io/doc/user/editing.html#%3Aargedit)  	:arge[dit]	add item to the argument list and edit it [:argdo](https://neovim.io/doc/user/editing.html#%3Aargdo)  	:argdo		do a command on all items in the argument list [:argglobal](https://neovim.io/doc/user/editing.html#%3Aargglobal)  	:argg[lobal]	define the global argument list [:arglocal](https://neovim.io/doc/user/editing.html#%3Aarglocal)  	:argl[ocal]	define a local argument list [:argument](https://neovim.io/doc/user/editing.html#%3Aargument)  	:argu[ment]	go to specific file in the argument list [:ascii](https://neovim.io/doc/user/various.html#%3Aascii)  	:as[cii]	print ascii value of character under the cursor [:autocmd](https://neovim.io/doc/user/autocmd.html#%3Aautocmd)  	:au[tocmd]	enter or show autocommands [:augroup](https://neovim.io/doc/user/autocmd.html#%3Aaugroup)  	:aug[roup]	select the autocommand group to use [:aunmenu](https://neovim.io/doc/user/gui.html#%3Aaunmenu)  	:aun[menu]	remove menu for all modes [:buffer](https://neovim.io/doc/user/windows.html#%3Abuffer)  	:b[uffer]	go to specific buffer in the buffer list [:bNext](https://neovim.io/doc/user/windows.html#%3AbNext)  	:bN[ext]	go to previous buffer in the buffer list [:ball](https://neovim.io/doc/user/windows.html#%3Aball)  		:ba[ll]		open a window for each buffer in the buffer list [:badd](https://neovim.io/doc/user/windows.html#%3Abadd)  		:bad[d]		add buffer to the buffer list [:balt](https://neovim.io/doc/user/windows.html#%3Abalt)  		:balt		like ":badd" but also set the alternate file [:bdelete](https://neovim.io/doc/user/windows.html#%3Abdelete)  	:bd[elete]	remove a buffer from the buffer list [:belowright](https://neovim.io/doc/user/windows.html#%3Abelowright)  	:bel[owright]	make split window appear right or below [:bfirst](https://neovim.io/doc/user/windows.html#%3Abfirst)  	:bf[irst]	go to first buffer in the buffer list [:blast](https://neovim.io/doc/user/windows.html#%3Ablast)  	:bl[ast]	go to last buffer in the buffer list [:bmodified](https://neovim.io/doc/user/windows.html#%3Abmodified)  	:bm[odified]	go to next buffer in the buffer list that has 				been modified [:bnext](https://neovim.io/doc/user/windows.html#%3Abnext)  	:bn[ext]	go to next buffer in the buffer list [:botright](https://neovim.io/doc/user/windows.html#%3Abotright)  	:bo[tright]	make split window appear at bottom or far right [:bprevious](https://neovim.io/doc/user/windows.html#%3Abprevious)  	:bp[revious]	go to previous buffer in the buffer list [:brewind](https://neovim.io/doc/user/windows.html#%3Abrewind)  	:br[ewind]	go to first buffer in the buffer list [:break](https://neovim.io/doc/user/vimeval.html#%3Abreak)  	:brea[k]	break out of while loop [:breakadd](https://neovim.io/doc/user/repeat.html#%3Abreakadd)  	:breaka[dd]	add a debugger breakpoint [:breakdel](https://neovim.io/doc/user/repeat.html#%3Abreakdel)  	:breakd[el]	delete a debugger breakpoint [:breaklist](https://neovim.io/doc/user/repeat.html#%3Abreaklist)  	:breakl[ist]	list debugger breakpoints [:browse](https://neovim.io/doc/user/editing.html#%3Abrowse)  	:bro[wse]	use file selection dialog [:bufdo](https://neovim.io/doc/user/windows.html#%3Abufdo)  	:bufd[o]	execute command in each listed buffer [:buffers](https://neovim.io/doc/user/windows.html#%3Abuffers)  	:buffers	list all files in the buffer list [:bunload](https://neovim.io/doc/user/windows.html#%3Abunload)  	:bun[load]	unload a specific buffer [:bwipeout](https://neovim.io/doc/user/windows.html#%3Abwipeout)  	:bw[ipeout]	really delete a buffer [:change](https://neovim.io/doc/user/change.html#%3Achange)  	:c[hange]	replace a line or series of lines [:cNext](https://neovim.io/doc/user/quickfix.html#%3AcNext)  	:cN[ext]	go to previous error [:cNfile](https://neovim.io/doc/user/quickfix.html#%3AcNfile)  	:cNf[ile]	go to last error in previous file [:cabbrev](https://neovim.io/doc/user/map.html#%3Acabbrev)  	:ca[bbrev]	like ":abbreviate" but for Command-line mode [:cabclear](https://neovim.io/doc/user/map.html#%3Acabclear)  	:cabc[lear]	clear all abbreviations for Command-line mode [:cabove](https://neovim.io/doc/user/quickfix.html#%3Acabove)  	:cabo[ve]	go to error above current line [:caddbuffer](https://neovim.io/doc/user/quickfix.html#%3Acaddbuffer)  	:cad[dbuffer]	add errors from buffer [:caddexpr](https://neovim.io/doc/user/quickfix.html#%3Acaddexpr)  	:cadde[xpr]	add errors from expr [:caddfile](https://neovim.io/doc/user/quickfix.html#%3Acaddfile)  	:caddf[ile]	add error message to current quickfix list [:cafter](https://neovim.io/doc/user/quickfix.html#%3Acafter)  	:caf[ter]	go to error after current cursor [:call](https://neovim.io/doc/user/userfunc.html#%3Acall)  		:cal[l]		call a function [:catch](https://neovim.io/doc/user/vimeval.html#%3Acatch)  	:cat[ch]	part](https://neovim.io/doc/user/quickfix.html#%3Acbefore)
        - [of a :try command [:cbefore](https://neovim.io/doc/user/quickfix.html#%3Acbefore)  	:cbe[fore]	go to error before current cursor [:cbelow](https://neovim.io/doc/user/quickfix.html#%3Acbelow)  	:cbel[ow]	go to error below current line [:cbottom](https://neovim.io/doc/user/quickfix.html#%3Acbottom)  	:cbo[ttom]	scroll to the bottom of the quickfix window [:cbuffer](https://neovim.io/doc/user/quickfix.html#%3Acbuffer)  	:cb[uffer]	parse error messages and jump to first error [:cc](https://neovim.io/doc/user/quickfix.html#%3Acc)  		:cc		go to specific error [:cclose](https://neovim.io/doc/user/quickfix.html#%3Acclose)  	:ccl[ose]	close quickfix window [:cd](https://neovim.io/doc/user/editing.html#%3Acd)  		:cd		change directory [:cdo](https://neovim.io/doc/user/quickfix.html#%3Acdo)  		:cdo		execute command in each valid error list entry [:cfdo](https://neovim.io/doc/user/quickfix.html#%3Acfdo)  		:cfd[o]		execute command in each file in error list [:center](https://neovim.io/doc/user/change.html#%3Acenter)  	:ce[nter]	format lines at the center [:cexpr](https://neovim.io/doc/user/quickfix.html#%3Acexpr)  	:cex[pr]	read errors from expr and jump to first [:cfile](https://neovim.io/doc/user/quickfix.html#%3Acfile)  	:cf[ile]	read file with error messages and jump to first [:cfirst](https://neovim.io/doc/user/quickfix.html#%3Acfirst)  	:cfir[st]	go to the specified error, default first one [:cgetbuffer](https://neovim.io/doc/user/quickfix.html#%3Acgetbuffer)  	:cgetb[uffer]	get errors from buffer [:cgetexpr](https://neovim.io/doc/user/quickfix.html#%3Acgetexpr)  	:cgete[xpr]	get errors from expr [:cgetfile](https://neovim.io/doc/user/quickfix.html#%3Acgetfile)  	:cg[etfile]	read file with error messages [:changes](https://neovim.io/doc/user/motion.html#%3Achanges)  	:changes	print the change list [:chdir](https://neovim.io/doc/user/editing.html#%3Achdir)  	:chd[ir]	change directory [:checkhealth](https://neovim.io/doc/user/health.html#%3Acheckhealth)  	:che[ckhealth]	run healthchecks [:checkpath](https://neovim.io/doc/user/tagsrch.html#%3Acheckpath)  	:checkp[ath]	list included files [:checktime](https://neovim.io/doc/user/editing.html#%3Achecktime)  	:checkt[ime]	check timestamp of loaded buffers [:chistory](https://neovim.io/doc/user/quickfix.html#%3Achistory)  	:chi[story]	list the error lists [:clast](https://neovim.io/doc/user/quickfix.html#%3Aclast)  	:cla[st]	go to the specified error, default last one [:clearjumps](https://neovim.io/doc/user/motion.html#%3Aclearjumps)  	:cle[arjumps]	clear the jump list [:clist](https://neovim.io/doc/user/quickfix.html#%3Aclist)  	:cl[ist]	list all errors [:close](https://neovim.io/doc/user/windows.html#%3Aclose)  	:clo[se]	close current window [:cmap](https://neovim.io/doc/user/map.html#%3Acmap)  		:cm[ap]		like ":map" but for Command-line mode [:cmapclear](https://neovim.io/doc/user/map.html#%3Acmapclear)  	:cmapc[lear]	clear all mappings for Command-line mode [:cmenu](https://neovim.io/doc/user/gui.html#%3Acmenu)  	:cme[nu]	add menu for Command-line mode [:cnext](https://neovim.io/doc/user/quickfix.html#%3Acnext)  	:cn[ext]	go to next error [:cnewer](https://neovim.io/doc/user/quickfix.html#%3Acnewer)  	:cnew[er]	go to newer error list [:cnfile](https://neovim.io/doc/user/quickfix.html#%3Acnfile)  	:cnf[ile]	go to first error in next file [:cnoremap](https://neovim.io/doc/user/map.html#%3Acnoremap)  	:cno[remap]	like ":noremap" but for Command-line mode [:cnoreabbrev](https://neovim.io/doc/user/map.html#%3Acnoreabbrev)  	:cnorea[bbrev]	like ":noreabbrev" but for Command-line mode [:cnoremenu](https://neovim.io/doc/user/gui.html#%3Acnoremenu)  	:cnoreme[nu]	like ":noremenu" but for Command-line mode [:copy](https://neovim.io/doc/user/change.html#%3Acopy)  		:co[py]		copy lines [:colder](https://neovim.io/doc/user/quickfix.html#%3Acolder)  	:col[der]	go to older error list [:colorscheme](https://neovim.io/doc/user/syntax.html#%3Acolorscheme)  	:colo[rscheme]	load a specific color scheme [:command](https://neovim.io/doc/user/map.html#%3Acommand)  	:com[mand]	create user-defined command [:comclear](https://neovim.io/doc/user/map.html#%3Acomclear)  	:comc[lear]	clear all user-defined commands [:compiler](https://neovim.io/doc/user/quickfix.html#%3Acompiler)  	:comp[iler]	do settings for a specific compiler [:continue](https://neovim.io/doc/user/vimeval.html#%3Acontinue)  	:con[tinue]	go back to :while [:confirm](https://neovim.io/doc/user/editing.html#%3Aconfirm)  	:conf[irm]	prompt user when confirmation required [:const](https://neovim.io/doc/user/vimeval.html#%3Aconst)  	:cons[t]	create a variable as a constant [:copen](https://neovim.io/doc/user/quickfix.html#%3Acopen)  	:cope[n]	open quickfix window [:cprevious](https://neovim.io/doc/user/quickfix.html#%3Acprevious)  	:cp[revious]	go to previous error [:cpfile](https://neovim.io/doc/user/quickfix.html#%3Acpfile)  	:cpf[ile]	go to last error in previous file [:cquit](https://neovim.io/doc/user/quickfix.html#%3Acquit)  	:cq[uit]	quit Vim with an error code [:crewind](https://neovim.io/doc/user/quickfix.html#%3Acrewind)  	:cr[ewind]	go to the specified error, default first one [:cunmap](https://neovim.io/doc/user/map.html#%3Acunmap)  	:cu[nmap]	like ":unmap" but for Command-line mode [:cunabbrev](https://neovim.io/doc/user/map.html#%3Acunabbrev)  	:cuna[bbrev]	like ":unabbrev" but for Command-line mode [:cunmenu](https://neovim.io/doc/user/gui.html#%3Acunmenu)  	:cunme[nu]	remove menu for Command-line mode [:cwindow](https://neovim.io/doc/user/quickfix.html#%3Acwindow)  	:cw[indow]	open or close quickfix window [:delete](https://neovim.io/doc/user/change.html#%3Adelete)  	:d[elete]	delete lines [:debug](https://neovim.io/doc/user/repeat.html#%3Adebug)  	:deb[ug]	run a command in debugging mode [:debuggreedy](https://neovim.io/doc/user/repeat.html#%3Adebuggreedy)  	:debugg[reedy]	read debug mode commands from normal input [:defer](https://neovim.io/doc/user/userfunc.html#%3Adefer)  	:defe[r]	call function when current function is done [:delcommand](https://neovim.io/doc/user/map.html#%3Adelcommand)  	:delc[ommand]	delete user-defined command [:delfunction](https://neovim.io/doc/user/userfunc.html#%3Adelfunction)  	:delf[unction]	delete a user function [:delmarks](https://neovim.io/doc/user/motion.html#%3Adelmarks)  	:delm[arks]	delete marks [:detach](https://neovim.io/doc/user/gui.html#%3Adetach)  	:detach		detach the current UI [:diffupdate](https://neovim.io/doc/user/diff.html#%3Adiffupdate)  	:dif[fupdate]	update ['diff'](https://neovim.io/doc/user/options.html#'diff') buffers [:diffget](https://neovim.io/doc/user/diff.html#%3Adiffget)  	:diffg[et]	remove differences in current buffer [:diffoff](https://neovim.io/doc/user/diff.html#%3Adiffoff)  	:diffo[ff]	switch off diff mode [:diffpatch](https://neovim.io/doc/user/diff.html#%3Adiffpatch)  	:diffp[atch]	apply a patch and show differences [:diffput](https://neovim.io/doc/user/diff.html#%3Adiffput)  	:diffpu[t]	remove differences in other buffer [:diffsplit](https://neovim.io/doc/user/diff.html#%3Adiffsplit)  	:diffs[plit]	show differences with another file [:diffthis](https://neovim.io/doc/user/diff.html#%3Adiffthis)  	:difft[his]	make current window a diff window [:digraphs](https://neovim.io/doc/user/digraph.html#%3Adigraphs)  	:dig[raphs]	show or enter digraphs [:display](https://neovim.io/doc/user/change.html#%3Adisplay)  	:di[splay]	display registers [:djump](https://neovim.io/doc/user/tagsrch.html#%3Adjump)  	:dj[ump]	jump to #define [:dl](https://neovim.io/doc/user/change.html#%3Adl)  		:dl		short
        - for [:delete](https://neovim.io/doc/user/change.html#%3Adelete) with the 'l' flag [:dlist](https://neovim.io/doc/user/tagsrch.html#%3Adlist)  	:dli[st]	list #defines [:doautocmd](https://neovim.io/doc/user/autocmd.html#%3Adoautocmd)  	:do[autocmd]	apply autocommands to current buffer [:doautoall](https://neovim.io/doc/user/autocmd.html#%3Adoautoall)  	:doautoa[ll]	apply autocommands for all loaded buffers [:dp](https://neovim.io/doc/user/change.html#%3Adp)  		:d[elete]p	short for [:delete](https://neovim.io/doc/user/change.html#%3Adelete) with the 'p' flag [:drop](https://neovim.io/doc/user/windows.html#%3Adrop)  		:dr[op]		jump to window editing file or edit file in 				current window [:dsearch](https://neovim.io/doc/user/tagsrch.html#%3Adsearch)  	:ds[earch]	list one #define [:dsplit](https://neovim.io/doc/user/tagsrch.html#%3Adsplit)  	:dsp[lit]	split window and jump to #define [:edit](https://neovim.io/doc/user/editing.html#%3Aedit)  		:e[dit]		edit a file [:earlier](https://neovim.io/doc/user/undo.html#%3Aearlier)  	:ea[rlier]	go to older change, undo [:echo](https://neovim.io/doc/user/vimeval.html#%3Aecho)  		:ec[ho]		echoes the result of expressions [:echoerr](https://neovim.io/doc/user/vimeval.html#%3Aechoerr)  	:echoe[rr]	like :echo, show like an error and use history [:echohl](https://neovim.io/doc/user/vimeval.html#%3Aechohl)  	:echoh[l]	set highlighting for echo commands [:echomsg](https://neovim.io/doc/user/vimeval.html#%3Aechomsg)  	:echom[sg]	same as :echo, put message in history [:echon](https://neovim.io/doc/user/vimeval.html#%3Aechon)  	:echon		same as :echo, but without `<EOL>` [:else](https://neovim.io/doc/user/vimeval.html#%3Aelse)  		:el[se]		part of an :if command [:elseif](https://neovim.io/doc/user/vimeval.html#%3Aelseif)  	:elsei[f]	part of an :if command [:emenu](https://neovim.io/doc/user/gui.html#%3Aemenu)  	:em[enu]	execute a menu by name [:endif](https://neovim.io/doc/user/vimeval.html#%3Aendif)  	:en[dif]	end previous :if [:endfor](https://neovim.io/doc/user/vimeval.html#%3Aendfor)  	:endfo[r]	end previous :for [:endfunction](https://neovim.io/doc/user/userfunc.html#%3Aendfunction)  	:endf[unction]	end of a user function started with :function [:endtry](https://neovim.io/doc/user/vimeval.html#%3Aendtry)  	:endt[ry]	end previous :try [:endwhile](https://neovim.io/doc/user/vimeval.html#%3Aendwhile)  	:endw[hile]	end previous :while [:enew](https://neovim.io/doc/user/editing.html#%3Aenew)  		:ene[w]		edit a new, unnamed buffer [:eval](https://neovim.io/doc/user/vimeval.html#%3Aeval)  		:ev[al]		evaluate an expression and discard the result [:ex](https://neovim.io/doc/user/editing.html#%3Aex)  		:ex		same as ":edit" [:execute](https://neovim.io/doc/user/vimeval.html#%3Aexecute)  	:exe[cute]	execute result of expressions [:exit](https://neovim.io/doc/user/editing.html#%3Aexit)  		:exi[t]		same as ":xit" [:exusage](https://neovim.io/doc/user/helphelp.html#%3Aexusage)  	:exu[sage]	overview of Ex commands [:fclose](https://neovim.io/doc/user/windows.html#%3Afclose)  	:fc[lose]	close floating window [:file](https://neovim.io/doc/user/editing.html#%3Afile)  		:f[ile]		show or set the current file name [:files](https://neovim.io/doc/user/windows.html#%3Afiles)  	:files		list all files in the buffer list [:filetype](https://neovim.io/doc/user/filetype.html#%3Afiletype)  	:filet[ype]	switch file type detection on/off [:filter](https://neovim.io/doc/user/various.html#%3Afilter)  	:filt[er]	filter output of following command [:find](https://neovim.io/doc/user/editing.html#%3Afind)  		:fin[d]		find file in ['path'](https://neovim.io/doc/user/options.html#'path') and edit it [:finally](https://neovim.io/doc/user/vimeval.html#%3Afinally)  	:fina[lly]	part of a :try command [:finish](https://neovim.io/doc/user/repeat.html#%3Afinish)  	:fini[sh]	quit sourcing a Vim script [:first](https://neovim.io/doc/user/editing.html#%3Afirst)  	:fir[st]	go to the first file in the argument list [:fold](https://neovim.io/doc/user/fold.html#%3Afold)  		:fo[ld]		create a fold [:foldclose](https://neovim.io/doc/user/fold.html#%3Afoldclose)  	:foldc[lose]	close folds [:folddoopen](https://neovim.io/doc/user/fold.html#%3Afolddoopen)  	:foldd[oopen]	execute command on lines not in a closed fold [:folddoclosed](https://neovim.io/doc/user/fold.html#%3Afolddoclosed)  	:folddoc[losed]	execute command on lines in a closed fold [:foldopen](https://neovim.io/doc/user/fold.html#%3Afoldopen)  	:foldo[pen]	open folds [:for](https://neovim.io/doc/user/vimeval.html#%3Afor)  		:for		for loop [:function](https://neovim.io/doc/user/userfunc.html#%3Afunction)  	:fu[nction]	define a user function [:global](https://neovim.io/doc/user/repeat.html#%3Aglobal)  	:g[lobal]	execute commands for matching lines [:goto](https://neovim.io/doc/user/motion.html#%3Agoto)  		:go[to]		go to byte in the buffer [:grep](https://neovim.io/doc/user/quickfix.html#%3Agrep)  		:gr[ep]		run ['grepprg'](https://neovim.io/doc/user/options.html#'grepprg') and jump to first match [:grepadd](https://neovim.io/doc/user/quickfix.html#%3Agrepadd)  	:grepa[dd]	like :grep, but append to current list [:gui](https://neovim.io/doc/user/vim_diff.html#%3Agui)  		:gu[i]		start the GUI [:gvim](https://neovim.io/doc/user/vim_diff.html#%3Agvim)  		:gv[im]		start the GUI [:help](https://neovim.io/doc/user/helphelp.html#%3Ahelp)  		:h[elp]		open a help window [:helpclose](https://neovim.io/doc/user/helphelp.html#%3Ahelpclose)  	:helpc[lose]	close one help window [:helpgrep](https://neovim.io/doc/user/helphelp.html#%3Ahelpgrep)  	:helpg[rep]	like ":grep" but searches help files [:helptags](https://neovim.io/doc/user/helphelp.html#%3Ahelptags)  	:helpt[ags]	generate help tags for a directory [:highlight](https://neovim.io/doc/user/syntax.html#%3Ahighlight)  	:hi[ghlight]	specify highlighting methods [:hide](https://neovim.io/doc/user/windows.html#%3Ahide)  		:hid[e]		hide current buffer for a command [:history](https://neovim.io/doc/user/cmdline.html#%3Ahistory)  	:his[tory]	print a history list [:horizontal](https://neovim.io/doc/user/windows.html#%3Ahorizontal)  	:hor[izontal]	following window command work horizontally [:insert](https://neovim.io/doc/user/insert.html#%3Ainsert)  	:i[nsert]	insert text [:iabbrev](https://neovim.io/doc/user/map.html#%3Aiabbrev)  	:ia[bbrev]	like ":abbrev" but for Insert mode [:iabclear](https://neovim.io/doc/user/map.html#%3Aiabclear)  	:iabc[lear]	like ":abclear" but for Insert mode [:if](https://neovim.io/doc/user/vimeval.html#%3Aif)  		:if		execute commands when condition met [:ijump](https://neovim.io/doc/user/tagsrch.html#%3Aijump)  	:ij[ump]	jump to definition of identifier [:ilist](https://neovim.io/doc/user/tagsrch.html#%3Ailist)  	:il[ist]	list lines where identifier matches [:imap](https://neovim.io/doc/user/map.html#%3Aimap)  		:im[ap]		like ":map" but for Insert mode [:imapclear](https://neovim.io/doc/user/map.html#%3Aimapclear)  	:imapc[lear]	like ":mapclear" but for Insert mode [:imenu](https://neovim.io/doc/user/gui.html#%3Aimenu)  	:ime[nu]	add menu for Insert mode [:inoremap](https://neovim.io/doc/user/map.html#%3Ainoremap)  	:ino[remap]	like ":noremap" but for Insert mode [:inoreabbrev](https://neovim.io/doc/user/map.html#%3Ainoreabbrev)  	:inorea[bbrev]	like ":noreabbrev" but for Insert mode [:inoremenu](https://neovim.io/doc/user/gui.html#%3Ainoremenu)  	:inoreme[nu]	like ":noremenu" but for Insert mode [:intro](https://neovim.io/doc/user/starting.html#%3Aintro)  	:int[ro]	print the introductory message [:iput](https://neovim.io/doc/user/change.html#%3Aiput)  		:ip[ut]		like [:put](https://neovim.io/doc/user/change.html#%3Aput), but adjust the indent to the 				current line [:isearch](https://neovim.io/doc/user/tagsrch.html#%3Aisearch)  	:is[earch]	list one line where identifier](https://neovim.io/doc/user/tagsrch.html#%3Aisplit)
        - [matches [:isplit](https://neovim.io/doc/user/tagsrch.html#%3Aisplit)  	:isp[lit]	split window and jump to definition of 				identifier [:iunmap](https://neovim.io/doc/user/map.html#%3Aiunmap)  	:iu[nmap]	like ":unmap" but for Insert mode [:iunabbrev](https://neovim.io/doc/user/map.html#%3Aiunabbrev)  	:iuna[bbrev]	like ":unabbrev" but for Insert mode [:iunmenu](https://neovim.io/doc/user/gui.html#%3Aiunmenu)  	:iunme[nu]	remove menu for Insert mode [:join](https://neovim.io/doc/user/change.html#%3Ajoin)  		:j[oin]		join lines [:jumps](https://neovim.io/doc/user/motion.html#%3Ajumps)  	:ju[mps]	print the jump list [:k](https://neovim.io/doc/user/motion.html#%3Ak)  		:k		set a mark [:keepalt](https://neovim.io/doc/user/editing.html#%3Akeepalt)  	:keepa[lt]	following command keeps the alternate file [:keepmarks](https://neovim.io/doc/user/motion.html#%3Akeepmarks)  	:kee[pmarks]	following command keeps marks where they are [:keepjumps](https://neovim.io/doc/user/motion.html#%3Akeepjumps)  	:keepj[umps]	following command keeps jumplist and marks [:keeppatterns](https://neovim.io/doc/user/cmdline.html#%3Akeeppatterns)  	:keepp[atterns]	following command keeps search pattern history [:lNext](https://neovim.io/doc/user/quickfix.html#%3AlNext)  	:lN[ext]	go to previous entry in location list [:lNfile](https://neovim.io/doc/user/quickfix.html#%3AlNfile)  	:lNf[ile]	go to last entry in previous file [:list](https://neovim.io/doc/user/various.html#%3Alist)  		:l[ist]		print lines [:labove](https://neovim.io/doc/user/quickfix.html#%3Alabove)  	:lab[ove]	go to location above current line [:laddexpr](https://neovim.io/doc/user/quickfix.html#%3Aladdexpr)  	:lad[dexpr]	add locations from expr [:laddbuffer](https://neovim.io/doc/user/quickfix.html#%3Aladdbuffer)  	:laddb[uffer]	add locations from buffer [:laddfile](https://neovim.io/doc/user/quickfix.html#%3Aladdfile)  	:laddf[ile]	add locations to current location list [:lafter](https://neovim.io/doc/user/quickfix.html#%3Alafter)  	:laf[ter]	go to location after current cursor [:last](https://neovim.io/doc/user/editing.html#%3Alast)  		:la[st]		go to the last file in the argument list [:language](https://neovim.io/doc/user/mlang.html#%3Alanguage)  	:lan[guage]	set the language (locale) [:later](https://neovim.io/doc/user/undo.html#%3Alater)  	:lat[er]	go to newer change, redo [:lbefore](https://neovim.io/doc/user/quickfix.html#%3Albefore)  	:lbe[fore]	go to location before current cursor [:lbelow](https://neovim.io/doc/user/quickfix.html#%3Albelow)  	:lbel[ow]	go to location below current line [:lbottom](https://neovim.io/doc/user/quickfix.html#%3Albottom)  	:lbo[ttom]	scroll to the bottom of the location window [:lbuffer](https://neovim.io/doc/user/quickfix.html#%3Albuffer)  	:lb[uffer]	parse locations and jump to first location [:lcd](https://neovim.io/doc/user/editing.html#%3Alcd)  		:lc[d]		change directory locally [:lchdir](https://neovim.io/doc/user/editing.html#%3Alchdir)  	:lch[dir]	change directory locally [:lclose](https://neovim.io/doc/user/quickfix.html#%3Alclose)  	:lcl[ose]	close location window [:ldo](https://neovim.io/doc/user/quickfix.html#%3Aldo)  		:ld[o]		execute command in valid location list entries [:lfdo](https://neovim.io/doc/user/quickfix.html#%3Alfdo)  		:lfd[o]		execute command in each file in location list [:left](https://neovim.io/doc/user/change.html#%3Aleft)  		:le[ft]		left align lines [:leftabove](https://neovim.io/doc/user/windows.html#%3Aleftabove)  	:lefta[bove]	make split window appear left or above [:let](https://neovim.io/doc/user/vimeval.html#%3Alet)  		:let		assign a value to a variable or option [:lexpr](https://neovim.io/doc/user/quickfix.html#%3Alexpr)  	:lex[pr]	read locations from expr and jump to first [:lfile](https://neovim.io/doc/user/quickfix.html#%3Alfile)  	:lf[ile]	read file with locations and jump to first [:lfirst](https://neovim.io/doc/user/quickfix.html#%3Alfirst)  	:lfir[st]	go to the specified location, default first one [:lgetbuffer](https://neovim.io/doc/user/quickfix.html#%3Algetbuffer)  	:lgetb[uffer]	get locations from buffer [:lgetexpr](https://neovim.io/doc/user/quickfix.html#%3Algetexpr)  	:lgete[xpr]	get locations from expr [:lgetfile](https://neovim.io/doc/user/quickfix.html#%3Algetfile)  	:lg[etfile]	read file with locations [:lgrep](https://neovim.io/doc/user/quickfix.html#%3Algrep)  	:lgr[ep]	run ['grepprg'](https://neovim.io/doc/user/options.html#'grepprg') and jump to first match [:lgrepadd](https://neovim.io/doc/user/quickfix.html#%3Algrepadd)  	:lgrepa[dd]	like :grep, but append to current list [:lhelpgrep](https://neovim.io/doc/user/helphelp.html#%3Alhelpgrep)  	:lh[elpgrep]	like ":helpgrep" but uses location list [:lhistory](https://neovim.io/doc/user/quickfix.html#%3Alhistory)  	:lhi[story]	list the location lists [:ll](https://neovim.io/doc/user/quickfix.html#%3All)  		:ll		go to specific location [:llast](https://neovim.io/doc/user/quickfix.html#%3Allast)  	:lla[st]	go to the specified location, default last one [:llist](https://neovim.io/doc/user/quickfix.html#%3Allist)  	:lli[st]	list all locations [:lmake](https://neovim.io/doc/user/quickfix.html#%3Almake)  	:lmak[e]	execute external command ['makeprg'](https://neovim.io/doc/user/options.html#'makeprg') and parse 				error messages [:lmap](https://neovim.io/doc/user/map.html#%3Almap)  		:lm[ap]		like ":map!" but includes Lang-Arg mode [:lmapclear](https://neovim.io/doc/user/map.html#%3Almapclear)  	:lmapc[lear]	like ":mapclear!" but includes Lang-Arg mode [:lnext](https://neovim.io/doc/user/quickfix.html#%3Alnext)  	:lne[xt]	go to next location [:lnewer](https://neovim.io/doc/user/quickfix.html#%3Alnewer)  	:lnew[er]	go to newer location list [:lnfile](https://neovim.io/doc/user/quickfix.html#%3Alnfile)  	:lnf[ile]	go to first location in next file [:lnoremap](https://neovim.io/doc/user/map.html#%3Alnoremap)  	:ln[oremap]	like ":noremap!" but includes Lang-Arg mode [:loadkeymap](https://neovim.io/doc/user/mbyte.html#%3Aloadkeymap)  	:loadk[eymap]	load the following keymaps until EOF [:loadview](https://neovim.io/doc/user/starting.html#%3Aloadview)  	:lo[adview]	load view for current window from a file [:lockmarks](https://neovim.io/doc/user/motion.html#%3Alockmarks)  	:loc[kmarks]	following command keeps marks where they are [:lockvar](https://neovim.io/doc/user/vimeval.html#%3Alockvar)  	:lockv[ar]	lock variables [:lolder](https://neovim.io/doc/user/quickfix.html#%3Alolder)  	:lol[der]	go to older location list [:lopen](https://neovim.io/doc/user/quickfix.html#%3Alopen)  	:lop[en]	open location window [:lprevious](https://neovim.io/doc/user/quickfix.html#%3Alprevious)  	:lp[revious]	go to previous location [:lpfile](https://neovim.io/doc/user/quickfix.html#%3Alpfile)  	:lpf[ile]	go to last location in previous file [:lrewind](https://neovim.io/doc/user/quickfix.html#%3Alrewind)  	:lr[ewind]	go to the specified location, default first one [:ls](https://neovim.io/doc/user/windows.html#%3Als)  		:ls		list all buffers [:ltag](https://neovim.io/doc/user/tagsrch.html#%3Altag)  		:lt[ag]		jump to tag and add matching tags to the 				location list [:lunmap](https://neovim.io/doc/user/map.html#%3Alunmap)  	:lu[nmap]	like ":unmap!" but includes Lang-Arg mode [:lua](https://neovim.io/doc/user/lua.html#%3Alua)  		:lua		execute [Lua](https://neovim.io/doc/user/lua.html#Lua) command [:luado](https://neovim.io/doc/user/lua.html#%3Aluado)  	:luad[o]	execute](https://neovim.io/doc/user/lua.html#%3Aluafile)
        - [Lua command for each line [:luafile](https://neovim.io/doc/user/lua.html#%3Aluafile)  	:luaf[ile]	execute [Lua](https://neovim.io/doc/user/lua.html#Lua) script file [:lvimgrep](https://neovim.io/doc/user/quickfix.html#%3Alvimgrep)  	:lv[imgrep]	search for pattern in files [:lvimgrepadd](https://neovim.io/doc/user/quickfix.html#%3Alvimgrepadd)  	:lvimgrepa[dd]	like :vimgrep, but append to current list [:lwindow](https://neovim.io/doc/user/quickfix.html#%3Alwindow)  	:lw[indow]	open or close location window [:move](https://neovim.io/doc/user/change.html#%3Amove)  		:m[ove]		move lines [:mark](https://neovim.io/doc/user/motion.html#%3Amark)  		:ma[rk]		set a mark [:make](https://neovim.io/doc/user/quickfix.html#%3Amake)  		:mak[e]		execute external command ['makeprg'](https://neovim.io/doc/user/options.html#'makeprg') and parse 				error messages [:map](https://neovim.io/doc/user/map.html#%3Amap)  		:map		show or enter a mapping [:mapclear](https://neovim.io/doc/user/map.html#%3Amapclear)  	:mapc[lear]	clear all mappings for Normal and Visual mode [:marks](https://neovim.io/doc/user/motion.html#%3Amarks)  	:marks		list all marks [:match](https://neovim.io/doc/user/pattern.html#%3Amatch)  	:mat[ch]	define a match to highlight [:menu](https://neovim.io/doc/user/gui.html#%3Amenu)  		:me[nu]		enter a new menu item [:menutranslate](https://neovim.io/doc/user/mlang.html#%3Amenutranslate)  :menut[ranslate] add a menu translation item [:messages](https://neovim.io/doc/user/message.html#%3Amessages)  	:mes[sages]	view previously displayed messages [:mkexrc](https://neovim.io/doc/user/starting.html#%3Amkexrc)  	:mk[exrc]	write current mappings and settings to a file [:mksession](https://neovim.io/doc/user/starting.html#%3Amksession)  	:mks[ession]	write session info to a file [:mkspell](https://neovim.io/doc/user/spell.html#%3Amkspell)  	:mksp[ell]	produce .spl spell file [:mkvimrc](https://neovim.io/doc/user/starting.html#%3Amkvimrc)  	:mkv[imrc]	write current mappings and settings to a file [:mkview](https://neovim.io/doc/user/starting.html#%3Amkview)  	:mkvie[w]	write view of current window to a file [:mode](https://neovim.io/doc/user/various.html#%3Amode)  		:mod[e]		show or change the screen mode [:next](https://neovim.io/doc/user/editing.html#%3Anext)  		:n[ext]		go to next file in the argument list [:new](https://neovim.io/doc/user/windows.html#%3Anew)  		:new		create a new empty window [:nmap](https://neovim.io/doc/user/map.html#%3Anmap)  		:nm[ap]		like ":map" but for Normal mode [:nmapclear](https://neovim.io/doc/user/map.html#%3Anmapclear)  	:nmapc[lear]	clear all mappings for Normal mode [:nmenu](https://neovim.io/doc/user/gui.html#%3Anmenu)  	:nme[nu]	add menu for Normal mode [:nnoremap](https://neovim.io/doc/user/map.html#%3Annoremap)  	:nn[oremap]	like ":noremap" but for Normal mode [:nnoremenu](https://neovim.io/doc/user/gui.html#%3Annoremenu)  	:nnoreme[nu]	like ":noremenu" but for Normal mode [:noautocmd](https://neovim.io/doc/user/autocmd.html#%3Anoautocmd)  	:noa[utocmd]	following commands don't trigger autocommands [:noremap](https://neovim.io/doc/user/map.html#%3Anoremap)  	:no[remap]	enter a mapping that will not be remapped [:nohlsearch](https://neovim.io/doc/user/pattern.html#%3Anohlsearch)  	:noh[lsearch]	suspend ['hlsearch'](https://neovim.io/doc/user/options.html#'hlsearch') highlighting [:noreabbrev](https://neovim.io/doc/user/map.html#%3Anoreabbrev)  	:norea[bbrev]	enter an abbreviation that will not be 				remapped [:noremenu](https://neovim.io/doc/user/gui.html#%3Anoremenu)  	:noreme[nu]	enter a menu that will not be remapped [:normal](https://neovim.io/doc/user/various.html#%3Anormal)  	:norm[al]	execute Normal mode commands [:noswapfile](https://neovim.io/doc/user/recover.html#%3Anoswapfile)  	:nos[wapfile]	following commands don't create a swap file [:number](https://neovim.io/doc/user/various.html#%3Anumber)  	:nu[mber]	print lines with line number [:nunmap](https://neovim.io/doc/user/map.html#%3Anunmap)  	:nun[map]	like ":unmap" but for Normal mode [:nunmenu](https://neovim.io/doc/user/gui.html#%3Anunmenu)  	:nunme[nu]	remove menu for Normal mode [:oldfiles](https://neovim.io/doc/user/starting.html#%3Aoldfiles)  	:ol[dfiles]	list files that have marks in the [shada](https://neovim.io/doc/user/starting.html#shada) file [:omap](https://neovim.io/doc/user/map.html#%3Aomap)  		:om[ap]		like ":map" but for Operator-pending mode [:omapclear](https://neovim.io/doc/user/map.html#%3Aomapclear)  	:omapc[lear]	remove all mappings for Operator-pending mode [:omenu](https://neovim.io/doc/user/gui.html#%3Aomenu)  	:ome[nu]	add menu for Operator-pending mode [:only](https://neovim.io/doc/user/windows.html#%3Aonly)  		:on[ly]		close all windows except the current one [:onoremap](https://neovim.io/doc/user/map.html#%3Aonoremap)  	:ono[remap]	like ":noremap" but for Operator-pending mode [:onoremenu](https://neovim.io/doc/user/gui.html#%3Aonoremenu)  	:onoreme[nu]	like ":noremenu" but for Operator-pending mode [:options](https://neovim.io/doc/user/options.html#%3Aoptions)  	:opt[ions]	open the options-window [:ounmap](https://neovim.io/doc/user/map.html#%3Aounmap)  	:ou[nmap]	like ":unmap" but for Operator-pending mode [:ounmenu](https://neovim.io/doc/user/gui.html#%3Aounmenu)  	:ounme[nu]	remove menu for Operator-pending mode [:packadd](https://neovim.io/doc/user/repeat.html#%3Apackadd)  	:pa[ckadd]	add a plugin from ['packpath'](https://neovim.io/doc/user/options.html#'packpath') [:packloadall](https://neovim.io/doc/user/repeat.html#%3Apackloadall)  	:packl[oadall]	load all packages under ['packpath'](https://neovim.io/doc/user/options.html#'packpath') [:pbuffer](https://neovim.io/doc/user/windows.html#%3Apbuffer)  	:pb[uffer]	edit buffer in the preview window [:pclose](https://neovim.io/doc/user/windows.html#%3Apclose)  	:pc[lose]	close preview window [:pedit](https://neovim.io/doc/user/windows.html#%3Apedit)  	:ped[it]	edit file in the preview window [:perl](https://neovim.io/doc/user/if_perl.html#%3Aperl)  		:pe[rl]		execute perl command [:perldo](https://neovim.io/doc/user/if_perl.html#%3Aperldo)  	:perld[o]	execute perl command for each line [:perlfile](https://neovim.io/doc/user/if_perl.html#%3Aperlfile)  	:perlf[ile]	execute perl script file [:print](https://neovim.io/doc/user/various.html#%3Aprint)  	:p[rint]	print lines [:profdel](https://neovim.io/doc/user/repeat.html#%3Aprofdel)  	:profd[el]	stop profiling a function or script [:profile](https://neovim.io/doc/user/repeat.html#%3Aprofile)  	:prof[ile]	profiling functions and scripts [:pop](https://neovim.io/doc/user/tagsrch.html#%3Apop)  		:po[p]		jump to older entry in tag stack [:popup](https://neovim.io/doc/user/gui.html#%3Apopup)  	:popu[p]	popup a menu by name [:ppop](https://neovim.io/doc/user/windows.html#%3Appop)  		:pp[op]		":pop" in preview window [:preserve](https://neovim.io/doc/user/recover.html#%3Apreserve)  	:pre[serve]	write all text to swap file [:previous](https://neovim.io/doc/user/editing.html#%3Aprevious)  	:prev[ious]	go to previous file in argument list [:psearch](https://neovim.io/doc/user/windows.html#%3Apsearch)  	:ps[earch]	like ":ijump" but shows match in preview window [:ptag](https://neovim.io/doc/user/windows.html#%3Aptag)  		:pt[ag]		show tag in preview window [:ptNext](https://neovim.io/doc/user/tagsrch.html#%3AptNext)  	:ptN[ext]	[:tNext](https://neovim.io/doc/user/tagsrch.html#%3AtNext) in preview window [:ptfirst](https://neovim.io/doc/user/tagsrch.html#%3Aptfirst)  	:ptf[irst]	[:trewind](https://neovim.io/doc/user/tagsrch.html#%3Atrewind) in preview window [:ptjump](https://neovim.io/doc/user/tagsrch.html#%3Aptjump)  	:ptj[ump](https://neovim.io/doc/user/tagsrch.html#%3Atjump)
        - []	[:tjump](https://neovim.io/doc/user/tagsrch.html#%3Atjump) and show tag in preview window [:ptlast](https://neovim.io/doc/user/tagsrch.html#%3Aptlast)  	:ptl[ast]	[:tlast](https://neovim.io/doc/user/tagsrch.html#%3Atlast) in preview window [:ptnext](https://neovim.io/doc/user/tagsrch.html#%3Aptnext)  	:ptn[ext]	[:tnext](https://neovim.io/doc/user/tagsrch.html#%3Atnext) in preview window [:ptprevious](https://neovim.io/doc/user/tagsrch.html#%3Aptprevious)  	:ptp[revious]	[:tprevious](https://neovim.io/doc/user/tagsrch.html#%3Atprevious) in preview window [:ptrewind](https://neovim.io/doc/user/tagsrch.html#%3Aptrewind)  	:ptr[ewind]	[:trewind](https://neovim.io/doc/user/tagsrch.html#%3Atrewind) in preview window [:ptselect](https://neovim.io/doc/user/tagsrch.html#%3Aptselect)  	:pts[elect]	[:tselect](https://neovim.io/doc/user/tagsrch.html#%3Atselect) and show tag in preview window [:put](https://neovim.io/doc/user/change.html#%3Aput)  		:pu[t]		insert contents of register in the text [:pwd](https://neovim.io/doc/user/editing.html#%3Apwd)  		:pw[d]		print current directory [:py3](https://neovim.io/doc/user/if_pyth.html#%3Apy3)  		:py3		execute Python 3 command [:python3](https://neovim.io/doc/user/if_pyth.html#%3Apython3)  	:python3	same as :py3 [:py3do](https://neovim.io/doc/user/if_pyth.html#%3Apy3do)  	:py3d[o]	execute Python 3 command for each line [:py3file](https://neovim.io/doc/user/if_pyth.html#%3Apy3file)  	:py3f[ile]	execute Python 3 script file [:python](https://neovim.io/doc/user/if_pyth.html#%3Apython)  	:py[thon]	execute Python command [:pydo](https://neovim.io/doc/user/if_pyth.html#%3Apydo)  		:pyd[o]		execute Python command for each line [:pyfile](https://neovim.io/doc/user/if_pyth.html#%3Apyfile)  	:pyf[ile]	execute Python script file [:pyx](https://neovim.io/doc/user/if_pyth.html#%3Apyx)  		:pyx		execute [python_x](https://neovim.io/doc/user/if_pyth.html#python_x) command [:pythonx](https://neovim.io/doc/user/if_pyth.html#%3Apythonx)  	:pythonx	same as :pyx [:pyxdo](https://neovim.io/doc/user/if_pyth.html#%3Apyxdo)  	:pyxd[o]	execute [python_x](https://neovim.io/doc/user/if_pyth.html#python_x) command for each line [:pyxfile](https://neovim.io/doc/user/if_pyth.html#%3Apyxfile)  	:pyxf[ile]	execute [python_x](https://neovim.io/doc/user/if_pyth.html#python_x) script file [:quit](https://neovim.io/doc/user/editing.html#%3Aquit)  		:q[uit]		quit current window (when one window quit Vim) [:quitall](https://neovim.io/doc/user/editing.html#%3Aquitall)  	:quita[ll]	quit Vim [:qall](https://neovim.io/doc/user/editing.html#%3Aqall)  		:qa[ll]		quit Vim [:read](https://neovim.io/doc/user/insert.html#%3Aread)  		:r[ead]		read file into the text [:recover](https://neovim.io/doc/user/recover.html#%3Arecover)  	:rec[over]	recover a file from a swap file [:redo](https://neovim.io/doc/user/undo.html#%3Aredo)  		:red[o]		redo one undone change [:redir](https://neovim.io/doc/user/various.html#%3Aredir)  	:redi[r]	redirect messages to a file or register [:redraw](https://neovim.io/doc/user/various.html#%3Aredraw)  	:redr[aw]	force a redraw of the display [:redrawstatus](https://neovim.io/doc/user/various.html#%3Aredrawstatus)  	:redraws[tatus]	force a redraw of the status line(s) and 				window bar(s) [:redrawtabline](https://neovim.io/doc/user/various.html#%3Aredrawtabline)  :redrawt[abline]  force a redraw of the tabline [:registers](https://neovim.io/doc/user/change.html#%3Aregisters)  	:reg[isters]	display the contents of registers [:resize](https://neovim.io/doc/user/windows.html#%3Aresize)  	:res[ize]	change current window height [:restart](https://neovim.io/doc/user/gui.html#%3Arestart)  	:restart	restart the Nvim server [:retab](https://neovim.io/doc/user/change.html#%3Aretab)  	:ret[ab]	change tab size [:return](https://neovim.io/doc/user/userfunc.html#%3Areturn)  	:retu[rn]	return from a user function [:rewind](https://neovim.io/doc/user/editing.html#%3Arewind)  	:rew[ind]	go to the first file in the argument list [:right](https://neovim.io/doc/user/change.html#%3Aright)  	:ri[ght]	right align text [:rightbelow](https://neovim.io/doc/user/windows.html#%3Arightbelow)  	:rightb[elow]	make split window appear right or below [:rshada](https://neovim.io/doc/user/starting.html#%3Arshada)  	:rsh[ada]	read from [shada](https://neovim.io/doc/user/starting.html#shada) file [:ruby](https://neovim.io/doc/user/if_ruby.html#%3Aruby)  		:rub[y]		execute Ruby command [:rubydo](https://neovim.io/doc/user/if_ruby.html#%3Arubydo)  	:rubyd[o]	execute Ruby command for each line [:rubyfile](https://neovim.io/doc/user/if_ruby.html#%3Arubyfile)  	:rubyf[ile]	execute Ruby script file [:rundo](https://neovim.io/doc/user/undo.html#%3Arundo)  	:rund[o]	read undo information from a file [:runtime](https://neovim.io/doc/user/repeat.html#%3Aruntime)  	:ru[ntime]	source vim scripts in ['runtimepath'](https://neovim.io/doc/user/options.html#'runtimepath') [:substitute](https://neovim.io/doc/user/change.html#%3Asubstitute)  	:s[ubstitute]	find and replace text [:sNext](https://neovim.io/doc/user/windows.html#%3AsNext)  	:sN[ext]	split window and go to previous file in 				argument list [:sandbox](https://neovim.io/doc/user/vimeval.html#%3Asandbox)  	:san[dbox]	execute a command in the sandbox [:sargument](https://neovim.io/doc/user/windows.html#%3Asargument)  	:sa[rgument]	split window and go to specific file in 				argument list [:sall](https://neovim.io/doc/user/windows.html#%3Asall)  		:sal[l]		open a window for each file in argument list [:saveas](https://neovim.io/doc/user/editing.html#%3Asaveas)  	:sav[eas]	save file under another name. [:sbuffer](https://neovim.io/doc/user/windows.html#%3Asbuffer)  	:sb[uffer]	split window and go to specific file in the 				buffer list [:sbNext](https://neovim.io/doc/user/windows.html#%3AsbNext)  	:sbN[ext]	split window and go to previous file in the 				buffer list [:sball](https://neovim.io/doc/user/windows.html#%3Asball)  	:sba[ll]	open a window for each file in the buffer list [:sbfirst](https://neovim.io/doc/user/windows.html#%3Asbfirst)  	:sbf[irst]	split window and go to first file in the 				buffer list [:sblast](https://neovim.io/doc/user/windows.html#%3Asblast)  	:sbl[ast]	split window and go to last file in buffer 				list [:sbmodified](https://neovim.io/doc/user/windows.html#%3Asbmodified)  	:sbm[odified]	split window and go to modified file in the 				buffer list [:sbnext](https://neovim.io/doc/user/windows.html#%3Asbnext)  	:sbn[ext]	split window and go to next file in the buffer 				list [:sbprevious](https://neovim.io/doc/user/windows.html#%3Asbprevious)  	:sbp[revious]	split window and go to previous file in the 				buffer list [:sbrewind](https://neovim.io/doc/user/windows.html#%3Asbrewind)  	:sbr[ewind]	split window and go to first file in the 				buffer list [:scriptnames](https://neovim.io/doc/user/repeat.html#%3Ascriptnames)  	:scr[iptnames]	list names of all sourced Vim scripts [:scriptencoding](https://neovim.io/doc/user/repeat.html#%3Ascriptencoding) :scripte[ncoding]  encoding used in sourced Vim script [:set](https://neovim.io/doc/user/options.html#%3Aset)  		:se[t]		show or set options [:setfiletype](https://neovim.io/doc/user/options.html#%3Asetfiletype)  	:setf[iletype]	set ['filetype'](https://neovim.io/doc/user/options.html#'filetype'), unless it was set already [:setglobal](https://neovim.io/doc/user/options.html#%3Asetglobal)  	:setg[lobal]	show global values of options [:setlocal](https://neovim.io/doc/user/options.html#%3Asetlocal)  	:setl[ocal]	show or set options locally [:sfind](https://neovim.io/doc/user/windows.html#%3Asfind)  	:sf[ind]	split current window and edit file in ['path'](https://neovim.io/doc/user/options.html#'path') [:sfirst](https://neovim.io/doc/user/windows.html#%3Asfirst)  	:sfir[st]	split window and go to first file in the 				argument list [](https://neovim.io/doc/user/sign.html#%3Asign)
        - [:sign](https://neovim.io/doc/user/sign.html#%3Asign)  		:sig[n]		manipulate signs [:silent](https://neovim.io/doc/user/various.html#%3Asilent)  	:sil[ent]	run a command silently [:sleep](https://neovim.io/doc/user/various.html#%3Asleep)  	:sl[eep]	do nothing for a few seconds [:sleep!](https://neovim.io/doc/user/various.html#%3Asleep%21)  	:sl[eep]!	do nothing for a few seconds, without the 				cursor visible [:slast](https://neovim.io/doc/user/windows.html#%3Aslast)  	:sla[st]	split window and go to last file in the 				argument list [:smagic](https://neovim.io/doc/user/change.html#%3Asmagic)  	:sm[agic]	:substitute with ['magic'](https://neovim.io/doc/user/options.html#'magic') [:smap](https://neovim.io/doc/user/map.html#%3Asmap)  		:smap		like ":map" but for Select mode [:smapclear](https://neovim.io/doc/user/map.html#%3Asmapclear)  	:smapc[lear]	remove all mappings for Select mode [:smenu](https://neovim.io/doc/user/gui.html#%3Asmenu)  	:sme[nu]	add menu for Select mode [:snext](https://neovim.io/doc/user/windows.html#%3Asnext)  	:sn[ext]	split window and go to next file in the 				argument list [:snomagic](https://neovim.io/doc/user/change.html#%3Asnomagic)  	:sno[magic]	:substitute with ['nomagic'](https://neovim.io/doc/user/options.html#'nomagic') [:snoremap](https://neovim.io/doc/user/map.html#%3Asnoremap)  	:snor[emap]	like ":noremap" but for Select mode [:snoremenu](https://neovim.io/doc/user/gui.html#%3Asnoremenu)  	:snoreme[nu]	like ":noremenu" but for Select mode [:sort](https://neovim.io/doc/user/change.html#%3Asort)  		:sor[t]		sort lines [:source](https://neovim.io/doc/user/repeat.html#%3Asource)  	:so[urce]	read Vim or Ex commands from a file [:spelldump](https://neovim.io/doc/user/spell.html#%3Aspelldump)  	:spelld[ump]	split window and fill with all correct words [:spellgood](https://neovim.io/doc/user/spell.html#%3Aspellgood)  	:spe[llgood]	add good word for spelling [:spellinfo](https://neovim.io/doc/user/spell.html#%3Aspellinfo)  	:spelli[nfo]	show info about loaded spell files [:spellrare](https://neovim.io/doc/user/spell.html#%3Aspellrare)  	:spellra[re]	add rare word for spelling [:spellrepall](https://neovim.io/doc/user/spell.html#%3Aspellrepall)  	:spellr[epall]	replace all bad words like last [z=](https://neovim.io/doc/user/spell.html#z%3D) [:spellundo](https://neovim.io/doc/user/spell.html#%3Aspellundo)  	:spellu[ndo]	remove good or bad word [:spellwrong](https://neovim.io/doc/user/spell.html#%3Aspellwrong)  	:spellw[rong]	add spelling mistake [:split](https://neovim.io/doc/user/windows.html#%3Asplit)  	:sp[lit]	split current window [:sprevious](https://neovim.io/doc/user/windows.html#%3Asprevious)  	:spr[evious]	split window and go to previous file in the 				argument list [:srewind](https://neovim.io/doc/user/windows.html#%3Asrewind)  	:sre[wind]	split window and go to first file in the 				argument list [:stop](https://neovim.io/doc/user/starting.html#%3Astop)  		:st[op]		suspend the editor or escape to a shell [:stag](https://neovim.io/doc/user/windows.html#%3Astag)  		:sta[g]		split window and jump to a tag [:startinsert](https://neovim.io/doc/user/insert.html#%3Astartinsert)  	:star[tinsert]	start Insert mode [:startgreplace](https://neovim.io/doc/user/insert.html#%3Astartgreplace)  :startg[replace] start Virtual Replace mode [:startreplace](https://neovim.io/doc/user/insert.html#%3Astartreplace)  	:startr[eplace]	start Replace mode [:stopinsert](https://neovim.io/doc/user/insert.html#%3Astopinsert)  	:stopi[nsert]	stop Insert mode [:stjump](https://neovim.io/doc/user/tagsrch.html#%3Astjump)  	:stj[ump]	do ":tjump" and split window [:stselect](https://neovim.io/doc/user/tagsrch.html#%3Astselect)  	:sts[elect]	do ":tselect" and split window [:sunhide](https://neovim.io/doc/user/windows.html#%3Asunhide)  	:sun[hide]	same as ":unhide" [:sunmap](https://neovim.io/doc/user/map.html#%3Asunmap)  	:sunm[ap]	like ":unmap" but for Select mode [:sunmenu](https://neovim.io/doc/user/gui.html#%3Asunmenu)  	:sunme[nu]	remove menu for Select mode [:suspend](https://neovim.io/doc/user/starting.html#%3Asuspend)  	:sus[pend]	same as ":stop" [:sview](https://neovim.io/doc/user/windows.html#%3Asview)  	:sv[iew]	split window and edit file read-only [:swapname](https://neovim.io/doc/user/recover.html#%3Aswapname)  	:sw[apname]	show the name of the current swap file [:syntax](https://neovim.io/doc/user/syntax.html#%3Asyntax)  	:sy[ntax]	syntax highlighting [:syntime](https://neovim.io/doc/user/syntax.html#%3Asyntime)  	:synti[me]	measure syntax highlighting speed [:syncbind](https://neovim.io/doc/user/scroll.html#%3Asyncbind)  	:sync[bind]	sync scroll binding [:t](https://neovim.io/doc/user/change.html#%3At)  		:t		same as ":copy" [:tNext](https://neovim.io/doc/user/tagsrch.html#%3AtNext)  	:tN[ext]	jump to previous matching tag [:tabNext](https://neovim.io/doc/user/tabpage.html#%3AtabNext)  	:tabN[ext]	go to previous tab page [:tabclose](https://neovim.io/doc/user/tabpage.html#%3Atabclose)  	:tabc[lose]	close current tab page [:tabdo](https://neovim.io/doc/user/tabpage.html#%3Atabdo)  	:tabd[o]	execute command in each tab page [:tabedit](https://neovim.io/doc/user/tabpage.html#%3Atabedit)  	:tabe[dit]	edit a file in a new tab page [:tabfind](https://neovim.io/doc/user/tabpage.html#%3Atabfind)  	:tabf[ind]	find file in ['path'](https://neovim.io/doc/user/options.html#'path'), edit it in a new tab page [:tabfirst](https://neovim.io/doc/user/tabpage.html#%3Atabfirst)  	:tabfir[st]	go to first tab page [:tablast](https://neovim.io/doc/user/tabpage.html#%3Atablast)  	:tabl[ast]	go to last tab page [:tabmove](https://neovim.io/doc/user/tabpage.html#%3Atabmove)  	:tabm[ove]	move tab page to other position [:tabnew](https://neovim.io/doc/user/tabpage.html#%3Atabnew)  	:tabnew		edit a file in a new tab page [:tabnext](https://neovim.io/doc/user/tabpage.html#%3Atabnext)  	:tabn[ext]	go to next tab page [:tabonly](https://neovim.io/doc/user/tabpage.html#%3Atabonly)  	:tabo[nly]	close all tab pages except the current one [:tabprevious](https://neovim.io/doc/user/tabpage.html#%3Atabprevious)  	:tabp[revious]	go to previous tab page [:tabrewind](https://neovim.io/doc/user/tabpage.html#%3Atabrewind)  	:tabr[ewind]	go to first tab page [:tabs](https://neovim.io/doc/user/tabpage.html#%3Atabs)  		:tabs		list the tab pages and what they contain [:tab](https://neovim.io/doc/user/tabpage.html#%3Atab)  		:tab		create new tab when opening new window [:tag](https://neovim.io/doc/user/tagsrch.html#%3Atag)  		:ta[g]		jump to tag [:tags](https://neovim.io/doc/user/tagsrch.html#%3Atags)  		:tags		show the contents of the tag stack [:tcd](https://neovim.io/doc/user/editing.html#%3Atcd)  		:tc[d]		change directory for tab page [:tchdir](https://neovim.io/doc/user/editing.html#%3Atchdir)  	:tch[dir]	change directory for tab page [:terminal](https://neovim.io/doc/user/various.html#%3Aterminal)  	:te[rminal]	open a terminal buffer [:tfirst](https://neovim.io/doc/user/tagsrch.html#%3Atfirst)  	:tf[irst]	jump to first matching tag [:throw](https://neovim.io/doc/user/vimeval.html#%3Athrow)  	:th[row]	throw an exception [:tjump](https://neovim.io/doc/user/tagsrch.html#%3Atjump)  	:tj[ump]	like ":tselect", but jump directly when there 				is only one match [:tlast](https://neovim.io/doc/user/tagsrch.html#%3Atlast)  	:tl[ast]	jump to last matching tag [:tlmenu](https://neovim.io/doc/user/gui.html#%3Atlmenu)  	:tlm[enu]	add menu for [Terminal-mode](https://neovim.io/doc/user/intro.html#Terminal-mode) [:tlnoremenu](https://neovim.io/doc/user/gui.html#%3Atlnoremenu)  	:tln[oremenu]	like ":noremenu" but for [Terminal-mode](https://neovim.io/doc/user/intro.html#Terminal-mode) [:tlunmenu](https://neovim.io/doc/user/gui.html#%3Atlunmenu)  	:tlu[nmenu]	remove menu](https://neovim.io/doc/user/intro.html#Terminal-mode)
        - [for [Terminal-mode](https://neovim.io/doc/user/intro.html#Terminal-mode) [:tmapclear](https://neovim.io/doc/user/map.html#%3Atmapclear)  	:tmapc[lear]	remove all mappings for [Terminal-mode](https://neovim.io/doc/user/intro.html#Terminal-mode) [:tmap](https://neovim.io/doc/user/map.html#%3Atmap)  		:tma[p]		like ":map" but for [Terminal-mode](https://neovim.io/doc/user/intro.html#Terminal-mode) [:tmenu](https://neovim.io/doc/user/gui.html#%3Atmenu)  	:tm[enu]	define menu tooltip [:tnext](https://neovim.io/doc/user/tagsrch.html#%3Atnext)  	:tn[ext]	jump to next matching tag [:tnoremap](https://neovim.io/doc/user/map.html#%3Atnoremap)  	:tno[remap]	like ":noremap" but for [Terminal-mode](https://neovim.io/doc/user/intro.html#Terminal-mode) [:topleft](https://neovim.io/doc/user/windows.html#%3Atopleft)  	:to[pleft]	make split window appear at top or far left [:tprevious](https://neovim.io/doc/user/tagsrch.html#%3Atprevious)  	:tp[revious]	jump to previous matching tag [:trewind](https://neovim.io/doc/user/tagsrch.html#%3Atrewind)  	:tr[ewind]	jump to first matching tag [:trust](https://neovim.io/doc/user/editing.html#%3Atrust)  	:trust		add or remove file from trust database [:try](https://neovim.io/doc/user/vimeval.html#%3Atry)  		:try		execute commands, abort on error or exception [:tselect](https://neovim.io/doc/user/tagsrch.html#%3Atselect)  	:ts[elect]	list matching tags and select one [:tunmap](https://neovim.io/doc/user/map.html#%3Atunmap)  	:tunma[p]	like ":unmap" but for [Terminal-mode](https://neovim.io/doc/user/intro.html#Terminal-mode) [:tunmenu](https://neovim.io/doc/user/gui.html#%3Atunmenu)  	:tu[nmenu]	remove menu tooltip [:undo](https://neovim.io/doc/user/undo.html#%3Aundo)  		:u[ndo]		undo last change(s) [:undojoin](https://neovim.io/doc/user/undo.html#%3Aundojoin)  	:undoj[oin]	join next change with previous undo block [:undolist](https://neovim.io/doc/user/undo.html#%3Aundolist)  	:undol[ist]	list leafs of the undo tree [:unabbreviate](https://neovim.io/doc/user/map.html#%3Aunabbreviate)  	:una[bbreviate]	remove abbreviation [:unhide](https://neovim.io/doc/user/windows.html#%3Aunhide)  	:unh[ide]	open a window for each loaded file in the 				buffer list [:uniq](https://neovim.io/doc/user/change.html#%3Auniq)  		:uni[q]		uniq lines [:unlet](https://neovim.io/doc/user/vimeval.html#%3Aunlet)  	:unl[et]	delete variable [:unlockvar](https://neovim.io/doc/user/vimeval.html#%3Aunlockvar)  	:unlo[ckvar]	unlock variables [:unmap](https://neovim.io/doc/user/map.html#%3Aunmap)  	:unm[ap]	remove mapping [:unmenu](https://neovim.io/doc/user/gui.html#%3Aunmenu)  	:unme[nu]	remove menu [:unsilent](https://neovim.io/doc/user/various.html#%3Aunsilent)  	:uns[ilent]	run a command not silently [:update](https://neovim.io/doc/user/editing.html#%3Aupdate)  	:up[date]	write buffer if modified [:vglobal](https://neovim.io/doc/user/repeat.html#%3Avglobal)  	:v[global]	execute commands for not matching lines [:version](https://neovim.io/doc/user/various.html#%3Aversion)  	:ve[rsion]	print version number and other info [:verbose](https://neovim.io/doc/user/various.html#%3Averbose)  	:verb[ose]	execute command with ['verbose'](https://neovim.io/doc/user/options.html#'verbose') set [:vertical](https://neovim.io/doc/user/windows.html#%3Avertical)  	:vert[ical]	make following command split vertically [:vimgrep](https://neovim.io/doc/user/quickfix.html#%3Avimgrep)  	:vim[grep]	search for pattern in files [:vimgrepadd](https://neovim.io/doc/user/quickfix.html#%3Avimgrepadd)  	:vimgrepa[dd]	like :vimgrep, but append to current list [:visual](https://neovim.io/doc/user/editing.html#%3Avisual)  	:vi[sual]	same as ":edit", but turns off "Ex" mode [:viusage](https://neovim.io/doc/user/helphelp.html#%3Aviusage)  	:viu[sage]	overview of Normal mode commands [:view](https://neovim.io/doc/user/editing.html#%3Aview)  		:vie[w]		edit a file read-only [:vmap](https://neovim.io/doc/user/map.html#%3Avmap)  		:vm[ap]		like ":map" but for Visual+Select mode [:vmapclear](https://neovim.io/doc/user/map.html#%3Avmapclear)  	:vmapc[lear]	remove all mappings for Visual+Select mode [:vmenu](https://neovim.io/doc/user/gui.html#%3Avmenu)  	:vme[nu]	add menu for Visual+Select mode [:vnew](https://neovim.io/doc/user/windows.html#%3Avnew)  		:vne[w]		create a new empty window, vertically split [:vnoremap](https://neovim.io/doc/user/map.html#%3Avnoremap)  	:vn[oremap]	like ":noremap" but for Visual+Select mode [:vnoremenu](https://neovim.io/doc/user/gui.html#%3Avnoremenu)  	:vnoreme[nu]	like ":noremenu" but for Visual+Select mode [:vsplit](https://neovim.io/doc/user/windows.html#%3Avsplit)  	:vs[plit]	split current window vertically [:vunmap](https://neovim.io/doc/user/map.html#%3Avunmap)  	:vu[nmap]	like ":unmap" but for Visual+Select mode [:vunmenu](https://neovim.io/doc/user/gui.html#%3Avunmenu)  	:vunme[nu]	remove menu for Visual+Select mode [:windo](https://neovim.io/doc/user/windows.html#%3Awindo)  	:wind[o]	execute command in each window [:write](https://neovim.io/doc/user/editing.html#%3Awrite)  	:w[rite]	write to a file [:wNext](https://neovim.io/doc/user/editing.html#%3AwNext)  	:wN[ext]	write to a file and go to previous file in 				argument list [:wall](https://neovim.io/doc/user/editing.html#%3Awall)  		:wa[ll]		write all (changed) buffers [:while](https://neovim.io/doc/user/vimeval.html#%3Awhile)  	:wh[ile]	execute loop for as long as condition met [:winsize](https://neovim.io/doc/user/gui.html#%3Awinsize)  	:wi[nsize]	get or set window size (obsolete) [:wincmd](https://neovim.io/doc/user/windows.html#%3Awincmd)  	:winc[md]	execute a Window (`CTRL-W`) command [:winpos](https://neovim.io/doc/user/gui.html#%3Awinpos)  	:winp[os]	get or set window position [:wnext](https://neovim.io/doc/user/editing.html#%3Awnext)  	:wn[ext]	write to a file and go to next file in 				argument list [:wprevious](https://neovim.io/doc/user/editing.html#%3Awprevious)  	:wp[revious]	write to a file and go to previous file in 				argument list [:wq](https://neovim.io/doc/user/editing.html#%3Awq)  		:wq		write to a file and quit window or Vim [:wqall](https://neovim.io/doc/user/editing.html#%3Awqall)  	:wqa[ll]	write all changed buffers and quit Vim [:wshada](https://neovim.io/doc/user/starting.html#%3Awshada)  	:wsh[ada]	write to ShaDa file [:wundo](https://neovim.io/doc/user/undo.html#%3Awundo)  	:wu[ndo]	write undo information to a file [:xit](https://neovim.io/doc/user/editing.html#%3Axit)  		:x[it]		write if buffer changed and close window [:xall](https://neovim.io/doc/user/editing.html#%3Axall)  		:xa[ll]		same as ":wqall" [:xmapclear](https://neovim.io/doc/user/map.html#%3Axmapclear)  	:xmapc[lear]	remove all mappings for Visual mode [:xmap](https://neovim.io/doc/user/map.html#%3Axmap)  		:xm[ap]		like ":map" but for Visual mode [:xmenu](https://neovim.io/doc/user/gui.html#%3Axmenu)  	:xme[nu]	add menu for Visual mode [:xnoremap](https://neovim.io/doc/user/map.html#%3Axnoremap)  	:xn[oremap]	like ":noremap" but for Visual mode [:xnoremenu](https://neovim.io/doc/user/gui.html#%3Axnoremenu)  	:xnoreme[nu]	like ":noremenu" but for Visual mode [:xunmap](https://neovim.io/doc/user/map.html#%3Axunmap)  	:xu[nmap]	like ":unmap" but for Visual mode [:xunmenu](https://neovim.io/doc/user/gui.html#%3Axunmenu)  	:xunme[nu]	remove menu for Visual mode [:yank](https://neovim.io/doc/user/change.html#%3Ayank)  		:y[ank]		yank lines into a register [:z](https://neovim.io/doc/user/various.html#%3Az)  		:z		print some lines [:~](https://neovim.io/doc/user/change.html#%3A~)  		:~		repeat last ":substitute"
- ranking keyboard symbols
    - _ 
    - * 
    - , 
    - . 
    - ) 
    - (   
    - ;   
    - -   
    - =  
    - /   
    - >  
    - "   
    - {   
    - &  
    - }   
    - :   
    - +  
    - #  
    - ]   
    - [   
    - <   
    - %  
    - !   
    - '   
    - |   
    - ?  
    - @  
    - $  
    - ^  
    - ~  
    - foo - bar  hhhh
- less keys #linux
    - SUMMARY OF LESS COMMANDS

        - Commands marked with  may be preceded by a number, N.

        - Notes in parentheses indicate the behavior if N is given. 
        - A key preceded by a caret indicates the Ctrl key; thus ^K is ctrl-K.

    - {{h}} or {{shift h}} Display this help.
    - {{q}} or {{Q}} or  {{ZZ}}     Exit.
    - {{:q}} or  {{:Q }}    Exit.(command)
    - Moving

        - e  ^E  {{j}}  ^N  CR    Forward  one line   (or N lines).

        - y  ^Y  {{k}}  ^K  ^P    Backward one line   (or N lines).

        - {{f}}  ^F  ^V  SPACE    Forward  one window (or N lines).

        - {{b}} ^B  ESC-v        Backward one window (or N lines).

        - z                   Forward  one window (and set window to N).

        - w                   Backward one window (and set window to N).

        - ESC-SPACE           Forward  one window, but don't stop at end-of-file.

        - d  ^D               Forward  one half-window (and set half-window to N).

        - u  ^U               Backward one half-window (and set half-window to N).

        - ESC-)  RightArrow   Right one half screen width (or N positions).

        - ESC-(  LeftArrow    Left  one half screen width (or N positions).

        - ESC-}  ^RightArrow   Right to last column displayed.

        - ESC-{  ^LeftArrow    Left  to first column.

        - F                    Forward forever; like "tail -f".

        - ESC-F                Like F but stop when search pattern is found.

        - r  ^R  ^L            Repaint screen.

        - R                    Repaint screen, discarding buffered input.

        - ---------------------------------------------------
        - Default "window" is the screen height.

        - Default "half-window" is half of the screen height.

        - --------------------------------------------------------------------------           
    - SEARCHING 
        - {{/pattern}}            Search forward for (N-th) matching line.

        - {{?pattern}}            Search backward for (N-th) matching line.

        - {{n}}                   Repeat previous search (for N-th occurrence).

        - {{N}}                   Repeat previous search in reverse direction.

        - ESC-n               Repeat previous search, spanning files.

        - ESC-N               Repeat previous search, reverse dir. & spanning files.

        - ESC-u                Undo (toggle) search highlighting.

        - &pattern            Display only matching lines

        - ---------------------------------------------------

        - A search pattern may begin with one or more of:

        - ^N or !  Search for NON-matching lines.

        - ^E or   Search multiple files (pass thru END OF FILE).

        - ^F or @  Start search at FIRST file (for /) or last file (for ?).

        - ^K       Highlight matches, but don't move (KEEP position).

        - ^R       Don't use REGULAR EXPRESSIONS.

        - ---------------------------------------------------------------------------
    - JUMPING

        - {{g}}  <  ESC-<         Go to first line in file (or line N).

        - {{G}}  >  ESC->         Go to last line in file (or line N).

        - {{p}}  %                Go to beginning of file (or N percent into file).

        - t                   Go to the (N-th) next tag.

        - T                   Go to the (N-th) previous tag.

        - {  (  [             Find close bracket } ) ].

        - }  )  ]             Find open bracket { ( [.

        - ESC-^F <c1> <c2>    Find close bracket <c2>.

        - ESC-^B <c1> <c2>    Find open bracket <c1>

        - ---------------------------------------------------

        - Each "find close bracket" command goes forward to the close bracket

        - matching the (N-th) open bracket in the top line.

        - Each "find open bracket" command goes backward to the open bracket

        - matching the (N-th) close bracket in the bottom line.


        - m<letter>            Mark the current top line with <letter>.

        - M<letter>            Mark the current bottom line with <letter>.

        - '<letter>            Go to a previously marked position.

        - ''                   Go to the previous position.

        - ^X^X                 Same as '.

        - ESC-M<letter>        Clear a mark.

        - ---------------------------------------------------

        - A mark is any upper-case or lower-case letter.

        - Certain marks are predefined:

        - ^  means  beginning of the file

        - $  means  end of the file

    - CHANGING FILES

        - :e [file]            Examine a new file.

        - ^X^V                 Same as :e.

        - :n                  Examine the (N-th) next file from the command line.

        - :p                  Examine the (N-th) previous file from the command line.

        - :x                  Examine the first (or N-th) file from the command line.

        - :d                   Delete the current file from the command line list.

        - =  ^G  :f            Print current file name.

    - MISCELLANEOUS COMMANDS

        - -<flag>              Toggle a command line option [see OPTIONS below].

        - --<name>             Toggle a command line option, by name.

        - _<flag>              Display the setting of a command line option.

        - __<name>             Display the setting of an option, by name.

        - +cmd                 Execute the less cmd each time a new file is examined.


        - !command             Execute the shell command with $SHELL.

        - |Xcommand            Pipe file between current pos & mark X to shell command.

        - s file               Save input to a file.

        - v                    Edit the current file with $VISUAL or $EDITOR.

        - V                    Print version number of "less".

    - OPTIONS

        - Most options may be changed either on the command line, or from within less by using the - or -- command.

        - Options may be given in one of two forms: either a single character preceded by a -, or a name preceded by --.

 
        - -?  ........ 
        - --help
                  Display help (from command line).
 
        - -a  ........  --search-skip-screen
                  Search skips current screen.

        - -A  ........  --SEARCH-SKIP-SCREEN
                  Search starts just after target line.

        - -b [N]  ....  --buffers=[N]
                  Number of buffers.

        - -B  ........  --auto-buffers
                  Don't automatically allocate buffers for pipes.

        - -c  ........  --clear-screen
                  Repaint by clearing rather than scrolling.

        - -d  ........  --dumb
                  Dumb terminal.

        - -D [xn.n]  .  --color=xn.n
                  Set screen colors. (MS-DOS only)

        - -e  -E  ....  --quit-at-eof  --QUIT-AT-EOF
                  Quit at end of file.

        - -f  ........  --force
                  Force open non-regular files.

        - -F  ........  --quit-if-one-screen
                  Quit if entire file fits on first screen.

        - -g  ........  --hilite-search
                  Highlight only last match for searches.

        - -G  ........  --HILITE-SEARCH
                  Don't highlight any matches for searches.

        - -h [N]  ....  --max-back-scroll=[N]
                  Backward scroll limit.

        - -i  ........  --ignore-case
                  Ignore case in searches that do not contain uppercase.

        - -I  ........  --IGNORE-CASE
                  Ignore case in all searches.

        - -j [N]  ....  --jump-target=[N]
                  Screen position of target lines.

        - -J  ........  --status-column
                  Display a status column at left edge of screen.

        - -k [file]  .  --lesskey-file=[file]
                  Use a lesskey file.

        - -K  ........  --quit-on-intr
                  Exit less in response to ctrl-C.

        - -L  ........  --no-lessopen
                  Ignore the LESSOPEN environment variable.

        - -m  -M  ....  --long-prompt  --LONG-PROMPT
                  Set prompt style.

        - -n  -N  ....  --line-numbers  --LINE-NUMBERS
                  Don't use line numbers.

        - -o [file]  .  --log-file=[file]
                  Copy to log file (standard input only).

        - -O [file]  .  --LOG-FILE=[file]
                  Copy to log file (unconditionally overwrite).

        - -p [pattern]  --pattern=[pattern]
                  Start at pattern (from command line).

        - -P [prompt]   --prompt=[prompt]
                  Define new prompt.

        - -q  -Q  ....  --quiet  --QUIET  --silent --SILENT
                  Quiet the terminal bell.

        - -r  -R  ....  --raw-control-chars  --RAW-CONTROL-CHARS
                  Output "raw" control characters.

        - -s  ........  --squeeze-blank-lines
                  Squeeze multiple blank lines.

        - -S  ........  --chop-long-lines
                  Chop (truncate) long lines rather than wrapping.

        - -t [tag]  ..  --tag=[tag]
                  Find a tag.

        - -T [tagsfile] --tag-file=[tagsfile]
                  Use an alternate tags file.

        - -u  -U  ....  --underline-special  --UNDERLINE-SPECIAL
                  Change handling of backspaces.

        - -V  ........  --version
                  Display the version number of "less".

        - -w  ........  --hilite-unread
                  Highlight first new line after forward-screen.

        - -W  ........  --HILITE-UNREAD
                  Highlight first new line after any forward movement.

        - -x [N[,...]]  --tabs=[N[,...]]
                  Set tab stops.

        - -X  ........  --no-init
                  Don't use termcap init/deinit strings.

        - -y [N]  ....  --max-forw-scroll=[N]
                  Forward scroll limit.

        - -z [N]  ....  --window=[N]
                  Set size of window.

        - -" [c[c]]  .  --quotes=[c[c]]
                  Set shell quote characters.

        - -~  ........  --tilde
                  Don't display tildes after end of file.

        - -# [N]  ....  --shift=[N]
                  Horizontal scroll amount (0 = one half screen width)
                --follow-name
                  The F command changes files if the input file is renamed.
                --mouse
                  Enable mouse input.
                --no-keypad
                  Don't send termcap keypad init/deinit strings.
                --no-histdups
                  Remove duplicates from command history.
                --rscroll=C
                  Set the character used to mark truncated lines.
                --save-marks
                  Retain marks across invocations of less.
                --use-backslash
                  Subsequent options use backslash as escape char.
                --wheel-lines=N
                  Each click of the mouse wheel moves N lines.

    - LINE EDITING

        - These keys can be used to edit text being entered on the "command line" at the bottom of the screen.

        - RightArrow ..................... ESC-l ... Move cursor right one character.

        - LeftArrow ...................... ESC-h ... Move cursor left one character.

        - ctrl-RightArrow  ESC-RightArrow  ESC-w ... Move cursor right one word.

        - ctrl-LeftArrow   ESC-LeftArrow   ESC-b ... Move cursor left one word.

        - HOME ........................... ESC-0 ... Move cursor to start of line.

        - END ............................ ESC-$ ... Move cursor to end of line.

        - BACKSPACE ................................ Delete char to left of cursor.

        - DELETE ......................... ESC-x ... Delete char under cursor.

        - ctrl-BACKSPACE   ESC-BACKSPACE ........... Delete word to left of cursor.

        - ctrl-DELETE .... ESC-DELETE .... ESC-X ... Delete word under cursor.

        - ctrl-U ......... ESC (MS-DOS only) ....... Delete entire line.

        - UpArrow ........................ ESC-k ... Retrieve previous command line.

        - DownArrow ...................... ESC-j ... Retrieve next command line.

        - TAB ...................................... Complete filename & cycle.

        - SHIFT-TAB ...................... ESC-TAB   Complete filename & reverse cycle.

        - ctrl-L ................................... Complete filename, list all.
    - 
- Typing
    - # Typing Speed Categories
        - Typing speed can be categorized into different levels based on proficiency and speed. Here are some categories:
            - **Average Typist**: 
                - Typists who type around 40 words per minute (WPM) are considered average. 
                - This is the typical speed for many people who do not specialize in typing.
            - **Above Average Typist**: 
                - Typists who can type between 50 to 60 WPM are considered above average. 
                - This speed is often expected in professional settings and can significantly enhance productivity.
            - **Professional Typist**: 
                - Typists who can type between 80 to 95 WPM are considered professional. 
                - These speeds are often required for dispatch positions and other time-sensitive typing jobs.
            - **Advanced Typist**: 
                - Typists who can type over 120 WPM are considered advanced.
                - This level of speed is rare and is often seen in competitive typing or among highly skilled typists.
            - **Speed Typist**: 
                - Some typists can achieve speeds over 200 WPM for short periods, such as 15-second typing tests with simple English words. 
        - These categories reflect different levels of typing proficiency and speed, which can impact productivity and suitability for various typing-related jobs. 
    - Where is key in Qwerty Layout?
        - f {{left index finger}} 
        - j {{right index finger}} 
        - g {{extent left index finger}} 
        - h {{extent right index finger}} 
        - r {{up left index finger}} 
        - u {{up extent right index finger}} 
        - t {{up extent left index finger}} 
        - y {{up right index finger}} 
        - v {{down left index finger}} 
        - m {{down right index finger}} 
        - b {{down extent left index finger}} 
        - n {{down extent right index finger}} 
        - 
        - d {{left middle finger}} 
        - k {{right middle finger}} 
        - e {{up left middle finger}} 
        - i {{up right middle finger}} 
        - c {{down left middle finger}} 
        - , (comma) {{down right middle finger}} 
        - 
        - s {{left ring finger}} 
        - l {{right ring finger}} 
        - w {{up left ring finger}} 
        - o {{up right ring finger}} 
        - x {{down left ring finger}} 
        - . (dot) {{down right ring finger}} 
        - 
        - a {{left little finger}} 
        - ; (semicolon) {{right little finger}} 
        - q {{up left little finger}} 
        - p {{up right little finger}} 
        - z {{down left little finger}} 
        - / {{down right little finger}} 
        - ' (apostrophe) {{extent right little finger}} 
        - [ (bracket) {{up extent right little finger}} 
        - ] (bracket) {{up extent right little finger}} 
        - \  {{up extent right little finger}} 
        - 
        - left thumb
        - right thumb
    - klavaro
        - do each at least lesson 13 times
        - 01 lesson jf 
            - top 77
        - 02 lesson dk
            - top 78
        - 03 lesson sl
            - top 75
        - 04 lesson a;
            - top 69
        - 05 lesson asdf
            - top 25
        - 06 lesson jkl;
            - top 31
        - 07 lesson gh
            - top 50
        - 08 lesson asdfg
            - top 22
        - 09 lesson hjkl;
            - top 28
        - 10 lesson asdfghjkl;
            - top 15
        - 11 lesson ru
            - top 63
        - 12 lesson ei
            - top 70
        - 13 lesson wo
            - top 65
        - 14 lesson qp
            - top 41
        - 15 lesson qwer
            - top 25
        - 16 lesson uiop
            - top 10
        - 17 lesson ty
            - top 54
        - 18 lesson qwert
        - 19 lesson yuiop
        - 20 lesson qwertyuiop
        - 21 lesson vm
            - top 58
        - 22 lesson c,
            - top 42
        - 23 lesson x.
            - top 38
        - 24 lesson z/
            - top 46
        - 25 lesson zxcv
        - 26 lesson m,./
        - 27 lesson bn
            - top 47
        - 28 lesson zxcvb
        - 29 lesson nm,./
        - 30 lesson zxcvbnm,./
        - 31 lesson qwertyuiopasdfghjkl;zxcvbnm,./
        - 32 lesson 1234
        - 33 lesson 7890
        - 34 lesson 12347890
        - 35 lesson 1234567890
        - 36 lesson 1234567890qwertyuiopasdfghjkl;zxcvbnm,./
        - 37 lesson !@#$
        - 38 lesson &*()
        - 39 lesson !@#$&*()
        - 40 lesson `-=%^_+
        - 41 lesson `-=~!@#$%^&*()_+
        - 42 lesson
        - 43 lesson
    - 
- tmux key #linux
    - Description Keys
    - General
        - Start a new tmux session tmux
        - Detach from current session tmux detach
        - Attach to last used session tmux attach
        - Show every session, window, pane, etc. tmux info
        - Send the prefix key ctrl + b  ctrl + b
        - Describe key binding ctrl + b  /
        - Prompt for a command ctrl + b  :
        - List key bindings ctrl + b  ?
        - Show a clock ctrl + b  t
        - Show messages ctrl + b  ~
        - Delete the most recent paste buffer ctrl + b  -
        - Choose a paste buffer from a list ctrl + b  =
        - List all paste buffers ctrl + b  #
        - Enter copy mode ctrl + b  [
        - Enter copy mode and scroll up ctrl + b  pageup
        - Paste the most recent paste buffer ctrl + b  ]
    - Windows
        - Split window vertically ctrl + b  "
        - Split window horizontally ctrl + b  %
        - Kill current window ctrl + b  &
        - Prompt for window index to select ctrl + b  '
        - Rename current window ctrl + b  ,
        - Move the current window ctrl + b  .
        - Select window 0 ctrl + b  0
        - Select window 1 ctrl + b  1
        - Select window 2 ctrl + b  2
        - Select window 3 ctrl + b  3
        - Select window 4 ctrl + b  4
        - Select window 5 ctrl + b  5
        - Select window 6 ctrl + b  6
        - Select window 7 ctrl + b  7
        - Select window 8 ctrl + b  8
        - Select window 9 ctrl + b  9
        - Display window information ctrl + b  i
        - Create a new window ctrl + b  c
        - Select the next window ctrl + b  n
        - Move the visible part of the window up ctrl + b  shift + up
        - Move the visible part of the window down ctrl + b  shift + down
        - Move the visible part of the window left ctrl + b  shift + left
        - Move the visible part of the window right ctrl + b  shift + right
        - Select the next window with an alert ctrl + b  alt + n
        - Select the previous window with an alert ctrl + b  alt + p
        - Choose a window from a list ctrl + b  w
        - Select the previously current window ctrl + b  l
    - Panes
        - Break pane to a new window ctrl + b  !
        - Rotate through the panes ctrl + b  ctrl + o
        - Select the pane above the active pane ctrl + b  up
        - Select the pane below the active pane ctrl + b  down
        - Select the pane to the left of the active pane ctrl + b  left
        - Select the pane to the right of the active pane ctrl + b  right
        - Move to the previously active pane ctrl + b  ;
        - Clear the marked pane ctrl + b  m
        - Search for a pane ctrl + b  f
        - Kill the active pane ctrl + b  x
        - Zoom the active pane ctrl + b  z
        - Swap the active pane with the pane above ctrl + b  {
        - Swap the active pane with the pane below ctrl + b  }
        - Rotate through the panes in reverse ctrl + b  alt + o
        - Spread panes out evenly ctrl + b  e
        - Toggle the marked pane ctrl + b  m
        - Select the next pane ctrl + b  o
        - Select the previous pane ctrl + b  p
        - Display pane numbers ctrl + b  q
    - Sessions
        - List all sessions tmux ls
        - Choose a session from a list ctrl + b  s
        - Rename current session ctrl + b  $
        - Switch to previous client ctrl + b  (
        - Switch to next client ctrl + b  )
        - Switch to the last client ctrl + b  l
        - Detach the current client ctrl + b  d
        - Suspend the current client ctrl + b  ctrl + z
        - Redraw the current client ctrl + b  r
        - Choose a client from a list ctrl + b  d
    - Layout
        - Set the even-horizontal layout ctrl + b  alt + 1
        - Set the even-vertical layout ctrl + b  alt + 2
        - Set the main-horizontal layout ctrl + b  alt + 3
        - Set the main-vertical layout ctrl + b  alt + 4
        - Select the tiled layout ctrl + b  alt + 5
        - Resize the pane up by 5 ctrl + b  alt + up
        - Resize the pane down by 5 ctrl + b  alt + down
        - Resize the pane left by 5 ctrl + b  alt + left
        - Resize the pane right by 5 ctrl + b  alt + right
        - Resize the pane up ctrl + b  ctrl + up
        - Resize the pane down ctrl + b  ctrl + down
        - Resize the pane left ctrl + b  ctrl + left
        - Resize the pane right ctrl + b  ctrl + right
        - Select next layout ctrl + b  space
