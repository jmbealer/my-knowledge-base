---
title: Operator Precedence
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-03
reference: 
description: 
aliases: 
tags: 
---
# Operator Precedence

Operator precedence determines how operators are parsed concerning each other. The following table summarizes the operator precedence in Python, from lowest precedence (least binding) to highest precedence (most binding). Operators in the same box have the same precedence. Unless the syntax is explicitly given, operators are binary. Operators in the same box group left to right (except for exponentiation, which groups from right to left).

Note: Comparisons, membership tests, and identity tests, all have the same precedence and have a left-to-right chaining feature as described in the Comparisons section.
Operator Name 	Description
:= 	Assignment expression
lambda 	Lambda expression
if – else 	Conditional expression
or 	Boolean OR
and 	Boolean AND
not x 	Boolean NOT
in, not in, is, is not, <, <=, >, >=, !=, == 	Comparisons, including membership tests and identity tests
| 	Bitwise OR
^ 	Bitwise XOR
& 	Bitwise AND
<<, >> 	Shifts
+, - 	Addition and subtraction
*, @, /, //, % 	Multiplication, matrix multiplication, division, floor division, remainder
+x, -x, ~x 	Positive, negative, bitwise NOT
** 	Exponentiation
await x 	Await expression
x[index], x[index:index], x(arguments...), x.attribute 	Subscription, slicing, call, attribute reference
(expressions...),[expressions...], {key: value...}, {expressions...} 	Binding or parenthesized expression, list display, dictionary display, set display
<!--ID: 1639528996527-->


1. Objective

In our last Python tutorial, we discussed Python sys Module. Today, we will see Python Operator Precedence. Given an expression of multiple operators, how do you go about it? What is 2+3*4%5-1? 13 or 3? To answer such questions, you will need to know what comes first. In this Python Operator Precedence tutorial, we address this issue. Moreover, we will learn PEMDAS and short-circuiting in python. At last, we will discuss the associativity of Python Operators.
So, let’s start the Python Operator Precedence tutorial.
Python Operator Precedence - PEMDAS & Short Circuiting

Python Operator Precedence – PEMDAS & Short Circuiting

First, let’s revise a little about Python Operators.
2. Python Operator Precedence Table

Take a look at the following table of Python Operator Precedence:
Operator 	Description
()                    (Highest precedence) 	Parentheses (grouping)
f(args…) 	Function call
(expressions…), [expressions…], {key: value…}, {expressions…} 	Binding or tuple display, list display, dictionary display, set display
x[index], x[index:index], x(arguments), x.attribute 	Subscription, slicing, call, attribute reference
await x 	Await expression
** 	Exponentiation
+x, –x, ~x 	Positive, negative, bitwise NOT
*, @, /, //, % 	Multiplication, division, remainder
+, – 	Addition, subtraction
<<, >> 	Bitwise shifts
& 	Bitwise AND
^ 	Bitwise XOR
| 	Bitwise OR
in, not in, is, is not, <, <=,  >, >=,
<>, !=, == 	Comparisons, membership, identity
not x 	Boolean NOT
and 	Boolean AND
or 	Boolean OR
if- else 	Conditional expression
lambda                  (Lowest precedence) 	Lambda expression
<!--ID: 1639528996557-->


In here, the operators in one cell evaluate left to right and exponentiation groups right to left. The lowest Precedence in Python Operator is the least binding and the highest Precedence in Python Operator is the most. It is also true that we observe the same precedence for comparisons, membership tests, and identity tests. These also have a left-to-right chaining feature.\
Have a look at Python Syntax and Semantics
3. What is Python Expression?

Before we can tell you about which operator comes first, you’d want to be introduced to expressions. An expression is a combination of values, variables, operators, and function calls. Notably, the Python interpreter can evaluate a valid expression. Why don’t we take an example?
>>> 4+3

7
4+3 is an expression with one operator. We can also put in more than one. The precedence rules show us the way to follow an order. The divisionn has a higher precedence than addition.
You must read about Python Statements
>>> 3+3/3

4.0
When we use parentheses, however, we can alter the order of execution here.
>>> (3+3)/3

