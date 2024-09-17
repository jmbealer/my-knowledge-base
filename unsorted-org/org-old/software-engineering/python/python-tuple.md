---
title: Tuples WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-51
reference: 
description: 
aliases: 
tags: 
---
# Tuples WIP

Tuples are immutable ordered collection of arbitrary objects(elements).

Tuples can contain any arbitrary objects(element).
A tuple without any elements(objects) is a empty tuple: <tuple>= ()
Tuples are ordered and unchangeable.
Tuples allow duplicate elements(objects).
Tuples are zero-indexed.

Tuples are immutable arrays(sequences); You can’t change its content once created
Tuples are elements(objects) separated by commas and enclosed by parentheses: <tuple>= (<element>,<element>)
Tuples can nested to arbitrary depth.
Tuples can hold mix data types.

Difference between Tuples and Lists:
Tuples are Immutable and Lists are Mutable
Tuple enclosed in parentheses and Lists are enclosed in square brackets
rest is the same

Tuple elements(objects) can't be added or removed dynamically
All elements(objects) in a tuple must be defined at creation time.
tuples can hold elements(objects) of arbitrary data types.
During program execution manipulating a tuple is faster than the equivalent list
  this is probably not going to be noticeable when the list or tuple is small.

If elements(objects) in collection meant to remain constant for the life of the program; use a tuple
Using a tuple instead of a list guards against accidental modification
Tuples are typically used to store collection of heterogeneous data.
Tuples are used for cases where an immutable sequence of homogeneous data is needed
(such as allowing storage in a set or dict instance)
Tuples can be used in set or dict


Tuple is a collection which is ordered and unchangeable.

## Creating Tuples
Python create tuples

To create an empty tuple or create a tuple with single element use the following commands.
Python empty tuple

4. Python Tuples

A tuple is like a list. You declare it using parentheses instead.
>>> subjects=('Physics','Chemistry','Maths')
>>> subjects

(‘Physics’, ‘Chemistry’, ‘Maths’)

To declare a tuple, we use parentheses.
>>> colors=('Red','Green','Blue')

d. Accessing, Reassigning, and Deleting Items

We can perform these operations on a tuple just like we can on a list. The only differences that exist are because a tuple is immutable, so you can’t mess with a single item or a slice.
>>> del a[0]

Traceback (most recent call last):

File “<pyshell#251>”, line 1, in <module>

del a[0]

TypeError: ‘tuple’ object doesn’t support item deletion

Even though this tuple has only one item, we couldn’t delete it because we used its index to delete.

For information about functions and methods on a tuple, refer to our article on Python Tuples.

c. Creating a tuple with a single item

Let’s do this once again. Create a tuple and assign a 1 to it.
>>> a=(1)

Now, let’s call the type() function on it.
>>> type(a)

<class ‘int’>

As you can see, this declared an integer, not a tuple.

To get around this, you need to append a comma to the end of the first item 1. This tells the interpreter that it’s a tuple.
>>> a=(1,)
>>> type(a)

<class ‘tuple’>

Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

An example showing how to build tuples in Python:

tupl1 = ('computersc', 'IT', 'CSE');
tup2 = (6,5,4,3,2,1);



## Index
Elements of a tuple are indexed like other sequences. The tuple indices start at 0. See the following statements.
python tuple indexing

Tuples are immutable which means it's items values are unchangeable. See the following statements.
Python tuples are immutable

## Slice
Slicing a tuple

Like other sequences like strings, tuples can be sliced. Slicing a tuple creates a new tuple but it does not change the original tuple.
Slice a Python tuples

4.1. Accessing and Slicing a Tuple

You access a tuple the same way as you’d access a list. The same goes for slicing it.
>>> subjects[1]

‘Chemistry’
>>> subjects[0:2]

(‘Physics’, ‘Chemistry’)





Using + and * operators in Tuples

Use + operator to create a new tuple that is a concatenation of tuples and use * operator to repeat a tuple. See the following statements.
python tuples with the operator



4.2. A tuple is Immutable

However, Python tuple is immutable. Once declared, you can’t change its size or elements.
>>> subjects[2]='Biology'

Traceback (most recent call last):
File “<pyshell#107>”, line 1, in <module>
subjects[2]=’Biology’
TypeError: ‘tuple’ object does not support item assignment
>>> subjects[3]='Computer Science'

Traceback (most recent call last):
File “<pyshell#108>”, line 1, in <module>
subjects[3]=’Computer Science’
TypeError: ‘tuple’ object does not support item assignment



    Sequences:
        Strings: Sequence of Unicode characters, like an HTML document.
        Bytes/Byte array: Any type of file.
        Lists: An ordered sequence of values.
        Tuples: An ordered, immutable sequence of values.



a. Python Tuple Packing

Python Tuple packing is the term for packing a sequence of values into a tuple without using parentheses.
>>> mytuple=1,2,3,       \#Or it could have been mytuple=1,2,3
>>> mytuple

(1, 2, 3)
b. Python Tuple Unpacking

The opposite of tuple packing, unpacking allots the values from a tuple into a sequence of variables.
>>> a,b,c=mytuple
>>> print(a,b,c)

1 2 3

## Python Tuples WIP
Access Tuple Items

You can access tuple items by referring to the index number, inside square brackets:
Example

Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
Negative Indexing

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
Example

Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
Range of Indexes

You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.
Example

Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

Note: The search will start at index 2 (included) and end at index 5 (not included).

Remember that the first item has index 0.
Range of Negative Indexes

Specify negative indexes if you want to start the search from the end of the tuple:
Example

This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
Change Tuple Values

Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
Example

Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
Loop Through a Tuple

You can loop through the tuple items by using a for loop.
Example

Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

You will learn more about for loops in our Python For Loops Chapter.
Check if Item Exists

To determine if a specified item is present in a tuple use the in keyword:
Example

Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
Tuple Length

To determine how many items a tuple has, use the len() method:
Example

Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
Add Items

Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
Example

You cannot add items to a tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" \# This will raise an error
print(thistuple)
Create Tuple With One Item

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
Example

One item tuple, remember the commma:
thistuple = ("apple",)
print(type(thistuple))

\#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
Remove Items

Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
Example

The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) \#this will raise an error because the tuple no longer exists
Join Two Tuples

To join two or more tuples you can use the + operator:
Example

Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
The tuple() Constructor

It is also possible to use the tuple() constructor to make a tuple.
Example

Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) \# note the double round-brackets
print(thistuple)
Tuple Methods

Python has two built-in methods that you can use on tuples.
Method 	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found

Table of Contents
1. Accessing Values In Tuples
2. Updating Tuples
3. Delete Elements From Tuples

Programs to show how to access values in Tuples:

tupl1 = ('computersc', 'IT', 'CSE');
tupl2 = (1993, 2016);
tupl3 = (2, 4, 6, 8, 10, 12, 14, 16);

print ("tupl1[0]", tupl1[0])
print ("tupl3[2:4]", tupl3[2:4])

tupl1[0] computersc
tupl3[2:4] (6, 8)

They are immutable, i.e., the values can't be changed directly. So we can just update by joining tuples. Let's demonstrate this with an example:

tupl1 = (2, 3, 4);
tupl2 = ('ab', 'cd');
tupl3 = tupl1 + tupl2

print (tupl3)

This code snippet will execute a combination of two tuples using the "+" operator.

(2, 3, 4, 'ab', 'cd')

To delete a tuple, we can use the del-statement.

del tuple_name;

tupl3 = (2, 4, 6, 8, 10, 12, 14, 16);

del tupl3;


x = ("apple", "banana", "cherry") 	tuple

  #python #datatypes #tuples
