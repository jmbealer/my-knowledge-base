---
title: Python Quotations WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# Python Quotations WIP

Python supports the single quote and the double quote for string literals. But if you begin a string with a single quote, you must end it with a single quote. The same goes for double-quotes.

The following string is delimited by single quotes.
>>> print('We need a chaperone');

Output:

We need a chaperone

This string is delimited by double-quotes.
>>> print("We need a 'chaperone'");

Output:

We need a ‘chaperone’

Notice how we used single quotes around the word chaperone in the string? If we used double quotes everywhere, the string would terminate prematurely.
>>> print("We need a "chaperone"");

Output:

SyntaxError: invalid syntax

