# Membership Operators `in, not in`

  Membership operators are used to test if a sequence is presented in an object.

Python Membership Operators

Membership operators are used to test if a sequence is presented in an object:
Operator 	Description 	Example 	Try it
in  	Returns True if a sequence with the specified value is present in the object 	x in y 	
not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y 	

Python Membership OperatorsSymbol	Operator Name	Description
in	in	The result of this operation becomes True if it finds a value in a specified sequence & False otherwise.
not in	not in	result of this operation becomes True if it doesn't find a value in a specified sequence and False otherwise.

Membership Python Operator

These operators test whether a value is a member of a sequence. The sequence may be a list, a string, or a tuple. We have two membership python operators- ‘in’ and ‘not in’.

a. in

This checks if a value is a member of a sequence. In our example, we see that the string ‘fox’ does not belong to the list pets. But the string ‘cat’ belongs to it, so it returns True. Also, the string ‘me’ is a substring to the string ‘disappointment’. Therefore, it returns true.
>>> pets=[‘dog’,’cat’,’ferret’]
>>> ‘fox’ in pets

Output: False
>>> ‘cat’ in pets

Output: True
>>> ‘me’ in ‘disappointment’

Output: True

b. not in

Unlike ‘in’, ‘not in’ checks if a value is not a member of a sequence.
>>> ‘pot’ not in ‘disappointment’

Output: True

In doubt yet in any Python operator with examples? Please comment.

Don’t you know about the trending Python Project at DataFlair? Here it is – Gender and Age Detection with Python
Python Identity Operator

Let us proceed towards identity Python Operator.

These operators test if the two operands share an identity. We have two identity operators- ‘is’ and ‘is not’.

a. is

If two operands have the same identity, it returns True. Otherwise, it returns False. Here, 2 is not the same as 20, so it returns False. Also, ‘2’ and “2” are the same. The difference in quotes does not make them different. So, it returns True.
>>> 2 is 20

Output: False
>>> ‘2’ is “2”

Output: True

b. is not

2 is a number, and ‘2’ is a string. So, it returns a True to that.
>>> 2 is not ‘2’

Output: True
