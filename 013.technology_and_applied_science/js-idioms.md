---
title: JavaScript Idioms
author: Justin Bealer
date_created: 2024-02-25, 10-53-28
date_modified: 2024-09-17, 09-30-01
reference: 
description: 
aliases: 
tags: 
---
# JavaScript Idioms

## Sorted

1.1 Print hello - Print a literal string on standard output

document.write("hello");

This prints the output to the rendered browser document.

However, this method is "strongly discouraged".

1.2  Print hello - Print a literal string on standard output
console.log('hello');

This prints output to the console on any standard browser.

## Unsorted
 
2
Print Hello 10 times
Loop to execute some code a constant number of times
 
for (let i = 0; i < 10; i++) {
  console.log("Hello");
}

let quarantines the scope of i to the loop, in ES6
Alternative implementation:

let count = 0;
while (count < 10) {
  count++;
  console.log('Hello');
};

Alternative implementation:

[...Array(10)].forEach(() => console.log('Hello'))

Alternative implementation:

console.log( 'Hello\n'.repeat(10) )

String built in function
 
3
Create a procedure
Like a function which doesn't return any value, thus has only side effects (e.g. Print to standard output)
 
var bli = function() {
 console.log('Hello World!!!');
}

Alternative implementation:

function bli() {
 console.log('Hello World!!!');
}

Alternative implementation:

let dog = 'Poodle';
const dogAlert = () => alert(dog);

Alternative implementation:

const greet = who => console.log(`Hi ${who}!`)

Arrow function syntax. It consists of three parts: arguments, arrow and code block.
 
4
Create a function
Create a function which returns the square of an integer
 
function square(x) {
 return x * x;
}

Alternative implementation:

const square = (x) => x * x;

Alternative implementation:

const square = n => n**2

The exponentiation operator is the most expressive way to do this.
Alternative implementation:

const square = (number) => Math.pow(number, 2);

5
Create a 2D Point data structure
Declare a container type for two floating-point numbers x and y
 
var p = { x: 1.122, y: 7.45 };

Types are implicit. Just initialize a variable.
Alternative implementation:

const point = { x: 1, y: 2 };

6
Iterate over list values
Do something with each item x of the list (or array) items, regardless indexes.
 
items.forEach((x) => {
    doSomething(x);
});

Alternative implementation:

for (x of items) {
 doSomething(x);
}

Alternative implementation:

items.forEach(doSomething)

No anonymous function here, we pass a function directly to forEach
Alternative implementation:

for (var i = 0; i<items.length; i++) {
  var x = items[i];
  doSomething(x);
}

Alternative implementation:

items.map(doSomething)

doSomething is a function
 
7
Iterate over list indexes and values
Print each index i with its value x from an array-like collection items
 
items.forEach((val, idx) => {
  console.log("index=" + idx + ", value=" + val);
});

This is the functional way of iterating.
Alternative implementation:

for (var i in items) {
   console.log("index=" + i + ", value=" + items[i]);
}

this is a horrible implementation, use the "functional" one above. If you don't need the index, using "for...of" is ok, "for...in" almost never is.
 
8
Create a map (associative array)
Create a new map object x, and provide some (key, value) pairs as initial content.
 
const x = {one: 1, two:2}

An object in JavaScript is essentially an associative array
Alternative implementation:

const x = new Map();
x.set("one", 1);
x.set("two", 2);

From ES2015
Alternative implementation:

const x = new Map([["one",1],["two",2]]);

The Map constructor can take an array of [key, value] pairs.
 
9
Create a Binary Tree data structure
The structure must be recursive because left child and right child are binary trees too. A node has access to children nodes, but not to its parent.
 
class Node {
  constructor (data) {
    this.data = data
    this.left = null
    this.right = null
  }
}

10
Shuffle a list
Generate a random permutation of the elements of list x
 
for (var i = x.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var temp = x[j];
    x[j] = x[i];
    x[i] = temp;
}

Shuffle a list in-place using the Fisher-Yates algorithm.
 
11
Pick a random element from a list
The list x must be non-empty.
 
x[Math.floor(Math.random() * x.length)]

Note that Math.random is not cryptographically secure.
Alternative implementation:

x[~~(Math.random() * x.length)];

~~ is a faster way to call Math.floor().

Note that Math.random is not cryptographically secure.
 
12
Check if list contains a value
Check if the list contains the value x.
list is an iterable finite container.
 
return list.indexOf(x) !== -1;

Array.prototype.includes() is preferred but if you are supporting browsers that are 5+ years old, for example IE11, and you are not using a transpiler, then the old syntax with indexOf is generally well-understood.
Alternative implementation:

return list.includes(x);

ES7 (Works on strings from ES6)
 
13
Iterate over map keys and values
Access each key k with its value x from an associative array mymap, and print them.
 
Object.entries(mymap).forEach(([key, value]) => {
 console.log('key:', key, 'value:', value);
});

Alternative implementation:

for (const key in mymap) {
    console.log('key:', key, 'value:', mymap[key]);
}

14
Pick uniformly a random floating point number in [a..b)
Pick a random number greater than or equals to a, strictly inferior to b. Precondition : a < b.
 
a + (b-a) * Math.random();

Alternative implementation:

a + Math.random() * (b - a)

15
Pick uniformly a random integer in [a..b]
Pick a random integer greater than or equals to a, inferior or equals to b. Precondition : a < b.
 
function pick(a, b) {
    return a + Math.floor(Math.random() * (b - a + 1));
}

You have to build it from a floating-point random number. It is important to use floor , not round .
 
16
Depth-first traversal of a binary tree
Call a function f on every node of binary tree bt, in depth-first infix order
 
function dfs(bt) {
 if (bt === undefined) return;
 dfs(bt.left);
 f(bt);
 dfs(bt.right);
}

17
Create a Tree data structure
The structure must be recursive. A node may have zero or more children. A node has access to its children nodes, but not to its parent.
 
class Node {
  constructor (value, children = []) {
    this.value = value
    this.children = children
  }
}

18
Depth-first traversal of a tree
Call a function f on every node of a tree, in depth-first prefix order
 
function DFS(f, root) {
 f(root)
 if (root.children) {
  root.children.forEach(child => DFS(f, child))
 }
}

Works in ES6
 
19
Reverse a list
Reverse the order of the elements of the list x.
This may reverse "in-place" and destroy the original ordering.
 
x = x.reverse();

note that Array.prototype.reverse() not only returns the reversed array, it works in place!
 
20
Return two values
Implement a function search which looks for item x in a 2D matrix m.
Return indices i, j of the matching cell.
Think of the most idiomatic way in the language to return the two values at the same time.
 
function search(m, x) {
    for (var i = 0; i < m.length; i++) {
        for (var j = 0; j < m[i].length; j++) {
            if (m[i][j] == x) {
                return [i, j];
            }
        }
    }
    return false;
}

Return an array if found, or false if not found.
 
21
Swap values
Swap the values of the variables a and b
 
var tmp = a;
a = b;
b = tmp;

Alternative implementation:

[a, b] = [b, a];

ECMA2015 and above
 
22
Convert string to integer
Extract the integer value i from its string representation s (in radix 10)
 
let i = parseInt(s, 10)

parseInt(string, radix);
The radix is an integer between 2 and 36.
Alternative implementation:

const i = Number(s);

Alternative implementation:

const i = +s

23
Convert real number to string with 2 decimal places
Given a real number x, create its string representation s with 2 decimal digits following the dot.
 
num.toFixed(2)

24
Assign to string the japanese word ネコ
Declare a new string s and initialize it with the literal value "ネコ" (which means "cat" in japanese)
 
s = "ネコ";

JavaScript was designed to use unicode.
 
25
Send a value to another thread
Share the string value "Alan" with an existing running process which will then display "Hello, Alan"
 
{
  // in file worker.js
  onmessage = ({data}) => {
    console.log (`Hello, ${data}`)
  }
}
{
  // in file main.js
  const worker = new Worker ('worker.js')
  worker.postMessage ('Alan')
}

Not supported in Internet Explorer or NodeJS.
Alternative implementation:

import { isMainThread, Worker, parentPort } from 'worker_threads';

if (isMainThread) {
  const worker = new Worker(new URL(import.meta.url));
  worker.postMessage('Alan');
} else {
  parentPort.once('message', (message) => {
    console.log(`Hello, ${message}`);
  });
}

Only supported in Node.js
 
26
Create a 2-dimensional array
Declare and initialize a matrix x having m rows and n columns, containing real numbers.
 
var x = [];
for (var i = 0; i < m; i++) {
  x[i] = [];
}

Alternative implementation:

const x = new Array(m).fill(new Array(n).fill(Math.random()));

27
Create a 3-dimensional array
Declare and initialize a 3D array x, having dimensions boundaries m, n, p, and containing real numbers.
 
const x = new Array(m).fill(
  new Array(n).fill(
    new Array(p).fill(Math.random())
  )
)

