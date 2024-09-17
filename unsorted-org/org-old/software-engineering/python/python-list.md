---
title: Lists WIP
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-52
reference: 
description: 
aliases: 
tags: 
---
# Lists WIP

: is a **sequence of values**.
: similar to an **array** in other programming languages but more **versatile**
: **values** are called **items or elements**
: are **ordered**; lists remember the order of items inserted.
: accessed by index; items in a list can be accessed using an index.
: can contain any sort of object; number, string, tuples, and other lists.
: are **changeable** (mutable)
  : change a list in-place, add new items, and delete or update existing items.

Lists are mutable ordered collection of arbitrary objects(elements).
Lists can contain any arbitrary object(elements).
A list without any elements (objects) is called an empty list: <list>=[]
Lt the current windowqists are similar to arrays.
Lists are ordered and changeable.
List allow duplicate elements(objects).
Lists are zero-indexed.

Lists are mutable dynamic arrays(sequences); You can change its content once created
List typically use to store collections of homogeneous elements(objects).
  where the precise degree of similarity will vary by application.

List are elements(objects) separated by commas and enclosed in square brackets.
`<list> = [<element>, <element>]`

List-Mutable: list allows elements to be added or removed dynamically.
List-Mutable: list will automatically adjust the backing store that holds these elements by allocation or releasing memory.
Lists can hold arbitrary elements(objects).
  Everything is an object in Python, including functions.
Can store different data types in a single list
List elements can be accessed by index
Lists can be nested to arbitrary depth

List can even contain complex objects, like functions, classes, and modules.
A list with a single object is sometimes referred to as a singleton list.

matrix is a list with two dimension:
`<list> = [[<element>, <element>],[<element>, <element>]]`
Lists can hold mix data types.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

## Declare

Create a List:
`<list> = [<elements>,<elements>]`

.Lists may be declared in several ways:
Using a pair of square brackets to denote the empty list: []
Using square brackets, separating elements with commas: [a], [a, b, c]
Using a list comprehension: [x for x in iterable]
Using the type constructor: list() or list(iterable)

A list without any element is called an empty list.
`<list> = []`

To build a list, just put some expressions in square brackets. The syntax is:

lst2 = [expression1 , …. , expression_N]

3. How to Create Python List?

A Python list may hold different types of values.
>>> days=['Monday','Tuesday','Wednesday',4,5,6,7.0]

A list may have python list.
>>> languages=[['English'],['Gujarati'],['Hindi'],'Romanian','Spanish']
>>> languages

[[‘English’], [‘Gujarati’], [‘Hindi’], ‘Romanian’, ‘Spanish’]

A list may also contain tuples or so.
>>> languages=[('English','Albanian'),'Gujarati','Hindi','Romanian','Spanish']
>>> languages[0]

(‘English’, ‘Romanian’)
>>> type(languages[0])

<class ‘tuple’>
>>> languages[0][0]='Albanian'

Traceback (most recent call last):

File “<pyshell#24>”, line 1, in <module>

languages[0][0]=’Albanian’

TypeError: ‘tuple’ object does not support item assignment

numbers = [1, 2, 3, 4, 10]
names = ['Jenny', 'Sam', 'Alexis']
mixed = ['Jenny', 1, 2]
list_of_lists = [['a', 1], ['b', 2]]


## Index
.List indices
List indices work the same way as string indices,
list indices start at 0.
color_list=["RED", "Blue", "Green", "Black"]
Item 	RED 	Blue 	Green 	Black
Index (from left) 	 0 	 1 	 2 	 3
Index (from right) 	-4 	-3 	-2 	-1

If index value is out of range, Python returns an error

List indices

List indices work the same way as string indices, list indices start at 0. If an index has a positive value it counts from the beginning and similarly it counts backward if the index has a negative value. As positive integers are used to index from the left end and negative integers are used to index from the right end, so every item of a list gives two alternatives indices. Let create a list called color_list with four items.
color_list=["RED", "Blue", "Green", "Black"]
Item 	RED 	Blue 	Green 	Black
Index (from left) 	 0 	 1 	 2 	 3
Index (from right) 	-4 	-3 	-2 	-1

If you give any index value which is out of range then interpreter creates an error message. See the following statements.

>>> color_list=["Red", "Blue", "Green", "Black"] \# The list have four elements
indices start at 0 and end at 3
>>> color_list[0] \# Return the First Element
'Red'
>>> print(color_list[0],color_list[3]) \# Print First and Last Elements
Red Black
>>> color_list[-1] \# Return Last Element
'Black'
>>> print(color_list[4]) \# Creates Error as the indices is out of range
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>

List Indices

Python list elements are ordered by index, a number referring to their placement in the list. List indices start at 0 and increment by one.

To access a list element by index, square bracket notation is used: list[index].
berries = ["blueberry", "cranberry", "raspberry"]

berries[0]   \# "blueberry"
berries[2]   \# "raspberry"
Negative List Indices

