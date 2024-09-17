---
title: What is Strings?
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-51
reference: 
description: 
aliases: 
tags: 
---
# What is Strings?

: strings == str
: strings are immutable sequences of Unicode characters.
: strings are wrapped inside single, double, or triple quotes.
: immutable; can't be changed after created
: strings wrapped with triple quotes are multi-line strings.
: strings are **arrays** of bytes representing unicode characters.

: python has no characters data type
: a single character is string with the length of 1.
: strings with a length of 1 is a sub-strings

Reassigning the existing string-variable is more straightforward in Python. We have to use + operator along with the sub-string location. Let's show this as an example:

ch = "Hello Python"

print ("UPDATED STRING WILL BE: " , ch [:8]+ "Python")

UPDATED STRING WILL BE: Hello PyPython

## Strings Example

'This is a String.'
"This is a String."
'This is not a String."
"This is not a String.'
'''This is
multi-line
String.'''
"""This is
multi-line
String."""

## String Operations

Assignment operator: “=”
Concatenate operator: “+”
String repetition operator: “*”
String slicing operator: “[]”
String comparison operator: “==” & “!=”
Membership operator: “in” & “not in”
Escape sequence operator: “\”
String formatting operator: “%” & “{}”

### String Slicing []

Slicing [] return the character from the given index.
Range Slicing [:] returns the characters from the given range.

A segment of a string is called a slice [].
Index 0 returns the first character of a string.
Index -1 returns the last character of a string.
Cutting a substring from a string is called string slicing.
If index is out of range for the string, Python returns an error.

slicing operator [].
str[start:stop]
str[start:stop:step]

We can use any expression, including variables and operators, as an index
str = 'Python'
str1 = str[2+2] \# Returns o same as str[4]

The value of the index has to be an integer.
str = 'Python'
str1 = str[2.2] \# Returns an error


.Examples; String Slicing []
string[a]: Returns a character from a positive index a of the string
string[-a]: Returns a character from a negative index a of the string
string[a:b]: Returns characters from positive index a to positive index b (not including)
string[a:-b]: Returns characters from positive index a to the negative index b of the string (not including)
string[a:]: Returns characters from positive index a to the end of the string.
string[:b]: Returns characters from the start of the string to the positive index b. (not including)
string[-a:]: Returns characters from negative index a to the end of the string.
string[:-b]: Returns characters from the start of the string to the negative index b. (not including)
string[::-1]: Returns a string with reverse order.
<!--ID: 1639528993680-->


str = 'Python'
str[1:4] \# Returns yth
  Returns characters from index 1 to but not including index 4.
str[1:] \# Returns ython
  Returns characters from index 1 to the end of the string.
str[:5] \# Returns Pytho
  Returns characters from the beginning of the string to index 5.
str[:] \# Returns Python
  Returns the whole string.
str[1:100] \# Returns ython
  Returns a truncated down string length.
str[1] \# Returns y
  Returns index 1
str[-3] \# Returns h
  Returns index -3
str[-5:-1] \# Returns ytho
  Returns characters from index -5 to but not including index -1.
str[-3:] \# Returns hon
  Returns characters from index -3 to the end of the string.
str[:-3] \# Returns Pyt
  Returns characters from the beginning of the string to index -3.
str[::-1] \# Returns nothyP
<!--ID: 1639528993695-->

  Returns a string with reverse order.


.Negative Indexing
Use negative indexes to start the slice from the end of the string:

\# Concatenates a new first letter on to a slice of greeting.
str = 'Python'
concat = 'X' + str[1:] \# Returns Xython

### String Concatenation

String Concatenation means joining one or more strings together.
String Concatenation Operator is (+).
Can't concatenate values of different types.


.String Concatenation example:
a = 'Hello' + 'World' \# HelloWorld
a = 'Hello' + ' ' + 'World' \# Hello World

a = "Hello"
b = "World"
c = a + b \# HelloWorld

a = "Hello"
b = "World"
c = a + " " + b \# Hello World

a = "Hello"
b = "World"
a += b \# HelloWorld

### String Repetition Operator

String Repetition Operator is (*).
String Repetition create a new string by repeating it a given number of times.

.String Repetition example:
a = 'Hello'
print(a*2) \#HelloHello

### Others
String length:

len() is a built-in function which returns the number of characters in a string:

>>> a = "Python string"
>>> len(a)
13
>>> a[13]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> a[12]
'g'
>>>

Traverse string with a while or for loop

    A lot of computations involve processing a string character by character at a time.
    They start at the beginning, select each character, in turn, do something to it, and continue until the end.
    This pattern of processing is called a traversal.
    One can traverse string with a while or for loop:

Code:

a = "STRING"
i = 0
while i < len(a):
    c = a[i]
    print(c)
    i = i + 1

