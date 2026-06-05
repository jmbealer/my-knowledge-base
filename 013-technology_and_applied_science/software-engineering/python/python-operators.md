---
title: What is Python Operators WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# What is Python Operators WIP

**Operators**
: are used to perform operations on variables and values.
: In computer programming languages operators are special symbols which represent computations, conditional matching etc.
Python operators are symbols that are used to perform mathematical or logical manipulations.

**Operands**
: The values the operator uses are called operands.
Operands are the values or variables with which the operator is applied to, and values of operands can manipulate by using the operators.

c = a + b:
operands is a and b
operator is +

## Python Built-in Operators

[Arithmetic Operators](arithmetic-operators.md) `+, -, *, /, //, %, **`
[Assignment Operators](assignment-operators.md) `=, +=, -=, /=, //= etc.`
[Comparison Operators](comparison-operators.md) `==, !=, >, <, >=, <=`
[Logical Operators](logical-operators.md) `and, or, not`
[Identity Operators](identity-operators.md) `is, is not`
[Bitwise Operators](bitwise-operators.md) `&, |, ^, >>, <<, ~`
[Membership Operators](membership-operators.md) `in, not in`
[Operator Precedence](operators-precedence.md)

### 1. Python Operator Overloading

In this Python tutorial, we are going to discuss Python Operator Overloading, examples of operator overloading in python, and python magic methods with some operators: python binary operator, python comparison operator, python unary operators, and python extended assignments. In the programming world, operator overloading is also called Operator Ad-hoc Polymorphism. Indeed, it is a case of polymorphism where different operators have different implementations based on their arguments. This is either defined by the programmer, by the programming language, or both.

So, let’s start the Python Magic Methods Tutorial.
Python Operator Overloading

Python Operator Overloading and Python Magic Methods
2. What is Python Operators Overloading?

In Python, an operator lets us perform an operation/procedure on one or more operands(values). Read up on our article on Python Operators. But for now, let’s take an example.
>>> 42+1

43
Here, we performed the addition of two numbers using the addition operator. You know that we can apply this operator to Python string too. In that case, we call it the concatenation operator. Let’s discuss Python Syntax before proceeding.
>>> '42'+'1'

‘421’
>>> 'hello'+' '+'world'

‘hello world’
And then when we do this to Python list, we concatenate two lists.
>>> [1,2,3]+[4,5,6]

[1, 2, 3, 4, 5, 6]
Python does this implicitly, but what for when you want to apply this operator to your own class? Can we? Let’s give it a try.
In this python operator overloading tutorial, we take a class ‘myfloat’ to represent floating-point numbers.
>>> class myfloat:
      def __init__(self,whole,fraction):
                self.whole=whole
                self.fraction=fraction
      def shownumber(self):
                print(f"I am {self.whole}.{self.fraction}")
>>> obj1=myfloat(3,7)
>>> obj1.shownumber()
<!--ID: 1639528995388-->


I am 3.7
>>> obj2=myfloat(3,3)
>>> obj2.shownumber()

I am 3.3
Now, let’s try adding two objects.
>>> obj1+obj2

Traceback (most recent call last):

File “<pyshell#24>”, line 1, in <module> obj1+obj2

TypeError: unsupported operand type(s) for +: ‘myfloat’ and ‘myfloat’
As you can see, this raised a TypeError. But don’t fret; we can do this, we’ll discuss in a later section.
3. Python Magic Methods

We observe that python methods have double underscores before and after their names. These are special methods and are also called ‘dunders’. These help us implement functionality that a normal method can’t represent.
By now, we have come across only one magic method- __init__(). But we can, in fact, define our own magic methods to implement operator overloading in Python. With this, we can define these operators to work on our custom classes. Some of these are-
a. Python Binary Operators

__add__ for +

__sub__ for –

__mul__ for *

__truediv__ for /

__floordiv__ for //

__mod__ for %

__pow__ for **

__and__ for &

__xor__ for ^

__or__ for |

__lshift__ for <<

__rshift__ for >>

In our article on Python Methods, we discussed these.
b. Python Extended Assignments

__iadd__ for +=

__isub__ for -=

__imul__ for *=

__idiv__ for /=

__ifloordiv__ for //=

__imod__ for %=

__ipow__ for **=

__ilshift__ for <<=

__irshift__ for >>=

__iand__ for &=

__ixor__ for ^=

__ior__ for |=
c. Python Unary Operators

__neg__ for –

__pos__ for +

__abs__ for abs()

__invert__ for ~

__complex__ for complex()

__int__ for int()

__long__ for long()

__float__ for float()

__oct__ for oct()

__hex__ for hex()
d. Python Comparison Operators

__lt__ for <

__le__ for <=

__eq__ for ==

__ne__ for !=