Negative indices for lists in Python can be used to reference elements in relation to the end of a list. This can be used to access single list elements or as part of defining a list range. For instance:

    To select the last element, my_list[-1].
    To select the last three elements, my_list[-3:].
    To select everything except the last two elements, my_list[:-2].

soups = ['minestrone', 'lentil', 'pho', 'laksa']
soups[-1]   \# 'laksa'
soups[-3:]  \# 'lentil', 'pho', 'laksa'
soups[:-2]  \# 'minestrone', 'lentil'
Zero-Indexing

In Python, list index begins at zero and ends at the length of the list minus one. For example, in this list, 'Andy' is found at index 2.
names = ['Roger', 'Rafael', 'Andy', 'Novak']

List Item Ranges Including First or Last Item

In Python, when selecting a range of list items, if the first item to be selected is at index 0, no index needs to be specified before the :. Similarly, if the last item selected is the last item in the list, no index needs to be specified after the :.
items = [1, 2, 3, 4, 5, 6]

`# All items from index `0` to `3``
print(items[:4])

`# All items from index `2` to the last item, inclusive`
print(items[2:])


List apply the standard interface sequence in which len(L) returns the number of items present in the list, and L[i] represents the item at index i. Also L[i:j] returns new list containing objects within 'i' and 'j'.

lst1 = ['computersc', 'IT', 'CSE'];
lst2 = [1993, 2016];
lst3 = [2, 4, 6, "g", "k", "s"];

print ("lst1[0]", lst1[0])
print ("lst3[2:4]", lst3[2:4])

lst1[0] computersc
lst3[2:4] [6, 'g']

How can I get the index of an element contained in the list?

