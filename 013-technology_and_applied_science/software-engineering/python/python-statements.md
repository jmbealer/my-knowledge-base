---
title: What Python Statement WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# What Python Statement WIP

Instructions written in the source code for execution are  called statements.

The different types of statements in Python are: Assignment satement,
Conditional statement, Looping statements,

Python Simple Statements
1. Expression Statement
2. Assignment Statement
3. Assert Statement
4. pass Statement
5. del Statement
6. return Statement
7. yield Statement
8. raise Statement
9. break Statement
10. continue Statement
11. import Statement
12. global Statement
13. nonlocal Statement

Python Compound Statements
1. if Statement
2. for Statement
3. while Statement
4. try Statement
5. with Statement
6. Function Definition Statement
7. Class Definition Statement
8. Coroutines Function Definition Statement


a. Multiline Python Statement

In Python, every statement ends with a newline character. But like we have seen, it is possible to span a statement over multiple lines. We do this using the ‘\’ character.


b. Multiple Python Statement in One Line

You can easily put multiple statements in python on one line.
>>> a=7; print(a)

7
You can also do this to an if-statement.
>>> if 2>1: print("2")

2

d. Blank Lines Python Statements

The interpreter simply ignores blank lines.


## Python Multi-line Statements WIP

Multiple Statements on a Single Line:

You can write two separate statements into a single line using a semicolon (;) character between two line.
Python multiple statement into a single line



Python Multiline Statements

This one is an important Python syntax. We saw that Python does not mandate semicolons. A new line means a new statement. But sometimes, you may want to split a statement over two or more lines. It may be to aid readability. You can do so in the following ways.
2.1. Use a backward slash
>>> print("Hi\
how are you?")

Output:

Hihow are you?

You can also use it to distribute a statement without a string across lines.
>>> a\
=\
10
>>> print(a)

Output:

10
2.2. Put the String in Triple Quotes
>>> print("""Hi
       how are you?""")

Output:

Hi
how are you?

However, you can’t use backslashes inside a docstring for statements that aren’t a string.
>>> """b\
=\
10"""

Output:

‘b=10’
>>> print(b)

Output:

Traceback (most recent call last):
File “<pyshell#6>”, line 1, in <module>
print(b)
NameError: name ‘b’ is not defined


6. Python Multiple Statements in One Line

You can also fit in more than one statement on one line. Do this by separating them with a semicolon. But you’d only want to do so if it supplements readability.
>>> a=7;print(a);

Output:

7



