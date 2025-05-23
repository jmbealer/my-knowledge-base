---
title: Python Built-in Methods
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-03
reference: 
description: 
aliases: 
tags: 
---
# Python Built-in Methods

## String Methods

Python has a set of built-in methods that you can use on strings.
Note: All string methods returns new values. They do not change the original string.
chained methods object.method1().method2()

Method Description

**.capitalize()** Converts the first character to upper case.
	string.capitalize()
**.lower()** Converts a string into lower case.
**.casefold()** Converts string into lower case.
	string.casefold()
	.casefold() method is stronger, more aggressive than .lower() method.
**.center()** Returns a centered string.
	string.center(length, character)
		length Required. The length of the returned string
		character Optional. The character of fill the missing space on each side.
		Default is ' '(space).
**.count()** Returns the number of times a specified value occurs in a string.
**.encode()** Returns an encoded version of the string.
**.endswith()** Returns true if the string ends with the specified value.
**.expandtabs()** Sets the tab size of the string.
**.find()** Searches the string for a specified value and returns the position of where it was found.
**.format()** Formats specified values in a string.
**.format_map()** Formats specified values in a string.
**.index()** Searches the string for a specified value and returns the position of where it was found.
**.isalnum()** Returns True if all characters in the string are alphanumeric.
**.isalpha()** Returns True if all characters in the string are in the alphabet.
**.isdecimal()** Returns True if all characters in the string are decimals.
**.isdigit()** Returns True if all characters in the string are digits.
**.isidentifier()** Returns True if the string is an identifier.
**.islower()** Returns True if all characters in the string are lower case.
**.isnumeric()** Returns True if all characters in the string are numeric.
**.isprintable()** Returns True if all characters in the string are printable.
**.isspace()** Returns True if all characters in the string are whitespaces.
**.istitle()** Returns True if the string follows the rules of a title.
**.isupper()** Returns True if all characters in the string are upper case.
**.join()** Joins the elements of an iterable to the end of the string.
**.ljust()** Returns a left justified version of the string.
**.lstrip()** Returns a left trim version of the string.
**.maketrans()** Returns a translation table to be used in translations.
**.partition()** Returns a tuple where the string is parted into three parts.
**.replace()** Returns a string where a specified value is replaced with a specified value.
**.rfind()** Searches the string for a specified value and returns the last position of where it was found.
**.rindex()** Searches the string for a specified value and returns the last position of where it was found.
**.rjust()** Returns a right justified version of the string.
**.rpartition()** Returns a tuple where the string is parted into three parts.
**.rsplit()** Splits the string at the specified separator, and returns a list.
**.rstrip()** Returns a right trim version of the string.
**.split()** Splits the string at the specified separator, and returns a list.
**.splitlines()** Splits the string at line breaks and returns a list.
**.startswith()** Returns true if the string starts with the specified value.
**.strip()** Returns a trimmed version of the string.
**.swapcase()** Swaps cases, lower case becomes upper case and vice versa.
**.title()** Converts the first character of each word to upper case.
**.translate()** Returns a translated string.
**.upper()** Converts a string into upper case.
**.zfill()** Fills the string with a specified number of 0 values at the beginning.

## List/Array Methods

Python has a set of built-in methods that you can use on lists/arrays.

Method 	Description

**append()** Adds an element at the end of the list.
**clear()** Removes all the elements from the list.
**copy()** Returns a copy of the list.
**count()** Returns the number of elements with the specified value.
**extend()** Add the elements of a list (or any iterable), to the end of the
current list.
**index()** Returns the index of the first element with the specified value.
**insert()** Adds an element at the specified position.
**pop()** Removes the element at the specified position.
**remove()** Removes the first item with the specified value.
**reverse()** Reverses the order of the list.
**sort()** Sorts the list.

## Dictionary Methods

Python has a set of built-in methods that you can use on dictionaries.
Method 	Description

**clear()** Removes all the elements from the dictionary.
**copy()** Returns a copy of the dictionary.
**fromkeys()** Returns a dictionary with the specified keys and value.
**get()** Returns the value of the specified key.
**items()** Returns a list containing a tuple for each key value pair.
**keys()** Returns a list containing the dictionary's keys.
**pop()** Removes the element with the specified key.
**popitem()** Removes the last inserted key-value pair.
**setdefault()** Returns the value of the specified key. If the key does not
exist: insert the key, with the specified value.
**update()** Updates the dictionary with the specified key-value pairs.
**values()** Returns a list of all the values in the dictionary.

## Tuple Methods

Python has two built-in methods that you can use on tuples.
Method 	Description

**count()** Returns the number of times a specified value occurs in a tuple.
**index()** Searches the tuple for a specified value and returns the position
of where it was found.

## Set Methods

Python has a set of built-in methods that you can use on sets.
Method 	Description

**add()** Adds an element to the set.
**clear()** Removes all the elements from the set.
**copy()** Returns a copy of the set.
**difference()** Returns a set containing the difference between two or more
sets.
**difference_update()** Removes the items in this set that are also included in
another, specified set.
**discard()** Remove the specified item.
**intersection()** Returns a set, that is the intersection of two other sets.
**intersection_update()** Removes the items in this set that are not present in
other, specified set(s).
**isdisjoint()** Returns whether two sets have a intersection or not.
**issubset()** Returns whether another set contains this set or not.
**issuperset()** Returns whether this set contains another set or not.
**pop()** Removes an element from the set.
**remove()** Removes the specified element.
**symmetric_difference()** Returns a set with the symmetric differences of two
sets.
**symmetric_difference_update()** inserts the symmetric differences from this
set and another.
**union()** Return a set containing the union of sets.
**update()** Update the set with another set, or any other iterable.

## File Methods

Python has a set of methods available for the file object.
Method 	Description

**close()** Closes the file.
**detach()** Returns the separated raw stream from the buffer.
**fileno()** Returns a number that represents the stream, from the operating
system's perspective.
**flush()** Flushes the internal buffer.
**isatty()** Returns whether the file stream is interactive or not.
**read()** Returns the file content.
**readable()** Returns whether the file stream can be read or not.
**readline()** Returns one line from the file.
**readlines()** Returns a list of lines from the file.
**seek()** Change the file position.
**seekable()** Returns whether the file allows us to change the file position.
**tell()** Returns the current file position.
**truncate()** Resizes the file to a specified size.
**writable()** Returns whether the file can be written to or not.
**write()** Writes the specified string to the file.
**writelines()** Writes a list of strings to the file.
