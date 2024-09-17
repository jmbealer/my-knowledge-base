---
title: Python if/elif/else Statement WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-52
reference: 
description: 
aliases: 
tags: 
---
# Python if/elif/else Statement WIP

## If Statement

`if <expr>:
  <statement(s)>
elif <expr>:
  <statement(s)>
else:
  <statement(s)>`
if/elif <expr>; expression evaluated in a Boolean context.
if/elif/else <statement(s)>; valid Python statement, which must be indented.
if/elif <expr>; is True, then <statement(s)> is executed.
  (evaluates to a value that is “truthy”)
if/elif <expr>; is False, then <statement(s)> is skipped over and not executed.

(Code) Block is a group of statement(s).
if-elif-else statement is used to conditionally execute block(s) of statement(s).

if <True>:
  <run statement>
if <False>:
  <skip statement>
elif <True>:
  <if <False> run statement>
elif <False>:
  <if <False> skip statement>
else:
  <if <False> and elif <False> run statement>
<run following_statement>


if/elif <expr>; takes an Boolean expression.
if/elif <True>; then indented statement(s) are executed.
if/elif <False>; then indented statement(s) are skipped and next outdented statement(s) are executed.
if/elif <expr>; a colon(:) is required after <expr>.

if/elif (<expr>): can use parentheses without raising a syntax error.

if/elif <expr>:
<statement>; without indentation, will raise an Error

if/elif/else statement(s) are evaluated in turn and executed first True <expr>

if/elif/else <expr>; is True, then its <statement(s)> are executed, and no further elif/else statement(s) are executed.

.One-Line if Statements
if/elif/else <expr>: <statement>; one-line if statement
if/elif/else <expr>: <statement>; <statement>; <statement> one-line if statement with multiple statement(s)
multiple <statement(s)> can be separated by semicolons(;) in one-line.
<expr> if <expr> else <expr>: one-line if/elif/else statement with multiple expression(s)
  <statement(s)

.Nested if statement(s)
Nested if statement(s): if statement(s) inside if statement(s)
if <expr>:
  <statement>
    if <expr>: Nested if statement(s)
      <statement>
    else:
      <statement>
Nested if/else statement; used to check more than one conditions.

.pass Statement
if <expr>: can't be empty
if <expr>:
  pass # avoid empty if statement error
pass statement(s); performs no action
pass statement(s); placeholder when a statement is syntactically required

## Elif Statement

elif is short for else if
elif/else statement(s) are optional
elif statement(s); if the previous conditions were False, then try this condition.
elif statement(s); called a chained conditional.
elif <expr>; you can define an arbitrary number of elif statement(s)
elif <expr>; allows for continued conditions after False if/elif statement(s).

elif <False>; continue to an optional else statement.

## Else Statement

if/elif <False>: else statement executes;
if/elif <False>: if no else statement no code is executed
else statement: must be define last
else statement: can only be one
else: provides alternate code to execute if if/elif statement are False.

## Operators

And

The and keyword is a logical operator, and is used to combine conditional statements:
Example

Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

Or

The or keyword is a logical operator, and is used to combine conditional statements:
Example

Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

Python supports the usual logical conditions from mathematics:

Equals: a == b Not Equals: a != b Less than: a < b Less than or equal to: a <= b Greater than: a > b Greater than or equal to: a >= b

Use the and operator in an if statement

`#create two boolean objects`

x = False
y = True

\#The validation will be True only if all the expressions generate a value True
if x and y:
    print('Both x and y are True')
else:
    print('x is False or y is False or both x and y are False')

Output:

x is False or y is False or both x and y are False

Use the in operator in an if statement

`#create a string`
s = 'jQuery'
`#create a list`
l = ['JavaScript', 'jQuery', 'ZinoUI']

`# in operator is used to replace various expressions that use the or
operator`
if s in l:
    print(s + ' Tutorial')

`#Alternate if statement with or operator`

if s == 'JavaScript' or s == 'jQuery' or s == 'ZinoUI':
     print(s + ' Tutorial')

Output:

jQuery Tutorial
jQuery Tutorial

The Python or operator combines two Boolean expressions and evaluates to True if at least one of the expressions returns True. Otherwise, if both expressions are False, then the entire expression evaluates to False.
True or True      # Evaluates to True
True or False     # Evaluates to True
False or False    # Evaluates to False
1 < 2 or 3 < 1    # Evaluates to True
3 < 1 or 1 > 6    # Evaluates to False
1 == 1 or 1 < 2   # Evaluates to True

Equal Operator ==

The equal operator, ==, is used to compare two values, variables or expressions to determine if they are the same.

If the values being compared are the same, the operator returns True, otherwise it returns False.

The operator takes the data type into account when making the comparison, so a string value of "2" is not considered the same as a numeric value of 2.
\# Equal operator

if 'Yes' == 'Yes':
  \# evaluates to True
  print('They are equal')

if (2 > 1) == (5 < 10):
  \# evaluates to True
  print('Both expressions give the same result')

c = '2'
d = 2

if c == d:
  print('They are equal')
else:
  print('They are not equal')
Not Equals Operator !=

The Python not equals operator, !=, is used to compare two values, variables or expressions to determine if they are NOT the same. If they are NOT the same, the operator returns True. If they are the same, then it returns False.

The operator takes the data type into account when making the comparison so a value of 10 would NOT be equal to the string value "10" and the operator would return True. If expressions are used, then they are evaluated to a value of True or False before the comparison is made by the operator.
\# Not Equals Operator

