---
title: Ble.sh - Command-line Editing
author: Justin Bealer
date_created: 2024-08-02, 02-39-19
date_modified: 2024-09-17, 09-30-01
reference: 
description: 
aliases: 
tags: 
---
# Ble.sh - Command-line Editing

Key combination Widget Description

## 4.1 Insertion

M-C-m, M-RET (Emacs) `newline` Insert a newline
C-q, C-v `quoted-insert` Insert the next key-input characters literally
insert `overwrite-mode` Toggle insert and overwrite mode

## 4.2 Selection

In addition to the cursor position,
There is another recorded position called *mark* in addition to the current position.
When `ble.sh` is in the selection state, the text between the current position and *mark* is considered the selected region.

C-@, C-SP, NUL  M-SP (Emacs) `set-mark` Set a mark and start selection
C-x C-x `exchange-point-and-mark` Exchange the current position and the mark
C-w, S-delete `kill-region-or kill-backward-uword` Cut the current selection or uword (see below)
M-w (Emacs) C-insert `copy-region-or copy-backward-uword` Copy the current selection or uword (see below)
C-y, S-insert `yank` Paste

## 4.3 Characterwise Movement and Operation

C-f, right `forward-char` Go to the next character
C-b, left                                `backward-char`                          Go to the previous character
C-d, delete                              `delete-region-or delete-forward-char`   Delete the current selection or the next character
C-?, DEL, C-h, BS  `delete-region-or delete-backward-char`  Delete the current selection or the previous character
C-t                                                 `transpose-chars`                        Exchange the next and previous characters
C-] (Emacs)                                         `character-search-forward`               Search a character forward
M-C-] (Emacs)                                       `character-search-backward`              Search a character backward

## 4.4 Wordwise Movement and Operation

There are five types of words in `ble.sh`.
`eword` is an English word consisting of alphabets and digits.
`cword` is a C word consisting of alphabets, digits and underscores.
`uword` is a Unix word consisting of non-space characters that are not in the shell variable `IFS`.
`sword` is a shell word consisting of characters that are not spaces or special characters of the shell.
`fword` is a filename consisting of characters that are not spaces or slashes.

The following table shows the operations related to `cword` which have default bindings.

 Key combination                                                      Widget                    Description
:-------------------------------------------------------------------::-------------------------:-------------------------------------------------------
 C-right  M-f (Emacs)                      `forward-cword`           Go to the beginning of the next `cword`
 C-left   M-b (Emacs)                      `backward-cword`          Go to the end of the previous `cword`
 M-d (Emacs)                                               `kill-forward-cword`      Cut the next `cword`
 M-h (Emacs)                                               `kill-backward-cword`     Cut the previous `cword`
 C-delete                                                  `delete-forward-cword`    Delete the next `cword`
 C-_, C-DEL, C-BS                    `delete-backward-cword`   Delete the previous `cword`

The following table shows the operations related to `sword`.

 Key combination                                                                Widget                    Description
:-----------------------------------------------------------------------------::-------------------------:-------------------------------------------------------
 M-right (Emacs)                                                     `forward-sword`           Go to the beginning of the next `cword`
 M-left  (Emacs)                                                     `backward-sword`          Go to the end of the previous `cword`
 M-delete (Emacs)                                                    `copy-forward-sword`      Copy the next `cword`
 M-C-?, M-DEL, M-C-h, M-BS (Emacs)  `copy-backward-sword`     Copy the previous `cword`

The following table shows the operations related to `eword`.

 Key combination         Widget              Description
:----------------------::-------------------:--------------------------------------------------------
 M-c (Emacs)  `capitalize-eword`  Capitalize until the end of the next `eword`
 M-l (Emacs)  `downcase-eword`    Convert to lowercase until the end of the next `eword`  
 M-u (Emacs)  `upcase-eword`      Convert to uppercase until the end of the next `eword`  

There is an operation related to the spaces as well.

 Key combination          Widget                     Description
:-----------------------::--------------------------:------------------------------------------
 M-\\ (Emacs)  `delete-horizontal-space`  Delete spaces around the current position

## 4.5 Linewise Movement and Operation

 Key combination                           Widget                                 Description
:----------------------------------------::--------------------------------------:------------------------------------------------------------------------
 C-a, home           `beginning-of-line`                    Go to the beginning of line
 C-e, end            `end-of-line`                          Go to the end of line
 M-m                   (Emacs)  `non-space-beginning-of-line`          Go to the non-space beginning of line
 C-k                            `kill-forward-line`                    Delete the range between the current position and the end of line
 C-u                            `kill-backward-line`                   Delete the range between the current position and the beginning of line

## 4.6 Beginning and End of Command line

 Key combination      Widget                       Description
:-------------------::----------------------------:-------------------------------------------
 C-home    `beginning-of-text`          Go to the beginning of text
 C-end     `end-of-text`                Go to the end of text

## 4.7 Shift Selection

The selection can also be performed by the cursor movements with the shift modifier S-.
The region selected by shift can be copied, cutted, or pasted by the same keybindings as the normal selection.

 Key combination                                                      Widget                                 Description
