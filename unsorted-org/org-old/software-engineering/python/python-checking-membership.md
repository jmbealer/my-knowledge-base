---
title: Python-checking-membership
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-03
reference: 
description: 
aliases: 
tags: 
---
# Python-checking-membership
== Checking Membership in Python WIP

In Python, we can check whether a string or character is a member of another string or not using "in" or "not in" operators.

These two membership operators are described in the table below:
Symbol	Operator Name	Description
in	in	The result of this operation becomes True if it finds a value in a specified sequence and False otherwise.
not in	not in	The result of this operation becomes True if it doesn't find a value in a specified sequence and False otherwise.

While comparing the string, these operators consider uppercase and lowercase letters or strings separately and make case sensitive comparisons.

str1 = input('Please enter first string: ')
str2 = input('Please enter second string: ')
if str2 in str1:
    print(str2+' found in the first string.')
else:
    print(str2+' not found in the first string.')

Please enter first string: We are writing core python
Please enter second string: python
python found in the first string.

The above program takes two inputs from the keyboard and checks whether the second string found in the first string or not.


