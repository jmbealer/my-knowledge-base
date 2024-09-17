---
title: Python-functions
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# Python-functions
== Python Functions WIP

functions are action that can be performed on data types.
math functions
is a self-contained block of code that encapsulates a specific task or related group of tasks.
need to know about function interface:
* what arguments (if any) it takes
* what value (if any) it returns

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

def <function_name>([<parameters>]):
    <statement(s)>
def keyword for defining a function
<parameters> An optional, comma-separated list of parameters that may be passed to the function
: Punctuation that denotes the end of the Python function header (the name and parameter list)
Creating a Function

In Python a function is defined using the def keyword:
Example
def my_function():
  print("Hello from a function")
Calling a Function

To call a function, use the function name followed by parenthesis:
Example
def my_function():
  print("Hello from a function")

my_function()
Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
Example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

Arguments are often shortened to args in Python documentations.
Parameters or Arguments?

The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.
Number of Arguments

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
Example

This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
If you try to call the function with 1 or 3 arguments, you will get an error:
Example

This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
Arbitrary Arguments, *args

If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
Example

If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

Arbitrary Arguments are often shortened to *args in Python documentations.
Keyword Arguments

You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
Arbitrary Keyword Arguments, **kwargs

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
Example

If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
Default Parameter Value

The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
Passing a List as an Argument

You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:
Example
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
Return Values

To let a function return a value, use the return statement:
Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
The pass Statement

function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
Example
def myfunction():
  pass
Recursion

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
Example

Recursion Example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



Function Parameters

Sometimes functions require input to provide data for their code. This input is defined using parameters.

Parameters are variables that are defined in the function definition. They are assigned the values which were passed as arguments when the function was called, elsewhere in the code.

For example, the function definition defines parameters for a character, a setting, and a skill, which are used as inputs to write the first sentence of a book.
def write_a_book(character, setting, special_skill):
  print(character + " is in " +
        setting + " practicing her " +
        special_skill)
Multiple Parameters

Python functions can have multiple parameters. Just as you wouldn’t go to school without both a backpack and a pencil case, functions may also need more than one input to carry out their operations.

To define a function with multiple parameters, parameter names are placed one after another, separated by commas, within the parentheses of the function definition.
def ready_for_school(backpack, pencil_case):
  if (backpack == 'full' and pencil_case == 'full'):
    print ("I'm ready for school!")
Functions

Some tasks need to be performed multiple times within a program. Rather than rewrite the same code in multiple places, a function may be defined using the def keyword. Function definitions may include parameters, providing data input to the function.

Functions may return a value using the return keyword followed by the value to return.
\# Define a function my_function() with parameter x

def my_function(x):
  return x + 1

\# Invoke the function

print(my_function(2))      \# Output: 3
print(my_function(3 + 5))  \# Output: 9
Function Indentation

Python uses indentation to identify blocks of code. Code within the same block should be indented at the same level. A Python function is one type of code block. All code under a function declaration should be indented to identify it as part of the function. There can be additional indentation within a function to handle other statements such as for and if so long as the lines are not indented less than the first line of the function code.
\# Indentation is used to identify code blocks

def testfunction(number):
  \# This code is part of testfunction
  print("Inside the testfunction")
  sum = 0
  for x in range(number):
    \# More indentation because 'for' has a code block
    \# but still part of he function
    sum += x
  return sum
print("This is not part of testfunction")
Calling Functions

Python uses simple syntax to use, invoke, or call a preexisting function. A function can be called by writing the name of it, followed by parentheses.

For example, the code provided would call the doHomework() method.
doHomework()
Function Arguments

Parameters in python are variables — placeholders for the actual values the function needs. When the function is called, these values are passed in as arguments.

For example, the arguments passed into the function .sales() are the “The Farmer’s Market”, “toothpaste”, and “$1” which correspond to the parameters grocery_store, item_on_sale, and cost.
def sales(grocery_store, item_on_sale, cost):
  print(grocery_store + " is selling " + item_on_sale + " for " + cost)

sales("The Farmer’s Market", "toothpaste", "$1")
Function Keyword Arguments

Python functions can be defined with named arguments which may have default values provided. When function arguments are passed using their names, they are referred to as keyword arguments. The use of keyword arguments when calling a function allows the arguments to be passed in any order — not just the order that they were defined in the function. If the function is invoked without a value for a specific argument, the default value will be used.
def findvolume(length=1, width=1, depth=1):
  print("Length = " + str(length))
  print("Width = " + str(width))
  print("Depth = " + str(depth))
  return length * width * depth;

findvolume(1, 2, 3)
findvolume(length=5, depth=2, width=4)
findvolume(2, depth=3, width=4)
Returning Multiple Values

