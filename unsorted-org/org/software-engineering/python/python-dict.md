= Dictionaries WIP

<dict> = {<key>:<value>, <key>:<value>}
<!--ID: 1639528995815-->


Python dictionary is a container of the unordered set of objects like lists.
dictionaries are wrapped in curly braces {}.
The items in a dictionary are a comma-separated list of key:value pairs where keys and values are Python data type. 
Each object or value accessed by key and keys are unique in the dictionary. 
As keys are used for indexing, they must be the immutable type (string, number, or tuple). 
<empty_dict> = {}
<!--ID: 1639528995837-->


dict()
are mutable
are dynamic. They can grow and shrink as needed.
can be nested
a list can contain another list. A dictionary can contain another dictionary.
A dictionary can also contain a list, and vice versa.
list elements are accessed by their position in the list, via indexing
dictionary elements are accessed via keys.

dictionaries are similar to associative arrays
collection of key-value pairs.
each key-value pair maps the key to its associative value.

Dictionaries: A key-paired values set in an unordered way.

<dict>[<key>] => <value>
.reassign
<dict>[<key>] = <new_value>


.List of Keys
Use the keys() function to get a list of keys in the dictionary.
>>> person.keys()
dict_keys([‘city’, ‘age’])

Think of a real-life dictionary. What is it used for? It holds word-meaning pairs. 
Likewise, a Python dictionary holds key-value pairs. 
However, you may not use an unhashable item as a key.

.Add item
<dict>['<key>'] = '<value>'
my_dict['name'] = 'john'
.Access Item
<dict>['<key>']
.Change
<dict>['<key>'] = '<new_value>'
.Remove
del <dict>['<key>']
.Iterate
    for k, v in my_dict.iteritems():
        print k, "=>", v

=== Python Dictionaries WIP
Dictionary

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
Example

Create and print a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
Accessing Items

You can access the items of a dictionary by referring to its key name, inside square brackets:
Example

Get the value of the "model" key:
x = thisdict["model"]

There is also a method called get() that will give you the same result:
Example

Get the value of the "model" key:
x = thisdict.get("model")
Change Values

You can change the value of a specific item by referring to its key name:
Example

Change the "year" to 2018:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
Loop Through a Dictionary

You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
Example

Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)
Example

Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
Example

You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)
Example

Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)
Check if Key Exists

To determine if a specified key is present in a dictionary use the in keyword:
Example

Check if "model" is present in the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
Dictionary Length

To determine how many items (key-value pairs) a dictionary has, use the len() function.
Example

Print the number of items in the dictionary:
print(len(thisdict))
Adding Items

Adding an item to the dictionary is done by using a new index key and assigning a value to it:
Example
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
Removing Items

There are several methods to remove items from a dictionary:
Example

The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
Example

The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
Example

The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
Example

The del keyword can also delete the dictionary completely:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) \#this will cause an error because "thisdict" no longer exists.
Example

The clear() method empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
Copy a Dictionary

You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
Example

Make a copy of a dictionary with the copy() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

Another way to make a copy is to use the built-in function dict().
Example

Make a copy of a dictionary with the dict() function:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
Nested Dictionaries

A dictionary can also contain many dictionaries, this is called nested dictionaries.
Example

Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

Or, if you want to nest three dictionaries that already exists as dictionaries:
Example

Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
The dict() Constructor

It is also possible to use the dict() constructor to make a new dictionary:
Example
thisdict = dict(brand="Ford", model="Mustang", year=1964)
\# note that keywords are not string literals
\# note the use of equals rather than colon for the assignment
print(thisdict)
Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.
Method 	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary



Accessing and writing data in a Python dictionary

Values in a Python dictionary can be accessed by placing the key within square brackets next to the dictionary. Values can be written by placing key within square brackets next to the dictionary and using the assignment operator (=). If the key already exists, the old value will be overwritten. Attempting to access a value with a key that does not exist will cause a KeyError.

