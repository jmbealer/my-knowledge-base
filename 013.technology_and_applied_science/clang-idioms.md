---
title: C Idioms
author: Justin Bealer
date_created: 2024-02-25, 10-42-43
date_modified: 2024-09-17, 09-30-01
reference: 
description: 
aliases: 
tags: 
---
# C Idioms

TARGET DECK: test-c-idioms
FILE TAGS: C idioms


## Sorted

// 1. **Print** a literal string **"hello"** to standard output
==#include== ==<stdio.h>==
==int main() {==
  ==printf== ==("hello\n");==
  ==return 0;==
}
<!--ID: 1708988841782-->

// 2. **Print** hello 10 times
// Loop to execute some code a constant number of times
==#include <stdio.h>==
==int main() {==
  ==for== ==(int i = 0;== ==i < 10; i++) {==
    ==printf==("hello\n");
  }
}
<!--ID: 1708989768631-->

// 3. Create a **procedure**
// Like a function which doesn't return any value, thus has only side effects
int main() {
  ==void finish(void) {==
    printf("My job here is done.\n");
  }
}
<!--ID: 1708990039156-->

// 4. Create a **function** which returns the **square** of an integer
int main() {
  ==int square(int x){==
    ==return x*x;==
  }
}
<!--ID: 1708990767081-->

// 5. Create a **2D Point data structure**
// Declare a container type for two floating-point numbers x and y
int main() {
  ==typedef struct {==
    ==double x;==
    ==double y;==
  ==} Point;==
}
<!--ID: 1708991277195-->

## Unsorted
6 Iterate over list values
Do something with each item x of the list (or array) items, regardless indexes.

for (unsigned int i = 0 ; i < items_length ; ++i){
        Item* x = &(items[i]);
	DoSomethingWith(x);
}

items_length type is: unsigned int
DoSomethingWith prototype is: void DoSomethingWith(Item*);

Alternative implementation:

for (size_t i = 0; i < sizeof(items) / sizeof(items[0]); i++) {
	DoSomethingWith(&items[i]);
}

sizeof the array divided by the size of the first element computes the number of elements, often defined as macro ARRAY_SIZE

7 Iterate over list indexes and values
Print each index i with its value x from an array-like collection items

for (size_t i = 0; i < n; i++) {
  printf("Item %d = %s\n", i, toString(items[i]));
}

The loop variable i is the index. Inside the loop, access the value with items[i]

8 Create a map (associative array)
Create a new map object x, and provide some (key, value) pairs as initial content.

#include <search.h>

ENTRY a = {"foo", "twenty"};
ENTRY b = {"bar", "three"};
if (hcreate (23)) {
    hsearch(a, ENTER);
    hsearch(b, ENTER);
}

This POSIX functions maintain a single global hashmap. The GNU C library provides hcreate_r

    Doc

9 Create a Binary Tree data structure
The structure must be recursive because left child and right child are binary trees too. A node has access to children nodes, but not to its parent.

struct treenode{
  int value;
  struct treenode* left;
  struct treenode* right;
}

10 Shuffle a list
Generate a random permutation of the elements of list x

#include <stdlib.h>
#include <time.h>

srand(time(NULL));
for (int i = 0; i < N-1; ++i)
{
    int j = rand() % (N-i) + i;
    int temp = x[i];
    x[i] = x[j];
    x[j] = temp;
}

Shuffles an array of n ints in-place using Fisher-Yates algorithm.

11 Pick a random element from a list
The list x must be non-empty.

#include <stdlib.h>

x[rand() % x_length];

rand needs to be initialized by calling void srand(unsigned int);

12 Check if list contains a value
Check if the list contains the value x.
list is an iterable finite container.

#include <stdbool.h>

bool contains(int x, int* list, size_t list_len) {
    for (int i=0 ; i<list_len ; i++)
        if (list[i] == x)
            return true;
    return false;
}

14 Pick uniformly a random floating point number in [a..b)
Pick a random number greater than or equals to a, strictly inferior to b. Precondition : a < b.

#include <stdlib.h>

double pick(double a, double b)
{
	return a + (double)rand() / ((double)RAND_MAX * (b - a));
}

this is not uniformly distributed!!

15 Pick uniformly a random integer in [a..b]
Pick a random integer greater than or equals to a, inferior or equals to b. Precondition : a < b.

#include <stdlib.h>

