-  ^^^**Bash**^^^ ^^^^^short for "^^^^^^^^ *Bourne Again SHell* ^^^^^^^^"^^^^^ 
    - [Size]();-[H0]()
    - sh
    - shell
- ^^^^^is an^^^^^ [interactive](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Human%E2%80%93computer_interaction)^^^^^command interpreter and command programming language^^^^^ 
    - interactive command interpreter 
    - command programming language
- ^^^^^ developed for^^^^^ [UNIX](https://en.wikipedia.org/api/rest_v1/page/mobile-html/UNIX)^^^^^-like operating systems.^^^^^
    - unix
    - operating systems 
- ^^^^^Created in 1989^^^^^^[[8]](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Bash_%28Unix_shell%29#cite_note-BashBeta-8)^ ^^^^^by Brian Fox ^^^^^ 
- unix shell
- terminal 
- 
- ^^^^^As a^^^^^ [command-line interface](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Command-line_interface) ^^^^^(CLI), Bash operates within a terminal emulator, or^^^^^ [text window](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Terminal_emulator)^^^^^, where users input commands to execute various tasks. ^^^^^
- ^^^^^It also supports the execution of commands from files, known as^^^^^ [shell scripts](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Shell_script)^^^^^, facilitating^^^^^ [automation](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Automation)^^^^^. ^^^^^
- ^^^^^In keeping with Unix shell conventions, Bash incorporates a rich set of features. ^^^^^
- ^^^^^The^^^^^ [keywords](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Keyword_%28computer_programming%29)^^^^^,^^^^^ [syntax](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Syntax_%28programming_languages%29)^^^^^,^^^^^ [dynamically scoped](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Scope_%28computer_science%29#Dynamic_scoping) ^^^^^variables, and other basic features of the^^^^^ [language](https://en.wikipedia.org/api/rest_v1/page/mobile-html/Formal_language) ^^^^^are all copied from the Bourne shell, (^^^^^`^^^sh^^^(#f8f9fa)`^^^^^). ^^^^^ 
- 
- 
- #!/bin/bash - This is called a "shebang" line. It tells the system which interpreter should be used to run this script. In this case, we're specifying the Bash shell.
- echo 'Hello, World!' - This line uses the echo command to print the text "Hello, World!" to the screen.
- 
- `chmod` is the command to change file permissions
- `+x` means "add execute permission"
- `hello.sh` is the name of our file
- 
- labex.io courses
    - **Quick Start with Shell** 
        - Hello, Bash!
            - Bash (Bourne Again SHell) is the most common and widely used shell in Unix-like systems. 
            - Zsh (Z Shell) is an extended version of Bash with some improvements and features.
            - For the purposes of this lab, the differences won't affect our work, as our scripts will explicitly use Bash through the shebang line (`#!/bin/bash`).
            - `labex:project/ $` 
                - This indicates that you're logged in as the user `labex`, and your current directory is `~/project` (which is shorthand for `/home/labex/project`).
            - This lab will guide you through creating a simple shell script that prints the classic "Hello, World!" message. 
            - You will learn the fundamentals of shell programming using the Bash shell, 
            - 
            - `touch hello.sh` Explain Code
            - This command creates an empty file named `hello.sh` in your current directory. 
            - The `.sh` extension is commonly used for shell scripts, but it's not mandatory.
            - ![](https://remnote-user-data.s3.amazonaws.com/Q1yiPx0PdfdQTJUD8p8zZT5yMDj9gH1kiZgbKUY3OHH9487MlJnXVAMX5elAu1H882JGuyeS10ylKFsbD29OQBcps52fh60OOhU3uBZXyIdAZhAs0Sysj-bAiFXU08II.png)
            - In the editor, type the following two lines exactly as shown:
            - ```
#!/bin/bash
echo 'Hello, World!'
``` Explain Code
            - Let's break down what these lines mean:
                1. `#!/bin/bash` - This is called a "shebang" line. It tells the system which interpreter should be used to run this script. In this case, we're specifying the Bash shell.
                2. `echo 'Hello, World!'` - This line uses the `echo` command to print the text "Hello, World!" to the screen.
            - 
            - # **Make the Script Executable**
                - [Size]();-[H1]()
            - Before we can run our script, we need to make it executable. In Unix-like systems, files have permissions that control who can read, write, or execute them. By default, new files are not executable.
            - To make our script executable, we use the `chmod` command (which stands for "change mode"). Type the following command in the terminal and press Enter:
            - `chmod +x hello.sh` Explain Code
            - Here's what this command does:
                - `chmod` is the command to change file permissions
                - `+x` means "add execute permission"
                - `hello.sh` is the name of our file
            - You won't see any output from this command if it's successful.
            - ![](https://remnote-user-data.s3.amazonaws.com/RTc7sgP4r4My86JRjPhAg74dxfIaiSfUf28TCZnIOnR2g54NqxdeiT5A-z6O2UjPc_DJwA70k700RYrPVTlnY0TFhv4NTPghaQD-ryDGYCStytNznFTvAZjLB9GRqMlL.png)**Labby** 
            - 
            - # **Execute the Script**
                - [Size]();-[H1]()
            - Now that our script is executable, we can run it. To run a script in the current directory, we use `./` before the script name. This `./` tells the system to look for the script in the current directory.
            - Type the following command in the terminal and press Enter:
            - `./hello.sh` Explain Code
            - If everything has been done correctly, you should see the output:
            - `Hello, World!` Explain Code
            - ![](https://remnote-user-data.s3.amazonaws.com/kDpOMtcymRJu7R3RxqMfIXk8ggJ4osFNhkw6ioz3HETCvMSs1ZiH5m9bY-Layaqb0QslM1ChFl7NRcZBZSMYuOYJZ7e8P1Pk4ctAlQht0g-lhtw4XCgoQwErgKTLSo0S.png)
            - Congratulations! You've just run your first shell script.
            - ![](https://remnote-user-data.s3.amazonaws.com/60sMZq3dTbBo8TABiI0GpDgcfJgqc3FiGl3NIMg7Vhv_uL3C9Qm19QqO-MuOSEVvOgDZ_mLKLqR5Fq6pVBM0mKykFSgATt098pNpqcciag_bVKkDZIh5dStAAJL8-wg_.png)**Labby** 
            - 
            - # **View the Script Contents**
                - [Size]();-[H1]()
            - As a final step, let's view the contents of our script file to confirm everything is correct. We can do this using the `cat` command, which displays the contents of a file in the terminal.
            - Type the following command in the terminal and press Enter:
            - `cat hello.sh` Explain Code
            - You should see the contents of your script displayed:
            - ```
#!/bin/bash
echo 'Hello, World!'
``` Explain Code
            - This is a good habit to get into when working with scripts – always double-check your work!
            - ![](https://remnote-user-data.s3.amazonaws.com/YsdL7_XhI6BiHNlCYH7skMsXX3R788Ez_PWZSGaYaza8cUYj-ic3smtYROTArLAP17ZPP5hO8VVMT4pk5Fp9bNG5_ogaFFM-4pvvWPAwsf_ivEgsiC3rr9SirxhZCUiY.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this lab, you have successfully created and executed a simple Bash shell script. You've learned how to:
                1. Navigate the WebIDE and use its integrated terminal
                2. Create a new script file using either the `touch` command or the WebIDE interface
                3. Edit a file using the WebIDE's built-in editor
                4. Understand the purpose of the shebang line in shell scripts
                5. Use the `echo` command to print text
                6. Make a script executable using the `chmod` command
                7. Run a shell script from the command line
                8. View the contents of a file using the `cat` command
            - These fundamental skills form the basis for more advanced shell scripting and automation tasks in Unix-like environments. As you continue to learn, you'll discover how powerful and flexible shell scripting can be for managing systems and automating tasks.
            - Remember, practice is key in programming. Try modifying the script to print different messages or create new scripts to perform other simple tasks. Don't be afraid to experiment – that's how you learn!
        - Working with Shell Variables
            - # **Create Shell Variables**
                - [Size]();-[H1]()
            - Shell variables are created by assigning a value to them using the `=` sign. Let's start by creating a simple shell script that defines some variables.
                1. Open a terminal in your WebIDE (VS Code).
                2. Create a new file named `variables.sh` in the `/home/labex/project` directory:
                    - `touch /home/labex/project/variables.sh` Explain Code
                3. Open the `variables.sh` file in the WebIDE and add the following content:
                    - ```
#!/bin/bash

PRICE_PER_APPLE=5
MyFirstLetters=ABC
greeting='Hello        world!'

echo "Price per apple: $PRICE_PER_APPLE"
echo "My first letters: $MyFirstLetters"
echo "Greeting: $greeting"
``` Explain Code
                    - In this script, we've created three variables:
                        - `PRICE_PER_APPLE`: An integer variable
                        - `MyFirstLetters`: A string variable
                        - `greeting`: A string variable with multiple spaces
                4. Save the file.
                5. Make the script executable:
                    - `chmod +x /home/labex/project/variables.sh` Explain Code
                6. Run the script:
                    - `./variables.sh` Explain Code
                    - You should see the following output:
                    - ```
Price per apple: 5
My first letters: ABC
Greeting: Hello        world!
``` Explain Code
                    - Notice that the extra spaces in the `greeting` variable are preserved in the output when using single quotes to define the variable and not using quotes in the echo statement.
            - ![](https://remnote-user-data.s3.amazonaws.com/1CrguFXhTy7YVcQ2jq9feLnnOD5d7oG5QU9tCQ-ldlYe2qxxbeAxOowj-FzB7622uu7AFMnQ7cxrbFeHarI9XdgXza5VslFlalEXEptkLYVjGTyk88SlOl9Zc5v27WBO.png)**Labby** 
            - 
            - # **Referencing Shell Variables**
                - [Size]();-[H1]()
            - When referencing shell variables, there are a few scenarios where you need to use special syntax. Let's explore these cases.
                1. Open the `variables.sh` file in the WebIDE.
                2. Replace the content of the file with the following:
                    - ```
#!/bin/bash

PRICE_PER_APPLE=5
MyFirstLetters=ABC
greeting='Hello        world!'

# Escaping special characters
echo "The price of an Apple today is: \$HK $PRICE_PER_APPLE"

# Avoiding ambiguity
echo "The first 10 letters in the alphabet are: ${MyFirstLetters}DEFGHIJ"

# Preserving whitespace
echo $greeting
echo "$greeting"
``` Explain Code
                3. Save the file.
                4. Run the script:
                    - `./variables.sh` Explain Code
                    - You should see the following output:
                    - ```
The price of an Apple today is: $HK 5
The first 10 letters in the alphabet are: ABCDEFGHIJ
Hello world!
Hello        world!
``` Explain Code
                    - Note the differences:
                        - The `$` sign is escaped in the first line to print it literally.
                        - Curly braces `{}` are used to clearly define the variable name in the second line.
                        - The last two lines show the difference between using quotes and not using quotes when referencing a variable with whitespace.
            - ![](https://remnote-user-data.s3.amazonaws.com/CQV-xEUIbzbvnSemYm_55ryEaaJ-TQYFEW0dsxIv9MY3vJugRa0AdJqr84d-bPhd385L6Kutg53MijJL0-Gp300tBoHMKSdv6hURRprVsC_k42VrjS-_SYQPzBp4M3tD.png)**Labby** 
            - 
            - # **Command Substitution**
                - [Size]();-[H1]()
            - Command substitution allows you to use the output of a command as the value of a variable. This is done by enclosing the command with `$()` or backticks (``).
                1. Open the `variables.sh` file in the WebIDE.
                2. Add the following content to the end of the file:
                    - ```
# Command substitution
CURRENT_DATE=$(date +"%Y-%m-%d")
echo "Today's date is: $CURRENT_DATE"

FILES_IN_DIR=$(ls)
echo "Files in the current directory:"
echo "$FILES_IN_DIR"

UPTIME=$(uptime -p)
echo "System uptime: $UPTIME"
``` Explain Code
                3. Save the file.
                4. Run the script:
                    - `./variables.sh` Explain Code
                    - You should see output similar to this (the actual values will depend on your system):
                    - ```
Today's date is: 2023-08-16
Files in the current directory:
variables.sh
System uptime: up 2 hours, 15 minutes
``` Explain Code
                    - In this example:
                        - `$(date +"%Y-%m-%d")` runs the `date` command and captures its output.
                        - `$(ls)` runs the `ls` command and captures its output.
                        - `$(uptime -p)` runs the `uptime` command with the `-p` option and captures its output.
            - ![](https://remnote-user-data.s3.amazonaws.com/uf91fWIQnvzVoPkcLxcHzdR4D4_UAunbnfcfOIixXq51WJVlIrdRh9GoHbcYJCND8TPcU9rnVVbbiydED5lk7mMiicEo3tNwEbAv1SU2kljmyHNbBqnkJtdeVw0zNucX.png)**Labby** 
            - 
            - # **Arithmetic Operations**
                - [Size]();-[H1]()
            - Shell variables can also be used in arithmetic operations. Bash provides the `$((expression))` syntax for performing arithmetic.
                1. Create a new file named `arithmetic.sh` in the `/home/labex/project` directory:
                    - `touch /home/labex/project/arithmetic.sh` Explain Code
                2. Open the `arithmetic.sh` file in the WebIDE and add the following content:
                    - ```
#!/bin/bash

X=10
Y=5

# Addition
SUM=$((X + Y))
echo "Sum of $X and $Y is: $SUM"

# Subtraction
DIFF=$((X - Y))
echo "Difference between $X and $Y is: $DIFF"

# Multiplication
PRODUCT=$((X * Y))
echo "Product of $X and $Y is: $PRODUCT"

# Division
QUOTIENT=$((X / Y))
echo "Quotient of $X divided by $Y is: $QUOTIENT"

# Modulus (remainder)
REMAINDER=$((X % Y))
echo "Remainder of $X divided by $Y is: $REMAINDER"

# Increment
X=$((X + 1))
echo "After incrementing, X is now: $X"

# Decrement
Y=$((Y - 1))
echo "After decrementing, Y is now: $Y"
``` Explain Code
                3. Save the file.
                4. Make the script executable:
                    - `chmod +x /home/labex/project/arithmetic.sh` Explain Code
                5. Run the script:
                    - `./arithmetic.sh` Explain Code
                    - You should see the following output:
                    - ```
Sum of 10 and 5 is: 15
Difference between 10 and 5 is: 5
Product of 10 and 5 is: 50
Quotient of 10 divided by 5 is: 2
Remainder of 10 divided by 5 is: 0
After incrementing, X is now: 11
After decrementing, Y is now: 4
``` Explain Code
                    - This script demonstrates various arithmetic operations using shell variables.
            - ![](https://remnote-user-data.s3.amazonaws.com/wZ33oUSp1K9mB0kyr855NmVwMl0Hgr3b6XQILFIV7e_DqChjUCptzWrAvgW4XYQuSZ7DBxGBnDrOcFGLwUd3IVX7eQRGJ0SOmAewRusXymX8Tt9KVZbX-vWMnpcZUUmo.png)**Labby** 
            - 
            - # **Using Environment Variables**
                - [Size]();-[H1]()
            - Environment variables are a type of variable that is available to all processes running in the current shell session. Let's explore some common environment variables and how to create our own.
                1. Create a new file named `environment.sh` in the `/home/labex/project` directory:
                    - `touch /home/labex/project/environment.sh` Explain Code
                2. Open the `environment.sh` file in the WebIDE and add the following content:
                    - ```
#!/bin/bash

# Displaying some common environment variables
echo "Home directory: $HOME"
echo "Current user: $LOGNAME"
echo "Shell being used: $SHELL"
echo "Current PATH: $PATH"

# Creating a new environment variable
export MY_VARIABLE="Hello from my variable"

# Displaying the new variable
echo "My new variable: $MY_VARIABLE"

# Creating a child process to demonstrate variable scope
bash -c 'echo "MY_VARIABLE in child process: $MY_VARIABLE"'

# Removing the environment variable
unset MY_VARIABLE

# Verifying the variable is unset
echo "MY_VARIABLE after unsetting: $MY_VARIABLE"
``` Explain Code
                3. Save the file.
                4. Make the script executable:
                    - `chmod +x /home/labex/project/environment.sh` Explain Code
                5. Run the script:
                    - `./environment.sh` Explain Code
                    - You should see output similar to this (the actual values will depend on your system):
                    - ```
Home directory: /home/labex
Current user: labex
Shell being used: /bin/zsh
Current PATH: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
My new variable: Hello from my variable
MY_VARIABLE in child process: Hello from my variable
MY_VARIABLE after unsetting:
``` Explain Code
                    - This script demonstrates how to access existing environment variables, create new ones, and remove them.
            - ![](https://remnote-user-data.s3.amazonaws.com/bNvLe8QTfD5T585QQZeWhJoFnFRmG5vORyHwGnGKoKiwWgSalZJRc3kIjz53QTafZygt9fZhCsr9s6emqyjeJFWJKAlyRAuR24rtMqfT4K-3wf6zTthMqlVTLzoSb0EX.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this lab, you learned how to work with shell variables in Linux. You explored creating and referencing variables, using command substitution to assign command outputs to variables, performing arithmetic operations with variables, and working with environment variables. These skills form a crucial foundation for shell scripting and will be invaluable as you continue to work with Linux systems.
            - Key takeaways from this lab include:
                - Creating and referencing shell variables
                - Using special syntax for variable referencing in different scenarios
                - Utilizing command substitution to capture command outputs
                - Performing arithmetic operations with shell variables
                - Working with environment variables
            - As you continue your journey in Linux and shell scripting, remember that variables are powerful tools for storing and manipulating data. Practice using them in your scripts to make your code more flexible and reusable.
        - Finding the Pirate's Treasure
            - # **Decoding the Treasure Map**
                - [Size]();-[H1]()
            - The treasure map has been encoded into a shell script that needs to be completed. The script uses basic arithmetic operations to convert the initial coordinates into the final location. Your task is to fill in the missing values and calculations to reveal where the treasure is buried.
            - ## **Tasks**
                - [Size]();-[H2]()
            - Complete the `treasure_map.sh` script in the `/home/labex/project` directory by:
                - Assigning the correct initial values to the `LATITUDE` and `LONGITUDE` variables.
                - Implementing arithmetic operations to calculate `PACES_NORTH` and `PACES_EAST`.
            - ## **Requirements**
                1. The shell script `treasure_map.sh` is located in `/home/labex/project` with the following code structure:
                - [Size]();-[H2]()
            - ```
#!/bin/bash

# Assign the correct values to these variables
LATITUDE=
LONGITUDE=

# Calculate the paces using arithmetic operations
PACES_NORTH=
PACES_EAST=

# Don't modify the line below
echo "The treasure is buried $PACES_NORTH paces north and $PACES_EAST paces east from the old oak tree."
``` Explain Code
                1. Use these values and calculations:
                    - Set `LATITUDE` to `15`.
                    - Set `LONGITUDE` to `25`.
                    - Calculate `PACES_NORTH` as latitude multiplied by 2.
                    - Calculate `PACES_EAST` as longitude divided by 5.
                2. The script will output the treasure location in this format:
            - `The treasure is buried X paces north and Y paces east from the old oak tree.` Explain Code
            - Where X and Y are the calculated values.
            - ## **Example Output**
                - [Size]();-[H2]()
            - `The treasure is buried 30 paces north and 5 paces east from the old oak tree.` Explain Code
            - ## **Hints**
                - Make sure the script is executable by using `chmod +x`.
                - [Size]();-[H2]()
            - ![](https://remnote-user-data.s3.amazonaws.com/PymJCTz9syE_W_GCzSxu0iFI7Y9e0MMRE6Oj5WCn0GglJC7YGtmQirU2gdGcOgYe-S8gNpBZh_gweg9gcSY2-IghaD5o6APZkKEKrboT6T10eDv7lzqbpn-SObtDNBEH.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this challenge, you have learned the fundamentals of shell scripting:
                - Assigning values to variables.
                - Performing arithmetic operations in shell scripts.
                - Executing scripts and formatting output.
            - These skills are foundational for more complex shell scripting tasks.
        - Passing Arguments to the Script
            - # **Introduction**
                - [Size]();-[H1]()
            - In Shell programming, the ability to pass arguments to a script is a fundamental and powerful feature. It allows scripts to be more flexible and reusable by accepting input from the command line. This lab will guide you through the process of creating a Shell script that can accept and use command-line arguments. You will learn how to access these arguments within your script, handle multiple arguments, and use special variables to process them efficiently.
            - ![](https://remnote-user-data.s3.amazonaws.com/lQMnQr_f44K1Bw_De0tYmv6PKIYCmuQ-sCBlZIP3ZNWuCk9z3WJVjuDmI_V80IC-ECZKoDP9-n_28P2FDnDJao3-ydHxHXV8uuMibjgBi87hPMgOMKOm7v3AOIMn9rWd.png)**Labby** 
            - 
            - # **Create a new script file**
                - [Size]();-[H1]()
            - Let's start by creating a new script file. We'll use the WebIDE (VS Code) for this lab.
                1. Open the WebIDE if it's not already open.
                2. In the file explorer on the left, navigate to the `/home/labex/project` directory.
                3. Right-click in the file explorer and select "New File".
                4. Name the new file `arguments.sh`.
            - Now that we have created the file, let's add the basic structure of our script:
            - ```
#!/bin/bash

# Your code will go here
``` Explain Code
            - The first line is called the "shebang" or "hashbang". It tells the system which interpreter to use to execute the script. In this case, we're using bash.
            - For beginners: The shebang line is important because it allows you to run the script directly (like `./arguments.sh`) instead of having to type `bash arguments.sh` every time. It's a small detail, but it makes your scripts more convenient to use.
            - ![](https://remnote-user-data.s3.amazonaws.com/ZqVQqJkkmUTqrwnG8snbmr4bj0YiPmggP4hmI9O3RUgFxxzNy6DuTqchSsYLd3UXIOZ1_K29bgS2nQRSWGlmn3NnkeB4ZpDFHEJ2dMCTP0v-F8BrLr02B1kag4pbgfl1.png)**Labby** 
            - 
            - # **Access script arguments**
                - [Size]();-[H1]()
            - Now, let's modify our script to access and display the arguments passed to it. In Shell scripting, special variables are used to access command-line arguments:
                - `$0` represents the name of the script itself
                - `$1`, `$2`, `$3`, etc., represent the first, second, third arguments, and so on
            - Add the following code to your `arguments.sh` file:
            - ```
#!/bin/bash

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: $3"
``` Explain Code
            - This script will display the script name and the first three arguments passed to it.
            - For beginners:
                - The `$` symbol is used to reference variables in bash.
                - `$0`, `$1`, `$2`, etc., are special variables that bash automatically sets for you when you run a script with arguments.
                - If you run the script without any arguments, `$1`, `$2`, and `$3` will be empty, but the script will still run without errors.
            - ![](https://remnote-user-data.s3.amazonaws.com/Lm-1aBXtG9BlxKt3V3Lefq-Ui_5D4dL3m4f4htxhTgyFjremsWieQ5h_2yKC083xm7hIPptk_qb4GCPz80wnHO_ri558RFIE145tFLq6FY_oVNCZnCSaU2v2mJz0awj-.png)**Labby** 
            - 
            - # **Make the script executable**
                - [Size]();-[H1]()
            - Before we can run our script, we need to make it executable. This is done using the `chmod` command. In the terminal, navigate to the project directory and run the following command:
            - ```
cd /home/labex/project
chmod +x arguments.sh
``` Explain Code
            - The `chmod +x` command adds execute permissions to the file, allowing it to be run as a script.
            - For beginners:
                - `chmod` stands for "change mode". It's used to change the permissions of a file or directory.
                - The `+x` option adds the execute permission. This is necessary for bash to be able to run the file as a script.
                - If you forget this step, you'll get a "permission denied" error when trying to run your script.
            - ![](https://remnote-user-data.s3.amazonaws.com/KZP0Fz-P7AaCoZnv6BWA7FAOXVBZO56sQcxJyOSxslMw1HCwTW-ACfjhlzXo4Ga1e2cQyc2OvYqMrrVrKtd7kmILR6FvWRAncWYpv-beeI-wI4Vw3XvkWTSUfHWORbXg.png)**Labby** 
            - 
            - # **Execute the script with arguments**
                - [Size]();-[H1]()
            - Now that our script is executable, let's run it with some arguments. In the terminal, execute the following command:
            - `./arguments.sh hello world example` Explain Code
            - You should see output similar to this:
            - ```
Script name: ./arguments.sh
First argument: hello
Second argument: world
Third argument: example
``` Explain Code
            - This output shows that our script successfully accessed and displayed the command-line arguments.
            - For beginners:
                - The `./` before the script name tells bash to look for the script in the current directory.
                - Each word after the script name becomes a separate argument. In this case, "hello" is the first argument, "world" is the second, and "example" is the third.
                - If you want to pass an argument with spaces, you need to use quotes, like this: `./arguments.sh "hello world" example`
            - ![](https://remnote-user-data.s3.amazonaws.com/A4OO2-3sNArDxWpXdryW8Apq6tnIzbe-yRc0oVUrOKMAXlqXBrmjXHpHmnrOlNZqTvZJI-KNNxNTEzigJblsqk3xwAqnXXL2HdAzzQ0oBHOqjaLLQzS9_cm1M4V3LKVb.png)**Labby** 
            - 
            - # **Handle the number of arguments**
                - [Size]();-[H1]()
            - Let's modify our script to handle different numbers of arguments. We'll use the `$#` special variable, which holds the number of arguments passed to the script.
            - Update your `arguments.sh` file with the following content:
            - ```
#!/bin/bash

if [ $# -eq 0 ]; then
  echo "No arguments provided."
elif [ $# -eq 1 ]; then
  echo "One argument provided: $1"
elif [ $# -eq 2 ]; then
  echo "Two arguments provided: $1 and $2"
else
  echo "More than two arguments provided:"
  echo "First argument: $1"
  echo "Second argument: $2"
  echo "Third argument: $3"
  echo "Total number of arguments: $#"
fi
``` Explain Code
            - This script uses conditional statements to handle different numbers of arguments.
            - For beginners:
                - `$#` is a special variable that contains the number of arguments passed to the script.
                - `[ $# -eq 0 ]` is a condition that checks if the number of arguments is equal to 0.
                - `elif` is short for "else if". It allows you to check multiple conditions in sequence.
                - The `-eq` operator means "equal to". There are other operators like `-lt` (less than), `-gt` (greater than), etc.
            - ![](https://remnote-user-data.s3.amazonaws.com/-1GlftKX-g0btGjHScQOitn1E5xRCm3SLd1bVVeIN_zMwcv04Y3ofG4zgbuo4jMtaeunUSHY4I-npwmnvidXrkmp_QWF12hXAIXfa0tuoSWAnP8pwFjJiVfl4Nq9FAQn.png)**Labby** 
            - 
            - # **Test the updated script**
                - [Size]();-[H1]()
            - Now, let's test our updated script with different numbers of arguments:
            - ```
./arguments.sh
./arguments.sh one
./arguments.sh one two
./arguments.sh one two three four
``` Explain Code
            - You should see different outputs based on the number of arguments provided.
            - For beginners:
                - Running the script without any arguments (`./arguments.sh`) will trigger the first condition in our script.
                - Each subsequent command adds more arguments, demonstrating how our script handles different cases.
                - Notice how the script's behavior changes based on the number of arguments. This kind of flexibility is very useful in real-world scripts.
            - ![](https://remnote-user-data.s3.amazonaws.com/NWq_bFPv8PqkIWn9YJcrE-WaHY7qPNzuLzb6isIrvr_OhLXMsRSPlzcz0AxU0olMuH_OEKTIOT00X2LI07Od6eY78hgIuua2r-YGFOL0z8APSzz2AK963pLkMSvkSY3_.png)**Labby** 
            - 
            - # **Loop through all arguments**
                - [Size]();-[H1]()
            - Finally, let's modify our script to loop through all provided arguments using the `$@` special variable, which represents all command-line arguments.
            - Update your `arguments.sh` file with the following content:
            - ```
#!/bin/bash

echo "Total number of arguments: $#"
echo "All arguments:"

count=1
for arg in "$@"; do
  echo "Argument $count: $arg"
  count=$((count + 1))
done
``` Explain Code
            - This script uses a `for` loop to iterate through all arguments and display them with their position.
            - For beginners:
                - `$@` is a special variable that contains all the arguments passed to the script.
                - The `for` loop is used to iterate over a list of items. In this case, it's iterating over all the arguments.
                - `$((count + 1))` is arithmetic expansion in bash. It's used to increment the count variable.
                - This script will work with any number of arguments, making it more flexible than our previous versions.
            - ![](https://remnote-user-data.s3.amazonaws.com/RlcYXjNaBkIIp3PRRvrDPPaUT3bgU3zSSJBE9dvkx9qotU8mQNuIwgMijVylO3dYXQHxRgi9kUgOOE_o-D9munIe0Dc3Kjj4wZi-ofdjDHw6j6QYI-dda3Qt2tR5ns2r.png)**Labby** 
            - 
            - # **Test the final script**
                - [Size]();-[H1]()
            - Let's test our final script with multiple arguments:
            - `./arguments.sh apple banana cherry date` Explain Code
            - You should see output similar to this:
            - ```
Total number of arguments: 4
All arguments:
Argument 1: apple
Argument 2: banana
Argument 3: cherry
Argument 4: date
``` Explain Code
            - This demonstrates that our script can now handle any number of arguments and display them all.
            - For beginners:
                - This final version of the script is much more flexible than our earlier versions.
                - It can handle any number of arguments, from zero to many.
                - The script now numbers each argument, which can be very useful in more complex scripts.
                - Try running the script with different numbers of arguments to see how it behaves.
            - ![](https://remnote-user-data.s3.amazonaws.com/WQQJkRejkZYT2DWkvKF42MohmHpwp3bzen5Nr3V8mFU4EkQ7zgFwemTt7VCSxskG3fGXQ1q8GEOSCxCwPs4M4WYm6d7DyyJ6BK-TNN1E5XNVBc75ckpv-n-EtNV8saGF.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this lab, you have learned how to create a Shell script that can accept and process command-line arguments. You've explored several key concepts:
                1. Creating and making a script executable
                2. Accessing individual arguments using special variables ($1, $2, etc.)
                3. Using the $# variable to determine the number of arguments
                4. Implementing conditional logic to handle different numbers of arguments
                5. Using the $@ variable to loop through all provided arguments
            - These skills are fundamental in Shell scripting and will allow you to create more flexible and powerful scripts that can adapt to different inputs. As you continue to develop your Shell scripting skills, you'll find that the ability to handle command-line arguments is crucial for creating versatile and reusable scripts for various tasks in system administration and automation.
        - Shell Arrays
            - # **Introduction**
                - [Size]();-[H1]()
            - In this lab, you will learn how to work with arrays in shell programming. Arrays are data structures that allow you to store multiple values under a single name, making it easier to organize and manipulate data. You will learn how to initialize arrays, add elements to them, access elements by their index, and determine the number of elements in an array. This knowledge is fundamental for more advanced shell scripting and data manipulation tasks.
            - ![](https://remnote-user-data.s3.amazonaws.com/Z9USG1SD6KG7H5zKCovQ_TmSaMuirmEJ8V3U2BDHUvaw5jtXGededfyOsYRH7_moo7w9nTegs_V1iXoA6F3G-5j7zMcuMXidH3mJN_NE-hAjIXx_CwfMOI26pNNXO1aa.png)**Labby** 
            - 
            - # **Create a new shell script file**
                - [Size]();-[H1]()
            - Let's start by creating a new shell script file where we'll write our array operations.
                1. Open your terminal in the WebIDE.
                2. Navigate to the project directory:
                    - `cd ~/project` Explain Code
                3. Create a new file named `arrays.sh` using the touch command:
                    - `touch arrays.sh` Explain Code
                4. Open the `arrays.sh` file in the WebIDE.
            - ![](https://remnote-user-data.s3.amazonaws.com/wv-LOTitj_Pw455tCqeNHEVH0K7IKSR4Ukzih88tCIHJtrvFOns3QtbX6HAPb41W_WiAsHY0gfA6BOSr4WVRXLgxyoyCOdn_e9rg4bYZHS8jCnve7Pkmq0EewGW9MYZY.png)**Labby** 
            - 
            - # **Initialize empty arrays**
                - [Size]();-[H1]()
            - Now that we have our script file, let's start by initializing three empty arrays.
            - Add the following code to your `arrays.sh` file:
            - ```
#!/bin/bash

# Initialize empty arrays
NUMBERS=()
STRINGS=()
NAMES=()
``` Explain Code
            - Let's break down what this code does:
                - The first line `#!/bin/bash` is called a shebang. It tells the system that this script should be executed by the Bash shell.
                - We're creating three empty arrays: `NUMBERS`, `STRINGS`, and `NAMES`.
                - The `()` syntax initializes an empty array.
            - ![](https://remnote-user-data.s3.amazonaws.com/G8bOOBz0OhFC06lgR0RZKRsDoFKhAOipVpp4_lAnhi8OYYftP1wgiO-OQUzFS-OLF1vz6tjMAxfURqn1GzcCjlB98fp6qqhQTM96bZGqvpR-fpSf8OPuOjYKNrbcQM4j.png)**Labby** 
            - 
            - # **Add elements to the arrays**
                - [Size]();-[H1]()
            - Now that we have our empty arrays, let's add some elements to them.
            - Add the following code to your `arrays.sh` file, below the array initializations:
            - ```
# Add elements to NUMBERS array
NUMBERS+=(1)
NUMBERS+=(2)
NUMBERS+=(3)

# Add elements to STRINGS array
STRINGS+=("hello")
STRINGS+=("world")

# Add elements to NAMES array
NAMES+=("John")
NAMES+=("Eric")
NAMES+=("Jessica")
``` Explain Code
            - Here's what this code does:
                - We use the `+=` operator to append elements to our arrays.
                - For `NUMBERS`, we're adding the integers 1, 2, and 3.
                - For `STRINGS`, we're adding the words "hello" and "world".
                - For `NAMES`, we're adding three names: "John", "Eric", and "Jessica".
                - Note that we enclose string elements in quotes, but numbers don't need quotes.
            - ![](https://remnote-user-data.s3.amazonaws.com/VTMbHI0Yfkja0dZrMZyRt79TshvAD0wil-9xDE0CSDSvNYAbl4upI92TR-j0vCdOhZrSW3plW346_zfor_cGC9OVbvUBmhk99Xm4otJ7PG93rcYXL9MXj6-h0V6liidP.png)**Labby** 
            - 
            - # **Determine the number of elements in an array**
                - [Size]();-[H1]()
            - One common operation with arrays is finding out how many elements they contain. Let's do this for our `NAMES` array.
            - Add the following code to your `arrays.sh` file:
            - ```
# Get the number of elements in the NAMES array
NumberOfNames=${#NAMES[@]}
``` Explain Code
            - This line does the following:
                - `${#NAMES[@]}` gives us the number of elements in the `NAMES` array.
                - We store this value in a variable called `NumberOfNames`.
                - The `@` symbol inside the brackets refers to all elements of the array.
                - The `#` symbol before `NAMES` tells the shell to count the elements.
            - ![](https://remnote-user-data.s3.amazonaws.com/_mVglPeeav85gtfpAyje8imKB0T60U3I-MZD7wu-OCkoP4Dpaf6ak7TOJklNWsJUpKgg7LoszriTORSXqqyyWkFfFGlyl75kxsJTjd-zZb6r_tNYb27HzzfChzTqpIrY.png)**Labby** 
            - 
            - # **Access a specific element in an array**
                - [Size]();-[H1]()
            - Now, let's access a specific element in our `NAMES` array. We'll get the second name.
            - Add this code to your `arrays.sh` file:
            - ```
# Access the second name in the NAMES array
second_name=${NAMES[1]}
``` Explain Code
            - Here's what this code does:
                - We're accessing the second element of the `NAMES` array with `${NAMES[1]}`.
                - Remember, array indices in Bash start at 0, so `[1]` gives us the second element.
                - We store this value in a variable called `second_name`.
            - ![](https://remnote-user-data.s3.amazonaws.com/vXJhhPexMNP36xXgdzyuol3gyO-HDAeaCYM2SiwGnXiyh7NcoQGN9FDCt-08o4WW3xUDiNEINLVvQh6vOOS5c0KNKKMAn_K7299Jqu-u5zh3Jzm7ZJArAh1iZqPkQHDe.png)**Labby** 
            - 
            - # **Print the arrays and variables**
                - [Size]();-[H1]()
            - Finally, let's add some code to print out our arrays and variables to see the results of our operations.
            - Add the following code to the end of your `arrays.sh` file:
            - ```
# Print the arrays and variables
echo "NUMBERS array: ${NUMBERS[@]}"
echo "STRINGS array: ${STRINGS[@]}"
echo "The number of names listed in the NAMES array: $NumberOfNames"
echo "The second name on the NAMES list is: $second_name"
``` Explain Code
            - This code does the following:
                - We use `echo` to print strings to the console.
                - `${NUMBERS[@]}` and `${STRINGS[@]}` print all elements of these arrays.
                - We print the `NumberOfNames` and `second_name` variables we created earlier.
            - ![](https://remnote-user-data.s3.amazonaws.com/lT5QHPwwwz5Uh-QAUCBb80WVQVbN15uXix9BbH2mdQ99d8dVKiTcZ8vMj-B8vDjSuzZU7A64I3aObPm3VHn5iAw0wW05t3lHafL19VpXEfk4yZ7Caw3zPx4g15Pvv2ir.png)**Labby** 
            - 
            - # **Run the script**
                - [Size]();-[H1]()
            - Now that we've written our script, it's time to run it and see the results.
                1. In your terminal, make sure you're in the correct directory:
                    - `cd ~/project` Explain Code
                2. Make the script executable:
                    - `chmod +x arrays.sh` Explain Code
                3. Run the script:
                    - `./arrays.sh` Explain Code
            - You should see output similar to this:
            - ```
NUMBERS array: 1 2 3
STRINGS array: hello world
The number of names listed in the NAMES array: 3
The second name on the NAMES list is: Eric
``` Explain Code
            - This output shows that our array operations were successful:
                - The `NUMBERS` array contains 1, 2, and 3.
                - The `STRINGS` array contains "hello" and "world".
                - We correctly counted 3 names in the `NAMES` array.
                - We successfully retrieved "Eric" as the second name.
            - ![](https://remnote-user-data.s3.amazonaws.com/onGgYqWmwn3O7atcGkx1wXFy6sT77j-CphcYYcxuGXaxaxY3354ikROmLtY7rS4eHaD4PzipbJBqiFu10ZU4rpmhjqu7wWsr-_WR5De184lK6qMnelG_InTnGsH3IU9P.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this lab, you've learned the fundamentals of working with arrays in shell scripting. You've practiced initializing arrays, adding elements to them, accessing specific elements, and determining the number of elements in an array. These skills are crucial for more advanced shell scripting tasks, especially when dealing with lists of data or when you need to perform operations on multiple items. Arrays provide a powerful way to organize and manipulate data in your shell scripts, making your code more efficient and easier to manage.
        - Interstellar Cargo Manifest
            - # **Introduction**
                - [Size]();-[H1]()
            - Welcome, space cadet! You're training to become a cargo officer on the interstellar ship "Nebula Nomad." Your first task is to create a simple inventory system for the ship's three cargo bays. You'll use shell arrays to store the inventory and accept a command-line argument to display the contents of a specific cargo bay.
            - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 94.77% pass rate.
            - ![](https://remnote-user-data.s3.amazonaws.com/kOhqDNJ-A1t-kR6aR8zo2e3wwipMgPCZV3Ar6V2-ogpWBOUm8QjqpOtsRS-M3Y-_o-rSl04vAgxBbqiHbcWxgm_xvycBYDEFoVfK08bBDUQEY7w06SJynBBPoghqWuwH.png)**Labby** 
            - 
            - # **Creating the Cargo Manifest Script**
                - [Size]();-[H1]()
            - ## **Tasks**
                1. Open the existing shell script named `cargo_manifest.sh` in the `/home/labex/project` directory.
                2. Complete the script by filling in the missing parts to create and display the ship's cargo inventory.
                3. Run the script with different arguments to display each cargo bay's inventory.
                - [Size]();-[H2]()
            - ## **Requirements**
                1. The script `cargo_manifest.sh` is already created in the `/home/labex/project` directory with a code framework.
                2. Complete the script by:
                    - Creating three arrays named `forward_bay`, `midship_bay`, and `aft_bay`.
                    - Each array should contain exactly 3 items (strings) representing cargo items.
                    - Use the `$1` variable to check which cargo bay inventory to display.
                    - Display the inventory of the requested cargo bay using `echo` statements.
                3. The script should accept one argument: either "forward", "midship", or "aft".
                4. If no argument is provided, the script should display: "Please specify a cargo bay: forward, midship, or aft"
                5. If an invalid argument is provided, the script should display: "Invalid cargo bay. Choose forward, midship, or aft."
                - [Size]();-[H2]()
            - ## **Example**
                - [Size]();-[H2]()
            - After completing the script, running it should produce output similar to this:
            - ```
$ ./cargo_manifest.sh forward
Forward Bay Inventory:
1. Space Suits
2. Oxygen Tanks
3. Repair Kits

$ ./cargo_manifest.sh midship
Midship Bay Inventory:
1. Food Supplies
2. Water Containers
3. Medical Equipment

$ ./cargo_manifest.sh aft
Aft Bay Inventory:
1. Spare Parts
2. Fuel Cells
3. Scientific Instruments

$ ./cargo_manifest.sh
Please specify a cargo bay: forward, midship, or aft

$ ./cargo_manifest.sh engine
Invalid cargo bay. Choose forward, midship, or aft.
``` Explain Code
            - The script's strings must reference the examples and remain unchanged to prevent test failures.
            - ![](https://remnote-user-data.s3.amazonaws.com/zmsbHQvO7WtTN7D_UDj3wdICPZmbjJf4Nhzwp5JQ9zxW6Yx5fI_pz93gy6bDtVYgHiOhuEm9m1ZCUBCNpI1a19ekBeIBY-pLr2Se_AYgiRqy0ce_tjbeYVkJjeSTqjJV.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this challenge, you've created a simple inventory management system using shell arrays and basic command-line argument handling. You've practiced defining arrays, accessing array elements, and using if statements to process command-line inputs. These fundamental skills are important for shell scripting and will help you in more advanced scripting tasks. Keep practicing, and you'll be ready to manage real interstellar cargo inventories in no time!
        - Arithmetic Operations in Shell
            - # **Introduction**
                - [Size]();-[H1]()
            - In this lab, you will learn how to perform basic arithmetic operations in Shell programming. You'll create a simple script to calculate the total cost of a fruit basket, demonstrating the use of variables and arithmetic expressions in Bash. This lab is designed for beginners, so we'll explain each step in detail.
            - ![](https://remnote-user-data.s3.amazonaws.com/3CCYBo74OA5UrarwQH-deR7GduODDJNM7KKM8FoKtbgILC98d6C0DSMZp3w5RurxXy01k7sCTOXNL0z_h5GKipTJa5HaE5_r_9vEq71-RL5kibDA-s2sovavBYrMBUBj.png)**Labby** 
            - 
            - # **Create a new Bash script**
                - [Size]();-[H1]()
            - Let's start by creating a new Bash script file.
                1. Open your terminal in the WebIDE. You should see a command prompt, which might look something like this: `labex@ubuntu:~/project$`.
                2. We'll create our script in the `project` directory. You're already in this directory by default, but let's make sure by using the `cd` command:
                    - `cd ~/project` Explain Code
                    - This command changes the current directory to `/home/labex/project`.
                3. Now, let's create a new file named `fruit_basket.sh`. We'll use the `touch` command, which creates an empty file:
                    - `touch fruit_basket.sh` Explain Code
                4. Open the `fruit_basket.sh` file in the WebIDE editor. You can do this by clicking on the file name in the file explorer on the left side of the WebIDE.
                5. Every Bash script should start with a "shebang" line. This line tells the system which interpreter to use to run the script. Add the following line at the beginning of the file:
                    - `#!/bin/bash` Explain Code
                    - This line specifies that the script should be run with the Bash interpreter.
            - ![](https://remnote-user-data.s3.amazonaws.com/UBUfH3TldXOLOsnL6BKYVy0PanagxMucWi3nCcYRp_M7wEKH6_WjhcN3bUGlb3edH2JXnUQ3tBqWphooF02roUb5vPb13GP8kYZV7F0vHyoCZcBkfSJHO4KWB7XiPAL8.png)**Labby** 
            - 
            - # **Define variables for fruit costs**
                - [Size]();-[H1]()
            - Now that we have our script file, let's define some variables to store the costs of different fruits and the basket.
            - Add the following lines to your `fruit_basket.sh` file:
            - ```
#!/bin/bash

# Define costs
COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1
``` Explain Code
            - Let's break this down:
                - In Bash, we don't need to declare variables before using them. We simply assign a value to a variable name.
                - Variable names are case-sensitive. By convention, we often use uppercase for constants (values that won't change).
                - There should be no spaces around the `=` sign when assigning values.
                - These values represent the cost in cents. For example, `COST_PINEAPPLE=50` means a pineapple costs 50 cents.
                - We don't need to specify a data type. Bash treats these as strings by default, but will handle them as numbers when we perform arithmetic operations.
            - ![](https://remnote-user-data.s3.amazonaws.com/ecuK5v-G5weN9ejEAi1FwaelTClz_MFF40XzPSa0GtOb-_GOx_ZYWZFLo3-VN7ryrsl_UrIdQDK5yxLUV4PTyudbCE9FgBeODX4h632nwMODp6GTEZp8BAZiljWg-_ZW.png)**Labby** 
            - 
            - # **Calculate the total cost**
                - [Size]();-[H1]()
            - Now that we have our costs defined, let's calculate the total cost of a fruit basket containing 1 pineapple, 2 bananas, and 3 watermelons.
            - Add the following line to your `fruit_basket.sh` file:
            - ```
#!/bin/bash

# Define costs
COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1

# Calculate total cost
TOTAL=$((COST_PINEAPPLE + (COST_BANANA * 2) + (COST_WATERMELON * 3) + COST_BASKET))
``` Explain Code
            - Let's examine this new line:
                - `$(( ))` is Bash's syntax for arithmetic operations. Anything inside these double parentheses is treated as an arithmetic expression.
                - Inside the arithmetic expression, we don't need to use `$` before variable names.
                - We're performing several operations:
                    - `COST_PINEAPPLE`: The cost of 1 pineapple
                    - `(COST_BANANA * 2)`: The cost of 2 bananas
                    - `(COST_WATERMELON * 3)`: The cost of 3 watermelons
                    - `COST_BASKET`: The cost of the basket itself
                - These values are all added together, and the result is stored in the `TOTAL` variable.
            - Note: Bash only handles integer arithmetic. If we were dealing with dollars and cents, we'd need to use a tool like `bc` for floating-point arithmetic.
            - ![](https://remnote-user-data.s3.amazonaws.com/SdFw-4JtAWskD4r_RFY6hoL13kcpDKclC6k09gK3VU14Vv58RyI0m_-5EXiZdV4XEVTMAYJW-XHAhSE-x95dPGj6MBNvremf6Oaj-gb8zwayY0e7QREpRxSMqHHiE4CJ.png)**Labby** 
            - 
            - # **Display the total cost**
                - [Size]();-[H1]()
            - To see the result of our calculation, we need to print the total cost. Add the following line to your `fruit_basket.sh` file:
            - ```
#!/bin/bash

# Define costs
COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1

# Calculate total cost
TOTAL=$((COST_PINEAPPLE + (COST_BANANA * 2) + (COST_WATERMELON * 3) + COST_BASKET))

# Display the total cost
echo "Total Cost is $TOTAL cents"
``` Explain Code
            - Let's break down this new line:
                - `echo` is a command that prints text to the terminal.
                - The text in quotes will be printed as-is, except for the `$TOTAL` part.
                - When a variable name is preceded by `$` inside a string, Bash replaces it with the variable's value. This is called variable expansion.
                - So if `TOTAL` is 128, the output will be "Total Cost is 128 cents".
            - ![](https://remnote-user-data.s3.amazonaws.com/QgfZYohTpDwqlemJWUa_KI6u7FT7E9TpdnkwPGkFKLJws0gH3czWzaj3VfTrc4QaHfw6hCkNG1mReOfZUNvaIjRFyBT_m0efkhoK_CHnSldIh9_sDsgDpyrtta-0d8fo.png)**Labby** 
            - 
            - # **Make the script executable and run it**
                - [Size]();-[H1]()
            - Now that our script is complete, we need to make it executable and then run it.
                1. In the terminal, make the script executable with the `chmod` command:
                    - `chmod +x ~/project/fruit_basket.sh` Explain Code
                    - This command changes the mode of the file, adding execute (`x`) permission for the user.
                2. Now, let's run the script:
                    - `~/project/fruit_basket.sh` Explain Code
                    - This command tells Bash to execute our script. The `~/project/` part specifies the path to our script.
            - You should see output similar to:
            - `Total Cost is 128 cents` Explain Code
            - This output shows that the total cost of our fruit basket (1 pineapple, 2 bananas, 3 watermelons, and the basket itself) is 128 cents.
            - ![](https://remnote-user-data.s3.amazonaws.com/o7WZSk1sOIPG884EwHBf4zi30ColoeyFyF2Bo8oIxLrKH6BMZ7EkyWlb-FT7FmkCtkNJiV3-zORBQL0vl1iliIQAYLw7OUj3QtmOGu1dZtMoFFSlMCAJgnOu7hoY8sZR.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this lab, you learned how to perform arithmetic operations using basic operators in Shell programming. You created a Bash script that calculates the total cost of a fruit basket by defining variables for individual costs and using arithmetic expressions to compute the total. You also learned how to make a script executable and run it from the command line.
            - Key points to remember:
                1. Bash scripts start with a shebang line (`#!/bin/bash`).
                2. Variables in Bash are assigned without spaces around the `=` sign.
                3. Arithmetic operations in Bash are performed inside `$(( ))`.
                4. The `echo` command is used to print output.
                5. Scripts need to be made executable with `chmod +x` before they can be run.
            - These skills form the foundation for more complex shell scripting tasks and can be applied to various scenarios where you need to perform calculations within your scripts.
        - Basic String Operations
            - # **Introduction**
                - [Size]();-[H1]()
            - In this lab, you will learn about fundamental string operations in shell scripting. String operations are essential for manipulating and extracting data from text in various scripting tasks. You will explore concepts such as determining string length, finding character positions, extracting substrings, and replacing parts of strings. These skills are crucial for effective text processing in shell scripts.
            - ## **Quick Reference Guide**
                - [Size]();-[H2]()
            - Here's a quick overview of the string operations we'll cover in this lab:
            - --------------------- Portal ---------------------Operation
                - String Length #Operation
                    - [Syntax](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Syntax.md)―${#string}
                    - [Description](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Description.md)―Calculates the number of characters in a string
                    - [Example](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Example.md)―${#"hello"} returns 5
                - Find Character Position #Operation
                    - [Syntax](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Syntax.md)―$(expr index "$string" "$char")
                    - [Description](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Description.md)―Finds the position of a character in a string (1-indexed)
                    - [Example](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Example.md)―$(expr index "abcdef" "c") returns 3
                - Extract Substring #Operation
                    - [Syntax](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Syntax.md)―${string:start:length}
                    - [Description](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Description.md)―Extracts a portion of a string (0-indexed)
                    - [Example](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Example.md)―${"hello":1:3} returns ell
                - Replace First Occurrence #Operation
                    - [Syntax](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Syntax.md)―${string/pattern/replacement}
                    - [Description](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Description.md)―Replaces the first occurrence of a pattern
                    - [Example](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Example.md)―${"hello"/l/L} returns heLlo
                - Replace All Occurrences #Operation
                    - [Syntax](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Syntax.md)―${string//pattern/replacement}
                    - [Description](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Description.md)―Replaces all occurrences of a pattern
                    - [Example](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Example.md)―${"hello"//l/L} returns heLLo
                - Replace at Beginning #Operation
                    - [Syntax](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Syntax.md)―${string/#pattern/replacement}
                    - [Description](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Description.md)―Replaces pattern only if at beginning of string
                    - [Example](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Example.md)―${"hello"/#he/HE} returns HEllo
                - Replace at End #Operation
                    - [Syntax](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Syntax.md)―${string/%pattern/replacement}
                    - [Description](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Description.md)―Replaces pattern only if at end of string
                    - [Example](bash/labex.io%20courses/Quick%20Start%20with%20Shell/Basic%20String%20Operations/Operation/Operation/Example.md)―${"hello"/%lo/LO} returns helLO
            - ![](https://remnote-user-data.s3.amazonaws.com/cOgoZGdnFJx-H7-irL4HgsxUL5wQZEnXJ0A583IlSKb_UV-302pzF4Ryi62s21mePE4Dhh5loQ8FYpMKcEZpiI-nqA3iJPBdUWwQsbQTJyjCKhpdbJhzXVfArviJwpvN.png)**Labby** 
            - 
            - # **Creating a Script File**
                - [Size]();-[H1]()
            - Let's start by creating a script file where we'll write our string operations.
                1. Open your terminal in the WebIDE. The terminal is where you'll type commands to interact with the Linux system.
                2. Navigate to the project directory:
                    - `cd ~/project` Explain Code
                    - This command changes your current directory to `~/project`. The `~` symbol represents your home directory, so `~/project` is a folder named "project" in your home directory.
                3. Create a new file named `string_operations.sh`:
                    - `touch string_operations.sh` Explain Code
                    - The `touch` command creates a new, empty file. If the file already exists, it updates the file's timestamp.
                4. Open the file in the WebIDE editor. You can do this by clicking on the file name in the file explorer on the left side of your WebIDE.
                5. Add the following shebang line at the top of the file to specify the interpreter:
                    - `#!/bin/bash` Explain Code
                    - This line, called a "shebang", tells the system to use the Bash shell to interpret this script. It's always the first line of a shell script.
            - ![](https://remnote-user-data.s3.amazonaws.com/CeYwpf2UkHMdXBbzy6giWQnu1bBwyCuS5KBN1LiE2zIQUY-Y2BofhHw8i4w0ORrqLd7TTKxecUsKew7z8dd3DzGkOGZQgpasADgGCQ2W4yH1bka79InMCQSHszDPlxe8.png)**Labby** 
            - 
            - # **String Length**
                - [Size]();-[H1]()
            - Now, let's learn how to determine the length of a string.
                1. Add the following code to your `string_operations.sh` file:
                    - ```
echo "Step 2: String Length"

STRING="Hello, World!"
LENGTH=${#STRING}

echo "The string is: $STRING"
echo "Its length is: $LENGTH"
``` Explain Code
                    - Let's break this down step by step:
                        - First, we add an echo command to display a header for this section.
                            - `echo "Step 2: String Length"` Explain Code
                        - Next, we define a variable called `STRING` and assign it the value "Hello, World!".
                            - `STRING="Hello, World!"` Explain Code
                            - In Bash, we don't need to use any special keywords to define variables. We simply write the variable name, followed by the equals sign, followed by the value.
                        - Then, we calculate the length of the string using the `${#variable}` syntax and store it in a variable called `LENGTH`.
                            - `LENGTH=${#STRING}` Explain Code
                            - The `${#variable}` is a special shell parameter expansion that returns the number of characters in the string stored in the variable.
                        - Finally, we display both the original string and its length.
                            - ```
echo "The string is: $STRING"
echo "Its length is: $LENGTH"
``` Explain Code
                            - The `$` symbol before a variable name tells Bash to replace it with the variable's value.
                2. Save the file. In most editors, you can do this by pressing Ctrl+S (or Cmd+S on Mac).
                3. Make the script executable:
                    - `chmod +x string_operations.sh` Explain Code
                    - This command changes the permissions of the file to make it executable:
                        - `chmod` stands for "change mode"
                        - `+x` means "add execute permission"
                        - Without this step, the system wouldn't know that this file should be treated as a program.
                4. Run the script:
                    - `./string_operations.sh` Explain Code
                    - The `./` prefix tells the shell to look for the script in the current directory. Without it, the shell would only look in directories listed in your PATH environment variable.
            - You should see output similar to:
            - ```
Step 2: String Length
The string is: Hello, World!
Its length is: 13
``` Explain Code
            - If you don't see this output, double-check that you've saved the file and made it executable.
            - ![](https://remnote-user-data.s3.amazonaws.com/e-Z0XN3FeFxCh-2ArQqxJmsMiwvcJM5ELQbFJPAQXDai6orI2BsPUY-16A16JLSc0dsRTGW0Z2sLioFSXc48J2gQ55LktmQU_FbdNCnx1b9LFewc6pdoG2wKHhuS8ZoF.png)**Labby** 
            - 
            - # **Finding Character Position**
                - [Size]();-[H1]()
            - Next, we'll learn how to find the position of a character in a string.
                1. Add the following code to your `string_operations.sh` file:
                    - ```
echo -e "\nStep 3: Finding Character Position"

STRING="abcdefghijklmnopqrstuvwxyz"
CHAR="j"

POSITION=$(expr index "$STRING" "$CHAR")

echo "The string is: $STRING"
echo "We're looking for the character: $CHAR"
echo "It is at position: $POSITION"
``` Explain Code
                    - Let's examine this code in detail:
                        - We start with an echo command that includes the `-e` option and a `\n` escape sequence.
                            - `echo -e "\nStep 3: Finding Character Position"` Explain Code
                                - The `-e` option enables interpretation of escape sequences.
                                - The `\n` escape sequence adds a newline before the text, creating a visual separation from the previous section.
                        - Next, we define two variables:
                            - ```
STRING="abcdefghijklmnopqrstuvwxyz"
CHAR="j"
``` Explain Code
                                - `STRING` contains the entire lowercase alphabet.
                                - `CHAR` contains the character "j" that we'll search for.
                        - We use the `expr index` command to find the position of the character:
                            - `POSITION=$(expr index "$STRING" "$CHAR")` Explain Code
                                - `expr` is a utility for evaluating expressions.
                                - The `index` operation searches for characters in a string.
                                - The `$()` syntax captures the output of the command and assigns it to the `POSITION` variable.
                                - We enclose the variables in double quotes (`"$STRING"`) to prevent issues with special characters.
                                - **Important**: This command returns positions starting from 1 (not 0).
                        - Finally, we print out the results:
                            - ```
echo "The string is: $STRING"
echo "We're looking for the character: $CHAR"
echo "It is at position: $POSITION"
``` Explain Code
                2. Save the file and run the script again:
                    - `./string_operations.sh` Explain Code
            - You should see additional output similar to:
            - ```
Step 3: Finding Character Position
The string is: abcdefghijklmnopqrstuvwxyz
We're looking for the character: j
It is at position: 10
``` Explain Code
            - Note that the position is 1-indexed, meaning the first character is at position 1, not 0. This is different from many programming languages where indexing typically starts at 0.
            - ![](https://remnote-user-data.s3.amazonaws.com/CblC_66jU04qQXFP64YzoW-NVQKtqXNaeZlm7bMkhnyTopS57rsT_nrcow7Z1g3fPceWBOiEu4zmdd0wT4nMyTG1jsCcd81iD8OrSTLOsnIV7p800cnk_mHO4nUaAR1C.png)**Labby** 
            - 
            - # **Substring Extraction**
                - [Size]();-[H1]()
            - Now, let's learn how to extract a portion of a string.
                1. Add the following code to your `string_operations.sh` file:
                    - ```
echo -e "\nStep 4: Substring Extraction"

STRING="The quick brown fox jumps over the lazy dog"
START=10
LENGTH=5

SUBSTRING=${STRING:$START:$LENGTH}

echo "The original string is: $STRING"
echo "Extracting 5 characters starting from position 10:"
echo "The substring is: $SUBSTRING"
``` Explain Code
                    - Let's analyze this code piece by piece:
                        - First, we add a header with a newline for visual separation:
                            - `echo -e "\nStep 4: Substring Extraction"` Explain Code
                        - Next, we define our variables:
                            - ```
STRING="The quick brown fox jumps over the lazy dog"
START=10
LENGTH=5
``` Explain Code
                                - `STRING` contains a sample sentence.
                                - `START` is the position where we want to start extracting (position 10).
                                - `LENGTH` is how many characters we want to extract (5 characters).
                        - We use Bash's substring extraction syntax to get a portion of the string:
                            - `SUBSTRING=${STRING:$START:$LENGTH}` Explain Code
                                - The syntax is `${variable:start_position:length}`
                                - `$START` and `$LENGTH` are variables containing the values 10 and 5.
                                - **Important**: Unlike the `expr index` command, the positions here are 0-indexed, meaning the first character is at position 0.
                        - Finally, we display the results:
                            - ```
echo "The original string is: $STRING"
echo "Extracting 5 characters starting from position 10:"
echo "The substring is: $SUBSTRING"
``` Explain Code
                2. Save the file and run the script again:
                    - `./string_operations.sh` Explain Code
            - You should see additional output similar to:
            - ```
Step 4: Substring Extraction
The original string is: The quick brown fox jumps over the lazy dog
Extracting 5 characters starting from position 10:
The substring is: brown
``` Explain Code
            - In the string "The quick brown fox...", position 10 (when counting from 0) is the 'b' in "brown", and the next 5 characters are "brown". This is why our extracted substring is "brown".
            - Keep in mind that the indexing is different from what we saw in the previous step:
                - In `expr index` (Step 3), positions start at 1 (first character is at position 1).
                - In substring extraction `${STRING:position:length}` (Step 4), positions start at 0 (first character is at position 0).
            - This is a common source of confusion in shell scripting, so it's important to remember which operations use which indexing system.
            - ![](https://remnote-user-data.s3.amazonaws.com/qXDQFoqVp_5iMnwRcjQZbgFUR0-gu6OzsRaCfIGAjSBdBELDqIvePC8CDPdj3nJXZSha9F7sow0FQzNo-2y_M6KrTArHsQvOyBS2H6lbSZgmA5nQj76a51JpjImyuY2Z.png)**Labby** 
            - 
            - # **String Replacement**
                - [Size]();-[H1]()
            - Finally, let's learn how to replace parts of a string.
                1. Add the following code to your `string_operations.sh` file:
                    - ```
echo -e "\nStep 5: String Replacement"

STRING="The quick brown fox jumps over the lazy dog"
echo "Original string: $STRING"

# Replace the first occurrence of 'o' with 'O'
NEW_STRING=${STRING/o/O}
echo "Replacing first 'o' with 'O': $NEW_STRING"

# Replace all occurrences of 'o' with 'O'
NEW_STRING=${STRING//o/O}
echo "Replacing all 'o' with 'O': $NEW_STRING"

# Replace 'The quick' with 'The slow' if it's at the beginning of the string
NEW_STRING=${STRING/#The quick/The slow}
echo "Replacing 'The quick' with 'The slow' at the beginning: $NEW_STRING"

# Replace 'dog' with 'cat' if it's at the end of the string
NEW_STRING=${STRING/%dog/cat}
echo "Replacing 'dog' with 'cat' at the end: $NEW_STRING"
``` Explain Code
                    - Let's go through each string replacement operation:
                        - First, we print a header and show the original string:
                            - ```
echo -e "\nStep 5: String Replacement"
STRING="The quick brown fox jumps over the lazy dog"
echo "Original string: $STRING"
``` Explain Code
                        - Replace the first occurrence of a character:
                            - ```
# Replace the first occurrence of 'o' with 'O'
NEW_STRING=${STRING/o/O}
echo "Replacing first 'o' with 'O': $NEW_STRING"
``` Explain Code
                                - The syntax is `${variable/pattern/replacement}`
                                - This will find the first occurrence of 'o' and replace it with 'O'
                                - Only the first 'o' in "brown" will be replaced, leaving the others unchanged.
                        - Replace all occurrences of a character:
                            - ```
# Replace all occurrences of 'o' with 'O'
NEW_STRING=${STRING//o/O}
echo "Replacing all 'o' with 'O': $NEW_STRING"
``` Explain Code
                                - The syntax is `${variable//pattern/replacement}` (note the double slash)
                                - The double slash tells Bash to replace ALL occurrences of the pattern
                                - All 'o's in the entire string will be replaced with 'O's.
                        - Replace a pattern at the beginning of a string:
                            - ```
# Replace 'The quick' with 'The slow' if it's at the beginning of the string
NEW_STRING=${STRING/#The quick/The slow}
echo "Replacing 'The quick' with 'The slow' at the beginning: $NEW_STRING"
``` Explain Code
                                - The syntax is `${variable/#pattern/replacement}`
                                - The `#` symbol specifies that the pattern must be at the beginning of the string
                                - This will only replace 'The quick' if it appears at the start of the string.
                        - Replace a pattern at the end of a string:
                            - ```
# Replace 'dog' with 'cat' if it's at the end of the string
NEW_STRING=${STRING/%dog/cat}
echo "Replacing 'dog' with 'cat' at the end: $NEW_STRING"
``` Explain Code
                                - The syntax is `${variable/%pattern/replacement}`
                                - The `%` symbol specifies that the pattern must be at the end of the string
                                - This will only replace 'dog' if it appears at the end of the string.
                2. Save the file and run the script again:
                    - `./string_operations.sh` Explain Code
            - You should see additional output similar to:
            - ```
Step 5: String Replacement
Original string: The quick brown fox jumps over the lazy dog
Replacing first 'o' with 'O': The quick brOwn fox jumps over the lazy dog
Replacing all 'o' with 'O': The quick brOwn fOx jumps Over the lazy dOg
Replacing 'The quick' with 'The slow' at the beginning: The slow brown fox jumps over the lazy dog
Replacing 'dog' with 'cat' at the end: The quick brown fox jumps over the lazy cat
``` Explain Code
            - These string replacement operations are powerful tools for manipulating text in shell scripts. They allow you to perform targeted replacements based on patterns and positions, which is especially useful for tasks like data processing, text formatting, or file content manipulation.
            - ![](https://remnote-user-data.s3.amazonaws.com/2Xn31vfC2WDcug5Pc7UDq1uq2-u6If-nifMxY0ll_VKhrvYxcsaKdAgKq2DhPDcIH3ZFzsTPCunvq603ZQ8tpil4UKE5Ny4rnYpr16aF6O6-IuQhal2u8F8mUT7bYnZl.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this lab, you have learned and practiced several fundamental string operations in shell scripting:
                1. Creating and executing a shell script.
                2. Calculating the length of a string using `${#string}`.
                3. Finding the position of a character in a string using `$(expr index "$string" "$char")`.
                4. Extracting a substring from a larger string using `${string:start:length}`.
                5. Performing various string replacement operations using:
                    - `${string/pattern/replacement}` - Replace first occurrence
                    - `${string//pattern/replacement}` - Replace all occurrences
                    - `${string/#pattern/replacement}` - Replace at beginning of string
                    - `${string/%pattern/replacement}` - Replace at end of string
            - These skills form the foundation for more complex text processing tasks in shell scripting. As you continue to work with shell scripts, you'll find these string operations invaluable for manipulating and analyzing text data in your projects. Remember, practice is key to mastering these concepts, so don't hesitate to experiment with different strings and operations!
        - Conditional Statements in Shell
            - # **Introduction**
                - [Size]();-[H1]()
            - In this lab, you will learn how to use conditional statements in shell programming to make logical decisions. We will cover the basic syntax of if-else statements, as well as how to use numeric and string comparisons to evaluate conditions. By the end of this lab, you will be able to write shell scripts that can make decisions based on various conditions.
            - ![](https://remnote-user-data.s3.amazonaws.com/wcFfNehOgDnMRa3P3R9AIEMG4t32_IZ8zpCIbIj9ShzcUVbXvAKc8rgwd__jvo7uwF1N6amiFJUijABu0rF0UD9PzSfCuDZ89bUO-Ab9jsOnDDbiuhUD4fwSrROtDll0.png)**Labby** 
            - 
            - # **Create Your First If Statement**
                - [Size]();-[H1]()
            - Let's start by creating a simple if statement that checks if a variable called `NAME` is equal to "John".
            - First, open a terminal in the WebIDE. You should be in the `/home/labex/project` directory by default. If you're not sure, you can always check your current directory with the `pwd` command.
            - Create a new file called `if.sh` using the following command:
            - `touch if.sh` Explain Code
            - This command creates an empty file named `if.sh` in your current directory.
            - Now, open the `if.sh` file in the WebIDE. You can do this by clicking on the file in the file explorer on the left side of the WebIDE.
            - Add the following content to the file:
            - ```
#!/bin/bash

NAME="John"
if [ "$NAME" = "John" ]; then
  echo "The name is John"
fi
``` Explain Code
            - Let's break down this script:
                1. `#!/bin/bash`: This is called a "shebang" line. It tells the system which interpreter to use to run the script. In this case, we're using Bash.
                2. `NAME="John"`: This line creates a variable called `NAME` and assigns it the value "John".
                3. `if [ "$NAME" = "John" ]; then`: This is the start of our if statement. It checks if the value of `NAME` is equal to "John".
                    - The square brackets `[ ]` are actually a command in Bash, equivalent to the `test` command.
                    - We put `"$NAME"` in quotes to handle cases where `NAME` might be empty or contain spaces.
                    - The semicolon and `then` are part of the if statement syntax in Bash.
                4. `echo "The name is John"`: This line will be executed if the condition is true.
                5. `fi`: This marks the end of the if statement. It's "if" spelled backwards!
            - Save the file after adding this content.
            - Now, we need to make the script executable. In Unix-like systems, files aren't executable by default for security reasons. We can change this using the `chmod` command:
            - `chmod +x if.sh` Explain Code
            - This command adds the execute permission to the file. The `+x` means "add execute permission".
            - Now, run the script:
            - `./if.sh` Explain Code
            - The `./` tells the shell to look for the script in the current directory.
            - You should see the output: `The name is John`
            - If you don't see this output, double-check that you've saved the file with the correct content and that you've made it executable.
            - ![](https://remnote-user-data.s3.amazonaws.com/5RRCb1zZjPtXdMlMGRgSpoXMQ8acWwqTS4rqeIvGyMZBPLFhkDR2BPR8zDz8HFA0oJi6LLqKrPX3_9Z1PsqHufmVblHuj5wWE6Q3WIrZkZWYoOpP_cwxl9wtUDMGnskz.png)**Labby** 
            - 
            - # **Add an Else Clause**
                - [Size]();-[H1]()
            - Now, let's expand our if statement to include an else clause. This allows us to specify what should happen when the condition is false.
            - Open the `if.sh` file in the WebIDE again and modify it as follows:
            - ```
#!/bin/bash

NAME="Alice"
if [ "$NAME" = "John" ]; then
  echo "The name is John"
else
  echo "The name is not John"
fi
``` Explain Code
            - Let's go through the changes:
                1. We've changed the `NAME` variable to "Alice". This is to demonstrate what happens when the condition is false.
                2. We've added an `else` clause. This clause specifies what should happen if the condition in the if statement is false.
                3. After the `else`, we've added another `echo` command that will run if `NAME` is not "John".
            - The `else` clause is optional in if statements, but it's very useful when you want to do something specific when the condition is false, rather than just doing nothing.
            - Save the file with these changes.
            - Now, run the script again:
            - `./if.sh` Explain Code
            - This time, you should see the output: `The name is not John`
            - This is because `NAME` is now "Alice", so the condition `[ "$NAME" = "John" ]` is false, and the code in the `else` block is executed.
            - Try changing the `NAME` variable back to "John" and run the script again. What output do you get? This is a good way to test that your if-else statement is working correctly for both cases.
            - ![](https://remnote-user-data.s3.amazonaws.com/frnSmjkan0GckGAs43oXuO2tfaVbL_wzHIsi87zdQs4Np2w7l9VBSvVYo58BdQhHPEf9ome8KGWbnb9mwAJx5OwjCmbGCeU9TjqGO4vAddxmr-rkHd65H-0MKq5g6kNV.png)**Labby** 
            - 
            - # **Introducing Elif**
                - [Size]();-[H1]()
            - Sometimes, we want to check multiple conditions. This is where the `elif` (else if) clause comes in handy. Let's modify our script to handle multiple names.
            - Update the `if.sh` file with the following content:
            - ```
#!/bin/bash

NAME="George"
if [ "$NAME" = "John" ]; then
  echo "John Lennon"
elif [ "$NAME" = "Paul" ]; then
  echo "Paul McCartney"
elif [ "$NAME" = "George" ]; then
  echo "George Harrison"
elif [ "$NAME" = "Ringo" ]; then
  echo "Ringo Starr"
else
  echo "Unknown member"
fi
``` Explain Code
            - Let's break down this script:
                1. We start with `NAME="George"`. This will be the name we're checking.
                2. The first `if` statement checks if the name is "John".
                3. If it's not "John", we move to the first `elif` (else if) statement, which checks if the name is "Paul".
                4. If it's not "Paul", we move to the next `elif`, checking for "George".
                5. If it's not "George", we check for "Ringo".
                6. If none of these conditions are true, we fall through to the `else` clause, which will echo "Unknown member".
            - The `elif` clause allows you to check multiple conditions in sequence. You can have as many `elif` clauses as you need. The conditions are checked in order, and the first one that's true will have its corresponding code block executed.
            - Save the file with these changes.
            - Now, run the script:
            - `./if.sh` Explain Code
            - You should see the output: `George Harrison`
            - Try changing the `NAME` variable to different values ("John", "Paul", "Ringo", or something else entirely) and run the script each time. Observe how the output changes based on the value of `NAME`.
            - ![](https://remnote-user-data.s3.amazonaws.com/RXXR1w_f_x_I0ZbecZMbF9tLr3m58fDblUh4mHfxFbYdK3uYVfSSlL0XccTEuWtOnfwXuY3EhAfIoPfIgrTG8r0BkdesJBCGAVA6txVJ5PQWM1Usd3Z5XBrsOsaBYDvc.png)**Labby** 
            - 
            - # **Numeric Comparisons**
                - [Size]();-[H1]()
            - Shell scripts can also compare numbers. Let's create a new script to demonstrate numeric comparisons.
            - Create a new file called `numeric.sh`:
            - `touch numeric.sh` Explain Code
            - Open `numeric.sh` in the WebIDE and add the following content:
            - ```
#!/bin/bash

NUMBER=10

if [ $NUMBER -lt 5 ]; then
  echo "The number is less than 5"
elif [ $NUMBER -eq 10 ]; then
  echo "The number is exactly 10"
elif [ $NUMBER -gt 15 ]; then
  echo "The number is greater than 15"
else
  echo "The number is between 5 and 15, but not 10"
fi
``` Explain Code
            - This script introduces numeric comparison operators:
                - `-lt`: less than
                - `-eq`: equal to
                - `-gt`: greater than
            - There are also others you can use:
                - `-le`: less than or equal to
                - `-ge`: greater than or equal to
                - `-ne`: not equal to
            - Notice that we use these special operators instead of symbols like `<` or `>`. This is because in Bash, `<` and `>` are used for input/output redirection, not for numeric comparison.
            - Now, let's make the script executable and run it:
            - ```
chmod +x numeric.sh
./numeric.sh
``` Explain Code
            - You should see the output: `The number is exactly 10`
            - Try changing the `NUMBER` variable to different values and run the script again. See how the output changes based on the value you set.
            - For example, if you change `NUMBER` to 20, you should get "The number is greater than 15". If you change it to 7, you should get "The number is between 5 and 15, but not 10".
            - ![](https://remnote-user-data.s3.amazonaws.com/dMdZCxaQLm3_UehJu4U_rUku0-hbzLb3yWqiZa_OmPwspdfOpx697uYIK6E5yKlph7if8TYJgzgiZKZCf-Fe3y5uwvJk9nrBOJBk2fHOwZchzJVBPcv4HKVJBCVDr3Ky.png)**Labby** 
            - 
            - # **String Comparisons and Logical Operators**
                - [Size]();-[H1]()
            - Lastly, let's explore string comparisons and logical operators. Create a new file called `string_logic.sh`:
            - `touch string_logic.sh` Explain Code
            - Open `string_logic.sh` in the WebIDE and add the following content:
            - ```
#!/bin/bash

STRING1="hello"
STRING2="world"
NUMBER1=5
NUMBER2=10

if [ "$STRING1" = "hello" ] && [ "$STRING2" = "world" ]; then
  echo "Both strings match"
fi

if [ $NUMBER1 -lt 10 ] || [ $NUMBER2 -gt 5 ]; then
  echo "At least one of the number conditions is true"
fi

if [[ "$STRING1" != "$STRING2" ]]; then
  echo "The strings are different"
fi

if [[ -z "$STRING3" ]]; then
  echo "STRING3 is empty or not set"
fi
``` Explain Code
            - This script demonstrates several new concepts:
                1. String equality comparison (`=`): This checks if two strings are exactly the same.
                2. Logical AND (`&&`): This operator allows you to combine two conditions. Both conditions must be true for the overall expression to be true.
                3. Logical OR (`||`): This operator also combines two conditions, but only one needs to be true for the overall expression to be true.
                4. String inequality comparison (`!=`): This checks if two strings are different.
                5. Checking if a string is empty (`-z`): This is true if the string is empty (has zero length).
            - Also, notice the use of double square brackets `[[ ]]` in some of the if statements. These are an enhanced version of the single square brackets and are preferred in Bash scripts when possible. They allow for more complex expressions and have fewer surprises with regard to word splitting and pathname expansion.
            - Make the script executable and run it:
            - ```
chmod +x string_logic.sh
./string_logic.sh
``` Explain Code
            - You should see all four echo statements printed, because all the conditions in the script are true.
            - ```
Both strings match
At least one of the number conditions is true
The strings are different
STRING3 is empty or not se
``` Explain Code
            - Try changing some of the values (like setting `STRING1` to something other than "hello") and see how it affects the output.
            - ![](https://remnote-user-data.s3.amazonaws.com/YM43nXHjaEPT_ll3N51E1wn3Ql7gxr6DQ2r9SN6dbJnooBoQDIeytTsDzUMGljkHCvkLcy1bdIGiE2LhUA4EW_I5kANdtKHGNpNyBtf5B83K-Ndfy9hAkmTrVkpy9GNk.png)**Labby** 
            - 
            - # **Summary**
                - [Size]();-[H1]()
            - In this lab, you have learned how to use conditional statements in shell programming. You have practiced using if-else statements, elif clauses, numeric comparisons, string comparisons, and logical operators. These tools allow you to create more complex and decision-based shell scripts.
            - Key takeaways:
                - The basic structure of if-else statements in shell scripts
                - How to use elif for multiple conditions
                - Numeric comparison operators (-lt, -gt, -eq, etc.)
                - String comparison and logical operators
                - The importance of making scripts executable with chmod
            - Remember, practice is key to becoming proficient in shell scripting. Try creating your own scripts that use these concepts in different ways. As you advance, you'll find these conditional statements essential for creating more sophisticated and useful scripts.
        - Weather Advisory System
        - Bash Scripting Loops
        - Comparing Arrays in Shell
        - Shell Functions
        - Four Function Calculator
        - Special Variables in Shell
        - Bash Trap Command
        - File System Operations in Shell
        - File System Explorer
    -  **Build a Linux System Monitor Using Bash**
        - [Size]();-[H0]()
    -  **Build a Task Scheduler Using Bash**
        - [Size]();-[H0]()
    -  **Building Flappy Bird Using C**
        - [Size]();-[H0]()
    -  **Creating a Typing Game Using Bash**
        - [Size]();-[H0]()
    -  **Chess Board in Terminal**
        - [Size]();-[H0]()
    -  **Implement Custom Trash-Enabled Command**
        - [Size]();-[H0]()
    -  **Users and Groups Creation and Deletion Batch**
        - [Size]();-[H0]()
    -  **Collect Files From Specified Time**
        - [Size]();-[H0]()
    -  **Copy Large Files with Preserved Structure**
        - [Size]();-[H0]()
    -  **Customizing Linux File Listing**
        - [Size]();-[H0]()
    -  **Extracting Information From Text**
        - [Size]();-[H0]()
    -  **Extracting Link Information From Text**
        - [Size]();-[H0]()
    -  **Get Program That Satisfies the Condition**
        - [Size]();-[H0]()
    -  **Linux Server Information Retrieval**
        - [Size]();-[H0]()
    -  **Nginx Log Analysis and Optimization**
        - [Size]();-[H0]()
    -  **Automated Daily System Log Backup**
        - [Size]();-[H0]()
    -  **Network Data Packet Statistics**
        - [Size]();-[H0]()
    -  **Random Password Generator Development**
        - [Size]();-[H0]()
    -  **Searching for Specific Files**
        - [Size]();-[H0]()
    -  **Samba File Sharing on Linux**
        - [Size]();-[H0]()
    -  **Shell Practice Challenges**
        - [Size]();-[H0]()
