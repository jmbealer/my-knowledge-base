---
title: "-*- Coding: Encoding -*-"
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-52
reference: 
description: 
aliases: 
tags: 
---
== Python Interpreter WIP
 Python Interpreter & its Environment (Source Code Encoding)

The default encoding for a Python source file is UTF-8. This is a Unicode Standard variable-width character encoding; it can encode 1,112,064 valid code points in Unicode using up to four 8-bit bytes. Using this encoding, we can use characters of most languages – we can use these in string literals, comments, and identifiers. Since the standard library makes use of ASCII characters only, you must declare the use of this encoding to your editor. This is to ensure that all such characters display without a problem. The font should be such that supports all characters in the file.
We add this comment as the first line of the file we want to use it in-
# -*- Coding: Encoding -*-

In this, encoding is a valid codec that Python supports. Similarly, when you want to use the Windows-1252 encoding, you can use this as the first line of code:
# -*- Coding: Cp1252 -*-

However, when you want to begin code with a UNIX shebang line, you can put the comment for encoding second-
#!/usr/bin/env python3
# -*- Coding: Cp1252 -*-

Do you know about Python Iterables and Python Itertools
3. How to Invoke the Python Interpreter?

On your machine, you can find your interpreter at an address like:
C:\Python36
Or it may reside on the location you selected at the time of installation. Add path using this command:
set path=%path%;C:\python36
Python Interpreter

How to Invoke the Python Interpreter?
a. Start the Python Interpreter

On Windows, when you want to run the Python interpreter in the shell, you can type the following:
$python

To get out of the interpreter in disassembling the Bytecode shell, you can type:
>>> quit()

Bye
Let’s Discuss Python Multiple Inheritance – Python MRO (Method Resolution Order)
Alternately, you can use an end-of-file character at the prompt. Python interpreter exits with a zero exit status. You can use it in a REPL (Read-Evaluate-Print-Loop) fashion. But if you want, you can save your Python code as a script and execute it using the interpreter:
$python demo.py

To enter interactive mode after running a script, you can pass –i before the script.
The command python -c command [arg] … executes statements in command, and python -m module [arg] … executes the source file for module.
b. Features of Python Interpreter

Python interpreter offers some pretty cool features:

    Interactive editing
    History substitution
    Code completion on systems with support for readline

In the first Python prompt, try pressing the following keys:
Ctrl+P
This tells you if your interpreter supports command-line editing. A beep indicates that it does support command-line editing. Otherwise, it will either perform a no-operation or echo ^p to indicate it isn’t available.
c. Passing Arguments

When you pass a script name and additional arguments to the shell when invoking the Python interpreter, it turns these into a list of strings. Then, it assigns these to the variable argv in the sys module. The following command will give us a list of this-
import sys

Without a script or arguments, sys.argv[0] denotes an empty string. A script name of ‘-‘ means that it sets sys.argv[0] to ‘-‘, and with ‘-c’, it is set to ‘-c’. A value of ’-m’ sets sys.argv[0] to the module’s full name. The command/ module handles the options after ‘-c’ or ‘-m’.
Do you know about Python Collections Module?
d. Interactive Mode

Python interpreter is in an interactive mode when it reads commands from a tty. The primary prompt is the following:
>>>

When it shows this prompt, it means it prompts the developer for the next command. This is the REPL. Before it prints the first prompt, Python interpreter prints a welcome message that also states its version number and a copyright notice.
This is the secondary prompt:
…

This prompt denotes continuation lines.
$ python3.7
Python 3.7 (default, Jul 16 2018, 04:38:07)
[GCC 4.8.2] on Windows
Type "help", "copyright", "credits" or "license" for more information.
>>>

You will find continuation lines when working with a multi-line construct:
>>> it_rains =True
>>> if it_rains:
    print("The produce will be good")

The produce will be good
You can also use the Python  interpreter as a calculator:
>>> 2*7
14
>>> 4/2
2.0

For more on numbers and strings with the interpreter, check out Python Numbers and Python Strings.
4. How Does Python Interpreter Works?

Well, internally, four things happen in a REPL:
i. Lexing- The lexer breaks the line of code into tokens.
ii. Parsing- The parser uses these tokens to generate a structure, here, an Abstract Syntax Tree, to depict the relationship between these tokens.
iii. Compiling- The compiler turns this AST into code object(s).
iv. Interpreting- The interpreter executes each code object.
Have a look at Python Operators with Syntax and Examples
How Does Python Interpreter Works?

How Does Python Interpreter Works?
a. Function Objects & Code Objects

When we talk of function objects, we mean to say that in Python, functions are first-class objects (functions indeed are objects). You can pass them around and talk about them without making a call to them.
>>> def bar(a):
  x=3
  return x+a
>>> bar

<function bar at 0x107ef7aa2>

Now bar.__code__ returns a code object:
>>> bar.__code__
<code object bar at 0x107eeccb2, file "<stdin>", line 1>

So, we conclude that a code object is an attribute of a function object. The dir() function will tell us more about the function:
>>> dir(bar.__code__)

[‘__class__’, ‘__cmp__’, ‘__delattr__’, ‘__doc__’, ‘__eq__’, ‘__format__’, ‘__ge__’,
‘__getattribute__’, ‘__gt__’, ‘__hash__’, ‘__init__’, ‘__le__’, ‘__lt__’, ‘__ne__’, ‘__new__’,
‘__reduce__’, ‘__reduce_ex__’, ‘__repr__’, ‘__setattr__’, ‘__sizeof__’, ‘__str__’,
‘__subclasshook__’, ‘co_argcount’, ‘co_cellvars’, ‘co_code’, ‘co_consts’, ‘co_filename’,
‘co_firstlineno’, ‘co_flags’, ‘co_freevars’, ‘co_lnotab’, ‘co_name’, ‘co_names’, ‘co_nlocals’,
‘co_stacksize’, ‘co_varnames’]
Let’s revise Recursion in Python with Examples
This gives us the attributes of the code object. Values of some more attributes:
>>> bar.__code__.co_varnames

(‘a’, ’x’)
>>> bar.__code__.co_consts

(None, 3)
>>> bar.__code__.co_argcount

1
b. The Bytecode

The following command gives us the bytecode:
>>> bar.__code__.co_code

‘d\x01\x00}\x01\x00|\x01\x00|\x00\x00\x17S’

This is a series of bytes, each of which the interpreter loops through and then makes an execution.
c. Disassembling the Bytecode

We will use the dis() method from the dis module to understand what’s going on- this isn’t part of what the interpreter does.
>>>import dis
>>> dis.dis(bar.__code__)

2             0 LOAD_CONST 1 (3)
               3 STORE_FAST 1 (x)
3             6 LOAD_FAST 1 (x)
               9 LOAD_FAST 0 (a)
               12BINARY_ADD
               13RETURN_VALUE
In this, the first set of numbers is the line numbers in the actual code. The second one depicts offsets of the bytecode. Then comes the set of names for the bytes- for human readability. The next column depicts the arguments and the last column lists the constants and names in the fourth column.
>>> bar.__code__.co_consts[1]

3
>>> bar.__code__.co_varnames[1]

‘x’