:-------------------------------------------------------------------::--------------------------------------:-------------------------------------------------------
 S-C-f, S-right                                 `@marked forward-char`                 Go to the next character with selection
 S-C-b, S-left                                  `@marked backward-char`                Go to the previous character with selection
 S-C-right  M-S-f, M-F (Emacs)  `@marked forward-cword`                Go to the beginning of the next `cword` with selection
 S-C-left   M-S-b, M-B (Emacs)  `@marked backward-cword`               Go to the end of the previous `cword` with selection
 M-S-right (Emacs)                                         `@marked forward-sword`                Go to the beginning of the next `cword` with selection
 M-S-left  (Emacs)                                         `@marked backward-sword`               Go to the end of the previous `cword` with selection
 S-C-a, S-home                                  `@marked beginning-of-line`            Go to the beginning of line with selection
 S-C-e, S-end                                   `@marked end-of-line`                  Go to the end of line with selection
 M-S-m, M-M (Emacs)                             `@marked non-space-beginning-of-line`  Go to the non-space beginning of line with selection
 S-C-p, S-up                                    `@marked backward-line`                Go to the previous line with selection
 S-C-n, S-down                                  `@marked forward-line`                 Go to the next line with selection
 S-C-home                                                  `@marked beginning-of-text`            Go to the beginning of text with selection
 S-C-end                                                   `@marked end-of-text`                  Go to the end of text with selection

When one of the above widget is called, `ble.sh` enters the selection mode,
where the same keybindings as the ones to start the selection are available as follows:

 Key combination                                              Widget                         Description
:-----------------------------------------------------------::------------------------------:----------------------------------------------------------
 \_\_default\_\_                                   `selection/exit-default`       Exit the selection mode and do the default
 \_\_line\_limit\_\_                               `nop`                          Ignore
 S-C-f, S-right                         `forward-char`                 Go to the next character keeping selection
 S-C-b, S-left                          `backward-char`                Go to the previous character keeping selection
 S-C-right  M-S-f, M-F  `forward-cword`                Go to the beginning of the next `cword` keeping selection
 S-C-left   M-S-b, M-B  `backward-cword`               Go to the end of the previous `cword` keeping selection
 M-S-right                                         `forward-sword`                Go to the beginning of the next `cword` keeping selection
 M-S-left                                          `backward-sword`               Go to the end of the previous `cword` keeping selection
 S-C-a, S-home                          `beginning-of-line`            Go to the beginning of line keeping selection
 S-C-e, S-end                           `end-of-line`                  Go to the end of line keeping selection
 M-S-m, M-M                             `non-space-beginning-of-line`  Go to the non-space beginning of line keeping selection
 S-C-p, S-up                            `backward-line`                Go to the previous line keeping selection
 S-C-n, S-down                          `forward-line`                 Go to the next line keeping selection
 S-C-home                                          `beginning-of-text`            Go to the beginning of text keeping selection
 S-C-end                                           `end-of-text`                  Go to the end of text keeping selection

## 4.8 Keyboard Macros

 Key combination   Widget                  Description
:----------------::-----------------------:------------------------------
 C-x (  `start-keyboard-macro`  Start recording of the macro  
 C-x )  `end-keyboard-macro`    End recording of the macro
 C-x e  `call-keyboard-macro`   Replay the macro
 C-x P  `print-keyboard-macro`  Display the macro

## 4.9 History

 Key combination                                   Widget                   Description
:------------------------------------------------::------------------------:------------------------------------------------------
 C-prior  M-\< (Emacs)  `history-beginning`      Go to the first history entry
 C-next   M-\> (Emacs)  `history-end`            Go to the last history entry
 C-p, up                     `backward-line history`  Go to the previous line or the previous history entry
 C-n, down                   `forward-line history`   Go to the next line or the next history entry

## 4.10 Incremental search (`isearch`)

The incremental search can be started by the following commands.

 Key combination  Widget                       Description
:---------------::----------------------------:----------------------------------
 C-r   `history-isearch-backward`   Start incremental search forward  
 C-s   `history-isearch-forward`    Start incremental search backward

In the incremental search mode, the following key bindings are available:

 Key combination                                                Widget                               Description
:-------------------------------------------------------------::------------------------------------:----------------------------------------------------------
 \_\_defchar\_\_                                     `isearch/self-insert`                Append to search target
 C-r                                                 `isearch/backward`                   Search forward
 C-s                                                 `isearch/forward`                    Search backward
 C-?, DEL, C-h, BS  `isearch/prev`                       Go back to the previous search state
 \_\_default\_\_                                     `isearch/exit-default`               Exit the search and do default
 C-g                                                 `isearch/cancel`                     Cancel the search and restore the state before the search
 C-m, RET                                 `isearch/exit`                       Exit the search
 C-j, C-RET                               `isearch/accept-line`                Exit the search and execute RET
 C-d                                                 `isearch/exit-delete-forward-char`   Exit the search and delete a forward character

## 4.11 Non-incremental search (`nsearch`)

The non-incremental search can be started by the following commands.

 Key combination                                           Widget                               Description
:--------------------------------------------------------::------------------------------------:------------------------------------------------------------------------------------------------------------------
 prior, C-x C-p, C-x up   `history-search-backward`            Start non-incremental prefix-search in forward direction with the string before the current position
 next, C-x C-n, C-x down  `history-search-forward`             Start non-incremental prefix-search in backward direction backward with the string before the current position
 C-x p                                          `history-substring-search-backward`  Start non-incremental substring-search in forward direction with the string before the current position
 C-x n                                          `history-substring-search-forward`   Start non-incremental substring-search in backward direction backward with the string before the current position
 C-x <                                          `history-nsearch-backward`           Start non-incremental prefix-search in forward direction with a user-provided string
 C-x >                                          `history-nsearch-forward`            Start non-incremental prefix-search in backward direction backward with a user-provided string