Python functions are able to return multiple values using one return statement. All values that should be returned are listed after the return keyword and are separated by commas.

In the example, the function square_point() returns x_squared, y_squared, and z_squared.
def square_point(x, y, z):
  x_squared = x * x
  y_squared = y * y
  z_squared = z * z
  \# Return all three values:
  return x_squared, y_squared, z_squared

three_squared, four_squared, five_squared = square_point(3, 4, 5)



Function Arguments

Default argument is fallback value

In Python, a default parameter is defined with a fallback value as a default argument. Such parameters are optional during a function call. If no argument is provided, the default value is used, and if an argument is provided, it will overwrite the default value.
def greet(name, msg="How do you do?"):
  print("Hello ", name + ', ' + msg)

greet("Ankit")
greet("Ankit", "How do you do?")

"""
this code will print the following for both the calls -
`Hello  Ankit, How do you do?`
"""
Mutable Default Arguments

Python’s default arguments are evaluated only once when the function is defined, not each time the function is called. This means that if a mutable default argument is used and is mutated, it is mutated for all future calls to the function as well. This leads to buggy behaviour as the programmer expects the default value of that argument in each function call.
\# Here, an empty list is used as a default argument of the function.
def append(number, number_list=[]):
  number_list.append(number)
  print(number_list)
  return number_list

\# Below are 3 calls to the `append` function and their expected and actual outputs:
append(5) \# expecting: [5], actual: [5]
append(7) \# expecting: [7], actual: [5, 7]
append(2) \# expecting: [2], actual: [5, 7, 2]
Python Default Arguments

A Python function cannot define a default argument in its signature before any required parameters that do not have a default argument. Default arguments are ones set using the form parameter=value. If no input value is provided for such arguments, it will take on the default value.
\# Correct order of declaring default argments in a function
def greet(name, msg = "Good morning!"):
  print("Hello ", name + ', ' + msg)
  
\# The function can be called in the following ways
greet("Ankit")
greet("Kyla","How are you?")

\# The following function definition would be incorrect
def greet(msg = "Good morning!", name):
  print("Hello ", name + ', ' + msg)
\# It would cause a "SyntaxError: non-default argument follows default argument"
Python function default return value

If we do not not specify a return value for a Python function, it returns None. This is the default behaviour.
\# Function returning None
def my_function(): pass

print(my_function())

\#Output
None
Python variable None check

To check if a Python variable is None we can make use of the statement variable is None.

If the above statement evaluates to True, the variable value is None.
\# Variable check for None
if variable_name is None:
    print "variable is None"
else:
    print "variable is NOT None"
Python function arguments

A function can be called using the argument name as a keyword instead of relying on its positional value. Functions define the argument names in its composition then those names can be used when calling the function.
\# The function will take arg1 and arg2
def func_with_args(arg1, arg2):
  print(arg1 + ' ' + arg2)
  
func_with_args('First', 'Second')
\# Prints:
\# First Second

func_with_args(arg2='Second', arg1='First')
\# Prints
\# First Second

13. Functions

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

In other words, Functions in Python programming, is a group of related statements that performs a specific task. Functions make our program more organized and help in code re-usability.
Uses Of Functions:

    Functions help in code reusability
    Functions provide organization to the code
    Functions provide abstraction
    Functions help in extensibility

Function Definition (def and return statements)
Scopes of Variables Inside Functions (global and nonlocal statements)
Default Argument Values
Keyword Arguments
Arbitrary Argument Lists
Unpacking Argument Lists (* and ** statements)
Lambda Expressions (lambda statement)
Documentation Strings
Function Annotations
Function Decorators
print() function is used to tell a computer to talk.
  - should be surrounded by quotes

      Functions
          Definition def
              def my_fn():
                  \# your code
                  print "hello"
          Calling
              my_fn()
              add
              result = add(1,2)
              print result
              print square(1,2)
              result1, result2= square(1,2)
              print result1,result2
          Arguments/Return
              def add(n1, n2):
                  print n1+n2
                  return n1+n2
          Multiple Return
              def square(n1,n2):
                  return n1**2, n2**2


input() function reads this value and returns it in a program as a string.
  may take an optional argument, that is a message
  it stops and waits for the user to enter some value and press Enter.
  default conversion is a string
  int(input()) converts input to integer
  reads some data from the user and returns it in a program as a string.
  if a user writes an inaccurate input, ValueError will occur.

== print() function WIP

The print statement has been replaced with a print() function, with keyword arguments to replace most of the special syntax of the old print statement.

The print statement can be used in the following ways :

    print("Good Morning")
    print("Good", <Variable Containing the String>)
    print("Good" + <Variable Containing the String>)
    print("Good %s" % <variable containing the string>)