int pick(int a, int b)
{
	int upper_bound = b - a + 1;
	int max = RAND_MAX - RAND_MAX % upper_bound;
	int r;

	do {
		r = rand();
	} while (r >= max);
	r = r % upper_bound;
	return a + r;
}

    Doc

17 Create a Tree data structure
The structure must be recursive. A node may have zero or more children. A node has access to its children nodes, but not to its parent.

typedef struct node_s
{
    int value;
    struct node_s *nextSibling;
    struct node_s *firstChild;
} node_t;

19 Reverse a list
Reverse the order of the elements of the list x.
This may reverse "in-place" and destroy the original ordering.

int *p1 = x;
int *p2 = x + N-1;

while (p1 < p2)
{
    int temp = *p1;
    *(p1++) = *p2;
    *(p2--) = temp;
}

Reverses an array of N ints, in-place.

20 Return two values
Implement a function search which looks for item x in a 2D matrix m.
Return indices i, j of the matching cell.
Think of the most idiomatic way in the language to return the two values at the same time.

#include <string.h>
#include <stdlib.h>

void search(void ***m,void *x,size_t memb_size,int len_x,int len_y,int *i,int *j)
{
	typedef void *m_type[len_x][len_y];
	m_type *m_ref=(m_type*)m;

	for(*i=0;*i<len_x;*i+=1)
	{
		for(*j=0;*j<len_y;*j+=1)
		{
			if(!memcmp((*m_ref)[*i][*j],x,memb_size))
			{
				return;
			}
		}
	}
	*i=*j=-1;
}

m is a matrix containing type (void *) pointing to the data (can be anything)

x is the pointer to the data to look for

memb_size is the size of one element in bytes (to be able to compare anything)

len_x and len_y are the dimensions

i and j are passed by reference and contain the values, or -1 if x was not found, after the function returned.

The typedef is to define the dimensions of the matrix m, this allows for subscript notation

    Demo

21 Swap values
Swap the values of the variables a and b

a^=b;
b^=a;
a^=b;

Only works for integer values (or casted pointers)

22 Convert string to integer
Extract the integer value i from its string representation s (in radix 10)

#include <stdlib.h>

int i = atoi(s);

    Doc

Alternative implementation:

#include <stdlib.h>

i = (int)strtol(s, (char **)NULL, 10);

The atoi() function has been deprecated by strtol()

    Doc

23 Convert real number to string with 2 decimal places
Given a real number x, create its string representation s with 2 decimal digits following the dot.

#include <stdio.h>

sprintf(s, "%.2f", x);

24 Assign to string the japanese word ネコ
Declare a new string s and initialize it with the literal value "ネコ" (which means "cat" in japanese)

const char * s = "ネコ";

C has no notion of character sets, output depends on locale settings and terminal capabilities.

26 Create a 2-dimensional array
Declare and initialize a matrix x having m rows and n columns, containing real numbers.

#include <stdlib.h>

double **x=malloc(m*sizeof(double *));
int i;
for(i=0;i<m;i++)
	x[i]=malloc(n*sizeof(double));

This uses dynamic allocation.

Alternative implementation:

const int m = 2;
const int n = 3;
double x[m][n];

This works when the values of m and n are known at compile time.

27 Create a 3-dimensional array
Declare and initialize a 3D array x, having dimensions boundaries m, n, p, and containing real numbers.

#include <stdlib.h>

double ***x=malloc(m*sizeof(double **));
int i,j;
for(i=0;i<m;i++)
{
	x[i]=malloc(n*sizeof(double *));
	for(j=0;j<n;j++)
	{
		x[i][j]=malloc(p*sizeof(double));
	}
}

Uses dynamic allocation.

If the values of m and n are known at compile time you can also use:

double x[m][n][p];

28 Sort by a property
Sort the elements of the list (or array-like collection) items in ascending order of x.p, where p is a field of the type Item of the objects in items.

#include <stdlib.h>

int compareProp (const void *a, const void *b)
{
    return (*(const Item**)a)->p - (*(const Item**)b)->p;
}

qsort(items, N, sizeof(Item*), compareProp);

items is an array of Item* with length N

31 Recursive factorial (simple)
Create the recursive function f which returns the factorial of the non-negative integer i, calculated from f(i-1)

unsigned int f(unsigned int i)
{
	return i?i*f(i-1):1;
}

