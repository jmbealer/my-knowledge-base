---
title: Python 3
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 11-01-02
reference: 
description: 
aliases: 
tags: 
---
= Python String Methods

all the string methods always return new values and do not change or manipulate
the original string.
a method is like a function, but it runs 'on' an object

<str>.join(<seq>)
joins list of string based on the separator provided.
replace(<str1>, <str2>)
remove a string from another string. If the string is not matched the initial
string is not changed.
split('separator')
splits the string based on the separator provided. default separator is space.
find()
rfind()
rstrip()
lstrip()
count()
len()

== Unsorted

.capitalize() method
<str>.capitalize() => converts the first character of the string to upper case;
the rest is lower case.

.casefold() method
converts string into lower case

.center() method
center()	Returns center-aligned string

.count() method
count()	Counts occurrences of a substring in a string
return occurrences of a substring in a string.

.encode() method
encode()	Return an encoded version of the string

.endswith() method
endswith()	Determines whether the string ends with a given suffix
checks if the string ends with a given suffix

.expandtabs() method
expandtabs()	Replaces tabs character with spaces

.find() method
find()	Searches the string for a given substring
returns the index of first occurrence of substring

.format() method
format()	Perform a string formatting operation

.format_map() method
format_map()	Perform a string formatting operation
  format the string using dictionary

.index() method
index()	Searches the string for a given substring
  returns index of substring

.isalnum() method
isalnum()	check if all characters in the string are alphanumeric.
  checks if all characters are alphanumeric

.isalpha() method
isalpha()	checks if all character in the string are in the alphabet.

.isdecimal() method
isdecimal()	checks if all characters in the string are decimals.

.isdigit() method
isdigit()	checks if all characters in the string are digits.

.isidentifier() method
isidentifier() checks if the string is an identifier

.islower() method
islower()	Determines whether string contains lowercase characters
  islower()	checks if all characters in the string are lowercase

.isnumeric() method
isnumeric()	Determines whether the string contains numeric characters
  isnumeric()	checks if all characters in the string are numeric

.isprintable() method
isprintable()	Determines whether string contains printable characters
  isprintable()	checks if all characters in the string are printable

.isspace() method
isspace()	Determines whether the string contains only whitespace characters
  isspace()	checks if all the characters in the string are whitespace

.istitle() method
istitle()	check if the string is a title-cased string

.isupper() method
isupper()	checks if string contains uppercase characters
  isupper()	checks if all characters in the string is uppercase

.join() method
join()	Joins all items in an iterable into a single string
  join() 	It is used to Join the elements of an iterable to the end of the string.

.ljust() method
ljust()	Returns left-aligned string

.lower() method
lower()	Converts all characters in a string to lowercase

.lstrip() method
lstrip()	Strips characters from the left end of a string
  removes leading characters

.maketrans() method
maketrans()	Returns a translation table to be used in translations

.partition() method
partition()	Divides a string based on a separator
  partition() 	It is used to return a tuple where the string is parted into three parts.
  returns a tuple

.replace() method
replace()	Replaces occurrences of a substring within a string
  replace a substring within a string

.rfind() method
rfind()	Searches the string for a given substring
  returns the highest index of substring

.rindex() method
rindex()	Searches the string for a given substring

.rjust() method
rjust()	Returns right-aligned string; right-justified

.rpartition() method
rpartition()	Divides a string based on a separator
  It is used to return a tuple where the string is parted into three parts.
  returns a tuple

.rsplit() method
rsplit()	Splits a string into a list of substrings
splits string from right

.rstrip() method
rstrip()	Strips characters from the right end of a string
removes trailing characters

.split() method
split()	Splits a string into a list of substrings
splits string from left

.splitlines() method
splitlines()	Splits the string at line breaks; returns a list

.startswith() method
startswith()	checks if the string starts with a given substring

.strip() method
strip()	Strips leading and trailing characters
removes both leading and trailing characters

.swapcase() method
swapcase()	Swaps case of all characters in a string; lower case becomes
uppercase and vice-versa

.title() method
title() convert the first character of each word to upper case.

.translate() method
translate()	Returns a translated string
returns mapped characters string

.upper() method
upper()	Converts all characters in a string to uppercase

.zfill() method
zfill() 	It is used to fill the string with a specified number of 0 values at the beginning.
Returns a Copy of The String Padded With Zeros


Casefold()
	Returns a casefolded copy of the string. Casefolded strings may be used for caseless matching.
	

>>> mystring = "hello PYTHON"
>>> print(mystring.casefold())
hello python

Center(width, [fillchar])
	Returns the string centered in a string of length width. Padding can be done using the specified fillchar (the default padding uses an ASCII space). The original string is returned if width is less than or equal to len(s)
	

>>> mystring = "Hello"
>>> x = mystring.center(12,
"-")
>>> print(x)
---Hello----

Count(sub, [start], [end])
	Returns the number of non-overlapping occurrences of substring (sub) in the range [start, end]. Optional arguments startand end are interpreted as in slice notation.
	

