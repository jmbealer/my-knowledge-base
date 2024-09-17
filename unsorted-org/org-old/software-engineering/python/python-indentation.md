---
title: What is Python Indentation? WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-52
reference: 
description: 
aliases: 
tags: 
---
# What is Python Indentation? WIP

Indentation refers to the spaces at the beginning of a code line.


Python uses indentation to indicate a block of code.
Example
if 5 > 2:
  print("Five is greater than two!")

Python will give you an error if you skip the indentation:
Example

Syntax Error:
if 5 > 2:
print("Five is greater than two!")

The number of spaces is up to you as a programmer, but it has to be at least one.
Example
if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")

You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
Example

Syntax Error:
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")

Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.


Indentation:

Python uses whitespace (spaces and tabs) to define program blocks whereas other languages like C, C++ use braces ({}) to indicate blocks of codes for class, functions or flow control. The number of whitespaces (spaces and tabs) in the indentation is not fixed, but all statements within the block must be the indented same amount. In the following program, the block statements have no indentation.


Indentation in Python refers to the (spaces and tabs) that are used at the beginning of a statement. The statements with the same indentation belong to the same group called a suite.

Consider the example of a correctly indented Python code statement mentioned below.

if a==1:
    print(a)
    if b==2:
        print(b)
print('end')

In the above code, the first and last line of the statement is related to the same suite because there is no indentation in front of them. So after executing first "if statement", the Python interpreter will go into the next statement. If the condition is not true, it will execute the last line of the statement.

By default, Python uses four spaces for indentation, and the programmer can manage it.

At the next level, the following statements are typed with four spaces(a tab) in front of them, and so they are in the same suite.

    print(a)
    if b==2:

The third statement: "if b==2" will be executed if the first statement: "if a==1" is true.

In the next statement, eight spaces (two tabs) have been typed in front of "print (b)", and hence it is in a separate suite, and it will execute only if the statement "if b==2" is true.

        print(b)


5. Python Indentation

Since Python doesn’t use curly braces to delimit blocks of code, this Python Syntax is mandatory. You can indent code under a function, loop, or class.
>>> if 2>1:
      print("2 is the bigger person");
      print("But 1 is worthy too");

Output:

2 is the bigger person
But 1 is worthy too

You can indent using a number of tabs or spaces, or a combination of those. But remember, indent statements under one block of code with the same amount of tabs and spaces.
>>> if 2>1:
     print("2 is the bigger person");
   print("But 1 is worthy too");

Output:

SyntaxError: unindent does not match any outer indentation level

3. Python Indentation

Unlike C++ or Java, Python does not use curly braces for indentation. Instead, Python mandates indentation. At this point, our inner monsters are laughing at the lazy programmers around us.
>>> if 2>1:
                print("2")

2
There are no strict rules on what kind of Python indentation you use. But it must be consistent throughout the block. Although, four whitespaces are usually preferred, and tabs are discouraged. Let’s take an example with an inconsistent indentation in python.
>>> if 2>1:
                print("1")
                 print("2")

SyntaxError: unexpected indent


Leading whitespace (spaces and tabs) at the beginning of a logical line is used to compute the indentation level of the line, which in turn is used to determine the grouping of statements.

Tabs are replaced (from left to right) by one to eight spaces such that the total number of characters up to and including the replacement is a multiple of eight (this is intended to be the same rule as used by Unix). The total number of spaces preceding the first non-blank character then determines the line’s indentation. Indentation cannot be split over multiple physical lines using backslashes; the whitespace up to the first backslash determines the indentation.

Indentation is rejected as inconsistent if a source file mixes tabs and spaces in a way that makes the meaning dependent on the worth of a tab in spaces; a TabError is raised in that case.

Cross-platform compatibility note: because of the nature of text editors on non-UNIX platforms, it is unwise to use a mixture of spaces and tabs for the indentation in a single source file. It should also be noted that different platforms may explicitly limit the maximum indentation level.

A formfeed character may be present at the start of the line; it will be ignored for the indentation calculations above. Formfeed characters occurring elsewhere in the leading whitespace have an undefined effect (for instance, they may reset the space count to zero).

The indentation levels of consecutive lines are used to generate INDENT and DEDENT tokens, using a stack, as follows.

Before the first line of the file is read, a single zero is pushed on the stack; this will never be popped off again. The numbers pushed on the stack will always be strictly increasing from bottom to top. At the beginning of each logical line, the line’s indentation level is compared to the top of the stack. If it is equal, nothing happens. If it is larger, it is pushed on the stack, and one INDENT token is generated. If it is smaller, it must be one of the numbers occurring on the stack; all numbers on the stack that are larger are popped off, and for each number popped off a DEDENT token is generated. At the end of the file, a DEDENT token is generated for each number remaining on the stack that is larger than zero.

      Indentation
          usually 4 spaces
          must keep same throught code block


Indentation - Python uses whitespace (spaces and tabs) to indicate a block of code
  if 5 > 2:
      print("Five is greater than two!") # correct indentation
  if 5 > 2:
  print("Five is greater than two!") # incorrect indentation



** Python Indentations
*** Python uses indentation to indicate a block of code.

** Python relies on indentation, using whitespaces, to define scope;
*** such as the scope of loops, functions and classes.
      Continuance
          \ ex: long_name= \
              "something"+ \ "something else"

Blocks can be nested to arbitrary depth. Each indent defines a new block, and each outdent ends the preceding block.