Overflows for i>20 in 64bits and for i>12 in 32bits

32 Integer exponentiation by squaring
Create function exp which calculates (fast) the value x power n.
x and n are non-negative integers.

unsigned int exp(unsigned int x,unsigned int n)
{
    if(n==0)
    {
        return 1;
    }
    if(n==1)
    {
        return x;
    }
    if(!(n%2))
    {
        return exp(x*x,n/2);
    }
    return x*exp(x*x,(n-1)/2);
}

38 Extract a substring
Find substring t consisting in characters i (included) to j (excluded) of string s.
Character indices start at 0 unless specified otherwise.
Make sure that multibyte characters are properly handled.

#include <stdlib.h>
#include <string.h>

char *t=malloc((j-i+1)*sizeof(char));
strncpy(t,s+i,j-i);

39 Check if string contains a word
Set the boolean ok to true if the string word is contained in string s as a substring, or to false otherwise.

#include <string.h>

int ok = strstr(s,word) != NULL;

    Demo
    Doc

41 Reverse a string
Create string t containing the same characters as string s, in reverse order.
Original string s must remain unaltered. Each character must be handled correctly regardless its number of bytes in memory.

#include <stdlib.h>
#include <string.h>

char *strrev(char *s)
{
	size_t len = strlen(s);
	char *rev = malloc(len + 1);

	if (rev) {
		char *p_s = s + len - 1;
		char *p_r = rev;

		for (; len > 0; len--)
			*p_r++ = *p_s--;
		*p_r = '\0';
	}
	return rev;
}

Returns NULL on failure

42 Continue outer loop
Print each item v of list a which is not contained in list b.
For this, write an outer loop to iterate on a and an inner loop to iterate on b.

int *v = a;
while (v < a+N)
{
    int *w = b;
    while (w < b+M)
    {
        if (*v == *w)
            goto OUTER;
               ++w;
    }
    printf("%d\n", *v);
       OUTER: ++v;
}

N is the length of a.
M is the length of b.

Using goto is usually considered bad practice in C.

43 Break outer loop
Look for a negative value v in 2D integer matrix m. Print it and stop searching.

#include <stdio.h>

int i,j;
for(i=0;i<sizeof(m)/sizeof(*m);i++)
{
	for(j=0;j<sizeof(*m)/sizeof(**m);j++)
	{
		if(m[i][j]<0)
		{
			printf("%d\n",m[i][j]);
			goto end;
		}
	}
}
end:

only works if m is allocated statically or on the stack, not if allocated in the heap.

edit: the statement above is misleading. It is referring to the use of sizeof() to set up the loops, and has nothing to do with using goto to break the loop. Using goto to break the loop will work as written, regardless of how the variables are allocated.

45 Pause execution for 5 seconds
Sleep for 5 seconds in current thread, before proceeding with the next instructions.

#include <unistd.h>

usleep(5000000);

usleep argument is in microseconds.
See : man 3 usleep

Alternative implementation:

#include <Windows.h>

Sleep(5000);

    Doc

48 Multi-line string literal
Assign to variable s a string literal consisting in several lines of text, including newlines.

char *s = "Huey\n"
          "Dewey\n"
          "Louie";

49 Split a space-separated string
Build list chunks consisting in substrings of the string s, separated by one or more space characters.

#include <string.h>

chunks[0] = strtok(s, " ");
for (int i = 1; i < N; ++i)
{
    chunks[i] = strtok(NULL, " ");
       if (!chunks[i])
        break;
}

N is the size of chunks.

strtok modifies s by adding null-characters between words.

50 Make an infinite loop
Write a loop that has no end clause.

#define forever while(1)

forever {
	// Do something
}

forever can be defined as a preprocessor constant to improve readability.

You may remove the curly braces if the block is only 1 instruction.

Alternative implementation:

for(;;){
	// Do something
}

You may remove the curly braces if the block is only 1 instruction.

Alternative implementation:

while(1){
	// Do something
}

You may remove the curly braces if the block is only 1 instruction.

Alternative implementation:

loop:
	goto loop;

    Demo

53 Join a list of strings
Concatenate elements of string list x joined by the separator ", " to create a single string y.

#include <string.h>

#define DELIM ", "
#define L 64

char y[L] = {'\0'};

for (int i = 0; i < N; ++i)
{
    if (i && x[i][0])
        strcat(y, DELIM);
       strcat(y, x[i]);
}

