---
title: 'Will Print "Hello"'
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-53
reference: 
description: 
aliases: 
tags: 
---
== Codecademy WIP



Errors

The Python interpreter will report errors present in your code. For most error cases, the interpreter will display the line of code where the error was detected and place a caret character ^ under the portion of the code where the error was detected.
if False ISNOTEQUAL True:
                  ^
SyntaxError: invalid syntax

ZeroDivisionError

A ZeroDivisionError is reported by the Python interpreter when it detects a division operation is being performed and the denominator (bottom number) is 0. In mathematics, dividing a number by zero has no defined value, so Python treats this as an error condition and will report a ZeroDivisionError and display the line of code where the division occurred. This can also happen if a variable is used as the denominator and its value has been set to or changed to 0.
numerator = 100
denominator = 0
bad_results = numerator / denominator

ZeroDivisionError: division by zero

SyntaxError

A SyntaxError is reported by the Python interpreter when some portion of the code is incorrect. This can include misspelled keywords, missing or too many brackets or parenthesis, incorrect operators, missing or too many quotation marks, or other conditions.
age = 7 + 5 = 4

File "<stdin>", line 1
SyntaxError: can't assign to operator

NameError

A NameError is reported by the Python interpreter when it detects a variable that is unknown. This can occur when a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined. The Python interpreter will display the line of code where the NameError was detected and indicate which name it found that was not defined.
misspelled_variable_name

NameError: name 'misspelled_variable_name' is not defined

print() Function

The print() function is used to output text, numbers, or other printable information to the console.

It takes one or more arguments and will output each of the arguments to the console separated by a space. If no arguments are provided, the print() function will output a blank line.
print("Hello World!")

print(100)

pi = 3.14159
print(pi)


The Scope of Variables

In Python, a variable defined inside a function is called a local variable. It cannot be used outside of the scope of the function, and attempting to do so without defining the variable outside of the function will cause an error.

In the example, the variable a is defined both inside and outside of the function. When the function f1() is implemented, a is printed as 2 because it is locally defined to be so. However, when printing a outside of the function, a is printed as 5 because it is implemented outside of the scope of the function.
a = 5

def f1():
  a = 2
  print(a)
  
print(a)   # Will print 5
f1()       # Will print 2
Returning Value from Function

A return keyword is used to return a value from a Python function. The value returned from a function can be assigned to a variable which can then be used in the program.

In the example, the function check_leap_year returns a string which indicates if the passed parameter is a leap year or not.
def check_leap_year(year):
  if year % 4 == 0:
    return str(year) + " is a leap year."
  else:
    return str(year) + " is not a leap year."

year_to_check = 2018
returned_value = check_leap_year(year_to_check)
print(returned_value) # 2018 is not a leap year.
Global Variables

A variable that is defined outside of a function is called a global variable. It can be accessed inside the body of a function.

In the example, the variable a is a global variable because it is defined outside of the function prints_a. It is therefore accessible to prints_a, which will print the value of a.
a = "Hello"

def prints_a():
  print(a)
  
# Will Print "Hello"
prints_a()
Parameters as Local Variables

Function parameters behave identically to a function’s local variables. They are initialized with the values passed into the function when it was called.

Like local variables, parameters cannot be referenced from outside the scope of the function.

In the example, the parameter value is defined as part of the definition of my_function, and therefore can only be accessed within my_function. Attempting to print the contents of value from outside the function causes an error.
def my_function(value):
  print(value)
  
# Pass the Value 7 into the Function
my_function(7)

# Causes an Error as `value` no Longer Exists
print(value)



Files
Python File Object

A Python file object is created when a file is opened with the open() function. You can associate this file object with a variable when you open a file using the with and as keywords. For example:

with open('somefile.txt') as file_object:

You can then print the content of the file object, file_object with print().

print(file_object)

You might see something like this on the output terminal:

<_io.TextIOWrapper name='somefile.txt' mode='r' encoding='UTF-8'>

Python Readline Method

To read only one line instead of multiple lines in a Python file, use the method .readline() on a file object that is returned from the open() function. Every subsequent .readline() will extract the next line in the file if it exists.

with open('story.txt') as story_object:
  print(story_object.readline())

will print only the first line in story.txt.
Parsing JSON files to dictionary

JSON format is used to store key value pairs. Python’s json module allows reading such data format and parsing it to a dictionary. The json.load function takes a file object as an argument and returns the data in a dictionary format.
# Use json.load with an Opened File Object to Read the Contents into a Python Dictionary

# Contents of file.json
# { 'userId': 10 }
<!--ID: 1639528996133-->



import json
with open('file.json') as json_file:
  python_dict = json.load(json_file)
  
print(python_dict.get('userId'))
# Prints 10
Python Append To File

Writing to an opened file with the 'w' flag overwrites all previous content in the file. To avoid this, we can append to a file instead. Use the 'a' flag as the second argument to open(). If a file doesn’t exist, it will be created for append mode.

with open('shopping.txt', 'a') as shop:
  shop.write('Tomatoes, cucumbers, celery\n')

Python Write To File

By default, a file when opened with open() is only for reading. A second argument 'r' is passed to it by default. To write to a file, first open the file with write permission via the 'w' argument. Then use the .write() method to write to the file. If the file already exists, all prior content will be overwritten.

with open('diary.txt','w') as diary:
  diary.write('Special events for today')

Python Readlines Method

Instead of reading the entire content of a file, you can read a single line at a time. Instead of .read() which returns a string, call .readlines() to return a list of strings, each representing an individual line in the file. Calling this code:

with open('lines.txt') as file_object:
  file_data = file_object.readlines()
print(file_data)

returns a list of strings in file_data:

['1. Learn Python.\n', '2. Work hard.\n', '3. Graduate.']

Iterating over the list, file_data, and printing it:

for line in file_data:
  print(line)

outputs:

1. Learn Python.

2. Work hard.

3. Graduate.

Class csv.DictWriter

In Python, the csv module implements classes to read and write tabular data in CSV format. It has a class DictWriter which operates like a regular writer but maps a dictionary onto output rows. The keys of the dictionary are column names while values are actual data.

The csv.DictWriter constructor takes two arguments. The first is the open file handler that the CSV is being written to. The second named parameter, fieldnames, is a list of field names that the CSV is going to handle.
# An Example of csv.DictWriter
import csv

with open('companies.csv', 'w') as csvfile:
  fieldnames = ['name', 'type']
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerow({'name': 'Codecademy', 'type': 'Learning'})
  writer.writerow({'name': 'Google', 'type': 'Search'})
<!--ID: 1639528996155-->


"""
After running the above code, companies.csv will contain the following information:

name,type
Codecademy,Learning
Google,Search
"""
Python Read Method

After a file is opened with open() returning a file object, call the .read() method of the file object to return the entire file content as a Python string. Executing the following Python code:

with open('mystery.txt') as text_file:
  text_data = text_file.read()
print(text_data)

will produce a string containing the entire content of the read file:

Mystery solved.
Congratulations!




