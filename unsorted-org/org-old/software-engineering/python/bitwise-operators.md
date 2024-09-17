---
title: Bitwise Operators `&, |, ^, >>, <<, ~`
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-53
reference: 
description: 
aliases: 
tags: 
---
# Bitwise Operators `&, |, ^, >>, <<, ~`

  Bitwise operators manipulate numbers on bit level.

Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers:
Operator 	Name 	Description
&  	AND 	Sets each bit to 1 if both bits are 1
| 	OR 	Sets each bit to 1 if one of two bits is 1
 ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
~  	NOT 	Inverts all the bits
<< 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

Python Bitwise Operators
Operator 	Shorthand 	Expression 	Description
& 	And 	x & y 	Bits that are set in both x and y are set.
| 	Or 	x | y 	Bits that are set in either x or y are set.
^ 	Xor 	x ^ y 	Bits that are set in x or y but not both are set.
~ 	Not 	~x 	Bits that are set in x are not set, and vice versa.
<< 	Shift left 	x <<y 	Shift the bits of x, y steps to the left
>> 	Shift right 	x >>y 	Shift the bits of x, y steps to the right.

`# Each step means 'multiply by two'`
* Each step means 'divide by two'

These operators are used to manipulate with bits, & performs bit-by-bit operations.

There are six types of bitwise operators supported by Python. These are:
Python Bitwise OperatorsSymbol	Operator Name	Description
&	Binary AND	This operator copies the bit to the result if it exists in both operands.
|	Binary OR	This operator copies the bit if it exists in either of the operands.
^	Binary XOR	This operator copies the bit if it is set in one operand but not both.
~	Binary 1s Complement	This is a unary operator and has the ability of 'flipping' bits.
<<	Binary Left Shift	The left operands value is moved left by the number of bits specified by the right operand using this operator.
>>	Binary Right Shift	The left operands value is moved right by the number of bits specified by the right operand using this operator.

Python Bitwise Operator

Let us now look at Bitwise Python Operator.
Python Operator

Bitwise Operators in Python

On the operands, these operate bit by bit.

a. Binary AND(&)

It performs bit by bit AND operation on the two values. Here, binary for 2 is 10, and that for 3 is 11. &-ing them results in 10, which is binary for 2. Similarly, &-ing 011(3) and 100(4) results in 000(0).
>>> 2&3

Output: 2
>>> 3&4

Output: 0

b. Binary OR(|)

It performs bit by bit OR on the two values. Here, OR-ing 10(2) and 11(3) results in 11(3).
>>> 2|3

Output: 3

ENJOYING NETFLIX??? Python developers are the reason for its popularity.

Check out how Python is used at Netflix?

c. Binary XOR(^)

It performs bit by bit XOR(exclusive-OR) on the two values. Here, XOR-ing 10(2) and 11(3) results in 01(1).
>>> 2^3

Output: 1

d. Binary One’s Complement(~)

It returns the one’s complement of a number’s binary. It flips the bits. Binary for 2 is 00000010. Its one’s complement is 11111101. This is binary for -3. So, this results in -3. Similarly, ~1 results in -2.
>>>~-3

Output: 2

Again, one’s complement of -3 is 2.

e. Binary Left-Shift(<<)

It shifts the value of the left operand the number of places to the left that the right operand specifies. Here, binary of 2 is 10. 2<<2 shifts it two places to the left. This results in 1000, which is binary for 8.
>>> 2<<2

Output: 8

f. Binary Right-Shift(>>)

It shifts the value of the left operand the number of places to the right that the right operand specifies. Here, binary of 3 is 11. 3>>2 shifts it two places to the right. This results in 00, which is binary for 0. Similarly, 3>>1 shifts it one place to the right. This results in 01, which is binary for 1.
>>> 3>>2
>>> 3>>1

Output: 1


1. Python Bitwise Operators

Previously, in our tutorial on Python Operators., Today, in this Python Bitwise Operators Tutorial, we will discuss Python Bitwise AND, OR, XOR, Left-shift, Right-shift, and 1’s complement Bitwise Operators in Python Programming. Along with this, we will discuss syntax and example of Python Bitwise Operators.

So, let’s start the Python Bitwise Operators Tutorial.
Python Bitwise Operators with Syntax and Example

Python Bitwise Operators with Syntax and Example

Learn: Python Functions with Syntax and Examples
2. Introduction to Python Bitwise Operators

Python Bitwise Operators take one to two operands, and operates on it/them bit by bit, instead of whole. To take an example, let’s see the ‘and’ and ‘&’ operators for the same thing.

Let’s take two numbers- 5 and 7. We’ll show you their binary equivalents using the function bin().
>>> bin(5)

‘0b101’
>>> bin(7)

‘0b111’

Now let’s try applying ‘and’ and ‘&’ to 5 and 7.
>>> 5 and 7

7
>>> 5&7

5

You would have expected them to return the same thing, but they’re not the same. One acts on the whole value, and one acts on each bit at once.