28
Sort by a property
Sort the elements of the list (or array-like collection) items in ascending order of x.p, where p is a field of the type Item of the objects in items.
 
items.sort(function(a,b) {
  return compareFieldP(a.p, b.p);
});

Implements your own compareFieldP depending on the type of p.
 
29
Remove item from list, by its index
Remove i-th item from list items.
This will alter the original list or return a new list, depending on which is more idiomatic.
Note that in most languages, the smallest valid value for i is 0.
 
let new_list = items.filter(function(val,idx,ary) { return idx != i });

Alternative implementation:

items.splice(i,1);

this will modify the original list (kinda)
 
30
Parallelize execution of 1000 independent tasks
Launch the concurrent execution of procedure f with parameter i from 1 to 1000.
Tasks are independent and f(i) doesn't return any value.
Tasks need not run all at the same time, so you may use a pool.
 
for (let i = 1; i <= 1000; i++) setTimeout(() => f(i), 0);

31
Recursive factorial (simple)
Create the recursive function f which returns the factorial of the non-negative integer i, calculated from f(i-1)
 
function f(i) {
   return i<2 ? 1 : i * f(i-1);
}

Alternative implementation:

const f = i => i === 0 ? 1 : i * f(i-1)

32
Integer exponentiation by squaring
Create function exp which calculates (fast) the value x power n.
x and n are non-negative integers.
 
function exp(x, n) {
   if (n===0) return 1;
   if (n===1) return x;
   return n%2 ? x * exp(x*x, (n-1)/2)
              : exp(x*x, n/2);
}

Alternative implementation:

const exp = Math.pow;

33
Atomically read and update variable
Assign to the variable x the new value f(x), making sure that no other thread may modify x between the read and the write.
 
let x = f(x)

JavaScript is single threaded, so we can be sure that no other thread will modify x in between :3
 
34
Create a set of objects
Declare and initialize a set x containing unique objects of type T.
 
let x = new Set();

35
First-class function : compose
Implement a function compose (A -> C) with parameters f (A -> B) and g (B -> C), which returns the composition function g ∘ f
 
function compose(f,g){
    return function(x){
        return g(f(x));
    };
}

36
First-class function : generic composition
Implement a function compose which returns composition function g ∘ f for any functions f and g having exactly 1 parameter.
 
function compose(f,g){
    return function(x){
        return g(f(x));
    };
}

In Javascript this is valid regardless the type of the inputs and outputs.
Alternative implementation:

const compose = f => g => x => g(f(x));

Curried function is idiomatic in a functional style.

Relies on ES2015 language features (lambda functions)
 
37
Currying
Transform a function that takes multiple arguments into a function for which some of the arguments are preset.
 
function curry (fn, scope) {

    scope = scope || window;
    
    // omit curry function first arguments fn and scope
    var args = Array.prototype.slice.call(arguments, 2);
    
    return function() {
 var trueArgs = args.concat(Array.prototype.slice.call(arguments, 0));
        fn.apply(scope, trueArgs);
    };
}

Call curry on a function, a scope and then just enumerate the arguments you want to be curried in the returned function ;)
Alternative implementation:

const curry = (fn, ...initialArgs) => (...args) => fn(...initialArgs, ...args);

const add = (a, b) => a + b;

const add5 = curry(add, 5);

const result = add5(1) // 6

38
Extract a substring
Find substring t consisting in characters i (included) to j (excluded) of string s.
Character indices start at 0 unless specified otherwise.
Make sure that multibyte characters are properly handled.
 
let t = s.substring(i, j);

Alternative implementation:

let t = s.slice(i, j);

39
Check if string contains a word
Set the boolean ok to true if the string word is contained in string s as a substring, or to false otherwise.
 
var ok = s.indexOf(word) !== -1;

indexOf returns -1 if the word isn't found.
Alternative implementation:

var ok = s.includes(word);

includes was added in ECMAScript 6.
 
41
Reverse a string
Create string t containing the same characters as string s, in reverse order.
Original string s must remain unaltered. Each character must be handled correctly regardless its number of bytes in memory.
 
var t = s.split("").reverse().join("");

42
Continue outer loop
Print each item v of list a which is not contained in list b.
For this, write an outer loop to iterate on a and an inner loop to iterate on b.
 
OUTER:
for (var i in a) {
   for (var j in b) {
      if (a[i] === b[j]) {
         continue OUTER;
      }
   }
   console.log(a[i] + " not in the list");
}

43
Break outer loop
Look for a negative value v in 2D integer matrix m. Print it and stop searching.
 
OUTER:
for (var i in m) {
   for (var j in m[i]) {
      if (m[i][j] < 0) {
         console.log("Negative value found: "+m[i][j]);
         break OUTER;
      }
   }
}

44
Insert element in list
Insert the element x at position i in the list s. Further elements must be shifted to the right.
 
s.splice(i, 0, x);

45
Pause execution for 5 seconds
Sleep for 5 seconds in current thread, before proceeding with the next instructions.
 
setTimeout(function(){
 // Instructions after delay
},5000);

Javascript does not have a sleep function. This execution flow is structured with a callback (it can be a closure).
Unit is millisecond.
Alternative implementation:

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

await sleep(5000);

Can be used only inside an async function!
Alternative implementation:

await new Promise(r => setTimeout(r, 5000));

Can be used only inside an async function!
 
46
Extract beginning of string (prefix)
Create the string t consisting of the 5 first characters of the string s.
Make sure that multibyte characters are properly handled.
 
let t = s.substring(0,5);

47
Extract string suffix
Create string t consisting in the 5 last characters of string s.
Make sure that multibyte characters are properly handled.
 
var t = s.slice(-5);

48
Multi-line string literal
Assign to variable s a string literal consisting in several lines of text, including newlines.
 
let s = "This is a very long string which needs \n" +
        "to wrap across multiple lines because \n" +
        "otherwise my code is unreadable.";

By concatenation.
Alternative implementation:

let s = "This is a very long string which needs \
to wrap across multiple lines because \
otherwise my code is unreadable.";

When using backslashes, indentation inside the string literal must be far left.
Alternative implementation:

let s = `This is a very long string which needs
to wrap across multiple lines because
otherwise my code is unreadable.`;

ES6 template literals
 
49
Split a space-separated string
Build list chunks consisting in substrings of the string s, separated by one or more space characters.
 
let chunks = s.split(/ +/);

50
Make an infinite loop
Write a loop that has no end clause.
 
while (true) {
 // to infinity
}

Alternative implementation:

for(;;) {
 console.log('Oops')
}

51
Check if map contains key
Determine whether the map m contains an entry for the key k
 
k in m

This will lookup a property in the object and its entire prototype chain.
Alternative implementation:

m.hasOwnProperty(k)

This is like "k in m" except it doesn't check up the prototype chain, which is often not what people want.
Alternative implementation:

_m.has(_k)

Uses an actual Map instance, rather than relying on objects and their keys
 
52
Check if map contains value
Determine whether the map m contains an entry with the value v, for some key.
 
Object.values(m).includes(v)

JavaScript objects are hashmaps.
Object.values() converts a hashmap to a list of values.
Array#includes then checks whether v is included.
Alternative implementation:

[...m.values()].includes(v)

Unlike the previous implementation, this works for Map objects rather than normal Objects.
 
53
Join a list of strings
Concatenate elements of string list x joined by the separator ", " to create a single string y.
 
y = x.join(", ");

54
Compute sum of integers
Calculate the sum s of the integer list or array x.
 
var s = x.reduce((a, b) => a + b, 0);

Alternative implementation:

var s = x.reduce((a, b) => a + b)

55
Convert integer to string
Create the string representation s (in radix 10) of the integer value i.
 
var s = i.toString();

Alternative implementation:

var s = i + "";

56
Launch 1000 parallel tasks and wait for completion
Fork-join : launch the concurrent execution of procedure f with parameter i from 1 to 1000.
Tasks are independent and f(i) doesn't return any value.
Tasks need not run all at the same time, so you may use a pool.
Wait for the completion of the 1000 tasks and then print "Finished".
 
{
  // in file worker.js
  onmessage = f
}
{
  // in file main.js
  for (let i = 0; i < 1000; i++) {
    new Worker ('worker.js')
      .postMessage (i)
  }
}

Alternative implementation:

const tasks = [];
for (let i = 0; i < 1000; i++) {
  tasks.push(f(i));
}

await Promise.all(tasks);
console.log("Finished");

Uses the async function f to create 1000 Promises which are await-ed. All tasks are run in a single thread.
 
57
Filter list
Create the list y containing the items from the list x that satisfy the predicate p. Respect the original ordering. Don't modify x in-place.
 
y = x.filter(p);

Keeps all the elements that pass the test p
 
58
Extract file content to a string
Create the string lines from the content of the file with filename f.
 
var fs = require('fs');