>>> listy = list("HELLO WORLD")
>>> print(listy)
['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
>>> index = listy.index("L")	\#get index of the first item whose value is passed as parameter
>>> print(index)
2
>>> index = listy.index("L", 4)	\#define the index from which you want to search
>>> print(index)
9
>>> index = listy.index("O", 3, 5)	\#define the segment of the list to be searched
>>> print(index)
4
>>>

Copy

How to use the double colon [ : : ]?

>>> listx=[1, 5, 7, 3, 2, 4, 6]
>>> print(listx)
[1, 5, 7, 3, 2, 4, 6]
>>> sublist=listx[2:7:2] \#list[start:stop:step], \#step specify an increment
between the elements to cut of the list.
>>> print(sublist)
[7, 2, 6]
>>> sublist=listx[::3] \#returns a list with a jump every 2 times.
<!--ID: 1639528995593-->

>>> print(sublist)
[1, 3, 6]
>>> sublist=listx[6:2:-2] \#when step is negative the jump is made back
>>> print(sublist)
[6, 2]
>>>

Copy

== Slice
.List Slices
Lists can be sliced like strings and other sequences. The syntax of list slices is easy :
sliced_list = List_Name[startIndex:endIndex]
This refers to the items of a list starting at index startIndex and stopping just before index endIndex. The default values for list are 0 (startIndex) and the end (endIndex) of the list. If you omit both indices, the slice makes a copy of the original list. See the following statements.

3.1. Slicing a List

You can slice a list the way you’d slice a string- with the slicing operator.
>>> days[1:3]

[‘Tuesday’, 3]

Indexing for a list begins with 0, like for a string. A Python doesn’t have arrays.

5. Slicing a Python List

When you want only a part of a Python list, you can use the slicing operator [].
>>> indices=['zero','one','two','three','four','five']
>>> indices[2:4]

[‘two’, ‘three’]

This returns items from index 2 to index 4-1 (i.e., 3)
>>> indices[:4]

[‘zero’, ‘one’, ‘two’, ‘three’]

This returns items from the beginning of the list to index 3.
>>> indices[4:]

[‘four’, ‘five’]

It returns items from index 4 to the end of the list in Python.
>>> indices[:]

[‘zero’, ‘one’, ‘two’, ‘three’, ‘four’, ‘five’]

This returns the whole list.

    Negative indices- The indices we mention can be negative as well. A negative index means traversal from the end of the list.

>>> indices[:-2]

[‘zero’, ‘one’, ‘two’, ‘three’]

This returns item from the list’s beginning to two items from the end.
>>> indices[1:-2]

[‘one’, ‘two’, ‘three’]

It returns items from the item at index 1 to two items from the end.
>>> indices[-2:-1]

[‘four’]

This returns items from two from the end to one from the end.
>>> indices[-1:-2]

[]
This returns an empty Python list, because the start is ahead of the stop for the traversal.

List Slicing

A slice, or sub-list of Python list elements can be selected from a list using a colon-separated starting and ending point.

The syntax pattern is myList[START_NUMBER:END_NUMBER]. The slice will include the START_NUMBER index, and everything until but excluding the END_NUMBER item.

When slicing a list, a new list is returned, so if the slice is saved and then altered, the original list remains the same.
tools = ['pen', 'hammer', 'lever']
tools_slice = tools[1:3] \# ['hammer', 'lever']
tools_slice[0] = 'nail'

`# Original list is unaltered:`
print(tools) \# ['pen', 'hammer', 'lever']

List Slices

Lists can be sliced like strings and other sequences.

Syntax:

sliced_list = List_Name[startIndex:endIndex]

This refers to the items of a list starting at index startIndex and stopping just before index endIndex. The default values for list are 0 (startIndex) and the end (endIndex) of the list. If you omit both indices, the slice makes a copy of the original list.

Cut first two items from a list:

Python List: Cut first two items of a list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"] \# The list have four elements
indices start at 0 and end at 3
>>> print(color_list[0:2]) \# cut first two items
['Red', 'Blue']
>>>

Copy

Cut second item from a list:

Python List: Cut second element from a list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"] \# The list have four elements
indices start at 0 and end at 3
>>> print(color_list[1:2])
['Blue']
>>> print(color_list[1:-2])
['Blue']
>>>

Copy

Cut second and third elements from a list:

Python List: Cut second and third elements from a list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"] \# The list have four elements
indices start at 0 and end at 3
>>> print(color_list[1:-1])
['Blue', 'Green']
>>>

Copy

Cut first three items from a list:

Python List: First three items from a list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"] \# The list have four elements
indices start at 0 and end at 3
>>> print(color_list[:3]) \# cut first three items
['Red', 'Blue', 'Green']
>>>

Copy

Creates copy of original list:

Python List: Creates copy of original list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"] \# The list have four elements
indices start at 0 and end at 3
>>> print(color_list[:]) \# Creates copy of original list
['Red', 'Blue', 'Green', 'Black']
>>>

Copy


== Mutable
.Lists are Mutable
Items in the list are mutable i.e. after creating a list you can change any item in the list. See the following statements.
Elements in the list are mutable, can be changed after creating a list

Using + and * operators in List

Use + operator to create a new list that is a concatenation of two lists and use * operator to repeat a list. See the following statements.
Python + and * operators in list


>>> days=['Monday','Tuesday',3,4,5,6,7]
>>> days

[‘Monday’, ‘Tuesday’, 3, 4, 5, 6, 7]

3.2. Length of a List

Python supports an inbuilt function to calculate the length of a list.
>>> len(days)

7

3.3. Reassigning Elements of a List

A list is mutable. This means that you can reassign elements later on.
>>> days[2]='Wednesday'
>>> days

[‘Monday’, ‘Tuesday’, ‘Wednesday’, 4, 5, 6, 7]

3.4.Iterating on the List

To iterate over the list we can use the for loop. By iterating, we can access each element one by one which is very helpful when we need to perform some operations on each element of list.

Code:
nums = [1,2,5,6,8]
for n in nums:
    print(n)

Output:

1
2
5
6
8
3.5. Multidimensional Lists

A list may have more than one dimension. Have a detailed look on this in DataFlair’s tutorial on Python Lists.
>>> a=[[1,2,3],[4,5,6]]
>>> a

[[1, 2, 3], [4, 5, 6]]



a. How to Declare Python List?

To use a list, you must declare it first. Do this using square brackets and separate values with commas.
>>> languages=['C++','Python','Scratch']

You can put any kind of value in a list. This can be a string, a Tuple, a Boolean, or even a list itself.
>>> list1=[1,[2,3],(4,5),False,'No']

Note that here, we put different kinds of values in the list. Hence, a list is (or can be) heterogeneous.
b. How to Access Python List?

1. Accessing an entire list

To access an entire list, all you need to do is to type its name in the shell.
>>> list1

[1, [2, 3], (4, 5), False, ‘No’]

2. Accessing a single item from the list

To get just one item from the list, you must use its index. However, remember that indexing begins at 0. Let’s first take a look at the two kinds of indexing.

    Positive Indexing– As you can guess, positive indexing begins at 0 for the leftmost/first item, and then traverses right.

>>> list1[3]

False

    Negative Indexing– Contrary to positive indexing, negative indexing begins at -1 for the rightmost/last item, and then traverses left. To get the same item form list1 by negative indexing, we use the index -2.

>>> type(list1[-2])

<class ‘bool’>

It is also worth noting that the index can’t be a float, it has to be an integer.
>>> list1[1.0]

Traceback (most recent call last):

File “<pyshell#219>”, line 1, in <module>

list1[1.0]

TypeError: list indices must be integers or slices, not float

If you face any doubt in a Python list or Python Data Structure, please comment.
3. Slicing a Python List

Sometimes, you may not want an entire list or a single item, but a number of items from it. Here, the slicing operator [:] comes into play.

Suppose we want items second through fourth from list ‘list1’. We write the following code for this.
>>> list1[1:4]

[[2, 3], (4, 5), False]

Here, we wanted the items from [2,3] to False. The indices for these boundary items are 1 and 3 respectively. But if the ending index is n, then it prints items till index n-1. Hence, we gave it an ending index of 4 here.

We can use negative indexing in the slicing operator too. Let’s see how.
>>> list1[:-2]

[1, [2, 3], (4, 5)]

Here, -2 is the index for the tuple (4,5).
c. A list is mutable

Mutability is the ability to be mutated, to be changed. A list is mutable, so it is possible to reassign and delete individual items as well.
>>> languages

[‘C++’, ‘Python’, ‘Scratch’]
>>> languages[2]='Java'
>>> languages

[‘C++’, ‘Python’, ‘Java’]

Of how to delete an item, we will see in section d.
d. How to Delete a Python List?

Like anything else in Python, it is possible to delete a list.

To delete an entire list, use the del keyword with the name of the list.
>>> list1

Traceback (most recent call last):

File “<pyshell#225>”, line 1, in <module>

list1

NameError: name ‘list1’ is not defined

But to delete a single item or a slice, you need its index/indices.
>>> del languages[2]
>>> languages

[‘C++’, ‘Python’]

Let’s delete a slice now.
>>> del languages[1:]
>>> languages

[‘C++’]
e. Reassigning a List in Python

You can either reassign a single item, a slice, or an entire list. Let’s take a new list and then reassign on it.
>>> list1=[1,2,3,4,5,6,7,8]

1. Reassigning a single item
>>> list1[0]=0
>>> list1

[0, 2, 3, 4, 5, 6, 7, 8]

2. Reassigning a slice

Now let’s attempt reassigning a slice.
>>> list1[1:3]=[9,10,11]
>>> list1

[0, 9, 10, 11, 4, 5, 6, 7, 8]

3. Reassigning the entire list

Finally, let’s reassign the entire list.
>>> list1=[0,0,0]
>>> list1

[0, 0, 0]


6. Reassigning a Python List (Mutable)

Python Lists are mutable. This means that you can reassign its items, or you can reassign it as a whole. Let’s take a new list.
>>> colors=['red','green','blue']
a. Reassigning the whole Python list

You can reassign a Python list by assigning it like a new list.
>>> colors=['caramel','gold','silver','occur']
>>> colors

[‘caramel’, ‘gold’, ‘silver’, ‘occur’]
b. Reassigning a few elements

You can also reassign a slice of a list in Python.
>>> colors[2:]=['bronze','silver']
>>> colors

[‘caramel’, ‘gold’, ‘bronze’, ‘silver’]

If we had instead put two values to a single one in the left, see what would’ve happened.
>>> colors=['caramel','gold','silver','occur']
>>> colors[2:3]=['bronze','silver']
>>> colors

[‘caramel’, ‘gold’, ‘bronze’, ‘silver’, ‘occur’]

colors[2:3] reassigns the element at index 2, which is the third element.

2:2 works too.
>>> colors[2:2]=['occur']
>>> colors

[‘caramel’, ‘gold’, ‘occur’, ‘bronze’, ‘silver’]
c. Reassigning a single element

You can reassign individual elements too.
>>> colors=['caramel','gold','silver','occur']
>>> colors[3]='bronze'
>>> colors

[‘caramel’, ‘gold’, ‘silver’, ‘bronze’]

Now if you want to add another item ‘holographic’ to the list, we cannot do it the conventional way.
>>> colors[4]='holographic'

Traceback (most recent call last):

File “<pyshell#2>”, line 1, in <module>

colors[4]=’holographic’

IndexError: list assignment index out of range

So, you need to reassign the whole list for the same.
>>> colors=['caramel','gold','silver','bronze','holographic']
>>> colors

[‘caramel’, ‘gold’, ‘silver’, ‘bronze’, ‘holographic’]


Lists are Mutable

Items in the list are mutable i.e. after creating a list you can change any item in the list. See the following statements.

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list[0])
Red
>>> color_list[0]="White" \# Change the value of first item "Red" to "White"
>>> print(color_list)
['White', 'Blue', 'Green', 'Black']
>>> print(color_list[0])
White
>>>