x is assumed to be an array containing N null-terminated strings.

L is arbitrary, but big enough to hold the concatenated string.

54 Compute sum of integers
Calculate the sum s of the integer list or array x.

int i,s;
for(i=s=0;i<n;i++)
{
	s+=x[i];
}

x is an array with size n.

Alternative implementation:

int sum = 0;
for (int i = 0; i < n; ++i) {
  sum += x[i];
}

55 Convert integer to string
Create the string representation s (in radix 10) of the integer value i.

#include <stdlib.h>

char s[0x1000]={};
itoa(i,s,10);

58 Extract file content to a string
Create the string lines from the content of the file with filename f.

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

FILE *file;
size_t len=0;
char *lines;
assert(file=fopen(f,"rb"));
assert(lines=malloc(sizeof(char)));

while(!feof(file))
{
	assert(lines=realloc(lines,(len+0x1000)*sizeof(char)));
	len+=fread(lines,1,0x1000,file);
}

assert(lines=realloc(lines,len*sizeof(char)));

Alternative implementation:

#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>

int err = 0;
int fd = 0;
void * ptr = NULL;
struct stat st;
if ((fd = open (f, O_RDONLY))
&& (err = fstat (fd, &st)) == 0
&& (ptr = mmap (NULL, st.st_size, PROT_READ, MAP_PRIVATE, fd, 0)) != -1) {
    const char * lines = ptr;
    puts (lines);
    munmap (ptr, st.st_size);
    close (fd);
}

Mapping the whole file into the process address space avoids allocating memory.

    Doc

59 Write to standard error stream
Print the message "x is negative" to standard error (stderr), with integer x value substitution (e.g. "-2 is negative").

#include <stdio.h>

fprintf(stderr,"%d is negative\n",x);

60 Read command line argument
Assign to x the string value of the first command line parameter, after the program name.

void main(int argc, char *argv[])
{
    char *x = argv[1];
}

argv[0] would be the program name. See §5.1.2.2.1 Program startup in linked doc n1570.pdf .

    Doc

61 Get current date
Assign to the variable d the current date/time value, in the most standard type.

#include <time.h>

time_t d=time(0);

Unix Timestamp

62 Find substring position
Set i to the first position of string y inside string x, if exists.

Specify if i should be regarded as a character index or as a byte index.

Explain the behavior when y is not contained in x.

#include <string.h>

int i=(int)(x-strstr(x,y));

65 Format decimal number
From the real value x in [0,1], create its percentage string representation s with one digit after decimal point. E.g. 0.15625 -> "15.6%"

#include <stdio.h>

printf("%.1lf%%\n", x * 100);

69 Seed random generator
Use seed s to initialize a random generator.

If s is constant, the generator output will be the same each time the program runs. If s is based on the current value of the system clock, the generator output will be different each time.

#include <stdlib.h>

srand(s);

70 Use clock as random generator seed
Get the current datetime and provide it as a seed to a random generator. The generator sequence will be different at each run.

#include <stdlib.h>
#include <time.h>

srand((unsigned)time(0));

71 Echo program implementation
Basic implementation of the Echo program: Print all arguments except the program name, separated by space, followed by newline.
The idiom demonstrates how to skip the first argument if necessary, concatenate arguments as strings, append newline and print it to stdout.

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    while (*++argv) {
        printf("%s", *argv);
        if (argv[1]) printf(" ");
    }
    printf("\n");
    return EXIT_SUCCESS;
}

74 Compute GCD
Compute the greatest common divisor x of big integers a and b. Use an integer type able to handle huge numbers.

#include <gmp.h>

mpz_t _a, _b, _x;
mpz_init_set_str(_a, "123456789", 10);
mpz_init_set_str(_b, "987654321", 10);
mpz_init(_x);

mpz_gcd(_x, _a, _b);
gmp_printf("%Zd\n", _x);

    Doc

75 Compute LCM
Compute the least common multiple x of big integers a and b. Use an integer type able to handle huge numbers.

#include <gmp.h>

mpz_t _a, _b, _x;
mpz_init_set_str(_a, "123456789", 10);
mpz_init_set_str(_b, "987654321", 10);
mpz_init(_x);

mpz_lcm(_x, _a, _b);
gmp_printf("%Zd\n", _x);

    Doc