Output:

>>>
S
T
R
I
N
G
>>>

Traversal with a for loop :

Print entire string on one line using for loop.

Code:

a = "Python"
i = 0
new=" "
for i in range (0,len(a)):
  b=a[i]
  \# + used for concatenation
  new = new+b
  i = i + 1
  \# prints each char on one line
  print(b)
  print(new)

Output:

>>>
P
 P
y
 Py
t
 Pyt
h
 Pyth
o
 Pytho
n
 Python
>>>



### Escape Characters

Backslashes (\) are used to escape or add special characters in a Python string.

Escape Characters also called Escape Sequences.

.Escape Characters example:
\' Single Quote (')
\" Double Quote (")
\\ Backslash (/)
\ Newline ignored
\a ASCII Bell (BEL)
\b ASCII Backspace (BS)
\f ASCII Form-feed (FF)
\n ASCII Line-feed (LF)
  Newline or next line
\r ASCII Carriage Return (CR)
\t ASCII Horizontal Tab (TAB)
\v ASCII Vertical Tab (VT)
\ooo Octal value (ooo)
\xhh Hex value (hh)
\cx or \C-x Control x
\M-\C-x Meta-Control-x
\e Escape
\s Space
\u0000 Unicode characters

## String Length

To get the length of a string, use the len() function.
Example

The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

Built-in Function len()

In Python, the built-in len() function can be used to determine the length of an object. It can be used to compute the length of strings, lists, sets, and other countable objects.
length = len("Hello")
print(length)
\# Output: 5

colors = ['red', 'yellow', 'green']
print(len(colors))
\# Output: 3

## String Formatting

String Formatting is use to join and combine two or more string with different data.
Formats specified values in a string.
old-school string formatting; % string formatting, str.format() method

### .format()
formats() string method is used for string formatting.
The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
You call the method on <template>, which is a string containing replacement
<template> is a string containing replacement fields.
replacement fields are enclosed in curly brackets {}.
<positional_arguments> and <keyword_arguments> are specify values inserted into the <template> replacement fields.
Positional arguments are inserted into the template in place of numbered replacement fields.
the numbering of replacement fields is zero-based.
'{0}/{1}/{2}'.format('foo', 'bar', 'baz') \# foo/bar/baz
automatic field numbering is omitting the numbers in the replacement field, in which the interpreter assumes sequential order.
cant intermingle automatic or explicit replacement field numbering.
keyword arguments are inserted into the <template> string in place of keyword replacement fields with the same name
'{x}/{y}/{z}'.format(x='foo', y='bar', z='baz') \# foo/bar/baz
You can specify both positional and keyword arguments in one Python .format() call.
All positional arguments must appear before any of the keyword arguments.
'{0}{x}{1}'.format('foo', 'bar', x='baz') # foobarbaz
x,y,z = 'foo', 'bar', 'baz'
'{0}/{1}/{s}'.format(x, y, s=x)
replacement fields indicate where in the <template> to insert the arguments to the method
replacement field consist of three components:
{[<name>][!<conversion>][:<format_spec>]}
<name> specifies the source of the value tobe formatted.
<conversion> Indicates which standard Python function to use to perform the conversion.
<format_spec> specifies more detail about how the value should be converted.
each component is optional and may  be omitted.
the <name> component is the first portion of a replacement field
<name> indicates which argument from the argument list is inserted into the Python format string in the given location.
<name> is either a number for a positional argument or a keyword for a keyword argument.
You can use indices with <name> to access the list's elements, if the argument is a list
a = ['foo', 'bar', 'baz']
'{0[0]}, {0[2]},'.format(a) # foo, baz
'{my_list[0]}, {my_list[2]},'.format(my_list=a) # foo, baz
You can use a key reference with <name> if the arguments is a dictionary
d = {'key1': 'foo', 'key2': 'bar'}
'{0[key1]}'.format(d) # foo
'{my_dict[key2]}'.format(my_dict=d) # bar
z = 3+5j
'real = {0.real}, imag = {0.imag}'.format(z) # real = 3.0 imag = 5.0
The <conversion> component is the second portion of a replacement field
Python can format an object as a string using three different built-in functions:
  str(), repr(), ascii()
By default, the Python .format() method uses str().
!s converts with str()
!r converts with repr()
!a converts with ascii()
'{0!s}'.format(42) # str(42)
'{0!r}'.format(42) # repr(42)
'{0!a}'.format(42) # ascii(42)
In many cases, the result remains the same regardless of which conversion function you use
The <format_spec> component is the last portion of a replacement field:
<format_spec> represents the guts of the Python .format() method’s functionality.
<format_spec> contains information that exerts fine control over how values are formatted prior to being inserted into the template string.
:[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<prec>][<type>]
The ten subcomponents of <format_spec>:
  : Separates the <format_spec> from the rest of the replacement field.
  <fill> Specifies how to pad values that don't occupy the entire field width.
  <align> Specifies how to justify values that don't occupy the entire field width.
  <sign> Controls whether a leading sign is included for numeric values.