Copy



== Python Lists WIP

Contents:

    List commands
    Create a Python list
    List indices
    Add an item to the end of the list
    Insert an item at a given position
    Modify an element by using the index of the element
    Remove an item from the list
    Remove all items from the list
    Slice Elements from a List
    Remove the item at the given position in the list, and return it
    Return the index in the list of the first item whose value is x
    Return the number of times 'x' appear in the list
    Sort the items of the list in place
    Reverse the elements of the list in place
    Return a shallow copy of the list
    Search the Lists and find elements
    Lists are mutable
    Convert a list to a tuple in python
    How to use the double colon [ : : ]?
    Find largest and the smallest items in a list
    Compare two lists in Python?
    Nested lists in Python
    How can I get the index of an element contained in the list?
    Using Lists as Stacks
    Using Lists as Queues
    Python Code Editor
    Python List Exercises

Lists: Commands

<list> = <list>[from_inclusive : to_exclusive : ±step_size]

<list>.append(<el>)
`# Or: <list> += [<el>]`
<list>.extend(<collection>)
 `# Or: <list> += <collection>`

<list>.sort()
<list>.reverse()
<list> = sorted(<collection>)
<iter> = reversed(<list>)

sum_of_elements  = sum(<collection>)
elementwise_sum  = [sum(pair) for pair in zip(list_a, list_b)]
sorted_by_second = sorted(<collection>, key=lambda el: el[1])
sorted_by_both   = sorted(<collection>, key=lambda el: (el[1], el[0]))
flatter_list     = list(itertools.chain.from_iterable(<list>))
product_of_elems = functools.reduce(lambda out, x: out * x, <collection>)
list_of_chars    = list(<str>)

