---
title: Python Cheat-Sheet
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-53
reference: 
description: 
aliases: 
tags: 
---
# Python Cheat-Sheet

\# Single-Line Comment

== Primitive Data-types and Operators
3 => int integer
1.2 => float floating point number
1+2j => complex

(1 + 1) * 3 => enforce precedence with parentheses
1 ** 1 => exponentiation/exponent, x**y, x to the power of y
1 % 1 => modulo/modulus/remainder
1 // 1 => floor division, integer division rounds down
1 / 1 => division, always return as float
1 * 1 => multiplication
1 - 1 => subtraction
1 + 1 => addition

True => True
False => False
not True => False
not False => True
True and False => False
False or True => True
True + True => 2, True is 1 with different keyword
True * 8 => 8
False - 5 => -5, False is 0 with different keyword
0 == False => True
1 == True => True
2 == True => False
-5 != False => True
1 == 1 => True, equal to, equality is ==
2 == 1 => False
1 != 1 => False, not equal to, inequality is !=
2 != 1 => True
1 < 10 => True, less than
1 > 10 => False, greater than
1 <= 10 => True, less than or equal to
1 >= 10 => False, greater than or equal to

'aaa' => str/strings
'a' + 'b' => 'ab', string concatenation
'a' * 3 => 'aaa', string replication

\# This is a comment
""" Doc-string
can be used as multi-line string"""

Subset Lists of Lists
my_list[list]/[itemOfList]

Numpy Arrays np.array(my_list)
