Cc-cpp/C++
==========



structure of a C++ program:
  include libraries: #include <iostream>
  main() function: int main()
  beginning of function: {
  what the program does
  end of function: }

std::cout is the "character output stream". pronounced "see-out".
<!--ID: 1639529002896-->

<< operator
\n is a special character that indicates a new line.
; is a punctuation that indicates a end of a statement.
  similar to a period in a sentence.

c++ is general-purpose coding language.
c++ runs line by line, from top to bottom.
std::cout is how you output to the terminal.

c++ is a case-sensitive language.
  case sensitivity: means that your keywords and variable declarations must
  match the case.

// single-line comment
test #include <iostream>
  pre-processor directive.
int main() {
  // statements
}
c++ must have a function called main().
a function is basically a sequence of instructions for the computer to execute.
main() function houses all of our instructions for our program.
the return statement is used to end a function. return 0;
  if the program reaches this statement, returning a value of 0 is an indication
  to the operating system that the code executed successfully.
  this line of code is optional.

c++ is a compiled language.
compiler translate code
c++ development phases:
  Code - writing the program.
  Save - saving the program.
  Compile - compiling via the terminal.
  Execute - executing via the terminal.
  Repeat - debug the errors if needed

a computer can only understand machine code.
a compiler translate the programs (codes) into machine code.
to compile a file: g++ <file-name> in the terminal
naming executables: g++ <file-name> -o <new>
the compiler then translates the c++ program and create a machine code file
called a.out
Execute: to execute the new machine code file: ./<machine_code_file>: ./a.out

Comments:
/ is called forward slashed
\ is called back slashed
// single-line comments
std::cout << "hi\n"; // single-line comment after code
/*
multi-line comments
*/

what you read and write is called source code.
what the computer executes is called executable, object code, or machine code (a
machine language).
typically C++ source code file are given the suffix:
  .cpp (ex: hello.cpp) or 
  .h (ex: std_lib_facllties.h).
source code > preprocessor >> compiler >> linker > executable

Compile:
a compiler translates the C++ program into machine language code 
  which it stores on the disk as a file with the extension .o(e.g. hello.o)
a linker then links the object code with standard library routines that the
program may use and creates an executable image which is also saved on disk,
usually as a file with the file name without any extension (e.g. hello).

Execute:
the executable is loaded from the disk to memory and the computer's CPU
(Central Processing Unit) executes the program one instruction at a time.

a variable is simple a name that represent a particular piece of your computer's
memory that has been set aside for you to store, retrieve, and use data.
basic data types:
- int: integer numbers
- double: floating-point numbers
- char: individual characters
- string: a sequence of characters
- bool: true/false values; truth values
every variable has has a type;
  which represents the kind of information you can store inside of it.
  it tell your compiler how much memory to set aside for the variable, and it
  defines what you can do with the variable.
  
every variable in C++ must be declared before it can be used
declare: create it
To declare a variable:
- A type for the variable.
- A name for the variable.
<type> <variable>;
In C++, variable names consist only of upper/lower case letter, digits, and/or
underscores.
C++ is known as a strongly typed language.
  If you try to give an integer value a decimal number, you get unexpected
  results, warnings, or errors.
initialize a variable
<variable> = <value>;
The = indicates assignment
  a single equal sign means "assign"

Arithmetic Operators:
- + addition
- - subtraction
- * multiplication
- / division
- % modulo (divides and gives the remainder)

Chaining:
use quotes when we want a literal string.
<<: chaining operator

user input:
cout for output
cin for input
- refers to the standard input stream
- pronounced "see-in"
- for character input
the second operand of the >> operator ("get from") specifies where that input
goes.

a variable represents a particular piece of your computer's memory that has been
set aside for to use to store, retrieve, and manipulate data.
single equal sign = indicates assignment, not equality in the mathematical sense.
cin: is how to receive input from the user.