`# Returns number of occurrences. Also works on strings.
  <int> = <list>.count(<el>)
\# Returns index of first occurrence or raises ValueError.
  index = <list>.index(<el>)
\# Inserts item at index and moves the rest to the right.
  <list>.insert(index, <el>)
\# Removes and returns item at index or from the end.
  <el> = <list>.pop([index])
\# Removes first occurrence of item or raises ValueError.
  <list>.remove(<el>)
\# Removes all items. Also works on dictionary and set.  
  <list>.clear()`

Use + operator to create a new list that is a concatenation of two lists and use * operator to repeat a list. See the following statements.

>>> color_list1 = ["White", "Yellow"]
>>> color_list2 = ["Red", "Blue"]
>>> color_list3 = ["Green", "Black"]
>>> color_list = color_list1 + color_list2 + color_list3
>>> print(color_list)
['White', 'Yellow', 'Red', 'Blue', 'Green', 'Black']
>>> number = [1,2,3]
>>> print(number[0]*4)
4
>>> print(number*4)
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>>

Copy

Copy
Add an item to the end of the list

Python List: Add item at the end of the list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.append("Yellow")
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black', 'Yellow']
>>>

Copy



== Modify an element by using the index of the element

Python List: modify an element in the list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list[2]="Yellow"  \#Change the third color
>>> print(color_list)
['Red', 'Blue', 'Yellow', 'Black']
>>>

Copy



== Convert a list to a tuple in Python

>>> listx = [1, 2, 3, 4]  
>>> print(listx)  
[1, 2, 3, 4]  
>>> tuplex = tuple(listx)  
>>> print(tuplex)  
(1, 2, 3, 4)
>>>

Copy


== Compare two lists in Python

>>> listx1, listx2=[3, 5, 7, 9], [3, 5, 7, 9]
>>> print (listx1 == listx2)
True
>>> listx1, listx2=[9, 7, 5, 3], [3, 5, 7, 9]	\#create two lists equal, but unsorted.
>>> print(listx1 == listx2)
False
>>> listx1, listx2 =[2, 3, 5, 7], [3, 5, 7, 9]	\#create two different list
>>> print(listx1 == listx2)
False
>>> print(listx1.sort() == listx2.sort())	\#order and compare
True
>>>

Copy

== Nested lists in Python

>>> listx = [["Hello", "World"], [0, 1, 2, 3, 4, 5]]
>>> print(listx)
[['Hello', 'World'], [0, 1, 2, 3, 4, 5]]
>>> listx = [["Hello", "World"], [0, 1, 2, 3, 3, 5]]
>>> print(listx)
[['Hello', 'World'], [0, 1, 2, 3, 3, 5]]
>>> print(listx[0][1])		\#The first [] indicates the index of the outer list.
World
>>> print(listx[1][3])		\#the second [] indicates the index nested lists.
3
>>> listx.append([True, False])		\#add new items
>>> print(listx)
[['Hello', 'World'], [0, 1, 2, 3, 3, 5], [True, False]]
>>> listx[1][2]=4
>>> print(listx)
[['Hello', 'World'], [0, 1, 4, 3, 3, 5], [True, False]]		\#update value items
>>>

Copy

== Using Lists as Stacks

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.append("White")
>>> color_list.append("Yellow")
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow']
>>> color_list.pop()
'Yellow'
>>> color_list.pop()
'White'
>>> color_list.pop()
'Black'
>>> color_list
['Red', 'Blue', 'Green']
>>>

Copy

== Using Lists as Queues

>>> from collections import deque
>>> color_list = deque(["Red", "Blue", "Green", "Black"])
>>> color_list.append("White")      \# White arrive
>>> print(color_list)
deque(['Red', 'Blue', 'Green', 'Black', 'White'])
>>> color_list.append("Yellow")     \# Yellow arrive
>>> print(color_list)
deque(['Red', 'Blue', 'Green', 'Black', 'White', 'Yellow'])
>>> color_list.popleft()            \# The first to arrive now leaves
'Red'
>>> print(color_list)
deque(['Blue', 'Green', 'Black', 'White', 'Yellow'])
>>> color_list.popleft()            \# The second to arrive now leaves
'Blue'
>>> print(color_list)
deque(['Green', 'Black', 'White', 'Yellow'])
>>> print(color_list)               \# Remaining queue in order of arrival
deque(['Green', 'Black', 'White', 'Yellow'])
>>>

Copy

== 4. How to Access Python List?

To access a Python list as a whole, all you need is its name.
>>> days

[‘Monday’, ‘Tuesday’, ‘Wednesday’, 4, 5, 6, 7.0]

