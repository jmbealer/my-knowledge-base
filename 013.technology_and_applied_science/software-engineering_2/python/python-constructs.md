---
title: Python-constructs
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# Python-constructs

== Python Constructs
i. Functions

A function in Python is a collection of statements grouped under a name. You can use it whenever you want to execute all those statements at a time. You can call it wherever you want and as many times as you want in a program. A function may return a value.
ii. Classes

As we discussed earlier, Python is an object-oriented language. It supports classes and objects. A class is an abstract data type. In other words, it is a blueprint for an object of a certain kind. It holds no values. An object is a real-world entity and an instance of a class.
iii. Modules

A Python module is a collection of related classes and functions. We have modules for mathematical calculations, string manipulations, web programming, and many more. We will discuss Python Module in detail in a later lesson.
iv. Packages

Python package is a collection of related modules. You can either import a package or create your own.
v. List

You can think of a list as a collection of values. Declared in the CSV (Comma-Separated Values) format and delimit using square brackets:
life = [‘love’, ‘wisdom’, ‘anxiety’];
arity = [1,2,3];

Notice that we do not declare the type for the list either. A list may also contain elements of different types, and the indexing begins at 0:
person = [‘firstname’, 21];
print(person[1])

Output: 21
You can also slice lists; slicing is a way of retrieving some values from it. We will learn more about it in further lessons.
vi. Tuple

A tuple is like a list, but it is immutable (you cannot change its values).
pizza = (‘base’, ‘sauce’, ‘cheese’, ‘mushroom’);
pizza[3] = ‘jalapeno’

This raises a TypeError.
vii. Dictionary

A dictionary is a collection of key-value pairs. Declare it using curly braces, and commas to separate key-value pairs. Also, separate values from keys using a colon (:).
student = {‘Name’: ‘Abc’, ‘Age’: 21}
print(student[‘Age’])
<!--ID: 1639528996109-->


Output: 21
viii. Comments and Docstrings

Declare comments using an octothorpe (#). However, Python does not support multiline comments. Also, docstrings are documentation strings that help explain the code.
\#This is a comment
“““
This is a docstring
”””
Python has a lot of other constructs. These include control structures, functions, exceptions, etc. We will discuss these in further tutorials.