fs.readFile(f, (err, lines) => {
    if (err) {
        // Handle error...
    }

    // Work with `lines` here.
}

Uses Node-specific file-system API.
 
59
Write to standard error stream
Print the message "x is negative" to standard error (stderr), with integer x value substitution (e.g. "-2 is negative").
 
const util = require("util");

console.error(util.format("%d is negative", x));

Alternative implementation:

console.error(x, "is negative");

Alternative implementation:

console.error(`${x} is negative`);

60
Read command line argument
Assign to x the string value of the first command line parameter, after the program name.
 
const x = process.argv[2]

This only works on nodeJS because browsers aren't a command line.
process.argv[0] is the filepath you're at.
process.argv[1] is `node` (the command used to run the program).
 
61
Get current date
Assign to the variable d the current date/time value, in the most standard type.
 
var d = Date.now();

This returns the number of milliseconds since epoch (not an object).

See the documentation for support and polyfills for non-modern browsers.
Alternative implementation:

var d = new Date();

62
Find substring position
Set i to the first position of string y inside string x, if exists.

Specify if i should be regarded as a character index or as a byte index.

Explain the behavior when y is not contained in x.
 
let i = x.indexOf(y);

This sets i to -1 if y is not found in x.
 
63
Replace fragment of a string
Assign to x2 the value of string x with all occurrences of y replaced by z.
Assume occurrences of y are not overlapping.
 
var x2 = x.replace(new RegExp(y, 'g'), z);

This works well only if y doesn't contain special regexp characters.
Alternative implementation:

const x2 = x.replaceAll(y, z);

64
Big integer : value 3 power 247
Assign to x the value 3^247
 
let x = 3n ** 247n;

Big integers (arbitrary precision integers) are currently only supported by Chrome, NodeJS, and Firefox.
 
65
Format decimal number
From the real value x in [0,1], create its percentage string representation s with one digit after decimal point. E.g. 0.15625 -> "15.6%"
 
const s = Math.round (x * 1000) / 10 + '%'

Sadly there's no builtin in JavaScript for this sort of thing.
Alternative implementation:

const percentFormatter = new Intl.NumberFormat('en-US', {
  style: 'percent',
  maximumSignificantDigits: 3
});

const s = percentFormatter.format(x);

Uses an Intl.NumberFormat to create a human-readable percentage string.
 
66
Big integer exponentiation
Calculate the result z of x power n, where x is a big integer and n is a positive integer.
 
let z = x**n

x and n should be of type BigInt, which is only supported in NodeJS, Firefox, and Chrome
 
67
Binomial coefficient "n choose k"
Calculate binom(n, k) = n! / (k! * (n-k)!). Use an integer type able to handle huge numbers.
 
const fac = x => x ? x * fac (x - 1) : x + 1
const binom = (n, k) => fac (n) / fac (k) / fac (n - k >= 0 ? n - k : NaN)

JavaScript is concise even when it has no builtins. The integer type (BigInt) is only supported by Firefox, NodeJS, and Chrome at the moment.
 
68
Create a bitset
Create an object x to store n bits (n being potentially large).
 
let x = new Buffer (Math.ceil (n / 8))

Buffers allocate bytes, so we divide n by 8 and take the ceiling of n
 
69
Seed random generator
Use seed s to initialize a random generator.

If s is constant, the generator output will be the same each time the program runs. If s is based on the current value of the system clock, the generator output will be different each time.
 
const seed = require ('seedrandom')

seed (s)

s is impure—it can give different outputs with the same input.
 
70
Use clock as random generator seed
Get the current datetime and provide it as a seed to a random generator. The generator sequence will be different at each run.
 
Math.random ()

Math.random uses the current time to generate a double floating point number from 0 to 1.
Repeated calls will give different outputs each time.
 
71
Echo program implementation
Basic implementation of the Echo program: Print all arguments except the program name, separated by space, followed by newline.
The idiom demonstrates how to skip the first argument if necessary, concatenate arguments as strings, append newline and print it to stdout.
 
console.log(process.argv.slice(2).join(" "));

In JavaScript, process.argv contains two entries that are to be skipped: The JavaScript interpreter, i.e. node, and the script name, i.e. echo.js.
 
73
Create a factory
Create a factory named fact for any sub class of Parent and taking exactly one string str as constructor parameter.
 
class Parent {
    constructor(str) {}
    fact(new_class, str) {
        if (new_class.prototype instanceof Parent) {
            return new new_class(str)
        }
    }
}

class Child extends Parent {}

74
Compute GCD
Compute the greatest common divisor x of big integers a and b. Use an integer type able to handle huge numbers.
 
const gcd = (a, b) => b === 0 ? a : gcd (b, a % b)

Warning: This implementation is not the most efficient. Figure out a more efficient way to do this if you're up for it!
 
75
Compute LCM
Compute the least common multiple x of big integers a and b. Use an integer type able to handle huge numbers.
 
const gcd = (a, b) => b === 0 ? a : gcd (b, a % b)
let x = (a * b) / gcd(a, b)

76
Binary digits from an integer
Create the string s of integer x written in base 2.

E.g. 13 -> "1101"
 
let s = x.toString(2);

77
Complex number
Declare a complex x and initialize it with value (3i - 2). Then multiply it by i.
 
var math = require('mathjs');

var x = math.complex(-2, 3);
x = math.multiply(x, math.i);

JS has no built-in complex numbers. The math.js library was used in this example.
 
78
"do while" loop
Execute a block once, then execute it again as long as boolean condition c is true.
 
do {
   something();
} while (c);

79
Convert integer to floating point number
Declare the floating point number y and initialize it with the value of the integer x .
 
let y = x + .0

You might say "Wait! All JavaScript numbers are floats!"
They certainly always behave like they are on the outside, but on the inside they treat some numbers as integers.
 
80
Truncate floating point number to integer
Declare integer y and initialize it with the value of floating point number x . Ignore non-integer digits of x .
Make sure to truncate towards zero: a negative x must yield the closest greater integer (not lesser).
 
let y = BigInt (x | 0)

`x | 0` chops off the bit of a number after the decimal.
`BigInt`s are a new JavaScript primitive for arbitrarily large integers. They are only supported by Chrome, NodeJS, and Firefox.
 
81
Round floating point number to integer
Declare the integer y and initialize it with the rounded value of the floating point number x .
Ties (when the fractional part of x is exactly .5) must be rounded up (to positive infinity).
 
var y = Math.round(x);

82
Count substring occurrences
Find how many times string s contains substring t.
Specify if overlapping occurrences are counted.
 
let n = 0 // the number of occurences
let acc = s
let i
while ((i = acc.indexOf (t)) + 1) {
  n++
  acc = acc.slice (i + 1)
}

Overlapping occurences are counted.
There's no builtin but at least JavaScript isn't friggin' Pascal.
 
83
Regex with character repetition
Declare regular expression r matching strings "http", "htttp", "httttp", etc.
 
const r = /htt+p/

Sugar for:
const r = new RegExp ('htt+p')
 
84
Count bits set in integer binary representation
Count number c of 1s in the integer i in base 2.

E.g. i=6 → c=2
 
const c = i.toString(2).replace(/[^1]/g, '').length

• Convert the number to binary
• Replace characters that aren't '1' by turning them to ''
• See how long the resulting list of '1's is
 
85
Check if integer addition will overflow
Write boolean function addingWillOverflow which takes two integers x, y and return true if (x+y) overflows.

An overflow may be above the max positive value, or below the min negative value.
 
function addingWillOverflow(x, y) {
  return x > 0 && y > 0 && x > Number.MAX_SAFE_INTEGER - y
}

87
Stop program
Exit immediately.
If some extra cleanup work is executed by the program runtime (not by the OS itself), describe it.
 
process.exit()

88
Allocate 1M bytes
Create a new bytes buffer buf of size 1,000,000.
 
let buf = new Buffer (1e6)

1e6 = 1 * 10 ^ 6
 
89
Handle invalid argument
You've detected that the integer value of argument x passed to the current function is invalid. Write the idiomatic way to abort the function execution and signal the problem.
 
throw new Error ('x is invalid')

Many JavaScript programs have similar structure to Python ones, even though the two languages have differing syntax and behavior.
 
90
Read-only outside
Expose a read-only integer x to the outside world while being writable inside a structure or a class Foo.
 
const Foo = function Counter () {
  let n = 0
  Object.defineProperty (this, 'value', {get: () => n++})
}
{
  const counter = new Foo ()
  counter.value // 0
  counter.value // 1
}

Alternative implementation:

class Foo {
  #x = 123;
  get x() {
    return this.#x;
  }
}

Stores a private property #x in the class Foo which is accessible via a getter.
 
91
Load JSON file into object
Read from the file data.json and write its content into the object x.
Assume the JSON data is suitable for the type of x.
 
const fs = require('fs');

const x = JSON.parse(fs.readFileSync('./data.json'));

Alternative implementation:

const x = require('./data.json');

require() caches when requiring a file for the first time and then uses that cache for future require() calls, so use fs.readFileSync() if the content of the JSON file changes during runtime.
 
92
Save object into JSON file
Write the contents of the object x into the file data.json.
 
const fs = require('fs');

fs.writeFileSync('data.json', JSON.stringify(x));

93
Pass a runnable procedure as parameter
Implement the procedure control which receives one parameter f, and runs f.
 
function control(f){
 f();
}

94
Print the type of a variable
Print the name of the type of x. Explain if it is a static type or dynamic type.

This may not make sense in all languages.
 
console.log(typeof x);

In most cases you'll get "object" unless you put in a primitive or function.
Alternative implementation:

console.log (x == null ? x + '' : x.constructor.name);

Gives you the name of the function used to build x—it always works due to the "everything is an object" principle.
 
95
Get file size
Assign to variable x the length (number of bytes) of the local file at path.
 
const {readFileSync: read} = require ('fs')

let x = read(path).length

Only works with NodeJS (server-side JavaScript) because the browser isn't allowed to access your files.
 
96
Check string prefix
Set the boolean b to true if string s starts with prefix prefix, false otherwise.
 
var b = s.startsWith(prefix);

ECMAScript 6 and above.
Alternative implementation:

var b = (s.lastIndexOf(prefix, 0) === 0);

Note the second parameter to lastIndexOf. This is not, however, the most readable possible code.
 
97
Check string suffix
Set boolean b to true if string s ends with string suffix, false otherwise.
 
var b = s.endsWith(suffix);

ECMAScript 6 and above.
 
98
Epoch seconds to date object
Convert a timestamp ts (number of seconds in epoch-time) to a date with time d. E.g. 0 -> 1970-01-01 00:00:00
 
new Date (ts * 1000)

JavaScript is big on type conversion.
Date is back from the olden days where we ripped our stuff from Java instead of Python :3
 
99
Format date YYYY-MM-DD
Assign to the string x the value of the fields (year, month, day) of the date d, in format YYYY-MM-DD.
 
let x = d.toISOString().slice(0, 10)

toISOString returns a date like "2011-10-05T14:48:00.000Z".

10 is the length of "YYYY-MM-DD".

The builtin Date type has some serious problems. You may want to use a custom date type.
 
100
Sort by a comparator
Sort elements of array-like collection items, using a comparator c.
 
items.sort(c);

c(a, b) returns a number to represent "a lesser than b", "a equals b", or "a greater than b".
 
101
Load from HTTP GET request into a string
Make an HTTP request with method GET to the URL u, then store the body of the response in the string s.
 
<script src="https://code.jquery.com/jquery-1.11.3.js"></script>

$.get(u, function(data){
  s = data;
});

Uses the jQuery library.
Alternative implementation:

var xmlHttp = new XMLHttpRequest();
xmlHttp.onreadystatechange = function() {
 if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
  s = xmlHttp.responseText;
}
xmlHttp.open("GET", u, true);
xmlHttp.send(null);

This is asynchronous.
Alternative implementation:

fetch(u)
  .then(res => res.text())
  .then(text => s = text)

Fetch is a relatively new API and isn't available in IE. A polyfill can be found here: <https://github.com/github/fetch>
Alternative implementation:

const res = await fetch(u)
s = await res.text()

Fetch is a relatively new API and isn't available in IE. A polyfill can be found here: <https://github.com/github/fetch>

Async/await is also an ES2017 feature.
 
105
Current executable name
Assign to the string s the name of the currently executing program (but not its full path).
 
var s = process.argv0;

This assumes a node environment with a process global.
 
106
Get program working directory
Assign to string dir the path of the working directory.
(This is not necessarily the folder containing the executable itself)
 
let dir = process.cwd ()

Only works in NodeJS because JavaScript in the browser does not know about your directories.
 
107
Get folder containing current program
Assign to string dir the path of the folder containing the currently running executable.
(This is not necessarily the working directory, though.)
 
const path = require('path');

const dir = path.resolve();

Alternative implementation:

const dir = __dirname;

108
Determine if variable name is defined
Print the value of variable x, but only if x has been declared in this program.
This makes sense in some languages, not all of them. (Null values are not the point, rather the very existence of the variable.)
 
if (typeof x !== 'undefined') {
    console.log(x);
}

However if x has previously been declared and set to undefined, this will not print x even though x has been declared.
Alternative implementation:

try {
 console.log(x);
} catch (e) {
 if (!e instanceof ReferenceError) {
  throw e;
 }
}

110
Check if string is blank
Set the boolean blank to true if the string s is empty, or null, or contains only whitespace ; false otherwise.
 
const blank = s == null || s.trim() === ''

Because _== is being used instead of ===, undefined will also return true—which is good because it represents the absence of a value just like null.
 
111
Launch other program
From current process, run program x with command-line parameters "a", "b".
 
const { exec } = require('child_process');

exec(`${x} a b`);

This assumes a node.js environment.

See the documentation for examples on how to capture output, and equivalent synchronous commands.

112
Iterate over map entries, ordered by keys
Print each key k with its value x from an associative array mymap, in ascending order of k.
 
[...mymap.entries()].sort().map(([_, x]) => console.log(x))

mymap has type Map.
We have to spread mymap.entries() because it returns an iterator instead of a list.
 
113
Iterate over map entries, ordered by values
Print each key k with its value x from an associative array mymap, in ascending order of x.
Multiple entries may exist for the same value x.
 
Object.entries(mymap)
  .sort((a, b) => a[1] - b[1])
  .forEach(([key, value]) => {
    console.log('key:', key, 'value:', value);
  });

114
Test deep equality
Set boolean b to true if objects x and y contain the same values, recursively comparing all referenced elements in x and y.
Tell if the code correctly handles recursive types.
 
const b = JSON.stringify(x) === JSON.stringify(y);

Won't work for things which aren't serializable (such as functions) or recursive.
Alternative implementation:

const arrayDeepEqual = (a, b) => a.length === b.length && a.every((x, i) => deepEqual(x, b[i]))

const deepEqual = (a, b) =>
  Array.isArray(a) && Array.isArray(b)
    ? arrayDeepEqual(a, b)
    : typeof a == 'object' && a && typeof b == 'object' && b
    ? arrayDeepEqual(Object.entries(a), Object.entries(b))
    : Number.isNaN(a) && Number.isNaN(b) || a === b

const b = deepEqual(x, y)

This does not handle recursive types, Maps/Sets/Dates, the prototype/class of objects, or non-enumerable properties such as symbols.
Alternative implementation:

import {isDeepStrictEqual} from 'util'

const b = isDeepStrictEqual(x, y)

Only works in Node.js. This correctly handles recursive types.

Only enumerable own properties are considered, object wrappers are compared both as objects and unwrapped values, and WeakMap and WeakSet comparisons do not rely on their values.
Alternative implementation:

import _ from 'underscore';

const b = _.isEqual(x, y);

115
Compare dates
Set boolean b to true if date d1 is strictly before date d2 ; false otherwise.
 
let b = d1 < d2

116
Remove occurrences of word from string
Remove all occurrences of string w from string s1, and store the result in s2.
 
var regex = RegExp(w, 'g');
var s2 = s1.replace(regex, '');

Search pattern can also be defined in Regular Expressions. See the documentation.

If a string is used instead of regex, only the first match will be replaced.
Alternative implementation:

const s2 = s1.split(w).join('')

Better not to use a RegExp, in case the word contains dots, asterisks, &c. One may also wish to remove redundant spaces afterward: str.replace(/\s+/g, ' ')
 
117
Get list size
Set n to the number of elements of the list x.
 
var n = x.length;

118
List to set
Create the set y from the list x.
x may contain duplicates. y is unordered and has no repeated values.
 
var y = new Set(x);

The Set function was added to JS in ES2015 (a.k.a ES6).
 
119
Deduplicate list
Remove duplicates from the list x.
Explain if the original order is preserved.
 
x = [...new Set(x)];

Original order is preserved.
Alternative implementation:

x = Array.from(new Set(x));

Original order is preserved.
Alternative implementation:

const seen = new Set();
x = x.filter( v => {
  if(seen.has(v))
    return false;
  seen.add(v);
  return true;
});

Original order is preserved.
 
120
Read integer from stdin
Read an integer value from the standard input into the variable n
 
const {createInterface} = require('readline')

const rl = createInterface ({
  input: process.stdin,
  output: process.stdout
})

rl.question('Input an integer: ', response => {
  let n = parseInt (response)
  // stuff to be done with n goes here

  rl.close()
})

This example only works with nodeJS (server-side JS) because browser JS does not have a standard input.
 
122
Declare an enumeration
Create an enumerated type Suit with 4 possible values SPADES, HEARTS, DIAMONDS, CLUBS.
 
const spades = 0
const hearts = 1
const diamonds = 2
const clubs = 3

Similar to the latter python implementation, this a fake enum.
 
123
Assert condition
Verify that predicate isConsistent returns true, otherwise report assertion violation.
Explain if the assertion is executed even in production environment or not.
 
console.assert(_isConsistent);

124
Binary search for a value in sorted array
Write the function binarySearch which returns the index of an element having the value x in the sorted array a, or -1 if no such element exists.
 
function binarySearch(a, x, i = 0) {
  if (a.length === 0) return -1
  const half = (a.length / 2) | 0
  return (a[half] === x) ?
    i + half :
    (a[half] > x) ?
    binarySearch(a.slice(0, half), x, i) :
    binarySearch(a.slice(half + 1), x, half + i + 1)
}

x | 0 removes the bit of x after the decimal.
This would be easier if JavaScript had more builtins for list processing.
 
125
Measure function call duration
measure the duration t, in nanoseconds, of a call to the function foo. Print this duration.
 
console.time('foo');
foo();
console.timeEnd('foo');

126
Multiple return values
Write a function foo that returns a string and a boolean value.
 
const foo = () => ({string: 'string', bool: true})

Usage:
let {string: a, bool: b} = foo ()
Alternative implementation:

const foo = () => ['string', true];

127
Source code inclusion
Import the source code for the function foo body from a file "foobody.txt".
 
import { readFile } from 'fs/promises';

const foo = new Function(await readFile('foobody.txt'));

131
Successive conditions
Execute f1 if condition c1 is true, or else f2 if condition c2 is true, or else f3 if condition c3 is true.
Don't evaluate a condition when a previous condition was true.
 
c1 ? f1 : c2 ? f2 : f3

The ternary operator is great for conciseness and statement-freedom.
It's not so great for clarity.
Oh well. \(^w^)/
Alternative implementation:

switch (true) {
  case c1:
    f1();
    break;
  case c2:
    f2();
    break;
  case c3:
    f3();
    break;
}

Using switch/case
Alternative implementation:

if (c1) {
  f1();
} else if (c2) {
  f2();
} else if (c3) {
  f3();
}

Using if/else
 
132
Measure duration of procedure execution
Run the procedure f, and return the duration of the execution of f.
 
function clock(f) {
  var start = new Date().getTime();
  f();
  var end = new Date().getTime();
  return end - start;
}

The result is in milliseconds.
Alternative implementation:

function clock(f) {
  var start = performance.now();
  f();
  var end = performance.now();
  return end - start;
}

The result is in milliseconds.
 
133
Case-insensitive string contains
Set boolean ok to true if string word is contained in string s as a substring, even if the case doesn't match, or to false otherwise.
 
var lowerS = s.toLowerCase();
var lowerWord = word.toLowerCase();
var ok = lowerS.indexOf(lowerWord) !== -1;

134
Create a new list
Declare and initialize a new list items, containing 3 elements a, b, c.
 
const items = [a, b, c];

Alternative implementation:

const items = new Array(a, b, c);

This works fine, but read the doc carefully!
 
135
Remove item from list, by its value
Remove at most 1 item from list items, having the value x.
This will alter the original list or return a new list, depending on which is more idiomatic.
If there are several occurrences of x in items, remove only one of them. If x is absent, keep items unchanged.
 
const idx = items.indexOf(x)
if (idx !== -1) items.splice(idx, 1)

136
Remove all occurrences of a value from a list
Remove all occurrences of the value x from list items.
This will alter the original list or return a new list, depending on which is more idiomatic.
 
const newlist = items.filter(y => x !== y)

137
Check if string contains only digits
Set the boolean b to true if the string s contains only characters in the range '0'..'9', false otherwise.
 
var b = /^[0-9]+$/.test(s);

Notice the ^ and $ for "beginning of string" and "end of string".
 
138
Create temp file
Create a new temporary file on the filesystem.
 
{
  "dependencies": "tempy^1.0.1"
}

import tempy from 'tempy'

const tempFile = tempy.file()

Alternative implementation:

{
  "dependencies": "tempy^1.0.1"
}

import tempy from 'tempy'

const resultOfCallback = tempy.file.task(tempFile => {
 // do something with tempFile
})

tempFile is automatically cleaned up after the callback is executed. resultOfCallback is the return value of the callback.
 
139
Create temp directory
Create a new temporary folder on filesystem, for writing.
 
const tempDir = await Deno.makeTempDir();

Only in Deno. Also see Deno.makeTempDirSync() for synchronous version.
 
140
Delete map entry
Delete from map m the entry having key k.

Explain what happens if k is not an existing key in m.
 
m.delete(k)

m has type Map
 
141
Iterate in sequence over two lists
Iterate in sequence over the elements of the list items1 then items2. For each iteration print the element.
 
for (let item of items1) console.log(item)
for (let item of items2) console.log(item)

Alternative implementation:

items1.concat(items2).forEach(console.log)

uses Array.concat(...) to join items.
Use .map(), .filter(), .reduce(), .forEach() to process.
 
142
Hexadecimal digits of an integer
Assign to string s the hexadecimal representation (base 16) of integer x.

E.g. 999 -> "3e7"
 
const s = x.toString(16)

143
Iterate alternatively over two lists
Iterate alternatively over the elements of the lists items1 and items2. For each iteration, print the element.

Explain what happens if items1 and items2 have different size.
 
const shorter = _items1.length >_items2.length ? _items2 :_items1;
const longer = _items1.length <=_items2.length ? _items2 :_items1;
shorter.map((m, i) => {
  console.log(m);
  console.log(longer[i]);
});

will limit each array to the length of the shortest array
Alternative implementation:

const iterator1 = items1[Symbol.iterator]()
const iterator2 = items2[Symbol.iterator]()

let result1 = iterator1.next()
let result2 = iterator2.next()

while(!(result1.done && result2.done)) {
  if (!result1.done) {
    console.log(result1.value)
    result1 = iterator1.next()
  }
  if (!result2.done) {
    console.log(result2.value)
    result2 = iterator2.next()
  }
}

Approach that purely uses Iterators, similar to the Java Iterator example
 
144
Check if file exists
Set boolean b to true if file at path fp exists on filesystem; false otherwise.

Beware that you should never do this and then in the next instruction assume the result is still valid, this is a race condition on any multitasking OS.
 
const fs = require('fs');

const b = fs.existsSync(fp);

Alternative implementation:

import { access } from 'fs/promises';

let b = true;
try {
 await access(fp);
} catch {
 b = false;
}

Sets b to false if the access function fails due to fp not being visible to the process.
Alternative implementation:

try {
 Deno.statSync(fp)
} catch(_e) {console.error("File does not exist.")}

145
Print log line with datetime
Print message msg, prepended by current date and time.

Explain what behavior is idiomatic: to stdout or stderr, and what the date format is.
 
console.log(Date(), msg);

In Node.js environment, console.log() prints to stdout.
Alternative implementation:

console.error(Date(), msg);

In Node.js environment, console.error() prints to stderr.
 
146
Convert string to floating point number
Extract floating point value f from its string representation s
 
let f = +s

The unary + operator converts its argument to a double precision floating point.
 
147
Remove all non-ASCII characters
Create string t from string s, keeping only ASCII characters
 
const t = [...s].filter(c => c.charCodeAt(0) <= 0x7f).join('')

Alternative implementation:

const t = s.replace(/[^\x00-\x7f]/gu, '')

148
Read list of integers from stdin
Read a list of integer numbers from the standard input, until EOF.
 
process.stdin.on('data', processLine)

function processLine (line) {
  const string = line + ''
  console.log(string)
}

Alternative implementation:

const ints = await new Promise(resolve => {
  let string = ''
  process.stdin
    .on('data', data => string += data.toString())
    .on('close', () => resolve(string.split('\n').map(line => Number.parseInt(line))))
})

149
Rescue the princess
As an exception, this content is not under license CC BY-SA 3.0 like the rest of this website.
 
150
Remove trailing slash
Remove the last character from the string p, if this character is a forward slash /
 
const slashscrape = p => (
  p.slice (-1) === '/' ?
    p.slice (0, -1) :
    p
)

151
Remove string trailing path separator
Remove last character from string p, if this character is the file path separator of current platform.

Note that this also transforms unix root path "/" into the empty string!
 
import * as path from 'path'

p = p.endsWith(path.sep) ? p.slice(0, -path.sep.length) : p

152
Turn a character into a string
Create string s containing only the character c.
 
let s = c

Similarly to python:
A character is a single character string, not a distinct datatype.
 
153
Concatenate string with integer
Create the string t as the concatenation of the string s and the integer i.
 
let t = s + i;

Alternative implementation:

let t = `${s}${i}`

Using template literals
 
154
Halfway between two hex color codes
Find color c, the average between colors c1, c2.

c, c1, c2 are strings of hex color codes: 7 chars, beginning with a number sign # .
Assume linear computations, ignore gamma corrections.
 
var c = "#";
for(var i = 0; i<3; i++) {
  var sub1 = c1.substring(1+2*i, 3+2*i);
  var sub2 = c2.substring(1+2*i, 3+2*i);
  var v1 = parseInt(sub1, 16);
  var v2 = parseInt(sub2, 16);
  var v = Math.floor((v1 + v2) / 2);
  var sub = v.toString(16).toUpperCase();
  var padsub = ('0'+sub).slice(-2);
  c += padsub;
}

Alternative implementation:

c = "#" + (() => {
  const [p1, p2] = [c1, c2].map((color) => parseInt(color.slice(1), 16)),
    a = [];

  for (let i = 0; i <= 2; i += 1) {
    a.push(Math.floor(((p1 >> (i *8) & 0xff) + (p2 >> (i* 8) & 0xff)) / 2));
  }

  return a.reverse().map((num) => num.toString(16).padStart(2, "0")).join("");
})();

155
Delete file
Delete from filesystem the file having path filepath.
 
const fs = require('fs');

try {
  fs.unlinkSync(filepath);
} catch (err) {
  console.error(err);
}

This is synchronous.
Alternative implementation:

import {unlink} from 'fs/promises'

await unlink(filepath)

This is asynchronous.
Alternative implementation:

Deno.remove(filepath, { recursive: true }).catch((err) => console.error(err));

For Deno runtime. Deno.removeSync is a similar function that is synchronous.
recursive can be set to false, but deleting a non-empty directory will fail.
 
156
Format integer with zero-padding
Assign to the string s the value of the integer i in 3 decimal digits. Pad with zeros if i < 100. Keep all digits if i ≥ 1000.
 
let s = i.toString();
if(i<100)
  s = ('00'+i).slice(-3);

157
Declare constant string
Initialize a constant planet with string value "Earth".
 
const planet = 'Earth'

It's considered good practice to use const unless your variable is mutable
 
158
Random sublist
Create a new list y from randomly picking exactly k elements from list x.

It is assumed that x has at least k elements.
Each element must have same probability to be picked.
Each element from x must be picked at most once.
Explain if the original ordering is preserved or not.
 
const idx = x.map((item, i) => i);
while (y.length < k) {
  const i = parseInt(Math.random() * idx.length, 10);
  y.push(x[[idx[i]]]);
  idx.splice(i, 1);
}

Note: lodash has a sample function.

Without native sampling in JS, create an array of unchosen indices of x and randomly pick them until y's length equals k.
 
160
Detect if 32-bit or 64-bit architecture
Execute f32() if platform is 32-bit, or f64() if platform is 64-bit.
This can be either a compile-time condition (depending on target) or a runtime detection.
 
os

const is64Bit = os.arch() === 'x64' || process.env.hasOwnProperty('PROCESSOR_ARCHITEW6432');
is64Bit ?_f64() : _f32();

161
Multiply all the elements of a list
Multiply all the elements of the list elements by a constant c
 
elements = elements.map(x => x * c)

Haskell's idioms are the best!
uh languages without basic list processing operations are good too
please don't hit me
 
162
Execute procedures depending on options
execute bat if b is a program option and fox if f is a program option.
 
const args = process.argv.slice(2)
if (args.includes('b')) bat()
else if (args.includes('f')) fox()

163
Print list elements by group of 2
Print all the list elements, two by two, assuming list length is even.
 
for (let index = 0; index < list.length; index = index + 2) {
  console.log(list[index], list[index + 1])
}

165
Last element of list
Assign to the variable x the last element of the list items.
 
const x = items[items.length - 1];

Alternative implementation:

const x = items.at(-1);

166
Concatenate two lists
Create the list ab containing all the elements of the list a, followed by all the elements of the list b.
 
var ab = a.concat(b);

This returns a new array.
 
167
Trim prefix
Create the string t consisting of the string s with its prefix p removed (if s starts with p).
 
let t = s.startsWith(p) ? s.substring(p.length) : s;

substring returns a string that starts from given index.
 
168
Trim suffix
Create string t consisting of string s with its suffix w removed (if s ends with w).
 
const t = s.endsWith(w) ? s.slice(0, -w.length) : s

169
String length
Assign to the integer n the number of characters of the string s.
Make sure that multibyte characters are properly handled.
n can be different from the number of bytes of s.
 
const n = s.length;

Alternative implementation:

const n = [...s].length;

Sets n to the count of characters in s, not the number of bytes.
 
170
Get map size
Set n to the number of elements stored in mymap.

This is not always equal to the map capacity.
 
const n = mymap.size

mymap has type Map
 
171
Add an element at the end of a list
Append the element x to the list s.
 
s.push(x);

s is an array and x will be inserted at the end.
Alternative implementation:

s = [...s, x];

172
Insert an entry in a map
Insert value v for key k in map m.
 
m.set(k, v);

m has type Map.
Alternative implementation:

m[k] = v;

m is an Object.
In this case m is used as a map of key/value pairs.
 
173
Format a number with grouped thousands
Number will be formatted with a comma separator between every group of thousands.
 
new Intl.NumberFormat().format(1000);

174
Make HTTP POST request
Make a HTTP request with method POST to the URL u
 
fetch(u, {
        method: "POST",
 body: JSON.stringify(data)
})

175
Bytes to hex string
From array a of n bytes, build the equivalent hex string s of 2n digits.
Each byte (256 possible values) is encoded as two hexadecimal characters (16 possible values per digit).
 
const s = Buffer.from(a).toString('hex')

Buffer is only available in Node.js.
Alternative implementation:

const s = a.map(n => n.toString(16).padStart(2, '0')).join('')

toString(16) returns just one character when n < 16.
 
176
Hex string to byte array
From hex string s of 2n digits, build the equivalent array a of n bytes.
Each pair of hexadecimal characters (16 possible values per digit) is decoded into one byte (256 possible values).
 
s
  .split('')
  .map((el, ix, arr) => ix % 2 ? null : el + arr[ix + 1])
  .filter(el => el !== null)
  .map(x => parseInt(x, 16))

- split the string into an array
- transform into alternating pairs of two chars and null (you could do this more cleanly with a for loop)
- filter out the nulls
- parse the two-char strings (you could do this inside the first map but this way reads better)
 
178
Check if point is inside rectangle
Set boolean b to true if if the point with coordinates (x,y) is inside the rectangle with coordinates (x1,y1,x2,y2) , or to false otherwise.
Describe if the edges are considered to be inside the rectangle.
 
const pointInRect = ({x1, y1, x2, y2}, {x, y}) => (
  (x > x1 && x < x2) && (y > y1 && y < y2)
)

179
Get center of a rectangle
Return the center c of the rectangle with coördinates(x1,y1,x2,y2)
 
const center = ({x1, y1, x2, y2}) => ({x: (x1 + x2) / 2, y: (y1 + y2) / 2})

Alternative implementation:

class Point {
  constructor (x, y) {
    this.x = x
    this.y = y
  }
}
const center = ({x1, y1, x2, y2}) => new Point ((x1 + x2) / 2, (y1 + y2) / 2)

180
List files in directory
Create the list x containing the contents of the directory d.

x may contain files and subfolders.
No recursive subfolder listing.
 
const fs = require('fs');

const x = fs.readdirSync(d)

182
Quine program
Output the source of the program.
 
c=console.log
q=decodeURIComponent('%22')
l=[
"c=console.log",
"q=decodeURIComponent('%22')",
"l=[",
"]",
"for(i=0;i<3;i++)c(l[i])",
"for(i=0;i<7;i++)c(q+l[i]+q+',')",
"for(i=3;i<7;i++)c(l[i])",
]
for(i=0;i<3;i++)c(l[i])
for(i=0;i<7;i++)c(q+l[i]+q+',')
for(i=3;i<7;i++)c(l[i])

183
Make HTTP PUT request
Make a HTTP request with method PUT to the URL u
 
fetch(u, {
        method: "PUT",
 body: JSON.stringify(data)
})

184
Tomorrow
Assign to variable t a string representing the day, month and year of the day after the current date.
 
var nextDate = new Date(new Date().getTime() + 24 *60* 60 * 1000);
var day = nextDate.getDate()
var month = nextDate.getMonth() + 1
var year = nextDate.getFullYear()
var t = `${day}/${month}/${year}`;

Note that Date.prototype.getMonth() is zero-based.
t is not zero padded, so it may have a single-digit day or month.
Alternative implementation:

var tomorrow = new Date();
tomorrow.setDate(tomorrow.getDate() + 1);

Alternative implementation:

var now = new Date()
var year = now.getFullYear()
var month = now.getMonth()
var day = now.getDate()

var tomorrow = new Date(0)
tomorrow.setFullYear(year, month, day + 1)
tomorrow.setHours(0, 0, 0, 0)

var shortDateFormat = Intl.DateTimeFormat(undefined, { dateStyle: "short" })
var t = shortDateFormat.format(tomorrow)

Adding 24 hours to the current time does not always get tomorrow because there could be a daylight saving time transition.

The user may not use "dd/mm/yyyy" as their preferred date format. shortDateFormat is a formatter that honors the user's preferences.
 
185
Execute function in 30 seconds
Schedule the execution of f(42) in 30 seconds.
 
let id = setTimeout(f, 30000, 42);

The second arg is the delay in milliseconds.

The subsequent args will be passed to the function f.

id identifies the timer created by setTimeout, and can be used to cancel the timeout.
 
186
Exit program cleanly
Exit a program cleanly indicating no error to OS
 
process.exit()

This is only for node.js
 
189
Filter and transform list
Produce a new list y containing the result of the function T applied to all elements e of the list x that match the predicate P.
 
y = x.filter(e => P(e)).map(e => T(e))

191
Check if any value in a list is larger than a limit
Given a one-dimensional array a, check if any value is larger than x, and execute the procedure f if that is the case
 
if(a.some(item => item > x)){
 f()
}

193
Transpose a two-dimensional matrix
Declare two two-dimensional arrays a and b of dimension n*m and m*n, respectively. Assign to b the transpose of a (i.e. the value with index interchange).
 
const a = [[1, 2, 3], [4, 5, 6]]
const m = a[0].length
const b = Array.from({ length: m }, (_, n) => a.map(row => row[n]))

Requires ES2015
 
195
Pass a two-dimensional array
Pass an array a of real numbers to the procedure (resp. function) foo. Output the size of the array, and the sum of all its elements when each element is multiplied with the array indices i and j (assuming they start from one).
 
/**

- @param {Array<Array>} arry
*
- @return {Array<Array>}
 */
function foo(arry) {
  let len = 0;
  let sum = 0;

  arry.forEach(function(base, i) {
    len += base.length;

    base.forEach(function(a, j) {
      sum += a * (i + 1) * (j + 1);
    });
  });

  console.log('Array size:', arry.length, ',', len);

  return sum;
}

foo(arry2d);

197
Get a list of lines from a file
Retrieve the contents of file at path into a list of strings lines, in which each element is a line of the file.
 
import fs from "fs";

fs.readFileSync(path).split("\n")

198
Abort program execution with error condition
Abort program execution with error condition x (where x is an integer value)
 
process.exit(x);

200
Return hypotenuse
Returns the hypotenuse h of the triangle where the sides adjacent to the square angle have lengths x and y.
 
var h = Math.sqrt(x*x + y*y);

Works even in older browsers.
Alternative implementation:

const h = Math.hypot(x, y);

201
Euclidean norm
Calculate n, the Euclidean norm of data (an array or list of floating point values).
 
const n = Math.hypot(...data)

Spread syntax requires ES6 or newer
Alternative implementation:

var n = Math.hypot.apply(null, data)

If support for older browsers is necessary.
 
202
Sum of squares
Calculate the sum of squares s of data, an array of floating point values.
 
s = data.reduce((a, c) => a + c ** 2, 0)

Array.reduce uses a function to reduce the array into a single sum of all the elements' squares.

The initial accumulator's value is 0.
 
204
Return fraction and exponent of a real number
Given a real number a, print the fractional part and the exponent of the internal representation of that number. For 3.14, this should print (approximately)

0.785 2
 
function frexp(a) {
    exponent = ( Math.floor(Math.log(a, 2)) + 1 )
    mantissa = ( a * Math.pow(2, -a) )

    return [ mantissa, exponent ]
}

205
Get an environment variable
Read an environment variable with the name "FOO" and assign it to the string variable foo. If it does not exist or if the system does not support environment variables, assign a value of "none".
 
const foo = process.env["FOO"] || "none";

Alternative implementation:

const foo = process.env.FOO ?? 'none'

The nullish colaescing operator (??) is available in ES2020 onwards. It ensures that if the FOO environment variable is the empty string, foo isn't set to 'none'.
 
206
Switch statement with strings
Execute different procedures foo, bar, baz and barfl if the string str contains the name of the respective procedure. Do it in a way natural to the language.
 
switch (str) {
  case "foo":
    foo();
    break;
  case "bar":
    bar();
    break;
  case "baz":
    baz();
    break;
  case "barfl":
    barfl();
    break;
}

208
Formula with arrays
Given the arrays a,b,c,d of equal length and the scalar e, calculate a = e*(a+b*c+cos(d)).
Store the results in a.
 
a.forEach((aa, i) => a[i] = e *(aa + b[i]* c[i] + Math.cos(d[i])))

210
Compiler version and options
Assign, at runtime, the compiler version and the options the program was compilerd with to variables version and options, respectively, and print them. For interpreted languages, substitute the version of the interpreter.

Example output:

GCC version 10.0.0 20190914 (experimental)
-mtune=generic -march=x86-64
 
const { version } = process;
console.log(version);

This doesn't work in a browser.
 
211
Create folder
Create the folder at path on the filesystem
 
import { mkdir } from 'fs/promises';

await mkdir(path);

214
Pad string on the right
Append extra character c at the end of string s to make sure its length is at least m.
The length is the number of characters, not the number of bytes.
 
s = s.padEnd(m, c);

215
Pad string on the left
Prepend extra character c at the beginning of string s to make sure its length is at least m.
The length is the number of characters, not the number of bytes.
 
s = s.padStart(m, c);

Introduced in ECMAScript 2017.
 
218
List intersection
Create the list c containing all unique elements that are contained in both lists a and b.
c should not contain any duplicates, even if a and b do.
The order of c doesn't matter.
 
const c = [...new Set(a)].filter(e => b.includes(e));

219
Replace multiple spaces with single space
Create the string t from the value of string s with each sequence of spaces replaced by a single space.

Explain if only the space characters will be replaced, or the other whitespaces as well: tabs, newlines.
 
let t = s.replace(/\s+/g, ' ');

This replaces any sequence of whitespaces with a single space.
 
220
Create a tuple value
Create t consisting of 3 values having different types.

Explain if the elements of t are strongly typed or not.
 
let t = [2.5, "hello", -1];

An Array may hold any list of values.
Elements are not strongly typed.
 
221
Remove all non-digits characters
Create string t from string s, keeping only digit characters 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.
 
t = s.replace(/[^\d]/gm,"");

222
Find the first index of an element in list
Set i to the first index in list items at which the element x can be found, or -1 if items does not contain x.
 
let i = items.indexOf(x);

223
for else loop
Loop through list items checking a condition. Do something else if no matches are found.

A typical use case is looping through a series of containers looking for one that matches a condition. If found, an item is inserted; otherwise, a new container is created.

These are mostly used as an inner nested loop, and in a location where refactoring inner logic into a separate function reduces clarity.
 
const found = items.some(condition);

if (!found) doSomethingElse();

224
Add element to the beginning of the list
Insert the element x at the beginning of the list items.
 
items.unshift(x);

Alternative implementation:

items = [x, ...items];

225
Declare and use an optional argument
Declare an optional integer argument x to procedure f, printing out "Present" and its value if it is present, "Not present" otherwise
 
function f(x) {
 console.log(x ? `Present: ${x}` : 'Not present');
}

226
Delete last element from list
Remove the last element from the list items.
 
items.pop();

This truncates items in-place.

Ignore the returned value (which is the just removed value).

If items is already an empty list, it will remain empty.
 
227
Copy a list
Create the new list y containing the same elements as the list x.

Subsequent modifications of y must not affect x (except for the contents referenced by the elements themselves if they contain pointers).
 
let y = x.slice();

228
Copy a file
Copy the file at path src to dst.
 
const { copyFileSync } = require('fs');

copyFileSync(src, dst);

232
Read a command line boolean flag
Print "verbose is true" if the flag -v was passed to the program command line, "verbose is false" otherwise.
 
const verbose = process.argv.includes('-v');
console.log('verbose is', verbose);

234
Encode bytes to base64
Assign to the string s the standard base64 encoding of the byte array data, as specified by RFC 4648.
 
let s = btoa(data);

btoa should be read as "binary to ASCII"
 
235
Decode base64
Assign to byte array data the bytes represented by the base64 string s, as specified by RFC 4648.
 
var data = atob(s)

atob should be read as "ASCII to binary"
 
237
Xor integers
Assign to c the result of (a xor b)
 
const c = a ^ b;

238
Xor byte arrays
Write in a new byte array c the xor result of byte arrays a and b.

a and b have the same size.
 
const c = Uint8Array.from(a, (v, i) => v ^ b[i])

239
Find first regular expression match
Assign to string x the first word of string s consisting of exactly 3 digits, or the empty string if no such match exists.

A word containing more digits, or 3 digits as a substring fragment, must not match.
 
const matches = s.match(/\b\d{3}\b/);
const x = matches ? matches[0] : '';

242
Iterate over a set
Call a function f on each element e of a set x.
 
for (const e of x) {
 f(e);
}

Alternative implementation:

let v = x.values();
let result = v.next();
while (!result.done) {
  f(result.value);
  result = v.next();
}

For old JS standards that don't support for...of.
Alternative implementation:

x.forEach(f);

x has type Set
 
243
Print list
Print the contents of the list or array a on the standard output.
 
console.log(a);

Alternative implementation:

console.table(a);

Displays a as a table where the first column contains the index, and the subsequent column(s) contain the values.
 
244
Print a map
Print the contents of the map m to the standard output: keys and values.
 
console.log(m);

Alternative implementation:

console.table(m);

Displays m as a table where the first column contains the key, and the subsequent column(s) contain the values.
 
245
Print value of custom type
Print the value of object x having custom type T, for log or debug.
 
console.log(x);

246
Count distinct elements
Set c to the number of distinct elements in the list items.
 
const c = new Set(items).size;

247
Filter list in-place
Remove all the elements from list x that don't satisfy the predicate p, without allocating a new list.
Keep all the elements that do satisfy p.

For languages that don't have mutable lists, refer to idiom #57 instead.
 
for (const [key, value] of x.entries()) {
 if (!p(value)) x.splice(key, 1);
}

Alternative implementation:

x = x.filter((e) => p(e));

249
Declare and assign multiple variables
Define variables a, b and c in a concise way.
Explain if they need to have the same type.
 
const [a, b, c] = [42, "hello", 5.0];

a, b, and c may have different types.
 
250
Pick a random value from a map
Choose a value x from map m.
m must not be empty. Ignore the keys.
 
// Objects
const values = Object.values(m);

// Maps
const values = [...m.values()];

const x = values[~~(Math.random() * values.length)]

This converts the values of m into an array first, because you cannot get a random element from an object or a map.
 
251
Parse binary digits
Extract integer value i from its binary string representation s (in radix 2)
E.g. "1101" -> 13
 
const i = parseInt(s, 2)

252
Conditional assignment
Assign to the variable x the string value "a" if calling the function condition returns true, or the value "b" otherwise.
 
const x = condition() ? 'a' : 'b';

253
Print stack trace
Print the stack frames of the current execution thread of the program.
 
console.trace()

254
Replace value in list
Replace all exact occurrences of "foo" with "bar" in the string list x
 
x = x.map(e => e === 'foo' ? 'bar' : e);

255
Print a set
Print the values of the set x to the standard output.
The order of the elements is irrelevant and is not required to remain the same next time.
 
console.log(x);

256
Count backwards
Print the numbers 5, 4, ..., 0 (included), one line per number.
 
for (let i = 5; i >= 0; i--) {
  console.log(i)
}

257
Traverse list backwards
Print each index i and value x from the list items, from the last down to the first.
 
[...items].reverse().forEach((item, index) =>
console.log(Math.abs(index -= items.length), item));

reverse a copy of the array items, then print each index and value.
Get the correct index by calculating the absolute value of the index - the length of the list
 
258
Convert list of strings to list of integers
Convert the string values from list a into a list of integers b.
 
let b = a.map(Number)

Array.prototype.map takes a function, which means you can pass it the name of Number.
 
259
Split on several separators
Build the list parts consisting of substrings of the input string s, separated by any of the characters ',' (comma), '-' (dash), '_' (underscore).
 
var parts = s.split(/[-_,]/)

260
Create an empty list of strings
Declare a new list items of string elements, containing zero elements
 
let items = [];

261
Format time hours-minutes-seconds
Assign to the string x the value of fields (hours, minutes, seconds) of the date d, in format HH:MM:SS.
 
const d = new Date();

let hr = d.getHours();
let min = d.getMinutes();
let sec = d.getSeconds();

if ( hr.toString().length === 1 ) {
  hr = '0' + hr;
}

if ( min.toString().length === 1 ) {
  min = '0' + min;
}

if ( sec.toString().length === 1 ) {
  sec = '0' + sec;
}

const x = '' + hr + ':' + min + ':' + sec;

Call `.toString().length` to check if zero padding needed.
 
265
Even parity bit
Calculate the parity p of the integer variable i : 0 if it contains an even number of bits set, 1 if it contains an odd number of bits set.
 
let i = 42
i.toString(2)
  .split('')
  .reduce((parity, bit) => parity ^ bit, 0)

266
Repeated string
Assign to the string s the value of the string v repeated n times, and write it out.

E.g. v="abc", n=5 ⇒ s="abcabcabcabcabc"
 
const s = v.repeat(n)

267
Pass string to argument that can be of any type
Declare an argument x to a procedure foo that can be of any type. If the type of the argument is a string, print it, otherwise print "Nothing."

Test by passing "Hello, world!" and 42 to the procedure.
 
function foo(x) {
  console.log(typeof x == 'string' ? x : 'Nothing.')
}

foo('Hello, world!')
foo(42)

272
Play FizzBuzz
Fizz buzz is a children's counting game, and a trivial programming task used to affirm that a programmer knows the basics of a language: loops, conditions and I/O.

The typical fizz buzz game is to count from 1 to 100, saying each number in turn. When the number is divisible by 3, instead say "Fizz". When the number is divisible by 5, instead say "Buzz". When the number is divisible by both 3 and 5, say "FizzBuzz"
 
for (let i = 1; i <= 100; i++) {
    let out = "";
    if (!(i % 3)) out += "Fizz";
    if (!(i % 5)) out += "Buzz";
    if (!out) out = i;
    console.log(out);
}

!(i % 3) and !(i % 5) are similar to (i % 3) == 0 and (i % 5) == 0, as !0 evaluates to true.
 
274
Remove all white space characters
Create the string t from the string s, removing all the spaces, newlines, tabulations, etc.
 
let t = s.replace(/\s/g,'');

This uses a regex.
\s means "a whitespace character"
g means "replace all occurrences"
 
276
Insert an element in a set
Insert an element e into the set x.
 
x.add(e);

x has type Set
 
283
Split with a custom string separator
Build the list parts consisting of substrings of input string s, separated by the string sep.
 
const parts = s.split(sep);

284
Create a zeroed list of integers
Create a new list a (or array, or slice) of size n, where all elements are integers initialized with the value 0.
 
const a = new Array(n).fill(0);

286
Iterate over characters of a string
Print a line "Char i is c" for each character c of the string s, where i is the character index of c in s (not the byte index).

Make sure that multi-byte characters are properly handled, and count for a single character.
 
for (const [i, c] of [...s].entries()) {
 console.log(`Char ${i} is ${c}`);
}

288
Check if set contains a value
Set the boolean b to true if the set x contains the element e, false otherwise.
 
let b = x.has(e);

x has type Set
 
289
Concatenate two strings
Create the string s by concatenating the strings a and b.
 
const s = a + b;

293
Create a stack
Create a new stack s, push an element x, then pop the element into the variable y.
 
const s = [1, 2, 3];
s.push(x);
const y = s.pop();

This is an array used as a stack.
 
299
Comment out a single line
Write a line of comments.

This line will not be compiled or executed.
 
// This is a comment

302
String interpolation
Given the integer x = 8, assign to the string s the value "Our sun has 8 planets", where the number 8 was evaluated from x.
 
let s = `Our sun has ${x} planets`;

This is a "template literal". It's delimited with backticks.
 
304
Encode string into UTF-8 bytes
Create the array of bytes data by encoding the string s in UTF-8.
 
const data = new TextEncoder().encode(s);

308
Integer to string in base b
Create the string representation s of the integer value n in base b.

18 in base 3 -> "200"
26 in base 5 -> "101"
121 in base 12 -> "a1"

let s = n.toString(b);

311
Deep copy an object
Create the new object y by cloning the all the contents of x, recursively.
 
let y = structuredClone(x);

316
Count occurrences in a list
Determine the number c of elements in the list x that satisfy the predicate p.
 
let c = x.filter(p).length

Array.prototype.filter takes in a predicate function, and runs it for every element in the array, if the predicate returns true, the element is kept, but if not, the element is removed.

So, c is the length of the array returned by Array.prototype.filter.
 
317
Random string
Create a string s of n characters having uniform random values out of the 62 alphanumeric values A-Z, a-z, 0-9
 
const s = ((n) => {
    const alphanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    let s = "";
    for (let i = 0; i < n; i += 1) {
        s += alphanum[~~(Math.random() * alphanum.length)];
    }
    return s;
})(n);

~~ is a faster way to call Math.floor().

Note that Math.random is not cryptographically secure.
 
327
Convert string to lower case
Assign to t the value of the string s, with all letters mapped to their lower case.
 
let t = s.toLowerCase();

328
Convert string to upper case
Assign to t the value of the string s, with all letters mapped to their upper case.
 
let t = s.toUpperCase();

329
Read value in a map
Assign to v the value stored in the map m for the key k.

Explain what happens if there is no entry for k in m.
 
v = m.get(k);

If k does not exist in m, v will be `undefined`.
 
331
Clear map
Remove all entries from the map m.

Explain if other references to the same map now see an empty map as well.
 
m.clear()

334
Combine 2 maps
Create the new map c containing all of the (key, value) entries of the two maps a and b.

Explain what happens for keys existing in both a and b.
 
let c = {...a, ...b}
