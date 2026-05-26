-  **Quick Start with Shell - **18 labs
    1. **Hello, Bash!**
        - 
        1.  ^^^**Create a Shell Script File**^^^
            - ^^^creates an empty file named^^^ `hello.sh` ^^^in your current directory. ^^^
                - {{`touch`}}` hello.sh` 
                - ^^^The^^^ {{`.sh`}} ^^^extension is commonly used for shell scripts, but it's not mandatory.^^^ 
        2.  ^^^**Edit the Shell Script**^^^
            - {{`#!/bin/bash`}} ^^^- This is called a "^^^^^^{{shebang}}^^^^^^" line. ^^^ 
                1. ^^^It tells the system which ^^^^^^{{interpreter}}^^^^^^ should be used to run this script. ^^^ 
                2. ^^^In this case, we're specifying the ^^^^^^{{Bash shell}}^^^^^^.^^^ 
            - `echo 'Hello, World!'` ^^^- This line uses the^^^ `echo` ^^^command to print the text "Hello, World!" to the screen.^^^
        3.  ^^^**Make the Script Executable**^^^
            - ^^^In Unix-like systems, files have permissions that control who can read, write, or execute them. ^^^
            - ^^^By default, new files are ^^^^^^{{not executable}}^^^^^^.^^^ 
            - ^^^To make our script ^^^^^^{{executable}}^^^^^^, we use the^^^ {{`chmod`}} ^^^command (which stands for "^^^^^^{{change mode}}^^^^^^"). ^^^ 
            - ^^^Type the following command in the terminal and press Enter:^^^
            - Make hello.sh executable
                - {{`chmod +x`}}` hello.sh` 
                    - {{`chmod`}} ^^^is the command to change file permissions^^^ 
                    - {{`+x`}} ^^^means "add execute permission"^^^ 
                    - {{`hello.sh`}} ^^^is the name of our file^^^ 
        4.  ^^^**Execute the Script**^^^
            - ^^^Now that our script is executable, we can run it. ^^^
            - ^^^To run a script in the current directory, we use^^^ {{`./`}} ^^^before the script name. ^^^ 
            - ^^^This^^^ `./` ^^^tells the system to look for the script in the ^^^^^^{{current}}^^^^^^ directory.^^^ 
            - Run hello.sh
                - {{`./hello.sh`}} 
        5.  ^^^**View the Script Contents**^^^
            - ^^^We can do this using the^^^ {{`cat`}} ^^^command, which displays the contents of a file in the terminal.^^^ 
            - display the contents of hello.sh
                - {{`cat`}}` hello.sh` 
    2. **Working with Shell Variables**
        - 
        1.  ^^^**Create Shell Variables**^^^
            - ^^^Shell variables are created by assigning a value to them using the^^^ {{`=`}} ^^^sign. ^^^ 
                1. ^^^Create a new file named^^^ `variables.sh` ^^^in the^^^ `/home/labex/project` ^^^directory:^^^
                    - `touch /home/labex/project/variables.sh`^^^ ^^^
                2. Bash variable syntax:
                    1. {{varname=value}} 
                3. ^^^Make the script executable:^^^
                    - `chmod`` +x /home/labex/project/variables.sh`^^^ ^^^
                4. ^^^Run the script:^^^
                    - `./variables.sh`^^^ ^^^ 
        2.  ^^^**Referencing Shell Variables**^^^
            1. Reference variable: {{`$var`}} 
            2. Escaping special characters: {{`$`}}`/` 
            3. Reference variable and avoiding ambiguity: {{`${var}`}} 
            4. Reference variable and preserving whitespace: {{`"$var"`}} 
            - ^^^The^^^ {{`$`}} ^^^sign is escaped in the first line to print it literally.^^^ 
            - ^^^{{Curly braces}}^^^{{ }}{{`{}`}} ^^^are used to clearly define the variable name in the second line.^^^ 
            - ^^^The last two lines show the difference between using quotes and not using quotes when referencing a variable with whitespace.^^^
        3.  ^^^{{**Command Substitution**}}^^^^^^ allows you to use the output of a command as the value of a variable. ^^^ 
            - ^^^This is done by enclosing the command with^^^ {{`$()`}} ^^^or ^^^^^^{{backticks (``)}}^^^^^^.^^^ 
            - Command Substitution syntax: {{`$(command)`}} 
            1. `$(date +"%Y-%m-%d")` ^^^runs the^^^ `date` ^^^command and captures its output.^^^ 
            2. `$(ls)` ^^^runs the^^^ `ls` ^^^command and captures its output.^^^ 
            3. `$(uptime -p)` ^^^runs the^^^ `uptime` ^^^command with the^^^ `-p` ^^^option and captures its output.^^^ 
        4.  ^^^**Arithmetic Operations**^^^
            -  Syntax for Arithmetic Operations:{{`$((expression))`}}  
            -  Addition
                1. `SUM=`{{`$((X + Y))`}} 
                2. `echo "Sum of $X and $Y is: $SUM"`
            -  Subtraction
                1. `DIFF=`{{`$((X - Y))`}} 
                2. `echo "Difference between $X and $Y is: $DIFF"`
            -  Multiplication
                1. `PRODUCT=`{{`$((X * Y))`}} 
                2. `echo "Product of $X and $Y is: $PRODUCT"`
            -  Division
                1. `QUOTIENT=`{{`$((X / Y))`}} 
                2. `echo "Quotient of $X divided by $Y is: $QUOTIENT"`
            -  Modulus (remainder)
                1. `REMAINDER=`{{`$((X % Y))`}} 
                2. `echo "Remainder of $X divided by $Y is: $REMAINDER"`
            -  Increment 
                1. `X=`{{`$((X + 1))`}} 
                2. `echo "After incrementing, X is now: $X"`
            -  Decrement 
                1. `Y=`{{`$((Y - 1))`}} 
                2. `echo "After decrementing, Y is now: $Y"`
        5.  ^^^**Using **^^^^^^{{**Environment Variables**}}^^^^^^ are a type of variable that is available to all processes running in the current shell session. ^^^ 
            1. Common Environment Variables:
                1. Home directory: {{$HOME}} 
                2. Current user: {{$LOGNAME}} 
                3. Shell being used: {{$SHELL}} 
                4. Current PATH: {{$PATH}} 
    3. Finding the Pirate's Treasure  
        - Decoding the Treasure Map
        - 
        - # ^^^**Introduction**^^^
            - ^^^Captain Blackbeard has hidden his treasure on a remote island and left behind a series of clues encoded as shell variables and arithmetic operations. ^^^
            - ^^^In this challenge, you will complete a partially written shell script to decode these clues and locate the treasure.^^^
        - # ^^^**Decoding the Treasure Map**^^^
            - ^^^The treasure map has been encoded into a shell script that needs to be completed. ^^^
            - ^^^The script uses basic arithmetic operations to convert the initial coordinates into the final location. ^^^
            - ^^^Your task is to fill in the missing values and calculations to reveal where the treasure is buried.^^^
        - ## ^^^**Tasks**^^^
            - ^^^Complete the^^^ `treasure_map.sh` ^^^script in the^^^ `/home/labex/project` ^^^directory by:^^^
                - ^^^Assigning the correct initial values to the^^^ `LATITUDE` ^^^and^^^ `LONGITUDE` ^^^variables.^^^
                - ^^^Implementing arithmetic operations to calculate^^^ `PACES_NORTH` ^^^and^^^ `PACES_EAST`^^^.^^^
        - ## ^^^**Requirements**^^^
            1. ^^^The shell script^^^ `treasure_map.sh` ^^^is located in^^^ `/home/labex/project` ^^^with the following code structure:^^^
        - ```bash
#!/bin/bash

# Assign the correct values to these variables
LATITUDE=
LONGITUDE=

# Calculate the paces using arithmetic operations
``````bash

PACES_NORTH=
PACES_EAST=

# Don't modify the line below
``````bash

echo "The treasure is buried $PACES_NORTH paces north and $PACES_EAST paces east from the old oak tree."
```^^^ ^^^ 
            1. ^^^Use these values and calculations:^^^
                - ^^^Set^^^ `LATITUDE` ^^^to^^^ `15`^^^.^^^
                - ^^^Set^^^ `LONGITUDE` ^^^to^^^ `25`^^^.^^^
                - ^^^Calculate^^^ `PACES_NORTH` ^^^as latitude multiplied by 2.^^^
                - ^^^Calculate^^^ `PACES_EAST` ^^^as longitude divided by 5.^^^
            2. ^^^The script will output the treasure location in this format:^^^
        - `The treasure ``is`` buried X paces north ``and`` Y paces east ``from`` the old oak tree.`^^^ ^^^
        - ^^^Where X and Y are the calculated values.^^^
        - ## ^^^**Example Output**^^^
            - `The treasure ``is`` buried ``30`` paces north ``and`` ``5`` paces east ``from`` the old oak tree.`^^^ ^^^
    4. **Passing Arguments to the Script**
        - 
        -  ^^^**Create a new script file**^^^
            - ^^^The first line is called the "^^^^^^{{shebang}}^^^^^^" or "^^^^^^{{hashbang}}^^^^^^". ^^^ 
                - ^^^It tells the system which ^^^^^^{{interpreter}}^^^^^^ to use to execute the script. ^^^ 
                    - ^^^In this case, we're using bash.^^^
        -  ^^^**Access script arguments**^^^
            - ^^^Now, let's modify our script to access and display the arguments passed to it. ^^^
                - ^^^In Shell scripting, special variables are used to access command-line arguments:^^^
                    - {{`$0`}} ^^^represents the ^^^^^^{{name}}^^^^^^ of the script itself^^^ 
                    - {{`$1`}}^^^{{,}}^^^{{ }}{{`$2`}}^^^{{,}}^^^{{ }}{{`$3`}}^^^{{, etc.,}}^^^^^^ represent the first, second, third ^^^^^^{{arguments}}^^^^^^, and so on^^^ 
            - Print the name of the script: `echo `{{`$0`}} 
            - Print the second argument: `echo `{{`$2`}} 
            - ^^^The^^^ {{`$`}} ^^^symbol is used to reference variables in bash.^^^ 
            - {{`$0`}}^^^{{,}}^^^{{ }}{{`$1`}}^^^{{,}}^^^{{ }}{{`$2`}}^^^{{, etc.}}^^^^^^, are special variables that bash automatically sets for you when you run a script with arguments.^^^ 
            - ^^^If you run the script without any arguments,^^^ `$1`^^^,^^^ `$2`^^^, and^^^ `$3` ^^^will be empty, but the script will still run without errors.^^^
        -  ^^^**Make the script executable**^^^
            - ^^^The^^^ `chmod +x` ^^^command adds execute permissions to the file, allowing it to be run as a script.^^^
            - ^^^For beginners:^^^
                - `chmod` ^^^stands for "change mode". ^^^
                    - ^^^It's used to change the permissions of a file or directory.^^^
                - ^^^The^^^ `+x` ^^^option adds the execute permission. ^^^
                    - ^^^This is necessary for bash to be able to run the file as a script.^^^
                - ^^^If you forget this step, you'll get a "permission denied" error when trying to run your script.^^^
        -  ^^^**Execute the script with arguments**^^^
            - Run script with arguments foo and bar:
                - {{`./script foo bar`}}` ` 
            - Run script with arguments foo bar and baz
                - {{`./script "foo bar" baz`}} 
            - ^^^For beginners:^^^
                - ^^^The^^^ `./` ^^^before the script name tells bash to look for the script in the current directory.^^^
                - ^^^Each word after the script name becomes a separate argument. ^^^
                    - ^^^In this case, "hello" is the first argument, "world" is the second, and "example" is the third.^^^
                - ^^^If you want to pass an argument with spaces, you need to use quotes, like this:^^^ `./arguments.sh "hello world" example`
        -  ^^^**Handle the number of arguments**^^^
            - ^^^Let's modify our script to handle different numbers of arguments. ^^^
            - ^^^We'll use the^^^ {{`$#`}} ^^^special variable, which holds the number of arguments passed to the script.^^^ 
            - 
            - ^^^Update your^^^ `arguments.sh` ^^^file with the following content:^^^
            - ```
#!/bin/bash
``````



``````
if
``````
 [ 
``````
$#
``````
 -eq 0 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"No arguments provided."
``````


``````
elif
``````
 [ 
``````
$#
``````
 -eq 1 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"One argument provided: 
``````
$1
``````
"
``````


``````
elif
``````
 [ 
``````
$#
``````
 -eq 2 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"Two arguments provided: 
``````
$1
``````
 and 
``````
$2
``````
"
``````


``````
else
``````

  
``````
echo
``````
 
``````
"More than two arguments provided:"
``````

  
``````
echo
``````
 
``````
"First argument: 
``````
$1
``````
"
``````

  
``````
echo
``````
 
``````
"Second argument: 
``````
$2
``````
"
``````

  
``````
echo
``````
 
``````
"Third argument: 
``````
$3
``````
"
``````

  
``````
echo
``````
 
``````
"Total number of arguments: 
``````
$#
``````
"
``````


``````
fi
```^^^ ^^^
            - ^^^This script uses conditional statements to handle different numbers of arguments.^^^
            - {{`$#`}} ^^^is a special variable that contains the number of arguments passed to the script.^^^ 
            - `[ $# -eq 0 ]` ^^^is a ^^^^^^{{condition}}^^^^^^ that checks if the number of arguments is equal to 0.^^^ 
            - {{`elif`}} ^^^is short for "^^^^^^{{else if}}^^^^^^". It allows you to check multiple conditions in sequence.^^^ 
            - ^^^The^^^ {{`-eq`}} ^^^operator means "^^^^^^{{equal to}}^^^^^^". ^^^ 
            - ^^^There are other operators like^^^ {{`-lt`}} ^^^(^^^^^^{{less than}}^^^^^^),^^^ {{`-gt`}} ^^^(^^^^^^{{greater than}}^^^^^^), etc.^^^ 
        -  ^^^**Test the updated script**^^^
            - ^^^Now, let's test our updated script with different numbers of arguments:^^^
            - ```
./arguments.sh
./arguments.sh one
./arguments.sh one two
./arguments.sh one two three four
```^^^ ^^^
            - ^^^You should see different outputs based on the number of arguments provided.^^^
            - ^^^For beginners:^^^
                - ^^^Running the script without any arguments (^^^`./arguments.sh`^^^) will trigger the first condition in our script.^^^
                - ^^^Each subsequent command adds more arguments, demonstrating how our script handles different cases.^^^
                - ^^^Notice how the script's behavior changes based on the number of arguments. This kind of flexibility is very useful in real-world scripts.^^^
        -  ^^^**Loop through all arguments**^^^
            - ^^^Finally, let's modify our script to loop through all provided arguments using ^^^
            - ^^^the^^^ {{`$@`}} ^^^special variable, which represents all command-line arguments.^^^ 
            - ^^^Update your^^^ `arguments.sh` ^^^file with the following content:^^^
            - ```
#!/bin/bash
``````


echo "Total number of arguments: $#"
echo "All arguments:"

count=1
for arg in "$@"; do
  echo "Argument $count: $arg"
  count=$((count + 1))
done
```^^^ ^^^ 
            - ^^^This script uses a^^^ {{`for`}} ^^^loop to iterate through all arguments and display them with their position.^^^ 
            - ^^^For beginners:^^^
                - {{`$@`}} ^^^is a special variable that contains all the arguments passed to the script.^^^ 
                - ^^^The^^^ {{`for`}} ^^^loop is used to ^^^^^^{{iterate}}^^^^^^ over a list of items. ^^^
                    - ^^^In this case, it's iterating over all the arguments.^^^ 
                - `$((count + 1))` ^^^is arithmetic expansion in bash. ^^^ 
                    - ^^^It's used to increment the count variable.^^^
                - ^^^This script will work with any number of arguments, making it more flexible than our previous versions.^^^
        -  ^^^**Test the final script**^^^
            - ^^^Let's test our final script with multiple arguments:^^^
            - `./arguments.sh apple banana cherry ``date`^^^ ^^^
            - ^^^You should see output similar to this:^^^
            - ```
Total number of arguments:
``````
 
``````
4
``````


``````
All arguments:
``````


``````
Argument 1:
``````
 
``````
apple
``````


``````
Argument 2:
``````
 
``````
banana
``````


``````
Argument 3:
``````
 
``````
cherry
``````


``````
Argument 4:
``````
 
``````
date
```^^^ ^^^
            - ^^^This demonstrates that our script can now handle any number of arguments and display them all.^^^
            - ^^^For beginners:^^^
                - ^^^This final version of the script is much more flexible than our earlier versions.^^^
                - ^^^It can handle any number of arguments, from zero to many.^^^
                - ^^^The script now numbers each argument, which can be very useful in more complex scripts.^^^
                - ^^^Try running the script with different numbers of arguments to see how it behaves.^^^
    5. **Shell Arrays**
        - 
        -  ^^^**Initialize empty arrays**^^^
            - Initialize an empty array: {{`arr=()`}} 
            - ^^^Now that we have our script file, let's start by initializing three empty arrays.^^^
            - ^^^Add the following code to your^^^ `arrays.sh` ^^^file:^^^
            - ```
#!/bin/bash
``````



``````
# Initialize empty arrays
``````

NUMBERS=()
STRINGS=()
NAMES=()
```^^^ ^^^
            - ^^^The first line^^^ `#!/bin/bash` ^^^is called a shebang. ^^^
                - ^^^It tells the system that this script should be executed by the Bash shell.^^^
            - ^^^We're creating three empty arrays:^^^ `NUMBERS`^^^,^^^ `STRINGS`^^^, and^^^ `NAMES`^^^.^^^
            - ^^^The^^^ {{`()`}} ^^^syntax initializes an empty array.^^^ 
        -  ^^^**Add elements to the arrays**^^^ 
            - Add an element to an array: {{`arr+=ele`}} 
            - ^^^Now that we have our empty arrays, let's add some elements to them.^^^
            - ^^^Add the following code to your^^^ `arrays.sh` ^^^file, below the array initializations:^^^
            - ```
# Add elements to NUMBERS array
``````

NUMBERS+=(1)
NUMBERS+=(2)
NUMBERS+=(3)


``````
# Add elements to STRINGS array
``````

STRINGS+=(
``````
"hello"
``````
)
STRINGS+=(
``````
"world"
``````
)


``````
# Add elements to NAMES array
``````

NAMES+=(
``````
"John"
``````
)
NAMES+=(
``````
"Eric"
``````
)
NAMES+=(
``````
"Jessica"
``````
)
```^^^ ^^^
            - ^^^We use the^^^ {{`+=`}} ^^^operator to append elements to our arrays.^^^ 
            - ^^^For^^^ `NUMBERS`^^^, we're adding the integers 1, 2, and 3.^^^
            - ^^^For^^^ `STRINGS`^^^, we're adding the words "hello" and "world".^^^
            - ^^^For^^^ `NAMES`^^^, we're adding three names: "John", "Eric", and "Jessica".^^^
            - ^^^Note that we enclose string elements in quotes, but numbers don't need quotes.^^^
        -  ^^^**Determine the number of elements in an array**^^^
            - Get the number of elements in the array: {{`${#arr[@]}`}} 
            - ^^^One common operation with arrays is finding out how many elements they contain. ^^^
            - ^^^Let's do this for our^^^ `NAMES` ^^^array.^^^
            - ^^^Add the following code to your^^^ `arrays.sh` ^^^file:^^^
            - ```
# Get the number of elements in the NAMES array
``````

NumberOfNames=
``````
${#NAMES[@]}
```^^^ ^^^
            - ^^^This line does the following:^^^
                - `${#NAMES[@]}` ^^^gives us the number of elements in the^^^ `NAMES` ^^^array.^^^
                - ^^^We store this value in a variable called^^^ `NumberOfNames`^^^.^^^
                - ^^^The^^^ {{`@`}} ^^^symbol inside the brackets refers to all elements of the array.^^^ 
                - ^^^The^^^ {{`#`}} ^^^symbol before^^^ `NAMES` ^^^tells the shell to count the elements.^^^ 
        -  ^^^**Access a specific element in an array**^^^
            - Get the second element in the array: {{`${arr[1]}`}} 
            - ^^^Now, let's access a specific element in our^^^ `NAMES` ^^^array. We'll get the second name.^^^
            - ^^^Add this code to your^^^ `arrays.sh` ^^^file:^^^
            - ```
# Access the second name in the NAMES array
``````

second_name=
``````
${NAMES[1]}
```^^^ ^^^
            - ^^^We're accessing the second element of the^^^ `NAMES` ^^^array with^^^ `${NAMES[1]}`^^^.^^^
            - ^^^Remember, array indices in Bash start at ^^^^^^{{0}}^^^^^^, so^^^ {{`[1]`}} ^^^gives us the second element.^^^ 
            - ^^^We store this value in a variable called^^^ `second_name`^^^.^^^
        -  ^^^**Print the arrays and variables**^^^
            - ^^^`Finally, let's add some code to print out our arrays and variables to see the results of our operations.`^^^
            - ^^^`Add the following code to the end of your`^^^` ``arrays.sh`` `^^^`file:`^^^
            - ```
# Print the arrays and variables
``````


``````
echo
``````
 
``````
"NUMBERS array: 
``````
${NUMBERS[@]}
``````
"
``````


``````
echo
``````
 
``````
"STRINGS array: 
``````
${STRINGS[@]}
``````
"
``````


``````
echo
``````
 
``````
"The number of names listed in the NAMES array: 
``````
$NumberOfNames
``````
"
``````


``````
echo
``````
 
``````
"The second name on the NAMES list is: 
``````
$second_name
``````
"
```^^^` `^^^
            - ^^^`This code does the following:`^^^
                - ^^^`We use`^^^` ``echo`` `^^^`to print strings to the console.`^^^
                - `${NUMBERS[@]}`` `^^^`and`^^^` ``${STRINGS[@]}`` `^^^`print all elements of these arrays.`^^^
                - ^^^`We print the`^^^` ``NumberOfNames`` `^^^`and`^^^` ``second_name`` `^^^`variables we created earlier.`^^^
        -  ^^^**Run the script**^^^
            - ^^^Now that we've written our script, it's time to run it and see the results.^^^
                1. ^^^In your terminal, make sure you're in the correct directory:^^^
                    - `cd`` ~/project`^^^ ^^^
                2. ^^^Make the script executable:^^^
                    - `chmod`` +x arrays.sh`^^^ ^^^
                3. ^^^Run the script:^^^
                    - `./arrays.sh`^^^ ^^^
            - ^^^You should see output similar to this:^^^
            - ```
NUMBERS 
``````
array
``````
: 
``````
1
``````
 
``````
2
``````
 
``````
3
``````

STRINGS 
``````
array
``````
: hello world
The number 
``````
of
``````
 names listed 
``````
in
``````
 the NAMES 
``````
array
``````
: 
``````
3
``````

The 
``````
second
``````
 name 
``````
on
``````
 the NAMES list 
``````
is
``````
: Eric
```^^^ ^^^
            - ^^^This output shows that our array operations were successful:^^^
                - ^^^The^^^ `NUMBERS` ^^^array contains 1, 2, and 3.^^^
                - ^^^The^^^ `STRINGS` ^^^array contains "hello" and "world".^^^
                - ^^^We correctly counted 3 names in the^^^ `NAMES` ^^^array.^^^
                - ^^^We successfully retrieved "Eric" as the second name.^^^
    6. Interstellar Cargo Manifest
        - Creating the Cargo Manifest Script
        - 
        - # ^^^**Introduction**^^^
        - ^^^Welcome, space cadet! You're training to become a cargo officer on the interstellar ship "Nebula Nomad." Your first task is to create a simple inventory system for the ship's three cargo bays. You'll use shell arrays to store the inventory and accept a command-line argument to display the contents of a specific cargo bay.^^^
        - 
        - # ^^^**Creating the Cargo Manifest Script**^^^
        - ## ^^^**Tasks**^^^
            1. ^^^Open the existing shell script named^^^ `cargo_manifest.sh` ^^^in the^^^ `/home/labex/project` ^^^directory.^^^
            2. ^^^Complete the script by filling in the missing parts to create and display the ship's cargo inventory.^^^
            3. ^^^Run the script with different arguments to display each cargo bay's inventory.^^^
        - ## ^^^**Requirements**^^^
            1. ^^^The script^^^ `cargo_manifest.sh` ^^^is already created in the^^^ `/home/labex/project` ^^^directory with a code framework.^^^
            2. ^^^Complete the script by:^^^
                - ^^^Creating three arrays named^^^ `forward_bay`^^^,^^^ `midship_bay`^^^, and^^^ `aft_bay`^^^.^^^
                - ^^^Each array should contain exactly 3 items (strings) representing cargo items.^^^
                - ^^^Use the^^^ `$1` ^^^variable to check which cargo bay inventory to display.^^^
                - ^^^Display the inventory of the requested cargo bay using^^^ `echo` ^^^statements.^^^
            3. ^^^The script should accept one argument: either "forward", "midship", or "aft".^^^
            4. ^^^If no argument is provided, the script should display: "Please specify a cargo bay: forward, midship, or aft"^^^
            5. ^^^If an invalid argument is provided, the script should display: "Invalid cargo bay. Choose forward, midship, or aft."^^^
        - ## ^^^**Example**^^^
        - ^^^After completing the script, running it should produce output similar to this:^^^
        - ```
$ 
``````
./cargo_manifest.sh forward
Forward Bay Inventory:
1. Space Suits
2. Oxygen Tanks
3. Repair Kits

``````

$ 
``````
./cargo_manifest.sh midship
Midship Bay Inventory:
1. Food Supplies
2. Water Containers
3. Medical Equipment

``````

$ 
``````
./cargo_manifest.sh aft
Aft Bay Inventory:
1. Spare Parts
2. Fuel Cells
3. Scientific Instruments

``````

$ 
``````
./cargo_manifest.sh
Please specify a cargo bay: forward, midship, or aft

``````

$ 
``````
./cargo_manifest.sh engine
Invalid cargo bay. Choose forward, midship, or aft.
```^^^ ^^^
        - ^^^The script's strings must reference the examples and remain unchanged to prevent test failures.^^^
    7. **Arithmetic Operations in Shell**
        - 
        -  ^^^**Define variables for fruit costs**^^^
            - ^^^Now that we have our script file, let's define some variables to store the costs of different fruits and the basket.^^^
            - ^^^Add the following lines to your^^^ `fruit_basket.sh` ^^^file:^^^
            - ```
#!/bin/bash
``````



``````
# Define costs
``````

COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1
```^^^ ^^^
            - ^^^In Bash, we don't need to declare variables before using them. ^^^
                - ^^^We simply assign a value to a variable name.^^^
            - ^^^Variable names are case-sensitive. ^^^
                - ^^^By convention, we often use uppercase for constants (values that won't change).^^^
            - ^^^There should be no spaces around the^^^ `=` ^^^sign when assigning values.^^^
            - ^^^These values represent the cost in cents. ^^^
                - ^^^For example,^^^ `COST_PINEAPPLE=50` ^^^means a pineapple costs 50 cents.^^^
            - ^^^We don't need to specify a data type. ^^^
                - ^^^Bash treats these as strings by default, but will handle them as numbers when we perform arithmetic operations.^^^
        -  ^^^**Calculate the total cost**^^^
            - ^^^Now that we have our costs defined, let's calculate the total cost of a fruit basket containing 1 pineapple, 2 bananas, and 3 watermelons.^^^
            - ^^^Add the following line to your^^^ `fruit_basket.sh` ^^^file:^^^
            - ```
#!/bin/bash
``````



``````
# Define costs
``````

COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1


``````
# Calculate total cost
``````

TOTAL=$((COST_PINEAPPLE + (COST_BANANA * 
``````
2
``````
) + (COST_WATERMELON * 
``````
3
``````
) + COST_BASKET))
```^^^ ^^^
            - ^^^Let's examine this new line:^^^
                - {{`$(( ))`}} ^^^is Bash's syntax for arithmetic operations. ^^^ 
                    - ^^^Anything inside these double parentheses is treated as an ^^^^^^{{arithmetic}}^^^^^^ expression.^^^ 
                - ^^^Inside the arithmetic expression, we don't need to use^^^ {{`$`}} ^^^before variable names.^^^ 
                - ^^^We're performing several operations:^^^
                    - `COST_PINEAPPLE`^^^: The cost of 1 pineapple^^^
                    - `(COST_BANANA * 2)`^^^: The cost of 2 bananas^^^
                    - `(COST_WATERMELON * 3)`^^^: The cost of 3 watermelons^^^
                    - `COST_BASKET`^^^: The cost of the basket itself^^^
                - ^^^These values are all added together, and the result is stored in the^^^ `TOTAL` ^^^variable.^^^
            - ^^^Note: Bash only handles ^^^^^^{{integer}}^^^^^^ arithmetic. ^^^ 
                - ^^^If we were dealing with dollars and cents, we'd need to use a tool like^^^ `bc` ^^^for floating-point arithmetic.^^^
        -  ^^^**Display the total cost**^^^ 
            - ^^^To see the result of our calculation, we need to print the total cost. Add the following line to your^^^ `fruit_basket.sh` ^^^file:^^^
            - ```
#!/bin/bash
``````



``````
# Define costs
``````

COST_PINEAPPLE=50
COST_BANANA=4
COST_WATERMELON=23
COST_BASKET=1


``````
# Calculate total cost
``````

TOTAL=$((COST_PINEAPPLE + (COST_BANANA * 
``````
2
``````
) + (COST_WATERMELON * 
``````
3
``````
) + COST_BASKET))


``````
# Display the total cost
``````


``````
echo
``````
 
``````
"Total Cost is 
``````
$TOTAL
``````
 cents"
```^^^ ^^^
            - ^^^Let's break down this new line:^^^
                - `echo` ^^^is a command that prints text to the terminal.^^^
                - ^^^The text in quotes will be printed as-is, except for the^^^ `$TOTAL` ^^^part.^^^
                - ^^^When a variable name is preceded by^^^ `$` ^^^inside a string, Bash replaces it with the variable's value. This is called variable expansion.^^^
                - ^^^So if^^^ `TOTAL` ^^^is 128, the output will be "Total Cost is 128 cents".^^^
        -  ^^^**Make the script executable and run it**^^^
            - ^^^Now that our script is complete, we need to make it executable and then run it.^^^
                1. ^^^In the terminal, make the script executable with the^^^ `chmod` ^^^command:^^^
                    - `chmod`` +x ~/project/fruit_basket.sh`^^^ ^^^
                    - ^^^This command changes the mode of the file, adding execute (^^^`x`^^^) permission for the user.^^^
                2. ^^^Now, let's run the script:^^^
                    - `~/project/fruit_basket.sh`^^^ ^^^
                    - ^^^This command tells Bash to execute our script. The^^^ `~/project/` ^^^part specifies the path to our script.^^^
            - ^^^You should see output similar to:^^^
            - `Total Cost ``is`` ``128`` cents`^^^ ^^^
            - ^^^This output shows that the total cost of our fruit basket (1 pineapple, 2 bananas, 3 watermelons, and the basket itself) is 128 cents.^^^
    8. **Basic String Operations**
        - 
        -  **Introduction**
            - In this lab, you will learn about fundamental string operations in shell scripting. 
            - {{String}} operations are essential for manipulating and extracting data from text in various scripting tasks. 
            - You will explore concepts such as determining string length, finding character positions, extracting substrings, and replacing parts of strings. 
            - These skills are crucial for effective text processing in shell scripts.
            - 
            - Quick Reference Guide
            - Here's a quick overview of the string operations we'll cover in this lab:
            - Operation - Syntax - Description - Example
            - String {{Length}} - {{`${#string}`}} 
                - Calculates the number of characters in a string
                - `${`{{`#"hello"`}}`}` returns 5
            - {{Find}} Character Position - {{`$(expr index "$string" "$char")`}} 
                - Finds the position of a character in a string (1-indexed) 
                - `$(`{{`expr index "abcdef" "c"`}}`)` returns 3
            - {{Extract}} Substring - {{`${string:start:length}`}}` ` 
                - Extracts a portion of a string (0-indexed) 
                - `${`{{`"hello":1:3`}}`}` returns ell
            - Replace {{First}} Occurrence -  {{`${string/pattern/replacement}`}} 
                - Replaces the first occurrence of a pattern 
                - `${`{{`"hello"/l/L`}}`}` returns heLlo
            - Replace {{All}} Occurrences -  {{`${string//pattern/replacement}`}} 
                - Replaces all occurrences of a pattern 
                - `${`{{`"hello"//l/L`}}`}` returns heLLo
            - Replace at {{Beginning}} {{`${string/#pattern/replacement}`}}{{ }} 
                - Replaces pattern only if at beginning of string 
                - `${`{{`"hello"/#he/HE`}}`}` returns HEllo
            - Replace at {{End}} - {{`${string/%pattern/replacement}`}} 
                - Replaces pattern only if at end of string 
                - `${`{{`"hello"/%lo/LO`}}`}` returns helLO
        -  ^^^**String Length**^^^
            - ^^^Now, let's learn how to determine the length of a string.^^^
                1. ^^^Add the following code to your^^^ `string_operations.sh` ^^^file:^^^
                    - ```
echo
``````
 
``````
"Step 2: String Length"
``````


STRING=
``````
"Hello, World!"
``````

LENGTH=
``````
${#STRING}
``````



``````
echo
``````
 
``````
"The string is: 
``````
$STRING
``````
"
``````


``````
echo
``````
 
``````
"Its length is: 
``````
$LENGTH
``````
"
```^^^ ^^^
                    - ^^^Let's break this down step by step:^^^
                        - ^^^First, we add an echo command to display a header for this section.^^^
                            - `echo`` ``"Step 2: String Length"`^^^ ^^^
                        - ^^^Next, we define a variable called^^^ `STRING` ^^^and assign it the value "Hello, World!".^^^
                            - `STRING=``"Hello, World!"`^^^ ^^^
                            - ^^^In Bash, we don't need to use any special keywords to define variables. We simply write the variable name, followed by the equals sign, followed by the value.^^^
                        - ^^^Then, we calculate the length of the string using the^^^ `${#variable}` ^^^syntax and store it in a variable called^^^ `LENGTH`^^^.^^^
                            - `LENGTH=``${#STRING}`^^^ ^^^
                            - ^^^The^^^ {{`${#var}`}} ^^^is a special shell parameter expansion that returns the number of characters in the string stored in the variable.^^^ 
                        - ^^^Finally, we display both the original string and its length.^^^
                            - ```
echo
``````
 
``````
"The string is: 
``````
$STRING
``````
"
``````


``````
echo
``````
 
``````
"Its length is: 
``````
$LENGTH
``````
"
```^^^ ^^^
                            - ^^^The^^^ `$` ^^^symbol before a variable name tells Bash to replace it with the variable's value.^^^
        -  ^^^**Finding Character Position**^^^
            - ^^^Next, we'll learn how to find the position of a character in a string.^^^
                1. ^^^Add the following code to your^^^ `string_operations.sh` ^^^file:^^^
                    - ```
echo
``````
 -e 
``````
"\nStep 3: Finding Character Position"
``````


STRING=
``````
"abcdefghijklmnopqrstuvwxyz"
``````

CHAR=
``````
"j"
``````


POSITION=$(
``````
expr
``````
 index 
``````
"
``````
$STRING
``````
"
``````
 
``````
"
``````
$CHAR
``````
"
``````
)


``````
echo
``````
 
``````
"The string is: 
``````
$STRING
``````
"
``````


``````
echo
``````
 
``````
"We're looking for the character: 
``````
$CHAR
``````
"
``````


``````
echo
``````
 
``````
"It is at position: 
``````
$POSITION
``````
"
```^^^ ^^^
                    - ^^^Let's examine this code in detail:^^^
                        - ^^^We start with an echo command that includes the^^^ `-e` ^^^option and a^^^ `\n` ^^^escape sequence.^^^
                            - `echo`` -e ``"\nStep 3: Finding Character Position"`^^^ ^^^
                                - ^^^The^^^ {{`-e`}} ^^^option enables interpretation of escape sequences.^^^ 
                                - ^^^The^^^ {{`\n`}} ^^^escape sequence adds a newline before the text, creating a visual separation from the previous section.^^^ 
                        - ^^^Next, we define two variables:^^^
                            - ```
STRING=
``````
"abcdefghijklmnopqrstuvwxyz"
``````

CHAR=
``````
"j"
```^^^ ^^^
                                - `STRING` ^^^contains the entire lowercase alphabet.^^^
                                - `CHAR` ^^^contains the character "j" that we'll search for.^^^
                        - ^^^We use the^^^ `expr index` ^^^command to find the position of the character:^^^
                            - `POSITION=$(``expr`` index ``"``$STRING``"`` ``"``$CHAR``"``)`^^^ ^^^
                                - {{`expr`}} ^^^is a utility for evaluating expressions.^^^ 
                                - ^^^The^^^ {{`index`}} ^^^operation searches for characters in a string.^^^ 
                                - ^^^The^^^ {{`$()`}} ^^^syntax captures the output of the command and assigns it to the^^^ `POSITION` ^^^variable.^^^ 
                                - ^^^We enclose the variables in ^^^^^^{{double}}^^^^^^ quotes (^^^`"$STRING"`^^^) to prevent issues with special characters.^^^ 
                                - ^^^**Important**^^^^^^: This command returns positions starting from 1 (not 0).^^^
                        - ^^^Finally, we print out the results:^^^
                            - ```
echo
``````
 
``````
"The string is: 
``````
$STRING
``````
"
``````


``````
echo
``````
 
``````
"We're looking for the character: 
``````
$CHAR
``````
"
``````


``````
echo
``````
 
``````
"It is at position: 
``````
$POSITION
``````
"
```^^^ ^^^
                2. ^^^Save the file and run the script again:^^^
                    - `./string_operations.sh`^^^ ^^^
            - ^^^You should see additional output similar to:^^^
            - ```
Step
``````
 
``````
3
``````
: Finding Character Position
The 
``````
string
``````
 
``````
is
``````
: abcdefghijklmnopqrstuvwxyz
We
``````
're looking for the character: j
``````

It 
``````
is
``````
 at position: 
``````
10
```^^^ ^^^
            - ^^^Note that the position is 1-indexed, meaning the first character is at position 1, not 0. This is different from many programming languages where indexing typically starts at 0.^^^
        -  ^^^**Substring Extraction**^^^
            - ^^^Now, let's learn how to extract a portion of a string.^^^
                1. ^^^Add the following code to your^^^ `string_operations.sh` ^^^file:^^^
                    - ```
echo
``````
 -e 
``````
"\nStep 4: Substring Extraction"
``````


STRING=
``````
"The quick brown fox jumps over the lazy dog"
``````

START=10
LENGTH=5

SUBSTRING=
``````
${STRING:$START:$LENGTH}
``````



``````
echo
``````
 
``````
"The original string is: 
``````
$STRING
``````
"
``````


``````
echo
``````
 
``````
"Extracting 5 characters starting from position 10:"
``````


``````
echo
``````
 
``````
"The substring is: 
``````
$SUBSTRING
``````
"
```^^^ ^^^
                    - ^^^Let's analyze this code piece by piece:^^^
                        - ^^^First, we add a header with a newline for visual separation:^^^
                            - `echo`` -e ``"\nStep 4: Substring Extraction"`^^^ ^^^
                        - ^^^Next, we define our variables:^^^
                            - ```
STRING=
``````
"The quick brown fox jumps over the lazy dog"
``````

START=10
LENGTH=5
```^^^ ^^^
                                - {{`STRING`}} ^^^contains a sample sentence.^^^ 
                                - {{`START`}} ^^^is the position where we want to start extracting (position 10).^^^ 
                                - {{`LENGTH`}} ^^^is how many characters we want to extract (5 characters).^^^ 
                        - ^^^We use Bash's substring extraction syntax to get a portion of the string:^^^
                            - `SUBSTRING=``${STRING:$START:$LENGTH}`^^^ ^^^
                                - ^^^The syntax is^^^ `${variable:start_position:length}`
                                - `$START` ^^^and^^^ `$LENGTH` ^^^are variables containing the values 10 and 5.^^^
                                - ^^^**Important**^^^^^^: Unlike the^^^ `expr index` ^^^command, the positions here are 0-indexed, meaning the first character is at position 0.^^^
                        - ^^^Finally, we display the results:^^^
                            - ```
echo
``````
 
``````
"The original string is: 
``````
$STRING
``````
"
``````


``````
echo
``````
 
``````
"Extracting 5 characters starting from position 10:"
``````


``````
echo
``````
 
``````
"The substring is: 
``````
$SUBSTRING
``````
"
```^^^ ^^^
                2. ^^^Save the file and run the script again:^^^
                    - `./string_operations.sh`^^^ ^^^
            - ^^^You should see additional output similar to:^^^
            - ```
Step
``````
 
``````
4
``````
: Substring Extraction
The original 
``````
string
``````
 
``````
is
``````
: The quick brown fox jumps over the lazy dog
Extracting 
``````
5
``````
 characters starting 
``````
from
``````
 position 
``````
10
``````
:
The substring 
``````
is
``````
: brown
```^^^ ^^^
            - ^^^In the string "The quick brown fox...", position 10 (when counting from 0) is the 'b' in "brown", and the next 5 characters are "brown". This is why our extracted substring is "brown".^^^
            - ^^^Keep in mind that the indexing is different from what we saw in the previous step:^^^
                - ^^^In^^^ `expr index` ^^^(Step 3), positions start at 1 (first character is at position 1).^^^
                - ^^^In substring extraction^^^ `${STRING:position:length}` ^^^(Step 4), positions start at 0 (first character is at position 0).^^^
            - ^^^This is a common source of confusion in shell scripting, so it's important to remember which operations use which indexing system.^^^
        -  ^^^**String Replacement**^^^
            - ^^^Finally, let's learn how to replace parts of a string.^^^
                1. ^^^Add the following code to your^^^ `string_operations.sh` ^^^file:^^^
                    - ```
echo
``````
 -e 
``````
"\nStep 5: String Replacement"
``````


STRING=
``````
"The quick brown fox jumps over the lazy dog"
``````


``````
echo
``````
 
``````
"Original string: 
``````
$STRING
``````
"
``````



``````
# Replace the first occurrence of 'o' with 'O'
``````

NEW_STRING=
``````
${STRING/o/O}
``````


``````
echo
``````
 
``````
"Replacing first 'o' with 'O': 
``````
$NEW_STRING
``````
"
``````



``````
# Replace all occurrences of 'o' with 'O'
``````

NEW_STRING=
``````
${STRING//o/O}
``````


``````
echo
``````
 
``````
"Replacing all 'o' with 'O': 
``````
$NEW_STRING
``````
"
``````



``````
# Replace 'The quick' with 'The slow' if it's at the beginning of the string
``````

NEW_STRING=
``````
${STRING/#The quick/The slow}
``````


``````
echo
``````
 
``````
"Replacing 'The quick' with 'The slow' at the beginning: 
``````
$NEW_STRING
``````
"
``````



``````
# Replace 'dog' with 'cat' if it's at the end of the string
``````

NEW_STRING=
``````
${STRING/%dog/cat}
``````


``````
echo
``````
 
``````
"Replacing 'dog' with 'cat' at the end: 
``````
$NEW_STRING
``````
"
```^^^ ^^^
                    - ^^^Let's go through each string replacement operation:^^^
                        - ^^^First, we print a header and show the original string:^^^
                            - ```
echo
``````
 -e 
``````
"\nStep 5: String Replacement"
``````

STRING=
``````
"The quick brown fox jumps over the lazy dog"
``````


``````
echo
``````
 
``````
"Original string: 
``````
$STRING
``````
"
```^^^ ^^^
                        - ^^^Replace the first occurrence of a character:^^^
                            - ```
# Replace the first occurrence of 'o' with 'O'
``````

NEW_STRING=
``````
${STRING/o/O}
``````


``````
echo
``````
 
``````
"Replacing first 'o' with 'O': 
``````
$NEW_STRING
``````
"
```^^^ ^^^
                                - ^^^The syntax is^^^ `${variable/pattern/replacement}`
                                - ^^^This will find the first occurrence of 'o' and replace it with 'O'^^^
                                - ^^^Only the first 'o' in "brown" will be replaced, leaving the others unchanged.^^^
                        - ^^^Replace all occurrences of a character:^^^
                            - ```
# Replace all occurrences of 'o' with 'O'
``````

NEW_STRING=
``````
${STRING//o/O}
``````


``````
echo
``````
 
``````
"Replacing all 'o' with 'O': 
``````
$NEW_STRING
``````
"
```^^^ ^^^
                                - ^^^The syntax is^^^ `${variable//pattern/replacement}` ^^^(note the double slash)^^^
                                - ^^^The double slash tells Bash to replace ALL occurrences of the pattern^^^
                                - ^^^All 'o's in the entire string will be replaced with 'O's.^^^
                        - ^^^Replace a pattern at the beginning of a string:^^^
                            - ```
# Replace 'The quick' with 'The slow' if it's at the beginning of the string
``````

NEW_STRING=
``````
${STRING/#The quick/The slow}
``````


``````
echo
``````
 
``````
"Replacing 'The quick' with 'The slow' at the beginning: 
``````
$NEW_STRING
``````
"
```^^^ ^^^
                                - ^^^The syntax is^^^ `${variable/#pattern/replacement}`
                                - ^^^The^^^ `#` ^^^symbol specifies that the pattern must be at the beginning of the string^^^
                                - ^^^This will only replace 'The quick' if it appears at the start of the string.^^^
                        - ^^^Replace a pattern at the end of a string:^^^
                            - ```
# Replace 'dog' with 'cat' if it's at the end of the string
``````

NEW_STRING=
``````
${STRING/%dog/cat}
``````


``````
echo
``````
 
``````
"Replacing 'dog' with 'cat' at the end: 
``````
$NEW_STRING
``````
"
```^^^ ^^^
                                - ^^^The syntax is^^^ `${variable/%pattern/replacement}`
                                - ^^^The^^^ `%` ^^^symbol specifies that the pattern must be at the end of the string^^^
                                - ^^^This will only replace 'dog' if it appears at the end of the string.^^^
                2. ^^^Save the file and run the script again:^^^
                    - `./string_operations.sh`^^^ ^^^
            - ^^^You should see additional output similar to:^^^
            - ```
Step 
``````
5
``````
: String Replacement
Original string: The quick brown fox jumps 
``````
over
``````
 the lazy dog
Replacing 
``````
first
``````
 
``````
'o'
``````
 
``````
with
``````
 
``````
'O'
``````
: The quick brOwn fox jumps 
``````
over
``````
 the lazy dog
Replacing 
``````
all
``````
 
``````
'o'
``````
 
``````
with
``````
 
``````
'O'
``````
: The quick brOwn fOx jumps 
``````
Over
``````
 the lazy dOg
Replacing 
``````
'The quick'
``````
 
``````
with
``````
 
``````
'The slow'
``````
 
``````
at
``````
 the beginning: The slow brown fox jumps 
``````
over
``````
 the lazy dog
Replacing 
``````
'dog'
``````
 
``````
with
``````
 
``````
'cat'
``````
 
``````
at
``````
 the 
``````
end
``````
: The quick brown fox jumps 
``````
over
``````
 the lazy cat
```^^^ ^^^
            - ^^^These string replacement operations are powerful tools for manipulating text in shell scripts. They allow you to perform targeted replacements based on patterns and positions, which is especially useful for tasks like data processing, text formatting, or file content manipulation.^^^
        -  ^^^**Summary**^^^
            - ^^^Calculating the length of a string using^^^ `${#string}`^^^.^^^
            - ^^^Finding the position of a character in a string using^^^ `$(expr index "$string" "$char")`^^^.^^^
            - ^^^Extracting a substring from a larger string using^^^ `${string:start:length}`^^^.^^^
            - ^^^Performing various string replacement operations using:^^^
                - `${string/pattern/replacement}` ^^^- Replace first occurrence^^^
                - `${string//pattern/replacement}` ^^^- Replace all occurrences^^^
                - `${string/#pattern/replacement}` ^^^- Replace at beginning of string^^^
                - `${string/%pattern/replacement}` ^^^- Replace at end of string^^^
    9. **Conditional Statements in Shell**
        - 
        -  ^^^**Create Your First If Statement**^^^
            - ^^^Let's start by creating a simple if statement that checks if a variable called^^^ `NAME` ^^^is equal to "John".^^^
            - ^^^First, open a terminal in the WebIDE. You should be in the^^^ `/home/labex/project` ^^^directory by default. If you're not sure, you can always check your current directory with the^^^ `pwd` ^^^command.^^^
            - ^^^Create a new file called^^^ `if.sh` ^^^using the following command:^^^
            - `touch`` if.sh`^^^ ^^^
            - ^^^This command creates an empty file named^^^ `if.sh` ^^^in your current directory.^^^
            - ^^^Now, open the^^^ `if.sh` ^^^file in the WebIDE. You can do this by clicking on the file in the file explorer on the left side of the WebIDE.^^^
            - Bash if statement:
                - {{`if [ condition ]; then`}} first line of if statement
                    - {{`commands`}} meat and potatoes of if statement
                - {{`fi`}}  last line of if statement
            - ^^^Add the following content to the file:^^^
            - ```
#!/bin/bash
``````


NAME=
``````
"John"
``````


``````
if
``````
 [ 
``````
"
``````
$NAME
``````
"
``````
 = 
``````
"John"
``````
 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"The name is John"
``````


``````
fi
```^^^ ^^^
            - ^^^Let's break down this script:^^^
                1. `#!/bin/bash`^^^: This is called a "shebang" line. ^^^
                    1. ^^^It tells the system which interpreter to use to run the script. In this case, we're using Bash.^^^
                2. `NAME="John"`^^^: This line creates a variable called^^^ `NAME` ^^^and assigns it the value "John".^^^
                3. `if [ "$NAME" = "John" ]; then`^^^: This is the start of our ^^^^^^{{if statement}}^^^^^^. It checks if the value of^^^ `NAME` ^^^is equal to "John".^^^ 
                    - ^^^The square brackets^^^ {{`[ ]`}} ^^^are actually a command in Bash, equivalent to the^^^ {{`test`}} ^^^command.^^^ 
                    - ^^^We put^^^ `"$NAME"` ^^^in ^^^^^^{{quotes}}^^^^^^ to handle cases where^^^ `NAME` ^^^might be empty or contain spaces.^^^ 
                    - ^^^The semicolon and^^^ `then` ^^^are part of the if statement syntax in Bash.^^^
                4. `echo "The name is John"`^^^: This line will be executed if the condition is true.^^^
                5. {{`fi`}}^^^: This marks the end of the if statement. It's "if" spelled backwards!^^^ 
        -  ^^^**Add an Else Clause**^^^
            - If statement with else clause:
                - `if [ condition ]; then` first line of if statement
                    - `commands` meat and potatoes of if statement
                - {{`else`}} last clause
                    - `commands` 
                - `fi`  last line of if statement
            - ^^^Now, let's expand our if statement to include an else clause. This allows us to specify what should happen when the condition is false.^^^
            - ^^^Open the^^^ `if.sh` ^^^file in the WebIDE again and modify it as follows:^^^
            - ```
#!/bin/bash
``````


NAME=
``````
"Alice"
``````


``````
if
``````
 [ 
``````
"
``````
$NAME
``````
"
``````
 = 
``````
"John"
``````
 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"The name is John"
``````


``````
else
``````

  
``````
echo
``````
 
``````
"The name is not John"
``````


``````
fi
```^^^ ^^^
            - ^^^Let's go through the changes:^^^
                1. ^^^We've changed the^^^ `NAME` ^^^variable to "Alice". This is to demonstrate what happens when the condition is false.^^^
                2. {{`else`}} ^^^clause specifies what should happen if the condition in the if statement is false.^^^ 
                3. ^^^After the^^^ `else`^^^, we've added another^^^ `echo` ^^^command that will run if^^^ `NAME` ^^^is not "John".^^^
            - ^^^The^^^ {{`else`}} ^^^clause is optional in if statements, but it's very useful when you want to do something specific when the condition is false, rather than just doing nothing.^^^ 
            - ^^^Save the file with these changes.^^^
            - ^^^Now, run the script again:^^^
            - `./if.sh`^^^ ^^^
            - ^^^This time, you should see the output:^^^ `The name is not John`
            - ^^^This is because^^^ `NAME` ^^^is now "Alice", so the condition^^^ `[ "$NAME" = "John" ]` ^^^is false, and the code in the^^^ `else` ^^^block is executed.^^^
            - ^^^Try changing the^^^ `NAME` ^^^variable back to "John" and run the script again. What output do you get? This is a good way to test that your if-else statement is working correctly for both cases.^^^
        -  ^^^**Introducing Elif**^^^
            -  If statement with else clause:
                -  `if [ condition ]; then` first line of if statement
                    -  `commands` meat and potatoes of if statement
                -  {{`elif`}} first clause
                    -  `commands`
                -  `else` last clause
                    -  `commands`
                -  `fi`  last line of if statement
            - ^^^Sometimes, we want to check multiple conditions. This is where the^^^ `elif` ^^^(else if) clause comes in handy. Let's modify our script to handle multiple names.^^^
            - ^^^Update the^^^ `if.sh` ^^^file with the following content:^^^
            - ```
#!/bin/bash
``````


NAME=
``````
"George"
``````


``````
if
``````
 [ 
``````
"
``````
$NAME
``````
"
``````
 = 
``````
"John"
``````
 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"John Lennon"
``````


``````
elif
``````
 [ 
``````
"
``````
$NAME
``````
"
``````
 = 
``````
"Paul"
``````
 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"Paul McCartney"
``````


``````
elif
``````
 [ 
``````
"
``````
$NAME
``````
"
``````
 = 
``````
"George"
``````
 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"George Harrison"
``````


``````
elif
``````
 [ 
``````
"
``````
$NAME
``````
"
``````
 = 
``````
"Ringo"
``````
 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"Ringo Starr"
``````


``````
else
``````

  
``````
echo
``````
 
``````
"Unknown member"
``````


``````
fi
```^^^ ^^^
            - ^^^Let's break down this script:^^^
                1. ^^^We start with^^^ `NAME="George"`^^^. This will be the name we're checking.^^^
                2. ^^^The first^^^ `if` ^^^statement checks if the name is "John".^^^
                3. ^^^If it's not "John", we move to the first^^^ `elif` ^^^(else if) statement, which checks if the name is "Paul".^^^
                4. ^^^If it's not "Paul", we move to the next^^^ `elif`^^^, checking for "George".^^^
                5. ^^^If it's not "George", we check for "Ringo".^^^
                6. ^^^If none of these conditions are true, we fall through to the^^^ `else` ^^^clause, which will echo "Unknown member".^^^
            - ^^^The^^^ {{`elif`}} ^^^clause allows you to check multiple conditions in sequence. ^^^ 
            - ^^^You can have as many^^^ {{`elif`}} ^^^clauses as you need. ^^^ 
            - ^^^The conditions are checked in order, and the first one that's true will have its corresponding code block executed.^^^
            - ^^^Save the file with these changes.^^^
            - ^^^Now, run the script:^^^
            - `./if.sh`^^^ ^^^
            - ^^^You should see the output:^^^ `George Harrison`
            - ^^^Try changing the^^^ `NAME` ^^^variable to different values ("John", "Paul", "Ringo", or something else entirely) and run the script each time. Observe how the output changes based on the value of^^^ `NAME`^^^.^^^
        -  ^^^**Numeric Comparisons**^^^
            - ^^^Shell scripts can also compare numbers. Let's create a new script to demonstrate numeric comparisons.^^^
            - ^^^Create a new file called^^^ `numeric.sh`^^^:^^^
            - `touch`` numeric.sh`^^^ ^^^
            - ^^^Open^^^ `numeric.sh` ^^^in the WebIDE and add the following content:^^^
            - ```
#!/bin/bash
``````


NUMBER=10


``````
if
``````
 [ 
``````
$NUMBER
``````
 -lt 5 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"The number is less than 5"
``````


``````
elif
``````
 [ 
``````
$NUMBER
``````
 -eq 10 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"The number is exactly 10"
``````


``````
elif
``````
 [ 
``````
$NUMBER
``````
 -gt 15 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"The number is greater than 15"
``````


``````
else
``````

  
``````
echo
``````
 
``````
"The number is between 5 and 15, but not 10"
``````


``````
fi
```^^^ ^^^
            - ^^^This script introduces numeric comparison operators:^^^
                - {{`-lt`}}^^^: ^^^^^^{{less than}}^^^ 
                - {{`-eq`}}^^^: ^^^^^^{{equal to}}^^^ 
                - {{`-gt`}}^^^: ^^^^^^{{greater than}}^^^ 
            - ^^^There are also others you can use:^^^
                - {{`-le`}}^^^: ^^^^^^{{less than or equal to}}^^^ 
                - {{`-ge`}}^^^: ^^^^^^{{greater than or equal to}}^^^{{ }} 
                - {{`-ne`}}^^^:^^^^^^{{ not equal to}}^^^ 
            - ^^^Notice that we use these special operators instead of symbols like^^^ `<` ^^^or^^^ `>`^^^. ^^^
                - ^^^This is because in Bash,^^^ `<` ^^^and^^^ `>` ^^^are used for input/output redirection, not for numeric comparison.^^^
            - ^^^Now, let's make the script executable and run it:^^^
            - ```
chmod
``````
 +x numeric.sh
./numeric.sh
```^^^ ^^^
            - ^^^You should see the output:^^^ `The number is exactly 10`
            - ^^^Try changing the^^^ `NUMBER` ^^^variable to different values and run the script again. See how the output changes based on the value you set.^^^
            - ^^^For example, if you change^^^ `NUMBER` ^^^to 20, you should get "The number is greater than 15". If you change it to 7, you should get "The number is between 5 and 15, but not 10".^^^
            - 
        -  ^^^**String Comparisons and Logical Operators**^^^
            - ^^^Lastly, let's explore string comparisons and logical operators. Create a new file called^^^ `string_logic.sh`^^^:^^^
            - `touch`` string_logic.sh`^^^ ^^^
            - ^^^Open^^^ `string_logic.sh` ^^^in the WebIDE and add the following content:^^^
            - ```
#!/bin/bash
``````


STRING1=
``````
"hello"
``````

STRING2=
``````
"world"
``````

NUMBER1=5
NUMBER2=10


``````
if
``````
 [ 
``````
"
``````
$STRING1
``````
"
``````
 = 
``````
"hello"
``````
 ] && [ 
``````
"
``````
$STRING2
``````
"
``````
 = 
``````
"world"
``````
 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"Both strings match"
``````


``````
fi
``````



``````
if
``````
 [ 
``````
$NUMBER1
``````
 -lt 10 ] || [ 
``````
$NUMBER2
``````
 -gt 5 ]; 
``````
then
``````

  
``````
echo
``````
 
``````
"At least one of the number conditions is true"
``````


``````
fi
``````



``````
if
``````
 [[ 
``````
"
``````
$STRING1
``````
"
``````
 != 
``````
"
``````
$STRING2
``````
"
``````
 ]]; 
``````
then
``````

  
``````
echo
``````
 
``````
"The strings are different"
``````


``````
fi
``````



``````
if
``````
 [[ -z 
``````
"
``````
$STRING3
``````
"
``````
 ]]; 
``````
then
``````

  
``````
echo
``````
 
``````
"STRING3 is empty or not set"
``````


``````
fi
```^^^ ^^^
            - ^^^This script demonstrates several new concepts:^^^
                1. ^^^String ^^^^^^{{equality}}^^^^^^ comparison (^^^{{`=`}}^^^): This checks if two strings are exactly the same.^^^ 
                2. ^^^Logical ^^^^^^{{AND}}^^^^^^ (^^^{{`&&`}}^^^): This operator allows you to combine two conditions. Both conditions must be true for the overall expression to be true.^^^ 
                3. ^^^Logical ^^^^^^{{OR}}^^^^^^ (^^^{{`||`}}^^^): This operator also combines two conditions, but only one needs to be true for the overall expression to be true.^^^ 
                4. ^^^String ^^^^^^{{inequality}}^^^^^^ comparison (^^^{{`!=`}}^^^): This checks if two strings are different.^^^ 
                5. ^^^Checking if a string is ^^^^^^{{empty}}^^^^^^ (^^^{{`-z`}}^^^): This is true if the string is empty (has zero length).^^^ 
            - ^^^Also, notice the use of double square brackets^^^ {{`[[ ]]`}} ^^^in some of the if statements. These are an enhanced version of the single square brackets and are preferred in Bash scripts when possible. ^^^
                - ^^^They allow for more complex expressions and have fewer surprises with regard to word splitting and pathname expansion.^^^ 
            - ^^^Make the script executable and run it:^^^
            - ```
chmod
``````
 +x string_logic.sh
./string_logic.sh
```^^^ ^^^
            - ^^^You should see all four echo statements printed, because all the conditions in the script are true.^^^
            - ```
Both strings match
At least one of the number conditions is true
The strings are different
STRING3 is empty or not se
```^^^ ^^^
            - ^^^Try changing some of the values (like setting^^^ `STRING1` ^^^to something other than "hello") and see how it affects the output.^^^
    10. **Weather Advisory System** 
        - Complete the Weather Advisory Script
        - 
        - # **Introduction**
        - Imagine you're developing a simple weather advisory system for a local meteorology office. Your task is to complete a shell script that provides weather advice based on temperature input. This challenge will test your understanding of shell scripting if statements and basic user input handling.
        - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 97% pass rate. It has received a 98% positive review rate from learners.
        - 
        - # **Complete the Weather Advisory Script**
        - ## **Tasks**
            1. Navigate to the `~/project` directory where you'll find a partially completed script named `weather_advisor.sh`.
            2. Open the `weather_advisor.sh` file and complete the if statements to provide weather advice based on the temperature input.
        - ## **Requirements**
            - The script `weather_advisor.sh` is already created in the `~/project` directory with a basic structure.
            - The script already includes the shebang and user input prompt.
            - Your task is to complete the if statements to provide the following advice:
                - If the temperature is below 0°C: "It's freezing! Wear a heavy coat and gloves."
                - If the temperature is between 0°C and 10°C (inclusive): "It's cold. A warm jacket is recommended."
                - If the temperature is between 11°C and 20°C (inclusive): "It's cool. A light jacket should suffice."
                - If the temperature is above 20°C: "It's warm. Enjoy the pleasant weather!"
            - Use `echo` to display the advice to the user.
        - ## **Example**
        - Here's an example of how the completed script should work:
        - ```
$ ./weather_advisor.sh
Enter the current temperature in Celsius: 15
It's cool. A light jacket should suffice.

$ ./weather_advisor.sh
Enter the current temperature in Celsius: -2
It's freezing! Wear a heavy coat and gloves.

$ ./weather_advisor.sh
Enter the current temperature in Celsius: 25
It's warm. Enjoy the pleasant weather!
``` Explain Code
        - The script's strings must reference the examples and remain unchanged to prevent test failures.
        - 
        - # **Summary**
        - In this challenge, you completed a simple weather advisory system using shell scripting. You practiced using if statements to make decisions based on user input and provided appropriate output using `echo`. This exercise reinforced your understanding of conditional logic in shell scripts and demonstrated a practical application of these concepts in a real-world scenario.
        - solution
            - #!/bin/bash

echo "Enter the current temperature in Celsius: "
read temp

if [ "$temp" -lt 0 ]; then
  echo "It's freezing! Wear a heavy coat and gloves."
elif [ "$temp" -le 10 ]; then
  echo "It's cold. A warm jacket is recommended."
elif [ "$temp" -le 20 ]; then
  echo "It's cool. A light jacket should suffice."
else
  echo "It's warm. Enjoy the pleasant weather!"
fi  
    11. Bash Scripting Loops
        - Setting Up the Environment
        - The for Loop
        - The while Loop
        - The until Loop
        - Using break and continue Statements
        - 
        - # **Introduction**
        - In this lab, you will learn how to use loops in Bash scripting. Loops are powerful tools that allow you to repeat a set of instructions multiple times, making your scripts more efficient and flexible. We will cover three types of loops: `for`, `while`, and `until`. Additionally, you will explore the `break` and `continue` statements, which provide control over loop execution. This lab is designed for beginners and will guide you through each concept step-by-step.
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 96% completion rate. It has received a 100% positive review rate from learners.
        - 
        - # **Setting Up the Environment**
        - Let's start by setting up our working environment. We'll create a new directory to store all our loop experiments.
        - Open a terminal in the WebIDE. You should be in the `/home/labex/project` directory by default. If you're not sure, you can always navigate there using this command:
        - `cd /home/labex/project` Explain Code
        - Now, let's create a new directory for our loop experiments:
        - ```
mkdir bash_loops
cd bash_loops
``` Explain Code
        - This creates a new directory called `bash_loops` and changes into it. We'll use this directory for all our loop experiments.
        - Why are we doing this? Organizing your scripts into directories is a good practice. It keeps your work tidy and makes it easier to find and manage your files.
        - 
        - # **The** `**for**` **Loop**
        - The `for` loop is used to iterate over a list of values. It's like saying, "For each item in this list, do something." Let's create a script that demonstrates how to use a `for` loop.
        - Create a new file called `for_loop.sh` in the `bash_loops` directory:
        - `touch for_loop.sh` Explain Code
        - Now, open the `for_loop.sh` file in the WebIDE and add the following content:
        - ```
#!/bin/bash

# Loop through an array of names
echo "Looping through an array:"
NAMES=("Alice" "Bob" "Charlie" "David")
for name in "${NAMES[@]}"; do
  echo "Hello, $name!"
done

echo # Print an empty line for readability

# Loop through a range of numbers
echo "Looping through a range of numbers:"
for i in {1..5}; do
  echo "Number: $i"
done
``` Explain Code
        - Let's break down what this script does:
            1. The first loop goes through an array of names. For each name in the array, it prints a greeting.
            2. The second loop uses a range `{1..5}` to count from 1 to 5.
        - The `"${NAMES[@]}"` syntax might look strange. The `@` means "all elements of the array," and the quotes and curly braces ensure that each element is treated as a separate item, even if it contains spaces.
        - Save the file and make it executable with this command:
        - `chmod +x for_loop.sh` Explain Code
        - The `chmod +x` command makes the file executable, which means you can run it as a program.
        - Now, run the script:
        - `./for_loop.sh` Explain Code
        - You should see output like this:
        - ```
Looping through an array:
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, David!

Looping through a range of numbers:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
``` Explain Code
        - This demonstrates how `for` loops can iterate over both arrays and ranges of numbers.
        - 
        - # **The** `**while**` **Loop**
        - The `while` loop executes a block of code as long as a specified condition is true. It's like saying, "While this condition is true, keep doing this."
        - Create a new file called `while_loop.sh`:
        - `touch while_loop.sh` Explain Code
        - Open the `while_loop.sh` file in the WebIDE and add the following content:
        - ```
#!/bin/bash

# Simple countdown using a while loop
count=5
echo "Countdown:"
while [ $count -gt 0 ]; do
  echo $count
  count=$((count - 1))
  sleep 1 # Wait for 1 second
done
echo "Blast off!"
``` Explain Code
        - Let's break down this script:
            1. We start with `count=5` to set our initial countdown value.
            2. The condition `[ $count -gt 0 ]` means "while count is greater than 0".
            3. Inside the loop, we print the current count, decrease it by 1, and wait for a second.
            4. This continues until count reaches 0, at which point the loop ends.
        - The `sleep 1` command pauses the script for 1 second, creating a real-time countdown effect.
        - Save the file and make it executable:
        - `chmod +x while_loop.sh` Explain Code
        - Now, run the script:
        - `./while_loop.sh` Explain Code
        - You'll see a countdown from 5 to 1, with a one-second pause between each number:
        - ```
Countdown:
5
4
3
2
1
Blast off!
``` Explain Code
        - This demonstrates how a `while` loop can repeat an action until a condition is no longer true.
        - 
        - # **The** `**until**` **Loop**
        - The `until` loop is similar to the `while` loop, but with an important difference: it continues executing until a specified condition becomes true. It's like saying, "Keep doing this until this condition is true."
        - Create a new file called `until_loop.sh`:
        - `touch until_loop.sh` Explain Code
        - Open the `until_loop.sh` file in the WebIDE and add the following content:
        - ```
#!/bin/bash

# Count up to 5 using an until loop
count=1
echo "Counting up to 5:"
until [ $count -gt 5 ]; do
  echo $count
  count=$((count + 1))
  sleep 1 # Wait for 1 second
done
``` Explain Code
        - Let's break down this script:
            1. We start with `count=1` as our initial value.
            2. The condition `[ $count -gt 5 ]` means "until count is greater than 5".
            3. Inside the loop, we print the current count, increase it by 1, and wait for a second.
            4. This continues until count becomes greater than 5, at which point the loop ends.
        - Save the file and make it executable:
        - `chmod +x until_loop.sh` Explain Code
        - Now, run the script:
        - `./until_loop.sh` Explain Code
        - You'll see the numbers 1 through 5 printed, with a one-second pause between each:
        - ```
Counting up to 5:
1
2
3
4
5
``` Explain Code
        - This demonstrates how an `until` loop can repeat an action until a condition becomes true.
        - 
        - # **Using** `**break**` **and** `**continue**` **Statements**
        - The `break` and `continue` statements are used to control the flow of loops. `break` exits a loop early, while `continue` skips the rest of the current iteration and moves to the next one.
        - Create a new file called `break_continue.sh`:
        - `touch break_continue.sh` Explain Code
        - Open the `break_continue.sh` file in the WebIDE and add the following content:
        - ```
#!/bin/bash

# Using break to exit a loop early
echo "Demonstration of break:"
for i in {1..10}; do
  if [ $i -eq 6 ]; then
    echo "Breaking the loop at $i"
    break
  fi
  echo $i
done

echo # Print an empty line for readability

# Using continue to skip iterations
echo "Demonstration of continue (printing odd numbers):"
for i in {1..10}; do
  if [ $((i % 2)) -eq 0 ]; then
    continue
  fi
  echo $i
done
``` Explain Code
        - Let's break down this script:
            1. In the first loop, we use `break` to exit the loop when `i` equals 6.
            2. In the second loop, we use `continue` to skip even numbers. The condition `$((i % 2)) -eq 0` checks if a number is even (divisible by 2 with no remainder).
        - The `%` operator calculates the remainder after division. So `i % 2` will be 0 for even numbers and 1 for odd numbers.
        - Save the file and make it executable:
        - `chmod +x break_continue.sh` Explain Code
        - Now, run the script:
        - `./break_continue.sh` Explain Code
        - You should see output like this:
        - ```
Demonstration of break:
1
2
3
4
5
Breaking the loop at 6

Demonstration of continue (printing odd numbers):
1
3
5
7
9
``` Explain Code
        - This demonstrates how `break` can exit a loop early, and how `continue` can skip certain iterations based on a condition.
        - 
        - # **Summary**
        - In this lab, you've learned about three types of loops in Bash scripting:
            1. `for` loops, which iterate over a list of items or a range of numbers.
            2. `while` loops, which continue as long as a condition is true.
            3. `until` loops, which continue until a condition becomes true.
        - You've also learned about `break` and `continue` statements, which give you more control over your loops.
        - These loop structures are fundamental to many scripts and will allow you to automate repetitive tasks efficiently. Practice using these loops in your own scripts to become more familiar with their behavior and use cases.
    12. Comparing Arrays in Shell
        - Create the script file
        - Add the shebang and initialize the arrays
        - Implement the first comparison loop
        - Implement the second comparison loop
        - Make the script executable and run it
        - 
        - # **Introduction**
        - In this lab, you will learn how to compare arrays in Shell scripting. Arrays are useful data structures for storing multiple values, and comparing them is a common task in programming. You will work with three arrays and develop a script to find the common elements among them. This process will help you understand array manipulation, loops, and conditional statements in Shell scripting.
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 97% completion rate. It has received a 99% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/vdb96t_3F3nwaeD-6mLLAx4fpxgRWbXFmtfuHv-v-IBYG4F45MXiF3ZXvXn016dNQ6-PVlQv-XiMjxNlNJbb37tQwelAhsHLuvHr74HiPIRKlwppfIOco_EcOac_QTWs.webp)**Labby** 
        - 
        - # **Create the script file**
        - First, let's create a new file for our script.
            1. Open a terminal in the WebIDE. You should see a command prompt ending with a `$` sign.
            2. Navigate to the project directory:
        - `cd ~/project` Explain Code
        - This command changes your current directory to the project folder. The `~` symbol represents your home directory, and `/project` is a subfolder within it.
            1. Create a new file named `array-comparison.sh`:
        - `touch array-comparison.sh` Explain Code
        - The `touch` command creates an empty file. If the file already exists, it updates the file's timestamp without modifying its contents.
            1. Open the file in the WebIDE editor. You can do this by clicking on the file name in the file explorer on the left side of your WebIDE interface.
        - ![](https://remnote-user-data.s3.amazonaws.com/YHIZ_vlEsxTyJs34SFI5qNegF7-sxDE0-mHgkhPmCcIvUqPMLUHkO2mT2D5C9iDGi0CQ_fQU79D4hTsUtHMyW0cgjt1aLNtHwwyOvkuJXsppyxSjkFhHl0KVc5zFWy1m.webp)**Labby**
        - 
        - # **Add the shebang and initialize the arrays**
        - Now, let's start writing our script by adding the shebang and initializing our arrays.
            1. Add the following content to `array-comparison.sh`:
        - ```
#!/bin/bash

# Initialize the arrays
a=(3 5 8 10 6)
b=(6 5 4 12)
c=(14 7 5 7)
``` Explain Code
        - Let's break this down:
            - The first line `#!/bin/bash` is called a shebang. It tells the system to use the Bash interpreter to run this script. This line is crucial for any shell script.
            - We then initialize three arrays: `a`, `b`, and `c`. In Bash, arrays are defined by enclosing the elements in parentheses `()` and separating them with spaces.
            - Each array contains different integer values. We'll use these arrays to find common elements.
        - ![](https://remnote-user-data.s3.amazonaws.com/uETubQrIrKkp1PCJE7ZduIHhsk5UffTpStI2F2dGtlY123v3YCFYzOx32KrD79COnaRYMlQD4XFGS17dfP8tVu1x5oW30qP8R3Z0f1iwReS3j9a08p65aNV3SFsFpvgz.webp)**Labby**
        - 
        - # **Implement the first comparison loop**
        - Let's implement the first comparison loop to find common elements between arrays `a` and `b`.
        - Add the following code to your script:
        - ```
# Initialize an array to store common elements between a and b
z=()

# Compare arrays a and b
for x in "${a[@]}"; do
  for y in "${b[@]}"; do
    if [ $x = $y ]; then
      z+=($x)
    fi
  done
done

echo "Common elements between a and b: ${z[@]}"
``` Explain Code
        - Let's explain this code in detail:
            - `z=()` initializes an empty array `z` to store the common elements.
            - `for x in "${a[@]}"` is a loop that iterates over each element in array `a`. The `"${a[@]}"` syntax expands to all elements of the array.
            - We then have a nested loop `for y in "${b[@]}"` that iterates over each element in array `b`.
            - `if [ $x = $y ]` checks if the current element from `a` is equal to the current element from `b`.
            - If they are equal, we add this element to array `z` using `z+=($x)`.
            - Finally, we print the common elements using `echo "Common elements between a and b: ${z[@]}"`. The `${z[@]}` syntax expands to all elements of array `z`.
        - ![](https://remnote-user-data.s3.amazonaws.com/Mdn9zuFSKElHsW55KFuvd-gsSxkWcceqsqsrGXDdBXKZce8aFModgOB774BNZQyFsxhYZXotkzdDvqGFcR932QPMssQRPh_EZYgrPLKls4JG0kwP7Dkbf1CH3-OwHbiv.webp)**Labby**
        - 
        - # **Implement the second comparison loop**
        - Now, let's implement the second comparison loop to find common elements between array `c` and the previously found common elements in array `z`.
        - Add the following code to your script:
        - ```
# Initialize an array to store common elements among a, b, and c
j=()

# Compare array c with the common elements found in z
for i in "${c[@]}"; do
  for k in "${z[@]}"; do
    if [ $i = $k ]; then
      j+=($i)
    fi
  done
done

echo "Common elements among a, b, and c: ${j[@]}"
``` Explain Code
        - This code is similar to the previous loop, but with a few key differences:
            - We initialize a new empty array `j` to store the final common elements.
            - The outer loop `for i in "${c[@]}"` iterates over elements in array `c`.
            - The inner loop `for k in "${z[@]}"` iterates over the common elements we found between `a` and `b`, which are stored in array `z`.
            - We compare elements from `c` with elements in `z`, and if there's a match, we add it to array `j`.
            - Finally, we print the common elements among all three arrays.
        - ![](https://remnote-user-data.s3.amazonaws.com/D3SX1MMqJKv46hWTE6hHedcG5XPCll-ef6pHx3JbKO_Dq55SFQAyCOJAO6EO-POqFog2hrRJZaUEhcps-N1ZRioyBSVtOLSlIW2WBjJ6Ldpmnu5SB9sAiBIxWhvVVvZj.webp)**Labby**
        - 
        - # **Make the script executable and run it**
        - Now that we have completed our script, let's make it executable and run it.
            1. In the terminal, make the script executable:
        - `chmod +x ~/project/array-comparison.sh` Explain Code
        - The `chmod` command changes the permissions of a file. The `+x` option adds executable permissions, allowing you to run the script.
            1. Run the script:
        - `~/project/array-comparison.sh` Explain Code
        - This command executes your script. The `~/project/` part specifies the path to the script.
        - You should see output similar to this:
        - ```
Common elements between a and b: 5 6
Common elements among a, b, and c: 5
``` Explain Code
        - This output shows that:
            - The common elements between arrays `a` and `b` are 5 and 6.
            - The common element among all three arrays (`a`, `b`, and `c`) is 5.
        - If you don't see this output or encounter an error, double-check your script for any typos or missing parts.
        - ![](https://remnote-user-data.s3.amazonaws.com/I-tsaiCHWezx-KSpNcLMDSTl4O7urc0AeSdn8sT1BVlrJ5CAZo0xq0FNajp2IeCniwERL-tFNcU5zsWR6h__BbcPis4X5PNpPmSxjfx8P97_39169XnK123dcp2v3dfP.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned how to compare arrays in Shell scripting. You created a script that finds common elements among three arrays using nested loops and conditional statements. This exercise demonstrated key concepts in Shell scripting, including:
            1. Creating and initializing arrays
            2. Using nested loops to compare array elements
            3. Conditional statements to check for equality
            4. Adding elements to arrays dynamically
            5. Making a script executable and running it
        - These skills are fundamental in Shell scripting and can be applied to more complex data processing tasks in the future. As you continue to work with Shell scripts, you'll find that array manipulation is a powerful tool for handling sets of data efficiently.
        - Remember, practice is key to mastering these concepts. Try modifying the script to work with different arrays or to find unique elements instead of common ones. Happy scripting!
    13. Shell Functions
        - Creating Your First Shell Function
        - Functions with Parameters
        - Return Values from Functions
        - Understanding Variable Scope
        - Advanced Function - ENGLISH_CALC
        - 
        - # **Introduction**
        - In this lab, we will explore shell functions in Linux. Shell functions are reusable blocks of code that perform specific tasks, making our scripts more organized and efficient. We'll learn how to create, call, and use functions with parameters in shell scripts. This lab is designed for beginners, so we'll take it step by step and explain each concept thoroughly.
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 95% completion rate. It has received a 99% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/EnPPJjz2J57-G8YAZbhL9mbpZsnO85FK2TMwwb-Iinx7dfDCqR8AW1NpSctXIDCA4QKy_X5AcLQE39_58GscLtYZpJse4ztE8OUim-WWf33Y13Czz9oxFU6ZNls7AWL9.webp)**Labby** 
        - 
        - # **Creating Your First Shell Function**
        - Let's start by creating a simple shell function. Shell functions are like mini-scripts within a larger script, allowing you to group commands that perform a specific task.
        - First, we need to create a new file. Open your terminal and type:
        - ```
cd ~/project
touch functions.sh
``` Explain Code
        - This command changes to the `project` directory and creates a new file called `functions.sh`. This file will contain our shell functions.
        - Now, let's add our first function:
        - ```
#!/bin/bash

# This is a simple function
greet() {
  echo "Hello, World!"
}

# This line calls (runs) the function
greet
``` Explain Code
        - Let's break this down:
            - The first line `#!/bin/bash` is called a shebang. It tells the system to use bash to interpret this script.
            - We define our function with `greet() { }`. Everything between the curly braces is part of the function.
            - Inside the function, we have a simple `echo` command that prints "Hello, World!".
            - The last line `greet` calls (runs) our function.
        - Now, let's make our script executable and run it:
        - ```
chmod +x functions.sh
./functions.sh
``` Explain Code
        - You should see:
        - `Hello, World!` Explain Code
        - If you don't see this output, double-check that you've typed everything correctly in the `functions.sh` file.
        - ![](https://remnote-user-data.s3.amazonaws.com/Efg4DKwr8lZrBVl-gClqxH38BevGX7e8Px7mfKrItdRfo0rGnuPxNzBVqIMQxh-sBRm1rgeR6Kyo_9vYUTkc-Qv5atzYcfSuu0Adc9-nH-m2uffHY9l7bcqYIS52YtiC.webp)**Labby**
        - 
        - # **Functions with Parameters**
        - Now that we've created a basic function, let's make it more flexible by adding parameters. Parameters allow us to pass information into our functions.
        - Open the `functions.sh` file again, and replace the content with the following code:
        - ```
#!/bin/bash

# Function with a parameter
greet() {
  echo "Hello, $1!"
}

# Function with multiple parameters
calculate() {
  echo "The sum of $1 and $2 is $(($1 + $2))"
}

# Call functions with arguments
greet "Alice"
calculate 5 3
``` Explain Code
        - Let's examine this code:
            - In the `greet` function, `$1` refers to the first argument passed to the function.
            - In the `calculate` function, `$1` and `$2` refer to the first and second arguments, respectively.
            - `$(($1 + $2))` performs arithmetic addition of the two parameters.
        - `./functions.sh` Explain Code
        - You should see:
        - ```
Hello, Alice!
The sum of 5 and 3 is 8
``` Explain Code
        - If you don't see this output, make sure you've saved the changes to the file correctly.
        - ![](https://remnote-user-data.s3.amazonaws.com/7xsXuWuBr5i63Cykqso2t5W4MpZRt54Wb4750T-SUigQ_D-F6STDO0RmpTPJ3nvGlj_BrRFy3_SBMPacXXu2KXCQlC5qH7AKhL2jBYflKo9gkFf3L1l4maWy4K2mlLzT.webp)**Labby**
        - 
        - # **Return Values from Functions**
        - In shell scripting, functions don't return values in the same way as in other programming languages. Instead, they can either echo a result that can be captured, or they can modify a global variable. Let's explore both methods.
        - Open `functions.sh` again, and update the content with the following code:
        - ```
#!/bin/bash

# Function that echoes a result
get_square() {
  echo $(($1 * $1))
}

# Function that modifies a global variable
RESULT=0
set_global_result() {
  RESULT=$(($1 * $1))
}

# Capture the echoed result
square_of_5=$(get_square 5)
echo "The square of 5 is $square_of_5"

# Use the function to modify the global variable
set_global_result 6
echo "The square of 6 is $RESULT"
``` Explain Code
        - Let's break this down:
            - `get_square` function uses `echo` to output the result, which we capture using `$()` syntax.
            - `set_global_result` function modifies the global variable `RESULT`.
            - We use `$()` to capture the output of `get_square` into a variable.
            - We call `set_global_result`, which modifies `RESULT`, and then we print `RESULT`.
        - Save the file and run it:
        - `./functions.sh` Explain Code
        - You should see:
        - ```
The square of 5 is 25
The square of 6 is 36
``` Explain Code
        - If you don't see this output, double-check your `functions.sh` file for any typos.
        - ![](https://remnote-user-data.s3.amazonaws.com/2KCCrmYNTHtUNVYezUscPO2wlLZMBi95F7wHkp-K2TGZS7FypKDHY2LA_kYI0g1qD589UGKlU9PCL7QT3BUI6UIml1OTNe_tj17DP-_4EgURHzvJa2lY6BOBdpzYvJlN.webp)**Labby**
        - 
        - # **Understanding Variable Scope**
        - In shell scripts, variables are global by default. This means they can be accessed from anywhere in the script. However, you can use the `local` keyword to create variables that are only accessible within a function. This is called local scope.
        - Let's modify our `functions.sh` file to demonstrate this concept.
        - Update the content with the following code:
        - ```
#!/bin/bash

# Global variable
GLOBAL_VAR="I'm global"

# Function with a local variable
demonstrate_scope() {
  local LOCAL_VAR="I'm local"
  echo "Inside function: GLOBAL_VAR = $GLOBAL_VAR"
  echo "Inside function: LOCAL_VAR = $LOCAL_VAR"
}

# Call the function
demonstrate_scope

echo "Outside function: GLOBAL_VAR = $GLOBAL_VAR"
echo "Outside function: LOCAL_VAR = $LOCAL_VAR"
``` Explain Code
        - Here's what's happening in this script:
            - We define a global variable `GLOBAL_VAR`.
            - Inside the `demonstrate_scope` function, we define a local variable `LOCAL_VAR` using the `local` keyword.
            - We print both variables inside the function.
            - After calling the function, we try to print both variables again outside the function.
        - Save the file and run it:
        - `./functions.sh` Explain Code
        - You should see output similar to this:
        - ```
Inside function: GLOBAL_VAR = I'm global
Inside function: LOCAL_VAR = I'm local
Outside function: GLOBAL_VAR = I'm global
Outside function: LOCAL_VAR =
``` Explain Code
        - Notice that `LOCAL_VAR` is empty when accessed outside the function. This is because local variables are only accessible within the function where they are defined.
        - ![](https://remnote-user-data.s3.amazonaws.com/vhiAwxJDj5nvfQL6RF5l-F46esU48PhB-bPzG8DK08N8XX__DFTHNpwcirIfEzS6fOLdbRaXtHLcLg79yJaFhymRqk9jHIif5tqiuY3es62cPLx8nFbm0bvKgOLZ4IaW.webp)**Labby**
        - 
        - # **Advanced Function - ENGLISH_CALC**
        - Now that we've covered the basics of shell functions, let's create a more advanced function called `ENGLISH_CALC`. This function will take three arguments: two numbers and an operation (plus, minus, or times).
        - Replace the content with the following code:
        - ```
#!/bin/bash

ENGLISH_CALC() {
  local num1=$1
  local operation=$2
  local num2=$3
  local result

  case $operation in
    plus)
      result=$((num1 + num2))
      echo "$num1 + $num2 = $result"
      ;;
    minus)
      result=$((num1 - num2))
      echo "$num1 - $num2 = $result"
      ;;
    times)
      result=$((num1 * num2))
      echo "$num1 * $num2 = $result"
      ;;
    *)
      echo "Invalid operation. Please use 'plus', 'minus', or 'times'."
      return 1
      ;;
  esac
}

# Test the function
ENGLISH_CALC 3 plus 5
ENGLISH_CALC 5 minus 1
ENGLISH_CALC 4 times 6
ENGLISH_CALC 2 divide 2 # This should show an error message
``` Explain Code
        - Let's break down this function:
            - We use `local` variables to store our inputs and results. This is good practice to avoid interfering with any global variables.
            - We use a `case` statement to handle different operations. This is similar to a switch statement in other languages.
            - For each valid operation, we perform the calculation and echo the result.
            - If an invalid operation is provided, we echo an error message and return 1 (in shell scripts, a non-zero return value indicates an error).
            - At the end, we test our function with various inputs, including an invalid operation.
        - Save the file and run it:
        - `./functions.sh` Explain Code
        - You should see the following output:
        - ```
3 + 5 = 8
5 - 1 = 4
4 * 6 = 24
Invalid operation. Please use 'plus', 'minus', or 'times'.
``` Explain Code
        - If you don't see this output, double-check your `functions.sh` file for any typos.
        - ![](https://remnote-user-data.s3.amazonaws.com/1kPjhDuDDhR1-kgZu0l4Sx9HiBLFbZ875h7YP0vnEsIJc2DbWj21UVQPxEyZNfCHrMHB8CAyqM8QO3PW7DHSWac_o1tLKMLmiM7nLqYOZrCveCM-Xm8HtYDa7FWHrOx2.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, we explored shell functions in Linux, starting from the basics and progressing to more advanced concepts. We learned how to:
            1. Create and call simple functions
            2. Work with function parameters
            3. Return values from functions using echo and global variables
            4. Understand variable scope and use local variables
            5. Create a more complex function that processes arithmetic operations
        - Shell functions are powerful tools that can help you write more organized, efficient, and reusable code. They allow you to break down complex scripts into smaller, manageable pieces, making your scripts easier to understand and maintain.
        - By mastering shell functions, you'll be able to write more sophisticated shell scripts and automate complex tasks more effectively in a Linux environment. Remember, practice is key to becoming proficient with shell scripting. Try modifying the functions we've created or create your own to solve specific problems you encounter in your work with Linux.
    14. Four Function Calculator
        - Create Calculator Functions
        - 
        - # **Introduction**
        - In this challenge, you'll create a basic four-function calculator in a shell script. This will help you understand the fundamentals of defining and using multiple functions in shell scripting.
        - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 98% pass rate. It has received a 96% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/TpnhEbKppT5ZsKPiEmMPWhclO2SWjqGhvmRbOUGnTufApuOTZeagtmPuKDO_O6xSGrqYkupEWgm4bepluKD5OqdvOkm7hiZMRHw09qiks17zuFEe_oIBkKhl9vGgegGK.webp)**Labby** 
        - 
        - # **Create Calculator Functions**
        - ## **Tasks**
            1. Navigate to the `~/project` directory where you'll find a partially completed script named `calculator.sh`.
            2. Open the `calculator.sh` file and complete the four functions: `add`, `subtract`, `multiply`, and `divide`.
        - ## **Requirements**
            - The script `calculator.sh` is already created in the `~/project` directory with a basic structure.
            - Your task is to complete the following functions:
                - `add`: Takes two parameters and returns their sum.
                - `subtract`: Takes two parameters and returns the result of subtracting the second from the first.
                - `multiply`: Takes two parameters and returns their product.
                - `divide`: Takes two parameters and returns the result of dividing the first by the second. Remember to handle division by zero.
            - Each function should take two parameters and echo the result.
            - The main part of the script (which calls the functions) is already provided.
            - **Important Note**: In the case statement, all operation symbols (`+`, `-`, `*`, `/`) are enclosed in quotes to prevent shell interpretation. The `*` symbol without quotes acts as a wildcard and would match any input, causing unexpected behavior.
        - ## **Example**
        - Here's an example of how the completed script should work:
        - ```
$ ./calculator.sh
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): +
Result: 15

$ ./calculator.sh
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): -
Result: 5

$ ./calculator.sh
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): *
Result: 50

$ ./calculator.sh
Enter first number: 10
Enter second number: 5
Enter operation (+, -, *, /): /
Result: 2

$ ./calculator.sh
Enter first number: 10
Enter second number: 0
Enter operation (+, -, *, /): /
Error: Division by zero is not allowed.
``` Explain Code
        - The script's strings must reference the examples and remain unchanged to prevent test failures.
        - ![](https://remnote-user-data.s3.amazonaws.com/Ep-PE2RAP2-m6OCNT82_3YvWx9MdJDukNhTD0oHqyjkCMFxuPv-YuJtXU5DQb3tcGCJUWtKtlVjgCkxNzbROgufg0Z_ANEgMCn2B4wOq7L8Hp5qTOh6OGbG9iJwj610m.webp)**Labby**
        - 
        - # **Summary**
        - In this challenge, you created a four-function calculator using shell scripting. You practiced defining multiple functions that take parameters, perform calculations, and return results. This exercise reinforced your understanding of basic function declaration and usage in shell scripts, demonstrating practical applications for simple computations and error handling.
    15. Special Variables in Shell
        - Creating Your First Script
        - Running the Script with Arguments
        - Understanding $? and $
        - Using Special Variables in Functions
        - Understanding the Difference Between $@ and $*
        - 
        - # **Introduction**
        - In this lab, you will learn about special variables in shell scripting. These variables provide essential information about the script execution environment, such as command-line arguments, script name, and process ID. Understanding these variables will help you write more flexible and powerful shell scripts.
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 98% completion rate. It has received a 99% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/JtbjqRoM8XXi_ZbfoYUtcWsX2mV04pMXxcXGYqT02uOYzRJRHD_CRxwTFmzvM017eAFA-sS3BstK83O8vyiY98bDc1wP21XAXHGfy9XxtkfwWE_BpbLB2giMvCYHGmSk.webp)**Labby** 
        - 
        - # **Creating Your First Script**
        - Let's start by creating a simple shell script to demonstrate the use of special variables.
            1. Open your terminal in the WebIDE. You should see a command prompt waiting for your input.
            2. Navigate to the project directory:
        - `cd ~/project` Explain Code
        - This command changes your current directory to `~/project`, which is your default working directory for this lab.
            1. Create a new file named `special_vars.sh` using the following command:
        - `touch special_vars.sh` Explain Code
        - The `touch` command creates an empty file if it doesn't exist, or updates its timestamp if it does.
            1. Open the file in the WebIDE editor. You can do this by clicking on the file name in the file explorer on the left side of your screen.
            2. Add the following content to the file:
        - ```
#!/bin/bash

echo "Script Name: $0"
echo "First Argument: $1"
echo "Second Argument: $2"
echo "All Arguments: $@"
echo "Number of Arguments: $#"
echo "Process ID: $$"
``` Explain Code
        - Let's break down what each line does:
            - `#!/bin/bash`: This is called a shebang. It tells the system to use bash to interpret this script.
            - `$0`: This special variable holds the name of the script.
            - `$1` and `$2`: These represent the first and second command-line arguments respectively.
            - `$@`: This represents all the command-line arguments passed to the script.
            - `$#`: This gives the count of command-line arguments.
            - `$$`: This provides the process ID of the current shell.
            1. Save the file after adding the content.
            2. Make the script executable by running the following command in your terminal:
        - `chmod +x special_vars.sh` Explain Code
        - The `chmod` command changes the permissions of a file. The `+x` option adds execute permission, allowing you to run the script.
        - ![](https://remnote-user-data.s3.amazonaws.com/lOu1nPGZVkHySpBfyULpzL9OSwkOm6W02IC8yht7SCwmIy6xblM40a1GscXK8MJDuLJ68oA74iG3Ycuq-aAP5I-QfXv9fzJvsk7pmo2TxgiBWQYJ1cm8XETy9OZETvVl.webp)**Labby**
        - 
        - # **Running the Script with Arguments**
        - Now that we have created our script, let's run it with different arguments to see how the special variables behave.
            1. Run the script without any arguments:
        - `./special_vars.sh` Explain Code
        - The `./` before the script name tells the shell to look for the script in the current directory.
        - You should see output similar to this:
        - ```
Script Name: ./special_vars.sh
First Argument:
Second Argument:
All Arguments:
Number of Arguments: 0
Process ID: 1234
``` Explain Code
        - Notice that the first and second arguments are empty, and the number of arguments is 0 since we didn't provide any.
            1. Now, run the script with some arguments:
        - `./special_vars.sh hello world` Explain Code
        - The output should look like this:
        - ```
Script Name: ./special_vars.sh
First Argument: hello
Second Argument: world
All Arguments: hello world
Number of Arguments: 2
Process ID: 1235
``` Explain Code
        - Here's what changed:
            - `$1` now contains "hello"
            - `$2` now contains "world"
            - `$@` shows all arguments: "hello world"
            - `$#` shows 2, because we provided two arguments
        - The Process ID (`$$`) might be different each time you run the script, as it's assigned by the operating system.
        - ![](https://remnote-user-data.s3.amazonaws.com/dVbI3bHuQjzVBvBwa59w2STnWl1Qt3A3bth_jq8g-s9jnO_XEmRtRg1nJZRaFVkv_0YuUWfAfqh-M6E0uPQ1FWGPNQXqmQ6rzrUoLbDXZ6CEs7FHjt1fixmz3uVKl6RG.webp)**Labby**
        - 
        - # **Understanding** `**$?**` **and** `**$!**`
        - Two other important special variables are `$?` and `$!`. Let's create a new script to demonstrate their use.
            1. Create a new file named `exit_status.sh`:
        - `touch ~/project/exit_status.sh` Explain Code
            1. Open the file in the WebIDE editor and add the following content:
        - ```
#!/bin/bash

echo "Running a successful command:"
ls /home
echo "Exit status: $?"

echo "Running a command that will fail:"
ls /nonexistent_directory
echo "Exit status: $?"

echo "Running a background process:"
sleep 2 &
echo "Process ID of last background command: $!"
``` Explain Code
        - Let's break down this script:
            - `$?` gives the exit status of the last executed command. 0 typically means success, while non-zero values indicate various error conditions.
            - `$!` gives the process ID of the last background command.
            - The `&` at the end of a command runs it in the background.
            1. Save the file and make it executable:
        - `chmod +x ~/project/exit_status.sh` Explain Code
            1. Run the script:
        - `./exit_status.sh` Explain Code
        - You should see output similar to this:
        - ```
Running a successful command:
labex
Exit status: 0
Running a command that will fail:
ls: cannot access '/nonexistent_directory': No such file or directory
Exit status: 2
Running a background process:
Process ID of last background command: 1236
``` Explain Code
        - Notice:
            - The first `ls` command succeeds, so `$?` is 0.
            - The second `ls` command fails (because the directory doesn't exist), so `$?` is 2 (a non-zero value indicating an error).
            - The `sleep` command runs in the background, and `$!` gives its process ID.
        - ![](https://remnote-user-data.s3.amazonaws.com/IP9S3nIzINreqhHTSvnS9cZAXG4wvUccDKYwsKe_jAJCKMNGAkACry_AVU3rbdvZ7kKvYWTJgto-mfzE8K25rQa5yknPGyhFl-b7DTIIR_Uf-kq0n3XSy0Bi3GklJHOG.webp)**Labby**
        - 
        - # **Using Special Variables in Functions**
        - Special variables can also be used within functions. Let's create a script to demonstrate this.
            1. Create a new file named `function_vars.sh`:
        - `touch ~/project/function_vars.sh` Explain Code
            1. Open the file in the WebIDE editor and add the following content:
        - ```
#!/bin/bash

function print_args {
  echo "Function Name: $0"
  echo "First Argument: $1"
  echo "Second Argument: $2"
  echo "All Arguments: $@"
  echo "Number of Arguments: $#"
}

echo "Calling function with two arguments:"
print_args hello world

echo "Calling function with four arguments:"
print_args one two three four
``` Explain Code
        - This script defines a function `print_args` that uses special variables. Then it calls this function twice with different numbers of arguments.
            1. Save the file and make it executable:
        - `chmod +x ~/project/function_vars.sh` Explain Code
            1. Run the script:
        - `./function_vars.sh` Explain Code
        - You should see output similar to this:
        - ```
Calling function with two arguments:
Function Name: ./function_vars.sh
First Argument: hello
Second Argument: world
All Arguments: hello world
Number of Arguments: 2
Calling function with four arguments:
Function Name: ./function_vars.sh
First Argument: one
Second Argument: two
All Arguments: one two three four
Number of Arguments: 4
``` Explain Code
        - Notice that:
            - `$0` still refers to the script name, not the function name.
            - `$1`, `$2`, `$@`, and `$#` work for function arguments just like they do for script arguments.
            - The values of these variables change each time the function is called with different arguments.
        - ![](https://remnote-user-data.s3.amazonaws.com/j6AtFnX7kap0X0cK9Tt4a_ZeJJd_rt-24fCikbzk7LgfgVC2Tvr8O6sYTyFhtpsTRcBBrqvRQLtzpvmCX-1HMl9QpU94uDrHrkLZyLJk4zOS_5nyLzi83p-REXypnXfu.webp)**Labby**
        - 
        - # **Understanding the Difference Between $****@ and $***
        - The special variables `$@` and `$*` are both used to represent all command-line arguments, but they behave differently when enclosed in double quotes. Let's create a script to demonstrate this difference.
            1. Create a new file named `at_vs_star.sh`:
        - `touch ~/project/at_vs_star.sh` Explain Code
            1. Open the file in the WebIDE editor and add the following content:
        - ```
#!/bin/bash

echo "Using \$@:"
for arg in "$@"; do
  echo "Argument: $arg"
done

echo "Using \$*:"
for arg in "$*"; do
  echo "Argument: $arg"
done
``` Explain Code
        - This script demonstrates the difference between `$@` and `$*` when used in a loop.
            1. Save the file and make it executable:
        - `chmod +x ~/project/at_vs_star.sh` Explain Code
            1. Run the script with multiple arguments, including some with spaces:
        - `./at_vs_star.sh "arg with spaces" another_arg "third arg"` Explain Code
        - You should see output similar to this:
        - ```
Using $@:
Argument: arg with spaces
Argument: another_arg
Argument: third arg
Using $*:
Argument: arg with spaces another_arg third arg
``` Explain Code
        - Here's what's happening:
            - With `"$@"`, each argument is treated as a separate entity. Arguments with spaces are preserved as single units.
            - With `"$*"`, all arguments are combined into a single string, separated by the first character of the IFS (Internal Field Separator) variable, which is usually a space.
        - This difference is crucial when you need to process arguments that might contain spaces or other special characters.
        - ![](https://remnote-user-data.s3.amazonaws.com/ZYMzpO_R-6imjdbcbMBeYGx5kqGb7XcYRf4JvAMFdUsTmsN2AeKMwBI9SYsKqz_Rz4AO3HJBckSjwh4opIgzL2JexhsSzyFA-k7oKsAGg4rYLfrFinzs5xOGhQW2Pjfa.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you have learned about special variables in shell scripting and how to use them effectively. You have created scripts that demonstrate the usage of various special variables such as `$0`, `$1`, `$@`, `$#`, `$$`, `$?`, and `$!`. You have also explored how these variables behave in different contexts, including within functions and when handling command-line arguments.
        - Key takeaways:
            1. `$0`, `$1`, `$2`, etc. represent the script name and command-line arguments.
            2. `$@` and `$#` allow you to work with all arguments and count them.
            3. `$$` gives you the current process ID, useful for creating unique temporary files.
            4. `$?` helps you check if the previous command was successful.
            5. `$!` gives you the PID of the last background process, useful for job control.
            6. `$@` and `$*` behave differently when quoted, which is important when handling arguments with spaces.
        - Understanding these special variables is crucial for writing more advanced and flexible shell scripts. They allow you to create scripts that can adapt to different inputs and provide valuable information about the script's execution environment.
        - As you continue to practice and experiment with shell scripting, you'll find many more ways to leverage these special variables in your work. Remember to consult the bash manual (`man bash`) for more detailed information on these and other special variables.
    16. Bash Trap Command
        - Create a Bash Script
        - Implement a Basic Trap Command
        - Make the Script Executable and Run It
        - Modify the Trap to Use a Function
        - 
        - # **Introduction**
        - In this lab, we will explore the `trap` command in Bash scripting. The `trap` command is a powerful tool that allows you to catch and handle signals, interruptions, and user inputs in your scripts. By using `trap`, you can define specific actions to be taken when particular signals are received, enabling you to manage unpredictable behavior and gracefully handle various scenarios. This lab is designed for beginners and will guide you through the process of using the `trap` command effectively.
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 98% completion rate. It has received a 100% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/6QzTMYWzrMEM_LWLA5_28RZEJLVUOhDceWU5p3vSoB-ufSvB8XTtgqc5WJOlJyLd7v_T2l79Y78diIYbkWkNlUoQJubdBoCFrYZtjNbQ6TkTL8f3J_snuVQ6W1TU4AG-.webp)**Labby** 
        - 
        - # **Create a Bash Script**
        - Let's start by creating a new Bash script file where we'll implement the `trap` command.
            1. Open a terminal in the WebIDE. You should see a prompt ending with a `$` symbol.
            2. Navigate to the project directory:
                - `cd ~/project` Explain Code
                - This command changes your current working directory to `/home/labex/project`.
            3. Create a new file named `trap_example.sh`:
                - `touch trap_example.sh` Explain Code
                - The `touch` command creates an empty file if it doesn't exist, or updates the modification time if it does.
            4. Open the `trap_example.sh` file in the WebIDE editor. You can do this by clicking on the file name in the file explorer on the left side of the WebIDE.
        - ![](https://remnote-user-data.s3.amazonaws.com/d6oVieXoogcWacYO3DEpD9JI9Y2tYb-6r39dK4SSAvoBD55gJyWlGgmctloQP683XsnowTaLDi-eYQaNAoAf1bZC4aQrml-gKpGrjlXBN0AN4BMl-nMLKb8d1RLyicz0.webp)**Labby** 
        - 
        - # **Implement a Basic Trap Command**
        - Now, let's implement a basic `trap` command in our script to catch specific signals and exit gracefully.
            1. Add the following content to the `trap_example.sh` file:
                - ```
#!/bin/bash

cleanup_and_exit() {
  echo -e "\nSignal received! Cleaning up and exiting..."
  exit 0
}

trap cleanup_and_exit SIGINT SIGTERM

echo "This script will run until you press Ctrl+C."
echo "Press Ctrl+C to see the trap in action and exit gracefully."

count=1
while true; do
  echo "Script is running... (iteration $count)"
  sleep 1
  ((count++))
done
``` Explain Code
                - Let's break down this script:
                    - The first line `#!/bin/bash` is called a shebang. It tells the system that this script should be executed by the Bash shell.
                    - We define a `cleanup_and_exit` function that prints a message and exits the script.
                    - The `trap` command is set up to call `cleanup_and_exit` when it catches either SIGINT (interrupt) or SIGTERM (termination) signals. SIGINT is typically sent when you press Ctrl+C, while SIGTERM is often used when a process is asked to terminate gracefully.
                    - The `echo` commands print instructions for the user.
                    - The `while` loop runs indefinitely, printing a message and incrementing a counter every second.
            2. Save the file after adding the content.
        - ![](https://remnote-user-data.s3.amazonaws.com/LBl-R2EMuRb8FiE2xkS83PrXFlHwXsLmicpeTivY80GFiLCeWdTlHZaSJxSiSgwAtLhEAYKtGgU6rlNNW8NF2iXmj4qNj5vK0e5mbbVqYHGADgvTf8vxT2YWmUvCMLg_.webp)**Labby**
        - 
        - # **Make the Script Executable and Run It**
        - Before we can run our script, we need to make it executable. This tells the system that this file is allowed to be run as a program.
            1. In the terminal, make the script executable:
                - `chmod +x ~/project/trap_example.sh` Explain Code
                - The `chmod` command changes the permissions of a file. The `+x` option adds execute permission.
            2. Run the script:
                - `~/project/trap_example.sh` Explain Code
                - This command tells Bash to execute our script.
            3. The script will start running. You'll see the instructions printed on the screen. Let it run for a few seconds.
            4. Now, press Ctrl+C to interrupt it. You should see the message "Signal received!" before the script exits. This is our trap in action!
        - ![](https://remnote-user-data.s3.amazonaws.com/Z42ckqLevfZkgI_0jNyrtEoGGGJVthYWuHSHdeHOCk8RixyZLIv-D-Fvp_0SUhltE336nGl7YI7CJr8uI7YvGdmmYUOxHily640CH7zzkuV4r-KGP_XTevD1sMgzlErn.webp)**Labby**
        - 
        - # **Modify the Trap to Use a Function**
        - Instead of using a simple function, let's modify our script to use a more complex function with the `trap` command. This allows us to perform more detailed actions when a signal is received.
            1. Open the `trap_example.sh` file in the WebIDE editor.
            2. Replace the content of the file with the following:
                - ```
#!/bin/bash

cleanup_and_exit() {
  echo -e "\nSignal received! Cleaning up..."
  echo "Performing cleanup tasks..."
  # Add any necessary cleanup code here
  echo "Cleanup completed."
  echo "Exiting script gracefully."
  exit 0
}

trap cleanup_and_exit SIGINT SIGTERM

echo "This script will run until you press Ctrl+C."
echo "Press Ctrl+C to see the trap function in action and exit gracefully."

count=1
while true; do
  echo "Script is running... (iteration $count)"
  sleep 1
  ((count++))
done
``` Explain Code
                - Let's examine the changes:
                    - We've expanded the `cleanup_and_exit` function to include more detailed messages and a placeholder for cleanup tasks.
                    - The function now simulates a more realistic cleanup process, which could include tasks like closing file handles, removing temporary files, or releasing other resources.
                    - We've updated the main loop to show an iteration count, making it clearer that the script is actively running.
            3. Save the file after making these changes.
            4. Run the script again and test it by pressing Ctrl+C:
                - `~/project/trap_example.sh` Explain Code
                - You should see the new messages from the `cleanup_and_exit` function when you interrupt the script, demonstrating a graceful exit.
        - ![](https://remnote-user-data.s3.amazonaws.com/thInW-Pev-2n3DdkryPCW2cY-n95wPxt4iA0D34aJDVvxKJYweE-5PyS871aZm2lhJD7rmV6wWfZ-9bQ0C11ZrUZM0nKWidSpJqmNsTU2fHBYY-hkhzX4iF0P7MPexg6.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned how to use the `trap` command in Bash scripting. You created a script that catches specific signals and defines actions to be taken when those signals are received. You explored different ways of using the `trap` command, including using inline commands and functions.
        - The `trap` command is a powerful tool for handling interruptions and performing cleanup actions in your Bash scripts. It allows you to create more robust and user-friendly command-line applications by gracefully handling unexpected terminations and user interrupts.
        - Remember, the ability to handle signals can be crucial in many scripting scenarios, such as ensuring proper cleanup of temporary files, closing network connections, or saving state before a script exits unexpectedly.
    17. File System Operations in Shell
        - Creating a Test File
        - Testing File Existence
        - Testing Directory Existence
        - Testing File Permissions
        - 
        - # **Introduction**
        - In this lab, you will learn how to perform various file tests in the shell. File tests are essential tools for checking the properties of files and directories in the file system. By the end of this lab, you will be familiar with common file test commands and their usage, which are fundamental skills for working with files in Linux environments.
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 99% completion rate. It has received a 100% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/Fn_v0jHE9OlFy-Hf9ZsSR1LWi5qaUKbXgs3sskUk-Y-hvAQ1H1IG2skPFQJObDw25u9VYW3rCyRsVPnJzXZ4YxE0mPp3DEnFHLXCbjNln1YcbMXwrv0qgKqGk_JwQUvP.webp)**Labby** 
        - 
        - # **Creating a Test File**
        - Before we begin with file operations, it's important to understand our working environment. In Linux, you're always working within a specific directory, and it's crucial to know where you are in the file system.
            1. Open a terminal in the WebIDE. This is where you'll type your commands.
            2. Create a new file named `test_file.txt`:
                - `touch test_file.txt` Explain Code
                - The `touch` command is used to create an empty file. If the file already exists, it updates the file's timestamp without changing its content.
            3. Add some content to the file:
                - `echo "This is a test file for our lab." > test_file.txt` Explain Code
                - This command uses `echo` to output the text, and `>` to redirect that output into the file. Be careful with `>`, as it will overwrite any existing content in the file.
            4. Verify the file contents:
                - `cat test_file.txt` Explain Code
                - `cat` is short for "concatenate", but it's often used to display the contents of a file. You should see the message "This is a test file for our lab."
        - If you make a mistake or want to start over, you can always remove the file with `rm test_file.txt` and start again from step 1.
        - ![](https://remnote-user-data.s3.amazonaws.com/57PEoiJC_y30s1WVgG_-00_mul01ARKVTsIVuoKUwFPKPyC5-EYdqIT2-KajQrwUfa8__5hv3sTGDe7SPDSm5k7nfNO5MS4A2PEgtU5q8fPXGAFMhGZa9srTNPsMa0um.webp)**Labby**
        - 
        - # **Testing File Existence**
        - Now that we have created a file, let's learn how to check if a file exists. This is a common task in shell scripts, especially when you need to perform operations on files.
            1. Create a new script file named `file_exists.sh`:
                - `touch file_exists.sh` Explain Code
            2. Add the following content to the file:
                - ```
#!/bin/bash

filename="test_file.txt"
if [ -e "$filename" ]; then
  echo "$filename exists"
else
  echo "$filename does not exist"
fi
``` Explain Code
                - Let's break this down:
                    - `#!/bin/bash` is called a shebang. It tells the system this is a bash script.
                    - We set a variable `filename` to "test_file.txt".
                    - The `if` statement checks if the file exists. `-e` is a test that returns true if the file exists.
                    - We use `echo` to print a message based on whether the file exists or not.
            3. Save the file and exit the editor.
            4. Make the script executable:
                - `chmod +x file_exists.sh` Explain Code
            5. Run the script:
                - `./file_exists.sh` Explain Code
                - You should see the output: "test_file.txt exists"
            6. Now, let's test with a non-existent file. First, we'll rename our test file:
                - `mv test_file.txt non_existent.txt` Explain Code
                - This command renames `test_file.txt` to `non_existent.txt`.
            7. Modify the script to check for the original file name "test_file.txt":
                - `nano file_exists.sh` Explain Code
                - Change the `filename` variable to "test_file.txt" if it's not already set to that.
            8. Run the script again:
                - `./file_exists.sh` Explain Code
                - You should see the output: "test_file.txt does not exist"
        - This script demonstrates how to check for file existence, which is crucial when your script needs to work with files that may or may not be present.
        - ![](https://remnote-user-data.s3.amazonaws.com/ZjlPH_N9kcXmgjHIo3UTMOiUuxKPLlAMVxKFdrNPvz8md4dffRakl5MU26QZRCVhCN5jD2p6pErI9cMENSrYUMfFW1Dz6owkXaRemDN5BFsWQbuhCNEdolN-OD2P7fEz.webp)**Labby**
        - 
        - # **Testing Directory Existence**
        - Similar to testing file existence, we can also check if a directory exists. This is useful when your script needs to work with directories that may or may not be present.
            1. Create a new script file named `dir_exists.sh`:
                - `touch dir_exists.sh` Explain Code
            2. Add the following content to the file:
                - ```
#!/bin/bash

dirname="test_directory"
if [ -d "$dirname" ]; then
  echo "$dirname exists"
else
  echo "$dirname does not exist"
fi
``` Explain Code
                - This script is very similar to our file existence script, but it uses `-d` instead of `-e`. The `-d` test checks specifically for directory existence.
            3. Save the file and exit the editor.
            4. Make the script executable:
                - `chmod +x dir_exists.sh` Explain Code
            5. Run the script:
                - `./dir_exists.sh` Explain Code
                - You should see the output: "test_directory does not exist"
            6. Now, let's create the directory and run the script again:
                - ```
mkdir test_directory
./dir_exists.sh
``` Explain Code
                - You should now see the output: "test_directory exists"
                - `mkdir` is the command to create a new directory.
        - This script demonstrates how to check for directory existence. This can be particularly useful in scripts that need to create, modify, or delete directories.
        - ![](https://remnote-user-data.s3.amazonaws.com/xhU7ZPEXYmDH9fLDRSMsBQnjeMwqWZcBoEs6-neA0SjTzK_gxUo8a2JAlx0YHXRfihjXlktHElPV1RP0I2TLOpyhz35YgTaRXau84uFYf1pRUvb8HD0bNz9O4WgfVeUm.webp)**Labby**
        - 
        - # **Testing File Permissions**
        - In Linux, every file and directory has associated permissions that determine who can read, write, or execute them. In this step, we'll learn how to check file permissions, specifically if a file is readable.
            1. First, let's rename our file back to its original name:
                - `mv non_existent.txt test_file.txt` Explain Code
            2. Create a new script file named `file_readable.sh`:
                - `touch file_readable.sh` Explain Code
            3. Add the following content to the file:
                - ```
#!/bin/bash

filename="test_file.txt"
if [ -r "$filename" ]; then
  echo "You have read permission for $filename"
else
  echo "You do not have read permission for $filename"
fi
``` Explain Code
                - This script uses the `-r` test, which checks if the file is readable by the current user.
            4. Save the file and exit the editor.
            5. Make the script executable:
                - `chmod +x file_readable.sh` Explain Code
            6. Run the script:
                - `./file_readable.sh` Explain Code
                - You should see the output: "You have read permission for test_file.txt"
            7. Now, let's remove the read permission and run the script again:
                - ```
chmod -r test_file.txt
./file_readable.sh
``` Explain Code
                - You should now see the output: "You do not have read permission for test_file.txt"
                - `chmod -r` removes read permissions from the file.
            8. Restore the read permission:
                - `chmod +r test_file.txt` Explain Code
                - It's important to restore the permissions so we don't accidentally leave our file unreadable.
        - This script demonstrates how to check file permissions. Understanding and managing file permissions is crucial for system security and proper functioning of scripts.
        - ![](https://remnote-user-data.s3.amazonaws.com/Ac5ZO3awb50TUyN6wJeJpv3HX2zu9Mwm1v7EDfWFUTMacKt41m7S6yLPxVp6OVmKaDNgwQQtnOBV32IqYmLIbQzOB09vwqYguqlwyW8Reo22LqnbWGYUSqfdYEH751K_.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned how to perform essential file system operations in the shell. You created scripts to test for file and directory existence, as well as file permissions. These skills are fundamental for working with files and directories in Linux environments and form the basis for more complex shell scripting tasks.
        - You practiced:
            1. Understanding your working environment
            2. Creating and manipulating files
            3. Writing and executing shell scripts
            4. Testing for file and directory existence
            5. Checking file permissions
        - These skills will be valuable as you continue to work with Linux systems and develop more advanced shell scripts. Remember to always check file and directory existence before performing operations on them to avoid errors in your scripts. Also, be mindful of file permissions when working with sensitive data or system files.
        - As you progress, you might want to explore more advanced file tests, learn about other shell scripting constructs like loops and functions, and practice combining these concepts to create more complex and powerful scripts.
    18. File System Explorer
        - Create the File System Explorer Script
        - 
        - # **Introduction**
        - In this challenge, you'll create a simple file system explorer script that demonstrates your understanding of basic file and directory operations in shell scripting. You'll use file tests to check for existence, type, and permissions of files and directories.
        - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 98% pass rate. It has received a 99% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/slwsZizJrtWN0NTjQLo1v-h5EI--e6_IvEeUmakMoV1Mqs33ghtJxMMbdnl7UCmHhs1Onbeln3AvXPT4_V8IGcf4n8fMiT-832lDtkLiP7Tm-gFYBM-VqGfONqZQYgm2.webp)**Labby** 
        - 
        - # **Create the File System Explorer Script**
        - ## **Tasks**
            1. Navigate to the `~/project` directory where you'll find a partially completed script named `file_explorer.sh`.
            2. Open the `file_explorer.sh` file and complete the `check_item` function to explore file system items.
        - ## **Requirements**
            - The script `file_explorer.sh` is already created in the `~/project` directory with a basic structure.
            - Your task is to complete the `check_item` function:
                - It should take one parameter (the name of a file or directory).
                - It should perform the following checks and echo the results:
                    - If the item exists
                    - If it's a file or a directory
                    - If it's readable
                - Use appropriate file test operators (`-e`, `-f`, `-d`, `-r`) for each check.
            - The main part of the script (which calls the function) is already provided.
        - ## **Example**
        - Here's an example of how the completed script should work:
        - ```
$ ./file_explorer.sh test_file.txt
Checking: test_file.txt
Exists: Yes
Type: File
Readable: Yes

$ ./file_explorer.sh non_existent.txt
Checking: non_existent.txt
Exists: No

$ ./file_explorer.sh test_directory
Checking: test_directory
Exists: Yes
Type: Directory
Readable: Yes
``` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/nyAOX6mhqV94-vhaZG47f-jFe9wZqvWkRAn8IQiV5wjiV4j-YesUFJX9gpetehRJZxoqQQZZHbjqvsc9H2oE6ixZSqbzgJtWOB3ERdiuxaTAOe8c75sii2_M737aUy0L.webp)**Labby**
        - 
        - # **Summary**
        - In this challenge, you created a simple file system explorer script using shell scripting. You practiced using file test operators to check for the existence, type, and permissions of files and directories. This exercise reinforced your understanding of basic file system operations in shell scripts, demonstrating practical applications for file and directory management tasks.
-  **Build a Linux System Monitor Using Bash - **2 labs
-  **Build a Task Scheduler Using Bash - **1 labs
-  **Building Flappy Bird Using C - **1 labs
-  **Creating a Typing Game Using Bash - **1 labs
-  **Chess Board in Terminal - **1 labs
-  **Implement Custom Trash-Enabled Command - **1 labs
-  **Users and Groups Creation and Deletion Batch - **1 labs
-  **Collect Files From Specified Time - **1 labs
-  **Copy Large Files with Preserved Structure - ** 1 labs
-  **Customizing Linux File Listing** - 1 labs
-  **Extracting Information From Text** - 1 labs
-  **Extracting Link Information From Text** - 1 labs
-  **Get Program That Satisfies the Condition - **1 labs
-  **Linux Server Information Retrieval** - 1 labs
-  **Nginx Log Analysis and Optimization** - 1 labs
-  **Automated Daily System Log Backup** - 1 labs
-  **Network Data Packet Statistics** - 1 labs
-  **Random Password Generator Development** - 1 labs
-  **Searching for Specific Files** - 1 labs
-  **Samba File Sharing on Linux** - 2 labs
-  **Shell Practice Challenges** - 26 labs
- 
- others
    - git fundamentals: add. commit. status, diff
        - # **Introduction**
        - 🧑‍💻 New to Git or LabEx? We recommend starting with the [**Quick Start with Git**](https://labex.io/courses/quick-start-with-git) course.
        - This challenge will test your knowledge of basic Git commands, specifically `git add`, `git commit`, `git status`, and `git diff`. These commands are essential for version control and managing changes to your Git repository.
        - ## **Achievements**
            - `git add`: This command adds changes to the staging area, preparing them to be committed.
            - `git commit`: This command saves changes to the repository, creating a new commit with a unique ID.
            - `git status`: This command shows the current status of the repository, including which changes are staged and which are not.
            - `git diff`: This command shows the differences between two states of a file or between two different files.
        - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 100% pass rate. It has received a 100% positive review rate from learners.
        - 
        - ## **Skills Graph**
        - ![](https://remnote-user-data.s3.amazonaws.com/8ePmpK-IpjQu00zZlQFMmASukS8QybP6Aa6cwipgufOjl__50ElL6raI626dg3ayA6263bZmmsbiX53jTkE_zKyBTM7nBJsOnqip4b5mY-91Vgqi-73VArQuWQmfV--Y.webp)**Labby**
        - 
        - # **Adding Changes to the Staging Area**
        - In this step, you will learn how to use the `git add` command to stage changes to your repository.
        - ## **Target**
            - Go to the `~/myrepo` directory for operations.
            - Stage changes to a file in your repository.
            - View the status of the repository to verify that the changes have been staged.
        - ## **Result Example**
        - Suppose you have a file called `my_file.txt` in your repository, the output of the `git status` command will show that the changes to `my_file.txt` have been staged:
        - ```
Changes to be committed:
(use "git restore --staged <file>..." to unstage)
modified: my_file.txt
``` Explain Code
        - ## **Requirements**
            - A Git repository with at least one file.
            - Make changes to the file.
            - Verify that the changes have not been staged.
            - Stage the changes.
            - Verify that the changes have been staged.
        - ![](https://remnote-user-data.s3.amazonaws.com/KSt-_yBmtKfqMmAF4aXvaNo_KmQY371A8c61V1QkJdHCHHf-tgzUHlQDB4TSUcSiG7sjXL201WzjRlAsPGiz0h6Lmg4u8FloofefmT4u_K-LilIqr4KV5FkM8s6B_q60.webp)**Labby**
        - 
        - # **Committing Changes to the Repository**
        - In this step, you will learn how to use the `git commit` command to save changes to your repository. The `-m` option allows you to add a commit message that describes the changes you have made. After running this command, you can use the `git status` command to verify that the changes have been committed:
        - ## **Target**
            - Commit the changes that you staged in the previous step.
            - View the status of the repository to verify that the changes have been committed.
        - ## **Result Example**
        - The output of the `git status` command will show that your repository is up to date:
        - ```
On branch master
nothing to commit, working tree clean
``` Explain Code
        - ## **Requirements**
            - A Git repository with at least one file.
            - Make changes to the file.
            - Stage the changes.
            - Commit the changes.
            - Verify that the repository is up to date.
        - ![](https://remnote-user-data.s3.amazonaws.com/ascriu6PAaqz2qJuQy4tEbYNdp2DZ2ZB5M0M3wnZuTUydnKqhIaJONiZ0NzstR_B0EUe1TBjpg8BMGq8wMmPAHDdw2S7bkZT3jbhKEUfV-AeATY61q3Jco6rSAcdO0H4.webp)**Labby**
        - 
        - # **Checking the Status of Your Repository**
        - In this step, you will learn how to use the `git status` command to check the current status of your repository.
        - ## **Target**
            - View the status of your repository before and after making changes.
            - Understand the output of the git status command.
        - ## **Result Example**
        - Suppose you have a file called `my_file.txt` in your repository, and you have made changes to it. Before staging or committing these changes, you can use the `git status` command to view the current status of your repository. The output of this command will show that there are changes to be committed:
        - ```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   my_file.txt

no changes added to commit (use "git add" and/or "git commit -a")
``` Explain Code
        - After staging and committing the changes, you can use the `git status` command again to verify that your repository is up to date. The output of this command will show that your repository is up to date:
        - ```
On branch master
nothing to commit, working tree clean
``` Explain Code
        - ## **Requirements**
            - A Git repository with at least one file.
            - Make changes to the file.
            - View the current status of your repository before and after staging and committing the changes.
            - Understand the output of the git status command.
        - ![](https://remnote-user-data.s3.amazonaws.com/40dAv4S9I6QjQC7p-2WGkZ9XvQFZcQezCBa6NIyJlhCmWZuVxJKZrpjT1Xk0H_sX4XkE1xqNfNmSA0GRBMYvls-jGkvG-A5RPIIEm9uyVh1gKIoxBIgcOAluAeOFUzrk.webp)**Labby**
        - 
        - # **Viewing Differences Between Two States**
        - In this step, you will learn how to use the `git diff` command to view the differences between two states of a file or between two different files.
        - ## **Target**
            - Make changes to a file in your repository.
            - View the differences between the current state of the file and a previous state.
        - ## **Result Example**
        - Suppose you have a file called `my_file.txt` in your repository, and you have made changes to it. After committing the changes, you can use the `git diff` command to view the differences between the current state of the file and the previous state. The `HEAD^` argument specifies the previous commit, and `HEAD` specifies the current commit. The output of this command will show the differences between the two commits:
        - ```diff
--git a/my_file.txt b/my_file.txt
index 1234567..89abcdef 100644
--- a/my_file.txt
+++ b/my_file.txt
@@ -1,2 +1,3 @@
This is the first line.
This is the second line.
+This is the third line.
``` Explain Code
        - ## **Requirements**
            - A Git repository with at least one file.
            - Make changes to the file.
            - Commit the changes.
            - View the differences between the current state of the file and a previous state.
        - ![](https://remnote-user-data.s3.amazonaws.com/mNkRpcZpMKbjA4q5LeNNRoFJiPlhjCz1Y5JN-8lHtRvFkrBpiZ4I-AlmT8bnz-ZMKDizDtIHVFmFsXMtC1aogKWKUg9kzRdjNbIJMnMEDHu7_1TP2tJJPJmrEzVCixL3.webp)**Labby**
        - 
        - # **Summary**
        - In this challenge, you learned how to use the `git add`, `git commit`, `git status`, and `git diff` commands to manage changes to your Git repository. You learned how to stage changes, commit changes, check the status of your repository, and view differences between two states of a file or between two different files.