Or, you can put it in a print statement.
>>> languages=[['English'],['Gujarati'],['Hindi'],'Romanian','Spanish']
>>> print(languages)

[[‘English’], [‘Gujarati’], [‘Hindi’], ‘Romanian’, ‘Spanish’]

To access a single element, use its index in square brackets after the list’s name. Indexing begins at 0.
>>> languages[0]

[‘English’]

An index cannot be a float value.
>>> languages[1.0]

Traceback (most recent call last):

File “<pyshell#70>”, line 1, in <module>

languages[1.0]

TypeError: list indices must be integers or slices, not float

Program to show how to add/update single or multiple elements in a list:

lst1 = ['computersc', 'IT', 'CSE'];

print ("Second value of the list is:")
print (lst1[1])

lst1[1] = 'Robotics'

print ("Updated value in the second index of list is:")
print (lst1[1])

Second value of the list is:
IT
Updated value in the second index of list is:
Robotics
== 7. How can we Delete a Python List?

You can delete a Python list, some of its elements, or a single element.
a. Deleting the entire Python list

Use the del keyword for the same.
>>> del colors
>>> colors

Traceback (most recent call last):

File “<pyshell#51>”, line 1, in <module>

colors

NameError: name ‘colors’ is not defined
b. Deleting a few elements

Use the slicing operator in python to delete a slice.
>>> colors=['caramel','gold','silver','bronze','holographic']
>>> del colors[2:4]
>>> colors

[‘caramel’, ‘gold’, ‘holographic’]
>>> colors[2]

‘holographic’

Now, ‘holographic’ is at position 2.
c. Deleting a single element

To delete a single element from a Python list, use its index.
>>> del colors[0]
>>> colors

[‘gold’, ‘holographic’]
To remove an element from the list, we can use the del-statement. The syntax for deleting an element from a list is:

del list_name[index_val];
Remove an item from the list

Python List: remove an element from the list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.remove("Black")
>>> print(color_list)
['Red', 'Blue', 'Green']

Copy
Remove all items from the list

Python List: remove all elements from the list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.clear()
>>> print(color_list)
[]
>>>

Copy


== 8. Multidimensional Lists in Python

You can also put a list in a list. Let’s look at a multidimensional list.
>>> grocery_list=[['caramel','P&B','Jelly'],['onions','potatoes'],['flour','oil']]
>>> grocery_list

[[‘caramel’, ‘P&B’, ‘Jelly’], [‘onions’, ‘potatoes’], [‘flour’, ‘oil’]]

This is a grocery Python list with lists in it, where the lists are according to a category.

Or, you can choose to go deeper.
>>> a=[[[1,2],[3,4],5],[6,7]]
>>> a

[[[1, 2], [3, 4], 5], [6, 7]]

To access the element 4 here, we type the following code into the shell.
>>> a[0][1][1]

4
== 9. Concatenation of Python List

The concatenation operator works for lists as well. It lets us join two lists, with their orders preserved.
>>> a,b=[3,1,2],[5,4,6]
>>> a+b

[3, 1, 2, 5, 4, 6]
Adding Lists Together

In Python, lists can be added to each other using the plus symbol +. As shown in the code block, this will result in a new list containing the same items in the same order with the first list’s items coming first.

Note: This will not work for adding one item at a time (use .append() method). In order to add one item, create a new list with a single value and then use the plus symbol to add the list.
items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
\# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']


== 10. Python List Operations
a. Multiplication

This is an arithmetic operation. Multiplying a Python list by an integer makes copies of its items that a number of times while preserving the order.
>>> a*=3
>>> a

[3, 1, 2, 3, 1, 2, 3, 1, 2]

However, you can’t multiply it by a float.
>>> a*3.0

Traceback (most recent call last):

File “<pyshell#89>”, line 1, in <module>

a*3.0

TypeError: can’t multiply sequence by non-int of type ‘float’
b. Membership

You can apply the ‘in’ and ‘not in’ operators on a Python list.
>>> 1 in a

True
>>> 2 not in a

False

== 11. Iterating on a list

Python list can be traversed with a for loop in python.
>>> for i in [1,2,3]:
         if i%2==0:
                print(f"{i} is composite\n")
<!--ID: 1639528995615-->


2 is composite

== 12. Python List Comprehension

You can create a new list just like you would do in mathematics. To do so, type an expression followed by a for statement, all inside square brackets. You may assign it to a variable. Let’s make a list for all even numbers from 1 to 20.
>>> even=[2*i for i in range(1,11)]
>>> even

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

Optionally, you can add an if-statement to filter out items. If we want to change this list to hold only those items from 1 to 20 that are even and are divisible by 3, we write the following code.
>>> even=[2*i for i in range(1,11) if i%3==0]
>>> even

[6, 12, 18]

Python List Comprehension

Python list comprehensions provide a concise way for creating lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses: [EXPRESSION for ITEM in LIST <if CONDITIONAL>].

The expressions can be anything - any kind of object can go into a list.

A list comprehension always returns a list.
\# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]

print(result)
\# [0, 4, 16, 36, 64]


