- 
- 
- Declare the first line→package main
- Import fmt package→import ("fmt")
- Create the main function→func main() {}
- Use the println function from fmt package→fmt.Println()
- Statements are separated by newline and→;
- 
- How to check if Go is set up go version
- 
- labex.io courses
    -  Quick Start with Golang 
        -  Beginner's Guide to Go Programming 
            - ^^^**Knowledge Points:**^^^
                - ^^^Standard output statement^^^
                - ^^^Code structure^^^
                - ^^^Running a program^^^
                - ^^^Common functions in the^^^ `fmt` ^^^package^^^ 
            - what in the fmt package 
            - how to find packages
            - what is the file extension? {{.go}} 
            - print hello
                - package main
import "fmt"
func main() {
  fmt.Println("hello")
}
            - ^^^The first line, ^^^{{`package main`}}^^^, indicates that this program belongs to the^^^ `main` ^^^package. ^^^ 
                - declare main package
            - ^^^The second line,^^^ {{`import "fmt"`}}^^^, imports the Go^^^ `fmt` ^^^package^^^ 
                - ^^^which allows us to format text input and output.^^^ 
                - import fmt package
            - ^^^ The^^^ `main` ^^^function is where the program starts execution, and inside it,^^^ `fmt.Println("hello, world")` ^^^will print^^^ `hello, world` ^^^to the terminal.^^^
            - ^^^To run the program, open the terminal and enter the following command:^^^
                - run hello.go : {{go run hello.go }} 
            - # ^^^**Program Structure and Syntax**^^^
                - ^^^In Go, a package is the basic unit of code management. ^^^
                - ^^^Every Go program begins with a^^^ `package` ^^^declaration. ^^^
                - ^^^In this case,^^^ `package main` ^^^tells Go that the code is part of the main program that will be executed.^^^
                - ^^^The^^^ `import "fmt"` ^^^statement imports the Go^^^ `fmt` ^^^package, which is used for input and output. ^^^
                - ^^^Go has a rich standard library, which allows us to perform many tasks with ease. ^^^
                - ^^^The^^^ `fmt` ^^^package is used to format text output, as we saw in the previous step.^^^
                - define the main function
                    - {{func main}}() {
}
                - ^^^In Go, all functions must begin with^^^ `func`^^^. ^^^
                - ^^^Notice that the opening brace^^^ `{` ^^^is placed at the end of the line. ^^^
                - ^^^This is a Go convention, and it’s different from other programming languages that might place the opening brace on a new line.^^^ 
                - ^^^This is because Go expects the opening brace to be directly on the same line.^^^
                - ^^^The key statement in the program is^^^ `fmt.Println("hello, world")``(#3ba9ff)`^^^, which calls the^^^ `fmt``(#3ba9ff)` ^^^package's^^^ `Println``(#3ba9ff)` ^^^function to print the string^^^ `"hello, world"``(#3ba9ff)` ^^^to the console. ^^^
                - ^^^This function automatically adds a newline character at the end of the string.^^^ 
            - # ^^^**Running the Program**^^^
                - ^^^Go is a compiled language, but when we use the^^^ `go run` ^^^command, Go first compiles the source code and then runs the resulting executable. So, the command:^^^
                - `go run helloWorld.go` 
                - ^^^is equivalent to running these two commands:^^^
                    - `# Compile the program(#aca397)
go build helloWorld.go

# Execute the compiled program(#aca397)
./helloWorld` 
                - compile hello.go : go build hello.go
                - run the compiled executable (hello) : ./hello
            - # ^^^**Common Functions in the**^^^ `**fmt**` ^^^**Package**^^^
                - ^^^Here are three common output functions:^^^
                    1. {{`fmt.Print()`}} ^^^– Outputs the text without a newline.^^^ 
                    2. {{`fmt.Println()`}} ^^^– Outputs the text with a newline.^^^ 
                    3. {{`fmt.Printf()`}} ^^^– Outputs formatted text.^^^ 
                - print hello without newline
                    - fmt.Print("hello")
                - print hello with newline
                    - fmt.Println("hello")
                - print hello with a placeholder and newline
                    - {{fmt.Printf("%s\n", "hello"}})
                    - what is %s
                - ^^^The^^^ `fmt` ^^^package also provides other functions for reading input, error handling, and more, which will be covered in later exercises.^^^
        - GOPATH and Module
            - # ^^^**Introduction**^^^
                - ^^^In this lab, we will learn about two different ways of managing dependencies in Go: GOPATH and Go Modules. ^^^
                - ^^^These are essential concepts for organizing and managing Go projects effectively.^^^
                - ^^^**Knowledge Points:**^^^
                    - ^^^GOPATH^^^
                    - ^^^GOROOT^^^
                    - ^^^Go Modules^^^
            - # ^^^**Basic Module GOPATH**^^^
                - ^^^Before Go 1.11, Go used a specific workspace called^^^ `GOPATH` ^^^to store all Go code. In this step, we'll understand how the GOPATH works.^^^
                    1. `GOROOT` ^^^is the directory where Go is installed, including its tools and standard library packages.^^^
                    2. `GOPATH` ^^^is where your personal Go code resides, and it contains three directories:^^^
                        - ^^^**src**^^^^^^: Stores your project source code.^^^
                        - ^^^**bin**^^^^^^: Stores compiled executable files.^^^
                        - ^^^**pkg**^^^^^^: Stores compiled packages that are not executable.^^^
                - ^^^To check the current^^^ `GOPATH` ^^^and^^^ `GOROOT`^^^, run the following commands:^^^
                - check the current GOPATH : go env | grep GOPATH
                - check the current GOROOT : go env | grep GOROOT
                - ^^^These commands will display the paths for^^^ `GOPATH` ^^^and^^^ `GOROOT` ^^^on your machine.^^^
            - # ^^^**Initialize mod**^^^
                - ^^^Go Modules, introduced in Go 1.11 and enabled by default in Go 1.13, aim to solve two major issues:^^^
                    - ^^^**Over-reliance on GOPATH**^^^^^^: ^^^
                        - ^^^Before Go Modules, code had to be stored inside the^^^ `GOPATH/src` ^^^directory. ^^^
                        - ^^^With Go Modules, you can store your code anywhere on your system.^^^
                    - ^^^**Version dependency issues**^^^^^^: ^^^
                        - ^^^Go Modules allow projects to manage and track dependencies with specific versions, making it easier to work with multiple versions of the same package.^^^
                - initialize go module for directory foo : go mod init foo
            - # ^^^**Importing other packages with mod**^^^
                - ^^^In this step, we will demonstrate how to import and use other modules in your Go project.^^^
                - ^^^The^^^ `helloWorld` ^^^package in the^^^ `helloWorld` ^^^folder has been initialized with Go Modules. Similarly, the^^^ `test` ^^^package, which also uses Go Modules, imports the^^^ `Say` ^^^function from the^^^ `helloWorld` ^^^package.^^^
                - ^^^To explore this, run the following command:^^^
                    1. ^^^First, look at the structure of the^^^ `helloWorld` ^^^and^^^ `test` ^^^directories:^^^
                        - ```
helloWorld
├── go.mod
└── helloWorld.go

``````
test
``````

├── go.mod
└── test.go
```^^^ Explain Code^^^
                    2. ^^^Next, open the^^^ `test/go.mod` ^^^file. You should see the following:^^^
                        - ```
module test


``````
go
``````
(#cd77e6) 
``````
1.15
``````
(#dba16b)

require 
``````
"helloWorld"
``````
(#9fcc7e) v0
``````
.0
``````
(#dba16b)
``````
.1
``````
(#dba16b)
replace 
``````
"helloWorld"
``````
(#9fcc7e) => 
``````
"../helloWorld"
``````
(#9fcc7e)
```^^^ Explain Code^^^
                - ^^^The^^^ `replace` ^^^directive tells Go to use the local path^^^ `../helloWorld` ^^^instead of fetching it from an external repository. The^^^ `require` ^^^directive specifies that the^^^ `test` ^^^package depends on version^^^ `v0.0.1` ^^^of the^^^ `helloWorld` ^^^package.^^^
                - --------------------- Portal ---------------------Parameter
                    - module #Parameter
                        - [Description](Go%20Programming%20Language/labex.io%20courses/Quick%20Start%20with%20Golang/GOPATH%20and%20Module/Importing%20other%20packages%20with%20mod/Parameter/Parameter/Description.md)―Specifies the package
                    - require #Parameter
                        - [Description](Go%20Programming%20Language/labex.io%20courses/Quick%20Start%20with%20Golang/GOPATH%20and%20Module/Importing%20other%20packages%20with%20mod/Parameter/Parameter/Description.md)―Specifies dependencies
                    - replace #Parameter
                        - [Description](Go%20Programming%20Language/labex.io%20courses/Quick%20Start%20with%20Golang/GOPATH%20and%20Module/Importing%20other%20packages%20with%20mod/Parameter/Parameter/Description.md)―Replaces dependencies
                    - exclude #Parameter
                        - [Description](Go%20Programming%20Language/labex.io%20courses/Quick%20Start%20with%20Golang/GOPATH%20and%20Module/Importing%20other%20packages%20with%20mod/Parameter/Parameter/Description.md)―Excludes dependencies
                - ^^^To run the^^^ `test.go` ^^^file in the^^^ `test` ^^^package:^^^
                - ```
cd
``````
 ~/project/test
go run test.go
```^^^ Explain Code^^^
                - ^^^The output should be:^^^
                - `hello, world``(#c1bab0)``(#161a21)`^^^ Explain Code^^^
            - # ^^^**Importing Remote Packages**^^^
                - ^^^In Go, you can easily import remote packages. Let's demonstrate this by using a remote package from GitHub.^^^
                    1. ^^^Create a directory^^^ `remoteModule`^^^:^^^
                        - ```
cd
``````
 ~/project

``````
mkdir
``````
 remoteModule

``````
cd
``````
 remoteModule
```^^^ Explain Code^^^
                    2. ^^^Initialize the Go Module:^^^
                        - `go mod init remoteModule``(#c1bab0)``(#161a21)`^^^ Explain Code^^^
                    3. ^^^Create a file^^^ `remote.go` ^^^inside the^^^ `remoteModule` ^^^folder with the following content:^^^
                        - `touch``(#161a21)`` remote.go``(#c1bab0)``(#161a21)`^^^ Explain Code^^^
                        - ```
package
``````
(#cd77e6) main


``````
import
``````
(#cd77e6) (
    
``````
"github.com/labex-labs/golang-dev-code/chap02module"
``````
(#9fcc7e)
)


``````
func
``````
(#cd77e6) 
``````
main
``````
(#5fb7f9)() {
    chap02module.StringTobase64(
``````
"miiy"
``````
(#9fcc7e))
}
```^^^ Explain Code^^^
                        - ^^^This program imports the^^^ `chap02module` ^^^package from GitHub and uses its^^^ `StringTobase64` ^^^function.^^^
                    4. ^^^Run the^^^ `remote.go` ^^^file using the following commands:^^^
                        - ```go
get github.com/labex-labs/golang-dev-code/chap02module
go run -v remote.go
```^^^ Explain Code^^^
                        - > ^^^^^Tips: Free user can't access the internet, so you can't run this command.^^^^^ [^^^^^Upgrade to the Pro plan^^^^^](https://labex.io/pricing?utm_source=labby) ^^^^^to get access to the internet.^^^^^
                - ^^^The^^^ `go get` ^^^command will download the^^^ `chap02module` ^^^package from GitHub and place it in your module cache. Once that's done, the^^^ `go run` ^^^command will execute your program.^^^
            - # ^^^**Mini Test**^^^
                - ^^^In this step, we will test our knowledge by creating a new file that uses the^^^ `Hello` ^^^function from the remote module.^^^
                    1. ^^^Create a folder^^^ `remoteModule2`^^^:^^^
                        - ```
cd
``````
 ~/project

``````
mkdir
``````
 remoteModule2

``````
cd
``````
 remoteModule2
```^^^ Explain Code^^^
                    2. ^^^Initialize the Go Module:^^^
                        - `go mod init remoteModule2``(#c1bab0)``(#161a21)`^^^ Explain Code^^^
                    3. ^^^Create a file^^^ `remote2.go` ^^^with the following content:^^^
                        - `touch``(#161a21)`` remote2.go``(#c1bab0)``(#161a21)`^^^ Explain Code^^^
                        - ```
package
``````
(#cd77e6) main


``````
import
``````
(#cd77e6) (
    
``````
"github.com/labex-labs/golang-dev-code/chap02module"
``````
(#9fcc7e)
)


``````
func
``````
(#cd77e6) 
``````
main
``````
(#5fb7f9)() {
    chap02module.Hello()
}
```^^^ Explain Code^^^
                    4. ^^^Run the program:^^^
                        - ```go
get github.com/labex-labs/golang-dev-code/chap02module
go run remote2.go
```^^^ Explain Code^^^
                        - ^^^The output should be:^^^
                        - `hello``(#c1bab0)``(#161a21)`^^^ Explain Code^^^
        - Build a Modular Go Project 
            - # ^^^**Introduction**^^^
                - [Size]();-[H1]()
            - ^^^In this challenge, you'll demonstrate your understanding of Go Modules by creating a modular project that showcases package management skills for a small utility library. The challenge involves creating a utility package with a function that converts a string to uppercase, and a main package that imports and uses the utility package's function. You'll also need to initialize Go Modules for both packages and ensure the main package successfully runs and prints the converted string.^^^
            - ^^^This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level challenge with a^^^ ^^^97.37%^^^ ^^^pass rate.^^^
            - ![](https://remnote-user-data.s3.amazonaws.com/e3JqVP7SH64pzgNFUfRbmMd6TfX-76n15dTnQVXQT-MJDgB5vRABdnoKflmUhpG2WbEFD1X8DASg4NzhltKsvdija2X3Mi3tEohWtsTjMIMkKCwDioC-v1OhKYnsVHSV.png)^^^^^**Labby**^^^^^ 
            - 
            - # ^^^**Build a Modular Go Project**^^^
                - [Size]();-[H1]()
            - ^^^In this challenge, you'll demonstrate your understanding of Go Modules by creating a modular project that showcases package management skills for a small utility library. To simplify the process, we've provided a setup script that initializes the project structure and pre-fills the basic code framework. Your task is to complete the^^^ `TODO` ^^^sections in the code.^^^
            - ## ^^^**Tasks**^^^
                1. ^^^Navigate to^^^ `~/project/utility/helper.go` ^^^and complete the^^^ `TODO` ^^^section:^^^
                    - `// ``(#aca397)``(#161a21)``TODO:``(#cd77e6)``(#161a21)`` Implement the ToUpperCase function using strings.ToUpper``(#aca397)``(#161a21)`^^^ Explain Code^^^
                2. ^^^Navigate to^^^ `~/project/main/main.go` ^^^and complete the^^^ `TODO` ^^^sections:^^^
                    - ```
// 
``````
(#aca397)
``````
TODO:
``````
(#cd77e6)
``````
 Call the utility.ToUpperCase function
``````
(#aca397)

``````
// 
``````
(#aca397)
``````
TODO:
``````
(#cd77e6)
``````
 Print the result using fmt.Println
``````
(#aca397)
```^^^ Explain Code^^^
                - [Size]();-[H2]()
            - ## ^^^**Requirements**^^^
                - ^^^Complete the provided^^^ `~/project/utility/helper.go` ^^^and^^^ `~/project/main/main.go` ^^^files by filling in the^^^ `TODO` ^^^sections.^^^
                - ^^^The utility package should define a function named^^^ `ToUpperCase` ^^^that converts a string to uppercase.^^^
                - ^^^The main package should call the^^^ `ToUpperCase` ^^^function and print its result.^^^
                - [Size]();-[H2]()
            - ## ^^^**Examples**^^^
                - [Size]();-[H2]()
            - ^^^After completing the^^^ `TODO` ^^^sections, your project structure should look like this:^^^
            - ```
~/project/
├── utility/
│   ├── 
``````
go
``````
(#cd77e6).mod
│   └── helper.
``````
go
``````
(#cd77e6)
└── main/
    ├── 
``````
go
``````
(#cd77e6).mod
    └── main.
``````
go
``````
(#cd77e6)
```^^^ Explain Code^^^
            - ^^^When you run the main package, the output should be:^^^
            - ```
cd
``````
 ~/project/main
go get utility
go run main.go
```^^^ Explain Code^^^
            - `HELLO, WORLD``(#c1bab0)``(#161a21)`^^^ Explain Code^^^
            - ## ^^^**Hints**^^^
                - ^^^The^^^ `strings.ToUpper` ^^^function from the standard library can help you convert a string to uppercase.^^^
                - ^^^Use^^^ `go mod init` ^^^to initialize Go Modules. (It's already done for you)^^^
                - ^^^Use^^^ `go get utility` ^^^to import the local utility package in the main package.^^^
                - [Size]();-[H2]()
            - ![](https://remnote-user-data.s3.amazonaws.com/1YJunwo8JoRRUEb1lICcXboPRTYdfnIGB5worlrNhL__p8OT73Fi_0P_OR-Jy5uNwOnvsLV1NADao-jO_FCHlWB8u3xyS5bJZD8kRdHeDMUP-Pqchduxb86esSl24ct0.png)^^^^^**Labby**^^^^^ 
            - 
            - # ^^^**Summary**^^^
                - [Size]();-[H1]()
            - ^^^In summary, this challenge requires you to create a modular Go project that demonstrates your understanding of Go Modules and package management. You'll need to develop a utility package with a function to convert a string to uppercase, and a main package that imports and uses the utility package's function. The challenge also involves initializing Go Modules for both packages and ensuring the main package runs successfully and prints the converted string.^^^
        - Creating and Importing Go Packages 
            - ^^^^^Declaring and Defining Packages^^^^^
            - ^^^^^Single-Item Import^^^^^
            - ^^^^^Grouped Imports^^^^^
            - ^^^^^Dot Import^^^^^
            - ^^^^^Alias Import^^^^^
            - ^^^^^Anonymous Import^^^^^
            - ^^^^^Understanding the init() Function^^^^^
        - ^^^^^Build a Math Utility Package^^^^^
            - ^^^^^Import and Use the mathutil Package^^^^^
        - ^^^^^Introduction to Go Variables^^^^^
            - ^^^^^What is a Variable?^^^^^
            - ^^^^^General Declaration Method^^^^^
            - ^^^^^Batch Declaration Method^^^^^
            - ^^^^^Default Initialization^^^^^
            - ^^^^^Standard Initialization^^^^^
            - ^^^^^Type Declaration by Inference^^^^^
            - ^^^^^Variable Scope^^^^^
            - ^^^^^Variable Lifetime^^^^^
            - ^^^^^Constants^^^^^
        - ^^^^^Craft Book Inventory Variables^^^^^
            - ^^^^^Craft Book Inventory Variables^^^^^
        - ^^^^^Data Processing with Operators in Golang^^^^^
            - ^^^^^Basic Form^^^^^
            - ^^^^^Increment and Decrement Operators^^^^^
            - ^^^^^Relational Operators^^^^^
            - ^^^^^Logical Operators^^^^^
            - ^^^^^Execution Order of Logical Operators^^^^^
            - ^^^^^Assignment Operators^^^^^
        - ^^^^^Calculate Product Discount Price^^^^^
            - ^^^^^Calculate Product Discount Price^^^^^
        - ^^^^^Numerical Types in Golang^^^^^
            - ^^^^^Integers^^^^^
            - ^^^^^Floating-Point Numbers^^^^^
            - ^^^^^Boolean Types^^^^^
            - ^^^^^Complex Numbers^^^^^
            - ^^^^^Literal Value Syntax^^^^^
        - ^^^^^Convert and Calculate Numeric Types^^^^^
            - ^^^^^Convert and Calculate Numeric Types^^^^^
        - ^^^^^Character Types in Golang^^^^^
            - ^^^^^ASCII Encoding^^^^^
            - ^^^^^Unicode Character Set^^^^^
            - ^^^^^UTF-8 Encoding^^^^^
            - ^^^^^byte and rune^^^^^
            - ^^^^^Quiz^^^^^
        - ^^^^^Decode Unicode Emojis^^^^^
            - ^^^^^Decode Unicode Emojis^^^^^
        - ^^^^^Go String Fundamentals^^^^^
            - ^^^^^What is a String^^^^^
            - ^^^^^Creating a String^^^^^
            - ^^^^^Declaring a String^^^^^
            - ^^^^^Getting the Length of a String^^^^^
            - ^^^^^Accessing String Elements^^^^^
            - ^^^^^Converting Strings and Integers^^^^^
            - ^^^^^Concatenating Strings^^^^^
            - ^^^^^Removing Leading and Trailing Spaces from a String^^^^^
        - ^^^^^Process User Registration Strings^^^^^
            - ^^^^^Process User Registration Strings^^^^^
        - ^^^^^Go Constants Fundamentals^^^^^
            - ^^^^^What Are Constants?^^^^^
            - ^^^^^Declaring Constants^^^^^
            - ^^^^^The iota Constant Generator^^^^^
            - ^^^^^Quiz^^^^^
        - ^^^^^Define Server Size Constants^^^^^
            - ^^^^^Define Server Size Constants^^^^^
        - ^^^^^If Branch Statement in Golang^^^^^
            - ^^^^^if statement^^^^^
            - ^^^^^if else statement^^^^^
            - ^^^^^else if statement^^^^^
            - ^^^^^Initialization Statement in the if Statement^^^^^
        - ^^^^^Sort Tasks with Conditional Logic^^^^^
            - ^^^^^Sort Tasks with Conditional Logic^^^^^
        - ^^^^^Switch-Case Branch Statements in Golang^^^^^
            - ^^^^^Basic Syntax^^^^^
            - ^^^^^Multiple Values in a Branch^^^^^
            - ^^^^^switch Statements with No Conditional Variable^^^^^
            - ^^^^^fallthrough Statement^^^^^
            - ^^^^^Initialization Statement in switch^^^^^
        - ^^^^^Implement Weather Advice Switch^^^^^
            - ^^^^^Implement the Weather Advice Function^^^^^
        - ^^^^^For Loops in Golang^^^^^
            - ^^^^^Characters in a String^^^^^
            - ^^^^^For Loop Syntax^^^^^
            - ^^^^^Using the For Loop^^^^^
            - ^^^^^The "break" Keyword^^^^^
            - ^^^^^The "continue" Keyword^^^^^
        - ^^^^^Reverse String with Go Loop^^^^^
            - ^^^^^Reverse String with Go Loop^^^^^
        - ^^^^^Goto Statement Usage^^^^^
            - ^^^^^Understanding the Syntax of goto^^^^^
            - ^^^^^Replacing break with goto^^^^^
            - ^^^^^Implementing a for Loop Using goto^^^^^
            - ^^^^^Exiting Nested Loops with goto^^^^^
        - ^^^^^Solve Nested Loop Complexity with Goto^^^^^
            - ^^^^^Solve Nested Loop Complexity with Goto^^^^^
        - ^^^^^Array Operations in Golang^^^^^
            - ^^^^^Array Definition^^^^^
            - ^^^^^Initialization List^^^^^
            - ^^^^^Inferred Length Initialization^^^^^
            - ^^^^^Initialization with Specified Indices^^^^^
            - ^^^^^Array Traversal^^^^^
            - ^^^^^Accessing Array Elements^^^^^
            - ^^^^^Value Type of Arrays^^^^^
        - ^^^^^Initialize Employee Names Array^^^^^
            - ^^^^^Initialize Employee Names Array^^^^^
        - ^^^^^Multidimensional Arrays in Golang^^^^^
            - ^^^^^Definition of a Two-Dimensional Array^^^^^
            - ^^^^^Initialization of a Two-Dimensional Array^^^^^
            - ^^^^^Initialization of a Two-Dimensional Array Using an Initialization List^^^^^
            - ^^^^^Initialization of a Two-Dimensional Array with Inferred Length^^^^^
            - ^^^^^Initializing a Two-Dimensional Array with Specified Index Values^^^^^
            - ^^^^^Traversing a Two-Dimensional Array^^^^^
            - ^^^^^Practical Uses of Arrays^^^^^
            - ^^^^^Upscaling a Two-Dimensional Array^^^^^
        - ^^^^^Design a Student Grade Tracker^^^^^
            - ^^^^^Design a Student Grade Tracker^^^^^
        - ^^^^^Golang Slice Data Structures^^^^^
            - ^^^^^What is a Slice^^^^^
            - ^^^^^Define a Slice^^^^^
            - ^^^^^A Slice is a Reference to an Array^^^^^
            - ^^^^^Data Structure of a Slice^^^^^
            - ^^^^^Operations on Slices: Add, Delete, Modify, and Search^^^^^
            - ^^^^^Expanding Slices^^^^^
            - ^^^^^Copying Slices^^^^^
            - ^^^^^Traversing Slices^^^^^
        - ^^^^^Slice Log Filter Challenge^^^^^
            - ^^^^^Implement Slice Log Filter Function^^^^^
        - ^^^^^Go Dictionary Fundamentals^^^^^
            - ^^^^^Introduction to Dictionaries^^^^^
            - ^^^^^Declaration of Maps^^^^^
            - ^^^^^The Initial Value nil^^^^^
            - ^^^^^Declaration with the make Keyword^^^^^
            - ^^^^^Manually Initializing an Empty Map^^^^^
            - ^^^^^Actually Initializing the Dictionary^^^^^
            - ^^^^^Adding and Updating Dictionary Elements^^^^^
            - ^^^^^Deleting Dictionary Elements^^^^^
            - ^^^^^Searching for Dictionary Elements^^^^^
            - ^^^^^Iterating Over Dictionaries^^^^^
        - ^^^^^Manage Student Grades with Go Maps^^^^^
            - ^^^^^Manage Student Grades with Go Maps^^^^^
        - ^^^^^Sorting Go Dictionaries^^^^^
            - ^^^^^Sorting Dictionaries^^^^^
            - ^^^^^Sort by Key^^^^^
            - ^^^^^Swapping Keys and Values in a Dictionary^^^^^
            - ^^^^^Sort by Value^^^^^
            - ^^^^^Sorted by sort.Slice^^^^^
            - ^^^^^Little Test^^^^^
            - ^^^^^Slices of Dictionaries^^^^^
            - ^^^^^Dictionaries with Slices as Values^^^^^
            - ^^^^^Reference Type Characteristics of Dictionaries^^^^^
        - ^^^^^Sort Student Grades Dynamically^^^^^
            - ^^^^^Sort Student Grades Dynamically^^^^^
        - ^^^^^Channel Primitives in Golang^^^^^
            - ^^^^^Overview of Channels^^^^^
            - ^^^^^Channel Types and Declaration^^^^^
            - ^^^^^Channel Initialization^^^^^
            - ^^^^^Channel Operations^^^^^
            - ^^^^^Channel Blocking^^^^^
            - ^^^^^Unidirectional Channels^^^^^
        - ^^^^^Build a Simple Channel Data Pipeline^^^^^
            - ^^^^^Build a Simple Channel Data Pipeline^^^^^
        - ^^^^^Structures in Golang^^^^^
            - ^^^^^Definition of Structure^^^^^
            - ^^^^^Instantiation using var^^^^^
            - ^^^^^Initial Value of a Structure^^^^^
            - ^^^^^Instantiation using new^^^^^
            - ^^^^^Instantiation using :=^^^^^
        - ^^^^^Design Student Struct in Go^^^^^
            - ^^^^^Design Student Struct in Go^^^^^
        - ^^^^^Functions in Golang^^^^^
            - ^^^^^Creating and Running a Basic Program^^^^^
            - ^^^^^Function Declaration^^^^^
            - ^^^^^Using the init Function^^^^^
            - ^^^^^Returning Multiple Values from a Function^^^^^
            - ^^^^^Working with Variadic Parameters^^^^^
        - ^^^^^Design Flexible Math Function^^^^^
            - ^^^^^Design Flexible Math Function^^^^^
        - ^^^^^Anonymous Functions in Golang^^^^^
            - ^^^^^Understanding Anonymous Functions^^^^^
            - ^^^^^Creating an Anonymous Function without Parameters^^^^^
            - ^^^^^Using Parameters in Anonymous Functions^^^^^
            - ^^^^^Returning Values from Anonymous Functions^^^^^
            - ^^^^^Declaring and Calling Anonymous Functions Immediately^^^^^
            - ^^^^^Using Anonymous Functions as Callback Functions^^^^^
        - ^^^^^Design Flexible Math Transformations^^^^^
            - ^^^^^Design Flexible Math Transformations^^^^^
    -  ^^^^^**What Day Is It Today?**^^^^^
        - ^^^^^What Day Is It Today?^^^^^
    -  ^^^^^**Development of Golang Caching Component**^^^^^
        - ^^^^^Development of Golang Caching Component^^^^^
            - ^^^^^What Is a Cache?^^^^^
            - ^^^^^Design of Cache System^^^^^
            - ^^^^^Development Preparation^^^^^
            - ^^^^^Basic Structure of a Cache System^^^^^
            - ^^^^^Implementing CRUD Interface for Cache System^^^^^
            - ^^^^^Import and Export of Cache System^^^^^
            - ^^^^^Other Interfaces of the Cache System^^^^^
            - ^^^^^Testing the Cache System^^^^^
    -  ^^^^^**Cache Request Execution Results**^^^^^
        - ^^^^^Cache Request Execution Results^^^^^
    -  ^^^^^**Implement JSON Comment Interpreter**^^^^^
        - ^^^^^Implement JSON Comment Interpreter^^^^^
    -  ^^^^^**Transparent Modification of HTTP Requests**^^^^^
        - ^^^^^Transparent Modification of HTTP Requests^^^^^
    - 