2.0
What we conclude here is that using parentheses, we can force the operators of lower precedence to run first. Or we can say that when two operators share an operand, the one with the higher precedence gets to go first.
4. Python Operator Precedence – PEMDAS

If you’re on this page reading about Python, you sure have heard about BODMAS somewhere in your journey so far (mathematics, school). In Python, however, we come across PEMDAS:
Parentheses
Exponentiation
Multiplication
Division
Addition
Subtraction
Let’s revise Python Iterables
A mnemonic to remember that will be “Please Excuse My Dear Aunt Susie”.
Let’s take an example.
>>> ((((13+5)*2)-4)/2)-13

3.0
How did that happen? Let’s work it out.
13+5 gives us 18
18*2 gives us 36
36-4 gives us 32
32/2 gives us 16.0 \#Note that division gives us floats!
16-13 gives us 3.0
5. Python Operator Precedence – Short Circuiting

Python always evaluates the left operand before the right- even in function arguments. For expressions with and or operations, it uses short-circuiting. This means it evaluates the second operand only until it is needed. Because of this, such statements can work reliably:
Python Operator Precedence - Short Circuiting

Python Operator Precedence – Short Circuiting

Do you know about Python Closure
>>> if(s!=None) and (len(s)<10): pass

To short-circuit is to stop executing the Boolean operation if we have already arrived at the truth value of the expression. Let’s take a look at this:

    X or Y- Evaluates Y only if X is false; otherwise, returns X
    X and Y- Evaluates Y only if X is true; otherwise, returns X

a. Short Circuiting with and/or

See what this gives us:
>>> 0 or "Hello" and 1

1
This doesn’t give us “Hello”, but 1, because:
0 or “Hello” gives us “Hello”
“Hello” and 1 gives us 1
Let’s discuss the Python Multiple Inheritance
b. Short-Circuiting with all()/any()

This also works with the all() and any() functions.
>>> def check(i):
      return i
>>> all(check(i) for i in [1,1,0,0,3])

False
This stops at the first False it gets (the 0 at the third position) and returns False.
>>> any(check(i) for i in [0,0,0,1,3])

True
This stops at the first True it gets (the 1 at the fourth position) and returns True.
c. Short Circuiting with Conditional Operators

Watch how this unfurls with conditional operators like > and <.
Have a look at Python Bitwise Operator
>>> 7>8>check(4)

False
This stops at 7>8 and returns False.
d. Short-Circuiting with Ternary Operators

Now, consider the following expression which is a ternary operator:
>>> print("One") if print("Two") else print("Three")

Two
Three
What happens here? Let’s find out.
Python first checks the condition print(“Two”). In evaluating this, it prints “Two”. Also, the Boolean value for this is False:
>>> bool(print("Two"))

Two
False
Since it is False, it does not evaluate print(“One”) and simply evaluates print(“Three”).
Hence, the final output we get is:
Two
Three
Let’s take a tour to Python Sets and Booleans
6. Associativity of Operators in Python

In that table above, many cells had more than one operator. These share precedence. So then, which to evaluate first? Associativity comes to the rescue here. Many operators have left-to-right associativity.
a. Associative Operators

    Multiplication (*) and Floor Division (//)

For an example, let’s consider the operators multiplication(*) and floor division(//). Watch how the left operand evaluates first:
>>> 3*5//4

3
>>> 3*(5//4)

3
While both give us the same result, they do that in different ways. Watch how:
For the first example:
3*5 gives us 15
15//4 gives us 3
For the second example:
5//4 gives us 1
3*1 gives us 3

    Exponentiation (**)

Now, let’s try this on exponentiation:
>>> (2**3)**2

64
You must read Python about Python Functions
And now without parentheses:
>>> 2**3**2

512
This is because this is equivalent to:
2**(3**2)
This gives us 2**9
This gives us 512
b. Non-Associative Operators

Assignment and comparison operators are not associative. What this means is that x<y<z is none of the following:
(x<y)<z
x<(y<z)
This expression is actually equivalent to (and this evaluates left-to-right):
x<y and y<z

  Operations uses the order of operations
      addition (+)
      subtraction (-)
      multiplication (*)
      division (/)
      exponents (**)