Actually, ‘and’ sees the value on the left. If it has a True Boolean value, it returns whatever value is on the right. Otherwise, it returns False. So, here, 5 and 7 is the same as True and 7. Hence, it returns 7. However, 5&7 is the same as 101&111. This results in 101, which is binary for 5. Let’s look at each of these operators bit by bit (pun intended).

Learn: Loops in Python with Syntax and Examples

Let’s move ahead with next Python Bitwise Operator
3. Python Bitwise AND (&) Operator

1 has a Boolean value of True, and 0 has that of False. Take a look at the following code.
>>> True/2

0.5
>>> False*2

0

This proves something. Now, the binary and (&) takes two values and performs an AND-ing on each pair of bits. Let’s take an example.
>>> 4 & 8

Binary for 4 is 0100, and that for 8 is 1000. So when we AND the corresponding bits, it gives us 0000, which is binary for 0. Hence, the output.

The following are the values when &-ing 0 and 1.

Table.1 Python Bitwise Operators – AND Operators
0 & 0 	0
0 & 1 	0
1 & 0 	0
1 & 1 	1

As you can see, an &-ing returns 1 only if both bits are 1.

You cannot, however, & strings.
>>> '$'&'%'

Traceback (most recent call last):

File “<pyshell#30>”, line 1, in <module>

‘$’&’%’

TypeError: unsupported operand type(s) for &: ‘str’ and ‘str’

Since Boolean values True and False have equivalent integer values of 1 and 0, we can & them.
>>> False&True

False
>>> True&True

True

Let’s try a few more combinations.
>>> 1&True

1
>>> 1.0&1.0

Traceback (most recent call last):

File “<pyshell#36>”, line 1, in <module>

1.0&1.0

TypeError: unsupported operand type(s) for &: ‘float’ and ‘float’

You can also type your numbers directly in binary, as we discussed in section 6a in our Python Numbers tutorial.
>>> 0b110 & 0b101

4

Here, 110 is binary for 6, and 101 for 5. &-ing them, we get 100, which is binary for 4.

Learn: Loops in Python with Syntax and Examples
4. Python Bitwise OR (|) Operators

Now lets discuss Python Bitwise OR (|) Operator

Compared to &, this one returns 1 even if one of the two corresponding bits from the two operands is 1.

Table.2 Python Bitwise Operators – OR Operators
0|0 	0
0|1 	1
1|0 	1
1|1 	1
>>> 6|1

7

This is the same as the following.
>>> 0b110|0b001

7

Let’s see some more examples.
>>> True|False

True

Learn: Python Decision Making Statements with Syntax and Examples

Lets move to another Python Bitwise Operator
5. Python Bitwise XOR (^) Operator

XOR (eXclusive OR) returns 1 if one operand is 0 and another is 1. Otherwise, it returns 0.

Table.1 Python Bitwise Operators – XOR Operators
0^0 	0
0^1 	1
1^0 	1
1^1 	0

Let’s take a few examples.
>>> 6^6

Here, this is the same as 0b110^0b110. This results in 0b000, which is binary for 0.
>>> 6^0

6

This is equivalent to 0b110^0b000, which gives us 0b110. This is binary for 6.
>>> 6^3

5

Here, 0b110^0b011 gives us 0b101, which is binary for 5.

Learn: Python Namespace and Variable Scope – Local and Global Variables

Now lets discuss Bitwise 1’s Complement (~)
6. Bitwise 1’s Complement (~)

This one is a bit different from what we’ve studied so far. This operator takes a number’s binary, and returns its one’s complement. For this, it flips the bits until it reaches the first 0 from right. ~x is the same as -x-1.
>>> ~2

-3
>>> bin(2)

‘0b10’
>>> bin(-3)

‘-0b11’

To make it clear, we mention the binary values of both. Another example follows.
>>> ~45

-46
>>> bin(45)

‘0b101101’
>>> bin(-46)

‘-0b101110’

Learn: Comparison Operator in Python with Syntax and Examples
7. Python Bitwise Left-Shift Operator (<<)

Finally, we arrive at left-shift and right-shift operators. The left-shift operator shifts the bits of the number by the specified number of places. This means it adds 0s to the empty least-significant places now. Let’s begin with an unusual example.
>>> True<<2

4

Here, True has an equivalent integer value of 1. If we shift it by two places to the left, we get 100. This is binary for 4.

Now let’s do it on integers.
>>> 2<<1

4

10 shifted by one place to the left gives us 100, which is, again, 4.
>>> 3<<2

12

Now, 11 shifted to the left by two places gives us 1100, which is binary for 12.

Now lets move to Next Python Bitwise Operator

Learn: Bitwise Operator in Python with Syntax and Example
8. Python Bitwise Right-Shift Operator (>>)

Now we’ll see the same thing for right-shift. It shifts the bits to the right by the specified number of places. This means that those many bits are lost now.
>>> 3>>1

1

3 has a binary value of 11, which shifted one place to the right returns 1. But before closing on this tutorial, we’ll take one last example.

Let’s check what’s the decimal value for 11111.
>>> int(0b11111)

31

Now, let’s shift it three places to the right.
>>> 31>>3

3

As you can see, it gives us 3, whose binary is 11. Makes sense, doesn’t it?