In the non-incremental search mode, the following key bindings are available:

 Key combination                                  Widget                   Description
:-----------------------------------------------::------------------------:----------------------------------------------------
 C-r, C-p, up    `nsearch/backward`       Search forward
 C-s, C-n, down  `nsearch/forward`        Search backward
 C-g                                   `nsearch/cancel`         Cancel the current search
 C-m, RET                   `nsearch/exit`           Exit the current search
 C-j, C-RET                 `nsearch/accept-line`    Exit the current search and execute RET  
 \_\_default\_\_                       `nsearch/exit-default`   Exit the current search and do default

### 4.11.1 Widget `history-search`<sup><a id="widget-history-search" href="#user-content-widget-history-search">†</a></sup>

```
SYNOPSIS

  history-search OPTS
  history-search-backward OPTS
  history-search-forward OPTS
  history-substring-search-backward OPTS
  history-substring-search-forward OPTS
  history-nsearch-backward OPTS
  history-nsearch-forward OPTS
  history-nsearch-backward-again OPTS
  history-nsearch-forward-again OPTS

OPTS is a colon-separated list of

  backward, forward, substr, input, again, hide-status, immediate-accept
  action=ACTION, point=POINT, empty=EMPTY

ACTION

  goto, load

POINT

  begin, end, match-begin, match-end

EMPTY

  empty-search, previous-search, hide-status, history-move

```

- `history-search-forward OPTS` is a synonym of `history-search forward:OPTS`
- `history-search-backward OPTS` is a synonym of `history-search backward:OPTS`
- `history-substring-search-forward OPTS` is a synonym of `history-search forward:substr:OPTS`
- `history-substring-search-backward OPTS` is a synonym of `history-search backward:substr:OPTS`
- `history-nsearch-forward OPTS` is a synonym of `history-search forward:input:OPTS`
- `history-nsearch-backward OPTS` is a synonym of `history-search backward:input:OPTS`
- `history-nsearch-forward-again OPTS` is a synonym of `history-search forward:again:OPTS`
- `history-nsearch-backward-again OPTS` is a synonym of `history-search backward:again:OPTS`

These widgets search a target string from the command history.
By default, the string before the cursor in the command line is used as the target string.
The target string may be input by the user using OPTS `input` or `again` (see below).
By default, the history entries that start from the target string are searched.
The history entries that contain the target string may be searched using OPTS `substr` (see below).

`OPTS` is a colon-separated list of the following fields:

