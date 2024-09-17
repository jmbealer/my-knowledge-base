---
title: Python-casting
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-53
reference: 
description: 
aliases: 
tags: 
---
# Python-casting
== Casting

## Type Conversion (Casting) WIP

Specify a Variable Type
Casting is when you want to specify a type on to a variable.
Casting in python is done using constructor functions:
  - int() - constructs an integer number from an integer literal, a float literal
  (by rounding down to the previous whole number), or a string literal
  (providing the string represents a whole number).
  - float() - constructs a float number from an integer literal, a float literal
  or a string literal (providing the string represents a float or an integer).
  - str() - constructs a string from a wide variety of data types, including
    strings, integer literals and float literals.
  Integers:
    x = int(1)   # x will be 1
    y = int(2.8) # y will be 2
    z = int("3") # z will be 3
  Floats:
    x = float(1)     # x will be 1.0
    y = float(2.8)   # y will be 2.8
    z = float("3")   # z will be 3.0
    w = float("4.2") # w will be 4.2
  Strings:
    x = str("s1") # x will be 's1'
    y = str(2)    # y will be '2'
    z = str(3.0)  # z will be '3.0'


Conversion

>>> float("4.5")
>>> int("25")
>>> int(5.625)
>>> float(6)
>>> int(True)
>>> float(False)
>>> str(True)
>>> bool(0)
>>> bool('Hello world')
>>> bool(223.5)

Output:

4.5
25
5
6.0
1
0.0
'True'
False
True
True


Type Conversion

Since Python is dynamically-typed, you may want to convert a value into another type. Python supports a list of functions for the same.
1. int()

It converts the value into an int.
>>> int(3.7)

3
Notice how it truncated 0.7 instead of rounding the number off to 4. You can also turn a Boolean into an int.
>>> int(True)

1
>>> int(False)

However, you cannot turn a string into an int. It throws an error.
>>> int("a")

Traceback (most recent call last):
File “<pyshell#135>”, line 1, in <module>;
int(“a”)
ValueError: invalid literal for int() with base 10: ‘a’

However, if the string has only numbers, then you can.
>>> int("77")

77
2. float()

It converts the value into a float.
>>> float(7)

7.0
>>> float(7.7)

7.7
>>> float(True)

1.0
>>> float("11")

You can also use ‘e’ to denote an exponential number.

11.0
>>> float("2.1e-2")

0.021
>>> float(2.1e-2)

0.021

However, this number works even without the float() function.
>>> 2.1e-2

0.021
3. str()

It converts the value into a string.
>>> str(2.1)

‘2.1’
>>> str(7)

‘7’
>>> str(True)

‘True’

You can also convert a list, a tuple, a set, or a dictionary into a string.
>>> str([1,2,3])

‘[1, 2, 3]’
4. bool()

It converts the value into a boolean.
>>> bool(3)

True
>>> bool(0)

False
>>> bool(True)

True
>>> bool(0.1)

True

You can convert a list into a Boolean.
>>> bool([1,2])

True

The function returns False for empty constructs.
>>> bool()

False
>>> bool([])

False
>>> bool({})

False

None is a keyword in Python that represents an absence of value.
>>> bool(None)

False
5. set()

It converts the value into a set.
>>> set([1,2,2,3])

{1, 2, 3}
>>> set({1,2,2,3})
<!--ID: 1639528996177-->


{1, 2, 3}

Explore Pythons sets and booleans with syntax and examples.
6. list()

It converts the value into a list.
>>> del list
>>> list("123")

[‘1’, ‘2’, ‘3’]
>>> list({1,2,2,3})
<!--ID: 1639528996200-->


[1, 2, 3]
>>> list({"a":1,"b":2})
<!--ID: 1639528996222-->


[‘a’, ‘b’]

However, the following raises an error.
>>> list({a:1,b:2})
<!--ID: 1639528996244-->


Traceback (most recent call last):
File “<pyshell#173>”, line 1, in <module>;
list({a:1,b:2})
TypeError: unhashable type: ‘set’
7. tuple()
<!--ID: 1639528996265-->


It converts the value into a tuple.
>>> tuple({1,2,2,3})
<!--ID: 1639528996288-->


(1, 2, 3)

