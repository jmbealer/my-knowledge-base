---
title: What Are Python Variables? WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-51
reference: 
description: 
aliases: 
tags: 
---
# What Are Python Variables? WIP

A Python variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing.
Variables are identifiers of a physical memory location, which is used to hold values temporarily during program execution.

Variables are created when first assigned.
Variables must be assigned before being referenced.
The value stored in a variable can be accessed or updated later.
The type (string, int, float etc.) of the variable is determined by Python
The interpreter allocates memory on the basis of the data type of a variable.

**Variables** are containers for storing data values.

Based on the value assigned, the interpreter decides its data type.
You can always store a different type in a variable.

No declaration required
Unlike other programming languages, Python has no command for declaring a variable.

Every variable in Python is an object.
Python is completely object oriented, and not "statically typed".
Python is a dynamically-typed language.

**Variable Syntax**
`<variable-name> = <value>`

What are **Values**?
Value is either string, numeric etc. Example : "Sara", 120, 25.36

**Deleting** Variables
You can delete a variable using the keyword `<del>`.

`<del> = <variable-name>`
`<del> <variable-name>`

## Variable Names

.Python Variable Naming Rules
A variable name can only start with a letter(A-Z/a-z) or an underscore(_).

A variable name can only contain alpha-numeric characters and underscores, such as (A-Z/a-z, 0-9, and _ ).
Can be any (reasonable) length.

A variable name cannot start with a number.

Variable names are case-sensitive (age, Age and AGE are three different variables).

Reserved words (keywords) cannot be used as variable (identifier) names.

A variable name can not contain spaces.

Good Variable Name

- Choose meaningful name instead of short name. roll_no is better than rn.
- Maintain the length of a variable name. Roll_no_of_a-student is too long?
- Be consistent; roll_no or RollNo
- Begin a variable name with an underscore(_) character for a special case.

Naming Variables

If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

## Variable Scope

The scope of a variable is that piece of code where that variable is visible or accessible.

.Variable Scope Range
Built-in Variables
Global Variables
Enclosed Variables
Local Variables

### Local Variables Scope

A local variable can be reached only within the scope where it's defined.

A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

Local variables overrides the scope of global variables.
A local variable refers to a variable declared inside a function.

.Local Variables Example:
def fun():
  x = 'This is a local variable'
  print(x)
fun()

.Function Inside Function
The local variable can be accessed from a function within the function:

def fun():
  x = 300
  def innerfun():
    print(x)
  innerfun()
fun()


### Global Variables Scope

A global variable refers to a variable declared outside a function.
Global variables are visible and accessible to the whole program.
  can used both inside and outside of a function.
  overwritten by local variables with same name.


.Global Variables Example:
x = "Global Variable"

#### `<global>` Keyword

`<global>` keyword: declares a global variable inside a function.
`<global>` keyword: also changes a global variable inside a function.

`<global>` keyword Example:
def fun():
  global x
  x = "Global Variable"
fun()

x = "Global Variable"
def fun():
  global x
  x = "Changed Global Variable"
fun()

### Enclosing Variables Scope
Enclosing Scope refers to a scope of a variable that is neither local nor global.
Enclosing Scope is also called Nonlocal.

.Enclosing Variables Example:
def fun():
  a='Local Variable for fun()'
  def innerfun():
    b='Local Variable for innerfun()'
    print(a) # Enclosing (Nonlocal) variable for innerfun()
    print(b)
  innerfun()
  print(a)

### Built-in Variables Scope

Built-in Variables have the widest scope.
Built-in Variables includes all the variables that get loaded when the interpreter starts.

#### `<nonlocal>` Keyword

`<nonlocal>` keyword: changes an enclosed variable inside a function.

`<nonlocal>` keyword example:
def fun():
  a='local variable'
  def innerfun():
    nonlocal a
    a='changed nonlocal variable'
    b='local variable'
  innerfun()
fun()

## Python Assignment Statements
.Assigning


.Legal variable names:
`myvar = "Legal"
my_var = "Legal"
_my_var = "Legal"
myVar = "Legal"
MYVAR = "Legal"
myvar2 = "Legal"`

.Illegal variable names:
2var = "Illegal"
v-ar = "Illegal"
v ar = "Illegal"


.Reassigning Variables
You can reuse variable names by simply assigning a new value to them.

.Multiple Variable Assignments

The basic assignment statement works for a single variable and a single expression.

You can assign the same value to multiple variables in one statement:

Syntax:

`<var1>=<var2>=<var3>...<varn> = <expr>`
`<var1>=<var2>=<var3>=<value>`

Example:

x = y = z = 1
x = y = z = "Orange"
age=fav=7

You can assign multiple values to multiple variables in one statement:

Syntax:

`<var>, <var>, ..., <var> = <expr>, <expr>, ..., <expr>`

Example:

x, y, z = 1, 2, "abcd"
x, y, z = "Assign", "Multiple", "Cherry"
age,city=21,'Indore'

.Swapping Variables:
Swapping variables means interchanging values.

Syntax:

`<var1>, <var2> = <var2>, <var1>`

Example:

x = 10
y = 20
x, y = y, x
a,b='red','blue'
a,b=b,a

a, b, _ = 1, 2, 3
underscore (_) conventional used as a dummy variable for unwanted values

.cascading assignment
a = b = c = 1

## Variable Casting
Variable casting is the process of converting a variable from one type to another.

.Variable Casting Syntax:
int(x) convert x to a plain integer.
int(x, base)
float(x) convert x to a floating-point number.
str(x) convert x to a string.

## Unsorted

  Multiple Assignment using commas (,) you can have multiple variables
  and values on a single line
      x, y, z = 0, 0, 0
  Constants is a variable whose value stays the same. python doesnt have built-in constant types, but programmers use all capital letters
  to indicate a variable should be treated as a constant and never be changed
      MAX_CONNECTIONS = 500

Naming files it’s best to use underscores

Variables are Labels that you can assign to values or a variable reference a certain value

  Rules and Guidelines
      Spaces are not allowed in variable names, but underscores can be used to separate words in variable names

The equal sign (=) is used to assign a value to a variable
If a variable is not “defined” (assigned a value), trying to use it will give you an error:


Although we don’t have to declare a type for Python variables, a value does have a type.
A variable is used to store data that will be used by the program. This data can be a number, a string, a Boolean, a list or some other data type. Every variable has a name which can consist of letters, numbers, and the underscore character.

The equal sign = is used to assign a value to a variable. After the initial assignment is made, the value of a variable can be updated to new values as needed.
`#` These are all valid variable names and assignment

user_name = "@sonnynomnom"
user_id = 100
verified = False

`#` A variable's value can be changed after assignment

points = 100
points = 120

  #python #variables