77 Complex number
Declare a complex x and initialize it with value (3i - 2). Then multiply it by i.

#include <complex.h>

float complex _x = -2 + 3 * I;

_x *= I;

    Doc

78 "do while" loop
Execute a block once, then execute it again as long as boolean condition c is true.

do {
	someThing();
	someOtherThing();
} while(c);

The block code is not repeated in the source.

Alternative implementation:

do
{
  stuff()
} while ( c ) ;

79 Convert integer to floating point number
Declare the floating point number y and initialize it with the value of the integer x .

float y = (float)x;

The (float) isn't really necessary, unless x is a double type. The compiler will cast x automatically.

80 Truncate floating point number to integer
Declare integer y and initialize it with the value of floating point number x . Ignore non-integer digits of x .
Make sure to truncate towards zero: a negative x must yield the closest greater integer (not lesser).

int y = (int)x;

The (int) isn't really necessary. The compiler will cast x automatically.

81 Round floating point number to integer
Declare the integer y and initialize it with the rounded value of the floating point number x .
Ties (when the fractional part of x is exactly .5) must be rounded up (to positive infinity).

#include <math.h>

int y = (int)floorf(x + 0.5f);

82 Count substring occurrences
Find how many times string s contains substring t.
Specify if overlapping occurrences are counted.

#include <string.h>

unsigned n;
for (n = 0; s = strstr(s, t); ++n, ++s)
	;

Overlapping occurrences are counted.
This destroys the pointer s.

    Demo

84 Count bits set in integer binary representation
Count number c of 1s in the integer i in base 2.

E.g. i=6 → c=2

#include <stdint.h>

uint32_t c = i;
c = (c & 0x55555555) + ((c & 0xAAAAAAAA) >> 1);
c = (c & 0x33333333) + ((c & 0xCCCCCCCC) >> 2);
c = (c & 0x0F0F0F0F) + ((c & 0xF0F0F0F0) >> 4);
c = (c & 0x00FF00FF) + ((c & 0xFF00FF00) >> 8);
c = (c & 0x0000FFFF) + ((c & 0xFFFF0000) >> 16);

add even and odd bits
then add even and odd pairs of bits
then add even and odd quadruples of bits
then add even and odd octets of bits
then add whatever groups of 16 bits are called
done

with gcc you can also use the function _builtin_popcount

85 Check if integer addition will overflow
Write boolean function addingWillOverflow which takes two integers x, y and return true if (x+y) overflows.

An overflow may be above the max positive value, or below the min negative value.

#include <limits.h>
#include <stdbool.h>

bool addingWillOverflow(int x, int y) {
  return ((x > 0) && (y > INT_MAX - x)) ||
         ((x < 0) && (y < INT_MIN - x));
}

INT_MAX and INT_MIN are defined in limits.h header, bool type is defined in stdbool.h

87 Stop program
Exit immediately.
If some extra cleanup work is executed by the program runtime (not by the OS itself), describe it.

#include <stdlib.h>

exit (EXIT_SUCCESS);

Alternative implementation:

return 0;

Only works in main(), actually.

Alternative implementation:

#include <stdlib.h>

abort();

Terminates the process immediatly, without executing exit handlers or flushing streams.

    Doc

88 Allocate 1M bytes
Create a new bytes buffer buf of size 1,000,000.

#include <stdlib.h>

void *buf = malloc(1000000);

    Doc

89 Handle invalid argument
You've detected that the integer value of argument x passed to the current function is invalid. Write the idiomatic way to abort the function execution and signal the problem.

enum {
    E_OK,
    E_OUT_OF_RANGE
};

int square(int x, int *result) {
    if (x > 1073741823) {
        return E_OUT_OF_RANGE;
    }
    *result = x*x;
    return E_OK;
}

93 Pass a runnable procedure as parameter
Implement the procedure control which receives one parameter f, and runs f.

void control (void (*f)()) {
        (*f)();
}

95 Get file size
Assign to variable x the length (number of bytes) of the local file at path.

#include <stdio.h>

FILE *f = fopen(path, "rb");
fseek(f, 0, SEEK_END);
int x = ftell(f);
fclose(f);

SEEK_END isn't necessarily supported by all implementations of stdio.h, but I've never run into a problem with it.

Alternative implementation:

#include <sys/stat.h>

struct stat st;
if (stat (path &st) == 0) x = st.st_size;

POSIX function stat avoids opening the file

    Doc