__ge__ for >=

__gt__ for >

Read up on what we have to say about Python Variables and Python Numbers.
Others include __radd__ for reverse add.
>>> class myclass:
   def __init__(self,age):
           self.age=age
   def __add__(self,other):
           return self.age+other
   def __radd__(self,other):
           return self.age+other
>>> a=myclass(1)
>>> a+2

3
>>> 2+a

3
If the interpreter cannot add left to right, it will call  __radd__() instead. Here, radd is in reverse/reflected add.
4. Python Operator Overloading Example

To be able to add our Python objects obj1 and obj2 for class ‘myfloat’, we can do the following.
>>> class myfloat:
      def __init__(self,whole,fraction):  
           self.whole=whole
           self.fraction=fraction
      def shownumber(self):
           print(f"I am {self.whole}.{self.fraction}")
      def __add__(self,other):
           if (self.fraction+other.fraction)>9:
                return myfloat(self.whole+other.whole+1,self.fraction+other.fraction-10)            return myfloat(self.whole+other.whole,self.fraction+other.fraction)
<!--ID: 1639528995417-->


Here, we added another method __add__, that takes two parameters (‘self’ and ‘other’) for the two objects. Then, it checks if the sum of the fraction parts of both objects is greater than 9. In that case, it transfers a 10 to the ‘whole’ part as a 1. This is for the carry. It then returns an object with the sums of the whole and fraction parts of both objects. However, if the condition isn’t met, it simply returns an object with the sums.
Let’s create objects obj1 and obj2 again, and try adding them.
>>> obj1=myfloat(3,7)
>>> obj1.shownumber()

I am 3.7
>>> obj2=myfloat(3,3)
>>> obj2.shownumber()

I am 3.3
>>> result=obj1+obj2
>>> print(f"I am {result.whole}.{result.fraction}")
<!--ID: 1639528995439-->


I am 7.0
As you can see, it works absolutely fine now and lets us add two objects of class ‘myfloat’.
>>> result

<__main__.myfloat object at 0x0572FD10>

This is the resulting object of adding obj1 and obj2.

Here, the interpreter translates obj1+obj2 to obj1.__add__(obj2).
5. More Examples of Python Operator Overloading

To really understand something, once is never enough. So, let’s take another example of Operator overloading in Python.
>>> class itspower:
        def __init__(self,x):
               self.x=x
        def __pow__(self,other):
               return self.x**other.x
>>> a=itspower(2)
>>> b=itspower(10)
>>> a**b

1024
In this, we take a class ‘itspower’ and two methods __init__ and __pow__.
__pow__ takes two objects and returns the ‘x’ of first raised to the power of the ‘x’ of the second. When we type a**b, the interpreter converts it implicitly to a.__pow__(b).
Now, let’s take another example to demonstrate few more such magic methods.
>>> class Person:
      def __init__(self,name,age):
         self.name=name
         self.age=age
      def __gt__(self,other):
         if self.age>other.age:
                return True
         return False
      def __abs__(self):
         return abs(self.age)
      def __iadd__(self,other):
         return self.age+other.age
>>> Nick=Person('Nick',7)
>>> Angela=Person('Angela',5)
>>> Nick>Angela

True
>>> Kim=Person('Kim',-8)
>>> abs(Kim)

8
>>> Tom=Person('Tom',7)
>>> Mikayla=Person('Mikayla',3)
>>> Tom+=Mikayla
>>> Tom

10
To leave this lesson on an engaging note, we would just like to leave this code here:
>>> '1'.__add__('1')

’11’
>>> 1.__add__(1)

SyntaxError: invalid syntax
>>> [1,2,3].__add__([4,5,6])

[1, 2, 3, 4, 5, 6]


1. Objective – Ternary Operator in Python

Today, we will see Python Ternary Operator. Moreover, we will discuss the example and syntax of Ternary Operator in Python. Also, we will learn before and nested Python Ternary Operators. At last, we will discuss ways for implementing Ternary operators in Python.
So, let’s start Python Ternary Operator.
Python Ternary Operator - Implementation With Example

Python Ternary Operator – Implementation With Example
2. Python Ternary Operator Example

Ternary operators in Python are terse conditional expressions. These are operators that test a condition and based on that, evaluate a value. This was made available since PEP 308 was approved and is available ever since version 2.4. This operator, if used properly, can reduce code size and enhance readability.
Do you know about Python Comparison Operator
a. Python if-else code

Let’s write code to compare two integers.
>>> a,b=2,3
>>> if a>b:
        print("a")
else:
        print("b")

b
b. Equivalent code with Ternary operator

So let’s try doing the same with ternary operators:
>>> a,b=2,3
>>> print("a" if a>b else "b")