== List Examples:
      List []
          Initialize
              my_list = []
          Add Item
              my_list.append()
          Access Item
              print my_list[]
          Change Item
              my_list[] = ""
          Remove Item
              del my_list[]
          Iterate
              for item in my_list:
                  print item

Example

Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)
Access Items

You access the list items by referring to the index number:
Example

Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
Negative Indexing

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
Example

Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
Range of Indexes

You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.
Example

Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

Note: The search will start at index 2 (included) and end at index 5 (not included).

Remember that the first item has index 0.

By leaving out the start value, the range will start at the first item:
Example

This example returns the items from the beginning to "orange":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

By leaving out the end value, the range will go on to the end of the list:
Example

This example returns the items from "cherry" and to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
Range of Negative Indexes

Specify negative indexes if you want to start the search from the end of the list:
Example

This example returns the items from index -4 (included) to index -1 (excluded)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
Change Item Value
To change the value of a specific item, refer to the index number:
Example

Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
Loop Through a List

You can loop through the list items by using a for loop:
Example

Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

You will learn more about for loops in our Python For Loops Chapter.
Check if Item Exists

To determine if a specified item is present in a list use the in keyword:
Example

Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
List Length

To determine how many items a list has, use the len() function:
Example

Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
Add Items

To add an item to the end of the list, use the append() method:
Example

Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

To add an item at the specified index, use the insert() method:
Example

Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
Remove Item

There are several methods to remove items from a list:
Example

The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
Example

The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
Example

The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
Example

The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
Example

The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
Copy a List

You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().
Example

Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

Another way to make a copy is to use the built-in method list().
Example

Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
Join Two Lists

There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.
Example

Join two list:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

Another way to join two lists are by appending all the items from list2 into list1, one by one:
Example

Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

Or you can use the extend() method, which purpose is to add elements from one list to another list:
Example

Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
The list() Constructor

It is also possible to use the list() constructor to make a new list.
Example

Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) \# note the double round-brackets
print(thislist)

== List Methods

Python has a set of built-in methods that you can use on lists.
Method 	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

14. Built-in Methods

While a function is what you can apply on a construct and get a result, a method is what you can do to it and change it. To call a method on a construct, you use the dot-operator(.). Python supports some built-in methods to alter a Python list.
Python List - Built-in Methods

Python List – Built-in Methods
a. append()

It adds an item to the end of the list.
>>> a

[2, 1, 3]
>>> a.append(4)
>>> a

[2, 1, 3, 4]
b. insert()

It inserts an item at a specified position.
>>> a.insert(3,5)
>>> a

[2, 1, 3, 5, 4]

This inserted the element 5 at index 3.
c. remove()

It removes the first instance of an item from the Python list.
>>> a=[2,1,3,5,2,4]
>>> a.remove(2)
>>> a

[1, 3, 5, 2, 4]

Notice how there were two 2s, but it removed only the first one.
d. pop()

It removes the element at the specified index, and prints it to the screen.
>>> a.pop(3)

2
>>> a

[1, 3, 5, 4]
e. clear()

It empties the Python list.
>>> a.clear()
>>> a

[]

It now has a False value.
>>> bool(a)

False
f. index()

It returns the first matching index of the item specified.
>>> a=[1,3,5,3,4]
>>> a.index(3)

1
g. count()

It returns the count of the item specified.
>>> a.count(3)

2
h. sort()

It sorts the list in an ascending order.
>>> a.sort()
>>> a

[1, 3, 3, 4, 5]
i. reverse()

It reverses the order of elements in the Python lists.
>>> a.reverse()
>>> a

[5, 4, 3, 3, 1]

List Method .sort()

The .sort() Python list method will sort the contents of whatever list it is called on. Numerical lists will be sorted in ascending order, and lists of Strings will be sorted into alphabetical order. It modifies the original list, and has no return value.
exampleList = [4, 2, 1, 3]
exampleList.sort()
print(exampleList)
\# Output: [1, 2, 3, 4]

List Method .count()

The .count() Python list method searches a list for whatever search term it receives as an argument, then returns the number of matching entries found.
backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')
print(numPen)
\# Output: 3
Determining List Length with len()

The Python len() function can be used to determine the number of items found in the list it accepts as an argument.
knapsack = [2, 4, 3, 7, 10]
size = len(knapsack)
print(size)
\# Output: 5


List Method .append()

In Python, you can add values to the end of a list using the .append() method. This will place the object passed in as a new element at the very end of the list. Printing the list afterwards will visually show the appended value. This .append() method is not to be confused with returning an entirely new list with the passed object.
orders = ['daisies', 'periwinkle']
orders.append('tulips')
print(orders)
\# Result: ['daisies', 'periwinkle', 'tulips']



== Functions
13. Built-in List Functions

There are some built-in functions in Python that you can use on python lists.
Python List Tutorial - Built-in List Functions

Python List Tutorial – Built-in List Functions
a. len()

It calculates the length of the list.
>>> len(even)

3
b. max()

It returns the item from the list with the highest value.
>>> max(even)

18

