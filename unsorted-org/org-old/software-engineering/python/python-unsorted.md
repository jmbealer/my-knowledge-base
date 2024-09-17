---
title: Python-unsorted
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# Python-unsorted
== Unsorted
=== Files

Reading and Writing (with statement)
Methods of File Objects

1. Learn Basics Concept of Python
14. File Operations / File Handling

File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.
File Handling

File Handling refers to those operations that are used to read or write a file.

To perform file handling, we need to perform these steps:

    Step1: Open File
    Step2: Read / Write File
    Step3: Close File

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.
Opening A File:

Python has a built-in function open() to open a file This function returns a file object, also called a handle, as it is used to read or modify the file accordingly
Writing To A File:

In order to write into a file we need to open it in write ‘w’, append ‘a’ or exclusive creation ‘x’ mode We need to be careful with the ‘w’ mode as it will overwrite into the file if it already exists. All previous data are erased Writing a string or sequence of bytes (for binary files) is done using write() method
Reading From A File:

To read the content of a file, we must open the file in the reading mode We can use the read(size) method to read in size number of data If size parameter is not specified, it reads and returns up to the end of the file
Closing A File:

When we are done with operations to the file, we need to properly close it. Closing a file will free up the resources that were tied with the file and is done using the close() method.
File Operations Using Python – CRUD Operation In Python:

What are the various file operations that you can generally perform?

We call it CRUD. CRUD stands for:

    Create
    Read
    Update
    Delete

There are four different methods (modes) for opening a file:

- "r" - Read - Default value. Opens a file for reading, error if the file does not exist

- "a" - Append - Opens a file for appending, creates the file if it does not exist

- "w" - Write - Opens a file for writing, creates the file if it does not exist

- "x" - Create - Creates the specified file, returns an error if the file exists

    In addition you can specify if the file should be handled as binary or text mode

        "t" - Text - Default value. Text mode

        "b" - Binary - Binary mode (e.g. images)

Types Of Files Supported By Python

Can you quickly think of all of the types of files that you know? Image, audio, video, text, scripts and many more.

The dependency on the native Operating System is the most important thing to keep in mind when considering the type of files supported.

Windows supports all of the file types mentioned in the first line. But does it support every type of file? Absolutely not! There are certain limitations here as well.

Now, coming to Python – There are 2 types of files mainly:

    Binary
    Text

A binary file is any type of file that is not a text file. Because of their nature, binary files can only be processed by an application that knows or understand the file’s structure. In other words, they must be applications that can read and interpret binary.

Text files are structured as a sequence of lines, where each line includes a sequence of characters. This is what you know as code or syntax. Each line is terminated with a special character, called the EOL or End of Line character.
15. Exception Handling:

The "try" block lets you test a block of code for errors.

The "except" block lets you handle the error.

The "finally" block lets you execute code, regardless of the result of the try- and except blocks.

      File Input/Output
          Open
              variable = open("file.txt","open mode")
          Open Modes 
              r = open for read (default)
              w = open for write, truncate
              r+ = open for read/write
              w+ = open for read/write, truncate
              a+ = open for read/append
          Read
              variable = texts.read()
          Read lines
              for vari in variable:
                  print vari,
          Write/Append
              variable.write("something\n")
          Close
              variable.close()


=== Additions

The pass statement
Generators (yield statement)

=== Brief Tour of the Standard Libraries

Serialization (json library)
File Wildcards (glob library)
String Pattern Matching (re library)
Mathematics (math, random, statistics libraries)
Dates and Times (datetime library)
Data Compression (zlib library)






The .real and .imag properties don’t need parentheses after them like .conjugate() does.

The .conjugate() method is a function that performs an action on a complex number, whereas .real and .imag don’t perform any action—they just return some information about the number.

The distinction between methods and properties is an important aspect of object-oriented programming.
