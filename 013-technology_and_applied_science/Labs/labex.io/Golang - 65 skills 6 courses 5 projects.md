-  **Quick Start with Golang - **44 labs
    - **Beginner's Guide to Go Programming**
        - 
        -  **First Go Program** 
            - what is the file ext for Go? {{.go}} 
            - You also can create a new file using the `touch` command:
                - `touch helloWorld.go` 
            - Now, open the file and write the following code:
                - `package main`
                - 
                - `import "fmt"`
                - 
                - `func main() {`
                    - `fmt.Println("hello, world")`
                - `}`
            - The first line, {{`package main`}}, indicates that this program belongs to the {{`main`}} package. 
            - The second line, {{`import "fmt"`}}, imports the Go {{`fmt`}} package, which allows us to format text input and output. 
            - The {{`main`}} function is where the program starts execution, and inside it, `fmt.Println("hello, world")` will print `hello, world` to the terminal.
            - To run the program, open the terminal and enter the following command:
                - {{`go run `}}`helloWorld.go` 
            - If everything is set up correctly, you should see the output:
                - `hello, world` 
            - This is a simple "Hello World" program. Now, let's explain the code and operations line by line.
        -  **Program Structure and Syntax**
            - In Go, a {{package}} is the basic unit of code management. 
            - Every Go program begins with a {{`package`}} declaration. 
            - In this case, {{`package main`}} tells Go that the code is part of the main program that will be executed.
            - The {{`import "fmt"`}} statement imports the Go {{`fmt`}} package, which is used for input and output. 
            - Go has a rich standard library, which allows us to perform many tasks with ease. 
            - The {{`fmt`}} package is used to format text output, as we saw in the previous step.
            - Next, we define the {{`main`}} function:
                - {{func main() {
}}} 
            - In Go, all functions must begin with {{`func`}}. 
            - Notice that the opening brace `{` is placed at the end of the line. 
            - This is a Go convention, and it’s different from other programming languages that might place the opening brace on a new line.
            - If you mistakenly place the opening brace on a new line like this:
                - func main()
{
}
            - You will get a compilation error:
            - ```
$ go run helloWorld.go
## command-line-arguments
./helloWorld.go:7:1: syntax error: unexpected semicolon or newline before {
``` 
            - This is because Go expects the opening brace to be directly on the same line.
            - The key statement in the program is `fmt.Println("hello, world")`, which calls the {{`fmt`}} package's {{`Println`}} function to print the string `"hello, world"` to the console. 
            - This function automatically adds a newline character at the end of the string.
        -  **Running the Program**
            - Go is a compiled language, but when we use the {{`go run`}} command, Go first compiles the source code and then runs the resulting executable. So, the command:
            - `g`{{`o run`}}` helloWorld.go` 
            - is equivalent to running these two commands:
            - ```
# Compile the program
go build helloWorld.go

# Execute the compiled program
./helloWorld
``` 
            - To try a new example, let's modify the program to greet other Gophers. Create a new file called `helloGopher.go`, and replace the code with:
            - You can create a new file using the `touch` command:
            - `touch helloGopher.go` 
            - ```
package main

import "fmt"

func main() {
 fmt.Println("hello Gopher.")
 fmt.Println("hello Gopher.")
 fmt.Println("hello Gopher.")
}
``` 
            - Now, instead of using `go run`, we'll use `go build` to compile the program, then run the generated executable:
            -  Compile the go program: {{`go build`}}` helloGopher.go` 
            - ```


# Run the compiled executable
./helloGopher
``` 
            - This will output:
            - ```
hello Gopher.
hello Gopher.
hello Gopher.
``` 
        -  **Common Functions in the** `**fmt**` **Package**
            - In Step 1, we used the `Println()` function from the `fmt` package to print output. The `fmt` package is one of the most commonly used packages in Go and offers several functions for formatting output.
            - Here are three common output functions:
                1. {{`fmt.Print()`}} – Outputs the text without a newline.
                2. {{`fmt.Println()`}} – Outputs the text with a newline.
                3. {{`fmt.Printf()`}} – Outputs formatted text.
            - Let's explore these functions in more detail. Create a new file called `fmt.go` and enter the following code:
            - ```
package main

import "fmt"

func main() {
    // Standard output
    fmt.Print("hello")
    fmt.Print("world")

    // Println adds a newline character after the standard output
    fmt.Println()
    fmt.Println("labex")

    // Printf provides formatted output
    fmt.Printf("%s\n", "London")
}
``` 
            - Run the program using the `go run` command:
            - `go run fmt.go` 
            - Explanation:
                - `fmt.Print("hello")` and `fmt.Print("world")` output text on the same line because `Print` does not add a newline.
                - `fmt.Println()` outputs a newline to separate the lines.
                - `fmt.Printf("%s\n", "London")` formats the output using the `%s` placeholder for the string "London".
            - Here’s a quick comparison of the functions:
                - functions - standard output - line break - formatted output
                    - {{Print}} - yes - no - no
                    - {{Println}} - yes - yes - no
                    - {{Printf}} - no - no - yes
            - The {{`fmt`}} package also provides other functions for reading input, error handling, and more, which will be covered in later exercises.
    - **Craft a Personalized Go Greeting**
        - 
        -  **Introduction**
            - In this challenge, you will create a welcoming Go script that demonstrates your programming skills. 
            - The goal is to build a personalized greeting for a new team member, showcasing your ability to use various output functions from the `fmt` package. 
            - You will be required to include a team member's name, and ensure the program compiles and runs without errors.
        -  **Craft a Personalized Go Greeting**
            - Welcome to the tech startup's onboarding challenge! Your mission is to create a welcoming Go script that demonstrates your programming skills.
            - ## **Tasks**
                - Open the Go program named `team_greeting.go` in the `~/project` directory
                - Use three different `fmt` package output functions in your program:
                    1. `fmt.Print()`
                    2. `fmt.Println()`
                    3. `fmt.Printf()`
                - Include a personalized greeting that welcomes a new team member
            - ## **Requirements**
                - The program must be saved as `team_greeting.go` in the `~/project` directory
                - Use all three output functions: `Print()`, `Println()`, and `Printf()`
                - Include at least one variable with the team member's name
                - Ensure the program compiles and runs without errors
            - ## **Examples**
            - After completing the tasks, compile and run your program using the following command:
            - ```
cd ~/project
go run team_greeting.go
``` 
            - Example output might look like:
            - ```
Hello Gopher
Welcome to the amazing tech team!
New Member: Alice joins our innovative startup
``` 
            - ## **Hints**
                - Remember to import the `fmt` package
                - Use `%s` placeholder in `Printf()` for string formatting
                - Check your syntax carefully
                - Use meaningful variable names
        -  **Summary**
            - In summary, this challenge requires you to create a Go program named `team_greeting.go` that demonstrates your programming skills. The program should include a personalized greeting for a new team member, utilizing three different output functions from the `fmt` package: `Print()`, `Println()`, and `Printf()`. The program must be saved in the `~/project` directory and compile and run without errors.
    - **GOPATH and Module**
        - 
        - **Preparation**
            - Decompress the helloWorld.tar.gz file in the current directory: {{`tar -xzf`}}` helloWorld.tar.gz ` 
        - **Basic Module GOPATH**
            - Before Go 1.11, Go used a specific workspace called {{GOPATH}} to store all Go code. 
            - In this step, we'll understand how the GOPATH works.
            - {{GOROOT}} is the directory where Go is installed, including its tools and standard library packages.
            - {{GOPATH}} is where your personal Go code resides, and it contains three directories:
                - {{src}}: Stores your project source code.
                - {{bin}}: Stores compiled executable files.
                - {{pkg}}: Stores compiled packages that are not executable.
            - To check the current GOPATH and GOROOT, run the following commands:
            -  Check the GOPATH directory: {{`go env | grep GOPATH`}}` ` 
            -  Check the GOROOT directory: {{`go env | grep GOROOT`}} 
        - **Initialize mod**
            - Go Modules, introduced in Go 1.11 and enabled by default in Go 1.13, aim to solve two major issues:
            - 
            - Over-reliance on GOPATH: Before Go Modules, code had to be stored inside the GOPATH/src directory. With Go Modules, you can store your code anywhere on your system.
            - Version dependency issues: Go Modules allow projects to manage and track dependencies with specific versions, making it easier to work with multiple versions of the same package.
            - In this step, we will initialize a Go Module for a new project.
            - 
            - Initialize the Go Module for this project: {{`go mod init`}}` testHello` 
        - **Importing other packages with mod**
            - In this step, we will demonstrate how to import and use other modules in your Go project.
            - 
            - The helloWorld package in the helloWorld folder has been initialized with Go Modules. Similarly, the test package, which also uses Go Modules, imports the Say function from the helloWorld package.
            - 
            - To explore this, run the following command:
            - 
            - First, look at the structure of the helloWorld and test directories:
            - 
            - helloWorld
            - ├── go.mod
            - └── helloWorld.go
            - test
            - ├── go.mod
            - └── test.go
                - 
            - Next, open the test/go.mod file. You should see the following:
            - 
            - module test
            - 
            - go 1.15
            - 
            - require "helloWorld" v0.0.1
            - replace "helloWorld" => "../helloWorld"
                - 
            - The replace directive tells Go to use the local path ../helloWorld instead of fetching it from an external repository. The require directive specifies that the test package depends on version v0.0.1 of the helloWorld package.
            - 
            - Parameter Description
            - {{module}} Specifies the package
            - {{require}} Specifies dependencies
            - {{replace}} Replaces dependencies
            - {{exclude}} Excludes dependencies
        - **Importing Remote Packages**
            - In Go, you can easily import remote packages. Let's demonstrate this by using a remote package from GitHub.
            - 
            - Create a directory remoteModule:
            - 
            - cd ~/project
            - mkdir remoteModule
            - cd remoteModule
                - 
            - Initialize the Go Module:
            - 
            - go mod init remoteModule
                - 
            - Create a file remote.go inside the remoteModule folder with the following content:
            - 
            - touch remote.go
                - 
            - package main
            - 
            - import (
                - "github.com/labex-labs/golang-dev-code/chap02module"
            - )
            - 
            - func main() {
                - chap02module.StringTobase64("miiy")
            - }
                - 
            - This program imports the chap02module package from GitHub and uses its StringTobase64 function.
            - 
            - Run the remote.go file using the following commands:
            - 
            - go get github.com/labex-labs/golang-dev-code/chap02module
            - go run -v remote.go
            - 
            - The go get command will download the chap02module package from GitHub and place it in your module cache. 
            - Once that's done, the go run command will execute your program.
        - **Mini Test**
            - In this step, we will test our knowledge by creating a new file that uses the Hello function from the remote module.
            - 
            - Create a folder remoteModule2:
            - 
            - cd ~/project
            - mkdir remoteModule2
            - cd remoteModule2
                - 
            - Initialize the Go Module:
            - 
            - go mod init remoteModule2
                - 
            - Create a file remote2.go with the following content:
            - 
            - touch remote2.go
                - 
            - package main
            - 
            - import (
                - "github.com/labex-labs/golang-dev-code/chap02module"
            - )
            - 
            - func main() {
                - chap02module.Hello()
            - }
                - 
            - Run the program:
            - 
            - go get github.com/labex-labs/golang-dev-code/chap02module
            - go run remote2.go
    - Build a Modular Go Project
        - 
        -  **Introduction**
            - In this challenge, you'll demonstrate your understanding of Go Modules by creating a modular project that showcases package management skills for a small utility library. 
            - The challenge involves creating a utility package with a function that converts a string to uppercase, and a main package that imports and uses the utility package's function. 
            - You'll also need to initialize Go Modules for both packages and ensure the main package successfully runs and prints the converted string.
        -  **Build a Modular Go Project**
            - In this challenge, you'll demonstrate your understanding of Go Modules by creating a modular project that showcases package management skills for a small utility library. To simplify the process, we've provided a setup script that initializes the project structure and pre-fills the basic code framework. Your task is to complete the `TODO` sections in the code.
            - ## **Tasks**
                1. Navigate to `~/project/utility/helper.go` and complete the `TODO` section:
                    - `// TODO: Implement the ToUpperCase function using strings.ToUpper` 
                2. Navigate to `~/project/main/main.go` and complete the `TODO` sections:
                    - ```
// TODO: Call the utility.ToUpperCase function
// TODO: Print the result using fmt.Println
``` 
            - ## **Requirements**
                - Complete the provided `~/project/utility/helper.go` and `~/project/main/main.go` files by filling in the `TODO` sections.
                - The utility package should define a function named `ToUpperCase` that converts a string to uppercase.
                - The main package should call the `ToUpperCase` function and print its result.
            - ## **Examples**
            - After completing the `TODO` sections, your project structure should look like this:
            - ```
~/project/
├── utility/
│   ├── go.mod
│   └── helper.go
└── main/
    ├── go.mod
    └── main.go
``` 
            - When you run the main package, the output should be:
            - ```
cd ~/project/main
go get utility
go run main.go
``` 
            - `HELLO, WORLD` 
            - ## **Hints**
                - The `strings.ToUpper` function from the standard library can help you convert a string to uppercase.
                - Use `go mod init` to initialize Go Modules. (It's already done for you)
                - Use `go get utility` to import the local utility package in the main package.
        -  **Summary**
            - In summary, this challenge requires you to create a modular Go project that demonstrates your understanding of Go Modules and package management. You'll need to develop a utility package with a function to convert a string to uppercase, and a main package that imports and uses the utility package's function. The challenge also involves initializing Go Modules for both packages and ensuring the main package runs successfully and prints the converted string.
    - Creating and Importing Go Packages
        - Declaring and Defining Packages
        - Single-Item Import
        - Grouped Imports
        - Dot Import
        - Alias Import
        - Anonymous Import
        - Understanding the init() Function
        - 
        - # **Introduction**
        - In the previous section, you completed a basic Go program, which included the following lines of code:
        - ```
package main
import "fmt"
``` Explain Code
        - How do we understand these two lines of code? How do we use the `package` and `import` statements effectively?
        - In this lab, you will learn how to create and import packages in Go. This will enable you to organize your code into reusable modules, making your Go projects more maintainable and scalable.
        - **Knowledge Points:**
            - Definition and declaration of a package
            - Understanding exported (public) and unexported (private) identifiers
            - Different forms of importing packages: single, grouped, dot, alias, and anonymous imports
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 84% completion rate. It has received a 84% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/B-ceJXZrkml3scvzp3N41QruhwxpRklb5TTpfK-Hgj26DtXVY0RYUpIpY9ESoUmhLeOHlEpYUBEsfkDMiW69-X1tBo2omsVkVepdILzgKAYzzk_-sUCWW5MPI1S3oFkM.webp)**Labby** 
        - 
        - # **Declaring and Defining Packages**
        - A **package** in Go is similar to modules in Python or libraries in C. It is a collection of source code files used to organize and reuse code. Every Go file must declare a package at the beginning of the file.
        - > **Note**: A Go program must have one and only one package named `main`, which serves as the entry point for execution. Without it, the program cannot generate an executable file.
        - **Key Points:**
            1. **Exported (Public) Identifiers:** Identifiers (variables, functions, types, etc.) that begin with an **uppercase letter** are accessible from other packages. Think of these as the public interface of your package.
            2. **Unexported (Private) Identifiers:** Identifiers that begin with a **lowercase letter** are only accessible within the same package. These are considered internal implementation details of the package.
            3. **Package Cohesion:** All files in the same folder must belong to the **same package**. This ensures that related code stays together.
            4. **Package Naming Conventions:** Package names should be lowercase, short, and descriptive, avoiding underscores or capital letters.
        - Let's create our own custom package:
            1. Create a folder named `propagandist` and a file `propagandist.go` inside it:
                - ```
mkdir ~/project/propagandist
touch ~/project/propagandist/propagandist.go
``` Explain Code
            2. Write the following code in `propagandist.go`:
                - ```
package propagandist

var Shout = "I Love LabEx" // Public variable
var secret = "I love the dress" // Private variable

func Hit() string {
    return "Don't hit me, please!"
}
``` Explain Code
                    - `Shout` is **public** because it starts with an uppercase letter. This means you can access it from other packages that import `propagandist`.
                    - `secret` is **private** because it starts with a lowercase letter. It can only be used within the `propagandist` package.
                    - `Hit` is a **public** function, accessible from other packages.
            3. Initialize a Go module for the package:
                - ```
cd ~/project/propagandist
go mod init propagandist
``` Explain Code
                - This command initializes a new Go module in the `propagandist` directory, which helps manage dependencies for the package.
        - ![](https://remnote-user-data.s3.amazonaws.com/nIY5roiNmqUz0j3wcLI3yJ03BOsZUF4PgfXE_HiLZ6N74KD_cKsgeRHsrI2b62JwAEOYcKJo2qQXxaBQBgmEgWCbQEZ6CgzN09IYUa1sXRD0Zo7vw0ibfuM9RF0CZzU2.webp)**Labby**
        - 
        - # **Single-Item Import**
        - To use the `propagandist` package, let's create a new Go program. This step will demonstrate how to import and use a single package in your Go code.
            1. Create a new Go file named `pacExercise.go` in the project folder:
                - `touch ~/project/pacExercise.go` Explain Code
            2. Initialize a Go module for the program:
                - ```
cd ~/project
go mod init pacExercise
``` Explain Code
            3. Update the `go.mod` file to include the local package dependency, run the following command in the terminal:
                - `echo "replace propagandist => ./propagandist" >> go.mod` Explain Code
                - **Important:** This command adds a `replace` directive to your `go.mod` file. This is crucial because it tells Go that the `propagandist` package should be sourced from the local directory `./propagandist` instead of attempting to download it from a remote repository. You should execute this command in your terminal, which will append the line `replace propagandist => ./propagandist` to your `go.mod` file. Don't directly write this line into the file manually.
            4. Write the following code in `pacExercise.go` to import and use the `propagandist` package:
                - ```
package main

import (
    "fmt"
    "propagandist"
)

func main() {
    fmt.Println(propagandist.Shout) // Access the public variable
}
``` Explain Code
                    - This code imports the `fmt` package for printing output and the `propagandist` package.
                    - It then accesses the public variable `Shout` from the `propagandist` package using `propagandist.Shout`.
            5. Run the program:
                - ```go
mod tidy
go run pacExercise.go
``` Explain Code
                - The `go mod tidy` command ensures that your `go.mod` file is updated with any new dependencies. The `go run pacExercise.go` command compiles and executes the program.
                - Expected Output:
                - `I Love LabEx` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/xr_AfeY5riPZng_pWL9skIrak4ZNkla3H4OsaZWglszi1SepoQ6nuUwCY2TuPCvKR6Bg0NUv2SBdKvdJwyJvBCEDn0ghQr8hV6X-A3wWqoQzBRgL5kmdqRncMW8omNyA.webp)**Labby**
        - 
        - # **Grouped Imports**
        - When importing multiple packages, you can use grouped imports for better readability and organization. This is a stylistic choice and doesn't change the functionality of your code.
            1. Modify `pacExercise.go` to use grouped imports:
                - ```
package main

import (
    "fmt"
    "propagandist"
)

func main() {
    fmt.Println(propagandist.Shout)
}
``` Explain Code
                - In the code snippet above, the packages `fmt` and `propagandist` are imported inside a single `import` block enclosed in parentheses. This makes it easier to read and manage multiple package imports. This is exactly the same as the previous example and shows how to use the grouped import syntax.
            2. Run the program to confirm it still works:
                - `go run pacExercise.go` Explain Code
                - The program should execute without errors and output the same result as before.
        - ![](https://remnote-user-data.s3.amazonaws.com/gF_Y9JECC-Th56RptE9iHGEI9iFrdWX_bQWyocZAsILbPflpMXAVI9CcrukxXwtraaXomeQjq1DV4WsMJDQF3mg2uSfzPdh61LryVLHERzxOwIglXR0zwW3-6L97XAml.webp)**Labby**
        - 
        - # **Dot Import**
        - Using a **dot import**, you can omit the package name prefix when calling its functions or variables. This is often discouraged in favor of explicit package names because it can lead to namespace conflicts and reduce readability. However, it's good to know what it is.
            1. Modify `pacExercise.go` to use a dot import for `fmt`:
                - ```
package main

import . "fmt"
import "propagandist"

func main() {
    Println(propagandist.Shout) // No `fmt.` prefix needed
}
``` Explain Code
            - Here, `import . "fmt"` means you can use functions and variables from the `fmt` package directly without the `fmt.` prefix.
            - For example, you use `Println` instead of `fmt.Println`.
            1. Run the program:
                - `go run pacExercise.go` Explain Code
                - Expected Output:
                - `I Love LabEx` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/VcXBZATKEJ5FTIJnSmDhLdO8dYfScRPWd3s03Bo9I56qM4iGVBFgd4mZo_BQPH5-zA8HteLq5-NAKPSMhFML57ttiH45sKN74jMg6TK5vSXXEhS3Fwmr0y3vVGF_Z66G.webp)**Labby**
        - 
        - # **Alias Import**
        - You can alias an imported package for clarity or to avoid conflicts when two packages have similar names. This is helpful for making your code more readable and managing namespace collisions.
            1. Modify `pacExercise.go` to alias `fmt` as `io`:
                - ```
package main

import io "fmt"
import "propagandist"

func main() {
    io.Println(propagandist.Shout) // Use the alias `io` instead of `fmt`
}
``` Explain Code
                    - `import io "fmt"` creates an alias `io` for the `fmt` package.
                    - Now, you use `io.Println` instead of `fmt.Println`.
            2. Run the program:
                - `go run pacExercise.go` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/iCLULw5DOAHwHD5ijV-qLuoa_fklhIXUjjCZMFz9zeIq6vdVnVQqUtlvOUcwSWLTiN9tgTK0teAzlEptIOUuioS6b7q_63PI6Q4B6UaPwY_FFKZ-H23if8I6g8Z8Ro5t.webp)**Labby**
        - 
        - # **Anonymous Import**
        - Anonymous imports are used to import a package for its side effects, such as running its `init()` function, without needing to directly reference any of its exported identifiers. This is useful for packages that register drivers or perform other initialization tasks.
            1. Modify `pacExercise.go` to include an anonymous import for `time`:
                - ```
package main

import (
    "fmt"
    "propagandist"
    _ "time" // Anonymous import
)

func main() {
    fmt.Println(propagandist.Shout)
}
``` Explain Code
                    - `import _ "time"` is an anonymous import. The underscore `_` is used as a blank identifier, telling the compiler that you are importing the package for its side effects and won't be referencing anything from it directly in your code.
                    - The `time` package's `init()` function will execute when this program runs. The `time` package does not have any particular side effects visible here, however, many packages use this to register database drivers, or configuration settings.
            2. Run the program:
                - `go run pacExercise.go` Explain Code
                - Expected Output:
                - `I Love LabEx` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/vDE3TsOUKpy6OytBt_hhnuBJlu8oQt39aBIgiGoejJoq-yYG3mJfot_UnCN6J16wFG_p7aVKXVliARL2767iIbpwzgXPT2rP9sIqWSiZMqX0-VxMF7LNEdfHTQhQfvhA.webp)**Labby** 
        - 
        - # **Understanding the** `**init()**` **Function**
        - The `init()` function is a special function in Go that plays a crucial role in package initialization. It's automatically executed by Go when a package is imported, before any other code in the `main` function runs. This section will explain the details of `init()` functions and how they work within Go's initialization process.
        - **Key Points About** `**init()**` **Functions:**
            1. **Definition and Purpose:**
                - An `init()` function has no parameters and no return values: `func init() {}`
                - It's used for package initialization tasks such as setting up initial states, registering drivers, or validating prerequisites.
            2. **Execution Order:**
                - Go guarantees that package initialization occurs only once, even if a package is imported multiple times.
                - The initialization follows a well-defined order:
                    1. Package level variables are initialized first
                    2. Then `init()` functions are executed
                    3. Finally, the `main()` function runs (only in the main package)
            3. **Multiple** `**init()**` **Functions:**
                - A single Go file can contain multiple `init()` functions
                - Multiple files in the same package can each have their own `init()` functions
                - All these `init()` functions will be executed, but the order within the same package is not guaranteed
            4. **Dependency Chain:**
                - When packages import other packages, Go ensures that the `init()` functions in dependencies are executed first
                - This creates a bottom-up initialization flow: deepest dependencies initialize first
        - Let's create a practical example to demonstrate how `init()` functions work:
            1. First, let's modify our `propagandist` package to include an `init()` function. Update `propagandist.go`:
                - ```
package propagandist

import "fmt"

var Shout = "I Love LabEx" // Public variable
var secret = "I love the dress" // Private variable
var initialized bool

func init() {
    fmt.Println("Initializing propagandist package...")
    initialized = true
}

func Hit() string {
    return "Don't hit me, please!"
}

func IsInitialized() bool {
    return initialized
}
``` Explain Code
            2. Now, let's create another file in the propagandist package to demonstrate multiple `init()` functions:
                - `touch ~/project/propagandist/second.go` Explain Code
                - Add the following content to the file:
                - ```
package propagandist

import "fmt"

func init() {
    fmt.Println("Second init function in propagandist package...")
}
``` Explain Code
            3. Create a new helper package to demonstrate initialization order:
                - ```
mkdir -p ~/project/helper
touch ~/project/helper/helper.go
``` Explain Code
                - Add the following content to the file:
                - ```
package helper

import "fmt"

var Message = "Helper package is ready"

func init() {
    fmt.Println("Initializing helper package...")
}

func GetMessage() string {
    return Message
}
``` Explain Code
            4. Add the module file for the helper package:
                - ```
cd ~/project/helper
go mod init helper
``` Explain Code
            5. Update your `pacExercise.go` to use both packages and demonstrate the initialization order:
                - ```
package main

import (
    "fmt"
    "helper"
    "propagandist"
)

func init() {
    fmt.Println("Initializing main package...")
}

func main() {
    fmt.Println("Main function is running")
    fmt.Println(propagandist.Shout)
    fmt.Println(helper.Message)
    fmt.Printf("Propagandist initialized: %v\n", propagandist.IsInitialized())
}
``` Explain Code
            6. Update the `go.mod` file in the main project to include the local helper package:
                - ```
cd ~/project
echo "replace helper => ./helper" >> go.mod
go mod tidy
``` Explain Code
            7. Run the program and observe the initialization order:
                - `go run pacExercise.go` Explain Code
                - Expected Output (the exact order of the two propagandist init functions might vary):
                - ```
Initializing helper package...
Initializing propagandist package...
Second init function in propagandist package...
Initializing main package...
Main function is running
I Love LabEx
Helper package is ready
Propagandist initialized: true
``` Explain Code
        - This output demonstrates the key aspects of Go's initialization process:
            1. Dependent packages are initialized before the packages that import them
            2. Within a single package, all `init()` functions will run (though their order is not guaranteed)
            3. The `main()` function runs only after all package initializations are complete
            4. Package-level variables are initialized before any `init()` functions run
        - This initialization sequence is an important consideration when designing Go packages, especially when managing dependencies or performing setup operations that must happen in a specific order.
        - ![](https://remnote-user-data.s3.amazonaws.com/SD-7EhdX8qH-sqBA0AZsgAENBqQpnZZLrcbtZULLVSwBqO9BpRVwmyULaZnC0LAFZO9UT1Jk0CDg4_Lej2jnnGjLRdNFqLXUMVUoEz0Zm9Dl9h0YFo0hOx-lNv_C0F1p.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned:
            1. How to create and define custom packages in Go, encapsulating reusable code.
            2. The difference between public (exported) and private (unexported) identifiers and how they impact accessibility.
            3. Various ways to import packages, each with its use case:
                - Single-item import: Importing one package at a time.
                - Grouped import: Importing multiple packages in a single block for better organization.
                - Dot import: Importing a package and using its identifiers directly without the package name prefix. (Use with caution)
                - Alias import: Renaming imported packages for better readability or to avoid naming conflicts.
                - Anonymous import: Importing a package solely for its side effects, such as initialization.
            4. The role of the `init()` function in packages and how anonymous imports can trigger its execution.
            5. The detailed workings of Go's initialization process, including:
                - How package-level variables are initialized before `init()` functions
                - The guaranteed execution order of `init()` functions across dependent packages
                - How multiple `init()` functions work within a package
                - The complete initialization flow from dependent packages to the main function
        - By completing this lab, you are now equipped to structure and manage Go projects using packages effectively. You can create reusable modules, control access to identifiers, better organize your code, and understand the initialization process, leading to more maintainable and scalable Go applications.
    - Build a Math Utility Package
        - Import and Use the mathutil Package
        - 
        - # **Introduction**
        - In this revised challenge, you will **use** an existing Go package (`challengeproject/mathutil`) that implements a `Square()` function. Your goal is to create a `main.go` file with basic placeholders for importing and calling `Square()`. After replacing the placeholder `TODO`s, running the program should print the squared result of a given integer (e.g., 25 if the integer is 5).
        - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 99% pass rate. It has received a 98% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/XTbJvMFo8vJPj5eVWrXxhsIOgSgFMeHLLZsAmqBfZp0pMfdnlGycBIT3MX-AMK7tYZqToP4kQ6bGmJCRM2c8O1vvGEQ8iQQQ354R6UzIM0VpL4GzJ8nffFuRGbQzA42K.png)**Labby** 
        - 
        - # **Import and Use the** `**mathutil**` **Package**
        - A complete `mathutil.go` already exists, providing a public `Square(x int) int` function. You only need to edit the placeholder `main.go` to:
            1. **Import** the `challengeproject/mathutil` package.
            2. **Call** the `Square()` function.
            3. **Print** the result.
        - ## **Tasks**
            1. Open `main.go` in the `~/project` directory.
            2. Replace the `TODO`s:
                - Add the grouped import for `"challengeproject/mathutil"`.
                - Call `mathutil.Square()` with your choice of integer (e.g., 5).
                - Use `fmt.Println()` to print the result.
        - ## **Requirements**
            - The `main.go` file must import `challengeproject/mathutil`.
            - The function call must be `mathutil.Square(5)` (can't be another integer).
            - Print the result to stdout.
        - ## **Examples**
        - When you **successfully complete** the challenge and run:
        - `go run main.go` Explain Code
        - You should see output similar to:
        - `25` Explain Code
        -  *(This example assumes you pass the integer 5 to*   `__Square()__`  *.)* 
        - ## **Hints**
            - Go uses the **module path** to locate the package. Make sure your import path matches the module name in `go.mod`.
            - The `Square()` function has been fully provided for you in `mathutil.go`.
        - ![](https://remnote-user-data.s3.amazonaws.com/BWoxiYLWDMUtFPZkOI9SSan-2NwUv8EbiiLJxn2ol5lKh8FRGzVmi1I1ZX0sSfdTbcjtOgq2O_AjeCopVomsKSKTrv8hDcYCa5wlXx77-489R1i-osjAYFN8oEU1ZYIo.png)**Labby** 
        - 
        - # **Summary**
        - This simplified challenge focuses on **importing** and **using** a pre-existing Go package function. By updating `main.go` with the correct imports and function calls, you will demonstrate your understanding of Go modules, imports, and function usage. After successful completion, you should see the correct squared result printed to your terminal.
    - Introduction to Go Variables
        - What is a Variable?
        - General Declaration Method
        - Batch Declaration Method
        - Default Initialization
        - Standard Initialization
        - Type Declaration by Inference
        - Variable Scope
        - Variable Lifetime
        - Constants
        - 
        - # **Introduction**
        - Why do we need variables in computer programming languages? This is an age-old question. Just as we can remember that the URL for the LabEx is `labex.io`, computer programs also need to remember some data for their use.
        - The purpose of variables is to represent a piece of data. In this section, we will explore how variables are used in the Go language.
        - **Knowledge Points:**
            - Variable declaration
            - Variable initialization
            - Variable usage
            - Variable lifetime
            - Constants
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 89% completion rate. It has received a 100% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/8pumjvZ4CF3c7leprbhtZApX5QcDivFeSN3_An2FsIFcRR7G0V5OJl4e63azPsR6Sz2z5r0j_HZCSjMn3YXbPJVw9newle2-wEd8Oybm_T7JN7QkLUvq8dA9xcDon4L7.png)**Labby** 
        - 
        - # **What is a Variable?**
        - What is a variable? In simple terms, a variable is a container used to store and save a piece of **mutable** data.
        - In compiled languages such as Go, the type of a variable is fixed.
        - ## **What Does it Mean for a Variable Type to be Fixed?**
        - It means that a variable can only hold one type of data. In other words, the items stored in the variable container are fixed.
        - If a variable is used to hold fruit, it should only hold fruit. Once the container has held fruit, it cannot be used to hold cookies. This is reflected in the code as a variable cannot be assigned with two different types of data.
        - ## **Variable Mutability**
        - As the name implies, a variable's value can change, as long as the change does not exceed the range allowed by its type.
        - The Go language has the following rules for variables:
            - The name **must** consist of letters, digits, and underscores.
            - The variable identifier cannot start with a digit.
            - The identifier cannot be a reserved keyword. [Check reserved keywords](https://golang.google.cn/ref/spec#Keywords)
            - Variable names are case-sensitive, but it is **not recommended** to use different capitalization to distinguish between two variables with the same name.
        - ![](https://remnote-user-data.s3.amazonaws.com/ma7kJrVP3bDkScQ-HI4QBOL1M2Y00t-796UqzeVcdIwRSUjzIPS6CPmW2tYNoHTzKUUCp2ZIk4-Bu-FkqxmhKRBs8YiZKp5Dp0lywd8AIfVbbQova8YKtIUMshQ7YwW6.png)**Labby** 
        - 
        - # **General Declaration Method**
        - In the Go language, the keyword used to declare variables in the general method is `var`.
        - The form of declaration is: `var identifier type`, which means:
        - `var variableName variableType.` Explain Code
        - What are the common variable types in Go?
        - --------------------- Portal ---------------------Keyword
            - int #Keyword
                - [Explanation](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Keyword/Keyword/Explanation.md)―Integer. The most common data type, taught in primary school mathematics.
            - string #Keyword
                - [Explanation](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Keyword/Keyword/Explanation.md)―String. A string of characters wrapped in double quotes, such as: "hello,world"
            - bool #Keyword
                - [Explanation](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Keyword/Keyword/Explanation.md)―Boolean. Represents true or false, with two possible values: true or false
        - Since variable types are not the focus of this section, only the three most common types are listed.
        - More types will be explained in the following courses.
        - ## **How do we declare a variable?**
        - Now let's declare an **integer** variable named `a`.
        - `var a int` Explain Code
        - How to remember it? You can silently say in your mind:
        - `Define a variable named `a`, which is of type int.` Explain Code
        - Unlike many traditional programming languages, the variable type used in Go is placed after the variable name.
        - This way of declaring variables makes the code easier to read from left to right and avoids the spiral reading logic of the C language. For more details, please refer to the [official documentation](https://go.dev/blog/declaration-syntax).
        - ## **What name should we give a variable?**
        - A good variable name should clearly indicate the meaning of the variable.
        - When naming variables, we need to pay attention to their expressiveness and avoid using abbreviations.
        - Here we will briefly introduce the basic method of variable naming: Camel Case Naming Convention.
        - Camel case naming convention uses mixed-case letters to represent a variable. The first word is in lowercase, and the first letter of each subsequent word is capitalized.
        - For example: `currentDate`. The first word, `current`, is in lowercase, and the second word, `Date`, starts with a capital letter.
        - In this way, a variable that represents the current date is easily understood.
        - This naming convention is generally used for important and commonly used variables, while temporary variables can be simplified as long as they do not cause duplication.
        - ![](https://remnote-user-data.s3.amazonaws.com/2SAD8ObD5Ly3hLBagrgLqKDqumyOgDLNbvhfKWtgiKZoaLJfCSUN4OtDszniSnj1yisShOhpE5DrvJsFxLbhwUlAb-5-4sxPmHm2yoj7D7URbnJegJRa3w8OaO_EQIO3.png)**Labby**
        - 
        - # **Batch Declaration Method**
        - Now let's declare three variables:
        - ```
var a int // Declare an integer variable named a
var b int // Declare an integer variable named b
var c int // Declare an integer variable named c
``` Explain Code
        - The observant students may have noticed that all three variables, `a, b, c`, are of type `int`.
        - In that case, we can use a **comma** to connect the variable names and reduce the amount of code.
        - `var a, b, c int // Declare three variables a, b, c as integers` Explain Code
        - But what if the three variables have different types?
        - ```
var a int    // Declare an integer variable named a
var b string // Declare a string variable named b
var c bool   // Declare a boolean variable named c
``` Explain Code
        - We seem to have encountered a similar situation when importing packages. Many packages with different names need to be imported together, so we can use a similar writing method:
        - ```
var (
    a int
    b string
    c bool
)
``` Explain Code
        - Note that this kind of declaration behavior similar to importing packages is generally used to define global variables.
        - ![](https://remnote-user-data.s3.amazonaws.com/vIKNthL0vaBsLT2jPjbrNsD3QQOEi88JSH69BVYTu0rMusNvU-CqkdlexIeCav8C2zWokfFobQjMSUhrcO4bvgnpygGUIeV9DYJlfJh-E5UUreeMQPT_ZAAasI16XKRZ.png)**Labby** 
        - 
        - # **Default Initialization**
        - In Go, all variables are given initial values when they are declared. Let's explore what the initial values of variables are!
        - Create a file named `varExercise.go` in the directory `~/project`.
        - `touch ~/project/varExercise.go` Explain Code
        - Write the following code to the file:
        - ```
package main

import "fmt"

func main() {
    var a int
    var b string
    var c bool
    fmt.Println(a)
    fmt.Println(b)
    fmt.Println(c)
}
``` Explain Code
        - You can try running it yourself and see if it matches the table below.
        - `go run varExercise.go` Explain Code
        - The types of initial values are summarized as follows:
        - --------------------- Portal ---------------------
            - int #Keyword
                - [Explanation](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Untitled/Keyword/Explanation.md)―Integer
                - [Initial Value](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Untitled/Keyword/Initial%20Value.md)―0
            - string #Keyword
                - [Explanation](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Untitled/Keyword/Explanation.md)―String
                - [Initial Value](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Untitled/Keyword/Initial%20Value.md)―""
            - bool #Keyword
                - [Explanation](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Untitled/Keyword/Explanation.md)―Boolean
                - [Initial Value](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Untitled/Keyword/Initial%20Value.md)―false
        - ![](https://remnote-user-data.s3.amazonaws.com/zdR_bAmDEU0Lh53pofTdmNUiVsuP2tA02uVwxHlhFfcmS0Clpet1Bnsjn_SdAcHQ5FOi4ffTynz4rS1awu2WQHmashS1JmGAyOx_UOKrmoBm9IK1zOR2ddwbXJHPAQuN.png)**Labby**
        - 
        - # **Standard Initialization**
        - Since the type of a variable can be determined by its initial value, can we change the default value or an already declared variable?
        - ```
var a int = 1
var b string = "labex"
var c bool = true

a = 233
b = "labex"
c = false
``` Explain Code
        - As shown above, we just need to add `=` after declaring the variable, followed by an initial value that is **compatible with the variable type**. If you want to change the value, just use the variable name followed by `=` and another value of the same type.
        - Modify the `varExercise.go` file:
        - ```
package main

import "fmt"

func main() {
    // Declare and initialize
    var a int = 1
    var b string = "labex"
    var c bool = true

    // Print the variables
    fmt.Println("Before modification:")
    fmt.Println(a)
    fmt.Println(b)
    fmt.Println(c)

    // Modify the variables
    a = 233
    b = "labex"
    c = false

    // Print the modified variables
    fmt.Println("After modification:")
    fmt.Println(a)
    fmt.Println(b)
    fmt.Println(c)
}
``` Explain Code
        - After running the code, the output is as follows:
        - ```
$ go run varExercise.go
Before modification:
1
labex
true
After modification:
233
labex
false
``` Explain Code
        - You can try running it yourself and modify the initial values.
        - We just mentioned that the initial value assigned to a variable must be of the same type as the variable declaration. What will happen if they are different?
        - For example, let's assign `"labex"` as the initial value to the `a` variable:
        - ```
package main

import "fmt"

func main() {
    var a int = "labex"
    fmt.Println(a)
}
``` Explain Code
        - Run the code:
        - ```
$ go run varExercise.go
# command-line-arguments
./varExercise.go:6:12: cannot use "labex" (type untyped string) as type int in assignment
``` Explain Code
        - As shown in the figure, we cannot assign a string type such as `"labex"` to a variable of type `int`. This is because Go is a strongly typed compiled language and cannot be compiled.
        - ![](https://remnote-user-data.s3.amazonaws.com/2dWc39CbRg289frI0QGdL0ZKbD0u2g6xhlx-y2d_wuL9rgOR2JDN6DK5Z8bq3yYhF0XAhlCCKRtoZWmCpqVabTuPQkDuxddjIluzfGWwq6AVhoJles_1Ej1xOncINhQe.png)**Labby**
        - 
        - # **Type Declaration by Inference**
        - Since Go can determine the type of a variable by its initial value, can we simplify the process of type declaration by eliminating the step of explicitly specifying the type?
        - ```
package main

import "fmt"

func main() {
    // var a int = 1
    var a = 1 // Type is inferred
    fmt.Println(a)
}
``` Explain Code
        - Now you don't even need to use the `var` keyword to define a variable.
        - This way of declaring and initializing a variable can also be combined with the batch declaration method:
        - ```
a, b, c := 0
// Declare variables a, b, c as integers and assign an initial value of 0
a, b, c := 0, "", true
// Declare variables a, b, c as integer, string, and boolean, respectively
``` Explain Code
        - Short declaration is very convenient, but be careful that `:=` is not an assignment operation. It is a way to declare variables and is unique to Go, used to declare and initialize local variables inside a function. The type of the variable will be automatically inferred based on the expression.
        - Sometimes we write the following code:
        - ```
func main() {
    a := 1
    println(a)
    a := 2
    println(a)
}
``` Explain Code
        - The compiler will tell you that there is an error in the code because the variable `a` has been redeclared. However, if it is written in the following way:
        - ```
func main() {
    a := 1
    if true {
        a := 2
        println(a) // Output: 2
    }
    println(a) // Output: 1
}
``` Explain Code
        - There is such an output because the `a` with a value of `1` above and the `a` with a value of `2` below are not in the same variable scope (within the same curly braces), so the compiler treats them as two different variables.
        - The compiler will not point out your mistake, but there will be unexpected output.
        - In Go, it is stipulated that:
        - Each statement outside a function must begin with a keyword (`var`, `func`, etc.).
        - Therefore, the short variable declaration can only be used to declare local variables, and cannot be used to declare global variables.
        - So what is a global variable and what is a local variable?
        - This involves the concept of variable lifetime, which will be explained in the next section.
        - ![](https://remnote-user-data.s3.amazonaws.com/mQUaQBJb4BGStLuutolObpQJxnmDr28pofXPiMNYkx0K9Q9fbtWF-oqTB_Owgo29OYLRc4zz-FzHGAVks14Lla3wIiO4fUguq3j0XDQBLwwUbPn0Km-kG2j8nsccjEGa.png)**Labby**
        - 
        - # **Variable Scope**
        - Variable scope refers to the range at which a variable in a program is effective, that is, how it can be used.
        - You must have noticed that if you declare a variable but do not use it, the code will not compile.
        - In other words, when Go is compiled, it checks whether each variable has been used, that is, whether it has been used within its scope.
        - We can simply divide variables into three types based on their declaration positions:
            - Variables defined within a function, called local variables
            - Variables defined outside a function, called global variables
            - Variables defined within a function definition, called formal parameters
        - ## **Local Variables**
        - In this section, most of the variables we define are local variables:
        - ```
package main

import "fmt"

func main() { // Function body
    var a int = 1 // Local variable
    fmt.Println(a)
}
``` Explain Code
        - Local variables are defined within the function body, such as `a` defined within the `main` function. The scope of variable `a` is limited to within the `main` function.
        - At the same time, if the variable is not used in the `main` function, the compiler will throw an error.
        - ## **Global Variables**
        - However, it is also possible to define a global variable.
        - ```
package main

import "fmt"

var a int = 1 // Global variable
func main() { // Function body
    fmt.Println(a)
}
``` Explain Code
        - Global variables are defined outside the function body, and their scope covers the entire program. Even if they are not called in any function, an error will not be reported by the compiler.
        - You can think about why global variables will not produce errors even if they are not called.
        - Answer
        - This is because the global variable may be called in another package.
        - Details about formal parameter variables will be explained in subsequent function-related courses.
        - ![](https://remnote-user-data.s3.amazonaws.com/Q-_an4OPbG2_fKkZcQM_35fhzltUm0lXfl_W1G3eJEyWRNInDWTMwI8IIyMwfJoRyxM1Bhx1qWSYpUUwbYlwZeUg8dPwsa6NlymRTc4UaziN33h7KGIEjizg4ehzWzjB.png)**Labby**
        - 
        - # **Variable Lifetime**
        - > Birds that fly away, hide the span. Scheming rabbits die, and hounds will stew. - Records of the Grand Historian
        - When a variable has completed its purpose, it should be destroyed to reduce memory usage.
            - Global variables: The lifetime of a global variable is consistent with the entire program runtime. When the program stops running, the global variable is cleared from memory.
            - Local variables: When there is no way to access a variable, its memory space will be reclaimed.
        - Such a design is the key to Go's high performance and efficient use of space.
        - During the lifetime of a variable, it cannot be redeclared.
        - You can write the following in `varExercise.go`:
        - ```
package main

import "fmt"

func main() {
    var a int = 1 // Local variable, lifetime is limited to the entire main function
    var a int = 2 // Redefinition
    fmt.Println(a)
}
``` Explain Code
        - After running the code:
        - `go run varExercise.go` Explain Code
        - You will see the following error message:
        - ```
./varExercise.go:7:9: a redeclared in this block
previous declaration at ./varExercise.go:6:9
``` Explain Code
        - The compiler tells us that `a` is defined again.
        - ![](https://remnote-user-data.s3.amazonaws.com/pFoT-cVfkU21WDa2bitFiL4_Y_jIBzpnbnwM3gySS7WfBdM7lJThe2Nrn4gpA1gye36kQNFwK7J1w_fPzOaNqjRVAdN08ApH15PhLofm7CMGc_7MEuVJRwWArpfW4rPN.png)**Labby**
        - 
        - # **Constants**
        - > Many things in life are like constants. We can perceive them but cannot change them.
        - If a variable will not change during the entire program runtime, then we should define it as a constant.
        - Constants are very similar to variables, and you can even think of them as variables with immutable values.
        - When declaring a constant, we only need to replace the `var` keyword with the `const` keyword.
        - `const Pi = 3.14159 // Using type inference initialization` Explain Code
        - Create a file named `constExercise.go` in the directory `~/project`.
        - `touch ~/project/constExercise.go` Explain Code
        - What will happen if we try to modify a constant?
        - ```
package main

import "fmt"

func main() {
    const Pi = 3.14159
    Pi = 2 // Error: cannot assign to Pi
    fmt.Println(Pi)
}
``` Explain Code
        - Run the code.
        - ```
$ go run constExercise.go
# command-line-arguments
./constExercise.go:7:8: cannot assign to Pi
``` Explain Code
        - The compiler tells us that the value of `Pi` cannot be reassigned.
        - When declaring a constant, we **must** provide an initial value.
        - And the initial value assigned to a constant must be fixed at compile time.
        - User-defined function return values are not considered fixed in Go.
        - ```
var a int = 1
// Value is fixed, declaration is valid.
const Pi = 3.14159
// The calculated value is also fixed, the declaration is valid.
const c = 1 / Pi
// Fixed return value from built-in function is valid.
const le = len("labex")
// The return value of the user-defined function is not fixed, the declaration is invalid.
const le = getLen("labby")
// `a` is a variable value that is not fixed, the declaration is invalid.
const k = a
``` Explain Code
        - Whether a constant declaration is valid can be summarized in the following table:
        - --------------------- Portal ---------------------Declaration Type
            - Fixed values and fixed value expressions #[[Declaration Type]] 
                - [Valid](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Declaration%20Type/Declaration%20Type/Valid.md)―Valid
            - Non-fixed values (variables) and their corresponding expressions #[[Declaration Type]] 
                - [Valid](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Declaration%20Type/Declaration%20Type/Valid.md)―Invalid
            - Built-in function (len()) receives a fixed value and fixed value expressions #[[Declaration Type]] 
                - [Valid](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Declaration%20Type/Declaration%20Type/Valid.md)―Valid
            - User-defined functions #[[Declaration Type]] 
                - [Valid](Golang%20-%2065%20skills%206%20courses%205%20projects/Quick%20Start%20with%20Golang%20-%2044%20labs/Introduction%20to%20Go%20Variables/Declaration%20Type/Declaration%20Type/Valid.md)―Invalid
        - ![](https://remnote-user-data.s3.amazonaws.com/WW2k7v3Wi4reK2oZWaZzuxpr0USy9wyV-_wC0mS3pKua28_4_k5QvRGs9ipNRHn9iC-GLjhqRYX1puOmNOOkK5_h-MgSyYQz_MJlQSM7zmUsxsQiEhqbWuIlDG1eLO6b.png)**Labby** 
        - 
        - # **Summary**
        - Let's review what we learned in this lab:
            - The ways to declare variables
            - The ways to initialize variables
            - The concept of variable lifetime
            - The use of constants and whether their declarations are valid
        - In this lab, we have reviewed the basic usage of variables in Go, demonstrated the ways to declare and use variables in different situations, and introduced constants.
    - Craft Book Inventory Variables
        - Craft Book Inventory Variables
    - Data Processing with Operators in Golang
        - Basic Form
        - Increment and Decrement Operators
        - Relational Operators
        - Logical Operators
        - Execution Order of Logical Operators
        - Assignment Operators
    - Calculate Product Discount Price
        - Calculate Product Discount Price
    - Numerical Types in Golang
        - Integers
        - Floating-Point Numbers
        - Boolean Types
        - Complex Numbers
        - Literal Value Syntax
    - Convert and Calculate Numeric Types
        - Convert and Calculate Numeric Types
    - Character Types in Golang
        - ASCII Encoding
        - Unicode Character Set
        - UTF-8 Encoding
        - byte and rune
        - Quiz
    - Decode Unicode Emojis
        - Decode Unicode Emojis
    - Go String Fundamentals
        - What is a String
        - Creating a String
        - Declaring a String
        - Getting the Length of a String
        - Accessing String Elements
        - Converting Strings and Integers
        - Concatenating Strings
        - Removing Leading and Trailing Spaces from a String
    - Process User Registration Strings
        - Process User Registration Strings
    - Go Constants Fundamentals
        - What Are Constants?
        - Declaring Constants
        - The iota Constant Generator
        - Quiz
    - Define Server Size Constants
        - Define Server Size Constants
    - If Branch Statement in Golang
        - if statement
        - if else statement
        - else if statement
        - Initialization Statement in the if Statement
    - Sort Tasks with Conditional Logic
        - Sort Tasks with Conditional Logic
    - Switch-Case Branch Statements in Golang
        - Basic Syntax
        - Multiple Values in a Branch
        - switch Statements with No Conditional Variable
        - fallthrough Statement
        - Initialization Statement in switch
    - Implement Weather Advice Switch
        - Implement the Weather Advice Function
    - For Loops in Golang
        - Characters in a String
        - For Loop Syntax
        - Using the For Loop
        - The "break" Keyword
        - The "continue" Keyword
    - Reverse String with Go Loop
        - Reverse String with Go Loop
    - Goto Statement Usage
        - Understanding the Syntax of goto
        - Replacing break with goto
        - Implementing a for Loop Using goto
        - Exiting Nested Loops with goto
    - Solve Nested Loop Complexity with Goto
        - Solve Nested Loop Complexity with Goto
    - Array Operations in Golang
        - Array Definition
        - Initialization List
        - Inferred Length Initialization
        - Initialization with Specified Indices
        - Array Traversal
        - Accessing Array Elements
        - Value Type of Arrays
    - Initialize Employee Names Array
        - Initialize Employee Names Array
    - Multidimensional Arrays in Golang
        - Definition of a Two-Dimensional Array
        - Initialization of a Two-Dimensional Array
        - Initialization of a Two-Dimensional Array Using an Initialization List
        - Initialization of a Two-Dimensional Array with Inferred Length
        - Initializing a Two-Dimensional Array with Specified Index Values
        - Traversing a Two-Dimensional Array
        - Practical Uses of Arrays
        - Upscaling a Two-Dimensional Array
    - Design a Student Grade Tracker
        - Design a Student Grade Tracker
    - Golang Slice Data Structures
        - What is a Slice
        - Define a Slice
        - A Slice is a Reference to an Array
        - Data Structure of a Slice
        - Operations on Slices: Add, Delete, Modify, and Search
        - Expanding Slices
        - Copying Slices
        - Traversing Slices
    - Slice Log Filter Challenge
        - Implement Slice Log Filter Function
    - Go Dictionary Fundamentals
        - Introduction to Dictionaries
        - Declaration of Maps
        - The Initial Value nil
        - Declaration with the make Keyword
        - Manually Initializing an Empty Map
        - Actually Initializing the Dictionary
        - Adding and Updating Dictionary Elements
        - Deleting Dictionary Elements
        - Searching for Dictionary Elements
        - Iterating Over Dictionaries
    - Manage Student Grades with Go Maps
        - Manage Student Grades with Go Maps
    - Sorting Go Dictionaries
        - Sorting Dictionaries
        - Sort by Key
        - Swapping Keys and Values in a Dictionary
        - Sort by Value
        - Sorted by sort.Slice
        - Little Test
        - Slices of Dictionaries
        - Dictionaries with Slices as Values
        - Reference Type Characteristics of Dictionaries
    - Sort Student Grades Dynamically
        - Sort Student Grades Dynamically
    - Channel Primitives in Golang
        - Overview of Channels
        - Channel Types and Declaration
        - Channel Initialization
        - Channel Operations
        - Channel Blocking
        - Unidirectional Channels
    - Build a Simple Channel Data Pipeline
        - Build a Simple Channel Data Pipeline
    - Structures in Golang
        - Definition of Structure
        - Instantiation using var
        - Initial Value of a Structure
        - Instantiation using new
        - Instantiation using :=
    - Design Student Struct in Go
        - Design Student Struct in Go
    - Functions in Golang
        - Creating and Running a Basic Program
        - Function Declaration
        - Using the init Function
        - Returning Multiple Values from a Function
        - Working with Variadic Parameters
    - Design Flexible Math Function
        - Design Flexible Math Function
    - Anonymous Functions in Golang
        - Understanding Anonymous Functions
        - Creating an Anonymous Function without Parameters
        - Using Parameters in Anonymous Functions
        - Returning Values from Anonymous Functions
        - Declaring and Calling Anonymous Functions Immediately
        - Using Anonymous Functions as Callback Functions
    - Design Flexible Math Transformations
        - Design Flexible Math Transformations
-  **What Day Is It Today? - **1 labs
-  **Development of Golang Caching Component - **1 labs
-  **Cache Request Execution Results - **1 labs
-  **Implement JSON Comment Interpreter - **1 labs
-  **Transparent Modification of HTTP Requests - **1 labs