If all the items in your list are strings, it will compare.
>>> max(['1','2','3'])

‘3’

But it fails when some are numeric, and some are strings in python.
>>> max([2,'1','2'])

Traceback (most recent call last):

File “<pyshell#116>”, line 1, in <module>

max([2,’1′,’2′])

TypeError: ‘>’ not supported between instances of ‘str’ and ‘int’
c. min()

It returns the item from the Python list with the lowest value.
>>> min(even)

6
d. sum()

It returns the sum of all the elements in the list.
>>> sum(even)

36

However, for this, the Python list must hold all numeric values.
>>> a=['1','2','3']
>>> sum(a)

Traceback (most recent call last):

File “<pyshell#112>”, line 1, in <module>

sum(a)

TypeError: unsupported operand type(s) for +: ‘int’ and ‘str’

It works on floats.
>>> sum([1.1,2.2,3.3])

6.6
e. sorted()

It returns a sorted version of the list, but does not change the original one.
>>> a=[3,1,2]
>>> sorted(a)

[1, 2, 3]
>>> a

[3, 1, 2]

If the Python list members are strings, it sorts them according to their ASCII values.
>>> sorted(['hello','hell','Hello'])

[‘Hello’, ‘hell’, ‘hello’]

Here, since H has an ASCII value of 72, it appears first.
f. list()

It converts a different data type into a list.
>>> list("abc")

[‘a’, ‘b’, ‘c’]

It can’t convert a single int into a list, though, it only converts iterables.
>>> list(2)

Traceback (most recent call last):

File “<pyshell#122>”, line 1, in <module>

list(2)

TypeError: ‘int’ object is not iterable
g. any()

It returns True if even one item in the Python list has a True value.
>>> any(['','','1'])

True

It returns False for an empty iterable.
>>> any([])

False
h. all()

It returns True if all items in the list have a True value.
>>> all(['','','1'])

False

It returns True for an empty iterable.
>>> all([])

True

sorted() Function

The Python sorted() function accepts a list as an argument, and will return a new, sorted list containing the same elements as the original. Numerical lists will be sorted in ascending order, and lists of Strings will be sorted into alphabetical order. It does not modify the original, unsorted list.
unsortedList = [4, 2, 1, 3]
sortedList = sorted(unsortedList)
print(sortedList)
\# Output: [1, 2, 3, 4]

Aggregating Iterables Using zip()

In Python, data types that can be iterated (called iterables) can be used with the zip() function to aggregate data. The zip() function takes iterables, aggregates corresponding elements based on the iterables passed in, and returns an iterator. Each element of the returned iterator is a tuple of values.

As shown in the example, zip() is aggregating the data between the owners’ names and the dogs’ names to match the owner to their dogs. zip() returns an iterator containing the data based on what the user passes to the function. Empty iterables passed in will result in an empty iterator. To view the contents of the iterator returned from zip(), we can cast it as a list by using the list() function and printing the results.
owners_names = ['Jenny', 'Sam', 'Alexis']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter']
owners_dogs = zip(owners_names, dogs_names)
print(list(owners_dogs))
\# Result: [('Jenny', 'Elphonse'), ('Sam', 'Dr.Doggy DDS'), ('Alexis', 'Carter')]

Find the largest and the smallest item in a list

>>> listx=[5, 10, 3, 25, 7, 4, 15]
>>> print(listx)
[5, 10, 3, 25, 7, 4, 15]
>>> print(max(listx))	# the max() function of built-in allows to know the highest
value in the list.
25
>>> print(min(listx)) \#the min() function of built-in allows to know the lowest
value in the list.
3
>>>

Copy

Remove the item at the given position in the list, and return it

Python List: Remove the item at the given position in the list, and return it

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.pop(2) \# Remove second item and return it
'Green'
>>> print(color_list)
['Red', 'Blue', 'Black']
>>>

Copy
Return the index in the list of the first item whose value is x
Python List: Return the number of times 'x' appear in the list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.index("Red")
0
>>> color_list.index("Black")
3
>>>

Copy
Return the number of times 'x' appear in the list
Python List: Return the index in the list of the first item whose value is x

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list=["Red", "Blue", "Green", "Black", "Blue"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black', 'Blue']
>>> color_list.count("Blue")
2
>>>

Copy
Sort the items of the list in place

Python List: Return the number of times 'x' appear in the list

See the following statements:

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.sort(key=None, reverse=False)
>>> print(color_list)
['Black', 'Blue', 'Green', 'Red']
>>>

Copy
Reverse the elements of the list in place

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.reverse()
>>> print(color_list)
['Black', 'Green', 'Blue', 'Red']
>>>

Copy
Return a shallow copy of the list

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.copy()
['Red', 'Blue', 'Green', 'Black']
>>>

Copy
Search the Lists and find Elements

>>> color_list=["Red", "Blue", "Green", "Black"]
>>> print(color_list)
['Red', 'Blue', 'Green', 'Black']
>>> color_list.index("Green")
2
>>>

Copy
t the current window

  #python #datatypes
