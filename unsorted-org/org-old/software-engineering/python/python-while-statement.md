---
title: Python-while-statement
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-51
reference: 
description: 
aliases: 
tags: 
---
# Python-while-statement
= Python while Statement WIP

Definite iteration: the number of repetitions is determined when the loop starts.
Definite iteration: performed with a for statement(s) (loop).
Definite iteration: is made of iterables and iterators
Indefinite iteration: the code block executes repeatedly until some condition is True.
Indefinite iteration: performed with a while statement(s) (loop).
Loops: a programming structure that implements iteration.
Loops: execute a sequence of statements several time in succession.
Two types of Iteration: Indefinite and Definite.
Iteration: Repetitive execution of the same block code.

<g_var>=<value>;
while <expr>:
    <statement(s)>;
    break \# terminate the loop
    <statement(s)>;
    continue \# restart the loop
    <statement(s)>;
    else: \# execute when the loop is exhausted.
    <statement(s)>;
<following statement(s)>
<statement(s)> represents the block to be repeatedly executed.
<statement(s)> often referred to as the body of the loop.
<statement(s)> denoted with indentation
<expr> invokes one or more variables then modified somewhere in the loop body.
<expr> valid Python Boolean expression.
<expr> if True, the loop body is executed, then checked again
<expr> if False, proceed to next statement beyond the loop body
<expr> is checked every time loop starts.
<expr> is always checked at start of loop.

while statement(s); execute a set of statement(s) as long the given condition is True
while statement(s); requires variables to be initialize, before loop is executed

i = 0 \# count to 5 using while statement
while i < 6: print(i); i += 1
if i doesn't increment, the loop becomes an infinite loop.

Infinite Loop; never becomes False.
Infinite Loop; is a loop that never terminates.
Infinite Loops result; when the conditions of the loop prevent it from terminating.
Infinite Loops caused by; error in conditional statement or error in logic.
Infinite Loop interrupt; press Ctrl-C
x = 10;
while (True):
     print(x)
     x += 1

Pre-tested loops: is also known as while loops.
while statement(s): can be viewed as a repeating if statement.
while statement(s): used in cases where the number of iterations is not known in advance.
always-True; is any non-zero value
always-False; is zero value

.do-while loop
Post-tested loops: is also known as do-while loops.
continues until a given condition satisfies
also called a  post-tested loop.
used when it is necessary to execute the loop at least once (mostly menu driven
programs)


== .break Statement

break/continue statement(s); terminate a loop iteration prematurely.
break statement(s): immediately terminates the loop entirely
break statement(s): then proceed to following statement outside of loop body
continue statement(s): immediately terminates the current loop iteration.
continue statement(s): then starts the next loop iteration.

Loop Control Statements: change execution from its normal sequence.
Loop Control Statements are: break, continue and pass

i = 0
while i <= 10:
  print(i); i += 1; \# stop loop when i is 5 then print break
  if i == 6: break
print('break')

break statement(s): stops the loop even if the condition is True.
break statement(s): skips optional else statement.


.continue Statement
i = 0
while i < 6:
  i += 1 \# if i is 3 restart loop
  if i == 3: continue
  print(i)

== .else Statement

while/for statement(s): optional else statement
while/for statement(s): else statement executes when the loop terminates.

With the else statement we can run a block of code once when the condition no longer is true:
Example

Print a message once the condition is false:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

Python: while and else statement

There is a structural similarity between while and else statement. Both have a block of statement(s) which is only executed when the condition is true. The difference is that block belongs to if statement executes once whereas block belongs to while statement executes repeatedly.

You can attach an optional else clause with while statement, in this case, syntax will be -
while (expression) :
    statement_1
    statement_2
    ......
else :
    statement_3
    statement_4
    ......

The while loop repeatedly tests the expression (condition) and, if it is true, executes the first block of program statements. The else clause is only executed when the condition is false it may be the first time it is tested and will not execute if the loop breaks, or if an exception is raised. If a break statement executes in first program block and terminates the loop then the else clause does not execute. In the following example, while loop calculates the sum of the integers from 0 to 9 and after completing the loop, else statement executes.


x = 0;
s = 0
while (x < 10):
     s = s + x
     x = x + 1
else :
     print('The sum of first 9 integers : ',s)

Output:

The sum of first 9 integers:  45

Flowchart:
Python while else loop

Example: while loop with if-else and break statement

x = 1;
s = 0
while (x < 10):
     s = s + x
     x = x + 1
     if (x == 5):
          break
else :
     print('The sum of first 9 integers : ',s)
print('The sum of ',x,' numbers is :',s)

Output:

The sum of  5  numbers is : 10

In the above example the loop is terminated when x becomes 5. Here we use break statement to terminate the while loop without completing it, therefore program control goes to outside the while - else structure and execute the next print statement.

Flowchart:

== .Nested Loops
Nested Loops	Programmers can use one loop inside another; i.e., they can use for loop inside while or vice - versa or for loop inside for loop or while inside while.

for iterating_var in sequence:
   for iterating_var in sequence:
      \#execute your code
         \#execute your code

for g in range(1, 6):
    for k in range(1, 3):
        print ("%d * %d = %d" % ( g, k, g*k))

1 * 1 = 1
1 * 2 = 2
2 * 1 = 2
2 * 2 = 4
3 * 1 = 3
3 * 2 = 6
4 * 1 = 4
4 * 2 = 8
5 * 1 = 5
5 * 2 = 10

These statements are used to change execution from its normal sequence.

Python Nested Loops

In Python, loops can be nested inside other loops. Nested loops can be used to access items of lists which are inside other lists. The item selected from the outer loop can be used as the list for the inner loop to iterate over.
groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

\# This outer loop will iterate over each list in the groups list
for group in groups:
  \# This inner loop will go through each name in each list
  for name in group:
    print(name)


    nested loops: You can use one or more loop inside any another while, for or do..while loop.
