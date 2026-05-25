Sets

A set is an unordered collection of unique elements. Basic uses include dealing with set theory (which support mathematical operations like union, intersection, difference, and symmetric difference) or eliminating duplicate entries. See the following statements.
Python Sets

    Sets: An unordered container of values.

mutable

7. Sets

A set can have a list of values. Define it using curly braces.
>>> a={1,2,3}
>>> a
<!--ID: 1639528994648-->


{1, 2, 3}
<!--ID: 1639528994669-->


It returns only one instance of any value present more than once.
>>> a={1,2,2,3}
>>> a
<!--ID: 1639528994691-->


{1, 2, 3}

However, a set is unordered, so it doesn’t support indexing.
>>> a[2]

Traceback (most recent call last):
File “<pyshell#127>”, line 1, in <module>
a[2]
TypeError: ‘set’ object does not support indexing

Also, it is mutable. You can change its elements or add more. Use the add() and remove() methods to do so.
>>> a={1,2,3,4}
>>> a
<!--ID: 1639528994716-->


{1, 2, 3, 4}
>>> a.remove(4)
>>> a
<!--ID: 1639528994738-->


{1, 2, 3}
>>> a.add(4)
>>> a
<!--ID: 1639528994764-->


{1, 2, 3, 4}
<!--ID: 1639528994785-->



5. Python Set

This is one of the important Python Data Structures. A Python set is a slightly different concept from a list or a tuple. A set, in Python, is just like the mathematical set. It does not hold duplicate values and is unordered. However, it is not immutable, unlike a tuple.

Let’s first declare a set. Use curly braces for the same.
>>> myset={3,1,2}
>>> myset
<!--ID: 1639528994800-->


{1, 2, 3}

As you can see, it rearranged the elements in an ascending order.

Since a set is unordered, there is no way we can use indexing to access or delete its elements. Then, to perform operations on it, Python provides us with a list of functions and methods like discard(), pop(), clear(), remove(), add(), and more. Functions like len() and max() also apply on sets.

Any Doubt yet in Python Data Structures? Please Comment.


=== Python Sets WIP
Set

A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets.
Example

Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
<!--ID: 1639528994826-->


Note: Sets are unordered, so you cannot be sure in which order the items will appear.
Access Items

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
Example

Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528994848-->


for x in thisset:
  print(x)
Example

Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528994868-->


print("banana" in thisset)
Change Items

Once a set is created, you cannot change its items, but you can add new items.
Add Items

To add one item to a set use the add() method.

To add more than one item to a set use the update() method.
Example

Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528994890-->


thisset.add("orange")

print(thisset)
Example

Add multiple items to a set, using the update() method:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528994911-->


thisset.update(["orange", "mango", "grapes"])

print(thisset)
Get the Length of a Set

To determine how many items a set has, use the len() method.
Example

Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528994934-->


print(len(thisset))
Remove Item

To remove an item in a set, use the remove(), or the discard() method.
Example

Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528994955-->


thisset.remove("banana")

print(thisset)

Note: If the item to remove does not exist, remove() will raise an error.
Example

Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528994977-->


thisset.discard("banana")

print(thisset)

Note: If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

The return value of the pop() method is the removed item.
Example

Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528994998-->


x = thisset.pop()

print(x)

print(thisset)

Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
Example

The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528995020-->


thisset.clear()

print(thisset)
Example

The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
<!--ID: 1639528995041-->


del thisset

print(thisset)
Join Two Sets

There are several ways to join two or more sets in Python.

You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
Example

The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
<!--ID: 1639528995063-->


set3 = set1.union(set2)
print(set3)
Example

The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
<!--ID: 1639528995085-->


set1.update(set2)
print(set1)

Note: Both union() and update() will exclude any duplicate items.

There are other methods that joins two sets and keeps ONLY the duplicates, or NEVER the duplicates, check the full list of set methods in the bottom of this page.
The set() Constructor

It is also possible to use the set() constructor to make a set.
Example

Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
Set Methods

Python has a set of built-in methods that you can use on sets.
Method 	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others


x = {"apple", "banana", "cherry"} 	set
    Set is a collection which is unordered and unindexed. No duplicate members.
    
<!--ID: 1639528995106-->


  #python #datatypes
