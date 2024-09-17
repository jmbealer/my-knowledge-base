---
title: Python Built-in Functions
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-53
reference: 
description: 
aliases: 
tags: 
---
# Python Built-in Functions

function(parameter)



abs() Returns the absolute value of a number
	abs(n) (n) parameter value required. A number
	x = abs(-3.25)
all() Returns True if all items in an iterable object are true
any() Returns True if any item in an iterable object is true
ascii() Returns a readable version of an object. Replaces none-ascii characters with escape character

bin() Returns the binary version of a number
bool() Returns the boolean value of the specified object
bytearray() Returns an array of bytes
bytes() Returns a bytes object
callable() Returns True if the specified object is callable, otherwise False
chr() Returns a character from the specified Unicode code.
classmethod() Converts a method into a class method
compile() Returns the specified source as an object, ready to be executed
complex() Returns a complex number
delattr() Deletes the specified attribute (property or method) from the specified object
dict() Returns a dictionary (Array)
dir() Returns a list of the specified object's properties and methods
divmod() Returns the quotient and the remainder when argument1 is divided by argument2
enumerate() Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval() Evaluates and executes an expression
exec() Executes the specified code (or object)
filter() Use a filter function to exclude items in an iterable object
float() Returns a floating point number
format() Formats a specified value
frozenset() Returns a frozenset object
getattr() Returns the value of the specified attribute (property or method)
globals() Returns the current global symbol table as a dictionary
hasattr() Returns True if the specified object has the specified attribute (property/method)
hash() Returns the hash value of a specified object
help() Executes the built-in help system
hex() Converts a number into a hexadecimal value
id() Returns the id of an object
input() Allowing user input
int() Returns an integer number
isinstance() Returns True if a specified object is an instance of a specified object
issubclass() Returns True if a specified class is a subclass of a specified object
iter() Returns an iterator object
len() Returns the length of an object
list() Returns a list
locals() Returns an updated dictionary of the current local symbol table
map() Returns the specified iterator with the specified function applied to each item
max() Returns the largest item in an iterable
memoryview() Returns a memory view object
min() Returns the smallest item in an iterable
next() Returns the next item in an iterable
object() Returns a new object
oct() Converts a number into an octal
open() Opens a file and returns a file object
ord() Convert an integer representing the Unicode of the specified character
pow() Returns the value of x to the power of y

print() Prints to the standard output device
	print(object(s), sep='separator', end='end', file=file, )

property() Gets, sets, deletes a property
range() Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr() Returns a readable version of an object
reversed() Returns a reversed iterator
round() Rounds a numbers
set() Returns a new set object
setattr() Sets an attribute (property/method) of an object
slice() Returns a slice object
sorted() Returns a sorted list
@staticmethod() Converts a method into a static method
str() Returns a string object
sum() Sums the items of an iterator
super() Returns an object that represents the parent class
tuple() Returns a tuple
type() Returns the type of an object
vars() Returns the __dict__ property of an object
zip() Returns an iterator, from two or more iterators
