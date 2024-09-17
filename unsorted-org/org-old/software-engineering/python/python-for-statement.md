---
title: Print the Numbers 0, 1, 2
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
= for Statements

<g_var>=<value>;
for <var> in <iterable>:
    <statement(s)>;
    break # terminate the loop
    <statement(s)>;
    continue # restart the loop
    <statement(s)>;
    else: # execute when the loop is exhausted.
    <statement(s)>;
<following statement(s)>
<iterable>: is a collection of objects; like list or tuple.
<statement(s)>: are executed once for each item in <iterable>.
<var>: takes on the value of the next element in <iterable> each time through the loop.
<var>: assigning temporary value to a variable on each successive iteration.

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)
Calls iter() to obtain an iterator for <a> # itr = iter(a)
Calls next() repeatedly to obtain each item from the iterator in turn. # next(itr)
Terminates the loop when next() raises the StopIteration exception. # next(itr) return StopIteration exception
loop body is executed once for each item next() returns
loop <i> set to the given item for each iteration

iterable: means an object can be used in iteration.
iterable(adjective): an object may be described as iterable.
iterable(noun): an object may be characterized as an iterable.
iter(): built-in function returns if object is iterable.
iterable data types: string, list, tuple, dict, set, and frozenset types.
iterator: a value producer that yields successive values form its associated iterable object

next(): built-in function used to obtain the next value from in iterator
a = ['foo', 'bar', 'baz']
b = iter(a)
next(b)

iterable an object that can be iterated over
iterator the object that produces successive items or values from its associated iterable
iter() used to obtain an iterator from an iterable

Many built-in and library objects are iterable.
itertools contains many function that returns iterables.

for statement(s): Python only implements collection-based iteration.
for statement(s): are called for loops
for statement(s): are more like an iterator method
for statement(s): execute a set of statements; once for each item in a sequence
for statement(s): doesn't require an indexing variable to set beforehand.


loop over a string
for x in "string":
  print(x)

Per-tested loops: is also known as for loops
for statement(s): best used for loops when the number of iterations is known in advance.
for statement(s): execute some part of code until the given condition is satisfied.

== Nested Loops

A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop":
Example

Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

variable_name 	It indicates target variable which will set a new value for each iteration of the loop.
sequence 	A sequence of values that will be assigned to the target variable variable_name. Values are provided using a list or a string or from the built-in function range().


In the above example color_list is a sequence contains a list of various color names. When the for loop executed the first item (i.e. Red) is assigned to the variable c. After this, the print statement will execute and the process will continue until we reach the end of the list.

Python for loop: Iterating over tuple, list, dictionary

Example: Iterating over tuple

The following example counts the number of even and odd numbers from a series of numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if x % 2:
    	     count_odd+=1
        else:
    	     count_even+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

Output:

Number of even numbers:4
Number of odd numbers: 5

In the above example a tuple named numbers is declared which holds the integers 1 to 9.

The best way to check if a given number is even or odd is to use the modulus operator (%).
The operator returns the remainder when dividing two numbers.
Modulus of 8 % 2 returns 0 as 8 is divided by 2, therefore 8 is even and modulus of 5 % 2 returns 1 therefore 5 is odd.

The for loop iterates through the tuple and we test modulus of x % 2 is true or not, for every item in the tuple and the process will continue until we rich the end of the tuple.
When it is true count_even increase by one otherwise count_odd is increased by one.
Finally, we print the number of even and odd numbers through print statements.

Example: Iterating over list

In the following example for loop iterates through the list "datalist" and prints each item and its corresponding Python type.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))
<!--ID: 1639528995721-->


Output:

Type of  1452  is  <class 'int'>
Type of  11.23  is  <class 'float'>
Type of  (1+2j)  is  <class 'complex'>
Type of  True  is  <class 'bool'>
Type of  w3resource  is  <class 'str'>
Type of  (0, -1)  is  <class 'tuple'>
Type of  [5, 12]  is  <class 'list'>
Type of  {'section': 'A', 'class': 'V'}  is  <class 'dict'>
<!--ID: 1639528995749-->


Example: Iterating over dictionary

In the following example for loop iterates through the dictionary "color" through its keys and prints each key.

>>> color = {"c1": "Red", "c2": "Green", "c3": "Orange"}
>>> for key in color:
   print(key)
 
c2
c1
c3
>>>
<!--ID: 1639528995771-->


Following for loop iterates through its values :

>>> color = {"c1": "Red", "c2": "Green", "c3": "Orange"}
>>> for value in color.values():
   print(value)
<!--ID: 1639528995793-->


Green
Red
Orange
>>>

== The break Statement

With the break statement we can stop the loop before it has looped through all the items:
Example

Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
Example

Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

The continue Statement

With the continue statement we can stop the current iteration of the loop, and continue with the next:
Example

Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

The pass Statement

for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
Example
for x in [0, 1, 2]:
  pass

You can attach an optional else clause with for statement, in this case, syntax will be -

for variable_name in sequence :
    statement_1
    statement_2
    ....
else :
    statement_3
    statement_4
    ....

The else clause is only executed after completing the for loop. If a break statement executes in first program block and terminates the loop then the else clause does not execute.



== The range() Function
To loop through a set of code a specified number of times, we can use the range() function,

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
Example

Using the range() function:
for x in range(6):
  print(x)

Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
Example

Using the start parameter:
for x in range(2, 6):
  print(x)

The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
Example

Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)
Else in For Loop

The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
Example

Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
  print(x)
else:
  print("Finally finished!")

Python for loop and range() function

The range() function returns a list of consecutive integers. The function has one, two or three parameters where last two parameters are optional. It is widely used in for loops. Here is the syntax.

range(a)
range(a,b)
range(a,b,c)

range(a) : Generates a sequence of numbers from 0 to a, excluding a, incrementing by 1.

Syntax:

for <variable> in range(<number>):

Example:

>>> for a in range(4):
  print(a)
 
  0
  1
  2
  3
>>>

range(a,b): Generates a sequence of numbers from a to b excluding b, incrementing by 1.

Syntax:

for "variable" in range("start_number", "end_number"):

Example:

>>> for a in range(2,7):
 print(a)

  2
  3
  4
  5
  6
>>>

range(a,b,c): Generates a sequence of numbers from a to b excluding b, incrementing by c.

Example:

>>> for a in range(2,19,5):
  print(a)
 
 2
 7
 12
 17
>>>

Python Loops with range().

In Python, a for loop can be used to perform an action a specific number of times in a row.

The range() function can be used to create a list that can be used to specify the number of iterations in a for loop.
# Print the Numbers 0, 1, 2
for i in range(3):
  print(i)

# Print "WARNING" 3 times
for i in range(3):
  print("WARNING")