# Selects an Alternate Output Form for Certain Presentation Types
  0 Causes values to be padded on the left with zeros instead of ASCII space characters.
  <width> Specifies the minimum width of the output.
  <group> Specifies a grouping character for numeric output.
  .<prec> Specifies the number of digits after the decimal point for floating-point presentation types, and the maximum output for string presentations types.
  <type> Specifies the presentation type, which is the type of conversion performed on the corresponding argument.
.The <type> subcomponent
<type> is the final portion of <format_spec>.
b Binary integer
c Single character
d Decimal integer
e or E Exponential
f or F Floating point
g or G Floating point or Exponential
o Octal integer
s String
x or X Hexadecimal integer
% Percentage
<!--ID: 1639528993709-->


'%d' % 42 # 42
'{:d}'.format(42) # 42
'%f' % 2.1 # 2.100000
'{:f}'.format(2.1) # 2.100000
'%s' % 'foobar' # foobar
'{:s}'.format('foobar') # foobar
'%x' % 31 # 1f
'{:x}'.format(31) # 1f
<!--ID: 1639528993734-->


Type: .format() Method; String Modulo Operator
b: Designates binary integer conversion; Not supported
i, u: Not supported; Designates integer conversion
c: Designates character conversion, and the corresponding value must be an integer; Designates character conversion, but the corresponding value may be either an integer or a single-character string
g, G: Chooses between floating point or exponential output, but the rules governing the choice are slightly more complicated; Chooses between floating point or exponential output, depending on the magnitude of the exponent and the value specified for <prec>
r, a: Not supported (though the functionality is provided by the !r and !a
conversion components in the replacement field); Designates conversion with repr() or ascii(), respectively
%: Converts a numeric argument to a percentage; Inserts a literal '%' character into the output

'{:b}'.format(257) # 100000001
d designates decimal integer conversion
'%c' % 35 # #
'%c' % # #
'{:c}'.format(35) # #
'%f%%' % 65.0 # 65.000000%
'{:%}'.format(0.65) # 65.000000%
multiplies the specified value by 100 and appends a percent sign
<!--ID: 1639528993747-->


.The <fill> and <align> Subcomponents
<fill> and <align> control how formatted output is padded and positioned within the specified field width.
these subcomponents only have meaning when the formatted field value doesn't occupy the entire field width,
which can only happen if a minimum field width is specified with <width>.
If <width> isn't specified, then <fill> and <align> are effectively ignored.

Values for the <align> subcomponents:
<
>
^
=
A value using the less-than sign (<) indicates that the output is left-justified:
'{0:<Bs}'.format('foo') # 'foo   '
'{0:<Bd}'.format('123') # '123   '
This behavior is the default for string values.
A value using the greater-than sign (>) indicates that the output is right-justified:
'{0:>Bs}'.format('foo') # '   foo'
'{0:>Bd}'.format('123') # '   123'
This behavior is the default for numeric values.
A value using a caret (>) indicates that the output is centered:
'{0:^Bs}'.format('foo') # '  foo  '
'{0:^Bd}'.format('123') # '  123  '
This behavior is the default for numeric values.
<!--ID: 1639528993770-->




.String Formatting syntax:
'{} {}'.format(list of variables)
`str.format(*args, **kwargs)`
<!--ID: 1639528993789-->


'{} {}'.format('Python', 'Format')
'Python Format'
<!--ID: 1639528993802-->


'{1} {0}'.format('Python', 'Format')
'Format Python'
<template>.format(<positional_arguments(s)>, <keyword_argument(s)>)
<!--ID: 1639528993825-->


.String formatting operator %
String formatters allow us to print characters and values at once.
String Format operator is %
String Format operator is followed by variables in parentheses or a tuple

<format_string> % <values>
'Just a %s in %s %d' % ('test', 'Python', 3)

%c character
%s string conversion via str() prior to formatting
%i signed decimal integer
%d signed decimal integer
%u unsigned decimal integer
%o octal integer
%x hexadecimal integer (lowercase letters)
%X hexadecimal integer (UPPERcase letters)
%e exponential notation (with lowercase 'e')
%E exponential notation (with UPPERcase 'E')
%f floating point real number
%g the shorter of %f and %e
%G the shorter of %f and %E


.f-strings
formatted string literal
A third option is to use f-strings.
>>> print(f"I just printed {x} pages to the printer {printer}")
i. f-strings
<!--ID: 1639528993844-->