96 Check string prefix
Set the boolean b to true if string s starts with prefix prefix, false otherwise.

#include <stdbool.h>
#include <string.h>

bool b = !strncmp(s, prefix, sizeof(prefix)-1);

100 Sort by a comparator
Sort elements of array-like collection items, using a comparator c.

#include <stdlib.h>


int c(const void *a,const void *b)
{
	int x = *(const int *)a;
	int y = *(const int *)b;

	if (x < y) return -1;
	if (x > y) return +1;
	return 0;
}

int main(void)
{
	int arr[]={1,6,3,7,2};
	qsort(arr,sizeof(arr)/sizeof(*arr),sizeof(*arr),c);

	return 0;
}

The comparison is often written as "return x - y;" instead which is broken due to possible integer over/underflow.

105 Current executable name
Assign to the string s the name of the currently executing program (but not its full path).

#include <string.h>

#ifdef _WIN32
#define PATH_SEP '\\'
#else
#define PATH_SEP '/'
#endif

int main(int argc, char* argv[])
{
    char *s = strchr(argv[0], PATH_SEP);
    s = s ? s + 1 : argv[0];

    return 0;
}

106 Get program working directory
Assign to string dir the path of the working directory.
(This is not necessarily the folder containing the executable itself)

#include <unistd.h>

char *dir = getcwd(NULL, 0);

various C library implementations may or may not support using getcwd() this way, with a NULL buffer pointer that tells getcwd() to malloc(3) the returned buffer, which the caller should free(3).

    Doc

107 Get folder containing current program
Assign to string dir the path of the folder containing the currently running executable.
(This is not necessarily the working directory, though.)

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>
#include <linux/limits.h>
#include <libgen.h>

int main()
{
    char exe[PATH_MAX], real_exe[PATH_MAX];
    ssize_t r;
    char *dir;

    if ((r = readlink("/proc/self/exe", exe, PATH_MAX)) < 0)
      exit(1);
    if (r == PATH_MAX)
	r -= 1;
    exe[r] = 0;
    if (realpath(exe, real_exe) == NULL)
	exit(1);
    dir = dirname(real_exe);
    puts(dir);
}

If the executable file that the current process is executing can be found searching $PATH, this is easier, but the general case can still be handled by examining where the symlink file /proc/self/exe points to.

    Doc

109 Number of bytes of a type
Set n to the number of bytes of a variable t (of type T).

n = sizeof (t);

110 Check if string is blank
Set the boolean blank to true if the string s is empty, or null, or contains only whitespace ; false otherwise.

#include <ctype.h>
#include <stdbool.h>

bool blank = true;
for (const char *p = s; *p; p++) {
	if (!isspace(*p)) {
		blank = false;
		break;
	}
}

s has type char*

    Doc

111 Launch other program
From current process, run program x with command-line parameters "a", "b".

#include <stdlib.h>

int system("x a b");

This spawns a shell and returns, when the child process has exited.

    Doc

117 Get list size
Set n to the number of elements of the list x.

size_t n = sizeof(x)/sizeof(*x);

Alternative implementation:

int n;
int x[5];
n = sizeof(x)/sizeof(*x);

C doesn't have the higher level concept of lists at least as many may understand it, so this completes the prompt using C arrays. sizeof(array) will return the amount of bytes all the elements of the array are taking up and sizeof(var) will return the amount of bytes a single variable is taking up. *x in this example is the same as x[0]; it retrieves the first element of the array, so we're dividing the amount of bytes total for the array by the amount of bytes each element uses.

120 Read integer from stdin
Read an integer value from the standard input into the variable n

#include <stdio.h>

int n;
scanf("%d", &n);

Alternative implementation:

#include <stdio.h>

int n[15];
fgets(n, 15, stdin);

int n[15]; Int with 15 bytes to use.

Fgets gets user input, and sets n to what it gets

122 Declare an enumeration
Create an enumerated type Suit with 4 possible values SPADES, HEARTS, DIAMONDS, CLUBS.

enum Suit {
    SPADES,
    HEARTS,
    DIAMONDS,
    CLUBS
};

123 Assert condition
Verify that predicate isConsistent returns true, otherwise report assertion violation.
Explain if the assertion is executed even in production environment or not.

#include <assert.h>

assert(isConsistent());

If NDEBUG is defined, the assert macro becomes void. Therefore, such expressions must not have side effects.

    Doc