In Python, single, double and triple quotes are used to denote a string. Most use single quotes when declaring a single character. Double quotes when declaring a line and triple quotes when declaring a paragraph/multiple lines.

Commands

print(<el_1>, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Use 'file=sys.stderr' for errors.
    Use 'flush=True' to forcibly flush the stream.

Pretty Print

from pprint import pprint
pprint(<collection>, width=80, depth=None)

    Levels deeper than 'depth' get replaced by '...'.

Double Quotes Use:

Example:

print("Python is very simple language")

Output:

Python is very simple language

Single Quotes Use:

Example:

print('Hello')

Output:

Hello

Triple Quotes Use:

Example:

print("""Python is very popular language.
It is also friendly language.""")

Output:

Python is very Popular Language.
It is also friendly language.

Variable Use:

Strings can be assigned to variable say string1 and string2 which can called when using the print statement.

Example:

str1 = 'Wel'
print(str1,'come')

Output:

Wel come

Example:

str1 = 'Welcome'
str2 = 'Python'
print(str1, str2)

Output:

Welcome Python

String Concatenation:

String concatenation is the "addition" of two strings. Observe that while concatenating there will be no space between the strings.

Example:

str1 = 'Python'
str2 = ':'
print('Welcome' + str1 + str2)

Output:

WelcomePython:

Using as String:

%s is used to refer to a variable which contains a string.

Example:

str1 = 'Python'
print("Welcome %s" % str1)

Output:

Welcome Python

Using other data types:

Similarly, when using other data types

    %d -> Integer
    %e -> exponential
    %f -> Float
    %o -> Octal
    %x -> Hexadecimal

This can be used for conversions inside the print statement itself.

Using as Integer:

Example:

print("Actual Number = %d" %15)

Output:

Actual Number = 15

Using as Exponential:

Example:

print("Exponential equivalent of the number = %e" %15)

Output:

Exponential equivalent of the number = 1.500000e+01

Using as Float:

Example:

print("Float of the number = %f" %15)

Output:

Float of the number = 15.000000

Using as Octal:

Example:

print("Octal equivalent of the number = %o" %15)

Output:

Octal equivalent of the number = 17

Using as Hexadecimal:

Example:

print("Hexadecimal equivalent of the number = %x" %15)

Output:

Hexadecimal equivalent of the number = f

Using multiple variables:

When referring to multiple variables parenthesis is used.

Example:

str1 = 'World'
str2 = ':'
print("Python %s %s" %(str1,str2))

Output:

Python World :

Other Examples of Print Statement:

The following are other different ways the print statement can be put to use.

Example-1:

% is used for %d type word

print("Welcome to %%Python %s" %'language')

Output:

Welcome to %Python language

Example-2:

\n is used for Line Break.

print("Sunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday")

Output:

Sunday
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday

Example-3:

Any word print multiple times.

print('-w3r'*5)

Output:

-w3r-w3r-w3r-w3r-w3r

Example-4:

\t is used for tab.

print("""
Language:
\t1 Python
\t2 Java\n\t3 JavaScript
""")

Output:

Language:
        1 Python
        2 Java
        3 JavaScript

Precision Width and Field Width:

Field width is the width of the entire number and precision is the width towards the right. One can alter these widths based on the requirements.

The default Precision Width is set to 6.

Example-1:

Notice upto 6 decimal points are returned. To specify the number of decimal points, '%(fieldwidth).(precisionwidth)f' is used.

print("%f" % 5.1234567890)

Output:

5.123457

Example-2:

Notice upto 5 decimal points are returned

print("%.5f" % 5.1234567890)

Output:

5.12346

Example-3:

If the field width is set more than the necessary than the data right aligns itself to adjust to the specified values.

print("%9.5f" % 5.1234567890)

Output:

  5.12346

Example-4:

Zero padding is done by adding a 0 at the start of fieldwidth.

print("%015.5f" % 5.1234567890)

Output:

000000005.12346

Example-5:

For proper alignment, a space can be left blank in the field width so that when a negative number is used, proper alignment is maintained.

print("% 9f" % 5.1234567890)
print("% 9f" % -5.1234567890)

Output:

 5.123457
-5.123457

Example-6:

'+' sign can be returned at the beginning of a positive number by adding a + sign at the beginning of the field width.

print("%+9f" % 5.1234567890)
print("% 9f" % -5.1234567890)

Output:

+5.123457
-5.123457

Example-7:

As mentioned above, the data right aligns itself when the field width mentioned is larger than the actually field width. But left alignment can be done by specifying a negative symbol in the field width.

print("%-9.4f" % 5.1234567890)

Output:

5.1235

