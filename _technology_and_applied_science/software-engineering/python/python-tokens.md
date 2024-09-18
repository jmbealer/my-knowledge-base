---
title: Python Tokens
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# Python Tokens

Tokens are very basic components of the source code.
Tokens are the smallest unit in a program.

## Keyword
Keywords are special reserve words


and 	def 	False 	import 	not 	True
as 	del 	finally 	in 	or 	try
assert 	elif 	for 	is 	pass 	while
break 	else 	from 	lambda 	print 	with
class 	except 	global 	None 	raise 	yield
continue 	exec 	if 	nonlocal 	return


## Identifiers
Identifiers are names used to identify a variable, function, class, object, name, and so on in a program.

.identifier naming rules:
Special characters are not allowed.
Keywords are not allowed as identifiers.
Name and name are two different identifiers, because Python is case-sensitive.
The rest of the identifier may contain letters(A-Z/a-z), underscores(_), and numbers(0-9).
Must start with letters(A-Z/a-z) or underscores.
Class names start with an uppercase letter.
All other identifiers start with a lowercase letter.

Starting an identifier with a single leading underscore indicates a private identifier.
Starting an identifier with two leading underscores indicates a strongly private identifier.
If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

Apart from these rules, there are a few naming conventions that you should follow while using this Python syntax:

  Use uppercase initials for class names, lowercase for all others.
  Name a private identifier with a leading underscore `( _username)`
  Name a strongly private identifier with two leading underscores `( __password)`
  Special identifiers by Python end with two leading underscores.

2. Ways to Define Identifiers in Python

We can define identifiers in Python in a few ways:
“An identifier is a user-defined name to represent a variable, a function, a class, a module, or any other object.”
“It is a programmable entity in Python- one with a name.”
“It is a name given to the fundamental building blocks in a program.”

3. Python Identifier Naming Rules
a. Rules in Identifiers in Python

So we know what a Python Identifier is. But can we name it anything? Or do certain rules apply? Well, we do have five rules to follow when naming identifiers in Python:
a. A Python identifier can be a combination of lowercase/ uppercase letters, digits, or an underscore. The following characters are valid:

  Lowercase letters (a to z)
  Uppercase letters (A to Z)
  Digits (0 to 9)
  Underscore (_)

Have a look at Python Number Types
Some valid names are:

  myVar
  var_3
  this_works_too

b. An identifier cannot begin with a digit.
Some valid names:

  \_9lives
  lives9

An invalid name:

  9lives

Identifiers in Python

Identifiers in Python – Naming Rules

c. We cannot use special symbols in the identifier name. Some of these are:
!
@
#
$
%
.

Identifiers in Python – Naming Rules in Python

d. We cannot use a keyword as an identifier. Keywords are reserved names in Python and using one of those as a name for an identifier will result in a SyntaxError.

Naming Rules in Python Identifiers

e. An identifier can be as long as you want. According to the docs, you can have an identifier of infinite length. However, the PEP-8 standard sets a rule that you should limit all lines to a maximum of 79 characters.
Do you know about Python Variables

b. Lexical Definitions in Python Identifiers

To sum those rules up lexically, we can say:
`identifier ::= (letter | “_”) (letter | digit | “_”)*    #It has to begin with a letter or an underscore; letters, digits, or/and underscores may follow
letter ::= lowercase | uppercase #Anything from a-z and from A-Z
lowercase ::= “a” … “z” #Lowercase letters a to z
uppercase ::= “A” … “Z” #Uppercase letters A to Z
digit ::= “0” … “9” #Integers 0 to 9`

4. Best Practices in Identifiers in Python

While it’s mandatory to follow the rules, it is also good to follow some recommended practices:

  Begin class names with an uppercase letter, begin all other identifiers with a lowercase letter
  Begin private identifiers with an underscore (_); Note that this doesn’t make a variable private, but discourages the user from attempting to access it
  Put __ around names of magic methods (use leading and trailing double underscores), avoid doing this to anything else. Also, built-in types already use this notation.
  Use leading double underscores only when dealing with mangling.