126 Multiple return values
Write a function foo that returns a string and a boolean value.

#include <stdbool.h>

typedef struct {
    const char * const a;
    const bool b;
} RetStringBool;

RetStringBool foo() {
    return (RetStringBool) {.a = "Hello", .b = true};
}

127 Source code inclusion
Import the source code for the function foo body from a file "foobody.txt".

void foo()
{
#include "foobody.txt"
}

Same as C++

131 Successive conditions
Execute f1 if condition c1 is true, or else f2 if condition c2 is true, or else f3 if condition c3 is true.
Don't evaluate a condition when a previous condition was true.

if (c1)
{
    f1();
}else if (c2)
{
    f2();
}
else if (c3)
{
    f3();
}

137 Check if string contains only digits
Set the boolean b to true if the string s contains only characters in the range '0'..'9', false otherwise.

#include <string.h>

char b = 0;
int n = strlen(s);
for (int i = 0; i < n; i++) {
	if (! (b = (s[i] >= '0' && s[i] <= '9')))
		break;
}

    Demo

Alternative implementation:

#include <ctype.h>
#include <stdbool.h>
#include <string.h>

bool b = true;
const int n = strlen(s);
for (int i = 0; i < n; ++i) {
  if (!isdigit(s[i])) {
    b = false;
    break;
  }
}

    Demo

138 Create temp file
Create a new temporary file on the filesystem.

#include <stdlib.h>

const char tmpl[] = "XXXXXX.tmp";
int fd = mkstemp(tmpl);

Template must contain six X characters that will be modified by mkstemp

    Doc

142 Hexadecimal digits of an integer
Assign to string s the hexadecimal representation (base 16) of integer x.

E.g. 999 -> "3e7"

char s[32];
snprintf(s, sizeof(s), "%x", i);

    Doc

144 Check if file exists
Set boolean b to true if file at path fp exists on filesystem; false otherwise.

Beware that you should never do this and then in the next instruction assume the result is still valid, this is a race condition on any multitasking OS.

#include <unistd.h>
#include <stdbool.h>

bool b = access(_fp, F_OK) == 0

    Doc

149 Rescue the princess
As an exception, this content is not under license CC BY-SA 3.0 like the rest of this website.


155 Delete file
Delete from filesystem the file having path filepath.

#include <unistd.h>

int main(void)
{
	if (unlink(filepath) == -1)
		err(1, "unlink");
	return 0;
}

157 Declare constant string
Initialize a constant planet with string value "Earth".

const char *_planet = "Earth";

162 Execute procedures depending on options
execute bat if b is a program option and fox if f is a program option.

#include <unistd.h>

int main(int argc, char * argv[])
{
        int optch;
        while ((optch = getopt(argc, argv, "bf")) != -1) {
                switch (optch) {
                        case 'b': bat(); break;
                        case 'f': fox(); break;
                }
        }
        return 0;
}

    Doc

163 Print list elements by group of 2
Print all the list elements, two by two, assuming list length is even.

#include <stdio.h>

for (unsigned i = 0; i < sizeof(list) / sizeof(list[0]); i += 2)
	printf("%d, %d\n", list[i], list[i + 1]);

I'm treating list as an array not a list because C doesn't have lists built in.
The length had better be even or there'll be undefined behaviour to pay!

165 Last element of list
Assign to the variable x the last element of the list items.

int length = sizeof(items) / sizeof(items[0]);
int x = items[length - 1];

Only works if items has not decayed to a pointer.

length is defined as the size of the items array in bytes, divided by the size of its first element in bytes.

167 Trim prefix
Create the string t consisting of the string s with its prefix p removed (if s starts with p).

#include <string.h>

size_t l = strlen(p);
const char * t = strncmp(s, p, l) ? s : s + l;

strlen computes the prefix length and strncmp returns zero if the first l characters match

173 Format a number with grouped thousands
Number will be formatted with a comma separator between every group of thousands.

#define _POSIX_C_SOURCE 200809L
#include <locale.h>
#include <stdio.h>

setlocale(LC_ALL, "");
printf("%'d\n", 1000);

    Doc

176 Hex string to byte array
From hex string s of 2n digits, build the equivalent array a of n bytes.
Each pair of hexadecimal characters (16 possible values per digit) is decoded into one byte (256 possible values).

