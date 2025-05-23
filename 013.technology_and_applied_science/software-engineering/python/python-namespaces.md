---
title: Python-namespaces
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
# Python-namespaces
== Python Namespaces WIP

Python Namespace

In this Python Tutorial, we discuss Python Namespace, Types of Namespace in python and Python Variable Scope, with their examples and python Syntax.
Python Namespace and Variable Scope - Local and Global Variables

Python Namespace and Variable Scope – Local and Global Variables

Try this: type ‘import this’ in the interpreter.
>>> import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one– and preferably only one –obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea — let’s do more of those!
2. What is Python Name?

Before we move on to namespaces in python, let’s talk about names in python. A Python name is an identifier- something we use to access a Python object and in Python, everything’s an object.

We’ll take an example.
>>> rank=1

Here, ‘rank’ is the name associated with the Python object 1. To get this object’s address in RAM, we use the id() function.
>>> id(rank)

492979856
>>> id(1)

492979856

To take a slightly more complex example, we store 2 in a name ‘a’. Then, we increment it by 1 and associate the name ‘b’ to the object 2. We keep checking the id as we go.
>>> a=2
>>> id(a)

492979872
>>> a+=1
>>> id(a)

492979888
>>> b=2
>>> id(b)

492979872
>>>
>>> id(2)

492979872
>>> id(3)

492979888

So what’s actually happening? We’ll illustrate.
Java Namespace - Python Name

Java Namespace – Python Name

As you can see, when we set ‘a’ to 3 and set ‘b’ to 2, ‘b’ starts pointing to the object ‘a’ once pointed to. Isn’t that quite efficient? It does not have to create another object to hold 2 for b. This dynamic name binding is powerful.

Also, a name can hold any kind of value.
>>> a=1
>>> a='one'

Finally, since everything is an object, so are Python functions. Consequently, you can associate them with names.
>>> identity=id
>>> identity(2)

492979872

Here, we associate the name ‘identity’ with the built-in function id().

Bonus Question- Check the following code and figure out what’s happening.
>>> def sayhello(): print('Hello')
>>> hi=sayhello()

Hello
>>> hi
>>> type(hi)

<class ‘NoneType’>

Well, since the function does not return anything, we get an object of class ‘NoneType’. Of course, None is an object that indicates no value. Did function sayhello() return a value, things would be different. Let’s take another example.
>>> def func1():
                print("Hi")
                return 1
>>> func2=func1()

Hi
>>> func2

1
>>> type(func2)

<class ‘int’>
3. What is Python Namespaces?

A namespace in python is a collection of names. So, a namespace is essentially a mapping of names to corresponding objects. At any instant, different python namespaces can coexist completely isolated- the isolation ensures that there are no name collisions. Simply speaking, two namespaces in python can have the same name without facing any problem. A namespace is implemented as a Python dictionary.

When we start the interpreter, a python namespace is created for as long as we don’t exist. This holds all built-in names. It is due to this that python functions like print() and id() are always available. Also, each module creates its own global namespace in python.

When you call a function, a local python namespace is created for all the names in it. A module has a global namespace. The built-in namespace encloses this. Take a look at the following figure to get a clearer understanding.
Types of Python Namespace

Types of Python Namespace
4. What is Python Variable Scope?

Through various python namespaces, not each can be accessed from every part of the program. A namespace is in variable scope in a part of a program, if it lets you access the python namespace without having to use a prefix.

At any instant, we have at least three nested python scopes:

    Current function’s variable scope- has local names
    Module’s variable scope- has global names
    The outermost variable scope- has built-in names

This in accordance with the three kinds of namespaces in python, we just discussed. This also decides the order of searching for when a reference is made. The order is- the local Python namespace, the global namespace, the built-in namespace. Also, a nested function creates a nested variable scope inside the outer function’s scope.
5. Few Python Namespace Example

To further what we said, let’s take an example.
>>> a=1
>>> def func1():
                b=2
                def func2():
                                c=3

In this code, ‘a’ is in the global namespace in python. ‘b’ is in the local namespace of func1, and ‘c’ is in the nested local python namespace of func2.

To func2, ‘c’ is local, ‘b’ is nonlocal, and ‘a’ is global. By nonlocal, we mean it isn’t global, but isn’t local either. Of course, here, you can write ‘c’, and read both ‘b’ and ‘c’. But you can’t access ‘a’, that would create a new local variable ‘a’. See this example,
>>> a=1
>>> def func1():
                b=2
                def func3():
                                a=2
                                b=3
                                c=3
                                print(f"a={a}, b={b}, c={c}")
                func3()
                print(f"b={b}")
>>> func1()
a=2, b=3, c=3
b=2
>>> a
<!--ID: 1639528995548-->


1
To deal with this situation, we can use the ‘global’ and ‘nonlocal’ keywords.
>>> a=1
>>> def func1():
                b=2
                def func3():
                                global a
                                a=2
                                nonlocal b
                                b=3
                                c=3
                                print(f"a={a}, b={b}, c={c}")
                func3()
                print(f"b={b}")
>>> func1()
a=2, b=3, c=3
b=3
>>> a
<!--ID: 1639528995570-->


2



