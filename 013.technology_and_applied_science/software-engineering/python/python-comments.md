---
title: What Are Python Comments (#) WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# What Are Python Comments (#) WIP

Python Comments begins with an octothorpe (hash, pound) character (#).
Python Comments can't be part of a string literal.
Comments extend to the end-of-the physical line.
Python Comments signifies the end of the logical line unless the implicit line joining rules are invoked.

Python Comments can be use to explain or test code
Python comments may appear at the start of a line or following whitespace or code, but not within a string literal.
Comments are ignored by the syntax.
A hash character (#) within a string literal is just a hash character (#).
Python Comments are non-executable statements.

.Examples:
`# Single-Line Comment`
print(test) # Single-Line Comment after code
`# print(Comment that prevent code execute)`

.Multi-Line Comments
Python does not support multi-line comments.

### Docstrings ("""""") ('''''')

A docstring is a documentation string.
Delimit a docstring using three double-quotes ("""""") or single-quotes ('''''').

Python also has extended documentation capability, called docstrings.

Docstrings can be one line, or multiline. Docstrings are also comments:

Python uses triple quotes at the beginning and end of the docstring:


Or, not quite as intended, you can use a multiline string.
Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

.Example
"""
This
is a
docstring (multi-line comment)
"""
As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have made a multiline comment.



Multi-line comment is useful when we need to comment on many lines. You can also use a single-line comment, but using a multi-line instead of single-line comment is easy to comment on multiple lines.

In Python Triple double quote (""") and single quote (''') are used for Multi-line commenting. It is used at the beginning and end of the block to comment on the entire block. Hence it is also called block comments.

4. Python Docstrings

As a comment, this Python Syntax is used to explain code. But unlike comments, they are more specific. Also, they are retained at runtime. This way, the programmer can inspect them at runtime.
>>> """This comment
is spanned across
multiple lines"""

‘This comment\nis spanned across\nmultiple lines’
This gives us an output because we type it in the shell. When you create a file and write this in that, there is no output. While triple quotes are generally used for multiline python comment, we can conveniently use them for python comment as well.
Triple quotes will also preserve formatting.
>>> print("""Hello
Hi""")

b. Docstrings Python Comment

A docstring is a documentation string in Python. It is the first statement in a module, function, class, or method in Python. In this, we explain what a python function/class does.

To check a function’s docstring, use its __doc__ attribute.

‘\n\tThis function prints Hi\n\t’
The interpreter is unable to get the docstring to a function if it isn’t the first thing in the python function.

b. Docstrings Python Comment

A docstring is a documentation string in Python. It is the first statement in a module, function, class, or method in Python. In this, we explain what a python function/class does.
>>> def sayhi():
  """
  This function prints Hi
  """
  print("Hi")
>>> sayhi()

Hi
To check a function’s docstring, use its __doc__ attribute.
>>> def sayhi():
  """
  This function prints Hi
  """
  print("Hi")
>>> sayhi.__doc__

‘\n\tThis function prints Hi\n\t’
The interpreter is unable to get the docstring to a function if it isn’t the first thing in the python function.
>>> def sayhi():
  print("Hi")
  """
  This function prints Hi
  """
>>> sayhi.__doc__
>>>