b
Voila! Done in one line. Python first evaluates the condition. If true, it evaluates the first expression; otherwise, it evaluates the second. There is a lazy evaluation. It also evaluates the conditions left to right.
You must learn about Python Data Structures
3. The syntax for Python Ternary Operator

Now, let’s learn a little the syntax for Python Ternary Operator.
[on_true] if [expression] else [on_false]

In C++, it looks like this:
max=(a>b)?a:b

But this isn’t quite Pythonic, so Guido, Python’s BDFL (a status from which he has resigned permanently), rejected it. Another reason for the veto is that we already have many uses for the colon(:).
One more example of Python ternary Operators:
>>> from random import random
>>> a,b=random(),random()
>>> res="a" if a>b else "b"
>>> res

‘b’
>>> a,b

(0.009415785735741311, 0.9675879478005226)
4. Ways to Implement Ternary Operator

Below, we are discussing different ways of implementing Python Ternary Operator:
Python Ternary Operator

Ways to Implement Ternary Operator
a. Using Python Tuples

We can use tuples to specify what to do if the condition is True/False.
Before moving on, you must learn a little about Python Tuples
>>> a,b=random(),random()
>>> (b,a)[a>b]

0.8182650892806171
This is equivalent to:
>>> (b,a)[True]

But we’re confused which this is- a or b. Let’s try tweaking this.
>>> (f"b:{b}",f"a:{a}")[a>b]
<!--ID: 1639528995461-->


‘b:0.8182650892806171’
That’s more like it. Looking at the code, you’ll reckon the first argument in the tuple corresponds to a Boolean value of False; the second- True. This is because of False=0 and True=1. The condition resides within the [ ].
Note that this method evaluates both elements of the tuple, and hence is less efficient. This happens because it must first build the tuple before it can look for an index.
>>> condition=True
>>> 2 if condition else 1/0    \#Follows the normal if-else logic tree

2
>>> (1/0,2)[condition]

Traceback (most recent call last):
 File “<pyshell#48>”, line 1, in <module>
   (1/0,2)[condition]
ZeroDivisionError: division by zero
b. Using Python Dictionaries

Likewise, we can make this happen using dictionaries with the same logic.
You must read about Python Dictionaries
>>> a,b=random(),random()
>>> {False:f"b:{b}",True:f"a:{a}"}[a>b]
<!--ID: 1639528995483-->


‘a:0.37237928632774675’
Since we specify what to do when here, we can interchange the positions of key-value pairs.
>>> {True:f"a:{a}",False:f"b:{b}"}[a>b]
<!--ID: 1639528995505-->


‘a:0.37237928632774675’
c. Using Lambdas

We can also make use of Python Lambda Functions to act as a ternary operator.
>>> (lambda :f"b:{b}",lambda :f"a:{a}")[a>b]()
<!--ID: 1639528995521-->


‘b:0.5955717855531699’
5. Nested Python Ternary Operator

Let’s try chaining these operators, shall we?
>>> a=random()
>>> "Less than zero" if a<0 else "Between 0 and 1" if a>=0 and a<=1 else "Greater than one"

‘Between 0 and 1’
Have a look at Python Closure
>>> a

0.8537574133103878
Here, we check for the value of a. If it falls shorter than 0, we print “Less than zero”; if between 0 and 1, we print “Between 0 and 1”. Else, we print “Greater than one”. Notice how we nested them.
6. Before Ternary Operators in Python

Before this was a thing with Python, this is what we did (we used a common idiom):
>>> a,b=2,3
>>> a<b and a or b

2
So how does this work? Let’s see.

    a is 2 and b is 3
    It checks if a<b
    If true, it gives us True and a or b
    This gives us a or b
    It checks a
    If false, it gives us False or b
    This gives us b

This method, however, doesn’t work for a=0. This is because that would be True and 0 or b, which is True and False or b, which is False or b, which is b. Oops!
Now why don’t you try formulating an expression for a>b and try explaining it to yourself?
Let’s learn about Python Data Science
It could also be beneficial to use the and/or logic when one of our expressions is the same as the condition:
>>> def sayhello(): print('Hello')
>>> sayhello() if sayhello() else 'Bye'

Hello
Hello
True
>>> sayhello() or 'Bye'

Hello
True

Operation priority
parentheses
power
unary minus
multiplication, division, and remainder
addition and subtraction

Python has a logical operator and. The and operator takes two boolean values, and returns True if both values are True.

Consider a and b:

    a is checked if it is True or False.
    If a is False, False is returned.
    b is checked if it is True or False.
    If b is False, False is returned.
    Otherwise, True is returned (as both a and b are therefore True ).

The and operator will only return True for True and True.

Make a function using the and operator.

Here, *= is an in-place assignment operator.
operator precedence

  #python #operators
