---
title: Python-numeric
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-52
reference: 
description: 
aliases: 
tags: 
---
# Python-numeric
Numbers

Numbers are created by numeric literals. Numeric objects are immutable, which means when an object is created its value cannot be changed.

Python has three distinct numeric types: integers, floating point numbers, and complex numbers. Integers represent negative and positive integers without fractional parts whereas floating point numbers represents negative and positive numbers with fractional parts. In addition, Booleans are a subtype of plain integers. See the following statements in Python shell.
Python integer float example

built-in numeric

Mathematically, a complex number (generally used in engineering) is a number of the form A+Bi where i is the imaginary number. Complex numbers have a real and imaginary part. Python supports complex numbers either by specifying the number in (real + imagJ) or (real + imagj) form or using a built-in method complex(x, y). See the following statements in Python Shell.

Python Complex Number

Order of operations

>>> (3+12) / 3
>>> 15 / (3 + 2)

Output:

5.0
3.0


    Numbers: An are integers (such as 1, 2, 3…), floats (such as 2.6, 4.8, etc.), fractions (such as ½. ¾, etc.), or even complex numbers.
        int (signed integer)
        float
        long
        complex



1. Python Numbers

There are four numeric Python data types.
1.1. int

int stands for integer. This Python Data Type holds signed integers. We can use the type() function to find which class it belongs to.
>>> a=-7
>>> type(a)

<class ‘int’>

An integer can be of any length, with the only limitation being the available memory.
>>> a=9999999999999999999999999999999
>>> type(a)

<class ‘int’>
1.2. float

This Python Data Type holds floating-point real values. An int can only store the number 3, but float can store 3.25 if you want.
>>> a=3.0
>>> type(a)

<class ‘float’>
1.3. long

This Python Data type holds a long integer of unlimited length. But this construct does not exist in Python 3.x.
1.4. complex

This Python Data type holds a complex number. A complex number looks like this: a+bj Here, a and b are the real parts of the number, and j is imaginary.
>>> a=2+3j
>>> type(a)

<class ‘complex’>

Use the isinstance() function to tell if Python variables belong to a particular class. It takes two parameters- the variable/value, and the class.
>>> print(isinstance(a,complex))

True

It’s time to know the detail insights of Python numbers.

Numbers
  Integers
  Floats any number with a decimal point a float. any numbers you divide becomes a float. any numbers you mix with a float becomes a float

  Underscores in Number - you can group digits using underscores to make large numbers more readable. python ignores the underscores when storing these kinds of values
      universe_age = 14_000_000

Numeric objects are immutable; once created their value never changes.



Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
Example

Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))



    None- The None keyword indicates the absence of value.



6. Writing numbers in binary, octal, and hexadecimal

More often than not, programmers need to deal with numbers other than decimal. To do this, you can use appropriate prefixes.
Number System 	Prefix
Binary 	0b or 0B
Octal 	0o or 0O
Hexadecimal 	0x or 0X
i. Binary

When you want to write a binary number, use the prefix 0b or 0B. For example, we know that the binary for 7 is 111.
>>> print(0b111)

7

You can also apply conversion functions on these numbers.
>>> int(0b10)

2
ii. Octal

The prefix for octal is 0o or 0O.
>>> print(0O10)

8

The following code causes an error. This is because the octal number system does not have the number 8. It has the numbers 0-7.
>>> print(0O8)

SyntaxError: invalid token
>>> float(0B10)

2.0
iii. Hexadecimal

The hexadecimal number system has numbers 0-9 and then A-F. For that, use the prefix 0x or 0X.
>>> print(0xFF)

255
>>> print(0xFE)

254

8. Python Decimal Module

Let’s try out adding 1.1 and 2.2 in the shell, and let’s compare it with 3.3.
>>> (1.1+2.2)==3.3

False

Why did it return False? Let’s try printing the sum.
>>> 1.1+2.2

3.3000000000000003

Woah, how did this happen? Well, this is duly attributed to hardware limitations, and is not a flaw of Python. Because the hardware stores decimals as binary fractions, it isn’t possible to store it very accurately. Let’s take an example.
>>> 1/3

0.3333333333333333

When we divide 1 by 3, it doesn’t return the full value, which is 0.3333333333333333… Python does provide a solution to this problem. It has the ‘decimal’ module, which lets us choose precision. We will learn about modules in a later lesson.
>>> import decimal
>>> print(decimal.Decimal(0.1))

0.1000000000000000055511151231257827021181583404541015625

Did you see what happened here? The Decimal() function preserved the significance.This was the Decimal Function Python number type.
9. The fractions Module

Another module that Python provides, the fractions module lets you deal with fractions. The Fraction() function returns the value in the form of numerator and denominator.
>>> from fractions import Fraction
>>> print(Fraction(1.5))

3/2

It can also take two arguments.
>>> print(Fraction(1,3))

1/3
10. The math Module

Another essential module is the math module. It has all important mathematical functions like exp, trigonometric functions, logarithmic functions, factorial, and more.
>>> import math
>>> math.factorial(5)

120
>>> math.exp(3)

20.085536923187668
>>> math.tan(90)

-1.995200412208242

This was all about the Python number types tutorial.