const char* hexstring = "deadbeef";
size_t length = sizeof(hexstring);
unsigned char bytearray[length / 2];

for (size_t i = 0, j = 0; i < (length / 2); i++, j += 2)
	bytearray[i] = (hexstring[j] % 32 + 9) % 25 * 16 + (hexstring[j+1] % 32 + 9) % 25;

178 Check if point is inside rectangle
Set boolean b to true if if the point with coordinates (x,y) is inside the rectangle with coordinates (x1,y1,x2,y2) , or to false otherwise.
Describe if the edges are considered to be inside the rectangle.

int isInsideRect(double x1, double y1, double x2, double y2, double px, double py){
	return px >= x1 && px <= x2 && py >= y1 && py <= y2;}

Using C convention with 1 for true and 0 for false.

Assuming that x1 < x2 and y1 < y2

180 List files in directory
Create the list x containing the contents of the directory d.

x may contain files and subfolders.
No recursive subfolder listing.

#include <dirent.h>

struct dirent ** x = NULL;
int n = scandir (p, &x, NULL, alphasort);

scandir allocates memory and returns the number of entries. each entry must be free'd. See also opendir, readdir and closedir and ftw for recursive traversal.

    Doc

182 Quine program
Output the source of the program.

int main(){char*s="int main(){char*s=%c%s%c;printf(s,34,s,34);return 0;}";printf(s,34,s,34);return 0;}

Alternative implementation:

main(p){printf(p="main(p){printf(p=%c%s%1$c,34,p);}",34,p);}

186 Exit program cleanly
Exit a program cleanly indicating no error to OS

#include <stdlib.h>

exit(EXIT_SUCCESS);

190 Call an external C function
Declare an external C function with the prototype

void foo(double *a, int n);

and call it, passing an array (or a list) of size 10 to a and 10 to n.

Use only standard features of your language.

void foo(double *a, int n);
double a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
foo (a, sizeof(a)/sizeof(*a));

Instead of hard coding the count, it should be calculated to avoid later mistakes with changed a[]!

191 Check if any value in a list is larger than a limit
Given a one-dimensional array a, check if any value is larger than x, and execute the procedure f if that is the case

unsigned i;
for (i = 0; i < sizeof(a) / sizeof(a[0]); ++i) {
	if (a[i] > x) {
		f();
		break;
	}
}

198 Abort program execution with error condition
Abort program execution with error condition x (where x is an integer value)

#include <stdlib.h>

exit(x);

Calls all functions registered with atexit, then flushes and closes all streams and finally terminates the process.

    Doc

204 Return fraction and exponent of a real number
Given a real number a, print the fractional part and the exponent of the internal representation of that number. For 3.14, this should print (approximately)

0.785 2

#include <math.h>
#include <stdio.h>

  double d = 3.14;
  double res;
  int e;

  res = frexp(d, &e);
  printf("%f %d\n",res,e);

205 Get an environment variable
Read an environment variable with the name "FOO" and assign it to the string variable foo. If it does not exist or if the system does not support environment variables, assign a value of "none".

#include <stdlib.h>

const char * foo = getenv("FOO");
if (foo == NULL) foo = "none";

Returns a pointer to the value or NULL

    Doc

208 Formula with arrays
Given the arrays a,b,c,d of equal length and the scalar e, calculate a = e*(a+b*c+cos(d)).
Store the results in a.

#include <math.h>

  for (i=0; i<n; i++)
    a[i] = e*(a[i]+b[i]*c[i]+cos(d[i]);

Assume n is the length.

252 Conditional assignment
Assign to the variable x the string value "a" if calling the function condition returns true, or the value "b" otherwise.

x = condition() ? "a" : "b";

256 Count backwards
Print the numbers 5, 4, ..., 0 (included), one line per number.

for (int i = 5; i >= 0; i--) {
	printf("%d\n", i);
}

262 Count trailing zero bits
Assign to t the number of trailing 0 bits in the binary representation of the integer n.

E.g. for n=112, n is 1110000 in base 2 ⇒ t=4

#include <stdio.h>

int t = -1;
if (n)
        while (! (n & 1<<++t));
else
        t = 8*sizeof(n);

299 Comment out a single line
Write a line of comments.

This line will not be compiled or executed.

// This is a comment.

343 Rename file
Rename the file at path1 into path2

#include <stdio.h>

rename(path1, path2);

    Doc