>>> mystr = "Hello Python"
>>> print(mystr.count("o"))
2
>>> print(mystr.count("th"))
1
>>> print(mystr.count("l"))
2
>>> print(mystr.count("h"))
1
>>> print(mystr.count("H"))
1
>>> print(mystr.count("hH"))
0

Encode(encoding = “utf-g”, errors = “strict”)
	Returns an encoded version of the string as a bytes object. The default encoding is utf-8. errors may be given to set a different error handling scheme. The possible value for errors are:

    strict (encoding errors raise a UnicodeError)

    ignore

    replace

    xmlcharrefreplace

    backslashreplace

    any other name registered via codecs.register_error()

 
	

>>> mystr = 'python!'
>>> print('The string is:',
mystr)
The string is: python!
>>> print('The encoded
version is: ',
mystr.encode("ascii",
"ignore"))
The encoded version is:
b'python!'
>>> print('The encoded
version (with replace) is:',
mystr.encode("ascii",
"replace"))
The encoded version (with
replace) is: b'python!'

endswith(suffix, [start], [end])
	Returns True if the string ends with the specified suffix, otherwise it returns False.
	

>>> mystr = "Python"
>>>
print(mystr.endswith("y"))
False
>>>
print(mystr.endswith("hon"))
True

Expandtabs(tabsize=8)
	Returns a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size.
	

>>> mystr = "1\t2\t3"
>>> print(mystr)
1 2 3
>>>
print(mystr.expandtabs())
1 2 3
>>>
print(mystr.expandtabs(tabsi
ze=15))
1 2
3
>>>
print(mystr.expandtabs(tabsi
ze=2))
1 2 3

Find(sub, [start], [end])
	Returns the lowest index in the string where substring sub is found within the slice s[start:end].
	

>>> mystring = "Python"
>>>
print(mystring.find("P"))
0
>>>
print(mystring.find("on"))
4

Format(*args, **kwargs)
	Performs a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}.
	

>>> print("{} and
{}".format("Apple",
"Banana"))
Apple and Banana
>>> print("{1} and
{0}".format("Apple",
"Banana"))
Banana and Apple
>>> print("{lunch} and
{dinner}".format(lunch="Peas
", dinner="Beans"))
Peas and Beans
<!--ID: 1639528994115-->


format_map(mapping)
	Similar to format(**mapping), except that mapping is used directly and not copied to a dictionary.
	

>>> lunch = {"Food":
"Pizza", "Drink": "Wine"}
>>> print("Lunch: {Food},
{Drink}".format_map(lunch))
Lunch: Pizza, Wine
>>> class Default(dict):
def __missing__(self,
key):
return key
>>> lunch = {"Drink":
"Wine"}
>>> print("Lunch: {Food},
{Drink}".format_map(Default(
lunch)))
Lunch: Food, Wine
<!--ID: 1639528994132-->


Index(sub, [start], [end])
	Searches the string for a specified value and returns the position of where it was found
	

>>> mystr = "HelloPython"
>>> print(mystr.index("P"))
5
>>>
print(mystr.index("hon"))
8
>>> print(mystr.index("o"))
4

isalnum
	Returns True if all characters in the string are alphanumeric
	

>>> mystr = "HelloPython"
>>> print(mystr.isalnum())
True
>>> a = "123"
>>> print(a.isalnum())
True
>>> a= "$*%!!!"
>>> print(a.isalnum())
False

Isalpha()
	Returns True if all characters in the string are in the alphabet
	

>>> mystr = "HelloPython"
>>> print(mystr.isalpha())
True
>>> a = "123"
>>> print(a.isalpha())
False
>>> a= "$*%!!!"
>>> print(a.isalpha())
False

Isdecimal()
	Returns True if all characters in the string are decimals
	

>>> mystr = "HelloPython"
>>> print(mystr.isdecimal())
False
>>> a="1.23"
>>> print(a.isdecimal())
False
>>> c = u"\u00B2"
>>> print(c.isdecimal())
False
>>> c="133"
>>> print(c.isdecimal())
True

Isdigit()
	Returns True if all characters in the string are digits
	

>>> c="133"
>>> print(c.isdigit())
True
>>> c = u"\u00B2"
>>> print(c.isdigit())
True
>>> a="1.23"
>>> print(a.isdigit())
False

isidentifier()
	Returns True if the string is an identifier
	

>>> c="133"
>>> print(c.isidentifier())
False
>>> c="_user_123"
>>> print(c.isidentifier())
True
>>> c="Python"
>>> print(c.isidentifier())
True

Islower()
	Returns True if all characters in the string are lower case
	

>>> c="Python"
>>> print(c.islower())
False
>>> c="_user_123"
>>> print(c.islower())
True
>>> print(c.islower())
False

Isnumeric()
	Returns True if all characters in the string are numeric
	

>>> c="133"
>>> print(c.isnumeric())
True
>>> c="_user_123"
>>> print(c.isnumeric())
False
>>> c="Python"
>>> print(c.isnumeric())
False

isprintable()
	Returns True if all characters in the string are printable
	