if "Yes" != "No":
  \# evaluates to True
  print("They are NOT equal")

val1 = 10
val2 = 20

if val1 != val2:
  print("They are NOT equal")

if (10 > 1) != (10 > 1000):
  \# True != False
  print("They are NOT equal")
Comparison Operators

In Python, relational operators compare two values or expressions. The most common ones are:

    < less than
    > greater than
    <= less than or equal to
    >= greater than or equal too

If the relation is sound, then the entire expression will evaluate to True. If not, the expression evaluates to False.
a = 2
b = 3
a < b  # evaluates to True
a > b  # evaluates to False
a >= b # evaluates to False
a <= b # evaluates to True
a <= a # evaluates to True


and Operator

The Python and operator performs a Boolean comparison between two Boolean values, variables, or expressions. If both sides of the operator evaluate to True then the and operator returns True. If either side (or both sides) evaluates to False, then the and operator returns False. A non-Boolean value (or variable that stores a value) will always evaluate to True when used with the and operator.
True and True     # Evaluates to True
True and False    # Evaluates to False
False and False   # Evaluates to False
1 == 1 and 1 < 2  # Evaluates to True
1 < 2 and 3 < 1   # Evaluates to False
"Yes" and 100     # Evaluates to True



not Operator

The Python Boolean not operator is used in a Boolean expression in order to evaluate the expression to its inverse value. If the original expression was True, including the not operator would make the expression False, and vice versa.
not True     # Evaluates to False
not False    # Evaluates to True
1 > 2        # Evaluates to False
not 1 > 2    # Evaluates to True
1 == 1       # Evaluates to True
not 1 == 1   # Evaluates to False

Define a negative if

If a condition is true the not operator is used to reverse the logical state, then logical not operator will make it false.

`#create a integer`
x = 20
print(x)

`#uses the not operator to reverse the result of the logical expression`

if not x == 50:
    print('the value of x different from 50')
else:
    print('the value of x is equal to 50')

Output:

 20
 the value of x different from 50

Short Hand If ... Else
Example

One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

This technique is known as Ternary Operators, or Conditional Expressions.

You can also have multiple else statements on the same line:
Example

One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



## Other

Handling Exceptions in Python

A try and except block can be used to handle error in code block. Code which may raise an error can be written in the try block. During execution, if that code block raises an error, the rest of the try block will cease executing and the except code block will execute.
def check_leap_year(year):
  is_leap_year = False
  if year % 4 == 0:
    is_leap_year = True

try:
  check_leap_year(2018)
  print(is_leap_year)
  \# The variable is_leap_year is declared inside the function
except:
  print('Your code raised an error!')
or Operator




2. Python Switch Case Statement

Python does not have a simple switch case construct.

But Python does not have this. So, to get around this, we use Python’s built-in dictionary construct to implement cases and decided what to do when a case is met. We can also specify what to do when none is met.

3. Solutions for Python Switch Case Statement

One way out would be to implement an if-elif-else ladder. Rather, we can use a dictionary to map cases to their functionality. Here, we define a function week() to tell us which day a certain day of the week is. A switcher is a dictionary that performs this mapping.
>>> def week(i):
        switcher={
                0:'Sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'Saturday'
             }
         return switcher.get(i,"Invalid day of week")

Now, we make calls to week() with different values.
>>> week(2)

‘Tuesday’
>>> week(0)

‘Sunday’
>>> week(7)

‘Invalid day of week’
>>> week(4.5)

‘Invalid day of week’

As you can see, for values other than the ones we mention in the switcher, it prints out “Invalid day of week”. This is because we tell it to do so using the get() method of a dictionary.
Do you know How can Python Send Email Via SMTP Server

a. Using Python Functions & Lambdas

We can also use functions and lambdas in the dictionary.
>>> def zero():
        return 'zero'
>>> def one():
        return 'one'
>>> def indirect(i):
        switcher={
                0:zero,
                1:one,
                2:lambda:'two'
                }
        func=switcher.get(i,lambda :'Invalid')
        return func()
>>> indirect(4)

‘Invalid’
>>> indirect(2)

‘two’
>>> indirect(1)

‘one’
>>> indirect(0.5)

‘Invalid’
b. With Python Classes

Using this concept with classes lets us choose a method at runtime.
>>> class Switcher(object):
          def indirect(self,i):
                   method_name='number_'+str(i)
                   method=getattr(self,method_name,lambda :'Invalid')
                   return method()
          def number_0(self):
                   return 'zero'
          def number_1(self):
                   return 'one'
          def number_2(self):
                   return 'two'
>>> s=Switcher()
>>> s.indirect(2)

‘two’
>>> s.indirect(4)

‘Invalid’
>>> s.number_1()

‘one’

There are six basic flow controls used in Python programming:

    if
    for
    while
    break
    continue
    pass

For Statement:

The for statement supports repeated execution of a statement or block of statements that is controlled by an iterable expression.
While Statement:

The while statement in Python programming supports repeated execution of a statement or block of statements that is controlled by a conditional expression.
Break Statement:

The break statement is allowed only inside a loop body. When break executes, the loop terminates. If a loop is nested inside other loops, break terminates only the innermost nested loop.
Continue Statement:

The continue statement is allowed only inside a loop body. When continue executes, the current iteration of the loop body terminates, and execution continues with the next iteration of the loop.