Let’s discuss Python Iterator

  Prefer using names longer than one character- index=1 is better than i=1
  Use underscores to combine words in an identifier, like in this_is_an_identifier
  Since Python is case-sensitive, name and Name are two different identifiers.
  Use camel case for naming. Let’s just clear the air here by saying camel case is myVarOne and Pascal case is MyVarOne.

5. Testing the Validity of Identifiers in Python

While it is great to follow the rules and guidelines, we can test an identifier’s validity just to be sure. For this, we make use of the keyword.iskeyword() function.
Have a look at Python Network Programming
The keyword module lets us determine whether a string is a keyword. It has two functions:

  keyword.iskeyword(s)- If s is a Python keyword, return true
  Keyword.kwlist- Return a sequence holding all keywords the interpreter understands. This includes even those that are active only when certain __future__ statements are in effect.

Coming back to iskeyword(s), it returns True if the string s is a reserved keyword. Else, it returns False. Let’s import this module.
>>> import keyword
>>> keyword.iskeyword('_$$_')

False
>>> keyword.iskeyword('return')

True
Also, the str.isidentifier() function will tell us if a string is a valid identifier. This is available since Python 3.0.
>>> '__$$__'.isidentifier()

False
>>> '__99__'.isidentifier()

True
>>> '9lives'.isidentifier()

False
>>> '9.5okay'.isidentifier()

False
Let’s discuss Python Flask
6. Reserved Classes of Python Identifiers

Finally, let us talk about classes of identifiers. Some classes have special meanings and to identify them, we use patterns of leading and trailing underscores:
a. Single Leading Underscore (_*)

We use this identifier to store the result of the last evaluation in the interactive interpreter. This result is stored in the __builtin__ module. Importing a module as from module import * does not import such private variables.
b. Leading and Trailing Double Underscores (__*__)

These are system-defined names (by the interpreter). A class can implement operations to be invoked by special syntax using methods with special names. Consider this an attempt at operator overloading in a Pythonic fashion. One such special/ magic method is __getitem__(). Then, x[i] is equivalent to x.__getitem__(i). In the near future, the set of names of this class by Python may be extended.
Have a look at Python SciPy Tutorial
c. Leading Double Underscores (__*)

These are class-private names. Within a class definition, the interpreter rewrites (mangles) such a name to avoid name clashes between the private attributes of base and derived classes.



## Literals
Literals are the data given in a variable or constant.

Basic types of literals are:
String Literals
Numeric Literals
Boolean Literals
Special Literals
  NONE: specifies that a field is not created.

## Operators
  Symbols that operate on data and produce results

## Delimiters
delimiters are symbols that preform three special roles in Python: grouping,
punctuation, and assignment/binding of objects to names.

Grouping: (  ) [  ] {  }
Punctuation: . , : ; @
Arithmetic Assignment/Binding: = += -= /= //= %= **=
Bit-wise Assignment/Binding: &= |= ^= <<= >>=
<!--ID: 1639528993659-->


## Python Character Set

Letters: A-Z, a-z
Digits: 0-9
Special Symbols: available over keyboard
Whitespace: blank space, tab, carriage return, newline, form feed
Other Characters: Unicode

## Unsorted
5. Python Tokens: Keywords

    Python keywords are special reserve keywords
    Convey a special meaning to the compiler/interpreter
    Each keywords have a special meaning and a specific operation
    Keywords CANNOT be used as variable

6. Python Tokens: Identifiers

    Identifiers are the name to identify a variable, function, class or an object
    RULES defined for naming an identifiers:
        No special character except underscore (_) can be used as an identifier
        Keywords should not be used as an identifiers
        Python is case sensitive, i.e. Var and var are two different identifier
        First character of an identifier can be character, underscore(_) but not digit.

7. Python Tokens: Literals

Literals are data given in a variable or constant

    String Literals
        Formed by enclosing a text in the quotes
        Both single and double quotes can be used
    Numeric Literals
        Int | long | Float | Complex
    Boolean Literals
        Can have only two values: True | False
    Special Literals
        Python has one special literal: None
        Used to specify to the field that is not created

8. Python Tokens: Operators

    Arithmetic Operator
    Assignment Operator
    Comparison Operator
    Logical Operator
    Bitwise Operator
    Identity Operator
    Membership Operator

  #python #tokens