To illustrate this review card, the second line of the example code block shows the way to access the value using the key "song". The third line of the code block overwrites the value that corresponds to the key "song".
my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}
print(my_dictionary["song"])
my_dictionary["song"] = "Paradise City"
Syntax of the Python dictionary
<!--ID: 1639528995859-->


The syntax for a Python dictionary begins with the left curly brace ({), ends with the right curly brace (}), and contains zero or more key : value items separated by commas (,). The key is separated from the value by a colon (:).
roaster = {"q1": "Ashley", "q2": "Dolly"}
Merging Dictionaries with the .update() Method in Python
<!--ID: 1639528995881-->


Given two dictionaries that need to be combined, Python makes this easy with the .update() function.

For dict1.update(dict2), the key-value pairs of dict2 will be written into the dict1 dictionary.

For keys in both dict1 and dict2, the value in dict1 will be overwritten by the corresponding value in dict2.
dict1 = {'color': 'blue', 'shape': 'circle'}
dict2 = {'color': 'red', 'number': 42}
<!--ID: 1639528995906-->


dict1.update(dict2)

\# dict1 is now {'color': 'red', 'shape': 'circle', 'number': 42}
Dictionary value types
<!--ID: 1639528995929-->


Python allows the values in a dictionary to be any type – string, integer, a list, another dictionary, boolean, etc. However, keys must always be an immutable data type, such as strings, numbers, or tuples.

In the example code block, you can see that the keys are strings or numbers (int or float). The values, on the other hand, are many varied data types.
dictionary = {
  1: 'hello', 
  'two': True, 
  '3': [1, 2, 3], 
  'Four': {'fun': 'addition'}, 
  5.0: 5.5
}
Python dictionaries
<!--ID: 1639528995951-->


A python dictionary is an unordered collection of items. It contains data as a set of key: value pairs.
my_dictionary = {1: "L.A. Lakers", 2: "Houston Rockets"}
Dictionary accession methods
<!--ID: 1639528995974-->


When trying to look at the information in a Python dictionary, there are multiple methods that access the dictionary and return lists of its contents.

.keys() returns the keys (the first object in the key-value pair), .values() returns the values (the second object in the key-value pair), and .items() returns both the keys and the values as a tuple.
ex_dict = {"a": "anteater", "b": "bumblebee", "c": "cheetah"}
<!--ID: 1639528995991-->


ex_dict.keys()
\# ["a","b","c"]

ex_dict.values()
\# ["anteater", "bumblebee", "cheetah"]

ex_dict.items()
\# [("a","anteater"),("b","bumblebee"),("c","cheetah")]
get() Method for Dictionary

Python provides a .get() method to access a dictionary value if it exists. This method takes the key as the first argument and an optional default value as the second argument, and it returns the value for the specified key if key is in the dictionary. If the second argument is not specified and key is not found then None is returned.
\# without default
{"name": "Victor"}.get("name")
\# returns "Victor"
<!--ID: 1639528996020-->


{"name": "Victor"}.get("nickname")
\# returns None
<!--ID: 1639528996042-->


\# with default
{"name": "Victor"}.get("nickname", "nickname is not a key")
\# returns "nickname is not a key"
The .pop() Method for Dictionaries in Python
<!--ID: 1639528996064-->


Python dictionaries can remove key-value pairs with the .pop() method. The method takes a key as an argument and removes it from the dictionary. At the same time, it also returns the value that it removes from the dictionary.
famous_museums = {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre', 'Athens': 'The Acropolis Museum'}
famous_museums.pop('Athens')
print(famous_museums) \# {'Washington': 'Smithsonian Institution', 'Paris': 'Le Louvre'}
<!--ID: 1639528996086-->


Conditional Operators

Conditional expressions or ternary operator have the lowest priority of all Python operations. The expression x if C else y first evaluates the condition, C (not x); if C is true, x is evaluated and its value is returned; otherwise, y is evaluated and its value is returned.



    Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


  #python #datatypes
