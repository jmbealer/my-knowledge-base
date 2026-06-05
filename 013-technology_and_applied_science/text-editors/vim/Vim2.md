---
title: Vim2
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 11-01-01
reference: 
description: 
aliases: 
tags: 
---
# Vim2

    normal
    insert
    command
    visual
s moves cursor left m-s
t moves cursor down
n moves cursor up
b moves cursor right m-b
x delete character under the cursor
i inserts before the cursor
a inserts after the cursor
dw delete word /#needs be at the beginning word
d$ delete to the end fo the line
d delete command
    [number] d object OR d [number] object
        number - is how many times to execute the command (optional, default=1)
        d - is the command to delete
        object - is what the command will operate on
            w - from the cursor to the end of the word, including the space.
            e - from the cursor to the end of the word, NOT including the space.
            $ - from the cursor to the end of the line.
dd delete line
    [number]-command
number-command-object
command mode
:qa! <cr>(Enter) /#quits without saving
:wqa <cr> /# writes and quits
/#adjusting typematic delay and rate
xset r rate 200 30
    maybe try 400 25
tneastn
itneas tntieants ienatist inatisea
Vim Navigation Commands
    move cursor wise
    move word wise
    move line wise
        G last line
        gg first line
    move screen wise
       H first line on screen
       M middle line on screen
       L last line on screen
       zz center screen
       zt top screen
       zb bottom screen

Vim Navigation
    Line navigation
Vim Navigation
    Line navigation
        k - navigate upwards
        j - navigate downwards
        l - navigate right side
        h - navigate left side
        
    Screen navigation
    Word navigation
    Special navigation
    Paragraph navigation
    Search navigation
    Code navigation
    Navigation from command line
set character limit to 80

vim --startuptime startup.txt startup.txt



Basic

| Key | Action | Followed by | New Key |
|--- | --- | --- | --- |
| a | enter insert mode after current character | Followed by |
| b | back word | Followed by | s
| c | change command | Followed by |
| d | delete command | Followed by |
| e | end of word | Followed by |
| f | find character after cursor in current line | Followed by |
| g | Action | Followed by |
| h | move left one character | Followed by |
| i | enter insert mode before current character | Followed by |
| j | move down one line | Followed by | t
| k | move up one line | Followed by | n
| l | move right one character | Followed by |
| m | set mark | Followed by |
| n | find next | Followed by |
| o | open line below and enter insert mode | Followed by |
| p | put buffer after cursor | Followed by |
| q | record macro | Followed by |
| r | replace single character at cursor | Followed by |
| s | substitute single character with new text | Followed by |
| t | til forward | Followed by |
| u | undo | Followed by |
| v | visual mode | Followed by |
| w | next word | Followed by | b
| x | delete character | Followed by |
| y | yank | Followed by |
| z | Action | Followed by |
| gj | Action | Followed by | t
| gk | Action | Followed by | n
| A | Append at end of line | Followed by |
| B | back one WORD | Followed by |
| C | Change to end of line | Followed by |
| D | Delete to end of line | Followed by |
| E | move to end of WORD | Followed by |
| F | backwards of "f" | Followed by |
| G | goto line number prefixed, or goto end if none | Followed by |
| H | home cursor - goto first line on screen | Followed by |
| I | enter insert mode before first non-whitespace character | Followed by |
| J | join current line with next line | Followed by |
| K | Action | Followed by |
| L | goto last line on screen | Followed by |
| M | goto middle line on screen | Followed by |
| N | Action | Followed by |
| O | open line above and enter insert mode | Followed by |
| P | put buffer before cursor | Followed by |
| Q | leave visual mode (go into "ex" mode) | Followed by |
| R | replaces through end of current line, then insert | Followed by |
| S | substitute entire line - delete line, enters insert mode | Followed by |
| T | Action | Followed by |
| U | Action | Followed by |
| V | Action | Followed by |
| W | forward WORD | Followed by |
| X | delete backwards single character | Followed by |
| Y | Action | Followed by |
| Z | Action | Followed by |
| 0 | move to column zero | Followed by |
| 1-9 | numeric precursor to other commands | Followed by |
| "Space" | move right one character | Followed by |
| $ | move to end of line | Followed by |
| % | match nearest [],(),{} on line, to its match (same line or others) |
| ^ | move to first non-whitespace character of line | Followed by |
| ( | move to previous sentence | Followed by |
| ) | move to next sentence | Followed by |
| "pipe" | move to column zero | Followed by |
| - | move to first non-whitespace of previous line | Followed by |
| _ | similar to "^" but uses numeric prefix oddly | Followed by |
| + | move to first non-whitespace of next line | Followed by |
| [ | move to previous "{...}" section | Followed by |
| ] | move to next "{...}" section | Followed by |
| { | move to previous blank-line separated section | Followed by |
| } | move to next blank-line separated section | Followed by |
| ' | move to marked line, memorized column | Followed by |
| : | ex-submode | Followed by |
| " | access numbered buffer; load or access lettered buffer | Followed by |
| ~ | reverse caso of current character and move cursor forward | Followed by |
| . | repeat last text-changing command | Followed by |
| < | unindent command | Followed by |
| > | indent command | Followed by |
<!--ID: 1639528993489-->