The letter ‘f’ precedes the string, and the variables are mentioned in curly braces in their places.
>>> name='Ayushi'
>>> print(f"It isn't {name}'s birthday")
<!--ID: 1639528993862-->


It isn’t Ayushi’s birthday

Notice that because we wanted to use two single quotes in the string, we delimited the entire string with double quotes instead.

11.3. f-strings

If you use an f-string, you just need to mention the identifiers in curly braces. Also, write ‘f’ right before the string, but outside the quotes used.
>>> print(f"I just printed {x} pages to the printer {printer}")
<!--ID: 1639528993876-->


Output:

I just printed 10 pages to the printer HP





8. Python String Formatters

Sometimes, you may want to print variables along with a string. You can either use commas, or use string formatters for the same.
>>> city='Ahmedabad'
>>> print("Age",21,"City",city)

Age 21 City Ahmedabad

ii. format() method

You can use the format() method to do the same. It succeeds the string, and has the variables as arguments separated by commas. In the string, use curly braces to posit the variables. Inside the curly braces, you can either put 0,1,.. or the variables. When doing the latter, you must assign values to them in the format method.
>>> print("I love {0}".format(a))
<!--ID: 1639528993899-->


I love dogs
>>> print("I love {a}".format(a='cats'))
<!--ID: 1639528993918-->


I love cats

The variables don’t have to defined before the print statement.
>>> print("I love {b}".format(b='ferrets'))
<!--ID: 1639528993930-->


I love ferrets

11.2. Format Method

The format method allows you to format a string in a similar way. At the places, you want to put values, put 0,1,2,.. in curly braces. Call the format method on the string and mention the identifiers in the parameters.
>>> print("I just printed {0} pages to the printer {1}".format(x, printer))
<!--ID: 1639528993958-->


Output:

I just printed 10 pages to the printer HP

You can also use the method to print out identifiers that match certain values.
>>> print("I  just printed {x} pages to the printer {printer}".format(x=7, printer='HP'))
<!--ID: 1639528993972-->


Output:

I just printed 7 pages to the printer HP



To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:


You can add parameters inside the curly brackets to specify how to convert the value:
Example

Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"
<!--ID: 1639528993996-->


Check out all formatting types in our String format() Reference.

Multiple Values

If you want to use more values, just add more values to the format() method:
print(txt.format(price, itemno, count))

And add more placeholders:
Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
<!--ID: 1639528994010-->


Index Numbers

You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
<!--ID: 1639528994034-->


Also, if you want to refer to the same value more than once, use the index number:
Example
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
Named Indexes
<!--ID: 1639528994054-->


You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
Example
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
<!--ID: 1639528994073-->


Or you can use the format method.
>>> print("I just printed {0} pages to the printer {1}".format(x, printer))
>>> print("I  just printed {x} pages to the printer {printer}".format(x=7, printer="Dell"))
<!--ID: 1639528994087-->


11. Python String Formatters

Now let us see the different types of String formatters in Python:

11.1. % Operator

You can use the % operator to format a string to contain text as well as values of identifiers. Use %s where you want a value to appear. After the string, put a % operator and mention the identifiers in parameters.
>>> x=10;  printer="HP"
>>> print("I just printed %s pages to the printer %s" % (x, printer))

Output:

I just printed 10 pages to the printer HP
11.2. Format Method

The format method allows you to format a string in a similar way. At the places, you want to put values, put 0,1,2,.. in curly braces. Call the format method on the string and mention the identifiers in the parameters.
>>> print("I just printed {0} pages to the printer {1}".format(x, printer))

Output:

I just printed 10 pages to the printer HP

You can also use the method to print out identifiers that match certain values.
>>> print("I  just printed {x} pages to the printer {printer}".format(x=7, printer='HP'))

Output:

I just printed 7 pages to the printer HP
11.3. f-strings

If you use an f-string, you just need to mention the identifiers in curly braces. Also, write ‘f’ right before the string, but outside the quotes used.
>>> print(f"I just printed {x} pages to the printer {printer}")

Output:

I just printed 10 pages to the printer HP



## String Search

Search a character in a string:

Code:

def search(char,str):
    L=len(str)
    print(L)
    i = 0
    while i < L:
        if str[i]== char:
            return 1
            i = i + 1
        return -1

print(search("P","PYTHON"))

Output:

>>>
6
1
>>>

    It takes a character and finds the index where that character appears in a string.
    If the character is not found, the function returns -1.

Another example

def search(char,str):
    L=len(str)
    print(L)
    i = 0
    while i < L:
        if str[i]== char:
            return 1
            i = i + 1
        return -1

print(search("S","PYTHON"))

Output:

>>>
6
-1
>>>

[python string methods](python-string-methods.md)

  #python #strings