>>> c="133"
>>> print(c.isprintable())
True
>>> c="_user_123"
>>> print(c.isprintable())
True
>>> c="\t"
>>> print(c.isprintable())
False

isspace()
	Returns True if all characters in the string are whitespaces
	

>>> c="133"
>>> print(c.isspace())
False
>>> c="Hello Python"
>>> print(c.isspace())
False
73
>>> c="Hello"
>>> print(c.isspace())
False
>>> c="\t"
>>> print(c.isspace())
True

istitle()
	Returns True if the string follows the rules of a title
	

>>> c="133"
>>> print(c.istitle())
False
>>> c="Python"
>>> print(c.istitle())
True
>>> c="\t"
>>> print(c.istitle())
False

isupper()
	Returns True if all characters in the string are upper case
	

>>> c="Python"
>>> print(c.isupper())
False
>>> c="PYHTON"
>>> print(c.isupper())
True
>>> c="\t"
>>> print(c.isupper())
False

join(iterable)
	Joins the elements of an iterable to the end of the string
	

>>> a ="-"
>>> print(a.join("123"))
1-2-3
>>> a="Hello Python"
>>> a="**"
>>> print(a.join("Hello
Python"))
H**e**l**l**o**
**P**y**t**h**o**n

ljust(width[,fillchar])
	Returns a left justified version of the string
	

>>> a="Hello"
>>> b = a.ljust(12, "_")
>>> print(b)
Hello_______

lower()
	Converts a string into lower case
	

>>> a = "Python"
>>> print(a.lower())
Python

lstrip([chars])
	Returns a left trim version of the string
	

>>> a = " Hello "
>>> print(a.lstrip(), "!")
Hello

maketrans(x[, y[, z]])
	Returns a translation table to be used in translations
	

>>> frm = "SecretCode"
>>> to = "4203040540"
>>> trans_table =
str.maketrans(frm,to)
>>> sec_code = "Secret
Code".translate(trans_table)
>>> print(sec_code)
400304 0540

partition(sep)
	Returns a tuple where the string is parted into three parts
	

>>> mystr = "Hello-Python"
>>> print(mystr.partition("-
"))
('Hello', '-', 'Python')
74
>>>
print(mystr.partition("."))
('Hello-Python', '', '')

replace(old, new[,count])
	Returns a string where a specified value is replaced with a specified value
	

>>> mystr = "Hello Python.
Hello Java. Hello C++."
>>>
print(mystr.replace("Hello",
"Bye"))
Bye Python. Bye Java. Bye
C++.
>>>
print(mystr.replace("Hello",
"Hell", 2))
Hell Python. Hell Java.
Hello C++.

rfind(sub[, start[,end]])
	Searches the string for a specified value and returns the last position of where it was found
	

>>> mystr = "Hello-Python"
>>> print(mystr.rfind("P"))
6
>>> print(mystr.rfind("-"))
5
>>> print(mystr.rfind("z"))
-1

rindex(sub[, start[,end]])
	Searches the string for a specified value and returns the last position of where it was found
	

>>> mystr = "Hello-Python"
>>> print(mystr.rindex("P"))
6
>>> print(mystr.rindex("-"))
5
>>> print(mystr.rindex("z"))
Traceback (most recent call
last):
File "<pyshell#253>", line
1, in <module>
print(mystr.rindex("z"))
ValueError: substring not
found

rjust(width[,fillchar])
	Returns the string right justified in a string of length width.
	

>>> mystr = "Hello Python"
>>> mystr1 = mystr.rjust(20,
"-")
>>> print(mystr1)
--------Hello Python

rpartition(sep)
	Returns a tuple where the string is parted into three parts
	

>>> mystr = "Hello Python"
>>>
print(mystr.rpartition("."))
('', '', 'Hello Python')
>>> print(mystr.rpartition("
"))
('Hello', ' ', 'Python')

rsplit(sep=None, maxsplit=-1)
	Splits the string at the specified separator, and returns a list
	

>>> mystr = "Hello Python"
>>> print(mystr.rsplit())
['Hello', 'Python']
>>> mystr = "Hello-Python-
Hello"
>>>
print(mystr.rsplit(sep="-",
maxsplit=1))
['Hello-Python', 'Hello']

rstrip([chars])
	Returns a right trim version of the string
	

>>> mystr = "Hello Python"
>>> print(mystr.rstrip(),
"!")
Hello Python !
>>> mystr = "------------
Hello Python-----------"
>>> print(mystr.rstrip(), "-
")
------------Hello Python----
------- -
>>> print(mystr.rstrip(),
"_")
------------Hello Python----
------- _

split(sep=None, maxsplit=-1)
	Splits the string at the specified separator, and returns a list
	

>>> mystr = "Hello Python"
>>> print(mystr.split())
['Hello', 'Python']
>>> mystr1="Hello,,Python"
>>> print(mystr1.split(","))
['Hello', '', 'Python']

splitlines([keepends])
	Splits the string at line breaks and returns a list
	

>>> mystr = "Hello:\n\n
Python\r\nJava\nC++\n"
>>>
print(mystr.splitlines())
['Hello:', '', ' Python',
'Java', 'C++']
>>>
print(mystr.splitlines(keepe
nds=True))
['Hello:\n', '\n', '
Python\r\n', 'Java\n',
'C++\n']

startswith(prefix[,start[, end]])
	Returns true if the string starts with the specified value
	

>>> mystr = "Hello Python"
>>>
print(mystr.startswith("P"))
False
>>>
print(mystr.startswith("H"))
True
>>>
print(mystr.startswith("Hell
"))
True

strip([chars])
	Returns a trimmed version of the string
	

>>> mystr = "
Hello Python
"
>>> print(mystr.strip(),
"!")
Hello Python !
>>> print(mystr.strip(), "
")
Hello Python

swapcase()
	Swaps cases, lower case becomes upper case and vice versa
	

>>> mystr = "Hello PYthon"
>>> print(mystr.swapcase())
hELLO python

title()
	Converts the first character of each word to upper case
	

>>> mystr = "Hello PYthon"
>>> print(mystr.title())
Hello Python
>>> mystr = "HELLO JAVA"
>>> print(mystr.title())
Hello Java

translate(table)
	Returns a translated string
	

>>> frm = "helloPython"
>>> to = "40250666333"
>>> trans_table =
str.maketrans(frm, to)
>>> secret_code = "Secret
Code".translate(trans_table)
>>> print(secret_code)
S0cr06 C3d0

upper()
	Converts a string into upper case
	

>>> mystr = "hello Python"
>>> print(mystr.upper())
HELLO PYTHON

zfill(width)
	Fills the string with a specified number of 0 values at the beginning
>>> mystr = "999"
>>> print(mystr.zfill(9))
000000999
>>> mystr = "-40"
>>> print(mystr.zfill(5))
-0040


Python strings are not mutable. All string methods return a new string.

== Substring

    str[n:m] → return a substring from index n to m.
    str[:m] → from beginning to m.
    str[n:] → from n to the end, including the end char.

Negative index counts from end, starting with -1

# Python 3

aa = "01234"
print(aa[2:4] == "23") # True

bb = "abcd"
print(bb[0:-2] == "ab") # True

cc = "abcd"
print(cc[2:] == "cd") # True

== Length

len(str) → return the number of chars in str.

# Python 3

a = "this"
print(len(a)) # 4

== Join

str1 + str2 → joins two strings into one.

# Python 3
print("aa" + " bb")

== Repeat

str * n → repeat the string n times.

# Python 3
print("a" * 3)     # aaa

== Search Substring

    str.startswith(prefix,start,end) → Return True if string starts with the prefix, else False. prefix can be a tuple, each element is a string. Optional start, end limits the range of positions to check.
    str.endswith(suffix, start, end) → similar to “startwith”, but check the end.
    str.find(substr,start,end) → Return index of the first occurrence of substr. Return -1 if substr is not found.
    str.rfind(substr,start,end) → similar to “find”, but start at right.
    str.index(substr,start,end) → similar to “find”, but raise ValueError when the substring is not found.
    str.rindex(substr,start,end) → similar to “index” but start from right.
    str.count(substr,start,end) → Return the number of non-overlapping occurrences of substring substr.

in the above, the start and end are optional.

== Find/Replace

    str.replace("old", "new" , count) → replace occurrences of substring. Only first count number of time is done. count is optional.

== Trim String

    str.strip("chars") → remove any char in chars at the leading/trailing ends of the string. The "chars" is a string specifying the set of characters to be removed, defaults to whitespace.
    str.rstrip("chars") → same as “strip”, but only do trailing end.
    str.lstrip("chars") → same as “strip”, but only do beginning end.

== String/List Conversion

    str.join(iterable) → Change a {list, tuple} into a string, by concatenating elements, and use str as separator.
    str.split("sep",maxsplit) → Return a list. Split string using "sep" as the delimiter. If maxsplit is given, at most maxsplit splits are done (result list will have at most maxsplit+1 elements). If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns ['']. If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns []. For example, ' 1  2   3  '.split() returns ['1', '2', '3'], and '  1  2   3  '.split(None, 1) returns ['1', '2   3  '].
    str.rsplit(sep, maxsplit) → same as “split” but begin at right.
    str.splitlines(keepends) → Return a list of the lines in the string, breaking at line boundaries. This method uses the universal newlines approach to splitting lines. Line breaks are not included in the resulting list unless keepends is given and true. For example, 'ab c\n\nde fg\rkl\r\n'.splitlines() returns ['ab c', '', 'de fg', 'kl'], while the same call with splitlines(True) returns ['ab c\n', '\n', 'de fg\r', 'kl\r\n']. Unlike split() when a delimiter string sep is given, this method returns an empty list for the empty string, and a terminal line break does not result in an extra line.
    str.partition(sep) → Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.
    str.rpartition(sep) → same as “partition” but begin at right. 
<!--ID: 1639528994152-->


== Check Character Case, Character Class

    str.isalnum() → Return True if all characters are alphanumeric and there is at least one character, else False.
    str.isalpha() → ◇
    str.isdigit() → ◇
    str.isupper() → ◇
    str.islower() → ◇
    str.isspace() → check whitespace characters.
    str.istitle() → true if every word start with cap letter.
    unicode.isnumeric() → Return True if there are only numeric characters in S, False otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH.
    unicode.isdecimal() → Return True if there are only decimal characters in S, False otherwise. Decimal characters include digit characters, and all characters that can be used to form decimal-radix numbers, e.g. U+0660, ARABIC-INDIC DIGIT ZERO.

    str.translate(table[, deletechars]) → Return a copy of the string where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256. You can use the maketrans() helper function in the string module to create a translation table. For string objects, set the table argument to None for translations that only delete characters:

== Letter Case Conversion

    str.capitalize() → capitalize the first character
    str.upper() → change to uppercase.
    str.lower() → change to lowercase.
    str.swapcase() → switch uppercase/lowercase.
    str.title() → make each word's first letter uppercase.

== Formatting Related Methods

    str.format(…) → formatting the string. (replace parts with arguments) [see Python: Format String].
    str.center(n) → add space to begin and end of string, so it's centered with respect to n chars.
    str.center(n,"char") → fill it with character char
    str.ljust(width, "fillchar") → Add fillchar to the end of string, so total length is width. fillchar defaults to space. The original string is returned if width is less than or equal to given string length.
    str.rjust(width, "fillchar") → same as “ljust” but done pads on the left.
    str.zfill(width) → Return the numeric string left filled with zeros in a string of length width. A sign prefix is handled correctly. The original string is returned if width is less than or equal length.
    str.expandtabs() → replace tab char by space.
    str.expandtabs(tabsize) → ◇

# -*- Coding: Utf-8 -*-
# Python 2
# Example of String Ljust
x = """something in water"""
y = x.ljust(30,"-")
print y
# Something in Water------------

== String Character Encoding/Decoding, Unicode

    str.decode(coding) → Decode the string using coding.
    str.encode(coding) → Encoded the string using coding.

For a list of possible encodings, see python doc “Standard Encodings”.

## String Methods


Python has a set of built-in methods that you can use on strings.
Example

The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
Example

The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())
Example

The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
Example

The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
Example

The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

Learn more about String Methods with our String Methods Reference
Check String

To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
Example

Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
Example

Check if the phrase "ain" is NOT present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

String Methods

Python has a set of built-in methods that you can use on strings.

Note: All string methods returns new values. They do not change the original string.
Method 	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle() 	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning


String: Commands

# Strips All Whitespace Characters from both Ends
<str>  = <str>.strip()
# Strips All Passed Characters from both Ends
<str>  = <str>.strip('<chars>')

# Splits on One or More Whitespace Characters
<list> = <str>.split()
# Splits on 'sep' Str at Most 'maxsplit' times
<list> = <str>.split(sep=None, maxsplit=-1)
# Splits on line Breaks. Keeps Them if 'keepends'
<list> = <str>.splitlines(keepends=False)
# Joins Elements Using String as Separator
<str>  = <str>.join(<coll_of_strings>)

# Checks if String Contains a Substring
<bool> = <sub_str> in <str>
# Pass Tuple of Strings for Multiple Options
<bool> = <str>.startswith(<sub_str>)
# Pass Tuple of Strings for Multiple Options
<bool> = <str>.endswith(<sub_str>)
# Returns Start Index of First Match or -1
<int>  = <str>.find(<sub_str>)
# Same but Raises ValueError if Missing
<int>  = <str>.index(<sub_str>)

# Replaces 'old' with 'new' at Most 'count' times
<str>  = <str>.replace(old, new [, count])
# True if Str Contains only Numeric Characters
<bool> = <str>.isnumeric()
# Nicely Breaks String into Lines
<list> = textwrap.wrap(<str>, width)

    Also: 'lstrip()', 'rstrip()'.
    Also: 'lower()', 'upper()', 'capitalize()' and 'title()'.

Char

# Converts Int to Unicode Char
<str> = chr(<int>)
# Converts Unicode Char to Int
<int> = ord(<str>)

>>> ord('0'), ord('9')
(48, 57)
>>> ord('A'), ord('Z')
(65, 90)
ord('a'), ord('z')
(97, 122)


Value conversion:

The new-style simple formatter calls by default the __format__() method of an object for its representation. If you just want to render the output of str(...) or repr(...) you can use the !s or !r conversion flags.

In %-style you usually use %s for the string representation but there is %r for a repr(...) conversion.

Setup:

class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

Example-1:

class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'
x='{0!s} {0!r}'.format(Data())
print (x)
<!--ID: 1639528994170-->


Output:

str repr

In Python 3 there exists an additional conversion flag that uses the output of repr(...) but uses ascii(...) instead.

Example-2:

class Data(object):

    def __repr__(self):
        return 'räpr'
x='{0!r} {0!a}'.format(Data())
print(x)
<!--ID: 1639528994189-->


Output:

räpr r\xe4pr

Padding and aligning strings:

A value can be padded to a specific length. See the following examples where the value '15' is encoded as part of the format string.

Note: The padding character can be spaces or a specified character.

Example:

Align right:

>>> '{:>15}'.format('Python')
'         Python'
>>>
<!--ID: 1639528994207-->


Align left:

>>> '{:15}'.format('Python')
'Python         '
>>>
<!--ID: 1639528994227-->


By argument:

In the previous example, the value '15' is encoded as part of the format string. It is also possible to supply such values as an argument.

Example:

>>> '{:<{}s}'.format('Python', 15)
'Python         '
>>>
<!--ID: 1639528994243-->


In the following example we have used '*' as a padding character.

Example:

>>> '{:*<15}'.format('Python')
'Python*********'
>>>
<!--ID: 1639528994263-->


Align center:

Example:

>>> '{:^16}'.format('Python')
'     Python     '
>>>
<!--ID: 1639528994279-->


Truncating long strings:

In the following example, we have truncated ten characters from the left side of a specified string.

Example:

>>> '{:.10}'.format('Python Tutorial')
'Python Tut'
>>>
<!--ID: 1639528994292-->


By argument:

Example:

>>> '{:.{}}'.format('Python Tutorial', 10)
'Python Tut'
>>>

Combining truncating and padding

In the following example, we have combined truncating and padding.

Example:

>>> '{:10.10}'.format('Python')
'Python    '
>>>
<!--ID: 1639528994314-->


Numbers:

Integers:

>>> '{:d}'.format(24)
'24'
>>>
<!--ID: 1639528994333-->


Floats:

>>> '{:f}'.format(5.12345678123)
'5.123457'
>>>
<!--ID: 1639528994345-->


Padding numbers:

Similar to strings numbers.

Example-1:

>>> '{:5d}'.format(24)
'   24'
>>>
<!--ID: 1639528994373-->


The padding value represents the length of the complete output for floating points. In the following example '{:05.2f}' will display the float using five characters with two digits after the decimal point.
<!--ID: 1639528994393-->


Example-2:

>>> '{:05.2f}'.format(5.12345678123)
'05.12'
>>>
<!--ID: 1639528994406-->


Signed numbers:

By default only negative numbers are prefixed with a sign, but you can display numbers prefixed with the positive sign also.

Example-1:

>>> '{:+d}'.format(24)
'+24'
>>>
<!--ID: 1639528994432-->


You can use a space character to indicate that negative numbers (should be prefixed with a minus symbol) and a leading space should be used for positive numbers.

Example-2:

>>> '{: d}'.format((- 24))
'-24'
>>>
<!--ID: 1639528994454-->


Example-3:

>>> '{: d}'.format(24)
' 24'
>>>
<!--ID: 1639528994468-->


You can control the position of the sign symbol relative to the padding.

Example-4:

>>> '{:=6d}'.format((- 24))
'-   24'
>>>
<!--ID: 1639528994496-->


Named placeholders:

Both formatting styles support named placeholders. Here is an example:

Example-1:

>>> data = {'first': 'Place', 'last': 'Holder!'}
>>> '{first} {last}'.format(**data)
'Place Holder!'
>>>
<!--ID: 1639528994511-->


.format() method can accept keyword arguments.

Example-2:

>>> '{first} {last}'.format(first='Place', last='Holder!')
'Place Holder!'
>>>
<!--ID: 1639528994541-->


Datetime:

You can format and print datetime object as per your requirement.

Example:

>>> from datetime import datetime
>>> '{:%Y-%m-%d %H:%M}'.format(datetime(2016, 7, 26, 3, 57))
'2016-07-26 03:57'
>>>
<!--ID: 1639528994556-->



Repeat String
Sometimes we need to repeat the string in the program, and we can do this easily by using the repetition operator in Python.

The repetition operator is denoted by a '*' symbol and is useful for repeating strings to a certain length.

str = 'Python program'
print(str*3)

The above lines of code will display the following outputs:

Python programPython programPython program

Similarly, it is also possible to repeat any part of the string by slicing:

str = 'Python program'
print(str[7:9]*3) \#Repeats the seventh and eighth character three times

prprpr


Remove Space From a String
Spaces are also considered as a character inside a string, and sometimes unnecessary spaces in the string cause wrong results.

For example, instead of typing 'Alex', a person typed his name 'Alex  ' (see two spaces at the end of the string), and if we compare them using the '==' operator.

if 'Alex' == 'Alex  ':
    print ("Hello Alex!")
else:
    print ("Not found")

Not found

The output of the above program will be 'not found', and this way, additional spaces may lead to wrong results. Therefore, such blank spaces should be removed from the string before being used. This is possible by using rstrip(), lstrip() and strip() methods in Python. These three functions do the same thing, but there is a slight difference between these three functions.
Function	Description
rstrip()	rstrip() method removes whitespace at the end of a string.
lstrip()	lstrip() method removes whitespace at the beginning of a string.
strip()	strip() method removes whitespace at the beginning and end (both sides) of a string.

These three methods do not remove empty spaces between the strings and are usually used where the input is taken from the user.

name = '  Chris Gayle  '
\#remove spaces from left
print (name.lstrip())

\#remove spaces from right
print (name.rstrip())

\#remove spaces from both side
print (name.strip())

Chris Gayle  
  Chris Gayle
Chris Gayle



Iterate String

To iterate through a string in Python, “for…in” notation is used.
str = "hello"
for c in str:
  print(c)
  
\# h
\# e
\# l
\# l
\# o


Python String .format()

The Python string method .format() replaces empty brace ({}) placeholders in the string with its arguments.

If keywords are specified within the placeholders, they are replaced with the corresponding named arguments to the method.
msg1 = 'Fred scored {} out of {} points.'
msg1.format(3, 10)
\# => 'Fred scored 3 out of 10 points.'
<!--ID: 1639528994584-->


msg2 = 'Fred {verb} a {adjective} {noun}.'
msg2.format(adjective='fluffy', verb='tickled', noun='hamster')
\# => 'Fred tickled a fluffy hamster.'
String Method .lower()
<!--ID: 1639528994603-->


The string method .lower() returns a string with all uppercase characters converted into lowercase.
greeting = "Welcome To Chili's"

print(greeting.lower())
\# Prints: welcome to chili's
String Method .strip()

The string method .strip() can be used to remove characters from the beginning and end of a string.

A string argument can be passed to the method, specifying the set of characters to be stripped. With no arguments to the method, whitespace is removed.
text1 = '   apples and oranges   '
text1.strip()       # => 'apples and oranges'

text2 = '...+...lemons and limes...-...'

\# Here we strip just the "." characters
text2.strip('.')    # => '+...lemons and limes...-'

\# Here we strip both "." and "+" characters
text2.strip('.+')   # => 'lemons and limes...-'

\# Here we strip ".", "+", and "-" characters
text2.strip('.+-')  # => 'lemons and limes'
String Method .title()

The string method .title() returns the string in title case. With title case, the first character of each word is capitalized while the rest of the characters are lowercase.
my_var = "dark knight"
print(my_var.title())

\# Prints: Dark Knight
String Method .split()

The string method .split() splits a string into a list of items:

    If no argument is passed, the default behavior is to split on whitespace.
    If an argument is passed to the method, that value is used as the delimiter on which to split the string.

text = "Silicon Valley"

print(text.split())
\# Prints: ['Silicon', 'Valley']

print(text.split('i'))  
\# Prints: ['S', 'l', 'con Valley']
Python string method .find()

The Python string method .find() returns the index of the first occurrence of the string passed as the argument. It returns -1 if no occurrence is found.
mountain_name = "Mount Kilimanjaro"
print(mountain_name.find("o")) # Prints 1 in the console.
String replace

The .replace() method is used to replace the occurence of the first argument with the second argument within the string.

The first argument is the old substring to be replaced, and the second argument is the new substring that will replace every occurence of the first one within the string.
fruit = "Strawberry"
print(fruit.replace('r', 'R'))

\# StRawbeRRy
String Method .upper()

The string method .upper() returns the string with all lowercase characters converted to uppercase.
dinosaur = "T-Rex"

print(dinosaur.upper())
\# Prints: T-REX
String Method .join()

The string method .join() concatenates a list of strings together to create a new string joined with the desired delimiter.

The .join() method is run on the delimiter and the array of strings to be concatenated together is passed in as an argument.
x = "-".join(["Codecademy", "is", "awesome"])

print(x)
\# Prints: Codecademy-is-awesome



10. Python String Functions

Python provides us with a number of functions that we can apply on strings or to create strings.
a. len()

The len() function returns the length of a string.
>>> a='book'
>>> len(a)

4

You can also use it to find how long a slice of the string is.
>>> len(a[2:])

2
b. str()

This function converts any data type into a string.
>>> str(2+3j)

‘(2+3j)’
>>> str(['red','green','blue'])

“[‘red’, ‘green’, ‘blue’]”
c. lower() and upper()

These methods return the string in lowercase and uppercase, respectively.
>>> a='Book'
>>> a.lower()

‘book’
>>> a.upper()

‘BOOK’
d. strip()

It removes whitespaces from the beginning and end of the string.
>>> a='  Book '
>>> a.strip()

‘Book’
e. isdigit()

Returns True if all characters in a string are digits.
>>> a='777'
>> a.isdigit()

True
>>> a='77a'
>>> a.isdigit()

False
f. isalpha()

Returns True if all characters in a string are characters from an alphabet.
>>> a='abc'
>>> a.isalpha()

True
>>> a='ab7'
>>> a.isalpha()

False
g. isspace()

Returns True if all characters in a string are spaces.
>>> a='   '
>>> a.isspace()

True
>>> a=' \'  '
>>> a.isspace()

False
h. startswith()

It takes a string as an argument, and returns True is the string it is applied on begins with the string in the argument.
>>> a.startswith('un')

True
i. endswith()

It takes a string as an argument, and returns True if the string it is applied on ends with the string in the argument.
>>> a='therefore'
>>> a.endswith('fore')

True
j. find()

It takes an argument and searches for it in the string on which it is applied. It then returns the index of the substring.
>>> 'homeowner'.find('meow')

2

If the string doesn’t exist in the main string, then the index it returns is 1.
>>> 'homeowner'.find('wow')
-1
k. replace()

It takes two arguments. The first is the substring to be replaced. The second is the substring to replace with.
>>> 'banana'.replace('na','ha')

‘bahaha’
l. split()

It takes one argument. The string is then split around every occurrence of the argument in the string.
>>> 'No. Okay. Why?'.split('.')

[‘No’, ‘ Okay’, ‘ Why?’]
m. join()

It takes a list as an argument and joins the elements in the list using the string it is applied on.
>>> "*".join(['red','green','blue'])

‘red*green*blue’

Learn: Python Functions with Syntax and Examples

11. Python String Operations
Python String Operations

Python String Operations
a. Comparison

Python Strings can compare using the relational operators.
>>> 'hey'<'hi'

True

‘hey’ is lesser than ‘hi lexicographically (because i comes after e in the dictionary)
>>> a='check'
>>> a=='check'

True
>>> 'yes'!='no'

True
b. Arithmetic

Some arithmetic operations can be applied on strings.
>>> 'ba'+'na'*2

‘banana’
c. Membership

The membership operators of Python can be used to check if string is a substring to another.
>>> 'na' in 'banana'

True
>>> 'less' not in 'helpless'

False
d. Identity

Python’s identity operators ‘is’ and ‘is not’ can be used on strings.
>>> 'Hey' is 'Hi'

False
>>> 'Yo' is not 'yo'

True
e. Logical

Python’s and, or, and not operators can be applied too. An empty string has a Boolean value of False.

1. and- If the value on the left is True it returns the value on the right. Otherwise, the value on the left is False, it returns False.
>>> '' and '1'

”
>>> '1' and ''

”
2. or- If the value on the left is True, it returns True. Otherwise, the value on the right is returned.

3. not- As we said earlier, an empty string has a Boolean value of False.
>>> not('1')

False
>>> not('')

True

center(), count(), find(), format(), isalnum(), lower(), maketrans(), replace()

## Unsorted
Changing Case in a String with Methods - a method is an action that Python c an perform on a piece of data
  the dot(.) in print(name.title()) \# tell Python to make the title() method act on variable
  every method is followed by a set of parenthesis, because methods often need additional information to do their work. that information is provided inside the parentheses
  .title() \# changes title case to capital letters
  .upper() \# all upper case letters
  .lower() \# all lower case letters
      useful for storing data

F-Strings The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.
  f{} or format()
      first_name = "ada"
      last_name = "lovelace"
      full_name = f"{first_name} {last_name}"
<!--ID: 1639528994619-->



Whitespace refer to any nonprinting character, such as spaces, tabs, and end-of-line symbols
  Adding Whitespace to Strings with Tabs or Newlines
      To add a tab to your text, use the character combination \t
          print("\tPython")
      To add a newline in a string, use the character combination \n
          print("Languages:\nPython\nC\nJavaScript")
      You can also combine tabs and newlines in a single string. The string "\n\t" tells Python to move to a new line, and start the next line with a tab.
          print("Languages:\n\tPython\n\tC\n\tJavaScript")
  Stripping Whitespace
      When Python detects extras space "python " it considers it significant unless told otherwise
          .strip() \# removes whitespace on both sides of a string temporarily
          .rstrip() \# removes whitespace on right end of a string temporarily
          .lstrip() \# removes whitespace on left end of a string temporarily
          to remove permanently add strip function to the variable name

Strings (and their methods)
  - is a block of text
  - Multi-line Strings (""" or ''')
x = "Hello World" 	str

They can be enclosed in single quotes ('...') or double quotes ("...") with the same result . \ can be used to escape quotes
If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote
String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line
Strings can be concatenated (glued together) with the + operator, and repeated with *
Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
This feature is particularly useful when you want to break long strings:
This only works with two literals though, not with variables or expressions:
If you want to concatenate variables or a variable and a literal, use +
Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
Indices may also be negative numbers, to start counting from the right:
Note that since -0 is the same as 0, negative indices start from -1.
In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
Note how the start is always included, and the end always excluded. This makes sure that s[:i] + s[i:] is always equal to s:
Slice indices have useful defaults; an omitted first index defaults to zero, an omitted second index defaults to the size of the string being sliced.
One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:
The first row of numbers gives the position of the indices 0…6 in the string; the second row gives the corresponding negative indices. The slice from i to j consists of all characters between the edges labeled i and j, respectively.
For non-negative indices, the length of a slice is the difference of the indices, if both are within bounds. For example, the length of word[1:3] is 2.
Attempting to use an index that is too large will result in an error:
However, out of range slice indexes are handled gracefully when used for slicing

  #python #string #methods