You can try your own combinations. Also try composite functions.
>>> tuple(list(set([1,2])))

(1, 2)


Specify a Variable Type

There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

    int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

Example

Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
Example

Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
Example

Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:
Example 	Data Type 	Try it
x = str("Hello World") 	str
x = int(20) 	int
x = float(20.5) 	float
x = complex(1j) 	complex
x = list(("apple", "banana", "cherry")) 	list
x = tuple(("apple", "banana", "cherry")) 	tuple
x = range(6) 	range
x = dict(name="John", age=36) 	dict
x = set(("apple", "banana", "cherry")) 	set
x = frozenset(("apple", "banana", "cherry")) 	frozenset
x = bool(5) 	bool
x = bytes(5) 	bytes
x = bytearray(5) 	bytearray
x = memoryview(bytes(5)) 	memoryview

Python has the capability and feature to convert within an expression containing the mixture of different types of values internally.

int(v): is used to convert any value 'v' to a plain integer
long(v): is used to convert a value 'v' to a long integer
float(v): is used to convert a value 'v' to floating-point value
complex(v): is used convert a value 'v' to the complex number having real part 'v' and imaginary part as 0
complex(u,v): is used convert values u and v to the complex number with real part 'u' and imaginary part 'v'

x = 10.5
y = 5

`#without type cast`
print (x + y)

`#after type cast`
print (int(x) + y)

15.5
15

The above example shows how float converted to an integer.


7. Python Conversion Functions

Although most times Python does the conversion as needed, you can do it explicitly if you want. These functions allow us to convert one numeric type into another python number types.
Python Number Types - Python Int, Float, Complete Numbers

Python Number Types – Python Conversion Functions
i. int()

The int() function can convert another numeric type into an int. It can also convert other types into an int, but in this tutorial, we focus on numeric types.
>>> int(7)

7
>>> int(7.7)

7

As you can see, it does not round the number 7.7 up to 8; it truncates the 0.7.

However, you cannot convert a complex number into an int.
>>> int(2+3j)

Traceback (most recent call last):

File “<pyshell#22>”, line 1, in <module>

int(2+3j)

TypeError: can’t convert complex to int
>>> int(3j)

Traceback (most recent call last):

File “<pyshell#23>”, line 1, in <module>

int(3j)

TypeError: can’t convert complex to int

We can also apply this function on representations other than decimal, i.e., binary, octal, and hexadecimal.
>>> int(0b10)

2
>>> int(0xF)

15
ii. float()

This function converts another numeric type into a float.
>>> float(110)

110.0
>>> float(110.0)

110.0

Like int(), float() can’t convert a complex either.
>>> float(3j)

Traceback (most recent call last):

File “<pyshell#26>”, line 1, in <module>

float(3j)

TypeError: can’t convert complex to float
>>> float(0o10)

8.0

Here, we applied it to an octal number.
iii. complex()

The complex() function converts another numeric type into a complex number.
>>> complex(2)

(2+0j)
>>> complex(2.3)

(2.3+0j)
>>> complex(2+3.0j)

(2+3j)
iv. bin()

The bin() function returns the binary value of a number.
>>> bin(2)

‘0b10’

However, you can’t apply it to a float value or a complex value. The same is true for oct() and hex() functions too.
>>> bin(2.3)

Traceback (most recent call last):

File “<pyshell#49>”, line 1, in <module>

bin(2.3)

TypeError: ‘float’ object cannot be interpreted as an integer
>>> bin(2+3j)

Traceback (most recent call last):

File “<pyshell#50>”, line 1, in <module>

bin(2+3j)

TypeError: ‘complex’ object cannot be interpreted as an integer
v. oct()

This function returns the octal value of a number.
>>> oct(8)

‘0o10’

We know that 8.0 is the same as 8, but the function doesn’t think the same. It is a float, so it cannot convert it into an oct.
>>> oct(8.0)

Traceback (most recent call last):

File “<pyshell#59>”, line 1, in <module>

oct(8.0)

TypeError: ‘float’ object cannot be interpreted as an integer
vi. hex()

The hex() function returns the hexadecimal value of a number.
>>> hex(255)

‘0xff’
>>> hex(0)

‘0x0’
>>> hex(0)

‘0x0’