- `backward` (default) ... Start searching in forward direction, i.e., searching for older history entries.
- `forward` ... Start searching in forward direction, i.e., searching for newer history entries.
- `substr` ... Find history entries that contains the target string.
- `input` ... Prompt the user to input the target string.
- `again` ... Use the target string previously input by the user.
- `hide-status` ... Do not show the `nsearch` status of ``(nsearch #N: << !M >>) `NEEDLE'``.
- `immediate-accept` ... The widget `nsearch/exit`---which is defautly bound to C-m and RET---immediately runs the command.
- `action=ACTION` ... Specify the type of action taken when the search string is matched to a history entry. ACTION is one of the following values:
  - `goto` (default) ... Go to the history entry.
  - `load` ... Load the text of the history entry without moving the current history position. This is Bash's default behavior.
- `point=POINT` ... Specify the cursor position after the action. POINT is one of the following values:
  - `begin` ... the beginning of the command line
  - `end` ... the end of the command line
  - `match-begin` ... the beginning of the matched part
  - `match-end` (default) ... the end of the matched part
- `empty=EMPTY` ... Specify the special treatment on the empty command search.
  - `empty-search` (default) ... Start `nsearch` with an empty string.
  - `hide-status` ... Start `nsearch` with an empty string but do not show the nsearch status.
  - `previous-search` ... Start `nsearch` with the previous search string.
  - `history-move` ... Go to the previous/next history entry without starting the `nsearch`.
    The cursor position is set to the beginning of the command line to keep the string before the cursor empty.

## 4.12 Insert Words in History (`lastarg`)

 Key combination                         Widget                  Description
:--------------------------------------::-----------------------:------------------------------------------------------
 M-., M-_ (Emacs)  `insert-last-argument`  Insert the last argument of the previous command
 C-M-y (Emacs)                `insert-nth-argument`   Insert the `N`[1]th argument of the previous command  

`ble.sh` enters the lastarg mode on the widget `insert-last-argument`.
In the lastarg mode, the following bindings are available.

 Key combination                                                    Widget                  Description
:-----------------------------------------------------------------::-----------------------:----------------------------------------------------------------
 \_\_default\_\_                                         `lastarg/exit-default`  Exit the lastarg mode and do the default
 C-g, C-x C-g, C-M-g (Emacs)  `lastarg/cancel`        Delete the current word and cancel the lastarg mode
 M-., M-_ (Emacs)                             `lastarg/next`          Go to the last argument of the `N`[1] entries before in history
 M-C-u                                                   `universal-arg`         Start and end the argument input
 M--, M-0, M-1, M-2, M-3, M-4, M-5, M-6, M-7, M-8, M-9 (Emacs)  `append-arg-or lastarg/exit-default`  Set the argument
 C--, C-0, C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-8, C-9  `append-arg-or lastarg/exit-default`  Set the argument
 -, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 (Emacs)  `append-arg-or lastarg/exit-default`  Set the argument

## 4.13 Prompt String

In `ble.sh`, *prompt string* can be specified for various places such as `PS1`, `PS2`, `PS0`, `bleopt prompt_rps1`, `read -p`.
In addition to the standard Bash escape sequences of the form `\...`, there are also a few extensions.

### 4.13.1 Prompt Sequence `\g{[TYPE:]SPEC}` (v0.4)

Graphic attributes can be specified by the *gspec* format or the format used in `ble-face face=[TYPE:]SPEC`.
In addition to `TYPE` accepted by `ble-face`, `face` can also be used as a synonym of `copy`.

```bash
# Example
PS1='[\g{bold,fg=green}\u\g{none}@\g{bold,fg=navy}\h\g{none}]\$ '
```

### 4.13.2 User-defined Prompt Sequences

```bash
function ble/prompt/backslash:X {
  ble/prompt/print STRING
  ble/prompt/process-prompt-string PROMPT_STRING
  ble/prmopt/unit/add-hash '$VARNAME'
}
PS1='[\X]\$ '
```

In addition to the prompt sequences defined by Bash, user-defined sequences can be added and specified in the prompt string.
A sequence `\X` can be defined by creating a shell function named `ble/prompt/backslash:X`.
In the shell function, the string to be inserted in the prompt can be added by
calling `ble/prompt/print STRING` or `ble/prompt/process-prompt-string PROMPT_STRING`.
The former form inserts the literal argument in the prompt
while the latter processes the argument as another prompt string,
i.e., the prompt sequences and shell expansions in the argument will be processed.
By calling `ble/prompt/unit/add-hash '$VARNAME'`, the dependencies of the expanded results on arbitrary variables can be declared.
The corresponding prompts will be automatically updated on the variable changes.

The prompt sequence `\q{NAME ARGS...}` (v0.4) can be used to call
the named prompt sequence with arguments.
The named prompt sequences are processed by calling the shell function `ble/prompt/backslash:NAME ARGS...`.

```bash
# Example: User-defined sequence "hello"
function ble/prompt/backslash:hello {
  ble/prompt/print "Hello, ${1:-world}!"
}
PS1='[\q{hello $USER}]\$ '
```

### 4.13.3 Prompt Sequence `\q{row}` (v0.4)<sup><a id="backslash-row" href="#user-content-backslash-row">†</a></sup>

This is expanded to the current line number in the command line.

```
\q{row}  # Example result: 1
```

### 4.13.4 Prompt Sequence `\q{column}` (v0.4)<sup><a id="backslash-column" href="#user-content-backslash-column">†</a></sup>

This is expanded to the current column number in the command line.

```
\q{column}  # Example result: 5
```

### 4.13.5 Prompt Sequence `\q{position}` (v0.4)<sup><a id="backslash-position" href="#user-content-backslash-position">†</a></sup>

This is expanded to the current line and column numbers in the command line.
The format can be specified to the first argument as a printf format string.

```
\q{position}                     # Example result: (1,5)
\q{position line %s, column %s}  # Example result: line 1, column 5
```

### 4.13.6 Prompt Sequence `\q{point}` (v0.4)<sup><a id="backslash-point" href="#user-content-backslash-point">†</a></sup>

This is expanded to the current offset of the cursor position in the command line string.

```
\q{point}  # Example result: 3
```

### 4.13.7 Prompt Sequence `\q{mark}` (v0.4)<sup><a id="backslash-mark" href="#user-content-backslash-mark">†</a></sup>

This is expanded to the current offset of the mark position in the command line string.

```
\q{mark}  # Example result: 0
```

### 4.13.8 Prompt Sequence `\q{history-index}` (v0.4)<sup><a id="backslash-history-index" href="#user-content-backslash-history-index">†</a></sup>

This is expanded to the current history index in the command history.

```
\q{history-index}  # Example result: 0
```

### 4.13.9 Prompt Sequence `\q{history-percentile}` (v0.4)<sup><a id="backslash-history-percentile" href="#user-content-backslash-history-percentile">†</a></sup>

This is expanded to the percentile position of the current history position in the command history.

```
\q{history-percentile}  # Example result: 100%
```

## 4.14 Prompts

In addition to the standard prompts of Bash, such as `PS1`, `PS2`, `PS0`, additional prompts listed in this section are also available in `ble.sh`.
See also the editing-mode specific prompts:

- [`bleopt prompt_emacs_mode_indicator`](Manual-§5-Emacs-Mode#user-content-bleopt-prompt_emacs_mode_indicator)
- [`bleopt prompt_vi_mode_indicator`](Manual-§6-Vim-Mode#user-content-bleopt-prompt_vi_mode_indicator)

### 4.14.1 Bleopt `prompt_rps1` (Prompt string) (v0.3)<sup><a id="bleopt-prompt_rps1" href="#user-content-bleopt-prompt_rps1">†</a></sup>

```bash
# default
bleopt prompt_rps1= # ble-0.4
bleopt rps1=        # ble-0.3 (obsolete)
```

The option sets the right prompt.

```bash
# Example: show current time
bleopt prompt_rps1='\t'
```

### 4.14.2 Bleopt `prompt_ps1_final` (Prompt string) (v0.4)<sup><a id="bleopt-prompt_ps1_final" href="#user-content-bleopt-prompt_ps1_final">†</a></sup>

```bash
# default
bleopt prompt_ps1_final=
```

When a non-empty value is specified,
the prompt is replaced by this value before leaving the current command line.

### 4.14.3 Bleopt `prompt_ps1_transient` (Colon-separated list) (v0.4)<sup><a id="bleopt-prompt_ps1_transient" href="#user-content-bleopt-prompt_ps1_transient">†</a></sup>

```bash
# default
bleopt prompt_ps1_transient=
```

This is a colon-separated list of `always`, `same-dir` and `trim`.
When `prompt_ps1_final` is empty and this option has a non-empty value,
the prompt specified by `PS1` is erased on leaving the current command line.
If the value contains a field `trim`, only the last line of multiline `PS1` is preserved and the other lines are erased.
Otherwise, the command line will be redrawn as if `PS1=` is specified.
When a field `same-dir` is contained in the value
and the current working directory is different from the final directory of the previous command line,
this option `prompt_ps1_transient` is ignored.

### 4.14.4 Bleopt `prompt_rps1_final` (Prompt string) (v0.4)<sup><a id="bleopt-prompt_rps1_final" href="#user-content-bleopt-prompt_rps1_final">†</a></sup>

```bash
# default
bleopt prompt_rps1_final=
```

When a non-empty value is specified,
the right prompt is replaced by this value before leaving the current command line.

### 4.14.5 Bleopt `prompt_rps1_transient` (Empty/Non-empty) (v0.3)<sup><a id="bleopt-prompt_rps1_transient" href="#user-content-bleopt-prompt_rps1_transient">†</a></sup>

```bash
# default
bleopt prompt_rps1_transient= # ble-0.4
bleopt rps1_transient=        # ble-0.3 (obsolete)
```

When `prompt_rps1_final` is empty and this option has a non-empty value,
the right prompt specified by bleopt option `prompt_rps1` is erased before going to a new line.

### 4.14.6 Bleopt `prompt_xterm_title` (Prompt string) (v0.4)<sup><a id="bleopt-prompt_xterm_title" href="#user-content-bleopt-prompt_xterm_title">†</a></sup>

```bash
# default
bleopt prompt_xterm_title=
```

When a non-empty value is specified,
the title of the terminal is replaced by the specified string
using OSC 0 ; ... BEL just before showing `PS1`.

### 4.14.7 Bleopt `prompt_screen_title` (Prompt string) (v0.4)<sup><a id="bleopt-prompt_screen_title" href="#user-content-bleopt-prompt_screen_title">†</a></sup>

```bash
# default
bleopt prompt_screen_title=
```

This option is only effective inside terminal multiplexers such as GNU screen and tmux.
When a non-empty value is specified,
the window title of the terminal multiplexer is replaced by the specified string
using ESC k ... ST just before showing `PS1`.

### 4.14.8 Bleopt `prompt_term_status` (Prompt string) (v0.4)<sup><a id="bleopt-prompt_term_status" href="#user-content-bleopt-prompt_term_status">†</a></sup>

```bash
# default
bleopt prompt_term_status=
```

This option is only effective when terminfo entries `tsl` and `fsl` (or termcap entries `ts` and `ds`) are available.
When a non-empty value is specified,
the content of the status line is replaced using terminfo just before showing `PS1`.

### 4.14.9 Bleopt `prompt_status_line` (Prompt string) (v0.4)<sup><a id="bleopt-prompt_status_line" href="#user-content-bleopt-prompt_status_line">†</a></sup>

```bash
# default
bleopt prompt_status_line=
```

This option specifies the content of the status line which would be shown at the bottom line of the terminal.
When the evaluated value is empty, the status line is disabled.

See also the following settings, `bleopt prompt_status_align` and `ble-face promtp_status_line`, to control the text alignment and the background face of the status line.

### 4.14.10 Bleopt `prompt_status_align` (Enumerable) (v0.4)<sup><a id="bleopt-prompt_status_align" href="#user-content-bleopt-prompt_status_align">†</a></sup>

```bash
# default
bleopt prompt_status_align=$'justify=\r'
```

This option specifies the position of the content of the status line.
The values `left`, `right`, `center`, or `justify=CHAR` can be specified.
When `justify=CHAR` (where `CHAR` is a user-specified character) is set,
the expanded results are split by the character `CHAR`
and arranged to fill the line just like the text justification.

### 4.14.11 Face `prompt_status_line` (v0.4)<sup><a id="face-prompt_status_line" href="#user-content-face-prompt_status_line">†</a></sup>

```bash
# default
ble-face prompt_status_line='fg=231,bg=240'
```

This face specifies the background face of the status line.

## 4.15 Settings for Editing and Executing Commands

### 4.15.1 Bleopt `indent_offset` (Arithmetic) (v0.2)<sup><a id="bleopt-indent_offset" href="#user-content-bleopt-indent_offset">†</a></sup>

```bash
# default
bleopt indent_offset=4
```

This option specifies the unit width of indentation.

### 4.15.2 Bleopt `indent_tabs` (Arithmetic) (v0.2)<sup><a id="bleopt-indent_tabs" href="#user-content-bleopt-indent_tabs">†</a></sup>

```bash
# default
bleopt indent_tabs=1
```

This option controls whether tabs are used for indentation or not.
If `0` is specified, indentation will be made with only spaces,
or otherwise tabs are also used for indentation.

### 4.15.3 Bleopt `edit_forced_textmap` (Arithmetic) (v0.2)<sup><a id="bleopt-edit_forced_textmap" href="#user-content-bleopt-edit_forced_textmap">†</a></sup>

```bash
# default
bleopt edit_forced_textmap=1
```

This option controls the usage of the layout information
for the operations such as movement up, down.
If this option has the value `0`,
the layout information is used only when it is up to date.
Otherwise, when the layout information is out of date,
it is updated to be used for the operations.

### 4.15.4 Bleopt `edit_line_type` (Enumerable) (v0.4)<sup><a id="bleopt-edit_line_type" href="#user-content-bleopt-edit_line_type">†</a></sup>

```bash
# default
bleopt edit_line_type=logical
```

This option controls the interpretation of lines when going to the beginning or the end of the current line.
When the value `logical` is specified, the logical line is used,
i.e., the beginning and the end of the line is determined based on the newline characters in the edited text.
When the value `graphical` is specified, the graphical line is used,
i.e., the beginning and the end of the displayed line in the terminal is used.

### 4.15.5 Bleopt `edit_magic_expand` (Colon-separated list) (v0.4)<sup><a id="bleopt-edit_magic_expand" href="#user-content-bleopt-edit_magic_expand">†</a></sup>

```bash
# default
bleopt edit_magic_expand=history:sabbrev
```

This option specifies the set of expansions performed by `magic-space` with a colon-separated list of expansion types.
The values `history`, `sabbrev`, `alias`, and `autocd` can be specified.

### 4.15.6 Bleopt `edit_magic_opts` (Colon-separated list) (v0.4)<sup><a id="bleopt-edit_magic_opts" href="#user-content-bleopt-edit_magic_opts">†</a></sup>

```bash
# default
bleopt edit_magic_opts=
```

This option configures the detailed behavior of the widget `magic-space` with a colon-separated list.
If the field `inline-sabbrev-no-insert` is specified, the insertion of `SP` is skipped when the inline sabbrev is performed by `magic-space`.

### 4.15.7 Bleopt `edit_magic_accept` (Colon-separated list) (v0.4)<sup><a id="bleopt-edit_magic_accept" href="#user-content-bleopt-edit_magic_accept">†</a></sup>

```bash
# default
bleopt edit_magic_accept=verify-syntax
```

This option specifies the expansions performed on accept-line by a
colon-separated list.  The expansion is performed in a similar way as Bash's
history expansion.  When `sabbrev`, `alias`, `autocd`, and `history` is
specified, the respective expansions are attempted on the command line.  The
history expansion performed by `history` is identical to the one enabled by the
shell option `set -H`.  When `verify` is specified, if sabbrev, alias, or
autocd expansions changed the command line, the execution of the command line
is canceled so the user can examine or continue to edit the expanded line.  The
history expansion can be controlled by `shopt -s histverify` in a similar
manner.  When `verify-syntax` is specified and any expansions change the
command string, a syntax check is performed.  The command execution is canceled
when the command string is not syntactically complete.  When `history-line` is
specified, the history expansion replaces the command line instead of just
printing the expansion result.

### 4.15.8 Bleopt `delete_selection_mode` (Empty/Non-empty) (v0.2)<sup><a id="bleopt-delete_selection_mode" href="#user-content-bleopt-delete_selection_mode">†</a></sup>

```bash
# default
bleopt delete_selection_mode=1
```

This option controls the behavior of insertion when the selection is activated.
If this option has a non-empty value,
the contents of the selection is deleted before characters are inserted.
If this option is empty,
the selection is cleared before characters are inserted.

### 4.15.9 Bleopt `undo_point` (v0.2)<sup><a id="bleopt-undo_point" href="#user-content-bleopt-undo_point">†</a></sup>

```bash
# default
bleopt undo_point=end
```

This option specifies the cursor position after `undo`.
If the value is `end`, the cursor is moved to the end of the dirty section.
If the value is `beg`, the cursor is moved to the beginning of the dirty section.
Otherwise, the cursor position is restored to the original position when the state is recorded.

### 4.15.10 Bleopt `history_preserve_point` (Empty/Non-empty)<sup><a id="bleopt-history_preserve_point" href="#user-content-bleopt-history_preserve_point">†</a></sup>

```bash
# default
bleopt history_preserve_point=
```

This option specifies the cursor position after the move between the history entries.
If a non-empty value is specified, `ble.sh` tries to preserve the position.
When the string after the move is shorter than the original position, the cursor position is moved to the end of text.
If the value is empty, the cursor position is moved to the end of text when it moved to the older history entry,
or the beginning of text when it moved to the recent history entry.

### 4.15.11 Bleopt `term_cursor_external` (Arithmetic) (v0.2)<sup><a id="bleopt-term_cursor_external" href="#user-content-bleopt-term_cursor_external">†</a></sup>

```bash
# default
bleopt term_cursor_external=0
```

This option controls the cursor shape when external commands are executed.
The value is specified with the parameter of `DECSCUSR`.
It is enabled when `terminfo` (or `termcap`) has the entry `Ss`.
If your terminal actually supports `DECSCUSR` even though it is not shown up in `terminfo`,
please add the following setting to `~/.blerc`.

```bash
_ble_term_Ss=$'\e[@1 q'
```

### 4.15.12 Bleopt `term_stty_restore` (Empty/Non-empty) (v0.4)<sup><a id="bleopt-term_stty_restore" href="#user-content-bleopt-term_stty_restore">†</a></sup>

```bash
# default
bleopt term_stty_restore=
```

When this setting is set to a non-empty value, `ble.sh` saves the TTY state at
the end of the command executation and restores it before the next command
execution.  This adds a slight overload of running an extra call of `stty`.

> [!WARNING]
> If this is enabled, when a command breaks the TTY state, the effect remains
> in later commands.
>
> When this option is enabled in `~/.blerc` or in `~/.bashrc`, `source
> ~/.bashrc` or `ble-update` or `ble-reload` should not be executed in the
> internal state such as in `PROMPT_COMMAND`.  This is because `ble.sh` saves
> the TTY state at the point of setting `term_stty_restore` as the intial
> external TTY state.  If `source ~/.bashrc` or `ble-update` or `ble-reload` is
> executed in the internal state, the internal state can be unexpectedly
> captured as the external TTY state.

### 4.15.13 Bleopt `allow_exit_with_jobs` (Empty/Non-empty) (v0.3)<sup><a id="bleopt-allow_exit_with_jobs" href="#user-content-bleopt-allow_exit_with_jobs">†</a></sup>

```bash
# default
bleopt allow_exit_with_jobs=
```

If the value is empty,
the shell will not exit with `delete-forward-char-or-exit` (defaultly to which C-d is bounded)
when there are remaining jobs.
If a non-empty value is specified, the shell exits even if there are remaining jobs.

### 4.15.14 Bleopt `prompt_eol_mark` (ANSI Escape sequences) (v0.3)<sup><a id="bleopt-prompt_eol_mark" href="#user-content-bleopt-prompt_eol_mark">†</a></sup>

```bash
# default
bleopt prompt_eol_mark=$'\e[94m[ble: EOF]\e[m'
```

This option specifies the string when the command did not end at the beginning of line in the terminal.

### 4.15.15 Bleopt `prompt_ruler` (Empty/Enumerate/ANSI Escape sequences) (v0.4)<sup><a id="bleopt-prompt_ruler" href="#user-content-bleopt-prompt_ruler">†</a></sup>

```bash
# default
bleopt prompt_ruler=
```

This option specifies the ruler between the previous command and the prompt (like powerlevel10k `POWERLEVEL9K_PROMPT_{ADD_NEWLINE,SHOW_RULER,RULER_*}`).
When the empty value is specified, the ruler is disabled.  This is the default.
When the value `empty-line` is specified, an empty line is inserted between the command and the prompt.
When the other values are specified, the value is interpreted as an ANSI sequences, and the result is repeated to fill a line.

### 4.15.16 Bleopt `prompt_command_changes_layout` (Empty/Non-empty) (v0.4)<sup><a id="bleopt-prompt_command_changes_layout" href="#user-content-bleopt-prompt_command_changes_layout">†</a></sup>

```bash
# default
bleopt prompt_command_changes_layout=
```

This option specifies whether the commands called from the blehook `PRECMD` or the variable `PROMPT_COMMAND` output texts to the terminal and changes the layout.
When a non-empty value is specified, `ble.sh` resets the layout before running the hooks `PRECMD` and `PROMPT_COMMAND` and restores the layout after running the hooks.
When a empty value is specified, ble.sh assumes that these hooks do not output texts to the terminal and do not changes the cursor positions and skip the special treatment.

### 4.15.17 Bleopt `exec_restore_pipestatus` (Empty/Non-empty) (v0.4)<sup><a id="bleopt-exec_restore_pipestatus" href="#user-content-bleopt-exec_restore_pipestatus">†</a></sup>

```bash
# default
bleopt exec_restore_pipestatus=

# restore PIPESTATUS
bleopt exec_restore_pipestatus=1
```

If this option is set to a non-empty value,
`ble.sh` restores the values of `PIPESTATUS` of the previous command before running the next user command.
By default, this is turned off because it adds extra execution costs.
The values of `PIPESTATUS` of the previous command are always available with the array `BLE_PIPESTATUS` regardless of this setting.

### 4.15.18 Bleopt `edit_marker` (ANSI Escape sequences) (v0.4)<sup><a id="bleopt-edit_marker" href="#user-content-bleopt-edit_marker">†</a></sup>

```bash
# default
bleopt edit_marker=$'\e[94m[ble: %s]\e[m'
```

This setting defines the default style of the markers (such as `[ble: ...]`) used by `ble.sh` for the normal notifications.
When it is set to an empty string, the marker is disabled (unless additional information other than the marker needs to be output after the marker).
This default style can be overridden by specific mark settings, such as `exec_elapsed_mark` and `exec_exit_mark`.

### 4.15.19 Bleopt `edit_marker_error` (ANSI Escape sequences) (v0.4)<sup><a id="bleopt-edit_marker_error" href="#user-content-bleopt-edit_marker_error">†</a></sup>

```bash
# default
bleopt edit_marker_error=$'\e[91m[ble: %s]\e[m'
```

This setting defines the default style of the markers (such as `[ble: ...]`) used by `ble.sh` for the error information.
When it is set to an empty string, the marker is disabled (unless additional information other than the marker needs to be output after the marker).
This default style can be overridden by specific mark settings, such as `exec_errexit_mark`.

### 4.15.20 Bleopt `exec_errexit_mark` (ANSI Escape sequences) (v0.4)<sup><a id="bleopt-exec_errexit_mark" href="#user-content-bleopt-exec_errexit_mark">†</a></sup>

```bash
# default
bleopt exec_errexit_mark=$'\e[91m[ble: exit %d]\e[m'
```

This option specifies the string printed when the command exited with non-zero exit status.
When the value is empty, the exit status line will not be shown.

### 4.15.21 Bleopt `exec_elapsed_mark` (ANSI Escape sequences) (v0.4)<sup><a id="bleopt-exec_elapsed_mark" href="#user-content-bleopt-exec_elapsed_mark">†</a></sup>

```bash
# default
bleopt exec_elapsed_mark=$'\e[94m[ble: elapsed %s (CPU %s%%)]\e[m'
```

This option specifies the format of the command execution time report.
The format takes two arguments: the first is the string that explains the elapsed time, and the second is a number that represents the percentage of CPU core usage.

### 4.15.22 Bleopt `exec_elapsed_enabled` (Arithmetic) (v0.4)<sup><a id="bleopt-exec_elapsed_enabled" href="#user-content-bleopt-exec_elapsed_enabled">†</a></sup>

```bash
# default
bleopt exec_elapsed_enabled='usr+sys>=10000'
```

This option specifies the condition that the command execution time report is displayed after the command execution.
The condition is specified by an arithmetic expression, where a non-zero result causes displaying the report.
In the arithmetic expression, variables `real`, `{usr,sys}{,_self,_child}`, and `cpu` can be used.
`real` represents the elapsed time.
`usr` and `sys` represent the user and system time, respectively.
The suffixes `_self` and `_child` represent the part consumed in the main shell process and the other child processes including subshells and external programs, respectively.
`cpu` represents the percentage of the CPU core usage in integer, which can be calculated by `(usr+sys)*100/real`.
The other time values are all in unit of milliseconds.

### 4.15.23 Bleopt `exec_exit_mark` (ANSI Escape sequences) (v0.4)<sup><a id="bleopt-exec_exit_mark" href="#user-content-bleopt-exec_exit_mark">†</a></sup>

```bash
# default
bleopt exec_exit_mark=$'\e[94m[ble: exit]\e[m'
```

This setting specifies the marker printed when the bash session ends.
When an empty string is specified, the marker is disabled.

### 4.15.24 Bleopt `history_share` (Empty/Non-empty) (v0.4)<sup><a id="bleopt-history_share" href="#user-content-bleopt-history_share">†</a></sup>

```bash
# default
bleopt history_share=
```

When this option has a non-empty value,
the history is synchronized to `$HISTFILE` every time a command is executed.

### 4.15.25 Bleopt `info_display` (Enumerable) (v0.4)<sup><a id="bleopt-info_display" href="#user-content-bleopt-info_display">†</a></sup>

```bash
# default
bleopt info_display=top
```

This option controls the position of the info pane where completion menu, mode names, and other information are shown.
When the value `top` is specified, the info pane is shown just below the command line.
When the value `bottom` is specified, the info pane is shown at the bottom of the terminal.

### 4.15.26 Bleopt `accept_line_threshold` (Arithmetic) (v0.4)<sup><a id="bleopt-accept_line_threshold" href="#user-content-bleopt-accept_line_threshold">†</a></sup>

```bash
# default
bleopt accept_line_threshold=5
```

This option controls the behavior of widget `accept-single-line-or-newline` in the single-line mode.
If this option is evaluated to a negative integer, the command is always executed.
If this option is evaluated to `0`, the widget inserts a newline when there is unprocessed user inputs.
If this option is evaluated to a positive integer *n*,
the widget inserts a newline when there is *n* or more user inputs.

### 4.15.27 Bleopt `line_limit_type` (Enumerable) (v0.4)<sup><a id="bleopt-line_limit_type" href="#user-content-bleopt-line_limit_type">†</a></sup>

```bash
# default
bleopt line_limit_type=none
```

This option controls the behavior when the number of characters exceeds the capacity specified by `line_limit_length`.
The value `none` means that the number of characters will not be checked.
The value `discard` means that the characters cannot be inserted when the number of characters exceeds the capacity.
The value `truncate` means that the command line is truncated from its end to fit into the capacity.
The value `editor` means that the widget `edit-and-execute` will be invoked to open an editor to edit the command line contents.

### 4.15.28 Bleopt `line_limit_length` (Arithmetic) (v0.4)<sup><a id="bleopt-line_limit_length" href="#user-content-bleopt-line_limit_length">†</a></sup>

```bash
# default
bleopt line_limit_length=10000
```

This option specifies the capacity of the command line in the number of characters.
The number 0 or negative numbers means the unlimited capacity.

### 4.15.29 Bleopt `history_limit_length` (Arithmetic) (v0.4)<sup><a id="bleopt-history_limit_length" href="#user-content-bleopt-history_limit_length">†</a></sup>

```bash
# default
bleopt history_limit_length=10000
```

This option specifies the maximal number of characters which can be appended into the history.
When this option has a positive value, commands with the length longer than the value is not appended to the history.
When this option has a non-positive value, commands are always appended to the history regardless of their length.

### 4.15.30 Bleopt `history_erasedups_limit` (Empty/Arithmetic) (v0.4)<sup><a id="bleopt-history_erasedups_limit" href="#user-content-bleopt-history_erasedups_limit">†</a></sup>

```bash
# default
bleopt history_erasedups_limit=0
```

This option controls the target range in the command history for `erasedups`, which is performed when it is specified in `HISTCONTROL`.
When this option has an empty value, the target range is the entire history as in the plain Bash.
When this option evaluates to a positive integer `count`, the target range is the last `count` entries in the command history.
When this option evaluates to a non-positive integer `offset`, `offset` specifies the beginning of the target range relative to the history count at the session start.
The end of the target range is always the end of the command history.
