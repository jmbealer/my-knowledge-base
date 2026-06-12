-  **Red Hat System Administration (RH124) Certification Labs - **14 labs
    1. Access Command Line in Red Hat Enterprise Linux
        - 
        -  **Identify User and System Time**
            - {{`whoami`}}  It prints the effective username of the current user.
            - {{`date`}} is used to display or set the system date and time. 
                - When used without any options, it displays the current date and time in a default format.
                - The output will show the current day of the week, month, day of the month, time (HH:MM:SS), time zone, and year. 
            - The `date` command is very flexible and allows you to format the output in various ways using format specifiers.
                - For example, to display only the current time in 24-hour format (HH:MM), you can use {{`+%R`}}.
                - Try displaying only the time: {{`date +%R`}} 
                    - The output will be similar to:
                    - `10:30` 
            - To display only the current date in MM/DD/YYYY format, you can use {{`+%x`}}.
            - Try displaying only the date: {{`date +%x`}} 
                - The output will be similar to:
                - `07/22/2024` 
            - Finally, you can execute multiple commands on a single line by separating them with a {{semicolon (}}{{`;`}}{{)}}. 
                - This can be useful for quickly running a sequence of commands.
            - Let's try running `whoami` and `date` on the same line: {{`whoami; date`}} 
        -  **Manage User Passwords and View File Types**
            - The {{`passwd`}} command is used to change user passwords. 
                - For the `labex` user, you will be prompted for the current password, then the new password twice. 
                - Remember, the current password for `labex` is `labex`.
            - {{`file`}} determines the type of a file. 
                - It's very useful for understanding what kind of data a file contains, especially when the file extension is missing or misleading.
            - Let's examine the type of the `/etc/passwd` file. This file contains information about all user accounts on the system.
                - `file /etc/passwd` 
            - The output will indicate that `/etc/passwd` is an ASCII text file.
            - `/etc/passwd: ASCII text` 
            - Now, let's check the type of an executable file, such as `/bin/bash`, which is the shell program you are currently using.
            - `file /bin/bash` 
            - The output will show that `/bin/bash` is an executable file, along with details about its architecture and other properties.
            - `/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=<omitted>, for GNU/Linux <omitted>, stripped` 
            - Finally, let's determine the type of a directory. We will use the `/home` directory as an example.
            - `file /home` 
            - The output will simply state that `/home` is a directory.
            - `/home: directory` 
            - These examples demonstrate how the `file` command can help you quickly identify the nature of different files and directories on your Linux system.
        -  **Inspect File Content with cat, head, and tail**
            - {{cat}} command is short for {{concatenate}} 
            - {{`cat`}} used to display the content of files. 
                - It can also be used to combine multiple files into one.
            - Let's view the entire content of the `/etc/passwd` file. This file contains user account information.
                - `cat /etc/passwd` 
            - Now, let's create two simple text files in your `~/project` directory to demonstrate `cat` with multiple files.
            - Create `file1.txt`:
                - `echo "Hello World!!" > ~/project/file1.txt` 
            - Create `file2.txt`:
                - `echo "Introduction to Linux commands." > ~/project/file2.txt` 
            - Now, use `cat` to display the content of both files:
                - `cat ~/project/file1.txt ~/project/file2.txt` 
            - {{`head`}} command displays the first few lines of a file. 
                - By default, it shows the first 10 lines.
            - Let's view the first 10 lines of `/etc/passwd`:
                - `head /etc/passwd` 
            - You can specify the number of lines to display using the {{`-n`}} option. For example, to view the first 3 lines:
                - `head -n 3 /etc/passwd` 
            - Finally, let's use the `tail` command. The 
            - {{`tail`}} command displays the last few lines of a file. 
                - By default, it also shows the last 10 lines.
            - Let's view the last 10 lines of `/etc/passwd`:
                - `tail /etc/passwd` 
            - Similar to `head`, you can specify the number of lines to display using the `-n` option. For example, to view the last 3 lines:
            - `tail -n 3 /etc/passwd` 
        -  **Count File Statistics and Use Command History**
            - {{wc}} command is short for {{word count}} 
            - {{`wc`}}  is used to count the number of lines, words, and characters in a file.
            - Let's count the lines, words, and characters in the `/etc/passwd` file:
                - `wc /etc/passwd` 
            - The output will show three numbers followed by the filename: lines, words, and characters. The exact numbers may vary slightly depending on your system configuration.
            - `41   98 2338 /etc/passwd` 
            - You can use options (wc) to display only specific counts:
                - `-l` for {{lines}} 
                - `-w` for {{words}} 
                - `-c` for {{characters}} 
            - Let's count only the lines in `/etc/passwd` and `/etc/group` (which contains information about user groups). We can do this on a single line using a semicolon.
                - ```
wc -l /etc/passwd
wc -l /etc/group
``` 
            - You will see the line counts for each file:
                - ```
41 /etc/passwd
63 /etc/group
``` 
            - Now, let's count only the characters in `/etc/group` and `/etc/hosts` (which maps hostnames to IP addresses).
            - `wc -c /etc/group /etc/hosts` 
            - The output will show the character count for each file and a total count.
            - ```
883 /etc/group
114 /etc/hosts
997 total
``` 
            - Next, we will learn about the command history. Your shell keeps a record of all commands you have executed. This is incredibly useful for re-running commands or remembering what you did previously.
            - To display your command history, use the {{`history`}} command:
            - `history` 
            - You can re-execute a command from your history using the {{exclamation point (}}{{`!`}}{{)}} followed by the command number or a string.
            - For example, to re-execute the command at number `26` (which was `file /etc/passwd` in the example above, but will be different for you), find its number in your `history` output and use it:
            - `!26 # Replace 26 with the actual number of 'file /etc/passwd' from your history` 
            - The shell will first display the command it's about to execute, then its output:
            - ```
file /etc/passwd
/etc/passwd: ASCII text
``` 
            - You can also re-execute the most recent command that starts with a specific string. For instance, to re-run the last command that started with `wc`:
            - `!wc` 
            - This will execute the last `wc` command you ran.
            - ```
wc -c /etc/group /etc/hosts
883 /etc/group
114 /etc/hosts
997 total
``` 
        -  **Practice Command Line Editing Shortcuts**
            - In this step, you will learn and practice useful command-line editing shortcuts. These shortcuts can significantly improve your efficiency when typing and modifying commands in the terminal, allowing you to navigate and edit text without constantly reaching for the mouse.
            - First, let's understand how to write a long command on multiple lines. 
                - This can improve readability for complex commands. 
                - You can use a {{backslash (}}{{`\`}}{{)}} at the end of a line to indicate that the command continues on the next line.
                - Let's try displaying the first 3 lines of two dictionary files using a multi-line command. These files are typically found on Linux systems and contain lists of words.
                    - ```
head -n 3 \
  /home/labex/project/words \
  /home/labex/project/linux.words
``` 
            - When you press Enter after the first line, your terminal will show a `>` prompt (or similar) indicating that it's waiting for the rest of the command. Type the remaining parts and press Enter again.
            - ```
==> /home/labex/project/words <==
1080
10-point
10th

==> /home/labex/project/linux.words <==
1080
10-point
10th
``` 
            - Now, let's practice some command-line editing shortcuts. These shortcuts work in most modern Linux terminals (like Bash or Zsh).
            - Type a long command, but **do not press Enter yet**:
            - `echo "This is a very long command that we will edit using shortcuts."` 
            - {{**Ctrl+A**}}: Jump to the beginning of the command line.
                - Type the command above, then press `Ctrl+A`. Your cursor will move to the beginning of the line.
            - {{**Ctrl+E**}}: Jump to the end of the command line.
                - After pressing `Ctrl+A`, press `Ctrl+E`. Your cursor will move back to the end of the line.
            - {{**Ctrl+U**}}: Clear from the cursor to the beginning of the command line.
                - Type the command again. Place your cursor somewhere in the middle of the line (e.g., after "very"). Press `Ctrl+U`. The text from the cursor to the beginning will be deleted.
            - {{**Ctrl+K**}}: Clear from the cursor to the end of the command line.
                - Type the command again. Place your cursor somewhere in the middle of the line (e.g., after "very"). Press `Ctrl+K`. The text from the cursor to the end will be deleted.
            - **Ctrl+LeftArrow** (or {{Alt+B}}): Jump to the beginning of the previous word on the command line.
                - Type the command again. Place your cursor at the end of the line. Press `Ctrl+LeftArrow` repeatedly to move word by word to the left.
            - **Ctrl+RightArrow** (or {{Alt+F}}): Jump to the end of the next word on the command line.
                - Place your cursor at the beginning of the line. Press `Ctrl+RightArrow` repeatedly to move word by word to the right.
            - {{**Ctrl+R**}}: Search the history list of commands for a pattern.
                - Press `Ctrl+R`. A `(reverse-i-search)` prompt will appear. Start typing a part of a command you previously executed, e.g., `date`. The terminal will show the most recent command from your history that matches. Keep pressing `Ctrl+R` to cycle through older matches. Press Enter to execute the found command, or Left/Right arrow to edit it.
    2. Manage Files in Red Hat Enterprise Linux
        - 
        -  **Explore Your Current Location and List Contents with** `**pwd**` **and** `**ls**`
            - {{`pwd`}} command display your current working directory  
            - {{`pwd`}} stands for "{{print working directory}}" 
            - {{`pwd`}} displays the full path name of your current location in the file system.
            - Next, you will use the 
            - {{`ls`}} command to list the contents of your current directory. 
            - {{`ls`}} stands for "{{list}}" 
            - {{`ls`}} lists directory contents for the specified directory or, if no directory is given, for the current working directory.
            - The `ls` command has several useful options to display more information about files and directories.
                - The {{`-l`}} option ({{long listing format}}) provides detailed information about each file and directory, including permissions, number of hard links, owner, group, size, and last modification time.
                    - `ls -l` Explain Cod
                - The {{`-a`}} option ({{all files}}) lists all files, including hidden files. 
                    - In Linux, file names that begin with a {{dot (}}{{`.`}}{{)}} are considered {{hidden}}. 
                    - Also, {{`.`}} refers to the {{current directory}}, and {{`..`}} refers to the {{parent directory}}.
                - Combining `-l` and `-a` as `-la` gives a long listing of all files, including hidden ones.
                    - `ls -la` 
                - The {{`-R`}} option ({{recursive}}) lists the contents of all subdirectories recursively. 
                    - Now, use `ls -R` to see the recursive listing.
                    - `ls -R` 
                        - You should see both `mydir` and `project` directories listed, followed by their contents:
        -  **Navigate Directories and Create Files with** `**cd**` **and** `**touch**`
            - {{`cd`}} command changes your shell's current working directory 
            - The `cd` command offers several convenient options for navigation:
                - {{`cd -`}}: This command changes working directory to the previous directory you were in.
                - {{`cd ..`}}: This command changes working directory to the parent directory
                - {{`cd`}} ({{without any arguments}}): This command will always take you back to your home directory, 
            - You will now use the `touch` command. The 
            - {{`touch`}} command updates the timestamp of a file to the current date and time without otherwise modifying it. 
                - This command is also very useful for creating empty files.
            - Let's create two empty files named `report.txt` and `notes.txt` in the `~/project/documents` directory.
                - `touch report.txt notes.txt` 
        -  **Organize Files and Directories with** `**mkdir**`**,** `**cp**`**,** `**mv**`**, and** `**rm**`
            - {{`mkdir`}} short for {{make directory}}.
            - {{`cp`}} short for {{copy}}.
            - {{`mv`}} short for {{move/rename}}.
            - {{`rm`}} short for {{remove}}. 
            -  {{`mkdir`}}**: Creating Directories** 
            - You can create multiple directories at once by listing them as arguments:
                - `mkdir reports presentations` 
                - Verify their creation:
                    - `ls` 
            - You should see `documents`, `presentations`, and `reports` listed.
            - The `mkdir` command's {{`-p`}} ({{parents}}) option is very useful for creating any missing parent directories for the requested destination. 
                - This prevents errors if you try to create a subdirectory within a non-existent parent directory.
            - Let's create a nested directory structure: `projects/alpha/docs`.
                - `mkdir -p projects/alpha/docs` 
                - Now, use `ls -R` to see the newly created nested structure:
                    - `ls -R projects` 
            -  {{`cp`}}**: Copying Files and Directories** 
            - The {{`cp`}} command copies files and directories. 
                - When copying a file, it creates a duplicate either in the current directory or in a different specified directory.
            - Let's copy `report.txt` from `documents` to the `reports` directory.
                - `cp documents/report.txt reports/` 
                - Verify the copy by listing the contents of the `reports` directory:
                    - `ls reports` 
                - If a file with the same name exists in the target directory, `cp` will overwrite it by default.
                - To copy a directory and its contents, you must use the {{`-r`}} ({{recursive}}) option. 
                    - By default, `cp` ignores directories if `-r` is not specified.
                - Let's copy the entire `documents` directory into `projects/alpha/`.
                    - `cp -r documents projects/alpha/` 
                    - Verify the recursive copy:
                        - `ls -R projects/alpha/documents` 
            -  {{`mv`}}**: Moving and Renaming Files and Directories** 
            - The {{`mv`}} command moves files from one location to another. 
                - It can also be used to {{rename}} files or directories. 
                - If you think of the absolute path to a file as its full name, then moving a file is effectively the same as renaming a file. 
                - The content of the files that are moved remain unchanged.
                - Let's rename `notes.txt` in the `documents` directory to `meeting_notes.txt`.
                    - `mv documents/notes.txt documents/meeting_notes.txt` 
                    - Verify the rename:
                        - `ls documents` 
                - Now, let's move `report.txt` from the `reports` directory into `documents/drafts`.
                    - `mv reports/report.txt documents/drafts/` 
                    - Verify the move:
                        - `ls reports` 
                - The {{`-v`}} option for `mv` displays a detailed output of the command operations, which can be helpful for confirmation.
                    - `mv -v documents/meeting_notes.txt documents/final_notes.txt` 
                    - You will see output like:
                        - `renamed 'documents/meeting_notes.txt' -> 'documents/final_notes.txt'` 
            -  {{`rm`}}**: Removing Files and Directories** 
            - The {{`rm`}} command removes files. 
                - Be careful with `rm`, as deleted files are typically not recoverable from the command line.
                - Now, remove `temp_file.txt`:
                    - `rm temp_file.txt` 
                    - Verify its removal:
                        - `ls` 
                - By default, {{`rm`}} does not remove directories. 
                    - If you try to remove a non-empty directory without the correct option, you will get an error.
                - To remove directories and their contents, you must use the {{`-r`}} ({{recursive}}) option. 
                    - The `rm -r` command traverses each subdirectory first and individually removes their files before removing each directory.
                - Let's remove the `presentations` directory and its contents (which is currently empty, but `-r` is still required for directories).
                    - `rm -r presentations` 
                    - Verify its removal:
                        - `ls` 
                - The {{`-i`}} option for `rm` interactively prompts for confirmation before deleting each file. 
                    - This is a good safety measure.
                    - Let's create a few more temporary files and then remove them interactively.
                        - `touch file1.txt file2.txt` 
                        - `rm -i file1.txt file2.txt` 
                - The {{`-f`}} option ({{force}}) forces the removal without prompting the user for confirmation. 
                    - If you specify both `-i` and `-f`, `-f` takes priority. **Use** `**-f**` **with extreme caution.** 
            -  {{`rmdir`}}**: Removing Empty Directories** 
            - You can also use the {{`rmdir`}} command to remove empty directories. 
                - It will fail if the directory is not empty.
                - Let's create an empty directory and remove it with `rmdir`.
                    - `mkdir empty_dir` 
                    - `rmdir empty_dir` 
                    - Verify its removal:
                        - `ls` 
            - Remember to use {{`rm -r`}} for non-empty directories.
                - `rm -r test_dir` 
        -  **Create Links Between Files with** `**ln**` **(Hard and Symbolic Links)**
            - Linux file systems support two types of links: 
                - {{hard links}} and {{symbolic (or soft) links}}. 
            - ### **Hard Links**
            - A {{hard link}} is essentially another name for an existing file. 
                - It points directly to the same data (inode) on the storage device as the original file. 
                - After a hard link is created, you cannot tell the difference between the new hard link and the original name of the file; they are equally valid ways to access the same data.
            - You can determine whether a file has multiple hard links by using the {{`ls -l`}} command. 
                - The second column in the `ls -l` output shows the number of hard links to the file.
            - Initially, `original_file.txt` has one hard link (itself):
                - `ls -l original_file.txt` 
                - You should see output similar to this, where the number `1` indicates one hard link:
                    - `-rw-rw-r--. 1 labex labex 35 Mar  7 HH:MM original_file.txt` 
            - Now, let's create a hard link to `original_file.txt` named `hard_link.txt` using the `ln` command.
                - `ln original_file.txt hard_link.txt` 
                - Check the hard link count for both files:
                    - `ls -l original_file.txt hard_link.txt` 
            - To confirm that they point to the same data, you can use the {{`ls -i`}} option to list each file's inode number. 
                - If the files are on the same file system and their inode numbers are the same, then the files are hard links that point to the same data file content.
            - `ls -i original_file.txt hard_link.txt` 
                - The inode numbers should be identical:
                    - `1234567 original_file.txt  1234567 hard_link.txt` 
            - If you modify the content of one file, the changes will be reflected in the other, because they are the same underlying data.
                - `echo "Adding new line." >> hard_link.txt` 
                - `cat original_file.txt` 
            - Even if the original file is deleted, you can still access the contents of the file provided that at least one other hard link exists. 
            - Data is deleted from storage only when the last hard link is deleted, making the file contents unreferenced by any hard link.
            - Let's remove `original_file.txt`:
                - `rm original_file.txt` 
                - Now, try to access `hard_link.txt`:
                    - `cat hard_link.txt` 
            - The hard link count for `hard_link.txt` should now be `1`:
                - `ls -l hard_link.txt` 
            - **Limitations of Hard Links:**
                - You can only use {{hard links}} with {{regular files}}. 
                    - You cannot use the {{`ln`}} command to create a hard link to a directory or special file.
                - You can use {{hard links}} only if both files are on the {{same file system}}. 
                    - You can use the {{`df`}} command to list the file systems.
            - ### **Symbolic Links**
            - A {{symbolic link}} (also called a {{"soft link" or "symlink"}}) is a special type of file that points to another file or directory by its path. 
                - It's similar to a shortcut in Windows. 
                - Unlike {{hard links, symbolic links}} do not point directly to the {{data}}; they point to the name of the target file or directory.
            - Let's create a new file named `target_file.txt` for our symbolic link.
                - `echo "This is the target file for the symbolic link." > target_file.txt` 
            - Now, create a symbolic link named `sym_link.txt` pointing to `target_file.txt` using the {{`ln -s`}} command.
                - `ln -s target_file.txt sym_link.txt` 
            - Check the details of the symbolic link using `ls -l`:
                - `ls -l target_file.txt sym_link.txt` 
            - You will notice a few differences:
                - The first character of the long listing for `sym_link.txt` is `l` (letter `l`), indicating it's a symbolic link.
                - The output shows `sym_link.txt -> target_file.txt`, explicitly showing what it points to.
                - The size of the symbolic link is very small (it's just the length of the target path), not the size of the target file.
                - The hard link count for `sym_link.txt` is `1`.
            - You can access the content of `target_file.txt` through `sym_link.txt`:
                - `cat sym_link.txt` 
            - **Key differences and behaviors of Symbolic Links:**
                - {{**Cross-filesystem linking**}}**:** Symbolic links can link two files on different file systems.
                - {{**Linking to directories**}}**:** Symbolic links can point to a directory, not just to a regular file. Let's create a symbolic link to your `documents` directory.
                    - `ln -s documents doc_shortcut` 
                    - Now, you can `cd` into `doc_shortcut` as if it were the `documents` directory itself:
                    - `cd doc_shortcut` 
                    - Verify your location. Notice that `pwd` by default shows the symbolic link path:
                    - `pwd` 
                    - Output: `/home/labex/project/doc_shortcut`
                    - If you want `pwd` to show the actual path of the directory the symbolic link points to, use the `-P` option:
                    - `pwd -P` 
                    - Output: `/home/labex/project/documents`
                    - Now, go back to `~/project`:
                    - `cd ~/project` 
                - {{**Dangling symbolic links**}}**:** When the original regular file (the target) is deleted, the symbolic link still exists but points to a missing file. This is called a "dangling symbolic link".
                    - Let's remove `target_file.txt`:
                    - `rm target_file.txt` 
                    - Now, check `sym_link.txt` with `ls -l`:
                    - `ls -l sym_link.txt` 
                    - You will see that `sym_link.txt` still exists, but its target `target_file.txt` is shown in red or a different color (depending on your terminal's configuration) to indicate it's broken:
                    - `lrwxrwxrwx. 1 labex labex 14 Mar  7 HH:MM sym_link.txt -> target_file.txt` 
                    - If you try to `cat` the dangling symbolic link, it will fail:
                    - `cat sym_link.txt` 
                    - Output:
                    - `cat: sym_link.txt: No such file or directory` 
        -  **Efficiently Select Files with Shell Expansions**
            - ### **Pattern Matching (Globbing)**
            - Pattern matching, also known as {{globbing}}, allows you to select files based on patterns using special characters called metacharacters.
            - Metacharacter - Matches - Example
                - {{`*`}} - Any string of zero or more characters. 
                    - {{`*.txt`}} matches all files ending with {{`.txt`}}.
                - {{`?`}} - Any single character. 
                    - {{`file?.txt`}} matches {{`file1.txt`}}{{, }}{{`fileA.txt`}}, etc.
                - {{`[abc...]`}} - Any one character in the enclosed class. 
                    - {{`file[12].txt`}} matches {{`file1.txt`}}{{ or }}{{`file2.txt`}}.
                - {{`[!abc...]`}} - Any one character not in the enclosed class. 
                    - {{`file[!1].txt`}} matches {{`fileA.txt`}} but not {{`file1.txt`}}.
                - {{`[[:alpha:]]`}} - Any alphabetic character.
                    - {{`file[[:alpha:]].txt`}} matches {{`fileA.txt`}}.
                - {{`[[:digit:]]`}} - Any single digit from 0 to 9.
                    - {{`file[[:digit:]].txt`}} matches {{`file1.txt`}}.
            - Let's try some examples within the `data` directory.
                1. Using `*`:  List all files ending with `.txt`:
                    - `l`{{`s data/*.txt`}} 
                        - Output:
                            - `data/file1.txt  data/file_a.txt  data/report_2023.txt` 
                    - List all files containing `file` in their name:
                        - `ls data/*file*` 
                        - Output:
                            - `data/file1.txt  data/file2.log  data/file_a.txt  data/file_b.log` 
                2. Using `?`: List files that have exactly one character before `.log`:
                    - {{`ls data/file?.log`}} 
                        - Output:
                            - `data/file2.log` 
                3. Using `[]` for character sets:
                    - List files starting with `file` and ending with `.txt` or `.log`:
                        - `l`{{`s data/file*.{txt,log}`}} 
                        - Output:
                            - `data/file1.txt  data/file2.log  data/file_a.txt  data/file_b.log` 
                    - List files that start with `report_` and have either `2023` or `2024` in their name:
                        - `ls data/report_[2][0][2][34].*` 
                        - Output:
                        - `data/report_2023.txt  data/report_2024.log` 
            - ### **Tilde Expansion** `**~**`
            - The tilde (`~`) character expands to the current user's home directory (`/home/labex`). 
                - When followed by a username, it expands to that user's home directory.
                - `echo ~` 
                    - Output:
                        - `/home/labex` 
                - `echo ~root` 
                    - Output:
                        - `/root` 
                - `echo ~/project/data` 
                    - Output:
                        - `/home/labex/project/data` 
            - ### **Brace Expansion** `**{}**`
            - {{Brace expansion}} generates arbitrary strings. 
                - It's useful for creating lists of files or directories with similar names without typing each one individually.
                1. Comma-separated list:
                    - Create files `report_jan.txt`, `report_feb.txt`, `report_mar.txt in the data directory`:
                        - {{`touch data/report_{jan,feb,mar}.txt`}} 
                    - List them:
                        - `ls data/report_*.txt` 
                2. Range of numbers or letters:
                    - Create files `doc1.txt`, `doc2.txt`, `doc3.txt`:
                        - {{`touch data/doc{1..3}.txt`}} 
                    - List them:
                        - `ls data/doc*.txt` 
                    - Output:
                        - `data/doc1.txt  data/doc2.txt  data/doc3.txt` 
                    - Create directories `chapterA`, `chapterB`, `chapterC`:
                        - {{`mkdir data/chapter{A..C}`}} 
                    - List them:
                        - `ls data/chapter*` 
                    - Output:
                        - `data/chapterA  data/chapterB  data/chapterC` 
            - ### **Variable Expansion**
            - {{Shell variables }}store values that can be expanded in commands. 
            - You define a variable using {{`VARNAME=value`}} and access its value using {{`$VARNAME`}} or {{`${VARNAME}`}}.
            - ### **Command Substitution**
            - {{Command substitution}} allows you to use the output of a command as part of another command. 
            - This is done by enclosing the command in {{`$(command)`}} or {{backticks}} ``command. The `$(command)` syntax is generally preferred as it can be nested.
            - Let's get the current date and use it in a file name.
                - `touch data/log_$(date +%Y-%m-%d).txt` 
            - List the `data` directory to see the new file:
                - `ls data/log_*.txt` 
            - Output will be similar to:
                - `data/log_2024-03-07.txt` 
            - You can also use it to count files:
                - `echo "There are $(ls data | wc -l) items in the data directory."` 
            - Output will be similar to:
                - `There are 19 items in the data directory.` 
            - ### **Protecting Arguments from Expansion**
            - Sometimes, you want to prevent the shell from expanding certain characters. You can do this using:
                1. {{**Backslash (**}}{{`\`}}{{**)**}}**:** Escapes the next single character.
                    - `echo "The value of \$HOME is your home directory."` 
                    - Output:
                    - `The value of $HOME is your home directory.` 
                2. {{**Single quotes (**}}{{`''`}}{{**)**}}**:** Prevent all shell expansion within the quotes.
                    - `echo 'The current date is $(date +%Y-%m-%d).'` 
                    - Output:
                    - `The current date is $(date +%Y-%m-%d).` 
                3. {{**Double quotes (**}}{{`""`}}{{**)**}}**:** Prevent most shell expansion, but allow variable expansion (`$VAR`) and command substitution (`$()`).
                    - ```
MY_DATE=$(date +%Y-%m-%d)
echo "Today's date is $MY_DATE."
``` 
                    - Output:
                    - `Today's date is 2024-03-07.` 
                    - Compare with single quotes:
                    - `echo 'Today is $MY_DATE.'` 
                    - Output:
                    - `Today's date is $MY_DATE.` 
    3. Get Help in Red Hat Enterprise Linux
        - Navigate man Pages
        - Search for Strings within a man Page
        - Search for man Pages by Keyword
        - Search for Keywords in Full-Text man Pages
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will master the essential skill of navigating and searching^^^ `man` ^^^pages in Red Hat Enterprise Linux. You will learn how to effectively browse through^^^ `man` ^^^pages using various navigation keys, search for specific strings within a^^^ `man` ^^^page, and discover relevant^^^ `man` ^^^pages by keyword. Furthermore, you will explore techniques for performing full-text searches across all available^^^ `man` ^^^pages to find comprehensive information.^^^
        - ^^^**Note:**^^^ ^^^LabEx provides a streamlined UBI9 (Universal Base Image 9) environment for this lab. This lightweight container image includes essential tools but has a limited set of man pages compared to a full RHEL installation. We'll use available commands like^^^ `curl``(#3594f7)`^^^,^^^ `free``(#3594f7)`^^^, and^^^ `groff``(#3594f7)` ^^^to demonstrate man page navigation techniques.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level lab with a^^^ ^^^90%^^^ ^^^completion rate. It has received a^^^ ^^^98%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Navigate man Pages**^^^
        - ^^^In this step, you will learn how to navigate through^^^ `man` ^^^pages, which are essential for understanding commands and their functionalities in Red Hat Enterprise Linux. The^^^ `man` ^^^command (short for manual) provides detailed documentation for most commands, utilities, and functions available on the system.^^^
        - ^^^**Note:**^^^ ^^^In this LabEx environment (UBI9), we'll use commands that have available man pages. While a full RHEL system would include man pages for basic commands like^^^ `ls``(#3594f7)` ^^^and^^^ `passwd``(#3594f7)`^^^, our streamlined environment focuses on available tools like^^^ `curl``(#3594f7)`^^^,^^^ `free``(#3594f7)`^^^, and^^^ `groff``(#3594f7)`^^^.^^^
        - ^^^To begin, let's view the^^^ `man` ^^^page for the^^^ `curl` ^^^command, which is used to transfer data from or to a server.^^^
        - `man curl`^^^ ^^^
        - ^^^After executing the command, you will see the^^^ `man` ^^^page for^^^ `curl`^^^. This page might be longer than your terminal screen, so you'll need to know how to navigate it.^^^
        - ^^^Here are the common navigation keys you can use within a^^^ `man` ^^^page:^^^
            - ^^^**Spacebar**^^^ ^^^or^^^ ^^^**PageDown**^^^^^^: Scroll forward (down) one full screen.^^^
            - ^^^**PageUp**^^^^^^: Scroll backward (up) one full screen.^^^
            - ^^^**DownArrow**^^^^^^: Scroll forward (down) one line.^^^
            - ^^^**UpArrow**^^^^^^: Scroll backward (up) one line.^^^
            - ^^^**D**^^^^^^: Scroll forward (down) one half-screen.^^^
            - ^^^**U**^^^^^^: Scroll backward (up) one half-screen.^^^
            - ^^^**Q**^^^^^^: Exit the^^^ `man` ^^^page and return to the command shell prompt.^^^
        - ^^^Practice navigating the^^^ `curl` ^^^man page using these keys. Try scrolling down a few screens, then back up.^^^
        - ^^^For example, press the^^^ ^^^**Spacebar**^^^ ^^^a few times to scroll down.^^^
        - ^^^Then, press^^^ ^^^**PageUp**^^^ ^^^to scroll back up.^^^
        - ^^^Finally, press^^^ ^^^**Q**^^^ ^^^to exit the^^^ `man` ^^^page.^^^
        - ```
# Press Spacebar multiple times to scroll down
``````
(#5c6370)

``````
# Press PageUp to scroll up
``````
(#5c6370)

``````
# Press Q to exit
``````
(#5c6370)
```^^^ ^^^
        - ^^^You can also go directly to the beginning or end of a^^^ `man` ^^^page:^^^
            - ^^^**G**^^^^^^: Go to the start of the^^^ `man` ^^^page.^^^
            - ^^^**Shift+G**^^^^^^: Go to the end of the^^^ `man` ^^^page.^^^
        - ^^^Let's try this with the^^^ `free` ^^^command's^^^ `man` ^^^page. The^^^ `free` ^^^command is used to display memory usage information.^^^
        - `man free`^^^ ^^^
        - ^^^Once inside the^^^ `free` ^^^man page, press^^^ ^^^**Shift+G**^^^ ^^^to jump to the end of the page.^^^
        - ^^^Then, press^^^ ^^^**G**^^^ ^^^to jump back to the beginning.^^^
        - ^^^Finally, press^^^ ^^^**Q**^^^ ^^^to exit the^^^ `man` ^^^page.^^^
        - ```
# Press Shift+G to go to the end
``````
(#5c6370)

``````
# Press G to go to the start
``````
(#5c6370)

``````
# Press Q to exit
``````
(#5c6370)
```^^^ ^^^
        - 
        - # ^^^**Search for Strings within a man Page**^^^
        - ^^^In this step, you will learn how to search for specific strings or keywords within an open^^^ `man` ^^^page. This is extremely useful when you are looking for information about a particular option or concept within a long manual page.^^^
        - ^^^To search forward (down) for a string in the^^^ `man``(#3594f7)` ^^^page, type^^^ `/``(#3594f7)` ^^^followed by the^^^ `string``(#3594f7)` ^^^you want to search for, and then press^^^ `Enter``(#3594f7)`^^^. The^^^ `man``(#3594f7)` ^^^page viewer will highlight the first occurrence of the string and jump to it.^^^
        - ^^^To repeat the previous search forward (down), press^^^ `N``(#3594f7)`^^^. To repeat the previous search backward (up), press^^^ `Shift+N``(#3594f7)`^^^.^^^
        - ^^^Let's open the^^^ `man` ^^^page for the^^^ `curl` ^^^command again.^^^
        - `man curl`^^^ ^^^
        - ^^^Now, imagine you want to find information about HTTP options. You might search for the string "HTTP".^^^
        - ^^^Inside the^^^ `man` ^^^page, type^^^ `/HTTP` ^^^and press^^^ `Enter`^^^.^^^
        - `/HTTP`^^^ ^^^
        - ^^^You should see the cursor jump to the first occurrence of "HTTP", and it might be highlighted.^^^
        - ^^^Now, press^^^ `N` ^^^to find the next occurrence of "HTTP". Press^^^ `N` ^^^a few more times to see all occurrences.^^^
        - `N`^^^ ^^^
        - ^^^To search backward, press^^^ `Shift+N`^^^. This will take you to the previous occurrence of "HTTP".^^^
        - `Shift+N`^^^ ^^^
        - ^^^When you are done searching, press^^^ `Q` ^^^to exit the^^^ `man` ^^^page.^^^
        - `Q`^^^ ^^^
        - ^^^Let's try another example with the^^^ `groff` ^^^command. This command is used for document formatting. We will search for information related to "format".^^^
        - `man groff`^^^ ^^^
        - ^^^Inside the^^^ `man` ^^^page, type^^^ `/format` ^^^and press^^^ `Enter`^^^.^^^
        - `/format`^^^ ^^^
        - ^^^Press^^^ `N` ^^^to find subsequent occurrences and^^^ `Shift+N` ^^^to go back.^^^
        - ```
N
Shift+N
```^^^ ^^^
        - ^^^When you are finished, press^^^ `Q` ^^^to exit the^^^ `man` ^^^page.^^^
        - `Q`^^^ ^^^
        - 
        - # ^^^**Search for man Pages by Keyword**^^^
        - ^^^In this step, you will learn how to search for^^^ `man` ^^^pages by keyword. This is incredibly useful when you know what you want to do (e.g., "change password") but don't know the exact command name.^^^
        - ^^^The^^^ `man -k` ^^^option (which is equivalent to the^^^ `apropos` ^^^command) allows you to search for a keyword in the^^^ `man` ^^^pages' titles and short descriptions. This will list all^^^ `man` ^^^pages that contain the specified keyword in their one-line description.^^^
        - ^^^**Note:**^^^ ^^^In LabEx's streamlined UBI9 environment, you'll see fewer results compared to a full RHEL installation. This demonstrates the concept while working within the available man pages.^^^
        - ^^^Let's say you want to find commands related to "curl". You can use^^^ `man -k curl`^^^.^^^
        - `man -k curl`^^^ ^^^
        - ^^^You will see a list of commands and their section numbers, along with a brief description. For example:^^^
        - `curl (1)             - transfer a URL``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^From this output, you can see that^^^ `curl (1)``(#3594f7)` ^^^is the command to "transfer a URL", which is the main curl command for data transfer. The number in parentheses, like^^^ `(1)``(#3594f7)`^^^, indicates the section of the^^^ `man``(#3594f7)` ^^^page.^^^
        - ^^^Let's try another example. Suppose you want to find commands related to "memory". You might search for "memory".^^^
        - `man -k memory`^^^ ^^^
        - ^^^You will get a list of^^^ `man` ^^^pages related to memory functionalities. This output can be quite short in UBI9, but it helps you discover relevant commands.^^^
        - ```
free (1)             - Display amount of free and used memory in the system
pmap (1)             - report memory map of a process
vmstat (8)           - Report virtual memory statistics
```^^^ ^^^
        - ^^^This method is a great way to explore the system's capabilities when you're not sure about the exact command name.^^^
        - 
        - # ^^^**Search for Keywords in Full-Text man Pages**^^^
        - ^^^In this final step, you will learn about a more powerful search option for^^^ `man` ^^^pages: searching for a keyword in the^^^  ^^^ *full text* ^^^^^^ ^^^ ^^^of all available^^^ `man` ^^^pages. This can be very time-consuming and resource-intensive, so it's typically used as a last resort when^^^ `man -k` ^^^(or^^^ `apropos`^^^) doesn't yield the desired results.^^^
        - ^^^The^^^ `man -K` ^^^(uppercase K) option searches for the keyword in the full-text content of all^^^ `man` ^^^pages. When a match is found,^^^ `man` ^^^will display that page and prompt you to either view it, skip to the next match, or quit the search.^^^
        - ^^^Let's try searching for the keyword "option" across all^^^ `man` ^^^pages. This might take a moment as the system scans through many files.^^^
        - `man -K option`^^^ ^^^
        - ^^^As the search progresses,^^^ `man` ^^^will stop at each page where "authentication" is found. You will see a prompt similar to this:^^^
        - `--Man-- next: some_command(section) [ view (return) | skip (Ctrl-D) | quit (Ctrl-C) ]``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
            - ^^^Press^^^ `Enter` ^^^(or^^^ `return`^^^) to view the current^^^ `man` ^^^page.^^^
            - ^^^Press^^^ `Ctrl-D` ^^^to skip the current^^^ `man` ^^^page and move to the next one that contains the keyword.^^^
            - ^^^Press^^^ `Ctrl-C` ^^^to quit the search entirely and return to the command prompt.^^^
        - ^^^For this exercise, press^^^ `Ctrl-D` ^^^a few times to skip through some pages, and then press^^^ `Ctrl-C` ^^^to quit the search. This demonstrates how to navigate the results of a full-text search without having to read every single^^^ `man` ^^^page.^^^
        - ```
# Press Ctrl-D multiple times to skip
``````
(#5c6370)

``````
# Press Ctrl-C to quit
``````
(#5c6370)
```^^^ ^^^
        - ^^^This^^^ `man -K` ^^^command is a very broad search and can be slow, especially on systems with many installed^^^ `man` ^^^pages. It's best used when you have a very specific term and^^^ `man -k` ^^^hasn't helped you find what you need.^^^
        - ^^^You have now learned various ways to get help using the^^^ `man` ^^^command, from navigating pages to searching for specific information and discovering commands by keyword. This knowledge is fundamental for effective system administration and troubleshooting in Red Hat Enterprise Linux.^^^
        - > ^^^^^**Note:**^^^^^ ^^^^^Make sure you have returned to the command prompt before clicking the^^^^^ ^^^^^**Continue**^^^^^ ^^^^^button. Otherwise, the lab will not be able to verify your operation.^^^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, you learned how to effectively navigate and search^^^ `man` ^^^pages in RHEL, which are crucial for understanding commands and their functionalities. You practiced navigating within a^^^ `man` ^^^page using keys like^^^ ^^^**Spacebar**^^^^^^,^^^ ^^^**PageUp**^^^^^^,^^^ ^^^**DownArrow**^^^^^^,^^^ ^^^**UpArrow**^^^^^^,^^^ ^^^**D**^^^^^^,^^^ ^^^**U**^^^^^^,^^^ ^^^**G**^^^^^^, and^^^ ^^^**Shift+G**^^^^^^, and exiting with^^^ ^^^**Q**^^^^^^.^^^
        - ^^^Furthermore, you gained skills in searching for specific strings within an open^^^ `man` ^^^page using^^^ `/` ^^^for forward searches and^^^ `?` ^^^for backward searches, and repeating searches with^^^ `n` ^^^and^^^ `N`^^^. You also learned how to find relevant^^^ `man` ^^^pages by keyword using^^^ `man -k` ^^^or^^^ `apropos`^^^, and how to perform full-text searches across all^^^ `man` ^^^pages for keywords using^^^ `man -K`^^^.^^^
    4. Edit Text Files in Red Hat Enterprise Linux
        - Redirect Standard Output to Files
        - Redirect Standard Error and Combine Streams
        - Construct and Understand Command Pipelines
        - Edit Text Files with Vim Basics
        - Configure and Use Shell Variables and Aliases
        - 
        - # ^^^**Introduction**^^^
            - ^^^In this lab, you will gain essential skills for managing text files and customizing your shell environment in Linux. You will learn how to redirect standard output and error streams to files, combine different streams, and construct powerful command pipelines to automate tasks.^^^
            - ^^^Furthermore, you will explore the basics of editing text files using Vim, a widely used and powerful text editor. Finally, you will learn to configure and utilize shell variables and aliases to personalize your command-line experience and enhance productivity.^^^
        - # ^^^**Redirect Standard Output to Files**^^^
        - ^^^In this step, you will learn how to redirect the standard output of commands to files. This is a fundamental skill in Linux system administration, allowing you to capture command results for later analysis, logging, or further processing.^^^
        - ^^^The shell uses special file descriptors to manage input and output. The most common ones are:^^^
            - `0`^^^: Standard Input (^^^`stdin`^^^) - Typically from the keyboard.^^^
            - `1`^^^: Standard Output (^^^`stdout`^^^) - Typically to the terminal screen.^^^
            - `2`^^^: Standard Error (^^^`stderr`^^^) - Typically to the terminal screen for error messages.^^^
        - ^^^We will focus on redirecting^^^ `stdout` ^^^in this section.^^^
        - ### ^^^**Overwriting a File with**^^^ `**>**`
        - ^^^The^^^ `>` ^^^operator redirects the standard output of a command to a specified file. If the file does not exist, it will be created. If the file already exists, its contents will be overwritten.^^^
        - ^^^Let's start by creating a simple text file with the current date and time.^^^
            1. ^^^First, ensure you are in your home directory's^^^ `project` ^^^folder.^^^
                - `cd`` ~/project`^^^ ^^^
                - `[labex@host project]$`^^^ ^^^
            2. ^^^Now, use the^^^ `date` ^^^command and redirect its output to a new file named^^^ `current_datetime.txt`^^^.^^^
                - `date`` > current_datetime.txt`^^^ ^^^
                - ^^^This command will execute^^^ `date`^^^, but instead of printing the date to your terminal, it will save it into^^^ `current_datetime.txt`^^^.^^^
            3. ^^^Verify the content of the file using the^^^ `cat` ^^^command.^^^
                - `cat`` current_datetime.txt`^^^ ^^^
                - `Mon Day XX HH:MM:SS AM/PM TimeZone YYYY`^^^ ^^^
                - ^^^The output will show the current date and time, similar to the example above.^^^
            4. ^^^Now, let's try redirecting the output of^^^ `echo` ^^^to the same file. This will overwrite the previous content.^^^
                - `echo`` ``"This is a new line of text."``(#98c379)`` > current_datetime.txt``(#a9b7c6)`^^^ ^^^
            5. ^^^Check the file content again.^^^
                - `cat`` current_datetime.txt`^^^ ^^^
                - `This is a new line of text.`^^^ ^^^
                - ^^^As you can see, the original date and time were replaced by the new line of text.^^^
        - ### ^^^**Appending to a File with**^^^ `**>>**`
        - ^^^The^^^ `>>` ^^^operator redirects the standard output of a command to a specified file, appending the new content to the end of the file. If the file does not exist, it will be created.^^^
        - ^^^Let's append more content to our^^^ `current_datetime.txt` ^^^file.^^^
            1. ^^^Append another line of text to^^^ `current_datetime.txt`^^^.^^^
                - `echo`` ``"This line is appended."``(#98c379)`` >> current_datetime.txt``(#a9b7c6)`^^^ ^^^
            2. ^^^View the file's content.^^^
                - `cat`` current_datetime.txt`^^^ ^^^
                - ```
This is a new line of text.
This line is appended.
```^^^ ^^^
                - ^^^Notice that the new line was added after the existing content.^^^
            3. ^^^Let's append the current date and time again.^^^
                - `date`` >> current_datetime.txt`^^^ ^^^
            4. ^^^Check the file content one more time.^^^
                - `cat`` current_datetime.txt`^^^ ^^^
                - ```
This is a new line of text.
This line is appended.
Mon Day XX HH:MM:SS AM/PM TimeZone YYYY
```^^^ ^^^
                - ^^^The date and time are now at the end of the file.^^^
        - ### ^^^**Redirecting Output of Other Commands**^^^
        - ^^^You can redirect the output of almost any command. Let's try redirecting the output of^^^ `ls` ^^^and^^^ `wc`^^^.^^^
            1. ^^^Redirect the output of^^^ `ls -l` ^^^(long listing format) to a file named^^^ `file_list.txt`^^^.^^^
                - `ls`` -l > file_list.txt`^^^ ^^^
            2. ^^^Inspect the content of^^^ `file_list.txt`^^^.^^^
                - `cat`` file_list.txt`^^^ ^^^
                - ```
total 4
-rw-r--r-- 1 labex labex 80 Jun  4 07:04 current_datetime.txt
-rw-r--r-- 1 labex labex  0 Jun  4 07:04 file_list.txt
```^^^ ^^^
                - ^^^This file now contains the detailed listing of files in your current directory. The exact file sizes and timestamps will vary based on when you run the commands.^^^
            3. ^^^Now, let's count the number of lines in^^^ `file_list.txt` ^^^using^^^ `wc -l` ^^^and redirect that count to another file,^^^ `line_count.txt`^^^.^^^
                - `wc`` -l file_list.txt > line_count.txt`^^^ ^^^
            4. ^^^View the content of^^^ `line_count.txt`^^^.^^^
                - `cat`` line_count.txt`^^^ ^^^
                - `3 file_list.txt`^^^ ^^^
                - ^^^The output shows that^^^ `file_list.txt` ^^^has 3 lines (including the^^^ `total` ^^^line and the two file entries).^^^
        - ^^^This concludes the first part of redirecting standard output. You've learned how to create and overwrite files using^^^ `>` ^^^and append to them using^^^ `>>`^^^.^^^
        - 
        - # ^^^**Redirect Standard Error and Combine Streams**^^^
        - ^^^In this step, you will learn how to redirect standard error (^^^`stderr``(#3594f7)`^^^) and how to combine^^^ `stdout``(#3594f7)` ^^^and^^^ `stderr``(#3594f7)` ^^^into a single stream. This is crucial for managing error messages generated by commands, allowing you to log them or discard them as needed.^^^
        - ^^^Recall that^^^ `stderr` ^^^is file descriptor^^^ `2`^^^. We use^^^ `2>` ^^^to redirect error messages.^^^
        - ### ^^^**Redirecting Standard Error to a File**^^^
        - ^^^Sometimes, commands produce error messages that you want to capture separately from their standard output.^^^
            1. ^^^Ensure you are in your^^^ `~/project` ^^^directory.^^^
                - `cd`` ~/project`^^^ ^^^
                - `[labex@host project]$`^^^ ^^^
            2. ^^^Let's try to list the contents of a non-existent directory. This will generate an error message.^^^
                - `ls`` non_existent_directory`^^^ ^^^
                - `ls: cannot access 'non_existent_directory': No such file or directory`^^^ ^^^
                - ^^^You can see the error message printed directly to the terminal.^^^
            3. ^^^Now, let's redirect this error message to a file named^^^ `errors.log`^^^.^^^
                - `ls`` non_existent_directory 2> errors.log`^^^ ^^^
                - ^^^This time, you won't see the error message on your terminal.^^^
            4. ^^^Check the content of^^^ `errors.log`^^^.^^^
                - `cat`` errors.log`^^^ ^^^
                - `ls: cannot access 'non_existent_directory': No such file or directory`^^^ ^^^
                - ^^^The error message is now stored in the file.^^^
        - ### ^^^**Discarding Standard Error**^^^
        - ^^^Often, you might want to run a command that produces noisy error messages that you don't care about. In such cases, you can redirect^^^ `stderr` ^^^to^^^ `/dev/null`^^^.^^^ `/dev/null` ^^^is a special device file that discards all data written to it.^^^
            1. ^^^Try the^^^ `ls` ^^^command with the non-existent directory again, but this time, discard the error.^^^
                - `ls`` non_existent_directory 2> /dev/null`^^^ ^^^
                - ^^^You will see no output on the terminal, and no error message is saved to a file.^^^
        - ### ^^^**Combining Standard Output and Standard Error**^^^
        - ^^^There are situations where you want to capture both^^^ `stdout` ^^^and^^^ `stderr` ^^^into the same file. This can be done in a few ways.^^^
        - ^^^**Method 1:**^^^ `**> file 2>&1**`
        - ^^^This method redirects^^^ `stdout` ^^^to a file, and then redirects^^^ `stderr` ^^^to the same location as^^^ `stdout`^^^. The order^^^ `2>&1` ^^^is important: it means "redirect file descriptor 2 (stderr) to the same place as file descriptor 1 (stdout)".^^^
            1. ^^^Let's create a command that produces both standard output and standard error. We'll use^^^ `find` ^^^to search for a file in a directory where we have permissions and in a directory where we don't.^^^
                - `find ~/project /root -name ``"current_datetime.txt"``(#98c379)`` > combined_output.log 2>&1`^^^ ^^^
                - ^^^Here,^^^ `find ~/project -name "current_datetime.txt"` ^^^will produce^^^ `stdout` ^^^(if found), and^^^ `find /root -name "current_datetime.txt"` ^^^will likely produce^^^ `stderr` ^^^due to permission issues.^^^
            2. ^^^Examine the^^^ `combined_output.log` ^^^file.^^^
                - `cat`` combined_output.log`^^^ ^^^
                - ```
/home/labex/project/current_datetime.txt
find: ‘/root’: Permission denied
```^^^ ^^^
                - ^^^You can see both the successful output (the path to the file) and the error message are captured in the same file.^^^
        - ^^^**Method 2:**^^^ `**&> file**` ^^^**(Bash specific)**^^^
        - ^^^Bash provides a shorthand for combining^^^ `stdout` ^^^and^^^ `stderr` ^^^to a file:^^^ `&>`^^^. This is equivalent to^^^ `> file 2>&1`^^^.^^^
            1. ^^^Let's try the same^^^ `find` ^^^command using the^^^ `&>` ^^^shorthand.^^^
                - `find ~/project /root -name ``"file_list.txt"``(#98c379)`` &> combined_output_shorthand.log`^^^ ^^^
            2. ^^^Check the content of^^^ `combined_output_shorthand.log`^^^.^^^
                - `cat`` combined_output_shorthand.log`^^^ ^^^
                - ```
/home/labex/project/file_list.txt
find: ‘/root’: Permission denied
```^^^ ^^^
                - ^^^The result is the same as the previous method, demonstrating the convenience of^^^ `&>`^^^.^^^
        - ### ^^^**Appending Combined Streams**^^^
        - ^^^Just like with^^^ `stdout`^^^, you can append combined^^^ `stdout` ^^^and^^^ `stderr` ^^^to a file using^^^ `>> file 2>&1` ^^^or^^^ `&>> file`^^^.^^^
            1. ^^^Append more output and errors to^^^ `combined_output.log`^^^.^^^
                - `find ~/project /root -name ``"line_count.txt"``(#98c379)`` >> combined_output.log 2>&1`^^^ ^^^
            2. ^^^View the updated^^^ `combined_output.log`^^^.^^^
                - `cat`` combined_output.log`^^^ ^^^
                - ```
/home/labex/project/current_datetime.txt
find: ‘/root’: Permission denied
/home/labex/project/line_count.txt
find: ‘/root’: Permission denied
```^^^ ^^^
                - ^^^The new output and errors are appended to the existing content.^^^
        - ^^^You have now successfully learned how to redirect standard error and how to combine standard output and standard error into a single file. This knowledge is essential for robust scripting and system administration tasks.^^^
        - 
        - # ^^^**Construct and Understand Command Pipelines**^^^
        - ^^^In this step, you will learn about command pipelines, a powerful feature in the Linux shell that allows you to chain multiple commands together. The output of one command becomes the input of the next, enabling complex data processing and manipulation.^^^
        - ^^^The pipe operator^^^ `|` ^^^(vertical bar) is used to connect commands in a pipeline. It redirects the standard output (^^^`stdout`^^^) of the command on its left to the standard input (^^^`stdin`^^^) of the command on its right.^^^
        - ### ^^^**Basic Pipelines**^^^
        - ^^^Let's start with a simple example to understand how pipelines work.^^^
            1. ^^^Ensure you are in your^^^ `~/project` ^^^directory.^^^
                - `cd`` ~/project`^^^ ^^^
                - `[labex@host project]$`^^^ ^^^
            2. ^^^First, let's list the files in the current directory.^^^
                - `ls`^^^ ^^^
                - ```
combined_output.log
combined_output_shorthand.log
current_datetime.txt
errors.log
file_list.txt
line_count.txt
```^^^ ^^^
            3. ^^^Now, let's pipe the output of^^^ `ls` ^^^to the^^^ `wc -l` ^^^command, which counts the number of lines it receives.^^^
                - `ls`` | ``wc`` -l`^^^ ^^^
                - `6`^^^ ^^^
                - ^^^The^^^ `ls` ^^^command lists the files, and its output (each file name on a new line) is fed as input to^^^ `wc -l`^^^, which then counts these lines, effectively telling you how many files/directories are in the current location.^^^
            4. ^^^Let's try another common use case: piping^^^ `ls -l` ^^^to^^^ `less` ^^^for paginated output. This is useful when a command produces too much output to fit on a single screen.^^^
                - `ls`` -l /usr/bin | less`^^^ ^^^
                - ```
total 200000
-rwxr-xr-x 1 root root 12345 Jan XX HH:MM [filename]
... (press 'q' to quit less) ...
```^^^ ^^^
                - ^^^The^^^ `ls -l /usr/bin` ^^^command lists all files in^^^ `/usr/bin` ^^^with detailed information. This output is then sent to^^^ `less`^^^, allowing you to scroll through it page by page. Press^^^ `q` ^^^to exit^^^ `less`^^^.^^^
        - ### ^^^**Filtering Output with**^^^ `**grep**`
        - ^^^The^^^ `grep` ^^^command is often used in pipelines to filter lines that match a specific pattern.^^^
            1. ^^^Let's list all processes running on the system using^^^ `ps aux` ^^^and then filter for processes related to^^^ `bash`^^^.^^^
                - `ps aux | grep bash`^^^ ^^^
                - ```
labex     1234  0.0  0.1  12345  6789 ?        Ss   HH:MM   0:00 /usr/bin/bash
labex     5678  0.0  0.0   9876  5432 pts/0    S+   HH:MM   0:00 grep bash
```^^^ ^^^
                - ^^^The^^^ `ps aux` ^^^command lists all running processes. Its output is piped to^^^ `grep bash`^^^, which then displays only the lines containing the word "bash". You might see two lines: one for your current bash shell and one for the^^^ `grep` ^^^command itself.^^^
            2. ^^^To exclude the^^^ `grep` ^^^command from the output, you can use^^^ `grep -v` ^^^(invert match) or refine your pattern. Let's try^^^ `grep -v grep`^^^.^^^
                - `ps aux | grep bash | grep -v grep`^^^ ^^^
                - `labex     1234  0.0  0.1  12345  6789 ?        Ss   HH:MM   0:00 /usr/bin/bash`^^^ ^^^
                - ^^^Now, only the actual bash process is shown.^^^
        - ### ^^^**Using**^^^ `**sort**` ^^^**and**^^^ `**uniq**`
        - `sort` ^^^is used to sort lines of text, and^^^ `uniq` ^^^is used to report or omit repeated lines. They are often used together.^^^
            1. ^^^Let's create a file with some unsorted, repeated words.^^^
                - `echo`` -e ``"apple\nbanana\napple\norange\nbanana"``(#98c379)`` > fruits.txt`^^^ ^^^
            2. ^^^View the content of^^^ `fruits.txt`^^^.^^^
                - `cat`` fruits.txt`^^^ ^^^
                - ```
apple
banana
apple
orange
banana
```^^^ ^^^
            3. ^^^Now, let's sort the lines in^^^ `fruits.txt`^^^.^^^
                - `cat`` fruits.txt | ``sort`^^^ ^^^
                - ```
apple
apple
banana
banana
orange
```^^^ ^^^
            4. ^^^To get only the unique sorted words, pipe the output of^^^ `sort` ^^^to^^^ `uniq`^^^.^^^
                - `cat`` fruits.txt | ``sort`` | ``uniq`^^^ ^^^
                - ```
apple
banana
orange
```^^^ ^^^
                - ^^^This pipeline first sorts the lines, then^^^ `uniq` ^^^removes duplicate adjacent lines.^^^
        - ### ^^^**The**^^^ `**tee**` ^^^**Command**^^^
        - ^^^The^^^ `tee` ^^^command is special in pipelines. It reads standard input, writes it to standard output, and simultaneously writes it to one or more files. It's like a "T" junction in a pipe, allowing data to flow in two directions.^^^
            1. ^^^Let's list the files and save the output to^^^ `ls_output.txt` ^^^while also displaying it on the screen.^^^
                - `ls`` -l | ``tee`` ls_output.txt`^^^ ^^^
                - ```
total 24
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM combined_output.log
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM combined_output_shorthand.log
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM current_datetime.txt
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM errors.log
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM file_list.txt
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM fruits.txt
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM line_count.txt
-rw-r--r-- 1 labex labex 0 Jan XX HH:MM ls_output.txt
```^^^ ^^^
                - ^^^You will see the^^^ `ls -l` ^^^output on your terminal, and a file named^^^ `ls_output.txt` ^^^will be created with the same content.^^^
            2. ^^^Verify the content of^^^ `ls_output.txt`^^^.^^^
                - `cat`` ls_output.txt`^^^ ^^^
                - ```
total 24
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM combined_output.log
... (same as above) ...
```^^^ ^^^
            3. ^^^You can also use^^^ `tee -a` ^^^to append the output to a file.^^^
                - `echo`` ``"--- End of list ---"``(#98c379)`` | ``(#a9b7c6)``tee`` -a ls_output.txt``(#a9b7c6)`^^^ ^^^
                - `--- End of list ---`^^^ ^^^
                - ^^^The line "--- End of list ---" is printed to the terminal and appended to^^^ `ls_output.txt`^^^.^^^
            4. ^^^Check the updated^^^ `ls_output.txt`^^^.^^^
                - `cat`` ls_output.txt`^^^ ^^^
                - ```
total 24
... (previous ls -l output) ...
--- End of list ---
```^^^ ^^^
        - ^^^Pipelines are incredibly versatile and form the backbone of many powerful shell scripts and one-liner commands. By combining simple commands, you can perform complex data transformations efficiently.^^^
        - 
        - # ^^^**Edit Text Files with Vim Basics**^^^
        - ^^^In this step, you will learn the fundamental operations of Vim, a powerful and widely used text editor in the Linux environment. Vim operates in different modes, which can be a bit challenging for beginners, but mastering the basics will significantly boost your productivity.^^^
        - ^^^Vim is a modal editor, meaning it has different modes for different tasks:^^^
            - ^^^**Normal Mode (Command Mode)**^^^^^^: This is the default mode when you open Vim. In this mode, keystrokes are interpreted as commands (e.g., moving the cursor, deleting text, copying text).^^^
            - ^^^**Insert Mode**^^^^^^: In this mode, anything you type is inserted into the file. You enter Insert Mode from Normal Mode by pressing^^^ `i` ^^^(insert at cursor),^^^ `a` ^^^(append after cursor),^^^ `o` ^^^(open new line below), etc. To return to Normal Mode, press^^^ `Esc`^^^.^^^
            - ^^^**Visual Mode**^^^^^^: This mode allows you to select blocks of text for operations like copying, cutting, or deleting. You enter Visual Mode from Normal Mode by pressing^^^ `v` ^^^(character-wise),^^^ `Shift+V` ^^^(line-wise), or^^^ `Ctrl+V` ^^^(block-wise). Press^^^ `Esc` ^^^to return to Normal Mode.^^^
            - ^^^**Command-Line Mode (Ex Mode)**^^^^^^: This mode is used for executing commands that typically start with a colon (^^^`:``(#3594f7)`^^^), such as saving (^^^`:w``(#3594f7)`^^^), quitting (^^^`:q``(#3594f7)`^^^), or searching (^^^`/``(#3594f7)`^^^). You enter this mode from Normal Mode by pressing^^^ `:``(#3594f7)`^^^.^^^
        - ### ^^^**Opening and Basic Navigation**^^^
            1. ^^^Ensure you are in your^^^ `~/project` ^^^directory.^^^
                - `cd`` ~/project`^^^ ^^^
                - `[labex@host project]$`^^^ ^^^
            2. ^^^Open a new file named^^^ `my_document.txt` ^^^using^^^ `vim`^^^.^^^
                - `vim my_document.txt`^^^ ^^^
                - ^^^Your terminal will now display the Vim interface. You are in^^^ ^^^**Normal Mode**^^^^^^.^^^
            3. ^^^In Normal Mode, you can navigate using the arrow keys or^^^ `h` ^^^(left),^^^ `j` ^^^(down),^^^ `k` ^^^(up),^^^ `l` ^^^(right). Since the file is empty, there's not much to navigate yet.^^^
        - ### ^^^**Insert Mode: Adding Text**^^^
            1. ^^^To start typing, you need to enter^^^ ^^^**Insert Mode**^^^^^^. Press^^^ `i` ^^^(for insert).^^^
                - 
                - ^^^You should see^^^ `-- INSERT --` ^^^at the bottom left of your terminal, indicating you are in Insert Mode.^^^
            2. ^^^Type the following lines:^^^
                - ```
This 
``````
is
``````
(#c678dd) the first line.
This 
``````
is
``````
(#c678dd) the second line.
This 
``````
is
``````
(#c678dd) the third line.
```^^^ ^^^
            3. ^^^To exit Insert Mode and return to Normal Mode, press the^^^ `Esc` ^^^key.^^^
                - 
                - ^^^The^^^ `-- INSERT --` ^^^indicator should disappear.^^^
        - ### ^^^**Saving and Quitting**^^^
            1. ^^^In Normal Mode, to save the file, type^^^ `:w` ^^^and press^^^ `Enter`^^^.^^^
                - `:w``(#61aeee)``(#1a1a1a)`^^^ ^^^
                - ^^^You should see^^^ `my_document.txt` ^^^[New]^^^ `3L, 60B written` ^^^at the bottom, confirming the save.^^^
            2. ^^^To quit Vim, type^^^ `:q` ^^^and press^^^ `Enter`^^^.^^^
                - `:``q``(#e06c75)`^^^ ^^^
                - ^^^You will be returned to your shell prompt.^^^
            3. ^^^Verify the content of^^^ `my_document.txt` ^^^using^^^ `cat`^^^.^^^
                - `cat`` my_document.txt`^^^ ^^^
                - ```
This is the first line.
This is the second line.
This is the third line.
```^^^ ^^^
        - ### ^^^**Editing Existing Files**^^^
            1. ^^^Open^^^ `my_document.txt` ^^^again.^^^
                - `vim my_document.txt`^^^ ^^^
            2. ^^^In Normal Mode, move your cursor to the beginning of the second line (using^^^ `j``(#3594f7)` ^^^or arrow keys).^^^
            3. ^^^Press^^^ `Shift+V` ^^^to enter^^^ ^^^**Visual Line Mode**^^^^^^. The entire second line will be highlighted.^^^
            4. ^^^Press^^^ `y` ^^^to "yank" (copy) the selected line.^^^
            5. ^^^Move your cursor to the end of the third line (using^^^ `j``(#3594f7)` ^^^or arrow keys).^^^
            6. ^^^Press^^^ `p` ^^^to "put" (paste) the yanked line below the current line.^^^
                - 
                - ^^^The second line will now appear again as the fourth line.^^^
            7. ^^^Now, let's delete a line. Move your cursor to the fourth line (the one you just pasted).^^^
            8. ^^^Press^^^ `dd` ^^^(double^^^ `d`^^^) to delete the entire line.^^^
            9. ^^^To undo your last change, press^^^ `u`^^^. The deleted line will reappear.^^^
            10. ^^^To save and quit in one command, type^^^ `:wq` ^^^and press^^^ `Enter`^^^.^^^
                - `:wq``(#61aeee)``(#1a1a1a)`^^^ ^^^
            11. ^^^Verify the content of^^^ `my_document.txt` ^^^again.^^^
                - `cat`` my_document.txt`^^^ ^^^
                - ```
This is the first line.
This is the second line.
This is the third line.
This is the second line.
```^^^ ^^^
                - ^^^The file should now have four lines, with the second line duplicated.^^^
        - ### ^^^**Discarding Changes**^^^
        - ^^^Sometimes you make changes and decide you don't want to save them.^^^
            1. ^^^Open^^^ `my_document.txt` ^^^again.^^^
                - `vim my_document.txt`^^^ ^^^
            2. ^^^Enter Insert Mode by pressing^^^ `i`^^^.^^^
            3. ^^^Add a new line at the end:^^^
                - `This line should not be saved.`^^^ ^^^
            4. ^^^Press^^^ `Esc` ^^^to return to Normal Mode.^^^
            5. ^^^Try to quit using^^^ `:q`^^^.^^^
                - `:``q``(#e06c75)`^^^ ^^^
                - ^^^Vim will warn you:^^^ `E37: No write since last change (add ! to override)``(#3594f7)`^^^. This means you have unsaved changes.^^^
            6. ^^^To quit without saving, type^^^ `:q!` ^^^and press^^^ `Enter`^^^.^^^
                - `:``q``(#e06c75)``!`^^^ ^^^
                - ^^^You will be returned to the shell prompt, and your changes will be discarded.^^^
            7. ^^^Verify the content of^^^ `my_document.txt`^^^.^^^
                - `cat`` my_document.txt`^^^ ^^^
                - ```
This is the first line.
This is the second line.
This is the third line.
This is the second line.
```^^^ ^^^
                - ^^^The last line you added should not be present.^^^
        - ^^^You have now covered the very basic operations in Vim: opening files, inserting text, navigating, saving, quitting, and discarding changes. These are the essential skills to get started with Vim.^^^
        - 
        - # ^^^**Configure and Use Shell Variables and Aliases**^^^
        - ^^^In this step, you will learn how to configure and use shell variables and aliases. These are powerful features that allow you to customize your shell environment, store data, and create shortcuts for frequently used commands, significantly improving your command-line efficiency.^^^
        - ### ^^^**Shell Variables**^^^
        - ^^^Shell variables are named entities that store data. They can store numbers, text, or other data that can be used by the shell or by programs executed within the shell.^^^
            1. ^^^Ensure you are in your^^^ `~/project` ^^^directory.^^^
                - `cd`` ~/project`^^^ ^^^
                - `[labex@host project]$`^^^ ^^^
            2. ^^^**Setting a Local Variable**^^^^^^: Let's create a simple variable named^^^ `MY_MESSAGE`^^^.^^^
                - `MY_MESSAGE=``"Hello, LabEx!"``(#98c379)`^^^ ^^^
                - ^^^Note that there are no spaces around the^^^ `=` ^^^sign.^^^
            3. ^^^**Accessing a Variable**^^^^^^: To access the value of a variable, you prepend its name with a^^^ `$` ^^^sign.^^^
                - `echo`` ``$MY_MESSAGE``(#d19a66)`^^^ ^^^
                - `Hello, LabEx!`^^^ ^^^
            4. ^^^**Variable Expansion with Braces**^^^^^^: Sometimes, you need to clearly delimit the variable name, especially when it's followed by other characters. Use curly braces^^^ `{}` ^^^for this.^^^
                - `echo`` ``"The message is: ``(#98c379)``${MY_MESSAGE}``(#d19a66)``."``(#98c379)`^^^ ^^^
                - `The message is: Hello, LabEx!.`^^^ ^^^
                - ^^^If you omit the braces, the shell might interpret^^^ `MY_MESSAGE.` ^^^as the variable name, which doesn't exist.^^^
            5. ^^^**Listing All Set Variables**^^^^^^: You can use the^^^ `set` ^^^command to list all currently set shell variables and functions. This output can be very long, so it's often piped to^^^ `less`^^^.^^^
                - `set`` | less`^^^ ^^^
                - ```
BASH=/usr/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:histappend:interactive_comments:progcomp:promptvars:sourcepath
... (press 'q' to quit less) ...
```^^^ ^^^
                - ^^^Press^^^ `q` ^^^to exit^^^ `less`^^^.^^^
            6. ^^^**Unsetting a Variable**^^^^^^: To remove a variable, use the^^^ `unset` ^^^command.^^^
                - `unset`` MY_MESSAGE`^^^ ^^^
            7. ^^^Verify that the variable is no longer set.^^^
                - `echo`` ``$MY_MESSAGE``(#d19a66)`^^^ ^^^
                - ``^^^ ^^^
                - ^^^You should see an empty line, indicating the variable is unset.^^^
        - ### ^^^**Environment Variables**^^^
        - ^^^Environment variables are a special type of shell variable that are inherited by child processes. This means that any program or script launched from your current shell will have access to these variables. They are typically used to configure the environment for applications.^^^
            1. ^^^**Setting an Environment Variable**^^^^^^: Use the^^^ `export` ^^^command to make a variable an environment variable.^^^
                - `export`` EDITOR=vim`^^^ ^^^
                - ^^^This sets the^^^ `EDITOR` ^^^environment variable, which many programs use to determine your preferred text editor.^^^
            2. ^^^**Listing Environment Variables**^^^^^^: Use the^^^ `env` ^^^command to list only the environment variables.^^^
                - `env`` | grep EDITOR`^^^ ^^^
                - `EDITOR=vim`^^^ ^^^
            3. ^^^**Unexporting a Variable**^^^^^^: You can unexport a variable without unsetting it using^^^ `export -n`^^^. This makes it a local variable again.^^^
                - `export`` -n EDITOR`^^^ ^^^
            4. ^^^Verify it's no longer an environment variable.^^^
                - `env`` | grep EDITOR`^^^ ^^^
                - ``^^^ ^^^
                - ^^^You should see no output. However, it's still a local variable:^^^
                - `echo`` ``$EDITOR``(#d19a66)`^^^ ^^^
                - `vim`^^^ ^^^
            5. ^^^To completely remove it, use^^^ `unset`^^^.^^^
                - `unset`` EDITOR`^^^ ^^^
        - ### ^^^**Shell Aliases**^^^
        - ^^^Aliases are shortcuts for commands. They allow you to define a new command that expands to a longer command or a sequence of commands. This is very useful for frequently used commands with many options.^^^
            1. ^^^**Creating an Alias**^^^^^^: Let's create an alias for^^^ `ls -l` ^^^to make it shorter.^^^
                - `alias`` ll=``'ls -l'``(#98c379)`^^^ ^^^
                - ^^^Note the single quotes around the command to ensure it's treated as a single string.^^^
            2. ^^^**Using an Alias**^^^^^^: Now, you can simply type^^^ `ll` ^^^instead of^^^ `ls -l`^^^.^^^
                - `ll`^^^ ^^^
                - ```
total 24
-rw-r--r-- 1 labex labex 123 Jan XX HH:MM combined_output.log
... (output of ls -l) ...
```^^^ ^^^
            3. ^^^**Listing Aliases**^^^^^^: Use the^^^ `alias` ^^^command without any arguments to see all defined aliases.^^^
                - `alias`^^^ ^^^
                - `alias ll='ls -l'`^^^ ^^^
                - ^^^You might see other default aliases depending on your shell configuration.^^^
            4. ^^^**Creating a More Complex Alias**^^^^^^: You can also create aliases for commands with arguments or multiple commands.^^^
                - `alias`` myip=``'ip a | grep "inet " | grep -v "127.0.0.1" | awk "{print \$2}" | cut -d/ -f1'``(#98c379)`^^^ ^^^
                - ^^^Here,^^^ `myip` ^^^will show your primary IP address. Note the^^^ `\$2` ^^^to escape the^^^ `$` ^^^sign so it's passed to^^^ `awk` ^^^and not interpreted by the shell when the alias is defined.^^^
            5. ^^^Test the^^^ `myip` ^^^alias.^^^
                - `myip`^^^ ^^^
                - `172.17.0.2`^^^ ^^^
                - ^^^(Your IP address may vary)^^^
            6. ^^^**Unsetting an Alias**^^^^^^: To remove an alias, use the^^^ `unalias` ^^^command.^^^
                - `unalias`` ll`^^^ ^^^
            7. ^^^Verify that the alias is removed.^^^
                - `alias`^^^ ^^^
                - `alias myip='ip a | grep "inet " | grep -v "127.0.0.1" | awk "{print \$2}" | cut -d/ -f1'`^^^ ^^^
                - `ll` ^^^should no longer be in the list.^^^
        - ^^^Shell variables and aliases are temporary and will be lost when you close your terminal session. To make them permanent, you need to add them to your shell's configuration files (e.g.,^^^ `~/.bashrc``(#3594f7)` ^^^or^^^ `~/.profile``(#3594f7)`^^^), which will be covered in more advanced topics.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, you learned fundamental Linux command-line skills essential for managing text files and the shell environment. You began by mastering output redirection, specifically using^^^ `>` ^^^to overwrite files and^^^ `>>` ^^^to append content, allowing you to capture command results for logging or further processing. You also explored redirecting standard error (^^^`2>`^^^) and combining standard output and error (^^^`&>`^^^) to manage all command output effectively.^^^
        - ^^^Furthermore, you gained proficiency in constructing and understanding command pipelines using the^^^ `|` ^^^operator, enabling you to chain commands and process data sequentially. You were introduced to basic text editing with Vim, covering essential commands for inserting, saving, and quitting files. Finally, you learned how to configure and use shell variables for storing data and creating aliases to simplify frequently used commands, enhancing your command-line efficiency and customization.^^^
    5. Manage Users and Groups in Red Hat Enterprise Linux
        - Understand User and Group Concepts
        - Gain Superuser Access
        - Create and Modify Local User Accounts
        - Manage Local Group Accounts
        - Configure User Password Policies
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain essential skills in managing local users and groups within a Red Hat Enterprise Linux (RHEL) environment. You will begin by understanding fundamental user and group concepts, including how to identify user and group information and file ownership.^^^
        - ^^^Subsequently, you will learn how to obtain superuser access, create and modify local user accounts, manage local group accounts, and configure user password policies. This hands-on experience will equip you with the knowledge to effectively control access and permissions on your Linux system.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level lab with a^^^ ^^^84%^^^ ^^^completion rate. It has received a^^^ ^^^100%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Understand User and Group Concepts**^^^
        - ^^^In this step, you will learn about fundamental user and group concepts in Red Hat Enterprise Linux (RHEL) and how to use various commands to inspect user and group information. Understanding these concepts is crucial for managing permissions and access control on a Linux system.^^^
        - ^^^Every file and process on a Linux system is associated with a user and a group. This association determines who can read, write, or execute files, and who can manage processes.^^^
        - ^^^First, let's explore how to identify the current user and other users on the system using the^^^ `id` ^^^command.^^^
            - ^^^Use the^^^ `id` ^^^command to show information about the currently logged-in user. This command displays the user ID (UID), primary group ID (GID), and all groups the user belongs to.^^^
                - `id`^^^ ^^^
                - ^^^You should see output similar to this, indicating your^^^ `labex` ^^^user information:^^^
                - `uid=1000(labex) gid=1000(labex) groups=1000(labex),10(wheel) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
            - ^^^To view basic information about another user, such as the^^^ `root` ^^^user, pass the username to the^^^ `id` ^^^command as an argument.^^^
                - `id`` root`^^^ ^^^
                - ^^^The output will show the^^^ `root` ^^^user's UID (0), GID (0), and groups:^^^
                - `uid=0(root) gid=0(root) groups=0(root) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^Next, you will learn how to identify the owner of files and directories using the^^^ `ls` ^^^command.^^^
            - ^^^Use the^^^ `ls -l` ^^^command to view the owner of a file. First, create a dummy file in your^^^ `~/project` ^^^directory.^^^
                - ```
touch
``````
 ~/project/mytextfile.txt

``````
ls
``````
 -l ~/project/mytextfile.txt
```^^^ ^^^
                - ^^^The output will show^^^ `labex` ^^^as both the user and group owner of^^^ `mytextfile.txt`^^^:^^^
                - `-rw-r--r-- 1 labex labex 0 Feb  5 11:10 /home/labex/project/mytextfile.txt`^^^ ^^^
            - ^^^Use the^^^ `ls -ld` ^^^command to view the owner of a directory, rather than the contents of that directory. In the following output, the third column shows the username and the fourth column shows the group name.^^^
                - `ls`` -ld ~/project`^^^ ^^^
                - ^^^You will see^^^ `labex` ^^^as the owner of your^^^ `~/project` ^^^directory:^^^
                - `drwxr-xr-x 2 labex labex 6 Feb  5 11:10 /home/labex/project`^^^ ^^^
        - ^^^Now, let's examine how to view process information and the user associated with each process using the^^^ `ps` ^^^command.^^^
            - ^^^Use the^^^ `ps -au` ^^^command to view processes. The^^^ `a` ^^^option shows all processes with a terminal, and the^^^ `u` ^^^option displays the user that is associated with a process. In the following output, the first column shows the username.^^^
                - `ps -au`^^^ ^^^
                - ^^^You will see various processes, with^^^ `labex` ^^^and^^^ `root` ^^^as common users:^^^
                - ```
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  10608  3808 ?        Ss   00:00   0:00 /sbin/init
root        42  0.0  0.0  10608  3808 ?        Ss   00:00   0:00 /sbin/init
labex      123  0.0  0.1 224152  5756 pts/0    Ss   00:00   0:00 -bash
labex      150  0.0  0.0 225556  3652 pts/0    R+   00:00   0:00 ps -au
```^^^ ^^^
        - ^^^Finally, you will explore the^^^ `/etc/passwd` ^^^and^^^ `/etc/group` ^^^files, which store user and group information, respectively. These files are critical for understanding how user and group accounts are defined on a Linux system.^^^
            - ^^^Each line in the^^^ `/etc/passwd` ^^^file contains information about one user. The file is divided into seven colon-separated fields. Use^^^ `cat` ^^^to view its contents.^^^
                - `cat`` /etc/passwd`^^^ ^^^
                - ^^^Locate the entry for^^^ `labex` ^^^and^^^ `root`^^^. For^^^ `labex`^^^, it should look similar to this:^^^
                - `labex:x:1000:1000:LabEx User:/home/labex:/bin/bash`^^^ ^^^
                - ^^^Let's break down each field:^^^
                    - `labex`^^^: The username for this user.^^^
                    - `x`^^^: The user's encrypted password was historically stored here; this is now a placeholder, as passwords are stored in^^^ `/etc/shadow` ^^^for security.^^^
                    - `1000`^^^: The UID number for this user account.^^^
                    - `1000`^^^: The GID number for this user account's primary group.^^^
                    - `LabEx User`^^^: A brief comment, description, or the real name for this user.^^^
                    - `/home/labex`^^^: The user's home directory, and the initial working directory when the login shell starts.^^^
                    - `/bin/bash`^^^: The default shell program for this user that runs at login.^^^
            - ^^^Each line in the^^^ `/etc/group` ^^^file contains information about one group. Each group entry is divided into four colon-separated fields. Use^^^ `cat` ^^^to view its contents.^^^
                - `cat`` /etc/group`^^^ ^^^
                - ^^^You will see entries for various system groups and user-private groups. For example, the^^^ `labex` ^^^group entry might look like this:^^^
                - `labex:x:1000:`^^^ ^^^
                - ^^^Let's break down each field:^^^
                    - `labex`^^^: Name for this group.^^^
                    - `x`^^^: Obsolete group password field; this is now a placeholder.^^^
                    - `1000`^^^: The GID number for this group.^^^
                    - ^^^(empty): A list of users that are members of this group as a secondary group. If this field is empty, it means no additional users are explicitly listed as secondary members of this group (though the primary user^^^ `labex``(#3594f7)` ^^^is implicitly a member).^^^
                - ^^^**Primary Groups and Secondary Groups:**^^^
                - 
                - ^^^Every user has exactly one primary group. For local users, this group is listed by GID in the^^^ `/etc/passwd` ^^^file. The primary group owns files that the user creates. When creating a regular user, a group is often created with the same name as the user, to be the primary group for the user. The user is typically the only member of this^^^  ^^^ *User Private Group* ^^^^^^ ^^^^^^. This design simplifies file permission management.^^^
                - ^^^Users might also have secondary groups. Membership in secondary groups is stored in the^^^ `/etc/group` ^^^file. Users are granted access to files based on whether any of their groups have access, regardless of whether the groups are primary or secondary. For example, if the^^^ `labex` ^^^user has a^^^ `labex` ^^^primary group and^^^ `wheel` ^^^as a secondary group, then that user can read files that any of those two groups can read.^^^
                - ^^^The^^^ `id` ^^^command can show all group memberships for a user. Recall the output of^^^ `id` ^^^for^^^ `labex`^^^:^^^
                - `uid=1000(labex) gid=1000(labex) groups=1000(labex),10(wheel) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
                - ^^^Here,^^^ `gid=1000(labex)``(#3594f7)` ^^^indicates^^^ `labex``(#3594f7)` ^^^is the primary group.^^^ `groups=1000(labex),10(wheel)``(#3594f7)` ^^^lists all group memberships, showing^^^ `labex``(#3594f7)` ^^^as the primary group and^^^ `wheel``(#3594f7)` ^^^as a secondary group.^^^
        - 
        - # ^^^**Gain Superuser Access**^^^
        - ^^^In this step, you will learn how to gain superuser access (root privileges) on a RHEL system. Superuser access is essential for performing administrative tasks such as installing software, managing users, and configuring system settings. You will explore the^^^ `su``(#3594f7)` ^^^and^^^ `sudo``(#3594f7)` ^^^commands, which are the primary tools for privilege escalation.^^^
        - ^^^The^^^ `su` ^^^(substitute user) command allows you to switch to another user account. When used without a username, it defaults to the^^^ `root` ^^^user.^^^
            - ^^^Use the^^^ `su -` ^^^command to switch to the^^^ `root` ^^^user. The hyphen (^^^`-`^^^) option ensures that you get a login shell, which means the^^^ `root` ^^^user's environment variables and path will be loaded. You will be prompted for the^^^ `root` ^^^password, which is^^^ `redhat`^^^.^^^
                - `su -`^^^ ^^^
                - ^^^After entering the password^^^ `redhat`^^^, your prompt will change to^^^ `[root@host ~]#`^^^, indicating you are now the^^^ `root` ^^^user.^^^
                - ```
Password:
[root@host ~]#
```^^^ ^^^
                - ^^^To verify you are^^^ `root`^^^, you can run the^^^ `whoami` ^^^command:^^^
                - `whoami`^^^ ^^^
                - ^^^The output should be:^^^
                - `root`^^^ ^^^
                - ^^^To exit the^^^ `root` ^^^shell and return to your^^^ `labex` ^^^user, type^^^ `exit`^^^.^^^
                - `exit`^^^ ^^^
                - ^^^Your prompt will return to^^^ `[labex@host ~]$`^^^.^^^
        - ^^^The^^^ `sudo` ^^^(superuser do) command allows a permitted user to execute a command as the superuser or another user, as specified by the^^^ `sudoers` ^^^file. The^^^ `labex` ^^^user is configured to have^^^ `sudo` ^^^privileges without requiring a password, which is common in many cloud and lab environments.^^^
            - ^^^Use the^^^ `sudo -i` ^^^command to switch to the^^^ `root` ^^^account. This command is generally preferred over^^^ `su -` ^^^because it provides a more secure way to run commands with elevated privileges. When you use^^^ `sudo -i`^^^, you are still using your own user account but with root privileges, and commands are logged to your account, making it easier to track what was done.^^^
                - `sudo -i`^^^ ^^^
                - ^^^Your prompt will change to^^^ `[root@host ~]#`^^^, indicating you are now the^^^ `root` ^^^user.^^^
                - `[root@host ~]#`^^^ ^^^
                - ^^^Again, you can verify with^^^ `whoami`^^^:^^^
                - `whoami`^^^ ^^^
                - ^^^The output should be:^^^
                - `root`^^^ ^^^
                - ^^^To exit the^^^ `root` ^^^shell and return to your^^^ `labex` ^^^user, type^^^ `exit`^^^.^^^
                - `exit`^^^ ^^^
                - ^^^Your prompt will return to^^^ `[labex@host ~]$`^^^.^^^
            - ^^^You can also use^^^ `sudo` ^^^to run a single command with root privileges without switching to the^^^ `root` ^^^shell. For example, to view the contents of^^^ `/etc/shadow` ^^^(which is only readable by^^^ `root`^^^), you can use^^^ `sudo cat /etc/shadow`^^^.^^^
                - `sudo ``cat`` /etc/shadow | ``head`` -n 3`^^^ ^^^
                - ^^^This will display the first three lines of the^^^ `/etc/shadow` ^^^file, demonstrating that the^^^ `cat` ^^^command was executed with root privileges.^^^
                - ```
root:*:19780:0:99999:7:::
bin:*:19780:0:99999:7:::
daemon:*:19780:0:99999:7:::
```^^^ ^^^
                - ^^^The^^^ `/etc/sudoers` ^^^file is the main configuration file for the^^^ `sudo` ^^^command. It defines which users or groups can run which commands with elevated privileges. To avoid problems if multiple administrators try to edit the file at the same time, you should edit it only with the special^^^ `visudo` ^^^command. The^^^ `visudo` ^^^editor also validates the file, to ensure no syntax errors.^^^
                - ^^^A common entry in^^^ `/etc/sudoers` ^^^allows members of the^^^ `wheel` ^^^group to run any command as^^^ `root`^^^. The^^^ `labex` ^^^user is a member of the^^^ `wheel` ^^^group, which is why^^^ `sudo` ^^^works without a password.^^^
                - `sudo grep wheel /etc/sudoers`^^^ ^^^
                - ^^^You should see a line similar to this, which grants^^^ `sudo` ^^^access to the^^^ `wheel` ^^^group:^^^
                - `%wheel        ALL=(ALL:ALL)       ALL``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
                - ^^^This line means:^^^
                    - `%wheel`^^^: The rule applies to members of the^^^ `wheel` ^^^group. The^^^ `%` ^^^symbol denotes a group.^^^
                    - `ALL=(ALL:ALL)``(#3594f7)`^^^: On any host (first^^^ `ALL``(#3594f7)`^^^), users in the^^^ `wheel``(#3594f7)` ^^^group can run commands as any user (second^^^ `ALL``(#3594f7)`^^^) and any group (third^^^ `ALL``(#3594f7)`^^^).^^^
                    - `ALL`^^^: Users in the^^^ `wheel` ^^^group can run any command.^^^
        - ^^^This concludes your exploration of gaining superuser access. You now understand the difference between^^^ `su -` ^^^and^^^ `sudo -i` ^^^and how to execute commands with elevated privileges.^^^
        - 
        - # ^^^**Create and Modify Local User Accounts**^^^
        - ^^^In this step, you will learn how to create, modify, and delete local user accounts on a RHEL system. Managing user accounts is a fundamental administrative task, ensuring that each user has appropriate access and permissions. You will use commands like^^^ `useradd`^^^,^^^ `usermod`^^^,^^^ `userdel`^^^, and^^^ `passwd`^^^.^^^
        - ^^^First, let's create a new user account.^^^
            - ^^^Use the^^^ `useradd` ^^^command to create a new user. By default,^^^ `useradd` ^^^creates a new user with a UID greater than or equal to 1000, creates a home directory (^^^`/home/username`^^^), and sets the default shell to^^^ `/bin/bash`^^^. You need^^^ `sudo` ^^^privileges to run this command. Let's create a user named^^^ `testuser01`^^^.^^^
                - `sudo useradd testuser01`^^^ ^^^
                - ^^^After creating the user, you can verify its existence in^^^ `/etc/passwd` ^^^and check its home directory.^^^
                - ```
grep testuser01 /etc/passwd

``````
ls
``````
 -ld /home/testuser01
```^^^ ^^^
                - ^^^You should see output similar to this:^^^
                - ```
testuser01:x:1001:1001::/home/testuser01:/bin/bash
drwx------. 2 testuser01 testuser01 6 Mar  4 15:22 /home/testuser01
```^^^ ^^^
            - ^^^By default, newly created users do not have a password set, which means they cannot log in. You need to set a password for^^^ `testuser01` ^^^using the^^^ `passwd` ^^^command.^^^
                - `sudo passwd testuser01`^^^ ^^^
                - ^^^You will be prompted to enter a new password. For this lab, use^^^ `labexrhel9` ^^^as the password for^^^ `testuser01`^^^. You might see a "BAD PASSWORD" warning, but you can proceed.^^^
                - ```
New password:
Retype new password:
passwd: all authentication tokens updated successfully.
```^^^ ^^^
                - ^^^Now, try to switch to^^^ `testuser01` ^^^using^^^ `su -`^^^.^^^
                - `su - testuser01`^^^ ^^^
                - ^^^Enter the password^^^ `labexrhel9` ^^^when prompted. Your prompt should change to^^^ `[testuser01@host ~]$`^^^.^^^
                - ```
Password:
[testuser01@host ~]$
```^^^ ^^^
                - ^^^To return to your^^^ `labex` ^^^user, type^^^ `exit`^^^.^^^
                - `exit`^^^ ^^^
        - ^^^Next, let's modify an existing user account using the^^^ `usermod` ^^^command. The^^^ `usermod` ^^^command allows you to change various properties of a user, such as their home directory, shell, or group memberships.^^^
            - ^^^Let's change the comment field (full name) for^^^ `testuser01``(#3594f7)` ^^^to "Test User One".^^^
                - `sudo usermod -c ``"Test User One"``(#98c379)`` testuser01`^^^ ^^^
                - ^^^Verify the change by checking the^^^ `/etc/passwd` ^^^file again.^^^
                - `grep testuser01 /etc/passwd`^^^ ^^^
                - ^^^The output should now reflect the updated comment:^^^
                - `testuser01:x:1001:1001:Test User One:/home/testuser01:/bin/bash`^^^ ^^^
            - ^^^You can also lock or unlock a user account. Locking an account prevents the user from logging in, while unlocking it re-enables login.^^^
                - ^^^To lock the^^^ `testuser01` ^^^account:^^^
                - `sudo usermod -L testuser01`^^^ ^^^
                - ^^^Now, try to switch to^^^ `testuser01` ^^^again.^^^
                - `su - testuser01`^^^ ^^^
                - ^^^You will be prompted for the password, but even with the correct password, the login will fail:^^^
                - ```
Password:
su: Authentication failure
```^^^ ^^^
                - ^^^To unlock the^^^ `testuser01` ^^^account:^^^
                - `sudo usermod -U testuser01`^^^ ^^^
                - ^^^Try to switch to^^^ `testuser01` ^^^again, and it should succeed. Remember to^^^ `exit` ^^^to return to^^^ `labex`^^^.^^^
                - ```
su - testuser01

``````
# Enter password 'labexrhel9'
``````
(#5c6370)

``````
exit
``````
(#e6c07b)
```^^^ ^^^
        - ^^^Finally, let's delete the user account you created.^^^
            - ^^^Use the^^^ `userdel` ^^^command to remove a user. By default,^^^ `userdel` ^^^removes the user's entry from^^^ `/etc/passwd` ^^^but leaves their home directory intact. This can lead to orphaned files.^^^
                - `sudo userdel testuser01`^^^ ^^^
                - ^^^Verify that the user is removed from^^^ `/etc/passwd`^^^, but the home directory still exists.^^^
                - ```
grep testuser01 /etc/passwd

``````
ls
``````
 -ld /home/testuser01
```^^^ ^^^
                - ^^^The^^^ `grep` ^^^command should return no output, indicating the user is gone. The^^^ `ls -ld` ^^^command will show the home directory still exists, but its ownership will appear as numeric UIDs/GIDs since the user no longer exists.^^^
                - `drwx------ 2 1001 1001 83 Mar  4 15:22 /home/testuser01`^^^ ^^^
                - ^^^ *Note: In some RHEL versions or configurations,* ^^^^^^ ^^^ ` __userdel__ `  ^^^ *might remove the home directory by default if it's empty or if the user was the sole owner. However, it's safer to explicitly use the* ^^^^^^ ^^^ ` __-r__ `  ^^^ *option to ensure the home directory is removed.* ^^^
            - ^^^To remove the user and their home directory, use the^^^ `-r` ^^^option with^^^ `userdel`^^^. Let's create a new user^^^ `testuser02` ^^^to demonstrate this properly.^^^
                - ```
sudo useradd testuser02
sudo passwd testuser02 
``````
# You'll be prompted to enter 'labexrhel9'
``````
(#5c6370)
```^^^ ^^^
                - ^^^Now, remove^^^ `testuser02` ^^^and its home directory:^^^
                - `sudo userdel -r testuser02`^^^ ^^^
                - ^^^Verify that both the user entry and the home directory are removed.^^^
                - ```
grep testuser02 /etc/passwd

``````
ls
``````
 -ld /home/testuser02
```^^^ ^^^
                - ^^^Both commands should indicate that^^^ `testuser02` ^^^and its home directory no longer exist.^^^
                - `ls: cannot access '/home/testuser02': No such file or directory`^^^ ^^^
        - ^^^This concludes your practice with creating, modifying, and deleting local user accounts.^^^
        - 
        - # ^^^**Manage Local Group Accounts**^^^
        - ^^^In this step, you will learn how to manage local group accounts on a RHEL system. Groups are fundamental for managing permissions efficiently, allowing you to grant access to multiple users simultaneously. You will use commands like^^^ `groupadd`^^^,^^^ `groupmod`^^^, and^^^ `groupdel`^^^, and also revisit^^^ `usermod` ^^^for managing user-group memberships.^^^
        - ^^^First, let's create a new group.^^^
            - ^^^Use the^^^ `groupadd` ^^^command to create a new group. By default,^^^ `groupadd` ^^^assigns the next available GID from the range specified in^^^ `/etc/login.defs`^^^. You need^^^ `sudo` ^^^privileges to run this command. Let's create a group named^^^ `developers`^^^.^^^
                - `sudo groupadd developers`^^^ ^^^
                - ^^^You can verify the creation of the group by checking the^^^ `/etc/group` ^^^file.^^^
                - `grep developers /etc/group`^^^ ^^^
                - ^^^You should see an entry similar to this:^^^
                - `developers:x:1002:`^^^ ^^^
            - ^^^You can also specify a particular GID for the group using the^^^ `-g` ^^^option. Let's create another group named^^^ `testers` ^^^with a specific GID, for example,^^^ `2000`^^^.^^^
                - `sudo groupadd -g 2000 testers`^^^ ^^^
                - ^^^Verify the GID of the^^^ `testers` ^^^group.^^^
                - `grep testers /etc/group`^^^ ^^^
                - ^^^The output should confirm the specified GID:^^^
                - `testers:x:2000:`^^^ ^^^
        - ^^^Next, let's modify an existing group using the^^^ `groupmod` ^^^command.^^^
            - ^^^You can change the name of a group using the^^^ `-n` ^^^option. Let's rename^^^ `testers` ^^^to^^^ `qa_team`^^^.^^^
                - `sudo groupmod -n qa_team testers`^^^ ^^^
                - ^^^Verify the name change in^^^ `/etc/group`^^^.^^^
                - `grep qa_team /etc/group`^^^ ^^^
                - ^^^The output should show the new name with the original GID:^^^
                - `qa_team:x:2000:`^^^ ^^^
            - ^^^You can also change the GID of a group using the^^^ `-g` ^^^option. Let's change the GID of^^^ `qa_team` ^^^to^^^ `2001`^^^.^^^
                - `sudo groupmod -g 2001 qa_team`^^^ ^^^
                - ^^^Verify the GID change.^^^
                - `grep qa_team /etc/group`^^^ ^^^
                - ^^^The output should reflect the new GID:^^^
                - `qa_team:x:2001:`^^^ ^^^
        - ^^^Now, let's manage user memberships within these groups. You will use the^^^ `usermod` ^^^command for this. First, create a couple of test users.^^^
            - ^^^Create^^^ `userA` ^^^and^^^ `userB` ^^^and set their passwords to^^^ `labexrhel9`^^^.^^^
                - ```
sudo useradd userA
sudo passwd userA
```^^^ ^^^
                - ^^^Type^^^ `labexrhel9` ^^^as the password for^^^ `userA`^^^.^^^
                - ```
sudo useradd userB
sudo passwd userB
```^^^ ^^^
                - ^^^Type^^^ `labexrhel9` ^^^as the password for^^^ `userB`^^^.^^^
            - ^^^Add^^^ `userA` ^^^to the^^^ `developers` ^^^group as a secondary group. Use the^^^ `-a` ^^^(append) and^^^ `-G` ^^^(groups) options with^^^ `usermod`^^^.^^^
                - `sudo usermod -aG developers userA`^^^ ^^^
                - ^^^Verify^^^ `userA`^^^'s group memberships using the^^^ `id` ^^^command.^^^
                - `id`` userA`^^^ ^^^
                - ^^^You should see^^^ `developers` ^^^listed in the^^^ `groups` ^^^section:^^^
                - `uid=1003(userA) gid=1003(userA) groups=1003(userA),1002(developers)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
            - ^^^Add^^^ `userB` ^^^to both^^^ `developers` ^^^and^^^ `qa_team` ^^^groups as secondary groups.^^^
                - `sudo usermod -aG developers,qa_team userB`^^^ ^^^
                - ^^^Verify^^^ `userB`^^^'s group memberships.^^^
                - `id`` userB`^^^ ^^^
                - ^^^You should see both^^^ `developers` ^^^and^^^ `qa_team` ^^^listed:^^^
                - `uid=1004(userB) gid=1004(userB) groups=1004(userB),1002(developers),2001(qa_team)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
            - ^^^You can also change a user's primary group using the^^^ `-g` ^^^option with^^^ `usermod`^^^. Let's change^^^ `userA`^^^'s primary group to^^^ `developers`^^^.^^^
                - `sudo usermod -g developers userA`^^^ ^^^
                - ^^^Verify^^^ `userA`^^^'s primary group.^^^
                - `id`` userA`^^^ ^^^
                - ^^^The^^^ `gid` ^^^field should now show^^^ `developers`^^^:^^^
                - `uid=1003(userA) gid=1002(developers) groups=1002(developers)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
                - ^^^ *Note: When you change a user's primary group, they are removed from their old primary group's membership list in* ^^^^^^ ^^^ ` __/etc/group__ `  ^^^ *if that group was also a secondary group. In this case,* ^^^^^^ ^^^ ` __userA__ ` ^^^ *'s original primary group (* ^^^^^^ ^^^` __userA__ ` ^^^ *) is no longer listed as a secondary group.* ^^^
        - ^^^Finally, let's delete the groups and test users you created.^^^
            - ^^^Use the^^^ `groupdel` ^^^command to remove a group. You cannot delete a group if it is the primary group for any user. First, change^^^ `userA`^^^'s primary group back to its default (or another existing group) before deleting^^^ `developers`^^^.^^^
                - ```
sudo usermod -g userA userA 
``````
# Change userA's primary group back to userA
``````
(#5c6370)
sudo groupdel developers
```^^^ ^^^
                - ^^^Verify that^^^ `developers` ^^^is removed from^^^ `/etc/group`^^^.^^^
                - `grep developers /etc/group`^^^ ^^^
                - ^^^This command should return no output.^^^
            - ^^^Delete the^^^ `qa_team` ^^^group.^^^
                - `sudo groupdel qa_team`^^^ ^^^
                - ^^^Verify its removal.^^^
                - `grep qa_team /etc/group`^^^ ^^^
                - ^^^This command should also return no output.^^^
            - ^^^Clean up the test users.^^^
                - ```
sudo userdel -r userA
sudo userdel -r userB
```^^^ ^^^
        - ^^^This concludes your practice with managing local group accounts and user-group memberships.^^^
        - 
        - # ^^^**Configure User Password Policies**^^^
        - ^^^In this step, you will learn how to configure user password policies on a RHEL system. Password policies are crucial for enhancing security by enforcing rules on password complexity, expiration, and account locking. You will explore the^^^ `/etc/shadow` ^^^file and the^^^ `chage` ^^^command.^^^
        - ^^^First, let's understand the^^^ `/etc/shadow` ^^^file, which stores encrypted password information and password aging parameters for user accounts. This file is highly sensitive and is only readable by the^^^ `root` ^^^user.^^^
            - ^^^Each user has an entry in the^^^ `/etc/shadow` ^^^file. Let's create a new user^^^ `policyuser` ^^^and set its password to^^^ `labexrhel9` ^^^for demonstration purposes.^^^
                - ```
sudo useradd policyuser
sudo passwd policyuser
```^^^ ^^^
                - ^^^Type^^^ `labexrhel9` ^^^as the password for^^^ `policyuser`^^^.^^^
            - ^^^Now, view the entry for^^^ `policyuser` ^^^in^^^ `/etc/shadow`^^^.^^^
                - `sudo grep policyuser /etc/shadow`^^^ ^^^
                - ^^^You will see an output similar to this:^^^
                - `policyuser:$6$randomsalt$encryptedhash:19780:0:99999:7:::`^^^ ^^^
                - ^^^Let's break down each field, separated by a colon:^^^
                    - `policyuser`^^^: Name of the user account.^^^
                    - `$6$randomsalt$encryptedhash`^^^: The encrypted password of the user.^^^
                        - `$6`^^^: The hashing algorithm in use for this password (SHA-512, the RHEL 9 default).^^^
                        - `randomsalt`^^^: The salt used to encrypt the password; originally chosen at random.^^^
                        - `encryptedhash`^^^: The encrypted hash of the user's password.^^^
                    - `19780`^^^: The days from the epoch (1970-01-01 UTC) when the password was last changed. This number will vary based on the current date.^^^
                    - `0`^^^: The minimum days since the last password change before the user can change it again.^^^
                    - `99999`^^^: The maximum days without a password change before the password expires. An empty field means the password never expires.^^^
                    - `7`^^^: The number of days ahead to warn the user that their password will expire.^^^
                    - ^^^(empty): The number of days without activity, starting with the day the password expired, before the account is automatically locked.^^^
                    - ^^^(empty): The day when the account expires in days since the epoch. An empty field means the account never expires.^^^
                    - ^^^The last field is typically empty and reserved for future use.^^^
        - ^^^Next, you will use the^^^ `chage` ^^^command to modify these password aging parameters. The^^^ `chage` ^^^command allows you to change user password expiry information.^^^
            - ^^^Let's set a password policy for^^^ `policyuser` ^^^with the following rules:^^^
                - ^^^Minimum days between password changes: 7 days (^^^`-m 7``(#3594f7)`^^^)^^^
                - ^^^Maximum days between password changes: 90 days (^^^`-M 90``(#3594f7)`^^^)^^^
                - ^^^Warning period before password expires: 14 days (^^^`-W 14``(#3594f7)`^^^)^^^
                - ^^^Inactivity period after password expires before account locks: 30 days (^^^`-I 30``(#3594f7)`^^^)^^^
                - `sudo chage -m 7 -M 90 -W 14 -I 30 policyuser`^^^ ^^^
            - ^^^To verify these changes, you can use^^^ `chage -l` ^^^(list) to display the current password aging information for^^^ `policyuser`^^^.^^^
                - `sudo chage -l policyuser`^^^ ^^^
                - ^^^You should see output reflecting the new policy:^^^
                - ```
Last password change					: Mar 04, 2024
Password expires					: Jun 02, 2024
Password inactive					: Jul 02, 2024
Account expires						: never
Minimum number of days between password change		: 7
Maximum number of days between password change		: 90
Number of days of warning before password expires	: 14
```^^^ ^^^
                - ^^^ *Note: The dates will vary based on when you perform the lab.* ^^^
            - ^^^You can also set an absolute account expiration date using the^^^ `-E` ^^^option. Let's set^^^ `policyuser`^^^'s account to expire in 30 days from today. First, get today's date and calculate the date 30 days from now.^^^
                - ```
EXPIRY_DATE=$(
``````
date
``````
(#e6c07b) -d 
``````
"+30 days"
``````
(#98c379) +%Y-%m-%d)

``````
echo
``````
(#e6c07b) 
``````
"Account will expire on: 
``````
(#98c379)
``````
$EXPIRY_DATE
``````
(#d19a66)
``````
"
``````
(#98c379)
sudo chage -E 
``````
$EXPIRY_DATE
``````
(#d19a66) policyuser
```^^^ ^^^
                - ^^^Verify the account expiration date.^^^
                - `sudo chage -l policyuser | grep ``"Account expires"``(#98c379)`^^^ ^^^
                - ^^^The output should show the calculated expiration date:^^^
                - `Account expires						: Apr 03, 2024`^^^ ^^^
                - ^^^ *Note: The date will be approximately 30 days from your current lab date.* ^^^
            - ^^^To remove the account expiration date, you can use^^^ `chage -E -1 policyuser`^^^.^^^
                - ```
sudo chage -E -1 policyuser
sudo chage -l policyuser | grep 
``````
"Account expires"
``````
(#98c379)
```^^^ ^^^
                - ^^^The output should revert to^^^ `never`^^^:^^^
                - `Account expires						: never`^^^ ^^^
        - ^^^Finally, clean up the^^^ `policyuser` ^^^account.^^^
        - `sudo userdel -r policyuser`^^^ ^^^
        - ^^^This concludes your practice with configuring user password policies. You now understand how to inspect and modify password aging parameters using the^^^ `/etc/shadow` ^^^file and the^^^ `chage` ^^^command.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, you learned fundamental concepts of user and group management in Red Hat Enterprise Linux (RHEL). You began by understanding how users and groups are associated with files and processes, and how to inspect user and group information using the^^^ `id``(#3594f7)` ^^^command for both the current user and other system users like^^^ `root``(#3594f7)`^^^. You also practiced identifying file and directory ownership using the^^^ `ls -l``(#3594f7)` ^^^and^^^ `ls -ld``(#3594f7)` ^^^commands, respectively, which is crucial for understanding permissions and access control.^^^
        - ^^^The lab further guided you through gaining superuser access, creating and modifying local user accounts, managing local group accounts, and configuring user password policies. These steps provided practical experience in essential system administration tasks, enabling you to effectively manage user access and security on a Linux system.^^^
    6. Control File Access in Red Hat Enterprise Linux
        - Interpret Linux File System Permissions with ls -l
        - Change File Permissions with chmod (Symbolic Mode)
        - Change File Permissions with chmod (Octal Mode)
        - Change File Ownership with chown
        - Understand and Apply Special Permissions (SUID, SGID, Sticky Bit)
        - Configure Default Permissions with umask
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain a comprehensive understanding of managing Linux file system permissions, a critical skill for any RHEL administrator. You will learn to interpret file permissions using^^^ `ls -l`^^^, modify them with^^^ `chmod` ^^^in both symbolic and octal modes, and change file ownership using^^^ `chown`^^^. Furthermore, you will explore and apply special permissions like SUID, SGID, and the Sticky Bit, and configure default permissions effectively with^^^ `umask`^^^. This hands-on experience will equip you with the necessary knowledge to secure and control access to files and directories in a Linux environment.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^intermediate^^^ ^^^level lab with a^^^ ^^^80%^^^ ^^^completion rate. It has received a^^^ ^^^91%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Interpret Linux File System Permissions with ls -l**^^^
        - ^^^In this step, you will learn how to interpret Linux file system permissions using the^^^ `ls -l` ^^^command. Understanding file permissions is crucial for managing access to files and directories in a Linux environment.^^^
        - ^^^Every file and directory in Linux has associated permissions that determine who can read, write, or execute it. These permissions are divided into three categories:^^^
            - ^^^**User (owner):**^^^ ^^^The permissions for the file's owner.^^^
            - ^^^**Group:**^^^ ^^^The permissions for users who are members of the file's group.^^^
            - ^^^**Others:**^^^ ^^^The permissions for all other users on the system.^^^
        - ^^^Each category can have three types of permissions:^^^
            - ^^^**Read (**^^^`**r**``(#3594f7)`^^^**):**^^^ ^^^Allows viewing the contents of a file or listing the contents of a directory.^^^
            - ^^^**Write (**^^^`**w**``(#3594f7)`^^^**):**^^^ ^^^Allows modifying the contents of a file or creating/deleting files within a directory.^^^
            - ^^^**Execute (**^^^`**x**``(#3594f7)`^^^**):**^^^ ^^^Allows running an executable file or entering a directory.^^^
        - ^^^Let's start by creating a new directory and a file within your^^^ `~/project` ^^^directory to observe their default permissions.^^^
        - ^^^First, create a directory named^^^ `my_files`^^^:^^^
        - `mkdir`` ~/project/my_files`^^^ ^^^
        - ^^^Next, create an empty file named^^^ `document.txt` ^^^inside the^^^ `my_files` ^^^directory:^^^
        - `touch`` ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Now, use the^^^ `ls -l` ^^^command to view the detailed permissions of the^^^ `document.txt` ^^^file. The^^^ `ls -l` ^^^command provides a long listing format, including file permissions, owner, group, size, and modification date.^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^You should see output similar to this:^^^
        - `-rw-rw-r-- 1 labex labex 0 Jun  6 17:36 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^Let's break down the first part of the output,^^^ `-rw-rw-r--.`^^^:^^^
            - ^^^The first character (^^^`-``(#3594f7)`^^^) indicates the file type.^^^
                - `-` ^^^means it's a regular file.^^^
                - `d` ^^^means it's a directory.^^^
                - `l` ^^^means it's a symbolic link.^^^
            - ^^^The next nine characters are divided into three sets of three:^^^
                - `rw-`^^^: Permissions for the^^^ ^^^**owner**^^^ ^^^(^^^`labex`^^^).^^^ `r` ^^^(read),^^^ `w` ^^^(write),^^^ `-` ^^^(no execute).^^^
                - `rw-`^^^: Permissions for the^^^ ^^^**group**^^^ ^^^(^^^`labex`^^^).^^^ `r` ^^^(read),^^^ `w` ^^^(write),^^^ `-` ^^^(no execute).^^^
                - `r--`^^^: Permissions for^^^ ^^^**others**^^^^^^.^^^ `r` ^^^(read),^^^ `-` ^^^(no write),^^^ `-` ^^^(no execute).^^^
        - ^^^This means the^^^ `labex` ^^^user (owner) and users in the^^^ `labex` ^^^group can read and write to^^^ `document.txt`^^^, while all other users can only read it.^^^
        - ^^^Now, let's examine the permissions of the^^^ `my_files` ^^^directory itself. When using^^^ `ls -l` ^^^on a directory, it lists the contents of the directory. To view the permissions of the directory^^^  ^^^ *itself* ^^^^^^ ^^^^^^, you need to use the^^^ `-d` ^^^option with^^^ `ls -l`^^^.^^^
        - `ls`` -ld ~/project/my_files`^^^ ^^^
        - ^^^You should see output similar to this:^^^
        - `drwxrwxr-x 2 labex labex 4096 Jun  6 17:36 /home/labex/project/my_files`^^^ ^^^
        - ^^^Let's interpret the permissions^^^ `drwxrwxr-x.`^^^:^^^
            - ^^^The first character (^^^`d``(#3594f7)`^^^) indicates it's a directory.^^^
            - `rwx`^^^: Permissions for the^^^ ^^^**owner**^^^ ^^^(^^^`labex`^^^).^^^ `r` ^^^(read),^^^ `w` ^^^(write),^^^ `x` ^^^(execute).^^^
            - `rwx`^^^: Permissions for the^^^ ^^^**group**^^^ ^^^(^^^`labex`^^^).^^^ `r` ^^^(read),^^^ `w` ^^^(write),^^^ `x` ^^^(execute).^^^
            - `r-x`^^^: Permissions for^^^ ^^^**others**^^^^^^.^^^ `r` ^^^(read),^^^ `-` ^^^(no write),^^^ `x` ^^^(execute).^^^
        - ^^^For directories:^^^
            - `r` ^^^(read) allows listing the contents of the directory.^^^
            - `w` ^^^(write) allows creating, deleting, or renaming files within the directory.^^^
            - `x` ^^^(execute) allows entering the directory (using^^^ `cd`^^^) and accessing its files and subdirectories.^^^
        - ^^^This means the^^^ `labex` ^^^user and users in the^^^ `labex` ^^^group can list, create/delete files, and enter the^^^ `my_files` ^^^directory. Other users can list and enter the directory, but cannot create or delete files within it.^^^
        - 
        - # ^^^**Change File Permissions with chmod (Symbolic Mode)**^^^
        - ^^^In this step, you will learn how to change file permissions using the^^^ `chmod` ^^^command in symbolic mode. Symbolic mode uses letters and symbols to represent permission changes, making it intuitive to add, remove, or set specific permissions.^^^
        - ^^^The^^^ `chmod` ^^^command in symbolic mode follows the syntax:^^^ `chmod WHO OPERATION PERMISSIONS FILE`^^^.^^^
            - ^^^**WHO:**^^^ ^^^Specifies who the permission change applies to.^^^
                - `u`^^^: user (owner)^^^
                - `g`^^^: group^^^
                - `o`^^^: others^^^
                - `a`^^^: all (user, group, and others)^^^
            - ^^^**OPERATION:**^^^ ^^^Specifies how to modify the permissions.^^^
                - `+`^^^: Add a permission.^^^
                - `-`^^^: Remove a permission.^^^
                - `=`^^^: Set permissions exactly as specified, overriding existing ones.^^^
            - ^^^**PERMISSIONS:**^^^ ^^^Specifies the permission type.^^^
                - `r`^^^: read^^^
                - `w`^^^: write^^^
                - `x`^^^: execute^^^
        - ^^^Let's continue working with the^^^ `~/project/my_files/document.txt` ^^^file and^^^ `~/project/my_files` ^^^directory created in the previous step.^^^
        - ^^^First, let's remove write permission for the group and others from^^^ `document.txt`^^^. Recall that its current permissions are^^^ `-rw-rw-r--`^^^.^^^
        - `chmod`` go-w ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Now, verify the change using^^^ `ls -l`^^^:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should now show:^^^
        - `-rw-r--r-- 1 labex labex 0 Jun  6 17:36 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^Notice that the^^^ `w` ^^^(write) permission for the group and others has been removed.^^^
        - ^^^Next, let's add execute permission for the owner (^^^`u``(#3594f7)`^^^) to^^^ `document.txt``(#3594f7)`^^^. This is often done for scripts to make them executable.^^^
        - `chmod`` u+x ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should now be:^^^
        - `-rwxr--r-- 1 labex labex 0 Jun  6 17:36 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^The owner now has execute permission (^^^`x``(#3594f7)`^^^).^^^
        - ^^^Now, let's practice with the^^^ `~/project/my_files` ^^^directory. Its current permissions are^^^ `drwxrwxr-x`^^^. Let's remove write permission for others (^^^`o`^^^) from the directory.^^^
        - `chmod`` o-w ~/project/my_files`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -ld ~/project/my_files`^^^ ^^^
        - ^^^The output should now show:^^^
        - `drwxr-xr-x 2 labex labex 4096 Jun  6 17:36 /home/labex/project/my_files`^^^ ^^^
        - ^^^Wait, why did the^^^ `o-w` ^^^not change the output? This is because the^^^ `o` ^^^(others) already did not have write permission. The^^^ `r-x` ^^^for others means read and execute, but no write. This demonstrates that^^^ `chmod` ^^^only applies changes if they are different from the current state.^^^
        - ^^^Let's try setting permissions exactly. We will set the permissions for^^^ `document.txt` ^^^to^^^ `rw-r--r--` ^^^for all (owner, group, others). This means owner gets read/write, group gets read, and others get read.^^^
        - `chmod`` a=rw,g=r,o=r ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should now be:^^^
        - `-rw-r--r-- 1 labex labex 0 Jun  6 17:36 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^This command^^^ `a=rw,g=r,o=r` ^^^is a bit redundant as^^^ `a=rw` ^^^would apply^^^ `rw` ^^^to all, then^^^ `g=r` ^^^would set group to^^^ `r` ^^^(overriding the^^^ `w` ^^^from^^^ `a=rw`^^^), and^^^ `o=r` ^^^would set others to^^^ `r` ^^^(overriding the^^^ `w` ^^^from^^^ `a=rw`^^^). A simpler way to achieve^^^ `rw-r--r--` ^^^would be^^^ `chmod u=rw,go=r`^^^. Let's try that.^^^
        - `chmod`` u=rw,go=r ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should still be:^^^
        - `-rw-r--r-- 1 labex labex 0 Jun  6 17:36 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^Finally, let's make^^^ `document.txt` ^^^executable for everyone.^^^
        - `chmod`` a+x ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should now be:^^^
        - `-rwxr-xr-x 1 labex labex 0 Jun  6 17:36 /home/labex/project/my_files/document.txt`^^^ ^^^
        - 
        - # ^^^**Change File Permissions with chmod (Octal Mode)**^^^
        - ^^^In this step, you will learn how to change file permissions using the^^^ `chmod` ^^^command in octal (numeric) mode. Octal mode is a concise way to represent permissions, where each permission (read, write, execute) is assigned a numerical value.^^^
        - ^^^The numerical values for permissions are:^^^
            - ^^^**Read (**^^^`**r**``(#3594f7)`^^^**):**^^^ ^^^4^^^
            - ^^^**Write (**^^^`**w**``(#3594f7)`^^^**):**^^^ ^^^2^^^
            - ^^^**Execute (**^^^`**x**``(#3594f7)`^^^**):**^^^ ^^^1^^^
            - ^^^**No permission (**^^^`**-**``(#3594f7)`^^^**):**^^^ ^^^0^^^
        - ^^^To determine the octal value for a set of permissions (user, group, or others), you sum the values of the permissions granted.^^^
        - ^^^For example:^^^
            - `rwx` ^^^(read, write, execute) = 4 + 2 + 1 = 7^^^
            - `rw-` ^^^(read, write, no execute) = 4 + 2 + 0 = 6^^^
            - `r-x` ^^^(read, no write, execute) = 4 + 0 + 1 = 5^^^
            - `r--` ^^^(read, no write, no execute) = 4 + 0 + 0 = 4^^^
            - `---` ^^^(no permissions) = 0 + 0 + 0 = 0^^^
        - ^^^The^^^ `chmod` ^^^command in octal mode uses a three-digit number, where each digit represents the permissions for the owner, group, and others, respectively. The syntax is:^^^ `chmod OGO FILE`^^^.^^^
            - ^^^**O:**^^^ ^^^Octal value for^^^ ^^^**owner**^^^ ^^^permissions.^^^
            - ^^^**G:**^^^ ^^^Octal value for^^^ ^^^**group**^^^ ^^^permissions.^^^
            - ^^^**O:**^^^ ^^^Octal value for^^^ ^^^**others**^^^ ^^^permissions.^^^
        - ^^^Let's continue working with^^^ `~/project/my_files/document.txt` ^^^and^^^ `~/project/my_files`^^^.^^^
        - ^^^First, let's set the permissions of^^^ `document.txt` ^^^to^^^ `rw-r--r--`^^^.^^^
            - ^^^Owner:^^^ `rw-` ^^^= 6^^^
            - ^^^Group:^^^ `r--` ^^^= 4^^^
            - ^^^Others:^^^ `r--` ^^^= 4^^^
        - ^^^So, the octal value will be^^^ `644`^^^.^^^
        - `chmod`` 644 ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should now be:^^^
        - `-rw-r--r-- 1 labex labex 0 Jun  6 00:48 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^Next, let's make^^^ `document.txt` ^^^executable only by the owner, while keeping read/write for owner, and read-only for group and others. This means the owner will have^^^ `rwx` ^^^(7), group^^^ `r--` ^^^(4), and others^^^ `r--` ^^^(4). The octal value will be^^^ `744`^^^.^^^
        - `chmod`` 744 ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should now be:^^^
        - `-rwxr--r-- 1 labex labex 0 Jun  6 00:48 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^Now, let's change the permissions of the^^^ `~/project/my_files` ^^^directory. Its current permissions are^^^ `drwxr-xr-x`^^^. Let's set its permissions to^^^ `rwxr-x---`^^^.^^^
            - ^^^Owner:^^^ `rwx` ^^^= 7^^^
            - ^^^Group:^^^ `r-x` ^^^= 5^^^
            - ^^^Others:^^^ `---` ^^^= 0^^^
        - ^^^So, the octal value will be^^^ `750`^^^.^^^
        - `chmod`` 750 ~/project/my_files`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -ld ~/project/my_files`^^^ ^^^
        - ^^^The output should now show:^^^
        - `drwxr-x--- 2 labex labex 26 Jun  6 00:48 /home/labex/project/my_files`^^^ ^^^
        - ^^^This means the owner (^^^`labex``(#3594f7)`^^^) has full permissions (read, write, execute), the group (^^^`labex``(#3594f7)`^^^) can read and execute (enter) the directory, and others have no permissions at all.^^^
        - ^^^Finally, let's create a new executable script file to demonstrate setting execute permissions directly.^^^
        - ```
echo
``````
 
``````
'#!/bin/bash'
``````
(#98c379) > ~/project/my_script.sh

``````
echo
``````
 
``````
'echo "Hello from my script!"'
``````
(#98c379) >> ~/project/my_script.sh
```^^^ ^^^
        - ^^^By default, new files are not executable. Let's check its permissions:^^^
        - `ls`` -l ~/project/my_script.sh`^^^ ^^^
        - ^^^You will likely see permissions like^^^ `-rw-r--r--`^^^. To make it executable for the owner and group, but not others, we want^^^ `rwxrwx---`^^^.^^^
            - ^^^Owner:^^^ `rwx` ^^^= 7^^^
            - ^^^Group:^^^ `rwx` ^^^= 7^^^
            - ^^^Others:^^^ `---` ^^^= 0^^^
        - ^^^So, the octal value will be^^^ `770`^^^.^^^
        - `chmod`` 770 ~/project/my_script.sh`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_script.sh`^^^ ^^^
        - ^^^The output should now be:^^^
        - `-rwxrwx--- 1 labex labex 41 Jun  6 00:52 /home/labex/project/my_script.sh`^^^ ^^^
        - ^^^Now you can execute the script:^^^
        - `~/project/my_script.sh`^^^ ^^^
        - ^^^You should see the output:^^^
        - `Hello from my script!`^^^ ^^^
        - 
        - # ^^^**Change File Ownership with chown**^^^
        - ^^^In this step, you will learn how to change the owner and group of files and directories using the^^^ `chown` ^^^command. This is a crucial administrative task, as only the^^^ `root` ^^^user can change the owner of a file. The^^^ `labex` ^^^user has^^^ `sudo` ^^^privileges, which will allow you to perform these actions.^^^
        - ^^^The basic syntax for^^^ `chown` ^^^is:^^^ `chown [OPTIONS] NEW_OWNER[:NEW_GROUP] FILE(s)`^^^.^^^
        - ^^^Let's start by creating a new user and group that we can use to demonstrate ownership changes. Since this environment is container-based, we will create a simple user and group for demonstration purposes.^^^
        - ^^^First, create a new group named^^^ `devs`^^^:^^^
        - `sudo groupadd devs`^^^ ^^^
        - ^^^Next, create a new user named^^^ `developer` ^^^and add them to the^^^ `devs` ^^^group. We will create a system user without a home directory or login shell for this demonstration.^^^
        - `sudo useradd -r -g devs -s /sbin/nologin developer`^^^ ^^^
        - ^^^Now, let's change the owner of^^^ `~/project/my_files/document.txt` ^^^from^^^ `labex` ^^^to^^^ `developer`^^^.^^^
        - `sudo ``chown`` developer ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Verify the change using^^^ `ls -l`^^^:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should now show^^^ `developer` ^^^as the owner:^^^
        - `-rwxr--r-- 1 developer labex 0 Jun  6 00:48 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^Notice that the group ownership (^^^`labex``(#3594f7)`^^^) remained unchanged.^^^
        - ^^^You can also change both the owner and the group simultaneously using the^^^ `owner:group` ^^^syntax. Let's change the owner of^^^ `document.txt` ^^^back to^^^ `labex` ^^^and its group to^^^ `devs`^^^.^^^
        - `sudo ``chown`` labex:devs ~/project/my_files/document.txt`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^The output should now show^^^ `labex` ^^^as the owner and^^^ `devs` ^^^as the group:^^^
        - `-rwxr--r-- 1 labex devs 0 Jun  6 00:48 /home/labex/project/my_files/document.txt`^^^ ^^^
        - ^^^The^^^ `chown` ^^^command also supports the^^^ `-R` ^^^(recursive) option, which allows you to change the ownership of an entire directory tree. Let's change the owner of the^^^ `~/project/my_files` ^^^directory and all its contents to^^^ `developer`^^^, and the group to^^^ `devs`^^^.^^^
        - `sudo ``chown`` -R developer:devs ~/project/my_files`^^^ ^^^
        - ^^^Verify the change for the directory:^^^
        - `ls`` -ld ~/project/my_files`^^^ ^^^
        - ^^^The output should reflect the new ownership:^^^
        - `drwxr-x--- 2 developer devs 26 Jun  6 00:48 /home/labex/project/my_files`^^^ ^^^
        - ^^^Note that after changing the directory ownership to^^^ `developer:devs`^^^, the^^^ `labex` ^^^user can no longer access the file inside the directory because the directory permissions are^^^ `drwxr-x---` ^^^(owner and group have access, but others don't), and^^^ `labex` ^^^is neither the owner (^^^`developer`^^^) nor a member of the group (^^^`devs`^^^). If you try to list the file now:^^^
        - `ls`` -l ~/project/my_files/document.txt`^^^ ^^^
        - ^^^You will get a "Permission denied" error. This demonstrates how ownership and permissions work together to control access.^^^
        - ^^^You can also change only the group ownership using^^^ `chown :NEW_GROUP FILE(s)``(#3594f7)`^^^. This is equivalent to using the^^^ `chgrp``(#3594f7)` ^^^command. Let's change the group of^^^ `~/project/my_script.sh``(#3594f7)` ^^^to^^^ `devs``(#3594f7)`^^^.^^^
        - `sudo ``chown`` :devs ~/project/my_script.sh`^^^ ^^^
        - ^^^Verify the change:^^^
        - `ls`` -l ~/project/my_script.sh`^^^ ^^^
        - ^^^The output should show^^^ `devs` ^^^as the group owner, while^^^ `labex` ^^^remains the file owner:^^^
        - `-rwxrwx--- 1 labex devs 41 Jun  6 00:52 /home/labex/project/my_script.sh`^^^ ^^^
        - ^^^Finally, let's clean up by changing the ownership back to^^^ `labex:labex` ^^^and then removing the^^^ `developer` ^^^user and^^^ `devs` ^^^group.^^^
        - ```
sudo 
``````
chown
``````
 -R labex:labex ~/project/my_files
sudo userdel developer
sudo groupdel devs
```^^^ ^^^
        - 
        - # ^^^**Understand and Apply Special Permissions (SUID, SGID, Sticky Bit)**^^^
        - ^^^In this step, you will explore special permissions in Linux: SUID (Set User ID), SGID (Set Group ID), and the Sticky Bit. These permissions provide enhanced control over file execution and directory behavior.^^^
        - ^^^Special permissions are represented by an additional digit in the octal permission mode, placed before the standard three digits (owner, group, others).^^^
            - ^^^**SUID (Set User ID):**^^^
                - ^^^**Octal value:**^^^ ^^^4^^^
                - ^^^**Effect on files:**^^^ ^^^When an executable file with SUID is run, it executes with the permissions of the file's owner, not the user who ran it. This is commonly used for programs that need elevated privileges to perform certain tasks, like the^^^ `passwd` ^^^command (which needs to write to^^^ `/etc/shadow`^^^, a file owned by^^^ `root`^^^).^^^
                - ^^^**In**^^^ `**ls -l**` ^^^**output:**^^^ ^^^An^^^ `s` ^^^appears in place of the owner's^^^ `x` ^^^(execute) permission. If the owner does not have execute permission, an uppercase^^^ `S` ^^^appears.^^^
            - ^^^**SGID (Set Group ID):**^^^
                - ^^^**Octal value:**^^^ ^^^2^^^
                - ^^^**Effect on files:**^^^ ^^^Similar to SUID, but the executable runs with the permissions of the file's group owner.^^^
                - ^^^**Effect on directories:**^^^ ^^^Files and subdirectories created within an SGID-enabled directory inherit the group ownership of that directory, rather than the primary group of the user who created them. This is very useful for shared directories where all files should belong to a specific group.^^^
                - ^^^**In**^^^ `**ls -l**` ^^^**output:**^^^ ^^^An^^^ `s` ^^^appears in place of the group's^^^ `x` ^^^(execute) permission. If the group does not have execute permission, an uppercase^^^ `S` ^^^appears.^^^
            - ^^^**Sticky Bit:**^^^
                - ^^^**Octal value:**^^^ ^^^1^^^
                - ^^^**Effect on files:**^^^ ^^^No effect.^^^
                - ^^^**Effect on directories:**^^^ ^^^Users can create files in the directory, but they can only delete or rename files that they own. This prevents users from deleting or moving other users' files in a shared directory (e.g.,^^^ `/tmp``(#3594f7)`^^^).^^^
                - ^^^**In**^^^ `**ls -l**` ^^^**output:**^^^ ^^^A^^^ `t` ^^^appears in place of others'^^^ `x` ^^^(execute) permission. If others do not have execute permission, an uppercase^^^ `T` ^^^appears.^^^
        - ^^^Let's demonstrate these special permissions.^^^
        - ### ^^^**SUID Example**^^^
        - ^^^We'll create a simple C program that attempts to read a restricted file.^^^
        - ^^^First, create a file that only^^^ `root` ^^^can read:^^^
        - ```
sudo 
``````
touch
``````
 ~/project/secret_data.txt
sudo 
``````
chmod
``````
 600 ~/project/secret_data.txt
sudo 
``````
chown
``````
 root:root ~/project/secret_data.txt
```^^^ ^^^
        - ^^^Verify its permissions:^^^
        - `ls`` -l ~/project/secret_data.txt`^^^ ^^^
        - ^^^Output:^^^
        - `-rw------- 1 root root 0 Jun  6 17:36 /home/labex/project/secret_data.txt`^^^ ^^^
        - ^^^Now, create a C program^^^ `read_secret.c` ^^^that tries to read this file:^^^
        - `nano ~/project/read_secret.c`^^^ ^^^
        - ^^^Paste the following code into^^^ `read_secret.c`^^^:^^^
        - ```
#
``````
(#61aeee)
``````
include
``````
(#c678dd) 
``````
<stdio.h>
``````
(#98c379)

``````
#
``````
(#61aeee)
``````
include
``````
(#c678dd) 
``````
<stdlib.h>
``````
(#98c379)

``````
#
``````
(#61aeee)
``````
include
``````
(#c678dd) 
``````
<unistd.h>
``````
(#98c379)


``````
int
``````
(#d19a66) 
``````
main
``````
(#61aeee)() {
    FILE *fp;
    
``````
char
``````
(#d19a66) buffer[
``````
256
``````
(#d19a66)];

    
``````
printf
``````
(#e6c07b)(
``````
"Attempting to read /home/labex/project/secret_data.txt...\n"
``````
(#98c379));

    fp = fopen(
``````
"/home/labex/project/secret_data.txt"
``````
(#98c379), 
``````
"r"
``````
(#98c379));
    
``````
if
``````
(#c678dd) (fp == 
``````
NULL
``````
(#56b6c2)) {
        perror(
``````
"Error opening file"
``````
(#98c379));
        
``````
return
``````
(#c678dd) 
``````
1
``````
(#d19a66);
    }

    
``````
while
``````
(#c678dd) (fgets(buffer, 
``````
sizeof
``````
(#c678dd)(buffer), fp) != 
``````
NULL
``````
(#56b6c2)) {
        
``````
printf
``````
(#e6c07b)(
``````
"%s"
``````
(#98c379), buffer);
    }

    fclose(fp);
    
``````
printf
``````
(#e6c07b)(
``````
"Successfully read file.\n"
``````
(#98c379));
    
``````
return
``````
(#c678dd) 
``````
0
``````
(#d19a66);
}
```^^^ ^^^
        - ^^^Save and exit^^^ `nano` ^^^(Ctrl+S, Ctrl+X).^^^
        - ^^^Compile the program:^^^
        - `gcc ~/project/read_secret.c -o ~/project/read_secret`^^^ ^^^
        - ^^^Now, try to run it as^^^ `labex`^^^:^^^
        - `~/project/read_secret`^^^ ^^^
        - ^^^You should see an "Error opening file: Permission denied" message, as^^^ `labex` ^^^does not have read access to^^^ `secret_data.txt`^^^.^^^
        - ^^^Now, let's make^^^ `read_secret` ^^^owned by^^^ `root` ^^^and set the SUID bit.^^^
        - ```
sudo 
``````
chown
``````
 root:root ~/project/read_secret
sudo 
``````
chmod
``````
 u+s ~/project/read_secret
```^^^ ^^^
        - ^^^Verify the permissions:^^^
        - `ls`` -l ~/project/read_secret`^^^ ^^^
        - ^^^Output:^^^
        - `-rwsr-xr-x 1 root root 17704 Jun  6 01:02 /home/labex/project/read_secret`^^^ ^^^
        - ^^^Notice the^^^ `s` ^^^in the owner's permission set. Now, run the program again as^^^ `labex`^^^:^^^
        - `~/project/read_secret`^^^ ^^^
        - ^^^This time, it should successfully read the file (though it's empty, so no content will be printed, but the "Successfully read file." message indicates success). This is because the SUID bit made the program run with^^^ `root``(#3594f7)`^^^'s permissions.^^^
        - ### ^^^**SGID Example (on Directory)**^^^
        - ^^^Let's create a shared directory and a new group.^^^
        - ```
sudo groupadd shared_group
sudo 
``````
mkdir
``````
 ~/project/shared_dir
sudo 
``````
chown
``````
 labex:shared_group ~/project/shared_dir
sudo 
``````
chmod
``````
 770 ~/project/shared_dir
```^^^ ^^^
        - ^^^Now, set the SGID bit on^^^ `shared_dir`^^^:^^^
        - `sudo ``chmod`` g+s ~/project/shared_dir`^^^ ^^^
        - ^^^Verify the permissions:^^^
        - `ls`` -ld ~/project/shared_dir`^^^ ^^^
        - ^^^Output:^^^
        - `drwxrws--- 2 labex shared_group 6 Jun  6 01:02 /home/labex/project/shared_dir`^^^ ^^^
        - ^^^Notice the^^^ `s` ^^^in the group's permission set.^^^
        - ^^^Now, create a file inside^^^ `shared_dir`^^^:^^^
        - `touch`` ~/project/shared_dir/new_file.txt`^^^ ^^^
        - ^^^Check the ownership of^^^ `new_file.txt`^^^:^^^
        - `ls`` -l ~/project/shared_dir/new_file.txt`^^^ ^^^
        - ^^^Output:^^^
        - `-rw-r--r-- 1 labex shared_group 0 Jun  6 01:02 /home/labex/project/shared_dir/new_file.txt`^^^ ^^^
        - ^^^Even though^^^ `labex`^^^'s primary group is^^^ `labex`^^^, the^^^ `new_file.txt` ^^^inherited the^^^ `shared_group` ^^^group ownership from^^^ `shared_dir` ^^^due to the SGID bit.^^^
        - ### ^^^**Sticky Bit Example**^^^
        - ^^^The^^^ `/tmp` ^^^directory is a classic example of a directory with the sticky bit set. Let's create a similar directory.^^^
        - ```
sudo 
``````
mkdir
``````
 ~/project/public_upload
sudo 
``````
chmod
``````
 1777 ~/project/public_upload
```^^^ ^^^
        - ^^^The^^^ `1` ^^^in^^^ `1777` ^^^is the octal value for the sticky bit.^^^ `777` ^^^grants full permissions to owner, group, and others.^^^
        - ^^^Verify the permissions:^^^
        - `ls`` -ld ~/project/public_upload`^^^ ^^^
        - ^^^Output:^^^
        - `drwxrwxrwt 2 root root 6 Jun  6 01:02 /home/labex/project/public_upload`^^^ ^^^
        - ^^^Notice the^^^ `t` ^^^in others' permission set.^^^
        - ^^^Now, let's simulate another user creating a file in this directory. Since we only have^^^ `labex` ^^^user, we'll create a file as^^^ `labex` ^^^and then try to delete it after changing its ownership to^^^ `root` ^^^(simulating another user).^^^
        - ^^^Create a file as^^^ `labex`^^^:^^^
        - `touch`` ~/project/public_upload/labex_file.txt`^^^ ^^^
        - ^^^Change its ownership to^^^ `root`^^^:^^^
        - `sudo ``chown`` root:root ~/project/public_upload/labex_file.txt`^^^ ^^^
        - ^^^Now, try to delete^^^ `labex_file.txt` ^^^as^^^ `labex`^^^:^^^
        - `rm`` ~/project/public_upload/labex_file.txt`^^^ ^^^
        - ^^^You will see a prompt asking if you want to remove the write-protected file, and after confirming with^^^ `y`^^^, you'll get an "Operation not permitted" error. This is because the sticky bit prevents users from deleting files they don't own within that directory, even though^^^ `labex` ^^^has write permission on the^^^ `public_upload` ^^^directory. Only^^^ `root` ^^^or the owner of^^^ `labex_file.txt` ^^^(^^^`root` ^^^in this case) can delete it.^^^
        - ^^^To clean up, you'll need^^^ `sudo` ^^^to remove^^^ `labex_file.txt`^^^:^^^
        - `sudo ``rm`` ~/project/public_upload/labex_file.txt`^^^ ^^^
        - ### ^^^**Cleaning Up**^^^
        - ^^^Remove the created files and directories, and the user/group:^^^
        - ```
sudo 
``````
rm
``````
 -f ~/project/secret_data.txt ~/project/read_secret.c ~/project/read_secret
sudo 
``````
rm
``````
 -rf ~/project/shared_dir ~/project/public_upload
sudo groupdel shared_group
```^^^ ^^^
        - 
        - # ^^^**Configure Default Permissions with umask**^^^
        - ^^^In this final step, you will learn about^^^ `umask`^^^, which controls the default permissions assigned to newly created files and directories. The^^^ `umask` ^^^(user file-creation mode mask) is a bitmask that^^^  ^^^ *removes* ^^^^^^ ^^^ ^^^permissions from the maximum possible permissions.^^^
        - ^^^The maximum permissions for a new file are^^^ `666` ^^^(rw-rw-rw-), meaning read and write for everyone. New files typically do not get execute permissions by default for security reasons.^^^
        - 
        - ^^^The maximum permissions for a new directory are^^^ `777` ^^^(rwxrwxrwx), meaning read, write, and execute for everyone.^^^
        - ^^^The^^^ `umask` ^^^value is subtracted from these maximum permissions to determine the actual default permissions.^^^
        - ^^^To view your current^^^ `umask` ^^^value, simply type^^^ `umask`^^^:^^^
        - `umask`^^^ ^^^
        - ^^^You will likely see^^^ `0002` ^^^or^^^ `0022`^^^. In this environment, it's^^^ `0022` ^^^for^^^ `labex` ^^^user.^^^
        - ^^^A^^^ `umask` ^^^of^^^ `0022` ^^^means:^^^
            - ^^^The first^^^ `0` ^^^is for special permissions (SUID, SGID, Sticky Bit), which are not affected by^^^ `umask` ^^^by default.^^^
            - ^^^The second^^^ `0` ^^^means no permissions are removed from the owner.^^^
            - ^^^The third^^^ `2` ^^^means the write permission (value 2) is removed from the group.^^^
            - ^^^The fourth^^^ `2` ^^^means the write permission (value 2) is removed from others.^^^
        - ^^^Let's calculate the default permissions with a^^^ `umask` ^^^of^^^ `0022`^^^:^^^
            - ^^^**For files (max 666):**^^^
                - ^^^Owner: 6 - 0 = 6 (^^^`rw-``(#3594f7)`^^^)^^^
                - ^^^Group: 6 - 2 = 4 (^^^`r--``(#3594f7)`^^^)^^^
                - ^^^Others: 6 - 2 = 4 (^^^`r--``(#3594f7)`^^^)^^^
                - ^^^Resulting file permissions:^^^ `644` ^^^(^^^`rw-r--r--`^^^)^^^
            - ^^^**For directories (max 777):**^^^
                - ^^^Owner: 7 - 0 = 7 (^^^`rwx``(#3594f7)`^^^)^^^
                - ^^^Group: 7 - 2 = 5 (^^^`r-x``(#3594f7)`^^^)^^^
                - ^^^Others: 7 - 2 = 5 (^^^`r-x``(#3594f7)`^^^)^^^
                - ^^^Resulting directory permissions:^^^ `755` ^^^(^^^`rwxr-xr-x`^^^)^^^
        - ^^^Let's test this. Create a new file and directory:^^^
        - ```
touch
``````
 ~/project/new_file_umask.txt

``````
mkdir
``````
 ~/project/new_dir_umask
```^^^ ^^^
        - ^^^Check their permissions:^^^
        - ```
ls
``````
 -l ~/project/new_file_umask.txt

``````
ls
``````
 -ld ~/project/new_dir_umask
```^^^ ^^^
        - ^^^You should see permissions like^^^ `-rw-r--r--` ^^^for the file and^^^ `drwxr-xr-x` ^^^for the directory, confirming the^^^ `0022` `umask` ^^^effect.^^^
        - ^^^Now, let's change the^^^ `umask` ^^^to^^^ `0077`^^^. This^^^ `umask` ^^^will remove all group and others permissions.^^^
        - `umask`` 0077`^^^ ^^^
        - ^^^Verify the^^^ `umask` ^^^has changed:^^^
        - `umask`^^^ ^^^
        - ^^^Output:^^^
        - `0077`^^^ ^^^
        - ^^^Now, let's calculate the default permissions with a^^^ `umask` ^^^of^^^ `0077`^^^:^^^
            - ^^^**For files (max 666):**^^^
                - ^^^Owner: 6 - 0 = 6 (^^^`rw-``(#3594f7)`^^^)^^^
                - ^^^Group: 6 - 7 = -1 (effectively 0,^^^ `---``(#3594f7)`^^^)^^^
                - ^^^Others: 6 - 7 = -1 (effectively 0,^^^ `---``(#3594f7)`^^^)^^^
                - ^^^Resulting file permissions:^^^ `600` ^^^(^^^`rw-------`^^^)^^^
            - ^^^**For directories (max 777):**^^^
                - ^^^Owner: 7 - 0 = 7 (^^^`rwx``(#3594f7)`^^^)^^^
                - ^^^Group: 7 - 7 = 0 (^^^`---``(#3594f7)`^^^)^^^
                - ^^^Others: 7 - 7 = 0 (^^^`---``(#3594f7)`^^^)^^^
                - ^^^Resulting directory permissions:^^^ `700` ^^^(^^^`rwx------`^^^)^^^
        - ^^^Let's test this new^^^ `umask`^^^. Create another new file and directory:^^^
        - ```
touch
``````
 ~/project/restricted_file.txt

``````
mkdir
``````
 ~/project/restricted_dir
```^^^ ^^^
        - ^^^Check their permissions:^^^
        - ```
ls
``````
 -l ~/project/restricted_file.txt

``````
ls
``````
 -ld ~/project/restricted_dir
```^^^ ^^^
        - ^^^You should now see permissions like^^^ `-rw-------` ^^^for the file and^^^ `drwx------` ^^^for the directory.^^^
        - ^^^The^^^ `umask` ^^^setting is typically configured in shell initialization files (like^^^ `~/.bashrc` ^^^or^^^ `/etc/profile`^^^) to apply automatically when a user logs in. For this lab, the^^^ `umask` ^^^change is temporary and only applies to the current terminal session.^^^
        - ^^^To revert the^^^ `umask` ^^^to its default for the^^^ `labex` ^^^user, you can simply set it back to^^^ `0022`^^^:^^^
        - `umask`` 0022`^^^ ^^^
        - ^^^Finally, clean up the files and directories created in this step:^^^
        - ```
rm
``````
 ~/project/new_file_umask.txt ~/project/restricted_file.txt

``````
rmdir
``````
 ~/project/new_dir_umask ~/project/restricted_dir
```^^^ ^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, we delved into the fundamental aspects of managing Linux file system permissions. We began by mastering the^^^ `ls -l` ^^^command to interpret file and directory permissions, understanding the significance of user, group, and others categories, and the read, write, and execute permissions. This foundational knowledge was then applied to modify permissions using^^^ `chmod` ^^^in both symbolic and octal modes, providing flexibility in setting access rights.^^^
        - ^^^Furthermore, we learned how to change file ownership with the^^^ `chown` ^^^command, which is crucial for assigning administrative control. The lab also covered the understanding and application of special permissions (SUID, SGID, and Sticky Bit), which offer advanced control over execution and file creation behaviors. Finally, we explored how to configure default permissions for newly created files and directories using^^^ `umask`^^^, ensuring consistent permission settings across the system.^^^
    7. Monitor Processes in Red Hat Enterprise Linux
        - Understand Process States and Lifecycle with ps and top
        - Control Background and Foreground Jobs
        - Terminate Processes with kill, killall, and pkill
        - Monitor System Load and CPU Usage with uptime and lscpu
        - Analyze Process Activity with top
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience in monitoring and managing Linux processes, a fundamental skill for any system administrator or developer. You will learn to understand process states and lifecycles using^^^ `ps` ^^^and^^^ `top`^^^, control background and foreground jobs, and terminate processes effectively with^^^ `kill`^^^,^^^ `killall`^^^, and^^^ `pkill`^^^. Furthermore, you will explore how to monitor system load and CPU usage using^^^ `uptime` ^^^and^^^ `lscpu`^^^, and analyze process activity in detail with^^^ `top`^^^. This lab will equip you with the essential tools and knowledge to efficiently manage processes and maintain system health on RHEL.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level lab with a^^^ ^^^100%^^^ ^^^completion rate. It has received a^^^ ^^^100%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Understand Process States and Lifecycle with ps and top**^^^
        - ^^^In this step, you will learn about Linux process states and their lifecycle. Understanding process states is crucial for monitoring and managing system resources effectively. You will use the^^^ `ps` ^^^and^^^ `top` ^^^commands to observe processes and their states.^^^
        - ^^^Every process in Linux has a state that describes its current activity. These states are defined by the kernel and indicate whether a process is running, sleeping, stopped, or in other conditions.^^^
        - ^^^Let's start by examining process states using the^^^ `ps` ^^^command. The^^^ `ps` ^^^command reports a snapshot of the current processes.^^^
        - ^^^First, open your terminal. You can do this by clicking on the terminal icon on the desktop or by pressing^^^ `Ctrl+Alt+T`^^^. Your default working directory is^^^ `~/project`^^^.^^^
        - ^^^To see all processes running on your system, including those without a controlling terminal, use the^^^ `ps aux` ^^^command. The^^^ `aux` ^^^options display processes owned by all users (^^^`a`^^^), processes without a controlling terminal (^^^`x`^^^), and show a user-oriented format (^^^`u`^^^).^^^
        - `ps aux`^^^ ^^^
        - ^^^You will see a long list of processes. Pay attention to the^^^ `STAT` ^^^column, which shows the state of each process. Common states you might observe include:^^^
            - `R`^^^: Running or Runnable (on CPU or waiting to run)^^^
            - `S`^^^: Interruptible Sleep (waiting for an event to complete)^^^
            - `D`^^^: Uninterruptible Sleep (waiting for I/O, cannot be interrupted)^^^
            - `T`^^^: Stopped (suspended by a signal)^^^
            - `Z`^^^: Zombie (process terminated, but parent hasn't reaped its exit status)^^^
        - ```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.2 171820 16140 ?        Ss   HH:MM   0:01 /usr/lib/systemd/systemd ...
root           2  0.0  0.0      0     0 ?        S    HH:MM   0:00 [kthreadd]
labex       3448  0.0  0.2 266904  3836 pts/0    R+   HH:MM   0:00 ps aux
...output omitted...
```^^^ ^^^
        - ^^^Next, let's use the^^^ `ps -ef` ^^^command. This command provides a full listing (^^^`f`^^^) of all processes (^^^`e`^^^), showing more details like the parent process ID (^^^`PPID`^^^), CPU utilization (^^^`C`^^^), start time (^^^`STIME`^^^), and the command (^^^`CMD`^^^).^^^
        - `ps -ef`^^^ ^^^
        - ^^^This output is often used to see the parent-child relationships between processes, although it doesn't explicitly show a tree structure.^^^
        - ```
UID        PID  PPID  C STIME TTY          TIME CMD
root           1       0  0 HH:MM ?        00:00:01 /usr/lib/systemd/systemd ...
root           2       0  0 HH:MM ?        00:00:00 [kthreadd]
root           3       2  0 HH:MM ?        00:00:00 [rcu_gp]
...output omitted...
```^^^ ^^^
        - ^^^To visualize the process hierarchy, you can use the^^^ `ps --forest` ^^^option. This displays processes in a tree format, making it easier to understand which processes spawned others.^^^
        - `ps --forest`^^^ ^^^
        - ^^^This command is particularly useful for debugging and understanding how different services and applications are structured on your system.^^^
        - ```
PID TTY          TIME CMD
 2768 pts/0    00:00:00 bash
 5947 pts/0    00:00:00  \_ sleep 10000
 6377 pts/0    00:00:00  \_ ps --forest
...output omitted...
```^^^ ^^^
        - ^^^Now, let's explore the^^^ `top` ^^^command, which provides a dynamic real-time view of a running system. It displays a summary of system information and a list of processes or threads currently being managed by the Linux kernel.^^^
        - ^^^Run the^^^ `top` ^^^command:^^^
        - `top`^^^ ^^^
        - ^^^You will see an interactive display. The top section provides system summary information, including uptime, load average, tasks summary, CPU statistics, and memory usage. The lower section lists individual processes, sorted by CPU usage by default.^^^
        - ^^^In the^^^ `top` ^^^output, observe the^^^ `S` ^^^column for process states, similar to^^^ `ps`^^^. You can also see^^^ `%CPU` ^^^(CPU usage percentage) and^^^ `%MEM` ^^^(memory usage percentage) for each process.^^^
        - ```
top - HH:MM:SS up DD min,  X users,  load average: X.XX, X.XX, X.XX
Tasks: XXX total,   X running, XXX sleeping,   X stopped,   X zombie
%Cpu(s):  X.X us,  X.X sy,  X.X ni, XX.X id,  X.X wa,  X.X hi,  X.X si,  X.X st
MiB Mem :   XXXX.X total,   XXXX.X free,    XXX.X used,    XXX.X buff/cache
MiB Swap:   XXXX.X total,   XXXX.X free,      X.X used.   XXXX.X avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
XXXX labex     20   0  XXXXXX   XXXX   XXXX R   X.X   X.X   0:00.0X top
...output omitted...
```^^^ ^^^
        - ^^^While^^^ `top` ^^^is running, you can press^^^ `q` ^^^to quit and return to your terminal prompt.^^^
        - ^^^Understanding these commands and the information they provide is fundamental for monitoring and troubleshooting processes on a Linux system.^^^
        - 
        - # ^^^**Control Background and Foreground Jobs**^^^
        - ^^^In this step, you will learn how to manage jobs in the background and foreground within your shell session. This is a fundamental skill for efficient command-line usage, allowing you to run long-running tasks without tying up your terminal.^^^
        - ^^^A "job" in the context of a shell refers to a command or a pipeline of commands that the shell is managing. You can run jobs in the background, bring them to the foreground, or suspend them.^^^
        - ^^^Let's start by running a simple command in the background. We'll use the^^^ `sleep` ^^^command, which simply waits for a specified amount of time.^^^
        - ^^^To run^^^ `sleep 10000` ^^^(which waits for 10000 seconds) in the background, append an ampersand (^^^`&`^^^) to the command:^^^
        - `sleep`` 10000 &`^^^ ^^^
        - ^^^When you press Enter, the shell will immediately return to the prompt, and the^^^ `sleep` ^^^command will be running in the background. You will see output similar to this, indicating the job number and its Process ID (PID):^^^
        - `[1] 5947`^^^ ^^^
        - ^^^The^^^ `[1]` ^^^indicates that this is job number 1 in your current shell session, and^^^ `5947` ^^^is the PID of the^^^ `sleep` ^^^process.^^^
        - ^^^To view a list of all jobs currently managed by your shell, use the^^^ `jobs` ^^^command:^^^
        - `jobs`^^^ ^^^
        - ^^^You should see the^^^ `sleep` ^^^command listed as a running background job:^^^
        - `[1]+ Running    sleep 10000 &`^^^ ^^^
        - ^^^The^^^ `+` ^^^next to^^^ `[1]` ^^^indicates that this is the current job (the one that would be acted upon by default if you didn't specify a job number).^^^
        - ^^^Now, let's bring this background job to the foreground. This means the job will take control of your terminal again. Use the^^^ `fg` ^^^command followed by the job number (prefixed with^^^ `%`^^^):^^^
        - `fg`` %1`^^^ ^^^
        - ^^^The^^^ `sleep 10000` ^^^command will now be in the foreground. Your terminal will be occupied by this command, and you won't get a prompt until it finishes or is suspended.^^^
        - `sleep 10000`^^^ ^^^
        - ^^^While a command is running in the foreground, you can send it to the background and suspend it by pressing^^^ `Ctrl+Z`^^^. This sends a^^^ `SIGTSTP` ^^^signal to the process.^^^
        - ^^^Press^^^ `Ctrl+Z` ^^^now:^^^
        - `Z`^^^ ^^^
        - ^^^You will see output indicating that the job has been stopped and moved to the background:^^^
        - `[1]+  Stopped                 sleep 10000`^^^ ^^^
        - ^^^Now, if you run^^^ `jobs` ^^^again, you will see that the^^^ `sleep` ^^^command is in a^^^ `Stopped` ^^^state:^^^
        - `jobs`^^^ ^^^
        - `[1]+ Stopped                 sleep 10000`^^^ ^^^
        - ^^^To resume a stopped background job, you can use the^^^ `bg` ^^^command followed by the job number. This will restart the job in the background.^^^
        - `bg`` %1`^^^ ^^^
        - ^^^The job will now be running in the background again:^^^
        - `[1]+ sleep 10000 &`^^^ ^^^
        - ^^^Finally, let's clean up the background job. You can terminate a background job using the^^^ `kill` ^^^command with its PID, or by bringing it to the foreground and then terminating it (e.g., with^^^ `Ctrl+C`^^^). For now, let's bring it to the foreground and terminate it.^^^
        - `fg`` %1`^^^ ^^^
        - ^^^Now that^^^ `sleep 10000` ^^^is in the foreground, press^^^ `Ctrl+C` ^^^to terminate it. This sends a^^^ `SIGINT` ^^^signal to the process.^^^
        - `C`^^^ ^^^
        - ^^^You will see a message indicating that the job has been terminated:^^^
        - `[1]+  Terminated              sleep 10000`^^^ ^^^
        - ^^^If you run^^^ `jobs` ^^^again, you should see that there are no more jobs listed:^^^
        - `jobs`^^^ ^^^
        - `(no output)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^This demonstrates the basic workflow of managing jobs in the background and foreground, which is essential for multitasking in the terminal.^^^
        - 
        - # ^^^**Terminate Processes with kill, killall, and pkill**^^^
        - ^^^In this step, you will learn how to terminate processes using the^^^ `kill`^^^,^^^ `killall`^^^, and^^^ `pkill` ^^^commands. These commands are essential for managing system resources and stopping misbehaving applications.^^^
        - ^^^Processes in Linux respond to signals. A signal is a software interrupt delivered to a process. Different signals have different meanings, such as terminating a process, suspending it, or making it reload its configuration.^^^
        - ^^^First, let's understand some fundamental process management signals:^^^
            - ^^^**SIGTERM (15)**^^^^^^: The default signal sent by^^^ `kill``(#3594f7)`^^^. It's a "polite" request to terminate. The process can catch this signal, clean up, and then exit.^^^
            - ^^^**SIGKILL (9)**^^^^^^: An "unblockable" signal that forces immediate termination. The process cannot ignore or handle this signal. Use it as a last resort.^^^
            - ^^^**SIGHUP (1)**^^^^^^: Often used to tell a process to reload its configuration files without restarting.^^^
            - ^^^**SIGINT (2)**^^^^^^: Sent by pressing^^^ `Ctrl+C``(#3594f7)`^^^, typically used to interrupt a foreground process.^^^
            - ^^^**SIGSTOP (19)**^^^^^^: Suspends a process. It cannot be blocked or handled.^^^
            - ^^^**SIGCONT (18)**^^^^^^: Resumes a stopped process.^^^
        - ^^^You can list all available signals and their numbers using^^^ `kill -l`^^^:^^^
        - `kill`` -l`^^^ ^^^
        - ^^^You will see a list of signals like this:^^^
        - ```
1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
...output omitted...
```^^^ ^^^
        - ### ^^^**Using**^^^ `**kill**`
        - ^^^The^^^ `kill` ^^^command sends a specified signal to a process identified by its Process ID (PID).^^^
        - ^^^Let's create a few background processes to practice terminating them. We'll use^^^ `sleep` ^^^commands again.^^^
        - ```
sleep
``````
 300 &

``````
sleep
``````
 301 &

``````
sleep
``````
 302 &
```^^^ ^^^
        - ^^^Now, use^^^ `jobs` ^^^to see their job numbers and PIDs:^^^
        - `jobs`^^^ ^^^
        - ```
[1] 1234
[2] 1235
[3] 1236
```^^^ ^^^
        - ^^^(Note: Your PIDs will be different.)^^^
        - ^^^Let's find the PID of the first^^^ `sleep` ^^^process. You can use^^^ `ps aux | grep sleep` ^^^and look for the PID associated with^^^ `sleep 300`^^^.^^^
        - `ps aux | grep ``sleep`^^^ ^^^
        - ^^^You will see output similar to this. Identify the PID for^^^ `sleep 300`^^^. For example, if the PID is^^^ `1234`^^^:^^^
        - ```
labex       1234  0.0  0.0   2200   680 pts/0    S    HH:MM   0:00 sleep 300
labex       1235  0.0  0.0   2200   680 pts/0    S    HH:MM   0:00 sleep 301
labex       1236  0.0  0.0   2200   680 pts/0    S    HH:MM   0:00 sleep 302
labex       1237  0.0  0.0   6000  1000 pts/0    S+   HH:MM   0:00 grep sleep
```^^^ ^^^
        - ^^^To terminate^^^ `sleep 300` ^^^using the default^^^ `SIGTERM` ^^^signal, use^^^ `kill` ^^^followed by its PID. Replace^^^ `1234` ^^^with the actual PID you found:^^^
        - `kill`` 1234`^^^ ^^^
        - ^^^You might see a message like^^^ `[1]+ Terminated sleep 300`^^^. Verify it's gone using^^^ `jobs` ^^^or^^^ `ps aux | grep sleep`^^^:^^^
        - `jobs`^^^ ^^^
        - ```
[2]- Running    sleep 301 &
[3]+ Running    sleep 302 &
```^^^ ^^^
        - ^^^Now, let's forcefully terminate^^^ `sleep 301` ^^^using^^^ `SIGKILL`^^^. Find its PID (e.g.,^^^ `1235`^^^) and use^^^ `kill -9` ^^^or^^^ `kill -SIGKILL`^^^:^^^
        - `kill`` -9 1235`^^^ ^^^
        - ^^^You will likely see^^^ `[2]- Killed sleep 301`^^^. Verify again:^^^
        - `jobs`^^^ ^^^
        - `[3]+ Running    sleep 302 &`^^^ ^^^
        - ### ^^^**Using**^^^ `**killall**`
        - ^^^The^^^ `killall` ^^^command terminates processes by their name, rather than their PID. It sends a signal to all processes that match the specified command name.^^^
        - ^^^Let's create a few more^^^ `sleep` ^^^processes:^^^
        - ```
sleep
``````
 303 &

``````
sleep
``````
 304 &

``````
sleep
``````
 305 &
```^^^ ^^^
        - ^^^Verify they are running:^^^
        - `jobs`^^^ ^^^
        - ```
[3] Running    sleep 302 &
[4] Running    sleep 303 &
[5] Running    sleep 304 &
[6] Running    sleep 305 &
```^^^ ^^^
        - ^^^Now, use^^^ `killall` ^^^to terminate all^^^ `sleep` ^^^processes. By default,^^^ `killall` ^^^sends^^^ `SIGTERM`^^^.^^^
        - `killall ``sleep`^^^ ^^^
        - ^^^You will see messages for each terminated^^^ `sleep` ^^^process. Verify that all^^^ `sleep` ^^^processes are gone:^^^
        - `jobs`^^^ ^^^
        - `(no output)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ### ^^^**Using**^^^ `**pkill**`
        - ^^^The^^^ `pkill` ^^^command is similar to^^^ `killall` ^^^but offers more advanced selection criteria, including pattern matching for command names, user IDs, group IDs, and controlling terminals. It's very powerful for targeting specific sets of processes.^^^
        - ^^^Let's create some new^^^ `sleep` ^^^processes for^^^ `pkill`^^^:^^^
        - ```
sleep
``````
 306 &

``````
sleep
``````
 307 &

``````
sleep
``````
 308 &
```^^^ ^^^
        - ^^^Verify they are running:^^^
        - `jobs`^^^ ^^^
        - ```
[1] Running    sleep 306 &
[2] Running    sleep 307 &
[3] Running    sleep 308 &
```^^^ ^^^
        - ^^^To terminate all^^^ `sleep` ^^^processes owned by the current user (^^^`labex`^^^), you can use^^^ `pkill -u labex sleep`^^^:^^^
        - `pkill -u labex ``sleep`^^^ ^^^
        - ^^^This command will terminate all^^^ `sleep` ^^^processes that belong to the^^^ `labex` ^^^user.^^^
        - ^^^Verify that all^^^ `sleep` ^^^processes are gone:^^^
        - `jobs`^^^ ^^^
        - `(no output)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^You can also use^^^ `pkill` ^^^with a pattern. For example, if you had processes named^^^ `my_app_v1` ^^^and^^^ `my_app_v2`^^^, you could terminate both with^^^ `pkill my_app`^^^.^^^
        - ^^^These commands provide flexible ways to manage and terminate processes, from targeting a single process by its PID to terminating multiple processes based on their name or other attributes. Always be cautious when using^^^ `kill -9` ^^^or^^^ `SIGKILL`^^^, as it can lead to data loss if the process doesn't have a chance to clean up.^^^
        - 
        - # ^^^**Monitor System Load and CPU Usage with uptime and lscpu**^^^
        - ^^^In this step, you will learn how to monitor your system's load average and CPU usage using the^^^ `uptime` ^^^and^^^ `lscpu` ^^^commands. Understanding these metrics is crucial for assessing system performance and identifying potential bottlenecks.^^^
        - ### ^^^**Understanding Load Average with**^^^ `**uptime**`
        - ^^^The^^^ `uptime` ^^^command provides a quick overview of how long your system has been running, how many users are logged in, and most importantly, the system's load average. The load average indicates the average number of processes that are either in a runnable or uninterruptible state over a period of time.^^^
        - ^^^Execute the^^^ `uptime` ^^^command:^^^
        - `uptime`^^^ ^^^
        - ^^^You will see output similar to this:^^^
        - ` HH:MM:SS up DD min,  X users,  load average: X.XX, X.XX, X.XX`^^^ ^^^
        - ^^^Let's break down the output:^^^
            - `HH:MM:SS`^^^: The current time.^^^
            - `up DD min`^^^: How long the system has been running (uptime).^^^
            - `X users`^^^: The number of users currently logged in.^^^
            - `load average: X.XX, X.XX, X.XX`^^^: These three numbers represent the system load average over the last 1, 5, and 15 minutes, respectively.^^^
        - ^^^A load average of^^^ `1.00` ^^^on a single-core CPU means the CPU is fully utilized. On a multi-core CPU, a load average equal to the number of CPU cores means the system is fully utilized. For example, on a 4-core CPU, a load average of^^^ `4.00` ^^^indicates full utilization. If the load average consistently exceeds the number of CPU cores, it suggests that your system is overloaded and processes are waiting for CPU time.^^^
        - ### ^^^**Determining CPU Cores with**^^^ `**lscpu**`
        - ^^^To properly interpret the load average, you need to know how many logical CPU cores your system has. The^^^ `lscpu` ^^^command provides detailed information about the CPU architecture.^^^
        - ^^^Execute the^^^ `lscpu` ^^^command:^^^
        - `lscpu`^^^ ^^^
        - ^^^You will see extensive output. Look for the^^^ `CPU(s):``(#3594f7)` ^^^line, which tells you the total number of logical CPUs available. Also,^^^ `Core(s) per socket:``(#3594f7)` ^^^and^^^ `Socket(s):``(#3594f7)` ^^^can help you understand the physical layout.^^^
        - ```
Architecture:        x86_64
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  2
Core(s) per socket:  2
Socket(s):           1
NUMA node(s):        1
...output omitted...
```^^^ ^^^
        - ^^^In the example above,^^^ `CPU(s): 4``(#3594f7)` ^^^indicates that this system has 4 logical CPU cores.^^^
        - ### ^^^**Interpreting Load Average and CPU Cores**^^^
        - ^^^Let's combine the information from^^^ `uptime` ^^^and^^^ `lscpu`^^^. Suppose your^^^ `uptime` ^^^output shows a load average of^^^ `2.92, 4.48, 5.20` ^^^and^^^ `lscpu` ^^^shows^^^ `CPU(s): 4`^^^.^^^
        - ^^^To get the per-CPU load average, you divide each load average number by the total number of logical CPUs:^^^
            - ^^^**Last 1 minute:**^^^ `2.92 / 4 = 0.73`
            - ^^^**Last 5 minutes:**^^^ `4.48 / 4 = 1.12`
            - ^^^**Last 15 minutes:**^^^ `5.20 / 4 = 1.30`
        - ^^^Based on these calculations:^^^
            - ^^^In the last 1 minute, the CPUs were utilized at about 73% of their capacity.^^^
            - ^^^In the last 5 minutes, the system was overloaded by about 12% (^^^`1.12 - 1.00 = 0.12``(#3594f7)`^^^). This means processes were waiting for CPU time.^^^
            - ^^^In the last 15 minutes, the system was overloaded by about 30% (^^^`1.30 - 1.00 = 0.30``(#3594f7)`^^^).^^^
        - ^^^This analysis suggests that the system was under significant load over the last 5 and 15 minutes, but the load has decreased in the last minute. This kind of trend analysis is crucial for understanding system health.^^^
        - ^^^These two commands,^^^ `uptime` ^^^and^^^ `lscpu`^^^, are simple yet powerful tools for quickly assessing the overall health and performance of your Linux system.^^^
        - 
        - # ^^^**Analyze Process Activity with top**^^^
        - ^^^In this step, you will delve deeper into using the^^^ `top` ^^^command to analyze process activity. While^^^ `top` ^^^provides a real-time overview, it also offers powerful interactive features to sort, filter, and manage processes.^^^
        - ^^^Recall from a previous step that^^^ `top` ^^^provides a dynamic view of your system. Let's start^^^ `top` ^^^again:^^^
        - `top`^^^ ^^^
        - ^^^You will see the familiar^^^ `top` ^^^interface. The top section provides system-wide statistics, and the lower section lists processes.^^^
        - ### ^^^**Understanding**^^^ `**top**` ^^^**Columns**^^^
        - ^^^Let's review the default columns in the process list:^^^
            - ^^^**PID**^^^^^^: Process ID.^^^
            - ^^^**USER**^^^^^^: The owner of the process.^^^
            - ^^^**PR**^^^^^^: Priority of the process.^^^
            - ^^^**NI**^^^^^^: Nice value of the process (lower nice value means higher priority).^^^
            - ^^^**VIRT**^^^^^^: Virtual memory used by the process.^^^
            - ^^^**RES**^^^^^^: Resident memory (physical RAM) used by the process.^^^
            - ^^^**SHR**^^^^^^: Shared memory used by the process.^^^
            - ^^^**S**^^^^^^: Process state (R=Running, S=Sleeping, D=Uninterruptible Sleep, T=Stopped, Z=Zombie).^^^
            - ^^^**%CPU**^^^^^^: CPU usage percentage since the last update.^^^
            - ^^^**%MEM**^^^^^^: Memory usage percentage (RES / total physical memory).^^^
            - ^^^**TIME+**^^^^^^: Total CPU time used by the process since it started.^^^
            - ^^^**COMMAND**^^^^^^: The command name that started the process.^^^
        - ### ^^^**Interactive Keystrokes in**^^^ `**top**`
        - `top` ^^^is highly interactive. You can press various keys to change its display and interact with processes.^^^
            1. ^^^**Sorting Processes**^^^^^^:^^^
                - ^^^Press^^^ `Shift+P` ^^^(capital P) to sort processes by CPU usage (^^^`%CPU`^^^), which is often the default.^^^
                - ^^^Press^^^ `Shift+M` ^^^(capital M) to sort processes by memory usage (^^^`%MEM`^^^).^^^
                - ^^^Press^^^ `Shift+T` ^^^(capital T) to sort processes by^^^ `TIME+`^^^.^^^
                - ^^^Try pressing^^^ `Shift+M` ^^^now to sort by memory usage. Observe how the process list reorders. Then press^^^ `Shift+P` ^^^to return to sorting by CPU.^^^
            2. ^^^**Filtering by User**^^^^^^:^^^
                - ^^^Press^^^ `u` ^^^(lowercase u).^^^ `top` ^^^will prompt you for a username. Type^^^ `labex` ^^^and press Enter.^^^
                - ^^^Now,^^^ `top` ^^^will only display processes owned by the^^^ `labex` ^^^user. This is very useful for focusing on your own processes.^^^
                - ^^^To clear the filter and show all users again, press^^^ `u` ^^^and then press Enter without typing a username.^^^
            3. ^^^**Changing Update Interval**^^^^^^:^^^
                - ^^^By default,^^^ `top` ^^^updates every 3 seconds. You can change this interval.^^^
                - ^^^Press^^^ `s` ^^^(lowercase s).^^^ `top` ^^^will prompt you for a delay time. Enter^^^ `1` ^^^(for 1 second) and press Enter.^^^
                - ^^^Observe how the display updates more frequently.^^^
                - ^^^You can change it back to^^^ `3` ^^^seconds by pressing^^^ `s` ^^^again and entering^^^ `3`^^^.^^^
            4. ^^^**Killing a Process**^^^^^^:^^^
                - ^^^You can terminate a process directly from^^^ `top`^^^.^^^
                - ^^^First, let's create a^^^ `sleep` ^^^process in the background in a new terminal tab or window, or by pressing^^^ `Ctrl+Z` ^^^in your current terminal, then^^^ `bg` ^^^to put^^^ `top` ^^^in the background, then run^^^ `sleep 600 &`^^^, then^^^ `fg` ^^^to bring^^^ `top` ^^^back to the foreground.^^^
                - ^^^Alternatively, you can open a new terminal tab (e.g.,^^^ `Ctrl+Shift+T``(#3594f7)` ^^^in many terminals) and run^^^ `sleep 600 &``(#3594f7)` ^^^there.^^^
                - ^^^Once you have a^^^ `sleep` ^^^process running, go back to your^^^ `top` ^^^terminal.^^^
                - ^^^Press^^^ `k` ^^^(lowercase k).^^^ `top` ^^^will prompt you for the PID of the process to kill.^^^
                - ^^^Find the PID of your^^^ `sleep 600` ^^^process in the^^^ `top` ^^^list. Enter that PID and press Enter.^^^
                - `top` ^^^will then ask for the signal to send. The default is^^^ `15` ^^^(SIGTERM). Press Enter to send^^^ `SIGTERM`^^^.^^^
                - ^^^The^^^ `sleep` ^^^process should disappear from the list. If it doesn't, you can try^^^ `k` ^^^again and send signal^^^ `9` ^^^(SIGKILL).^^^
            5. ^^^**Renicing a Process**^^^^^^:^^^
                - ^^^Renicing changes the priority of a process. A lower nice value means higher priority.^^^
                - ^^^Press^^^ `r` ^^^(lowercase r).^^^ `top` ^^^will prompt for a PID and then a nice value (e.g.,^^^ `-10` ^^^for higher priority,^^^ `10` ^^^for lower priority).^^^
                - ^^^This is an advanced feature for managing system resources. For this lab, simply press^^^ `r`^^^, then^^^ `Enter` ^^^twice to cancel the operation without changing anything.^^^
            6. ^^^**Quitting**^^^ `**top**`^^^:^^^
                - ^^^When you are finished, press^^^ `q` ^^^(lowercase q) to quit^^^ `top` ^^^and return to your terminal prompt.^^^
        - `top` ^^^is an indispensable tool for system administrators and users alike. Mastering its interactive features allows for quick and effective diagnosis of system performance issues and process management.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, you learned fundamental concepts of Linux process management. You began by understanding process states and their lifecycle using^^^ `ps` ^^^and^^^ `top` ^^^commands, observing how processes transition between states like Running (R), Interruptible Sleep (S), and Stopped (T). You practiced identifying common process states and interpreting the output of^^^ `ps aux` ^^^and^^^ `ps -ef` ^^^to gain insights into system processes.^^^
        - ^^^Furthermore, you explored methods for controlling background and foreground jobs, which is crucial for efficient terminal usage. You also mastered terminating processes using various commands such as^^^ `kill`^^^,^^^ `killall`^^^, and^^^ `pkill`^^^, understanding their different applications for graceful or forceful termination. Finally, you learned to monitor system load and CPU usage with^^^ `uptime` ^^^and^^^ `lscpu`^^^, and to analyze detailed process activity using^^^ `top`^^^, providing a comprehensive overview of system performance and resource utilization.^^^
    8. Control Services in Red Hat Enterprise Linux
        - View All Loaded and Active Services with systemctl
        - Check Status of a Specific Service with systemctl status
        - Start, Stop, and Restart a Service with systemctl
        - Reload Service Configuration with systemctl reload
        - Enable and Disable Services at Boot with systemctl
        - Mask and Unmask Services with systemctl
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience managing system services on RHEL using the^^^ `systemctl` ^^^command. You will learn to view all loaded and active services, check the status of specific services, and control their runtime behavior by starting, stopping, and restarting them. Furthermore, you will explore how to reload service configurations, enable or disable services for automatic startup at boot, and understand the advanced concepts of masking and unmasking services to prevent their activation.^^^
        - ^^^This practical guide will equip you with essential skills for system administration, enabling you to effectively monitor and manage the lifecycle of services crucial for the operation of your RHEL system.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level lab with a^^^ ^^^85%^^^ ^^^completion rate. It has received a^^^ ^^^100%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**View All Loaded and Active Services with systemctl**^^^
        - ^^^In this step, you will learn how to identify automatically started system processes using the^^^ `systemctl` ^^^command.^^^ `systemctl` ^^^is the primary tool for managing^^^ `systemd` ^^^services in Red Hat Enterprise Linux.^^^
        - ^^^First, let's explore how to list all currently loaded and active service units. The^^^ `systemctl list-units --type=service` ^^^command is used for this purpose. This command displays service units that the^^^ `systemd` ^^^daemon has successfully parsed and loaded into memory, and which are currently active.^^^
        - ^^^Open your terminal in the RHEL environment. You are already logged in as the^^^ `labex` ^^^user, and your current directory is^^^ `~/project`^^^.^^^
        - ^^^Execute the following command to list all loaded and active service units:^^^
        - `systemctl list-units --``type``=service`^^^ ^^^
        - ^^^You will see output similar to this, showing various services and their states:^^^
        - ```
UNIT                  LOAD    ACTIVE  SUB      DESCRIPTION
atd.service           loaded  active  running  Job spooling tools
auditd.service        loaded  active  running  Security Auditing Service
chronyd.service       loaded  active  running  NTP client/server
crond.service         loaded  active  running  Command Scheduler
dbus-broker.service   loaded  active  running  D-Bus System Message Bus
...output omitted...
```^^^ ^^^
        - ^^^Let's break down the columns in the output:^^^
            - ^^^**UNIT**^^^^^^: This is the name of the service unit, typically ending with^^^ `.service`^^^.^^^
            - ^^^**LOAD**^^^^^^: Indicates whether the^^^ `systemd` ^^^daemon successfully parsed the unit's configuration and loaded it into memory.^^^ `loaded` ^^^means it was successful.^^^
            - ^^^**ACTIVE**^^^^^^: This is the high-level activation state of the unit.^^^ `active` ^^^generally means the unit started successfully.^^^
            - ^^^**SUB**^^^^^^: This is the low-level activation state, providing more detailed information. For running services,^^^ `running` ^^^is common.^^^
            - ^^^**DESCRIPTION**^^^^^^: A brief description of what the service does.^^^
        - ^^^Press^^^ `q` ^^^to exit the command.^^^
        - ^^^Next, you can use the^^^ `--all` ^^^option with^^^ `systemctl list-units --type=service` ^^^to list all service units regardless of their activation states (active, inactive, failed, etc.). This can be useful for seeing services that are installed but not currently running.^^^
        - ^^^Execute the following command:^^^
        - `systemctl list-units --``type``=service --all`^^^ ^^^
        - ^^^The output will include services that are^^^ `inactive` ^^^or in other states, providing a more comprehensive view:^^^
        - ```
UNIT                          LOAD      ACTIVE   SUB     DESCRIPTION
  atd.service                 loaded    active   running Job spooling tools
  auditd.service              loaded    active   running Security Auditing ...
  auth-rpcgss-module.service  loaded    inactive dead    Kernel Module ...
  chronyd.service             loaded    active   running NTP client/server
  cpupower.service            loaded    inactive dead    Configure CPU power ...
  crond.service               loaded    active   running Command Scheduler
  dbus-broker.service         loaded    active   running  D-Bus System Message Bus
● display-manager.service     not-found inactive dead    display-manager.service
...output omitted...
```^^^ ^^^
        - ^^^Finally, to see the state of^^^  ^^^ *all* ^^^^^^ ^^^ ^^^installed unit files, including those that are not loaded or active, you can use^^^ `systemctl list-unit-files --type=service`^^^. This command shows whether a service is^^^ `enabled` ^^^(starts at boot),^^^ `disabled` ^^^(does not start at boot),^^^ `static` ^^^(cannot be enabled directly but might be started by another unit), or^^^ `masked` ^^^(prevented from starting).^^^
        - ^^^Execute the following command:^^^
        - `systemctl list-unit-files --``type``=service`^^^ ^^^
        - ^^^You will see output similar to this, indicating the^^^ `STATE` ^^^and^^^ `VENDOR PRESET` ^^^for each service unit file:^^^
        - ```
UNIT FILE                         STATE       VENDOR PRESET
arp-ethers.service                disabled    disabled
atd.service                       enabled     enabled
auditd.service                    enabled     enabled
auth-rpcgss-module.service        static      -
autovt@.service                   alias       -
blk-availability.service          disabled    disabled
...output omitted...
```^^^ ^^^
        - ^^^This command is particularly useful for understanding which services are configured to start automatically when the system boots up.^^^
        - 
        - # ^^^**Check Status of a Specific Service with systemctl status**^^^
        - ^^^In this step, you will learn how to check the detailed status of a specific service using the^^^ `systemctl status` ^^^command. This command provides comprehensive information about a service, including whether it's running, its process ID, memory usage, and recent log entries.^^^
        - ^^^We will use the^^^ `crond.service` ^^^(cron daemon) as an example. The cron daemon is a common service that handles scheduled tasks.^^^
        - ^^^Open your terminal in the RHEL environment. Ensure you are in your^^^ `~/project` ^^^directory.^^^
        - ^^^Execute the following command to check the status of the^^^ `crond.service`^^^:^^^
        - `systemctl status crond.service`^^^ ^^^
        - ^^^You will see detailed output similar to this:^^^
        - ```
● crond.service - Command Scheduler
     Loaded: loaded (/usr/lib/systemd/system/crond.service; enabled; preset: enabled)
     Active: active (running) since Mon 2022-03-14 05:38:10 EDT; 25min ago
   Main PID: 1089 (crond)
      Tasks: 1 (limit: 35578)
     Memory: 1.2M
        CPU: 12ms
     CGroup: /system.slice/crond.service
             └─1089 /usr/sbin/crond -n

Mar 14 05:38:10 workstation systemd[1]: Started Command Scheduler.
Warning: some journal files were not opened due to insufficient permissions.
```^^^ ^^^
        - ^^^Let's examine the key fields in the output:^^^
            - `**Loaded**`^^^: This line tells you if the service unit's configuration file has been processed. It also shows the path to the unit file (^^^`/usr/lib/systemd/system/crond.service`^^^) and its enablement status (^^^`enabled` ^^^means it's configured to start at boot).^^^
            - `**Active**`^^^: This is crucial. It indicates the current state of the service.^^^ `active (running)` ^^^means the service is currently active and its processes are running. It also shows how long it has been active. Other states could be^^^ `inactive` ^^^(not running),^^^ `active (exited)` ^^^(completed a one-time task), or^^^ `failed` ^^^(encountered an error).^^^
            - `**Main PID**`^^^: The Process ID (PID) of the main process associated with the service, along with the command name.^^^
            - `**Tasks**`^^^: The number of tasks (threads) the service is currently using.^^^
            - `**Memory**`^^^: The amount of memory the service is consuming.^^^
            - `**CPU**`^^^: The CPU time consumed by the service.^^^
            - `**CGroup**`^^^: Information about the control group the service belongs to, which is used for resource management.^^^
            - ^^^The lines below^^^ `CGroup` ^^^show recent log entries related to the service, providing insights into its startup and ongoing activities.^^^
        - ^^^In addition to^^^ `systemctl status`^^^, there are simpler commands to quickly check specific aspects of a service's state:^^^
            - ^^^To check if a service is active:^^^
                - `systemctl is-active crond.service`^^^ ^^^
                - ^^^Expected output:^^^
                - `active`^^^ ^^^
            - ^^^To check if a service is enabled (configured to start at boot):^^^
                - `systemctl is-enabled crond.service`^^^ ^^^
                - ^^^Expected output:^^^
                - `enabled`^^^ ^^^
            - ^^^To check if a service has failed:^^^
                - `systemctl is-failed crond.service`^^^ ^^^
                - ^^^Expected output (if running correctly):^^^
                - `active`^^^ ^^^
                - ^^^If a service had issues starting or running, this command would return^^^ `failed`^^^.^^^
        - ^^^These commands are useful for scripting or quick checks when you don't need the full detailed output of^^^ `systemctl status`^^^.^^^
        - 
        - # ^^^**Start, Stop, and Restart a Service with systemctl**^^^
        - ^^^In this step, you will learn how to manage the lifecycle of system services using^^^ `systemctl` ^^^commands. You will practice starting, stopping, and restarting a service. For this exercise, we will use a dummy service that we will create. This approach ensures that we can safely manipulate a service without affecting critical system functions.^^^
        - ^^^First, let's create a simple service unit file. This file will define a service that simply writes a timestamp to a log file every few seconds.^^^
        - ^^^Create a new service unit file named^^^ `mytest.service` ^^^directly in the systemd system directory using^^^ `nano`^^^:^^^
        - `sudo nano /etc/systemd/system/mytest.service`^^^ ^^^
        - ^^^Paste the following content into the^^^ `nano` ^^^editor:^^^
        - ```
[Unit]
``````
(#e06c75)

``````
Description
``````
(#d19a66)=My Test Service

``````
After
``````
(#d19a66)=network.target


``````
[Service]
``````
(#e06c75)

``````
Type
``````
(#d19a66)=simple

``````
ExecStart
``````
(#d19a66)=/bin/bash -c 
``````
'while true; do echo "$(date): My Test Service is running." >> /tmp/mytest.log; sleep 5; done'
``````
(#98c379)

``````
ExecStop
``````
(#d19a66)=/bin/bash -c 
``````
'echo "$(date): My Test Service stopped." >> /tmp/mytest.log'
``````
(#98c379)

``````
Restart
``````
(#d19a66)=
``````
on
``````
(#56b6c2)-failure


``````
[Install]
``````
(#e06c75)

``````
WantedBy
``````
(#d19a66)=multi-user.target
```^^^ ^^^
            - `**[Unit]**`^^^: Contains generic information about the unit.^^^ `Description` ^^^provides a human-readable name, and^^^ `After=network.target` ^^^specifies that this service should start after the network is up.^^^
            - `**[Service]**`^^^: Defines the behavior of the service.^^^
                - `Type=simple`^^^: Indicates a simple service type where the^^^ `ExecStart` ^^^command is the main process.^^^
                - `ExecStart`^^^: The command to execute when the service starts. Here, it's a bash loop that writes a timestamped message to^^^ `/tmp/mytest.log` ^^^every 5 seconds.^^^
                - `ExecStop`^^^: The command to execute when the service stops. It writes a stop message to the log.^^^
                - `Restart=on-failure`^^^: Configures the service to restart if it exits with a non-zero status.^^^
            - `**[Install]**`^^^: Contains information about how the service should be installed.^^^ `WantedBy=multi-user.target` ^^^means this service should be started when the system reaches the multi-user runlevel.^^^
        - ^^^Save the file by pressing^^^ `Ctrl+X`^^^, then^^^ `Y` ^^^to confirm, and^^^ `Enter` ^^^to save the file.^^^
        - ^^^Now, reload the systemd daemon to recognize the new service file:^^^
        - `sudo systemctl daemon-reload`^^^ ^^^
        - ## ^^^**Starting a Service**^^^
        - ^^^To start a service, use the^^^ `systemctl start` ^^^command.^^^
        - ^^^Execute the following command to start^^^ `mytest.service`^^^. Note that we need to use^^^ `sudo` ^^^because^^^ `systemctl` ^^^operations typically require root privileges.^^^
        - `sudo systemctl start mytest.service`^^^ ^^^
        - ^^^There will be no immediate output if the command is successful.^^^
        - ^^^Now, verify that the service is running by checking its status:^^^
        - `systemctl status mytest.service`^^^ ^^^
        - ^^^You should see output indicating that the service is^^^ `active (running)``(#3594f7)`^^^:^^^
        - ```
● mytest.service - My Test Service
     Loaded: loaded (/etc/systemd/system/mytest.service; disabled; preset: disabled)
     Active: active (running) since ...
   Main PID: ... (bash)
      Tasks: 2 (limit: ...)
     Memory: ...
        CPU: ...
     CGroup: /system.slice/mytest.service
             ├─... /bin/bash -c "while true; do echo \"\$(date): My Test Service is running.\" >> /tmp/mytest.log; sleep 5; done"
             └─... sleep 5

...output omitted...
```^^^ ^^^
        - ^^^You can also check the log file to see if the service is writing messages:^^^
        - `tail`` -f /tmp/mytest.log`^^^ ^^^
        - ^^^You should see new lines appearing every 5 seconds, similar to this:^^^
        - ```
Tue Jul 22 09:15:09 AM CST 2025: My Test Service is running.
Tue Jul 22 09:15:14 AM CST 2025: My Test Service is running.
```^^^ ^^^
        - ^^^Press^^^ `Ctrl+C` ^^^to exit^^^ `tail`^^^.^^^
        - ## ^^^**Stopping a Service**^^^
        - ^^^To stop a running service, use the^^^ `systemctl stop` ^^^command.^^^
        - ^^^Execute the following command to stop^^^ `mytest.service`^^^:^^^
        - `sudo systemctl stop mytest.service`^^^ ^^^
        - ^^^Again, there will be no immediate output.^^^
        - ^^^Verify that the service has stopped:^^^
        - `systemctl status mytest.service`^^^ ^^^
        - ^^^The output should now show^^^ `Active: inactive (dead)``(#3594f7)`^^^:^^^
        - ```
○ mytest.service - My Test Service
     Loaded: loaded (/etc/systemd/system/mytest.service; disabled; preset: disabled)
     Active: inactive (dead) since ...
...output omitted...
```^^^ ^^^
        - ^^^Check the log file^^^ `/tmp/mytest.log` ^^^again. You should see the "My Test Service stopped." message and no new "running" messages appearing.^^^
        - `tail`` /tmp/mytest.log`^^^ ^^^
        - ^^^The output will look similar to this:^^^
        - ```
Tue Jul 22 09:15:24 AM CST 2025: My Test Service is running.
Tue Jul 22 09:15:28 AM CST 2025: My Test Service stopped.
```^^^ ^^^
        - ## ^^^**Restarting a Service**^^^
        - ^^^To restart a service, use the^^^ `systemctl restart` ^^^command. This command first stops the service and then starts it again. This is useful when you've made changes to a service's configuration and need them to take effect.^^^
        - ^^^Execute the following command to restart^^^ `mytest.service`^^^:^^^
        - `sudo systemctl restart mytest.service`^^^ ^^^
        - ^^^Verify that the service is running again:^^^
        - `systemctl status mytest.service`^^^ ^^^
        - ^^^You should see^^^ `Active: active (running)``(#3594f7)` ^^^again, and the^^^ `Main PID``(#3594f7)` ^^^will likely be a new number, indicating a new process has started.^^^
        - ```
● mytest.service - My Test Service
     Loaded: loaded (/etc/systemd/system/mytest.service; disabled; preset: disabled)
     Active: active (running) since ...
   Main PID: ... (bash)
      Tasks: 2 (limit: ...)
     Memory: ...
        CPU: ...
     CGroup: /system.slice/mytest.service
             ├─... /bin/bash -c "while true; do echo \"\$(date): My Test Service is running.\" >> /tmp/mytest.log; sleep 5; done"
             └─... sleep 5
...output omitted...
```^^^ ^^^
        - ^^^Check the log file^^^ `/tmp/mytest.log` ^^^to confirm that the service has resumed writing "running" messages.^^^
        - `tail`` -f /tmp/mytest.log`^^^ ^^^
        - ^^^You should see a "stopped" message followed by new "running" messages:^^^
        - ```
Tue Jul 22 09:15:28 AM CST 2025: My Test Service stopped.
Tue Jul 22 09:15:40 AM CST 2025: My Test Service is running.
```^^^ ^^^
        - ^^^Press^^^ `Ctrl+C` ^^^to exit^^^ `tail`^^^.^^^
        - 
        - # ^^^**Applying Configuration Changes to a Service**^^^
        - ^^^In this step, you will learn about reloading service configurations. Some services can apply changes to their configuration files without needing a full restart. This is known as "reloading" the service. Reloading is generally preferred over restarting because it avoids service downtime and preserves existing connections or states. When a service is reloaded, its Process ID (PID) typically remains the same, unlike a full restart where the PID changes.^^^
        - ^^^We will continue to use our^^^ `mytest.service` ^^^from the previous step. We will modify its behavior and then attempt to reload it to see what happens.^^^
        - ^^^First, ensure^^^ `mytest.service` ^^^is running. If it's not, start it:^^^
        - `sudo systemctl start mytest.service`^^^ ^^^
        - ^^^Verify its status and take note of its^^^ `Main PID`^^^:^^^
        - `systemctl status mytest.service`^^^ ^^^
        - ^^^Now, let's modify the^^^ `mytest.service` ^^^file to change the message it logs and the interval. We will change the log message and the^^^ `sleep` ^^^duration.^^^
        - ^^^Open^^^ `/etc/systemd/system/mytest.service` ^^^with^^^ `nano`^^^:^^^
        - `sudo nano /etc/systemd/system/mytest.service`^^^ ^^^
        - ^^^Change the^^^ `ExecStart` ^^^line to the following, modifying the message and the^^^ `sleep` ^^^time from^^^ `5` ^^^to^^^ `2` ^^^seconds:^^^
        - ```
[Unit]
``````
(#e06c75)

``````
Description
``````
(#d19a66)=My Test Service

``````
After
``````
(#d19a66)=network.target


``````
[Service]
``````
(#e06c75)

``````
Type
``````
(#d19a66)=simple

``````
ExecStart
``````
(#d19a66)=/bin/bash -c 
``````
'while true; do echo "$(date): My Test Service (reloaded) is running." >> /tmp/mytest.log; sleep 2; done'
``````
(#98c379)

``````
ExecStop
``````
(#d19a66)=/bin/bash -c 
``````
'echo "$(date): My Test Service stopped." >> /tmp/mytest.log'
``````
(#98c379)

``````
Restart
``````
(#d19a66)=
``````
on
``````
(#56b6c2)-failure


``````
[Install]
``````
(#e06c75)

``````
WantedBy
``````
(#d19a66)=multi-user.target
```^^^ ^^^
        - ^^^Save the file by pressing^^^ `Ctrl+X`^^^, then^^^ `Y`^^^, and^^^ `Enter`^^^.^^^
        - ^^^After saving the changes, you need to inform^^^ `systemd` ^^^that the service's configuration has changed.^^^
        - `sudo systemctl daemon-reload`^^^ ^^^
        - ^^^Now, let's try to reload the service to apply the changes:^^^
        - `sudo systemctl reload mytest.service`^^^ ^^^
        - ^^^You will likely encounter an error:^^^
        - `Failed to reload mytest.service: Job type reload is not applicable for unit mytest.service.`^^^ ^^^
        - ^^^This error occurs because our simple service is not configured to handle a reload request. For a service to be reloadable, its unit file must include an^^^ `ExecReload` ^^^directive, which specifies the command to run to reload the configuration. Since our^^^ `mytest.service` ^^^lacks this,^^^ `systemd` ^^^doesn't know how to reload it.^^^
        - ^^^In situations like this,^^^ `systemd` ^^^provides a convenient command:^^^ `reload-or-restart`^^^. This command will attempt to reload the service, but if reloading is not supported, it will fall back to restarting the service. This is often a safer and more effective way to apply configuration changes.^^^
        - ^^^Let's use^^^ `reload-or-restart` ^^^now:^^^
        - `sudo systemctl reload-or-restart mytest.service`^^^ ^^^
        - ^^^This command should succeed. Now, check the status of the service again:^^^
        - `systemctl status mytest.service`^^^ ^^^
        - ^^^Observe the^^^ `Main PID`^^^. Since our service was restarted (because it couldn't be reloaded), you will notice that the^^^ `Main PID` ^^^is a^^^  ^^^ *new* ^^^^^^ ^^^ ^^^number. This confirms that the old process was stopped and a new one was started with the updated configuration.^^^
        - ^^^Finally, let's check the^^^ `/tmp/mytest.log` ^^^file to see if the changes have taken effect.^^^
        - `tail`` -f /tmp/mytest.log`^^^ ^^^
        - ^^^You should see the new log message "My Test Service (reloaded) is running." appearing every 2 seconds. Press^^^ `Ctrl+C``(#3594f7)` ^^^to exit^^^ `tail``(#3594f7)`^^^.^^^
        - 
        - # ^^^**Enable and Disable Services at Boot with systemctl**^^^
        - ^^^In this step, you will learn how to configure services to start automatically at boot time (enable) or prevent them from starting at boot (disable). This is crucial for managing system resources and ensuring that necessary services are available when the system starts.^^^
        - ^^^In a typical^^^ `systemd` ^^^environment, enabling a service creates symbolic links in the appropriate^^^ `systemd` ^^^configuration directories (e.g.,^^^ `/etc/systemd/system/multi-user.target.wants/`^^^) that point to the service's unit file. Disabling a service removes these links.^^^
        - ^^^Since we are in a containerized environment where^^^ `systemd` ^^^might not be fully operational in the traditional sense, the^^^ `enable` ^^^and^^^ `disable` ^^^commands might not create actual symlinks in the^^^ `/etc/systemd/system` ^^^directory that persist across container restarts. However,^^^ `systemctl` ^^^still processes these commands and updates its internal state, which is what we will observe.^^^
        - ^^^We will continue to use our^^^ `mytest.service` ^^^for this demonstration.^^^
        - ^^^First, ensure^^^ `mytest.service` ^^^is stopped from the previous step:^^^
        - `sudo systemctl stop mytest.service`^^^ ^^^
        - ## ^^^**Enabling a Service**^^^
        - ^^^To enable a service, use the^^^ `systemctl enable` ^^^command. This command configures the service to start automatically when the system boots.^^^
        - ^^^Execute the following command to enable^^^ `mytest.service`^^^:^^^
        - `sudo systemctl ``enable`` mytest.service`^^^ ^^^
        - ^^^You might see output similar to this, indicating that a symbolic link^^^  ^^^ *would be* ^^^^^^ ^^^ ^^^created in a full^^^ `systemd` ^^^environment:^^^
        - `Created symlink /etc/systemd/system/multi-user.target.wants/mytest.service → /etc/systemd/system/mytest.service.`^^^ ^^^
        - ^^^Now, verify that the service is enabled using^^^ `systemctl is-enabled`^^^:^^^
        - `systemctl is-enabled mytest.service`^^^ ^^^
        - ^^^Expected output:^^^
        - `enabled`^^^ ^^^
        - ^^^This confirms that^^^ `systemctl` ^^^now considers^^^ `mytest.service` ^^^to be enabled for boot.^^^
        - ^^^You can also combine enabling and starting a service in one command using the^^^ `--now` ^^^option. This is a convenient way to ensure a service is both running immediately and configured to start on future boots.^^^
        - ^^^First, let's disable it to prepare for the^^^ `--now` ^^^demonstration:^^^
        - `sudo systemctl ``disable`` mytest.service`^^^ ^^^
        - ^^^Now, enable and start it simultaneously:^^^
        - `sudo systemctl ``enable`` --now mytest.service`^^^ ^^^
        - ^^^Verify its status and enablement:^^^
        - ```
systemctl status mytest.service
systemctl is-enabled mytest.service
```^^^ ^^^
        - ^^^You should see^^^ `Active: active (running)``(#3594f7)` ^^^from the^^^ `status``(#3594f7)` ^^^command and^^^ `enabled``(#3594f7)` ^^^from the^^^ `is-enabled``(#3594f7)` ^^^command.^^^
        - ## ^^^**Disabling a Service**^^^
        - ^^^To disable a service, use the^^^ `systemctl disable` ^^^command. This command removes the configuration that causes the service to start at boot time.^^^
        - ^^^Execute the following command to disable^^^ `mytest.service`^^^:^^^
        - `sudo systemctl ``disable`` mytest.service`^^^ ^^^
        - ^^^You might see output indicating the removal of the symbolic link:^^^
        - `Removed /etc/systemd/system/multi-user.target.wants/mytest.service.`^^^ ^^^
        - ^^^Now, verify that the service is disabled:^^^
        - `systemctl is-enabled mytest.service`^^^ ^^^
        - ^^^Expected output:^^^
        - `disabled`^^^ ^^^
        - ^^^Similar to enabling, you can combine disabling and stopping a service using the^^^ `--now` ^^^option. This will stop the service immediately and prevent it from starting on future boots.^^^
        - `sudo systemctl ``disable`` --now mytest.service`^^^ ^^^
        - ^^^Verify its status and enablement:^^^
        - ```
systemctl status mytest.service
systemctl is-enabled mytest.service
```^^^ ^^^
        - ^^^You should see^^^ `Active: inactive (dead)``(#3594f7)` ^^^from the^^^ `status``(#3594f7)` ^^^command and^^^ `disabled``(#3594f7)` ^^^from the^^^ `is-enabled``(#3594f7)` ^^^command.^^^
        - ^^^This concludes the demonstration of enabling and disabling services. Remember that in a real^^^ `systemd` ^^^environment, these commands directly manipulate the boot configuration.^^^
        - 
        - # ^^^**Mask and Unmask Services with systemctl**^^^
        - ^^^In this final step, you will learn about masking and unmasking services. Masking a service is a powerful way to prevent it from being started, either manually or automatically at boot.^^^
        - ^^^When you mask a service,^^^ `systemd` ^^^creates a symbolic link from^^^ `/etc/systemd/system/<service-name>.service` ^^^to^^^ `/dev/null`^^^, effectively making the service unit file unavailable to^^^ `systemd`^^^. This is a stronger alternative to^^^ `disable`^^^.^^^
        - ^^^This mechanism works best for services that are defined in^^^ `/usr/lib/systemd/system`^^^, which is where packages install their service files. The^^^ `mask` ^^^command creates an overriding "empty" file in^^^ `/etc/systemd/system`^^^. However, as you have discovered, if you try to mask a service that you created directly in^^^ `/etc/systemd/system` ^^^(like our^^^ `mytest.service`^^^), the command can fail because it is designed to not overwrite an existing configuration file, which would cause data loss.^^^
        - ^^^To demonstrate masking correctly, we will use a pre-existing service,^^^ `atd.service`^^^.^^^
        - ^^^First, let's check the current status of^^^ `atd.service`^^^. It should be active and enabled.^^^
        - `systemctl status atd.service`^^^ ^^^
        - ^^^The output will be similar to this, showing the service is active and running:^^^
        - ```
● atd.service - Deferred execution scheduler
     Loaded: loaded (/usr/lib/systemd/system/atd.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-07-22 09:13:06 CST; 22min ago
       Docs: man:atd(8)
   Main PID: 1222 (atd)
      Tasks: 1 (limit: 22509)
     Memory: 900.0K
        CPU: 5ms
     CGroup: /system.slice/atd.service
             └─1222 /usr/sbin/atd -f
```^^^ ^^^
        - ## ^^^**Masking a Service**^^^
        - ^^^It's good practice to stop a service before masking it.^^^
        - `sudo systemctl stop atd.service`^^^ ^^^
        - ^^^Now, execute the following command to mask^^^ `atd.service`^^^:^^^
        - `sudo systemctl mask atd.service`^^^ ^^^
        - ^^^You will see output indicating the creation of a symbolic link to^^^ `/dev/null`^^^:^^^
        - `Created symlink /etc/systemd/system/atd.service → /dev/null.`^^^ ^^^
        - ^^^Now, try to start the masked service:^^^
        - `sudo systemctl start atd.service`^^^ ^^^
        - ^^^You will receive an error message, indicating that the service is masked:^^^
        - `Failed to start atd.service: Unit atd.service is masked.`^^^ ^^^
        - ^^^You can also check the state of the service using^^^ `systemctl list-unit-files`^^^:^^^
        - `systemctl list-unit-files --``type``=service | grep atd.service`^^^ ^^^
        - ^^^The output should show^^^ `masked` ^^^for^^^ `atd.service`^^^:^^^
        - `atd.service                            masked      enabled`^^^ ^^^
        - ^^^This confirms that the service is now masked and cannot be started.^^^
        - ## ^^^**Unmasking a Service**^^^
        - ^^^To unmask a service, use the^^^ `systemctl unmask` ^^^command. This command removes the symbolic link to^^^ `/dev/null`^^^, restoring the original service file from^^^ `/usr/lib/systemd/system`^^^.^^^
        - ^^^Execute the following command to unmask^^^ `atd.service`^^^:^^^
        - `sudo systemctl unmask atd.service`^^^ ^^^
        - ^^^You will see output indicating the removal of the symbolic link:^^^
        - `Removed "/etc/systemd/system/atd.service".`^^^ ^^^
        - ^^^Now, check the state of the service using^^^ `systemctl list-unit-files` ^^^again:^^^
        - `systemctl status atd.service`^^^ ^^^
        - ^^^You should see^^^ `Active: active (running)``(#3594f7)`^^^, similar to this:^^^
        - ```
● atd.service - Deferred execution scheduler
     Loaded: loaded (/usr/lib/systemd/system/atd.service; enabled; preset: enabled)
     Active: active (running) since Tue 2025-07-22 09:36:10 CST; 2s ago
       Docs: man:atd(8)
   Main PID: 7372 (atd)
      Tasks: 1 (limit: 22509)
     Memory: 868.0K
        CPU: 6ms
     CGroup: /system.slice/atd.service
             └─7372 /usr/sbin/atd -f
```^^^ ^^^
        - ^^^This concludes the lab on controlling services and daemons. You have learned how to view, start, stop, restart, reload, enable, disable, mask, and unmask services using^^^ `systemctl`^^^.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, we gained hands-on experience managing control system services using the^^^ `systemctl` ^^^command, even within a containerized environment where^^^ `systemd` ^^^might not be the primary init system. We learned how to list all loaded and active service units using^^^ `systemctl list-units --type=service`^^^, understanding the^^^ `UNIT`^^^,^^^ `LOAD`^^^,^^^ `ACTIVE`^^^, and^^^ `SUB` ^^^columns to interpret service states.^^^
        - ^^^Furthermore, we explored essential service management operations: checking the status of a specific service with^^^ `systemctl status`^^^, and controlling service lifecycle by starting, stopping, and restarting services. We also covered how to reload service configurations, enable and disable services to control their behavior at boot time, and the advanced concepts of masking and unmasking services to prevent them from being started. This comprehensive set of skills provides a solid foundation for managing services on RHEL systems.^^^
    9. Secure SSH in Red Hat Enterprise Linux
        - Access Remote Systems with SSH
        - Generate and Use SSH Key Pairs for Passwordless Authentication
        - Manage SSH Keys with ssh-agent
        - Troubleshoot SSH Connection Issues
        - Customize SSH Client Configurations
        - Understanding OpenSSH Server Security Configuration
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience with configuring and securing SSH connections, a fundamental skill for managing remote Linux systems. You will begin by learning how to access remote systems using SSH, understanding the client-server architecture and basic connection commands. This includes verifying SSH client installation, connecting to a remote host, handling host authenticity prompts, and logging in and out of remote systems.^^^
        - ^^^Building on this foundation, you will then delve into more advanced topics such as generating and utilizing SSH key pairs for passwordless authentication, managing these keys effectively with^^^ `ssh-agent`^^^, and troubleshooting common SSH connection issues. Finally, you will learn to customize SSH client configurations for improved efficiency and enhance the security of your OpenSSH server by disabling root login and password authentication, ensuring robust and secure remote access.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level lab with a^^^ ^^^88%^^^ ^^^completion rate. It has received a^^^ ^^^100%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Access Remote Systems with SSH**^^^
        - ^^^In this step, you will learn how to access remote systems using SSH (Secure Shell). SSH is a cryptographic network protocol for operating network services securely over an unsecured network. It provides a secure channel over an unsecured network by using a client-server architecture, connecting an SSH client with an SSH server.^^^
        - ^^^**Note:**^^^ ^^^In this lab environment, some security features like root login restrictions may already be configured for security purposes. This is normal and demonstrates best practices in action.^^^
        - ^^^First, you will connect to the local system using SSH. This demonstrates the SSH client-server architecture even when connecting to the same machine. You will use the^^^ `ssh` ^^^command to connect to^^^ `localhost`^^^.^^^
        - ^^^The basic syntax for^^^ `ssh` ^^^is:^^^
        - 
        - `ssh [username]@[hostname_or_IP]`
        - ^^^If you don't specify a username, SSH will attempt to log in with your current local username. In this case, your local username is^^^ `labex`^^^.^^^
        - ^^^Let's try to connect to^^^ `localhost` ^^^using your current username:^^^
        - `ssh localhost`^^^ ^^^
        - ^^^When you connect for the first time, SSH will ask you to confirm the authenticity of the host. This is a security measure to prevent man-in-the-middle attacks. Type^^^ `yes` ^^^and press^^^ `Enter`^^^.^^^
        - ```
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is SHA256:h5k1mmPFylpxUCsKx+Mf8rN4wOrk9TmyRfzTvGWRm7A.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'localhost' (ED25519) to the list of known hosts.
labex@localhost's password:
```^^^ ^^^
        - ^^^You will be prompted for the password of the^^^ `labex` ^^^user. Enter^^^ `labex` ^^^and press^^^ `Enter`^^^.^^^
        - ```
labex@localhost's password:
Last login: Mon Jun  9 01:34:39 2025 from 47.251.66.143
[labex@host ~]$
```^^^ ^^^
        - ^^^You are now logged in via SSH to localhost. Notice that your prompt may show^^^ `[labex@localhost ~]$`^^^, indicating you are connected via SSH.^^^
        - ^^^To log out of the SSH session, use the^^^ `exit` ^^^command:^^^
        - `exit`^^^ ^^^
        - ```
logout
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - ^^^Now, let's try connecting to^^^ `localhost` ^^^as the^^^ `root` ^^^user. Note that in this environment, root login may be disabled by default for security reasons.^^^
        - `ssh root@localhost`^^^ ^^^
        - ^^^You will be prompted for the root password. However, you may encounter a "Permission denied" message if root login is disabled:^^^
        - ```
root@localhost's password:
Permission denied, please try again.
root@localhost's password:
Permission denied, please try again.
root@localhost's password:
```^^^ ^^^
        - ^^^If root login is disabled, this is expected behavior and demonstrates a security best practice. You can press^^^ `Ctrl+C` ^^^to cancel the connection attempt.^^^
        - ^^^SSH can also be used to execute a single command on a remote system without opening an interactive shell. This is useful for quick checks or automation.^^^
        - ^^^Let's run the^^^ `hostname` ^^^command on^^^ `localhost` ^^^as the^^^ `labex` ^^^user:^^^
        - `ssh labex@localhost hostname`^^^ ^^^
        - ^^^You will be prompted for the^^^ `labex` ^^^user's password. Enter^^^ `labex` ^^^and press^^^ `Enter`^^^.^^^
        - ```
labex@localhost's password:
6846375f1c0e35fea6cb03e6
[labex@host ~]$
```^^^ ^^^
        - ^^^The^^^ `hostname` ^^^command was executed via SSH, and its output was displayed on your local terminal. You were not dropped into an interactive shell.^^^
        - ^^^Finally, let's explore how SSH manages known hosts. When you connect to a new SSH server, its public key fingerprint is added to your^^^ `~/.ssh/known_hosts` ^^^file. This file helps your SSH client verify the identity of the server in future connections.^^^
        - ^^^You can view the contents of your^^^ `~/.ssh/known_hosts` ^^^file:^^^
        - `cat`` ~/.ssh/known_hosts`^^^ ^^^
        - ```
localhost ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHvl7dcZkvMNOr3cjKjlR2/JgFbGpURThT/bHnLZN6gG
localhost ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCynhy3601o9ZSGZoY0KB/QSonk5ykod2Tb7sCAqVn4ZgTCwd96BhPjJLPNQ6ldNASo1e7EzfT4BUjG5T0ZDRhgaI65qmDwITWipTWUfmYT5XoScyf6NDhcRxYiJwztFEkOvLcPhelS6UXj5Z7HdmYH4Nc5wiF00Wah3Jc0/2CfQsFZCXTn/7Kp8KKbBbPqPzr2R3WIULEacOxx9HKVv+2TvYg/OHZz40hTsr1c68DD7h5PMBNe21YB3HLRRk2LQEC7v7BFD+DCek9GNR66JBjbLDljtwWCaPCY0UntBjjvJ3W2LhX5RDZQHV/iaUSj2tEXnvPt9KSqGfBS91D12dBXyOmWVnTpvvI17BdDkEeefas2Uz4d7Bv/PDxZR6IKkaIGQ/ZnRhSEhBNvfqlBGqkOhRr6jQJK+rQMnsZCT6OEgW7osWzkw5Bs1wY/RNToeQqrRMclqffO9plFI688N2iT86+nxrvBVZg4yMMm2J1lleaBvinXCB8jE6lrtwoAdgk=
localhost ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKYWY8Ty6TrbQS/0fUljBWuUpkyPCS/5P6ZwxhSYsqjRBIprMANI/JQotZqHYq2w3b2X/n8O+J3/WuIB6XMl1f4=
```^^^ ^^^
        - ^^^These entries confirm that your client has recorded multiple public keys for^^^ `localhost` ^^^(ED25519, RSA, and ECDSA). The SSH server may support multiple key types for compatibility. If any of these server keys ever change unexpectedly, SSH will warn you, which is a crucial security feature.^^^
        - 
        - # ^^^**Generate and Use SSH Key Pairs for Passwordless Authentication**^^^
        - ^^^In this step, you will learn how to generate SSH key pairs and use them for passwordless authentication. SSH key-based authentication is a more secure and convenient alternative to password authentication. Instead of typing a password every time you connect, you use a pair of cryptographic keys: a private key (kept secret on your local machine) and a public key (placed on the remote server).^^^
        - ^^^First, you need to generate an SSH key pair. You will use the^^^ `ssh-keygen` ^^^command for this purpose. By default,^^^ `ssh-keygen` ^^^creates an RSA key pair and saves the private key in^^^ `~/.ssh/id_rsa` ^^^and the public key in^^^ `~/.ssh/id_rsa.pub`^^^.^^^
        - ^^^Execute the^^^ `ssh-keygen` ^^^command:^^^
        - `ssh-keygen`^^^ ^^^
        - ^^^You will be prompted for a few options:^^^
        - ```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/labex/.ssh/id_rsa):
```^^^ ^^^
        - ^^^Press^^^ `Enter` ^^^to accept the default file path (^^^`/home/labex/.ssh/id_rsa`^^^).^^^
        - `Enter passphrase (empty for no passphrase):``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^For this lab, press^^^ `Enter` ^^^twice to leave the passphrase empty. While using a passphrase is recommended for real-world scenarios to add an extra layer of security, we will skip it here for simplicity and to demonstrate passwordless authentication directly.^^^
        - ```
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/labex/.ssh/id_rsa
Your public key has been saved in /home/labex/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:QoV7pNBFu1kafGP3VJhpZuIdr1zc+qamJ1C2YAadgNY labex@6846375f1c0e35fea6cb03e6
The key's randomart image is:
+---[RSA 3072]----+
|     . *=o .   +.|
|    . =oE.o . O. |
|     o.++.=..*.+.|
|     .o .O+o+o. =|
|      ..So + o.+ |
|       .  . . +  |
|           .   . |
|            . o o|
|            .=.o |
+----[SHA256]-----+
```^^^ ^^^
        - ^^^Now, verify that the key files have been created in the^^^ `~/.ssh/` ^^^directory:^^^
        - `ls`` -l ~/.ssh/`^^^ ^^^
        - ```
total 16
-rw------- 1 labex labex 2622 Jun  9 01:37 id_rsa
-rw-r--r-- 1 labex labex  584 Jun  9 01:37 id_rsa.pub
-rw------- 1 labex labex  825 Jun  9 01:35 known_hosts
-rw-r--r-- 1 labex labex   91 Jun  9 01:35 known_hosts.old
```^^^ ^^^
        - ^^^You should see^^^ `id_rsa` ^^^(your private key) and^^^ `id_rsa.pub` ^^^(your public key). Note the permissions:^^^ `id_rsa` ^^^has^^^ `rw-------` ^^^(read/write only for the owner), which is crucial for security. You may also see^^^ `known_hosts.old` ^^^which is a backup of the previous known_hosts file.^^^
        - ^^^Next, you need to copy your public key to enable passwordless authentication. The^^^ `ssh-copy-id` ^^^command is designed for this purpose. It appends your public key to the^^^ `~/.ssh/authorized_keys` ^^^file, allowing you to log in without a password.^^^
        - ^^^Execute the^^^ `ssh-copy-id` ^^^command, specifying the user and hostname:^^^
        - `ssh-copy-id labex@localhost`^^^ ^^^
        - ^^^You will be prompted for the^^^ `labex` ^^^user's password. Enter^^^ `labex` ^^^and press^^^ `Enter`^^^.^^^
        - ```
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/labex/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
labex@localhost's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'labex@localhost'"
and check to make sure that only the key(s) you wanted were added.
```^^^ ^^^
        - ^^^The command output confirms that one key was added. Now, try to log in to^^^ `localhost` ^^^as^^^ `labex` ^^^without providing a password:^^^
        - `ssh labex@localhost`^^^ ^^^
        - ^^^If everything is configured correctly, you should be logged in via SSH without being prompted for a password.^^^
        - ```
Last login: Mon Jun  9 01:37:39 2025 from 47.251.66.143
[labex@host ~]$
```^^^ ^^^
        - ^^^You have successfully configured passwordless SSH authentication using key pairs!^^^
        - ^^^To exit the remote session, type^^^ `exit`^^^:^^^
        - `exit`^^^ ^^^
        - ```
exit
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - 
        - # ^^^**Manage SSH Keys with ssh-agent**^^^
        - ^^^In this step, you will learn how to manage your SSH keys using^^^ `ssh-agent`^^^. The^^^ `ssh-agent` ^^^is a program that runs in the background and holds your private keys in memory. This is particularly useful when your private keys are protected by a passphrase. Instead of typing the passphrase every time you use the key, you type it once when you add the key to the^^^ `ssh-agent`^^^, and then the agent handles the authentication for you for the duration of your session.^^^
        - ^^^Although you generated a key without a passphrase in the previous step, we will now create a new key with a passphrase to demonstrate the utility of^^^ `ssh-agent`^^^.^^^
        - ^^^First, generate a new SSH key pair with a passphrase. We will name this key^^^ `id_rsa_passphrase` ^^^to distinguish it from the default^^^ `id_rsa` ^^^key.^^^
        - `ssh-keygen -f ~/.ssh/id_rsa_passphrase`^^^ ^^^
        - ^^^You will be prompted to enter a passphrase. For this lab, use^^^ `mypassphrase` ^^^as the passphrase.^^^
        - ```
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): mypassphrase
Enter same passphrase again: mypassphrase
Your identification has been saved in /home/labex/.ssh/id_rsa_passphrase
Your public key has been saved in /home/labex/.ssh/id_rsa_passphrase.pub
The key fingerprint is:
SHA256:BuSxVlJb1lsiUFi2I5DAvyL01fJ5d480LT86dgtcHEg labex@6846375f1c0e35fea6cb03e6
The key's randomart image is:
+---[RSA 3072]----+
|   ...=o+=*. E   |
|    .o.*.=..+ o  |
|     .=.o o. = . |
|  .  .+... .. . .|
| . . . +S.     + |
|  . o ..o . o * .|
|   . .   . . = * |
|             oooo|
|            ..+.o|
+----[SHA256]-----+
```^^^ ^^^
        - ^^^**Note:**^^^ ^^^If you accidentally press Enter without typing a passphrase, the key will be created without one. In that case, you can delete the files and run the command again, making sure to enter^^^ `mypassphrase` ^^^when prompted.^^^
        - ^^^Now, let's copy this new public key to^^^ `localhost` ^^^so you can use it for authentication.^^^
        - `ssh-copy-id -i ~/.ssh/id_rsa_passphrase.pub labex@localhost`^^^ ^^^
        - ^^^Since you already have passwordless authentication set up with your default key, the command may not prompt for a password and will use your existing authentication:^^^
        - ```
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/labex/.ssh/id_rsa_passphrase.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'labex@localhost'"
and check to make sure that only the key(s) you wanted were added.
```^^^ ^^^
        - ^^^Now, try to connect to^^^ `localhost` ^^^using this new key. You will need to specify the private key file using the^^^ `-i` ^^^option.^^^
        - `ssh -i ~/.ssh/id_rsa_passphrase labex@localhost`^^^ ^^^
        - ^^^If you set a passphrase for the key, you will be prompted for it. However, if you accidentally created the key without a passphrase (as shown in the example output), you will be logged in directly:^^^
        - ```
Last login: Mon Jun  9 01:39:25 2025 from 47.251.66.143
[labex@host ~]$
```^^^ ^^^
        - ^^^You are logged in. Now, exit the session:^^^
        - `exit`^^^ ^^^
        - ```
exit
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - ^^^**Note:**^^^ ^^^If your key doesn't have a passphrase, you can still continue with the^^^ `ssh-agent` ^^^demonstration to understand how it works, even though it won't prompt for a passphrase in this case.^^^
        - ^^^First, start the^^^ `ssh-agent` ^^^in your current shell session. The^^^ `eval` ^^^command is used to properly set the environment variables that^^^ `ssh-agent` ^^^outputs.^^^
        - `eval`` ``"``(#98c379)``$(ssh-agent)``(#e06c75)``"``(#98c379)`^^^ ^^^
        - `Agent pid 1024`^^^ ^^^
        - ^^^The output will show the process ID (PID) of the^^^ `ssh-agent``(#3594f7)`^^^.^^^
        - ^^^Next, add your private key (^^^`id_rsa_passphrase``(#3594f7)`^^^) to the^^^ `ssh-agent``(#3594f7)`^^^.^^^
        - `ssh-add ~/.ssh/id_rsa_passphrase`^^^ ^^^
        - ^^^If your key has a passphrase, you will be prompted for it. If not, the key will be added directly:^^^
        - `Identity added: /home/labex/.ssh/id_rsa_passphrase (labex@6846375f1c0e35fea6cb03e6)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^Now that the key is added to the^^^ `ssh-agent`^^^, try connecting to^^^ `localhost` ^^^again using the same key.^^^
        - `ssh -i ~/.ssh/id_rsa_passphrase labex@localhost`^^^ ^^^
        - ^^^You should be able to connect without being prompted for a passphrase (whether your key has one or not, since it's now managed by the agent):^^^
        - ```
Last login: Mon Jun  9 01:39:49 2025 from 127.0.0.1
[labex@host ~]$
```^^^ ^^^
        - ^^^You have successfully used^^^ `ssh-agent` ^^^to manage your SSH key.^^^
        - ^^^**Important Note:**^^^ ^^^The^^^ `ssh-agent` ^^^environment variables are only available in the shell session where you started it. If you're in an SSH session, you need to exit back to your local shell to use^^^ `ssh-add` ^^^commands.^^^
        - ^^^Exit the SSH session first:^^^
        - `exit`^^^ ^^^
        - ```
exit
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - ^^^Now, to see the keys currently loaded in your^^^ `ssh-agent`^^^, you can use^^^ `ssh-add -l`^^^:^^^
        - `ssh-add -l`^^^ ^^^
        - ^^^If the agent is running and has keys loaded, you'll see output like:^^^
        - `3072 SHA256:BuSxVlJb1lsiUFi2I5DAvyL01fJ5d480LT86dgtcHEg /home/labex/.ssh/id_rsa_passphrase (RSA)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^However, if you see an error message like "Could not open a connection to your authentication agent", it means the agent environment variables are not set in your current session.^^^
        - ^^^To remove all identities from the^^^ `ssh-agent`^^^, use^^^ `ssh-add -D`^^^:^^^
        - `ssh-add -D`^^^ ^^^
        - ^^^If the agent is accessible, you'll see:^^^
        - `All identities removed.`^^^ ^^^
        - ^^^However, if you see "Could not open a connection to your authentication agent", it means the agent environment is not available in your current session.^^^
        - ^^^Now, if you try to connect again and your key has a passphrase, you will be prompted for it because the key has been removed from the agent:^^^
        - `ssh -i ~/.ssh/id_rsa_passphrase labex@localhost`^^^ ^^^
        - ^^^If your key has a passphrase, you'll see:^^^
        - `Enter passphrase for key '/home/labex/.ssh/id_rsa_passphrase':`^^^ ^^^
        - ^^^If your key doesn't have a passphrase, you'll still be able to connect directly. Press^^^ `Ctrl+C` ^^^to cancel the connection attempt if prompted for a passphrase.^^^
        - ^^^Finally, to stop the^^^ `ssh-agent` ^^^process, you can use^^^ `ssh-agent -k`^^^:^^^
        - `ssh-agent -k`^^^ ^^^
        - ^^^If the SSH_AGENT_PID environment variable is not set, you may see:^^^
        - `SSH_AGENT_PID not set, cannot kill agent`^^^ ^^^
        - ^^^This is normal if the agent was started in a different shell session or if the environment variables were not properly exported.^^^
        - 
        - # ^^^**Troubleshoot SSH Connection Issues**^^^
        - ^^^In this step, you will learn how to troubleshoot common SSH connection issues. When SSH connections fail, it can be challenging to pinpoint the exact problem. The^^^ `ssh` ^^^command provides verbose output options that can help diagnose issues by showing detailed information about the connection process.^^^
        - ^^^The^^^ `ssh` ^^^command offers three verbosity levels:^^^ `-v`^^^,^^^ `-vv`^^^, and^^^ `-vvv`^^^. Each additional^^^ `v` ^^^increases the amount of debugging information displayed.^^^
        - ^^^Let's start by attempting to connect to a non-existent port on localhost to demonstrate connection failure and see the debugging output.^^^
        - ^^^First, try with^^^ `-v` ^^^(verbose) to connect to port 2222 (which should not be running):^^^
        - `ssh -v -p 2222 labex@localhost`^^^ ^^^
        - ^^^You will see output similar to this, indicating that the connection is refused:^^^
        - ```
OpenSSH_8.7p1, OpenSSL 3.0.1 14 Dec 2021
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Reading configuration data /etc/ssh/ssh_config.d/01-training.conf
debug1: /etc/ssh/ssh_config.d/01-training.conf line 1: Applying options for *
debug1: Reading configuration data /etc/ssh/ssh_config.d/50-redhat.conf
debug1: /etc/ssh/ssh_config.d/50-redhat.conf line 3: Applying options for *
debug1: Connecting to localhost [127.0.0.1] port 2222.
ssh: connect to host localhost port 2222: Connection refused
```^^^ ^^^
        - ^^^Now, let's try with^^^ `-vv` ^^^(more verbose):^^^
        - `ssh -vv -p 2222 labex@localhost`^^^ ^^^
        - ^^^The output will be more detailed, providing additional debugging messages:^^^
        - ```
OpenSSH_8.7p1, OpenSSL 3.0.1 14 Dec 2021
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Reading configuration data /etc/ssh/ssh_config.d/01-training.conf
debug1: /etc/ssh/ssh_config.d/01-training.conf line 1: Applying options for *
debug1: Reading configuration data /etc/ssh/ssh_config.d/50-redhat.conf
debug1: /etc/ssh/ssh_config.d/50-redhat.conf line 3: Applying options for *
debug2: resolving "localhost" port 2222
debug2: ssh_connect_direct: entering
debug1: Connecting to localhost [127.0.0.1] port 2222.
debug1: connect to address 127.0.0.1 port 2222: Connection refused
ssh: connect to host localhost port 2222: Connection refused
```^^^ ^^^
        - ^^^Finally, try with^^^ `-vvv` ^^^(most verbose):^^^
        - `ssh -vvv -p 2222 labex@localhost`^^^ ^^^
        - ^^^This level provides the maximum amount of debugging information, which can be overwhelming but extremely useful for complex issues.^^^
        - ```
OpenSSH_8.7p1, OpenSSL 3.0.1 14 Dec 2021
debug3: ssh_connect_internal: entering
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Reading configuration data /etc/ssh/ssh_config.d/01-training.conf
debug1: /etc/ssh/ssh_config.d/01-training.conf line 1: Applying options for *
debug1: Reading configuration data /etc/ssh/ssh_config.d/50-redhat.conf
debug1: /etc/ssh/ssh_config.d/50-redhat.conf line 3: Applying options for *
debug2: resolving "localhost" port 2222
debug2: ssh_connect_direct: entering
debug1: Connecting to localhost [127.0.0.1] port 2222.
debug1: connect to address 127.0.0.1 port 2222: Connection refused
ssh: connect to host localhost port 2222: Connection refused
```^^^ ^^^
        - ^^^In this case, the error^^^ `Connection refused` ^^^clearly indicates that there is no SSH server running on port 2222.^^^
        - ^^^Now, let's simulate a common issue: a changed host key. In the first step, you connected to^^^ `localhost`^^^, and its public key was added to your^^^ `~/.ssh/known_hosts` ^^^file. If the SSH server key were to change (e.g., due to a server rebuild or a malicious attack), your SSH client would detect this mismatch and refuse to connect.^^^
        - ^^^To simulate this, we will intentionally modify the^^^ `known_hosts` ^^^entry for^^^ `localhost` ^^^to make it invalid.^^^
        - ^^^First, open the^^^ `~/.ssh/known_hosts` ^^^file using^^^ `nano`^^^:^^^
        - `nano ~/.ssh/known_hosts`^^^ ^^^
        - ^^^You will see multiple lines with different key types:^^^
        - ```
localhost ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHvl7dcZkvMNOr3cjKjlR2/JgFbGpURThT/bHnLZN6gG
localhost ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCynhy3601o9ZSGZoY0KB/QSonk5ykod2Tb7sCAqVn4ZgTCwd96BhPjJLPNQ6ldNASo1e7EzfT4BUjG5T0ZDRhgaI65qmDwITWipTWUfmYT5XoScyf6NDhcRxYiJwztFEkOvLcPhelS6UXj5Z7HdmYH4Nc5wiF00Wah3Jc0/2CfQsFZCXTn/7Kp8KKbBbPqPzr2R3WIULEacOxx9HKVv+2TvYg/OHZz40hTsr1c68DD7h5PMBNe21YB3HLRRk2LQEC7v7BFD+DCek9GNR66JBjbLDljtwWCaPCY0UntBjjvJ3W2LhX5RDZQHV/iaUSj2tEXnvPt9KSqGfBS91D12dBXyOmWVnTpvvI17BdDkEeefas2Uz4d7Bv/PDxZR6IKkaIGQ/ZnRhSEhBNvfqlBGqkOhRr6jQJK+rQMnsZCT6OEgW7osWzkw5Bs1wY/RNToeQqrRMclqffO9plFI688N2iT86+nxrvBVZg4yMMm2J1lleaBvinXCB8jE6lrtwoAdgk=
localhost ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKYWY8Ty6TrbQS/0fUljBWuUpkyPCS/5P6ZwxhSYsqjRBIprMANI/JQotZqHYq2w3b2X/n8O+J3/WuIB6XMl1f4=
```^^^ ^^^
        - ^^^Choose one of the lines to modify. For this example, let's modify the ED25519 key (the first line). Modify a few characters in the long key string (e.g., change the last character from^^^ `G``(#3594f7)` ^^^to^^^ `A``(#3594f7)`^^^). Be careful not to delete the entire line or other parts of the file.^^^
        - ^^^For example, change:^^^
        - 
        - `...ZN6gG`
        - 
        - ^^^to:^^^
        - 
        - `...ZN6gA`
        - ^^^Save the file by pressing^^^ `Ctrl+X`^^^, then^^^ `Y` ^^^to confirm saving, and^^^ `Enter` ^^^to confirm the filename.^^^
        - ^^^Now, try to connect to^^^ `localhost` ^^^again:^^^
        - `ssh labex@localhost`^^^ ^^^
        - ^^^You will receive a warning about a changed host key:^^^
        - ```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ED25519 key sent by the remote host is
SHA256:h5k1mmPFylpxUCsKx+Mf8rN4wOrk9TmyRfzTvGWRm7A.
Please contact your system administrator.
Add correct host key in /home/labex/.ssh/known_hosts to get rid of this message.
Offending key in /home/labex/.ssh/known_hosts:1
ED25519 host key for localhost has changed and you have requested strict checking.
Host key verification failed.
```^^^ ^^^
        - ^^^This is a critical security warning. If you encounter this in a real-world scenario, you should investigate why the host key changed. If it's a legitimate change (e.g., server reinstallation), you need to remove the old entry from^^^ `known_hosts``(#3594f7)`^^^.^^^
        - ^^^To fix this, you can either manually edit^^^ `~/.ssh/known_hosts` ^^^and remove the offending line, or use^^^ `ssh-keygen -R` ^^^to remove the entry for^^^ `localhost`^^^.^^^
        - ^^^Let's use^^^ `ssh-keygen -R` ^^^to remove the incorrect entry:^^^
        - `ssh-keygen -R localhost`^^^ ^^^
        - ```
# Host localhost found: line 1
# Host localhost found: line 2
# Host localhost found: line 3
/home/labex/.ssh/known_hosts updated.
Original contents retained as /home/labex/.ssh/known_hosts.old
```^^^ ^^^
        - ^^^Now, try connecting to^^^ `localhost` ^^^again. You will be prompted to confirm the host's authenticity, just like the very first time you connected.^^^
        - `ssh labex@localhost`^^^ ^^^
        - ```
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is SHA256:h5k1mmPFylpxUCsKx+Mf8rN4wOrk9TmyRfzTvGWRm7A.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'localhost' (ED25519) to the list of known hosts.
Last login: Mon Jun  9 01:40:03 2025 from 127.0.0.1
[labex@host ~]$
```^^^ ^^^
        - ^^^You are now successfully connected again using key-based authentication.^^^
        - ^^^Exit the session:^^^
        - `exit`^^^ ^^^
        - ```
exit
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - 
        - # ^^^**Customize SSH Client Configurations**^^^
        - ^^^In this step, you will learn how to customize your SSH client configurations using the^^^ `~/.ssh/config` ^^^file. This file allows you to define aliases and specific connection parameters for different remote hosts, simplifying your SSH commands and making them more consistent.^^^
        - ^^^The^^^ `~/.ssh/config` ^^^file is a powerful tool for managing your SSH connections. You can specify various options such as the username, the private key file to use, the port number, and even more advanced settings like proxy commands.^^^
        - ^^^First, let's create or open the^^^ `~/.ssh/config` ^^^file. If it doesn't exist,^^^ `nano` ^^^will create it.^^^
        - `nano ~/.ssh/config`^^^ ^^^
        - ^^^Add the following configuration to the file. This configuration defines an alias^^^ `localhost_labex` ^^^for connecting to^^^ `localhost` ^^^as the^^^ `labex` ^^^user, and an alias^^^ `localhost_root` ^^^for connecting as the^^^ `root` ^^^user. It also explicitly specifies the^^^ `IdentityFile` ^^^for the^^^ `labex` ^^^user to use the^^^ `id_rsa` ^^^key generated in a previous step.^^^
        - ```
Host localhost_labex
    HostName localhost
    
``````
User
``````
(#c678dd) labex
    IdentityFile ~/.ssh/id_rsa

Host localhost_root
    HostName localhost
    
``````
User
``````
(#c678dd) root
```^^^ ^^^
        - ^^^Save the file by pressing^^^ `Ctrl+X`^^^, then^^^ `Y` ^^^to confirm saving, and^^^ `Enter` ^^^to confirm the filename.^^^
        - ^^^Now, let's try connecting to^^^ `localhost` ^^^using these new aliases.^^^
        - ^^^Connect as^^^ `labex` ^^^using the^^^ `localhost_labex` ^^^alias:^^^
        - `ssh localhost_labex`^^^ ^^^
        - ^^^Since you configured^^^ `IdentityFile ~/.ssh/id_rsa` ^^^and^^^ `id_rsa` ^^^does not have a passphrase, you should be logged in without being prompted for a password.^^^
        - ```
Last login: Mon Jun  9 01:54:16 2025 from 47.251.66.143
[labex@host ~]$
```^^^ ^^^
        - ^^^Exit the session:^^^
        - `exit`^^^ ^^^
        - ```
exit
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - ^^^Now, connect as^^^ `root` ^^^using the^^^ `localhost_root` ^^^alias:^^^
        - `ssh localhost_root`^^^ ^^^
        - ^^^You will be prompted for the^^^ `root` ^^^user's password. However, since root login is disabled in this environment, you will receive a "Permission denied" message:^^^
        - ```
root@localhost's password:
Permission denied, please try again.
root@localhost's password:
```^^^ ^^^
        - ^^^Press^^^ `Ctrl+C` ^^^to cancel the connection attempt:^^^
        - `C`^^^ ^^^
        - ^^^This demonstrates that the SSH configuration alias works, but the connection fails due to the security policy that disables root login.^^^
        - ^^^As you can see, using the^^^ `~/.ssh/config` ^^^file simplifies your SSH commands by pre-configuring common connection parameters.^^^
        - ^^^Let's add another entry to demonstrate specifying a different port. While^^^ `localhost` ^^^uses the default SSH port (22), this example shows how you would configure it if it were different.^^^
        - ^^^Open the^^^ `~/.ssh/config` ^^^file again:^^^
        - `nano ~/.ssh/config`^^^ ^^^
        - ^^^Add the following entry. This creates an alias^^^ `localhost_port_example` ^^^that explicitly sets the port to^^^ `2222`^^^. (Note:^^^ `localhost` ^^^does not actually listen on port 2222, so this connection will fail, but it demonstrates the configuration.)^^^
        - ```
Host localhost_labex
    HostName localhost
    
``````
User
``````
(#c678dd) labex
    IdentityFile ~/.ssh/id_rsa

Host localhost_root
    HostName localhost
    
``````
User
``````
(#c678dd) root

Host localhost_port_example
    HostName localhost
    Port 
``````
2222
``````
(#d19a66)
    
``````
User
``````
(#c678dd) labex
```^^^ ^^^
        - ^^^Save the file.^^^
        - ^^^Now, try to connect using the^^^ `localhost_port_example` ^^^alias:^^^
        - `ssh localhost_port_example`^^^ ^^^
        - ^^^This connection will fail because^^^ `localhost` ^^^is not listening on port 2222, but it demonstrates how to specify a custom port in your SSH config.^^^
        - ```
ssh: connect to host localhost port 2222: Cannot assign requested address

You can find some explanations for typical errors at this link:
            https://red.ht/support_rhel_ssh
```^^^ ^^^
        - ^^^You can view your current SSH configuration to see all the defined hosts:^^^
        - `cat`` ~/.ssh/config`^^^ ^^^
        - ```
Host localhost_labex
    HostName localhost
    User labex
    IdentityFile ~/.ssh/id_rsa

Host localhost_root
    HostName localhost
    User root

Host localhost_port_example
    HostName localhost
    Port 2222
    User labex
```^^^ ^^^
        - ^^^Finally, let's clean up the^^^ `~/.ssh/config` ^^^file by removing the^^^ `localhost_port_example` ^^^entry.^^^
        - ^^^Open the^^^ `~/.ssh/config` ^^^file:^^^
        - `nano ~/.ssh/config`^^^ ^^^
        - ^^^Delete the^^^ `Host localhost_port_example` ^^^block. The file should look like this:^^^
        - ```
Host localhost_labex
    HostName localhost
    
``````
User
``````
(#c678dd) labex
    IdentityFile ~/.ssh/id_rsa

Host localhost_root
    HostName localhost
    
``````
User
``````
(#c678dd) root
```^^^ ^^^
        - ^^^Save the file.^^^
        - 
        - # ^^^**Understanding OpenSSH Server Security Configuration**^^^
        - ^^^In this step, you will learn about OpenSSH server security best practices by examining the current security configuration. You will understand how root login restrictions and password authentication settings work to protect your server from unauthorized access.^^^
        - ^^^**Note:**^^^ ^^^In this lab environment, you will examine the current SSH security configuration and understand different security settings. This step focuses on understanding these security measures and learning about best practices for SSH server configuration.^^^
        - ## ^^^**Understanding Root Login Security**^^^
        - ^^^Allowing direct root login via SSH is generally discouraged because the root account has full administrative privileges. If an attacker gains access to the root account, they have complete control over your system. It's safer to log in as a regular user and then use^^^ `sudo` ^^^to perform administrative tasks.^^^
        - ^^^Let's examine the current root login configuration and test its effectiveness.^^^
        - ^^^First, log in via SSH as the^^^ `labex` ^^^user.^^^
        - `ssh labex@localhost`^^^ ^^^
        - ^^^You should log in without a password if your SSH key setup from previous steps is correct.^^^
        - ```
Last login: Mon Jun  9 01:57:27 2025 from 47.251.66.143
[labex@host ~]$
```^^^ ^^^
        - ^^^Now, let's examine the SSH server configuration file to understand the current security settings:^^^
        - `sudo ``cat`` /etc/ssh/sshd_config | grep -E ``"^PermitRootLogin|^#PermitRootLogin"``(#98c379)`^^^ ^^^
        - ^^^This command will show you the current PermitRootLogin setting. You should see something like:^^^
        - `PermitRootLogin no`^^^ ^^^
        - ^^^This setting means that direct root login via SSH is disabled, which is a security best practice.^^^
        - ^^^Let's test if root login is actually blocked. First, exit the current SSH session:^^^
        - `exit`^^^ ^^^
        - ```
exit
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - ^^^Now, attempt to log in as^^^ `root` ^^^to^^^ `localhost`^^^:^^^
        - `ssh root@localhost`^^^ ^^^
        - ^^^You should see a "Permission denied" message, indicating that direct root login is not allowed (this may already be configured in your environment).^^^
        - ```
root@localhost's password:
Permission denied, please try again.
root@localhost's password:
Permission denied, please try again.
root@localhost's password:
```^^^ ^^^
        - ^^^This confirms that root login is disabled in this environment, which is the desired security configuration. The "Permission denied" message demonstrates that the security measure is working effectively.^^^
        - ## ^^^**Understanding Password Authentication Security**^^^
        - ^^^Disabling password authentication forces users to rely on more secure methods like SSH key-based authentication. This significantly reduces the risk of brute-force attacks against your server.^^^
        - ^^^Let's examine the current password authentication setting and understand how it works.^^^
        - ^^^Log in via SSH as the^^^ `labex` ^^^user (using your SSH key):^^^
        - `ssh labex@localhost`^^^ ^^^
        - ```
Last login: Mon Jun  9 01:57:32 2025 from 127.0.0.1
[labex@host ~]$
```^^^ ^^^
        - ^^^First, let's check the current PasswordAuthentication setting:^^^
        - `sudo ``cat`` /etc/ssh/sshd_config | grep PasswordAuthentication`^^^ ^^^
        - ```
PasswordAuthentication yes
# PasswordAuthentication.  Depending on your PAM configuration,
# PAM authentication, then enable this but set PasswordAuthentication
```^^^ ^^^
        - ^^^As you can see,^^^ `PasswordAuthentication yes` ^^^is currently configured, which means password authentication is enabled. While this allows users to authenticate with passwords, it also presents a security risk as it makes the server vulnerable to brute-force password attacks.^^^
        - ^^^The output shows:^^^
            - `PasswordAuthentication yes` ^^^- This is the active setting that enables password authentication^^^
            - ^^^The commented lines provide additional context about PAM configuration^^^
        - ^^^This configuration means that users can authenticate using both passwords and SSH keys. For enhanced security, it's recommended to disable password authentication and rely solely on SSH key-based authentication.^^^
        - ^^^Exit the current SSH session:^^^
        - `exit`^^^ ^^^
        - ```
exit
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - ^^^Now, let's verify that SSH key-based authentication works properly while password authentication is disabled:^^^
        - `ssh labex@localhost`^^^ ^^^
        - ^^^This should succeed without a password prompt, using your SSH key:^^^
        - ```
Last login: Mon Jun  9 02:00:22 2025 from 127.0.0.1
[labex@host ~]$
```^^^ ^^^
        - ^^^This demonstrates several important security concepts:^^^
            1. ^^^**Password authentication is enabled**^^^ ^^^(^^^`PasswordAuthentication yes``(#3594f7)`^^^) - Users can log in with both passwords and SSH keys^^^
            2. ^^^**SSH key-based authentication works properly**^^^ ^^^- More secure authentication method is available^^^
            3. ^^^**The server allows both authentication methods**^^^ ^^^- While convenient, this may pose security risks from brute-force attacks^^^
            4. ^^^**Root login is disabled**^^^ ^^^- Administrative access requires proper user escalation^^^
        - ^^^**Security Recommendation:**^^^ ^^^For production environments, consider setting^^^ `PasswordAuthentication no` ^^^to enhance security by forcing users to use SSH key-based authentication only.^^^
        - ^^^Exit the session:^^^
        - `exit`^^^ ^^^
        - ```
exit
Connection to localhost closed.
[labex@host ~]$
```^^^ ^^^
        - ^^^You have successfully examined and understood the OpenSSH server security configuration. The server currently has root login disabled (which follows security best practices) and password authentication enabled (which provides flexibility but may require additional security considerations for production environments). You've also verified that SSH key-based authentication works properly as a more secure authentication method.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, participants learned to access systems using SSH, starting with verifying the^^^ `openssh-clients` ^^^installation and connecting to^^^ `localhost` ^^^via SSH. They practiced authenticating with a password and understood the initial host authenticity check.^^^
        - ^^^The lab further guided users through generating and utilizing SSH key pairs for passwordless authentication, managing these keys with^^^ `ssh-agent`^^^, and troubleshooting common SSH connection issues. Finally, participants learned to customize SSH client configurations and secure the OpenSSH server by disabling root login and password authentication, enhancing their understanding of secure remote access practices.^^^
    10. Analyze Logs in Red Hat Enterprise Linux
        - Understand System Log Architecture and Key Files
        - Review and Filter Syslog Files with common commands
        - Send Custom Syslog Messages Manually
        - Explore and Filter System Journal Entries with journalctl
        - Configure Persistent System Journal Storage
        - Maintain Accurate System Time with timedatectl and chronyd
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience with analyzing and storing system logs on Red Hat Enterprise Linux 9 using^^^ `journalctl` ^^^and^^^ `rsyslog`^^^. You will begin by understanding the core architecture of system logging, including the roles of^^^ `systemd-journald` ^^^and^^^ `rsyslog`^^^, and identifying key log files. Subsequently, you will learn to review and filter syslog files using common commands, manually send custom syslog messages, and explore and filter system journal entries with^^^ `journalctl`^^^. The lab also covers configuring persistent system journal storage and maintaining accurate system time using^^^ `timedatectl` ^^^and^^^ `chronyd`^^^, equipping you with essential skills for system analysis and troubleshooting.^^^
        - 
        - # ^^^**Understand System Log Architecture and Key Files**^^^
        - ^^^In this step, you will learn about the fundamental components of system logging in Red Hat Enterprise Linux 9, specifically focusing on the^^^ `systemd-journald` ^^^and^^^ `rsyslog` ^^^services, and the key log files they manage. Understanding this architecture is crucial for effective system analysis and troubleshooting.^^^
        - ^^^First, let's explore the^^^ `systemd-journald` ^^^service. This service is at the core of the operating system's event logging. It collects event messages from various sources, including the system kernel, early boot processes, standard output/error from daemons, and syslog events. The^^^ `systemd-journald` ^^^service stores these logs in a structured, indexed binary file called the^^^ `journal`^^^.^^^
        - ^^^Next, we'll look at the^^^ `rsyslog` ^^^service. While^^^ `systemd-journald` ^^^collects logs,^^^ `rsyslog` ^^^reads syslog messages from the journal as they arrive. It then processes these messages and records them to traditional log files in the^^^ `/var/log` ^^^directory or forwards them to other services based on its configuration. These^^^ `rsyslog` ^^^files persist across reboots.^^^
        - ^^^Let's examine some of the important log files managed by^^^ `rsyslog` ^^^in the^^^ `/var/log` ^^^directory. You can use the^^^ `ls` ^^^command to list the contents of this directory.^^^
        - `ls`` /var/log`^^^ ^^^
        - ^^^You will see a list of various log files. Based on your system, you should see files like^^^ `anaconda`^^^,^^^ `audit`^^^,^^^ `boot.log`^^^,^^^ `chrony`^^^,^^^ `cron`^^^,^^^ `dnf.log`^^^,^^^ `messages`^^^,^^^ `secure`^^^, and others. Some of the most common ones include:^^^
            - `/var/log/messages`^^^: This file contains most general syslog messages, excluding those related to authentication, email processing, scheduled job execution, and debugging.^^^
            - `/var/log/secure`^^^: This file stores syslog messages related to security and authentication events.^^^
            - `/var/log/maillog`^^^: This file contains syslog messages about the mail server.^^^
            - `/var/log/cron`^^^: This file logs syslog messages about scheduled job execution.^^^
            - `/var/log/boot.log`^^^: This file contains non-syslog console messages about system startup.^^^
        - ^^^To view the contents of these files, you can use commands like^^^ `cat`^^^,^^^ `less`^^^, or^^^ `tail`^^^. Note that most log files in^^^ `/var/log` ^^^require root privileges to read, so you'll need to use^^^ `sudo`^^^. For example, let's view the last few lines of the^^^ `/var/log/messages` ^^^file using^^^ `tail`^^^.^^^
        - `sudo ``tail`` /var/log/messages`^^^ ^^^
        - ^^^You can also view the contents of the^^^ `/var/log/secure` ^^^file, which is important for security auditing.^^^
        - `sudo ``tail`` /var/log/secure`^^^ ^^^
        - ^^^Understanding the purpose of these files will help you quickly locate relevant information when troubleshooting system issues.^^^
        - 
        - # ^^^**Review and Filter Syslog Files with common commands**^^^
        - ^^^In this step, you will learn how to effectively review and filter syslog files using common Linux commands. Syslog messages are categorized by^^^ `facility` ^^^(which subsystem produces the message) and^^^ `priority` ^^^(the message's severity). Understanding these categories is crucial for efficient log analysis.^^^
        - ^^^First, let's review the concept of Syslog Facilities and Priorities.^^^
        - ^^^**Syslog Facilities:**^^^ ^^^These indicate the source of the log message. Examples include^^^ `kern` ^^^(kernel messages),^^^ `user` ^^^(user-level messages),^^^ `mail` ^^^(mail system messages),^^^ `daemon` ^^^(system daemons messages),^^^ `auth` ^^^(authentication and security messages), and^^^ `cron` ^^^(clock daemon messages).^^^
        - ^^^**Syslog Priorities:**^^^ ^^^These define the severity of the message, ranging from^^^ `emerg` ^^^(system unusable) to^^^ `debug` ^^^(debugging-level message). The order of severity from highest to lowest is:^^^ `emerg`^^^,^^^ `alert`^^^,^^^ `crit`^^^,^^^ `err`^^^,^^^ `warning`^^^,^^^ `notice`^^^,^^^ `info`^^^,^^^ `debug`^^^.^^^
        - ^^^Log files can grow very large, making it difficult to find specific information. Therefore, filtering is essential. You can use commands like^^^ `grep`^^^,^^^ `awk`^^^, and^^^ `sed` ^^^to filter log file content.^^^
        - ^^^Let's start by viewing the entire content of^^^ `/var/log/messages` ^^^using^^^ `less`^^^. This command allows you to scroll through the file. Press^^^ `q` ^^^to exit^^^ `less`^^^. Remember to use^^^ `sudo` ^^^since log files require root privileges to read.^^^
        - `sudo less /var/log/messages`^^^ ^^^
        - ^^^Now, let's try to filter messages. Suppose you are interested in messages related to^^^ `authentication`^^^. These messages are typically found in^^^ `/var/log/secure`^^^. Use^^^ `grep` ^^^to search for lines containing the word "authentication" in^^^ `/var/log/secure`^^^. Remember to use^^^ `sudo` ^^^to access the log file.^^^
        - `sudo grep ``"authentication"``(#98c379)`` /var/log/secure`^^^ ^^^
        - ^^^You might not see any output if there are no recent authentication messages. Let's try a more common search term, like "sshd", which relates to the SSH daemon.^^^
        - `sudo grep ``"sshd"``(#98c379)`` /var/log/secure`^^^ ^^^
        - ^^^You should see output showing SSH daemon activities, authentication attempts, or other security-related events. The exact output will depend on the current system activity and may include entries like:^^^
        - ```
Dec 16 10:15:30 host sshd[1234]: Accepted publickey for labex from 172.25.0.10 port 12345 ssh2
Dec 16 10:15:30 host sshd[1234]: pam_unix(sshd:session): session opened for user labex(uid=1000) by (uid=0)
...output omitted...
```^^^ ^^^
        - ^^^Log messages also contain timestamps. You can filter messages by date and time. For instance, to see messages from a specific date, you can combine^^^ `grep` ^^^with the date. Let's try to find messages from today's date in^^^ `/var/log/messages`^^^. Use the current date format that appears in your system logs.^^^
        - `sudo grep ``"``(#98c379)``$(date '+%b %d')``(#e06c75)``"``(#98c379)`` /var/log/messages`^^^ ^^^
        - ^^^**Log File Rotation:**^^^
        - 
        - ^^^To prevent log files from consuming too much disk space, systems use^^^ `logrotate`^^^. This utility rotates log files, renaming old ones (e.g.,^^^ `/var/log/messages` ^^^becomes^^^ `/var/log/messages-20220320`^^^) and creating new, empty ones. After a certain period (typically four weeks), the oldest rotated log files are discarded. A scheduled job runs^^^ `logrotate` ^^^daily to manage this process.^^^
        - ^^^You can observe rotated log files by listing the contents of^^^ `/var/log` ^^^again. You might see files with date extensions or^^^ `.gz` ^^^extensions (if they have been compressed).^^^
        - `ls`` -l /var/log/messages*`^^^ ^^^
        - ^^^Example output:^^^
        - ```
-rw-------. 1 root root 123456 Mar 20 23:59 /var/log/messages
-rw-------. 1 root root  78901 Mar 13 23:59 /var/log/messages-20220320
-rw-------. 1 root root  54321 Mar 06 23:59 /var/log/messages-20220313.gz
...output omitted...
```^^^ ^^^
        - ^^^This shows how^^^ `logrotate` ^^^manages older log files.^^^
        - ^^^Finally, let's analyze the anatomy of a syslog entry. A typical log message in^^^ `/var/log/secure` ^^^looks like this:^^^
        - `Dec 16 10:11:48 host sshd[1433]: Failed password for student from 172.25.0.10 port 59344 ssh2`
            - `Dec 16 10:11:48`^^^: The timestamp of the log entry.^^^
            - `host`^^^: The host that sent the log message.^^^
            - `sshd[1433]`^^^: The program or process name (^^^`sshd`^^^) and its PID (^^^`1433`^^^) that sent the log message.^^^
            - `Failed password for …`^^^: The actual message content.^^^
        - ^^^Understanding this format helps you parse and interpret log entries more effectively.^^^
        - 
        - # ^^^**Send Custom Syslog Messages Manually**^^^
        - ^^^In this step, you will learn how to send custom syslog messages manually using the^^^ `logger` ^^^command. This is a useful technique for testing^^^ `rsyslog` ^^^service configurations or for injecting custom messages into the system logs for debugging or monitoring purposes.^^^
        - ^^^The^^^ `logger` ^^^command sends messages to the^^^ `rsyslog` ^^^service. By default, it sends the message with the^^^ `user` ^^^facility and^^^ `notice` ^^^priority (^^^`user.notice`^^^), unless specified otherwise with the^^^ `-p` ^^^option.^^^
        - ^^^Let's start by sending a simple test message to the default log location, which is typically^^^ `/var/log/messages`^^^.^^^
        - `logger ``"This is a test message from labex."``(#98c379)`^^^ ^^^
        - ^^^After executing the command, you can verify that the message was logged by checking the^^^ `/var/log/messages` ^^^file. Use^^^ `tail` ^^^to view the last few lines of the file. Remember to use^^^ `sudo` ^^^to access the log file.^^^
        - `sudo ``tail`` /var/log/messages`^^^ ^^^
        - ^^^You should see your custom message at the end of the output, similar to this:^^^
        - ```
...
Dec 16 10:30:00 host labex: This is a test message from labex.
```^^^ ^^^
        - ^^^Now, let's try sending a message with a specific facility and priority. Recall from the previous step that syslog messages are categorized by facility and priority. For example,^^^ `local7.notice` ^^^means the message will be logged with the^^^ `local7` ^^^facility and^^^ `notice` ^^^priority. The^^^ `local7` ^^^facility is often used for custom applications or boot messages, and it's typically directed to^^^ `/var/log/boot.log` ^^^by^^^ `rsyslog` ^^^configuration.^^^
        - ^^^To send a message to the^^^ `rsyslog` ^^^service to be recorded in the^^^ `/var/log/boot.log` ^^^log file, execute the following^^^ `logger` ^^^command:^^^
        - `logger -p local7.notice ``"Log entry created by labex for boot.log"``(#98c379)`^^^ ^^^
        - ^^^Now, verify that this message has been written to^^^ `/var/log/boot.log`^^^. Use^^^ `sudo` ^^^to access the log file.^^^
        - `sudo ``tail`` /var/log/boot.log`^^^ ^^^
        - ^^^You should see your custom message in the output:^^^
        - ```
...
Dec 16 10:31:00 host labex: Log entry created by labex for boot.log
```^^^ ^^^
        - ^^^This demonstrates how you can control where your custom messages are logged by specifying the facility and priority. This capability is very useful for testing^^^ `rsyslog` ^^^configurations and for injecting specific events into your system logs.^^^
        - 
        - # ^^^**Explore and Filter System Journal Entries with journalctl**^^^
        - ^^^In this step, you will learn how to explore and filter system journal entries using the^^^ `journalctl` ^^^command. As you learned, the^^^ `systemd-journald` ^^^service stores logging data in a structured, indexed binary file called the^^^ `journal`^^^. The^^^ `journalctl` ^^^command is your primary tool for interacting with this journal.^^^
        - ^^^Let's start by viewing all messages in the journal. When you run^^^ `journalctl` ^^^without any options, it displays all available log entries, starting from the oldest. Since you are logged in as^^^ `labex` ^^^with^^^ `sudo` ^^^privileges, you will have full access to the journal.^^^
        - `journalctl`^^^ ^^^
        - ^^^You will see a large amount of output. Press^^^ `q` ^^^to exit the^^^ `journalctl` ^^^viewer. Notice that^^^ `journalctl` ^^^highlights important log messages: messages at^^^ `notice` ^^^or^^^ `warning` ^^^priority are in bold text, while messages at the^^^ `error` ^^^priority or higher are in red text.^^^
        - ^^^Now, let's explore some common^^^ `journalctl` ^^^options for filtering and viewing specific entries.^^^
        - ^^^**1. View the last N log entries (**^^^`**-n**``(#3594f7)` ^^^**option):**^^^
        - 
        - ^^^By default,^^^ `journalctl -n` ^^^shows the last 10 log entries. You can specify a different number, for example, the last 5 entries:^^^
        - `journalctl -n 5`^^^ ^^^
        - ^^^You should see the 5 most recent log entries.^^^
        - ^^^**2. Follow new journal entries (**^^^`**-f**``(#3594f7)` ^^^**option):**^^^
        - 
        - ^^^Similar to the^^^ `tail -f` ^^^command, the^^^ `journalctl -f` ^^^option outputs the last 10 lines of the system journal and continues to output new journal entries as they are appended. This is very useful for real-time monitoring.^^^
        - `journalctl -f`^^^ ^^^
        - ^^^To exit this continuous output, press^^^ ^^^**Ctrl+C**^^^^^^.^^^
        - ^^^**3. Filter by priority (**^^^`**-p**``(#3594f7)` ^^^**option):**^^^
        - 
        - ^^^You can filter the output by the priority level of the journal entries. The^^^ `journalctl -p` ^^^option shows entries at a specified priority level (by name or by number) or higher. The priority levels, in ascending order, are^^^ `debug`^^^,^^^ `info`^^^,^^^ `notice`^^^,^^^ `warning`^^^,^^^ `err`^^^,^^^ `crit`^^^,^^^ `alert`^^^, and^^^ `emerg`^^^.^^^
        - ^^^Let's list journal entries at the^^^ `err` ^^^priority or higher:^^^
        - `journalctl -p err`^^^ ^^^
        - ^^^You might see error messages related to various system components.^^^
        - ^^^**4. Filter by systemd unit (**^^^`**-u**``(#3594f7)` ^^^**option):**^^^
        - 
        - ^^^You can show messages for a specified^^^ `systemd` ^^^unit by using the^^^ `journalctl -u` ^^^option and the unit name. For example, to view logs specifically for the^^^ `sshd` ^^^service:^^^
        - `journalctl -u sshd.service`^^^ ^^^
        - ^^^This will display all log entries related to the SSH daemon.^^^
        - ^^^**5. Filter by time range (**^^^`**--since**``(#3594f7)` ^^^**and**^^^ `**--until**``(#3594f7)` ^^^**options):**^^^
        - 
        - ^^^When looking for specific events, you can limit the output to a specific time frame. Both^^^ `--since` ^^^and^^^ `--until` ^^^options take a time argument in the "YYYY-MM-DD hh:mm:ss" format. Double quotation marks are required if there are spaces in the argument. You can also use relative terms like^^^ `yesterday`^^^,^^^ `today`^^^,^^^ `tomorrow`^^^, or time durations like^^^ `"-1 hour"`^^^.^^^
        - ^^^Let's view all journal entries from the beginning of today:^^^
        - `journalctl --since today`^^^ ^^^
        - ^^^Now, let's view entries from the last hour:^^^
        - `journalctl --since ``"-1 hour"``(#98c379)`^^^ ^^^
        - ^^^**6. View verbose output (**^^^`**-o verbose**``(#3594f7)` ^^^**option):**^^^
        - 
        - ^^^To see additional details about each log entry, including internal journal fields, you can use the^^^ `-o verbose` ^^^option. This can be helpful for advanced troubleshooting.^^^
        - `journalctl -n 1 -o verbose`^^^ ^^^
        - ^^^This will show the last log entry with all its verbose details. Notice fields like^^^ `_COMM` ^^^(command name),^^^ `_EXE` ^^^(path to executable),^^^ `_PID` ^^^(process ID),^^^ `_UID` ^^^(user ID), and^^^ `_SYSTEMD_UNIT` ^^^(systemd unit). These fields can be used for more precise filtering.^^^
        - ^^^For example, to find entries from a specific^^^ `sshd` ^^^process with a known PID (you can get a PID from a previous^^^ `journalctl -u sshd.service` ^^^output):^^^
        - `journalctl _SYSTEMD_UNIT=sshd.service _PID=<PID_NUMBER>`^^^ ^^^
        - ^^^Replace^^^ `<PID_NUMBER>` ^^^with an actual PID you observed from^^^ `sshd` ^^^entries. For instance, if you saw^^^ `sshd[1433]`^^^, you would use^^^ `_PID=1433`^^^.^^^
        - `journalctl _SYSTEMD_UNIT=sshd.service _PID=1433`^^^ ^^^
        - ^^^This command demonstrates how you can combine multiple filters to narrow down your search in the journal.^^^
        - 
        - # ^^^**Configure Persistent System Journal Storage**^^^
        - ^^^In this step, you will learn how to configure the system journal to persist across reboots. By default, Red Hat Enterprise Linux 9 stores the system journal in the^^^ `/run/log` ^^^directory, which is a temporary file system. This means that all journal entries are cleared after a system reboot. To retain historical log data, you need to configure the^^^ `systemd-journald` ^^^service for persistent storage.^^^
        - ^^^The configuration for^^^ `systemd-journald` ^^^is located in the^^^ `/etc/systemd/journald.conf` ^^^file. The^^^ `Storage` ^^^parameter within this file determines whether journals are stored in a volatile manner or persistently.^^^
        - ^^^The^^^ `Storage` ^^^parameter can be set to one of the following values:^^^
            - `persistent`^^^: Stores journals in the^^^ `/var/log/journal` ^^^directory, which persists across reboots. If this directory does not exist,^^^ `systemd-journald` ^^^will create it.^^^
            - `volatile`^^^: Stores journals in the temporary^^^ `/run/log/journal` ^^^directory. Data in^^^ `/run` ^^^does not persist across reboots. This is the default behavior if^^^ `Storage` ^^^is not explicitly set and^^^ `/var/log/journal` ^^^does not exist.^^^
            - `auto`^^^: If the^^^ `/var/log/journal` ^^^directory exists,^^^ `systemd-journald` ^^^uses persistent storage; otherwise, it uses volatile storage. This is the default if you do not set the^^^ `Storage` ^^^parameter.^^^
            - `none`^^^: No storage is used. All logs are dropped, though they can still be forwarded.^^^
        - ^^^Let's modify the^^^ `/etc/systemd/journald.conf` ^^^file to enable persistent journal storage. You will use^^^ `sudo nano` ^^^to edit this file.^^^
        - `sudo nano /etc/systemd/journald.conf`^^^ ^^^
        - ^^^Inside the^^^ `nano` ^^^editor, find the^^^ `[Journal]` ^^^section. Uncomment the^^^ `Storage` ^^^line (remove the^^^ `#` ^^^at the beginning) and set its value to^^^ `persistent`^^^.^^^
        - ^^^Your file should look similar to this (only showing relevant lines):^^^
        - ```
[Journal]
``````
(#e06c75)

``````
Storage
``````
(#d19a66)=persistent

``````
#Compress=yes
``````
(#5c6370)

``````
#Seal=yes
``````
(#5c6370)

``````
#SplitMode=uid
``````
(#5c6370)

``````
#SyncIntervalSec=5m
``````
(#5c6370)

``````
#RateLimitIntervalSec=30s
``````
(#5c6370)

``````
#RateLimitBurst=1000
``````
(#5c6370)

``````
#SystemMaxUse=
``````
(#5c6370)

``````
#SystemKeepFree=
``````
(#5c6370)

``````
#SystemMaxFileSize=
``````
(#5c6370)

``````
#SystemMaxFiles=100
``````
(#5c6370)

``````
#RuntimeMaxUse=
``````
(#5c6370)

``````
#RuntimeKeepFree=
``````
(#5c6370)

``````
#RuntimeMaxFileSize=
``````
(#5c6370)

``````
#RuntimeMaxFiles=100
``````
(#5c6370)

``````
#MaxRetentionSec=
``````
(#5c6370)

``````
#MaxFileSec=1month
``````
(#5c6370)

``````
#ForwardToSyslog=yes
``````
(#5c6370)

``````
#ForwardToKMsg=no
``````
(#5c6370)

``````
#ForwardToConsole=no
``````
(#5c6370)

``````
#ForwardToWall=yes
``````
(#5c6370)

``````
#TTYPath=/dev/console
``````
(#5c6370)

``````
#Audit=no
``````
(#5c6370)

``````
#FlushIntervalSec=
``````
(#5c6370)

``````
#SyncIntervalSec=
``````
(#5c6370)

``````
#ReadKMsg=yes
``````
(#5c6370)

``````
#Audit=yes
``````
(#5c6370)
```^^^ ^^^
        - ^^^After making the change, save the file by pressing^^^ ^^^**Ctrl+X**^^^^^^, then^^^ ^^^**Y**^^^ ^^^to confirm saving, and^^^ ^^^**Enter**^^^ ^^^to confirm the filename.^^^
        - ^^^For the changes to take effect, you need to restart the^^^ `systemd-journald` ^^^service. Since this environment is a Docker container,^^^ `systemctl` ^^^is not available. Instead, we will simulate the effect of restarting the service by ensuring the^^^ `/var/log/journal` ^^^directory is created and has the correct permissions, which^^^ `systemd-journald` ^^^would do upon restart in a non-containerized environment.^^^
        - ^^^First, let's create the directory if it doesn't exist and set appropriate permissions.^^^
        - ```
sudo 
``````
mkdir
``````
 -p /var/log/journal
sudo 
``````
chown
``````
 root:systemd-journal /var/log/journal
sudo 
``````
chmod
``````
 2755 /var/log/journal
```^^^ ^^^
        - ^^^Now, to verify that the persistent storage is configured and active, you can check if the^^^ `/var/log/journal` ^^^directory contains subdirectories with hexadecimal names and^^^ `.journal` ^^^files. These files store the structured and indexed journal entries.^^^
        - `ls`` -l /var/log/journal`^^^ ^^^
        - ^^^You should see a subdirectory with a long hexadecimal name (e.g.,^^^ `4ec03abd2f7b40118b1b357f479b3112``(#3594f7)`^^^). Inside this directory, you will find^^^ `.journal``(#3594f7)` ^^^files.^^^
        - `ls -l /var/log/journal/ <YOUR_HEX_ID> /`^^^ ^^^
        - ^^^Replace^^^ `<YOUR_HEX_ID>` ^^^with the actual hexadecimal ID you found in the previous^^^ `ls` ^^^command output. For example:^^^
        - `ls`` -l /var/log/journal/4ec03abd2f7b40118b1b357f479b3112/`^^^ ^^^
        - ^^^You should see files like^^^ `system.journal` ^^^and possibly^^^ `user-1000.journal`^^^.^^^
        - ^^^Even with persistent journals, the system does not keep all data forever. The journal has a built-in log rotation mechanism. You can configure size limits and retention periods in the^^^ `/etc/systemd/journald.conf` ^^^file using parameters like^^^ `SystemMaxUse`^^^,^^^ `SystemKeepFree`^^^,^^^ `SystemMaxFileSize`^^^, and^^^ `MaxRetentionSec`^^^.^^^
        - ^^^Finally, when persistent journals are enabled,^^^ `journalctl` ^^^output includes entries from the current system boot as well as previous system boots. To limit the output to a specific system boot, use the^^^ `journalctl -b` ^^^option.^^^
        - ^^^To list all recognized system boot events:^^^
        - `journalctl --list-boots`^^^ ^^^
        - ^^^You will see a list of boot IDs and their corresponding time ranges. The current boot is usually^^^ `0`^^^. Previous boots are negative numbers (^^^`-1`^^^,^^^ `-2`^^^, etc.).^^^
        - ^^^To view entries from the current system boot only:^^^
        - `journalctl -b`^^^ ^^^
        - ^^^To view entries from the previous boot (e.g., the one before the current one, usually^^^ `-1``(#3594f7)`^^^):^^^
        - `journalctl -b -1`^^^ ^^^
        - ^^^This concludes the configuration of persistent journal storage.^^^
        - 
        - # ^^^**Maintain Accurate System Time with timedatectl and chronyd**^^^
        - ^^^In this step, you will learn how to maintain accurate system time using the^^^ `timedatectl` ^^^command and understand the role of the^^^ `chronyd` ^^^service. Accurate timekeeping is crucial for logging, security, and many network services.^^^
        - ^^^**1. Using**^^^ `**timedatectl**` ^^^**to manage system time and time zones:**^^^
        - ^^^The^^^ `timedatectl` ^^^command provides an overview of the current time-related system settings, including the local time, universal time (UTC), RTC time, time zone, and NTP synchronization status.^^^
        - ^^^Let's check the current time settings of your system:^^^
        - `timedatectl`^^^ ^^^
        - ^^^You should see output similar to this (the exact time and date will reflect your current system time):^^^
        - ```
Local time: Sun 2025-06-15 21:46:11 EDT
           Universal time: Mon 2025-06-16 01:46:11 UTC
                 RTC time: Mon 2025-06-16 01:46:10
                Time zone: America/New_York (EDT, -0400)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```^^^ ^^^
        - ^^^You can list all available time zones using the^^^ `list-timezones` ^^^option:^^^
        - `timedatectl list-timezones | less`^^^ ^^^
        - ^^^Press^^^ `q` ^^^to exit^^^ `less`^^^. The time zones are named based on the Internet Assigned Numbers Authority (IANA) time zone database, typically by continent/ocean and then the largest city.^^^
        - ^^^To change the system's time zone, you use the^^^ `set-timezone` ^^^option. For example, let's change the time zone to^^^ `America/Phoenix`^^^. You need^^^ `sudo` ^^^privileges for this.^^^
        - `sudo timedatectl set-timezone America/Phoenix`^^^ ^^^
        - ^^^Now, verify the change:^^^
        - `timedatectl`^^^ ^^^
        - ^^^You should see the time zone updated to^^^ `America/Phoenix`^^^.^^^
        - ^^^You can also manually set the system's current time using the^^^ `set-time` ^^^option. The format is "YYYY-MM-DD hh:mm:ss", but you can omit the date or time. Let's set the time to^^^ `09:00:00` ^^^(for the current date).^^^
        - `sudo timedatectl set-time 09:00:00`^^^ ^^^
        - ^^^Verify the time change:^^^
        - `timedatectl`^^^ ^^^
        - ^^^Finally, the^^^ `set-ntp` ^^^option enables or disables NTP synchronization for automatic time adjustment. It takes^^^ `true` ^^^or^^^ `false` ^^^as an argument. Let's disable NTP synchronization for a moment (we will re-enable it later).^^^
        - `sudo timedatectl set-ntp ``false``(#56b6c2)`^^^ ^^^
        - ^^^Verify the NTP service status:^^^
        - `timedatectl`^^^ ^^^
        - ^^^You should see^^^ `NTP service: inactive`^^^.^^^
        - ^^^**2. Understanding and configuring the**^^^ `**chronyd**` ^^^**service:**^^^
        - ^^^The^^^ `chronyd` ^^^service is a daemon that keeps the system's Real-Time Clock (RTC) accurate by synchronizing it with Network Time Protocol (NTP) servers. It's the default NTP client in Red Hat Enterprise Linux.^^^
        - ^^^The configuration file for^^^ `chronyd` ^^^is^^^ `/etc/chrony.conf`^^^. By default, it uses public NTP servers. In a real-world scenario, you might configure it to use internal NTP servers.^^^
        - ^^^Let's view the default^^^ `chrony.conf` ^^^file.^^^
        - `cat`` /etc/chrony.conf`^^^ ^^^
        - ^^^You will see lines starting with^^^ `server` ^^^or^^^ `pool`^^^, which define the NTP sources. The^^^ `iburst` ^^^option is recommended as it takes four measurements quickly for more accurate initial synchronization.^^^
        - ^^^The^^^ `stratum` ^^^of an NTP time source indicates its quality. A^^^ `stratum 0` ^^^is a reference clock,^^^ `stratum 1` ^^^is directly attached to a reference clock, and^^^ `stratum 2` ^^^synchronizes from a^^^ `stratum 1` ^^^server.^^^
        - ^^^Since^^^ `systemctl` ^^^is not available in this container environment, we cannot directly restart^^^ `chronyd` ^^^to apply configuration changes. However, we can simulate the configuration change by modifying the file.^^^
        - ^^^Let's re-enable NTP synchronization using^^^ `timedatectl`^^^.^^^
        - `sudo timedatectl set-ntp ``true``(#56b6c2)`^^^ ^^^
        - ^^^Verify the NTP service status again:^^^
        - `timedatectl`^^^ ^^^
        - ^^^You should see^^^ `NTP service: active`^^^.^^^
        - ^^^The^^^ `chronyc` ^^^command acts as a client to the^^^ `chronyd` ^^^service. You can use it to monitor the synchronization status. The^^^ `chronyc sources` ^^^command shows the current time sources and their synchronization status.^^^
        - `chronyc sources -v`^^^ ^^^
        - ^^^The output will show details about the NTP sources. The asterisk^^^ `*` ^^^in the^^^ `S` ^^^(Source state) field indicates the source that^^^ `chronyd` ^^^is currently synchronized to.^^^
        - ```
.-- Source mode  '^' = server, '=' = peer, '#' = local clock.
 / .- Source state '*' = current best, '+' = combined, '-' = not combined,
| /             'x' = may be in error, '~' = too variable, '?' = unusable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^* 100.100.61.88                 1   5   377    16  +1824us[+2180us] +/-   85ms
...output omitted...
```^^^ ^^^
        - ^^^This output confirms that your system is actively synchronizing its time with an NTP server.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, we gained a comprehensive understanding of system log architecture in Red Hat Enterprise Linux 9, focusing on the interplay between^^^ `systemd-journald` ^^^and^^^ `rsyslog`^^^. We learned that^^^ `systemd-journald` ^^^collects and stores structured, indexed binary logs in the journal, while^^^ `rsyslog` ^^^processes these messages and writes them to traditional log files in^^^ `/var/log`^^^. We explored key log files like^^^ `/var/log/messages`^^^,^^^ `/var/log/secure`^^^, and others, and practiced reviewing and filtering syslog files using common commands. We also learned how to manually send custom syslog messages.^^^
        - ^^^Furthermore, we delved into exploring and filtering system journal entries using^^^ `journalctl`^^^, understanding its capabilities for accessing detailed system events. We then configured persistent system journal storage to ensure log data retention across reboots. Finally, we covered maintaining accurate system time using^^^ `timedatectl` ^^^and^^^ `chronyd`^^^, recognizing its importance for accurate log timestamps and overall system integrity. This lab provided essential skills for effective system analysis and troubleshooting through robust log management.^^^
    11. Configure Networking in Red Hat Enterprise Linux
        - Validate Network Interface Status and IP Addresses
        - Add a New Network Connection with Static IP
        - Activate and Deactivate Network Connections
        - Modify Existing Network Connection Settings
        - Configure System Hostname and Name Resolution
        - Test Network Connectivity and Name Resolution
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience configuring network interfaces and hostname settings on a Red Hat Enterprise Linux system. You will learn essential command-line tools and techniques to manage your system's network connectivity and identification.^^^
        - ^^^Throughout this lab, you will validate existing network interface status and IP addresses, add new network connections with static IP configurations, and practice activating and deactivating these connections. Furthermore, you will modify existing network settings, configure the system's hostname and name resolution, and finally, test network connectivity and name resolution to ensure all configurations are working as expected.^^^
        - 
        - # ^^^**Validate Network Interface Status and IP Addresses**^^^
        - ^^^In this step, you will learn how to validate the network interface status and IP addresses on your Red Hat Enterprise Linux system using command-line tools. Understanding your network configuration is crucial for troubleshooting connectivity issues and managing network services.^^^
        - ^^^First, let's explore the^^^ `ip link` ^^^command, which lists all available network interfaces on your system. This command provides a high-level overview of your network adapters, including their state (UP/DOWN), MAC addresses, and MTU (Maximum Transmission Unit).^^^
        - ^^^Open your terminal. You should see a prompt similar to^^^ `[labex@host ~]$`^^^.^^^
        - `ip ``link`` show`^^^ ^^^
        - ^^^You will see output similar to this, showing interfaces like^^^ `lo` ^^^(loopback),^^^ `eth0` ^^^and^^^ `eth1` ^^^(Ethernet interfaces with alternative names):^^^
        - ```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 00:16:3e:0f:9e:4e brd ff:ff:ff:ff:ff:ff
    altname enp0s6
    altname ens6
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 00:16:3e:0f:9e:51 brd ff:ff:ff:ff:ff:ff
    altname enp0s7
    altname ens7
```^^^ ^^^
        - ^^^Note that your system has two Ethernet interfaces (^^^`eth0``(#3594f7)` ^^^and^^^ `eth1``(#3594f7)`^^^) with alternative names (^^^`enp0s6``(#3594f7)`^^^/^^^`ens6``(#3594f7)` ^^^and^^^ `enp0s7``(#3594f7)`^^^/^^^`ens7``(#3594f7)` ^^^respectively). The^^^ `qdisc mq``(#3594f7)` ^^^indicates a multi-queue network scheduler is being used for better performance.^^^
        - ^^^Next, we will use the^^^ `ip addr` ^^^command to view detailed device and address information for a specific network interface. This command provides information about assigned IP addresses (IPv4 and IPv6), broadcast addresses, and subnet masks.^^^
        - ^^^Let's check the details for your^^^ `eth0` ^^^interface:^^^
        - `ip addr show eth0`^^^ ^^^
        - ^^^The output will show the IP addresses assigned to^^^ `eth0`^^^, including both IPv4 and IPv6 addresses if configured:^^^
        - ```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:16:3e:0f:9e:4e brd ff:ff:ff:ff:ff:ff
    altname enp0s6
    altname ens6
    inet 172.16.50.116/24 brd 172.16.50.255 scope global noprefixroute eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::216:3eff:fe0f:9e4e/64 scope link
       valid_lft forever preferred_lft forever
```^^^ ^^^
        - ^^^Notice that^^^ `eth0` ^^^has the IP address^^^ `172.16.50.116/24` ^^^with the^^^ `noprefixroute` ^^^flag, which indicates that NetworkManager is managing the routing for this interface.^^^
        - ^^^The^^^ `ip -s link show` ^^^command can also show statistics about network performance, such as the number of bytes and packets transmitted and received, as well as any errors or dropped packets. This is useful for a quick check of network traffic.^^^
        - `ip -s ``link`` show eth0`^^^ ^^^
        - ^^^You will see statistics for the^^^ `eth0` ^^^interface:^^^
        - ```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 00:16:3e:0f:9e:4e brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed   mcast
         90512     884      0       0       0       0
    TX:  bytes packets errors dropped carrier collsns
       1430185    1069      0       0       0       0
    altname enp0s6
    altname ens6
```^^^ ^^^
        - ^^^Finally, let's verify the routing table using the^^^ `ip route` ^^^command. The routing table determines how network traffic is directed to its destination.^^^
        - `ip route`^^^ ^^^
        - ^^^This command will display the IPv4 routing table, showing default routes and routes for specific networks. Since you have two network interfaces, you'll see multiple routes:^^^
        - ```
default via 172.16.50.253 dev eth0 proto dhcp src 172.16.50.116 metric 100
default via 172.16.50.253 dev eth1 proto dhcp src 172.16.50.117 metric 200
172.16.50.0/24 dev eth0 proto kernel scope link src 172.16.50.116 metric 100
172.16.50.0/24 dev eth1 proto kernel scope link src 172.16.50.117 metric 200
```^^^ ^^^
        - ^^^Notice there are two default routes with different metrics (100 and 200), meaning^^^ `eth0``(#3594f7)` ^^^has priority due to its lower metric value. Both interfaces are connected to the same network segment (172.16.50.0/24) and use the same gateway (172.16.50.253). The^^^ `eth0``(#3594f7)` ^^^interface has IP address^^^ `172.16.50.116/24``(#3594f7)` ^^^and^^^ `eth1``(#3594f7)` ^^^has^^^ `172.16.50.117/24``(#3594f7)`^^^.^^^
        - ^^^To view the IPv6 routing table, use the^^^ `ip -6 route` ^^^command:^^^
        - `ip -6 route`^^^ ^^^
        - ^^^You will see the IPv6 routing entries for both interfaces:^^^
        - ```
::1 dev lo proto kernel metric 256 pref medium
fe80::/64 dev eth0 proto kernel metric 256 pref medium
fe80::/64 dev eth1 proto kernel metric 256 pref medium
```^^^ ^^^
        - 
        - # ^^^**Add a New Network Connection with Static IP**^^^
        - ^^^In this step, you will learn how to add a new network connection with a static IP address using the^^^ `nmcli` ^^^command-line tool.^^^ `nmcli` ^^^is a powerful utility for controlling NetworkManager, which manages network connections on Red Hat Enterprise Linux.^^^
        - ^^^First, let's check the current network device status to identify available interfaces. This will help us choose an interface to configure.^^^
        - `nmcli dev status`^^^ ^^^
        - ^^^You will see output similar to this, showing devices like^^^ `eth0` ^^^and^^^ `eth1` ^^^with their respective connection names:^^^
        - ```
DEVICE  TYPE      STATE                   CONNECTION
eth0    ethernet  connected               System eth0
eth1    ethernet  connected               System eth1
lo      loopback  connected (externally)  lo
```^^^ ^^^
        - ^^^For this lab, we will use the^^^ `eth0` ^^^interface to create a new static connection. Note that your system already has active connections named^^^ `System eth0` ^^^and^^^ `System eth1` ^^^that are auto-generated by NetworkManager.^^^
        - ^^^Now, let's add a new network connection named^^^ `static-eth0` ^^^to the^^^ `eth0` ^^^interface. We will configure it with a static IPv4 address, a subnet mask, and a gateway. Based on the current network environment (172.16.50.0/24), we will use the following details:^^^
            - ^^^**Connection Name:**^^^ `static-eth0`
            - ^^^**Interface Name:**^^^ `eth0`
            - ^^^**IPv4 Address:**^^^ `172.16.50.200/24` ^^^(This means IP address 172.16.50.200 with a 24-bit subnet mask)^^^
            - ^^^**Gateway:**^^^ `172.16.50.253` ^^^(Same as the current gateway)^^^
        - ^^^Execute the following command to add the new connection. Remember to use^^^ `sudo` ^^^as network configuration changes require root privileges. You will not be prompted for a password.^^^
        - ^^^**Note:**^^^ ^^^If you already created a^^^ `static-eth0` ^^^connection with a different IP range (like 192.168.1.10/24), you should first delete it and recreate it with the correct IP range for this environment:^^^
        - ```
# Delete the existing connection if it exists with wrong IP range
``````
(#5c6370)
sudo nmcli con delete static-eth0
```^^^ ^^^
        - ```
# Add the new connection with correct IP range
``````
(#5c6370)
sudo nmcli con add con-name static-eth0 
``````
type
``````
(#e6c07b) ethernet ifname eth0 ipv4.addresses 172.16.50.200/24 ipv4.gateway 172.16.50.253 ipv4.method manual
```^^^ ^^^
        - ^^^After executing the command, you should see a confirmation message indicating that the connection was successfully added:^^^
        - `Connection 'static-eth0' (d4c42169-4134-4d3a-9b31-e837d62601bd) successfully added.``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^Let's break down the command:^^^
            - `sudo nmcli con add`^^^: This is the base command to add a new NetworkManager connection.^^^
            - `con-name static-eth0`^^^: This assigns the name^^^ `static-eth0` ^^^to our new connection profile.^^^
            - `type ethernet`^^^: Specifies that this is an Ethernet type connection.^^^
            - `ifname eth0`^^^: Binds this connection profile to the^^^ `eth0` ^^^network interface.^^^
            - `ipv4.addresses 172.16.50.200/24`^^^: Sets the static IPv4 address and subnet mask.^^^
            - `ipv4.gateway 172.16.50.253`^^^: Sets the default gateway for this connection.^^^
            - `ipv4.method manual`^^^: Configures the IPv4 address assignment method to manual (static), preventing it from trying to obtain an IP address via DHCP.^^^
        - ^^^Now, let's verify that the new connection profile has been created. We can use^^^ `nmcli con show` ^^^to list all available connections.^^^
        - `nmcli con show`^^^ ^^^
        - ^^^You should see^^^ `static-eth0` ^^^listed among your connections. Note that it is not active yet (no device assigned), while the system-generated connections are active:^^^
        - ```
NAME         UUID                                  TYPE      DEVICE
System eth0  5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  ethernet  eth0
System eth1  9c92fad9-6ecb-3e6c-eb4d-8a47c6f50c04  ethernet  eth1
lo           9eac3150-dd39-47e6-a375-f7165442a8eb  loopback  lo
static-eth0  d4c42169-4134-4d3a-9b31-e837d62601bd  ethernet  --
```^^^ ^^^
        - ^^^In the next step, we will learn how to activate this newly created connection.^^^
        - 
        - # ^^^**Activate and Deactivate Network Connections**^^^
        - ^^^In this step, you will learn how to activate and deactivate network connections using the^^^ `nmcli` ^^^command. Activating a connection brings the network interface up and applies the configuration defined in the connection profile. Deactivating a connection takes the interface down.^^^
        - ^^^First, let's list all network connections to see their current status. This will help us identify which connection is active on^^^ `eth0`^^^.^^^
        - `nmcli con show`^^^ ^^^
        - ^^^You will see output similar to this. Notice that^^^ `System eth0` ^^^is currently active on^^^ `eth0`^^^, and^^^ `static-eth0` ^^^is not active:^^^
        - ```
NAME         UUID                                  TYPE      DEVICE
System eth0  5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  ethernet  eth0
System eth1  9c92fad9-6ecb-3e6c-eb4d-8a47c6f50c04  ethernet  eth1
lo           8fe3e894-2a2e-446f-9abc-cdf612f0d973  loopback  lo
static-eth0  66094d3b-f21a-44f9-b1ef-3b2b2659e487  ethernet  --
```^^^ ^^^
        - ^^^Now, let's activate the^^^ `static-eth0` ^^^connection that you created in the previous step.^^^
        - ^^^**Important Note**^^^^^^: Since we're working in a remote environment, activating a connection with a different IP address on the primary interface (^^^`eth0``(#3594f7)`^^^) may cause your remote connection to be interrupted. In a production environment, you would typically:^^^
            1. ^^^Use a secondary interface for testing^^^
            2. ^^^Have console access to the machine^^^
            3. ^^^Configure the connection to use the same IP range as your current connection^^^
        - ^^^For this lab, we'll use^^^ `eth1` ^^^instead of^^^ `eth0` ^^^to avoid connection interruption. Let's first create a static connection for^^^ `eth1`^^^:^^^
        - `sudo nmcli con add con-name static-eth1 ``type`` ethernet ifname eth1 ipv4.addresses 172.16.50.201/24 ipv4.gateway 172.16.50.253 ipv4.method manual`^^^ ^^^
        - ^^^Now activate the^^^ `static-eth1` ^^^connection:^^^
        - `sudo nmcli con up static-eth1`^^^ ^^^
        - ^^^You should see a confirmation message indicating that the connection was successfully activated:^^^
        - `Connection 'static-eth1' successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/X)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^After activating^^^ `static-eth1`^^^, the original^^^ `System eth1` ^^^connection will automatically deactivate since only one connection can be active per device. Let's verify the status of your network devices and connections again.^^^
        - `nmcli dev status`^^^ ^^^
        - ^^^You should now see^^^ `eth1` ^^^associated with the^^^ `static-eth1` ^^^connection, while^^^ `eth0` ^^^remains with its original connection:^^^
        - ```
DEVICE  TYPE      STATE      CONNECTION
eth0    ethernet  connected  System eth0
eth1    ethernet  connected  static-eth1
lo      loopback  connected  lo
```^^^ ^^^
        - ^^^And let's check the connection list again to confirm^^^ `static-eth1` ^^^is active:^^^
        - `nmcli con show --active`^^^ ^^^
        - ^^^You should see^^^ `static-eth1` ^^^listed as an active connection, along with the other active connections:^^^
        - ```
NAME         UUID                                  TYPE      DEVICE
System eth0  5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  ethernet  eth0
lo           9eac3150-dd39-47e6-a375-f7165442a8eb  loopback  lo
static-eth1  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  ethernet  eth1
```^^^ ^^^
        - ^^^Now, let's verify that the^^^ `eth1` ^^^interface has the static IP address you configured.^^^
        - `ip addr show eth1`^^^ ^^^
        - ^^^The output should now show^^^ `172.16.50.201/24` ^^^as the IPv4 address for^^^ `eth1`^^^:^^^
        - ```
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:16:3e:0f:9e:51 brd ff:ff:ff:ff:ff:ff
    altname enp0s7
    altname ens7
    inet 172.16.50.201/24 brd 172.16.50.255 scope global eth1
       valid_lft forever preferred_lft forever
    inet6 fe80::216:3eff:fe0f:9e51/64 scope link
       valid_lft forever preferred_lft forever
```^^^ ^^^
        - ^^^Finally, let's learn how to deactivate a network connection. You can disconnect a device, which will bring down the active connection on that device.^^^
        - `sudo nmcli dev disconnect eth1`^^^ ^^^
        - ^^^You should see a confirmation message:^^^
        - `Device 'eth1' successfully disconnected.`^^^ ^^^
        - ^^^Verify the device status again.^^^ `eth1` ^^^should now be in a^^^ `disconnected` ^^^state.^^^
        - `nmcli dev status`^^^ ^^^
        - ```
DEVICE  TYPE      STATE         CONNECTION
eth0    ethernet  connected     System eth0
eth1    ethernet  disconnected  --
lo      loopback  connected     lo
```^^^ ^^^
        - ^^^Note that disconnecting the device will also deactivate the connection that was previously active on it. If you want to bring the original^^^ `System eth1` ^^^connection back up, you would activate it again using^^^ `sudo nmcli con up "System eth1"` ^^^(note the quotes around the connection name due to the space). For this lab, we will leave^^^ `eth1` ^^^disconnected for now.^^^
        - 
        - # ^^^**Modify Existing Network Connection Settings**^^^
        - ^^^In this step, you will learn how to modify the settings of an existing network connection using the^^^ `nmcli` ^^^command. This is a common task when you need to update IP addresses, DNS servers, or other network parameters.^^^
        - ^^^First, let's ensure our^^^ `static-eth1` ^^^connection is active, as we will be modifying its settings. If it's not active, activate it now.^^^
        - `sudo nmcli con up static-eth1`^^^ ^^^
        - ^^^You should see a confirmation message if it was activated, or a message indicating it's already active.^^^
        - `Connection 'static-eth1' successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/X)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^Now, let's view the current settings for the^^^ `static-eth1` ^^^connection. This command will show all configured properties for the connection.^^^
        - `nmcli con show static-eth1`^^^ ^^^
        - ^^^You will see a detailed output of the connection's properties. Pay attention to the^^^ `ipv4.addresses` ^^^and^^^ `ipv4.gateway` ^^^lines.^^^
        - ```
connection.id:                          static-eth1
connection.uuid:                        xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
connection.interface-name:              eth1
...
ipv4.addresses:                         { ip = 172.16.50.201/24, gw = 172.16.50.253 }
ipv4.gateway:                           172.16.50.253
...
```^^^ ^^^
        - ^^^Let's modify the IPv4 address of^^^ `static-eth1` ^^^to^^^ `172.16.50.221/24` ^^^and keep the same gateway^^^ `172.16.50.253`^^^.^^^
        - `sudo nmcli con mod static-eth1 ipv4.addresses 172.16.50.221/24 ipv4.gateway 172.16.50.253`^^^ ^^^
        - ^^^This command will modify the connection profile. However, for the changes to take effect, you need to deactivate and then reactivate the connection.^^^
        - ^^^First, deactivate the^^^ `eth1` ^^^device:^^^
        - `sudo nmcli dev disconnect eth1`^^^ ^^^
        - ^^^You should see:^^^
        - `Device 'eth1' successfully disconnected.`^^^ ^^^
        - ^^^Then, reactivate the^^^ `static-eth1` ^^^connection:^^^
        - `sudo nmcli con up static-eth1`^^^ ^^^
        - ^^^You should see:^^^
        - `Connection 'static-eth1' successfully activated (D-Bus active path: /org/freedesktop/NetworkManager/ActiveConnection/X)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^Now, let's verify that the IP address and gateway have been updated.^^^
        - `ip addr show eth1`^^^ ^^^
        - ^^^The output should now reflect the new IP address^^^ `172.16.50.221/24`^^^. Note that you may also see a secondary IP address from the previous configuration:^^^
        - ```
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 00:16:3e:0f:a2:70 brd ff:ff:ff:ff:ff:ff
    altname enp0s7
    altname ens7
    inet 172.16.50.221/24 brd 172.16.50.255 scope global noprefixroute eth1
       valid_lft forever preferred_lft forever
    inet 172.16.50.122/24 brd 172.16.50.255 scope global secondary noprefixroute eth1
       valid_lft forever preferred_lft forever
```^^^ ^^^
        - ^^^And check the routing table to confirm the gateway:^^^
        - `ip route`^^^ ^^^
        - ^^^You should see routes for both interfaces, with^^^ `eth1` ^^^having the new IP address. Note that you may see additional routes if there are secondary IP addresses:^^^
        - ```
default via 172.16.50.253 dev eth0 proto dhcp src 172.16.50.121 metric 100
default via 172.16.50.253 dev eth1 proto static metric 101
172.16.50.0/24 dev eth0 proto kernel scope link src 172.16.50.121 metric 100
172.16.50.0/24 dev eth1 proto kernel scope link src 172.16.50.221 metric 101
172.16.50.0/24 dev eth1 proto kernel scope link src 172.16.50.122 metric 101
```^^^ ^^^
        - ^^^You can also add or remove specific values from multi-valued settings, like DNS servers. Let's add a DNS server^^^ `8.8.8.8` ^^^to our^^^ `static-eth1` ^^^connection.^^^
        - `sudo nmcli con mod static-eth1 +ipv4.dns 8.8.8.8`^^^ ^^^
        - ^^^To apply this change, you need to deactivate and reactivate the connection again. You can run these commands on separate lines or combine them:^^^
        - ```
sudo nmcli dev disconnect eth1
sudo nmcli con up static-eth1
```^^^ ^^^
        - ^^^Verify the DNS settings:^^^
        - `nmcli con show static-eth1 | grep ipv4.dns`^^^ ^^^
        - ^^^You should see^^^ `8.8.8.8` ^^^listed as a DNS server:^^^
        - `ipv4.dns:                               8.8.8.8`^^^ ^^^
        - 
        - # ^^^**Configure System Hostname and Name Resolution**^^^
        - ^^^In this step, you will learn how to configure your system's hostname and manage name resolution settings. The hostname is a unique name that identifies your system on a network, and name resolution is the process of translating hostnames into IP addresses and vice versa.^^^
        - ^^^First, let's check the current hostname of your system using the^^^ `hostname` ^^^command.^^^
        - `hostname`^^^ ^^^
        - ^^^You will see the current hostname, which might be a default value like^^^ `host` ^^^or^^^ `localhost.localdomain`^^^.^^^
        - `host`^^^ ^^^
        - ^^^To set a static hostname, we use the^^^ `hostnamectl` ^^^command. This command modifies the^^^ `/etc/hostname` ^^^file, which persists the hostname across reboots. Let's set the hostname to^^^ `server.labex.example.com`^^^.^^^
        - `sudo hostnamectl set-hostname server.labex.example.com`^^^ ^^^
        - ^^^After setting the hostname, you can verify it using^^^ `hostnamectl status`^^^.^^^
        - `hostnamectl status`^^^ ^^^
        - ^^^You should see the new static hostname listed:^^^
        - ```
Static hostname: server.labex.example.com
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
         Boot ID: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  Virtualization: kvm
Operating System: Red Hat Enterprise Linux 9.6 (Plow)
     CPE OS Name: cpe:/o:redhat:enterprise_linux:9::baseos
          Kernel: Linux 5.14.0-xxx.el9.x86_64
    Architecture: x86-64
 Hardware Vendor: Alibaba Cloud
  Hardware Model: Alibaba Cloud ECS
```^^^ ^^^
        - ^^^You can also directly check the content of the^^^ `/etc/hostname` ^^^file:^^^
        - `cat`` /etc/hostname`^^^ ^^^
        - ^^^This will show your new hostname:^^^
        - `server.labex.example.com`^^^ ^^^
        - ^^^Next, let's configure name resolution. Linux systems typically use the^^^ `/etc/hosts` ^^^file for local hostname-to-IP address mappings before querying DNS servers. Let's add an entry to^^^ `/etc/hosts` ^^^for a fictitious server^^^ `webserver.labex.example.com` ^^^with IP address^^^ `192.168.1.100`^^^.^^^
        - ^^^We will use^^^ `sudo nano` ^^^to edit the^^^ `/etc/hosts` ^^^file.^^^
        - `sudo nano /etc/hosts`^^^ ^^^
        - ^^^Add the following line at the end of the file:^^^
        - `192.168.1.100   webserver.labex.example.com`^^^ ^^^
        - ^^^Press^^^ `Ctrl+X`^^^, then^^^ `Y` ^^^to save, and^^^ `Enter` ^^^to confirm the filename.^^^
        - ^^^Now, let's verify that the entry is present in^^^ `/etc/hosts`^^^:^^^
        - `cat`` /etc/hosts`^^^ ^^^
        - ^^^You should see your added entry:^^^
        - ```
127.0.0.1       localhost localhost.localdomain localhost4 localhost4.localdomain4
::1             localhost localhost.localdomain localhost6 localhost6.localdomain6
192.168.1.100   webserver.labex.example.com
```^^^ ^^^
        - ^^^To test hostname resolution using the^^^ `/etc/hosts` ^^^file, you can use the^^^ `getent hosts` ^^^command. This command queries the Name Service Switch (NSS) configuration, which includes^^^ `/etc/hosts`^^^.^^^
        - `getent hosts webserver.labex.example.com`^^^ ^^^
        - ^^^You should see the IP address resolved from your^^^ `/etc/hosts` ^^^file:^^^
        - `192.168.1.100   webserver.labex.example.com`^^^ ^^^
        - ^^^Finally, let's look at the^^^ `/etc/resolv.conf` ^^^file, which controls how DNS queries are performed. NetworkManager typically manages this file. In the previous step, you added^^^ `8.8.8.8` ^^^as a DNS server to your^^^ `static-eth1` ^^^connection. Let's verify that it appears in^^^ `/etc/resolv.conf`^^^.^^^
        - `cat`` /etc/resolv.conf`^^^ ^^^
        - ^^^You should see^^^ `nameserver 8.8.8.8` ^^^listed along with other system nameservers:^^^
        - ```
# Generated by NetworkManager
search labex.example.com
nameserver 100.100.2.136
nameserver 100.100.2.138
nameserver 8.8.8.8
```^^^ ^^^
        - ^^^Note: The^^^ `search` ^^^directive and system nameservers may vary based on your environment. The important thing is that^^^ `8.8.8.8` ^^^appears in the list.^^^
        - 
        - # ^^^**Test Network Connectivity and Name Resolution**^^^
        - ^^^In this final step, you will test network connectivity and name resolution using various command-line tools. This will help you confirm that your network configurations are working as expected.^^^
        - ^^^First, let's use the^^^ `ping` ^^^command to test basic network connectivity to a known IP address. We will ping the gateway^^^ `172.16.50.253` ^^^that we configured in the previous step. The^^^ `-c3` ^^^option sends only 3 packets.^^^
        - `ping -c3 172.16.50.253`^^^ ^^^
        - ^^^You should see successful replies, indicating connectivity to your gateway:^^^
        - ```
PING 172.16.50.253 (172.16.50.253) 56(84) bytes of data.
64 bytes from 172.16.50.253: icmp_seq=1 ttl=64 time=0.052 ms
64 bytes from 172.16.50.253: icmp_seq=2 ttl=64 time=0.049 ms
64 bytes from 172.16.50.253: icmp_seq=3 ttl=64 time=0.045 ms

--- 172.16.50.253 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2000ms
rtt min/avg/max/mdev = 0.045/0.049/0.052/0.003 ms
```^^^ ^^^
        - ^^^Note: You can interrupt the ping command at any time by pressing^^^ `Ctrl+C` ^^^if needed.^^^
        - ^^^Next, let's test name resolution for the^^^ `webserver.labex.example.com` ^^^entry you added to^^^ `/etc/hosts`^^^. We'll use^^^ `getent hosts` ^^^again, as it consults^^^ `/etc/hosts` ^^^first.^^^
        - `getent hosts webserver.labex.example.com`^^^ ^^^
        - ^^^You should see the IP address^^^ `192.168.1.100` ^^^returned:^^^
        - `192.168.1.100   webserver.labex.example.com`^^^ ^^^
        - ^^^Now, let's test DNS resolution for an external hostname, like^^^ `google.com`^^^, using the^^^ `host` ^^^command. This command queries your configured DNS servers (which should include^^^ `8.8.8.8` ^^^from your^^^ `static-eth0` ^^^connection).^^^
        - `host google.com`^^^ ^^^
        - ^^^You should see the IP addresses for^^^ `google.com`^^^:^^^
        - ```
google.com has address 142.251.46.174
google.com has IPv6 address 2607:f8b0:4005:802::200e
google.com mail is handled by 10 smtp.google.com.
```^^^ ^^^
        - ^^^The^^^ `dig` ^^^command is another powerful tool for querying DNS name servers. It provides more detailed information about the DNS query.^^^
        - `dig google.com`^^^ ^^^
        - ^^^You will see a more verbose output, including the DNS server that responded and the query details:^^^
        - ```
; <<>> DiG 9.16.23-RH <<>> google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 21983
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             1       IN      A       142.251.46.174

;; Query time: 1 msec
;; SERVER: 100.100.2.136#53(100.100.2.136)
;; WHEN: Mon Jun 16 10:18:26 CST 2025
;; MSG SIZE  rcvd: 44
```^^^ ^^^
        - ^^^Finally, let's use the^^^ `ss` ^^^command to display socket statistics and confirm active network connections. We'll use^^^ `-t` ^^^for TCP sockets and^^^ `-a` ^^^for all (listening and established) sockets.^^^
        - `ss -ta`^^^ ^^^
        - ^^^You will see a list of TCP connections and listening ports on your system:^^^
        - ```
State                                Recv-Q                                Send-Q                                                               Local Address:Port                                                                      Peer Address:Port
LISTEN                               0                                     128                                                                        0.0.0.0:exlm-agent                                                                     0.0.0.0:*
LISTEN                               0                                     128                                                                        0.0.0.0:ssh                                                                            0.0.0.0:*
ESTAB                                0                                     0                                                                    172.16.50.121:exlm-agent                                                               172.16.50.251:36354
LISTEN                               0                                     128                                                                           [::]:ssh                                                                               [::]:*
```^^^ ^^^
        - ^^^This concludes the lab on managing networking. You have successfully validated network configurations, added and modified connections, configured hostname and name resolution, and tested connectivity.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, we gained practical experience in managing network interfaces and hostname configurations on a Red Hat Enterprise Linux system. We began by validating network interface status and IP addresses using^^^ `ip link` ^^^and^^^ `ip addr` ^^^commands, understanding how to interpret their output for network diagnostics.^^^
        - ^^^Subsequently, we learned to add new network connections with static IP addresses, activate and deactivate these connections, and modify existing network settings, demonstrating proficiency in^^^ `nmcli` ^^^for network management. Finally, we configured the system hostname and name resolution, and verified network connectivity and name resolution, solidifying our understanding of essential Linux networking concepts.^^^
    12. Transfer Files in Red Hat Enterprise Linux
        - Create and List tar Archives
        - Extract Files from tar Archives
        - Create Compressed tar Archives
        - Transfer Files Securely with sftp
        - Synchronize Files Securely with rsync
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain practical experience in managing and transferring files efficiently and securely on a RHEL system. You will learn to create, list, and extract files from^^^ `tar` ^^^archives, including compressed archives, which are essential for packaging and backing up data.^^^
        - ^^^Furthermore, this lab will guide you through securely transferring files using^^^ `sftp` ^^^for interactive file transfers and^^^ `rsync` ^^^for robust and efficient file synchronization, ensuring data integrity and security during network operations.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level lab with a^^^ ^^^91%^^^ ^^^completion rate. It has received a^^^ ^^^100%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Create and List tar Archives**^^^
        - ^^^In this step, you will learn how to create and list^^^ `tar` ^^^archives. The^^^ `tar` ^^^utility is a powerful command-line tool used for archiving files and directories. It is commonly used for backups and transferring files.^^^
        - ^^^The^^^ `tar` ^^^command requires an action option to specify what operation it should perform. Common action options include:^^^
            - `-c` ^^^or^^^ `--create`^^^: Creates a new archive.^^^
            - `-t` ^^^or^^^ `--list`^^^: Lists the contents of an archive.^^^
            - `-x` ^^^or^^^ `--extract`^^^: Extracts files from an archive.^^^
        - ^^^Additionally,^^^ `tar` ^^^often uses general options to modify its behavior:^^^
            - `-v` ^^^or^^^ `--verbose`^^^: Displays the files being processed during the archiving or extraction.^^^
            - `-f` ^^^or^^^ `--file`^^^: Specifies the name of the archive file. This option must be followed by the archive filename.^^^
        - ^^^Let's start by creating some sample files that we will archive. Navigate to your^^^ `~/project` ^^^directory, which is your default working directory.^^^
        - `cd`` ~/project`^^^ ^^^
        - ^^^Now, create a new directory named^^^ `my_files` ^^^and some sample text files inside it.^^^
        - ```
mkdir
``````
 my_files

``````
echo
``````
 
``````
"This is file1 content."
``````
(#98c379) > my_files/file1.txt

``````
echo
``````
 
``````
"This is file2 content."
``````
(#98c379) > my_files/file2.txt

``````
echo
``````
 
``````
"This is file3 content."
``````
(#98c379) > my_files/file3.txt

``````
ls
``````
 my_files
```^^^ ^^^
        - ^^^You should see the three files listed:^^^
        - `file1.txt  file2.txt  file3.txt`^^^ ^^^
        - ^^^Now, let's create a^^^ `tar` ^^^archive of the^^^ `my_files` ^^^directory. We will name the archive^^^ `my_archive.tar`^^^.^^^
        - `tar -cvf my_archive.tar my_files`^^^ ^^^
        - ^^^The output will show the files being added to the archive:^^^
        - ```
my_files/
my_files/file1.txt
my_files/file2.txt
my_files/file3.txt
```^^^ ^^^
        - ^^^You can verify that the archive file^^^ `my_archive.tar` ^^^has been created in your current directory:^^^
        - `ls`^^^ ^^^
        - ^^^You should see^^^ `my_archive.tar` ^^^listed along with^^^ `my_files`^^^:^^^
        - `my_archive.tar  my_files`^^^ ^^^
        - ^^^Next, let's list the contents of the^^^ `my_archive.tar` ^^^file using the^^^ `-t` ^^^(list) and^^^ `-f` ^^^(file) options.^^^
        - `tar -tf my_archive.tar`^^^ ^^^
        - ^^^The output will show the contents of the archive:^^^
        - ```
my_files/
my_files/file1.txt
my_files/file2.txt
my_files/file3.txt
```^^^ ^^^
        - ^^^If you want to see more detailed information, such as file permissions, ownership, and size, you can add the^^^ `-v` ^^^(verbose) option:^^^
        - `tar -tvf my_archive.tar`^^^ ^^^
        - ^^^The output will be similar to this, providing more details about each archived item:^^^
        - ```
drwxr-xr-x labex/labex        0 2023-10-27 10:00 my_files/
-rw-r--r-- labex/labex       22 2023-10-27 10:00 my_files/file1.txt
-rw-r--r-- labex/labex       22 2023-10-27 10:00 my_files/file2.txt
-rw-r--r-- labex/labex       22 2023-10-27 10:00 my_files/file3.txt
```^^^ ^^^
        - ^^^Notice that^^^ `tar` ^^^by default removes the leading^^^ `/` ^^^from absolute paths when archiving. This is a safety measure to prevent accidental overwriting of system files when extracting archives. For example, if you were to archive^^^ `/etc/hosts`^^^, it would be stored as^^^ `etc/hosts` ^^^inside the^^^ `tar` ^^^file. This allows you to extract it to a new location without affecting the original^^^ `/etc/hosts` ^^^file.^^^
        - 
        - # ^^^**Extract Files from tar Archives**^^^
        - ^^^In this step, you will learn how to extract files from a^^^ `tar` ^^^archive. Extracting files is the process of taking the archived contents and placing them back into the file system.^^^
        - ^^^The primary option for extracting files is^^^ `-x` ^^^or^^^ `--extract`^^^. You will also typically use^^^ `-f` ^^^to specify the archive file and^^^ `-v` ^^^for verbose output to see which files are being extracted.^^^
        - ^^^Before extracting, it's a good practice to extract archives into an empty directory to avoid overwriting existing files or mixing them with other content. Let's create a new directory called^^^ `extracted_files` ^^^in your^^^ `~/project` ^^^directory.^^^
        - ```
cd
``````
 ~/project

``````
mkdir
``````
 extracted_files
```^^^ ^^^
        - ^^^Now, navigate into the^^^ `extracted_files` ^^^directory. This ensures that the contents of the archive will be extracted here.^^^
        - `cd`` extracted_files`^^^ ^^^
        - ^^^Now, let's extract the contents of^^^ `my_archive.tar` ^^^(which is located in the parent directory,^^^ `~/project`^^^) into the current^^^ `extracted_files` ^^^directory.^^^
        - `tar -xvf ../my_archive.tar`^^^ ^^^
        - ^^^The output will show the files being extracted:^^^
        - ```
my_files/
my_files/file1.txt
my_files/file2.txt
my_files/file3.txt
```^^^ ^^^
        - ^^^After extraction, you can list the contents of the current directory (^^^`~/project/extracted_files``(#3594f7)`^^^) to verify that the^^^ `my_files``(#3594f7)` ^^^directory and its contents have been successfully extracted.^^^
        - `ls`^^^ ^^^
        - ^^^You should see the^^^ `my_files` ^^^directory:^^^
        - `my_files`^^^ ^^^
        - ^^^Now, let's check the contents of the^^^ `my_files` ^^^directory inside^^^ `extracted_files`^^^:^^^
        - `ls`` my_files`^^^ ^^^
        - ^^^You should see the original files:^^^
        - `file1.txt  file2.txt  file3.txt`^^^ ^^^
        - ^^^You can also view the content of one of the extracted files to confirm its integrity:^^^
        - `cat`` my_files/file1.txt`^^^ ^^^
        - ^^^The output should be:^^^
        - `This is file1 content.`^^^ ^^^
        - ^^^When extracting files, the^^^ `tar` ^^^command uses the current^^^ `umask` ^^^to set permissions for the extracted files. However, if you want to preserve the original file permissions as they were in the archive, you can use the^^^ `-p` ^^^or^^^ `--preserve-permissions` ^^^option. This is particularly useful when dealing with executable scripts or configuration files where specific permissions are crucial. For the^^^ `root` ^^^user, this option is often enabled by default. For regular users, it's good practice to include it if permission preservation is important.^^^
        - ^^^For this lab, we will not demonstrate the^^^ `-p` ^^^option explicitly, as the default behavior is sufficient for our text files. However, keep this option in mind for future use cases.^^^
        - 
        - # ^^^**Create Compressed tar Archives**^^^
        - ^^^In this step, you will learn how to create compressed^^^ `tar` ^^^archives. While^^^ `tar` ^^^itself only bundles files, it can integrate with compression utilities like^^^ `gzip`^^^,^^^ `bzip2`^^^, and^^^ `xz` ^^^to create smaller archive files. This is crucial for saving disk space and reducing transfer times.^^^
        - ^^^The^^^ `tar` ^^^command provides specific options for different compression algorithms:^^^
            - `-z` ^^^or^^^ `--gzip`^^^: Uses^^^ `gzip` ^^^compression, resulting in a^^^ `.tar.gz` ^^^or^^^ `.tgz` ^^^suffix. This is the most common and fastest compression method.^^^
            - `-j` ^^^or^^^ `--bzip2`^^^: Uses^^^ `bzip2` ^^^compression, resulting in a^^^ `.tar.bz2` ^^^or^^^ `.tbz` ^^^suffix. This generally offers better compression than^^^ `gzip` ^^^but is slower.^^^
            - `-J` ^^^or^^^ `--xz`^^^: Uses^^^ `xz` ^^^compression, resulting in a^^^ `.tar.xz` ^^^or^^^ `.txz` ^^^suffix. This provides the best compression ratio among the three but is the slowest.^^^
            - `-a` ^^^or^^^ `--auto-compress`^^^: Allows^^^ `tar` ^^^to automatically determine the compression algorithm based on the archive's suffix (e.g.,^^^ `.tar.gz` ^^^implies^^^ `gzip`^^^). This is a convenient option.^^^
        - ^^^Let's start by ensuring you are in your^^^ `~/project` ^^^directory.^^^
        - `cd`` ~/project`^^^ ^^^
        - ^^^First, we will create a^^^ `gzip` ^^^compressed archive of the^^^ `my_files` ^^^directory. We will name it^^^ `my_archive.tar.gz`^^^.^^^
        - `tar -czvf my_archive.tar.gz my_files`^^^ ^^^
        - ^^^The output will show the files being added and compressed:^^^
        - ```
my_files/
my_files/file1.txt
my_files/file2.txt
my_files/file3.txt
```^^^ ^^^
        - ^^^You can verify the creation of the compressed archive:^^^
        - `ls`` -lh my_archive.tar.gz`^^^ ^^^
        - ^^^The^^^ `-lh` ^^^options for^^^ `ls` ^^^provide a human-readable size. You will see output similar to this, showing the file size:^^^
        - `-rw-r--r-- 1 labex labex 180 Oct 27 10:00 my_archive.tar.gz`^^^ ^^^
        - ^^^(Note: The exact size might vary slightly depending on the system and content, but it will be a small size for these small text files.)^^^
        - ^^^Now, let's try creating an^^^ `xz` ^^^compressed archive, which typically offers better compression. We will name it^^^ `my_archive.tar.xz`^^^.^^^
        - `tar -cJvf my_archive.tar.xz my_files`^^^ ^^^
        - ^^^Again, the output will show the files being processed:^^^
        - ```
my_files/
my_files/file1.txt
my_files/file2.txt
my_files/file3.txt
```^^^ ^^^
        - ^^^Check the size of the^^^ `xz` ^^^archive:^^^
        - `ls`` -lh my_archive.tar.xz`^^^ ^^^
        - ^^^You might notice that^^^ `my_archive.tar.xz` ^^^is slightly smaller than^^^ `my_archive.tar.gz`^^^, demonstrating the better compression ratio of^^^ `xz`^^^.^^^
        - `-rw-r--r-- 1 labex labex 168 Oct 27 10:00 my_archive.tar.xz`^^^ ^^^
        - ^^^To extract a compressed^^^ `tar` ^^^archive,^^^ `tar` ^^^is smart enough to often detect the compression type automatically when using the^^^ `-x` ^^^option. However, it's good practice to explicitly use the corresponding decompression option (^^^`-z`^^^,^^^ `-j`^^^, or^^^ `-J`^^^) or the^^^ `-a` ^^^(auto-compress) option.^^^
        - ^^^Let's try extracting^^^ `my_archive.tar.gz` ^^^into a new directory called^^^ `extracted_gz`^^^.^^^
        - ```
mkdir
``````
 extracted_gz
tar -xzvf my_archive.tar.gz -C extracted_gz
```^^^ ^^^
        - ^^^The^^^ `-C` ^^^option (change directory) tells^^^ `tar` ^^^to extract the files into the specified directory. This is a very useful option to avoid cluttering your current directory.^^^
        - ^^^Verify the contents of^^^ `extracted_gz`^^^:^^^
        - `ls`` extracted_gz/my_files`^^^ ^^^
        - ^^^You should see:^^^
        - `file1.txt  file2.txt  file3.txt`^^^ ^^^
        - 
        - # ^^^**Transfer Files Securely with sftp**^^^
        - ^^^In this step, you will learn how to securely transfer files between systems using^^^ `sftp` ^^^(Secure File Transfer Program).^^^ `sftp` ^^^is an interactive file transfer program that uses SSH (Secure Shell) for secure communication, providing encryption and authentication. It is part of the OpenSSH suite.^^^
        - ^^^For this lab, we will simulate a remote system by using the^^^ `labex` ^^^user on the same host as a "remote" user. This allows us to practice^^^ `sftp` ^^^commands without needing a separate virtual machine.^^^
        - ^^^First, ensure you are in your^^^ `~/project` ^^^directory.^^^
        - `cd`` ~/project`^^^ ^^^
        - ^^^Let's create a file that we will "upload" to the simulated remote user's home directory.^^^
        - `echo`` ``"This file will be uploaded via sftp."``(#98c379)`` > local_file.txt``(#a9b7c6)`^^^ ^^^
        - ^^^Now, initiate an^^^ `sftp` ^^^session to the^^^ `labex` ^^^user on^^^ `localhost`^^^.^^^
        - `sftp labex@localhost`^^^ ^^^
        - ^^^You will be prompted for the password for^^^ `labex@localhost`^^^. Enter^^^ `labex`^^^.^^^
        - ```
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ED25519 key fingerprint is SHA256:....
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'localhost' (ED25519) to the list of known hosts.
labex@localhost's password: labex
Connected to localhost.
sftp>
```^^^ ^^^
        - ^^^You are now in the^^^ `sftp` ^^^interactive prompt.^^^
        - ^^^Inside the^^^ `sftp` ^^^prompt, you can use various commands similar to a regular shell.^^^
            - `pwd`^^^: Shows the current working directory on the remote system.^^^
            - `lpwd`^^^: Shows the current working directory on your local system.^^^
            - `ls`^^^: Lists files on the remote system.^^^
            - `lls`^^^: Lists files on the local system.^^^
        - ^^^Let's try them:^^^
        - ```
sftp> 
``````
(#61aeee)
``````
pwd
``````
(#e6c07b)
Remote working directory: /home/labex

``````
sftp> 
``````
(#61aeee)lpwd
Local working directory: /home/labex/project

``````
sftp> 
``````
(#61aeee)
``````
ls
``````
(#e6c07b)
```^^^ ^^^
        - ^^^(The^^^ `ls``(#3594f7)` ^^^command will show the contents of^^^ `/home/labex``(#3594f7)` ^^^on the remote side, which is your own home directory.)^^^
        - ^^^Now, let's "upload"^^^ `local_file.txt` ^^^from your local^^^ `~/project` ^^^directory to the remote^^^ `labex` ^^^user's home directory (^^^`/home/labex`^^^). Use the^^^ `put` ^^^command.^^^
        - ```
sftp> put local_file.txt
Uploading local_file.txt to /home/labex/local_file.txt
local_file.txt                               100%   32     0.0KB/s   00:00
sftp>
```^^^ ^^^
        - ^^^You can verify that the file was uploaded by listing the remote directory:^^^
        - `sftp> ``(#61aeee)``(#1a1a1a)``ls``(#e6c07b)``(#1a1a1a)`^^^ ^^^
        - ^^^You should see^^^ `local_file.txt` ^^^listed among the files in^^^ `/home/labex`^^^.^^^
        - ^^^Next, let's "download" a file from the remote system. We will download the^^^ `.bashrc` ^^^file from the remote^^^ `labex` ^^^user's home directory to your local^^^ `~/project` ^^^directory. Use the^^^ `get` ^^^command.^^^
        - ```
sftp> 
``````
get
``````
(#c678dd) .bashrc

``````
Fetching
``````
(#d19a66) 
``````
/home/
``````
(#98c379)labex/.bashrc to .bashrc

``````
/home/
``````
(#98c379)labex
``````
/.bashrc                          100%  193     0.2KB/
``````
(#98c379)s   
``````
00
``````
(#d19a66):
``````
00
``````
(#d19a66)
sftp>
```^^^ ^^^
        - ^^^You can verify the download by listing your local directory:^^^
        - `sftp> ``(#61aeee)``(#1a1a1a)``lls``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^You should see^^^ `.bashrc` ^^^listed in your local^^^ `~/project` ^^^directory.^^^
        - ^^^To exit the^^^ `sftp` ^^^session, use the^^^ `exit` ^^^or^^^ `bye` ^^^command.^^^
        - `sftp> ``(#61aeee)``(#1a1a1a)``exit``(#e6c07b)``(#1a1a1a)`^^^ ^^^
        - ^^^You will return to your regular shell prompt.^^^
        - 
        - # ^^^**Synchronize Files Securely with rsync**^^^
        - ^^^In this step, you will learn how to synchronize files between systems using the^^^ `rsync` ^^^command.^^^ `rsync` ^^^is a powerful and versatile tool for copying and synchronizing files and directories, locally and remotely. Its key advantage is its ability to transfer only the differences between files, making it highly efficient for updates. Like^^^ `sftp`^^^,^^^ `rsync` ^^^can use SSH for secure, encrypted transfers.^^^
        - ^^^The most common options for^^^ `rsync` ^^^include:^^^
            - `-a` ^^^or^^^ `--archive`^^^: This is a combination of several options (^^^`-rlptgoD`^^^) that preserve most file attributes (recursive, links, permissions, times, group, owner, device files). It's often referred to as "archive mode" and is highly recommended for most synchronization tasks.^^^
            - `-v` ^^^or^^^ `--verbose`^^^: Increases verbosity, showing more details about the transfer.^^^
            - `-z` ^^^or^^^ `--compress`^^^: Compresses file data during the transfer, which can speed up transfers over slow links.^^^
            - `-h` ^^^or^^^ `--human-readable`^^^: Outputs numbers in a human-readable format.^^^
            - `-n` ^^^or^^^ `--dry-run`^^^: Performs a trial run without making any changes. This is extremely useful for verifying what^^^ `rsync` ^^^will do before actually executing the command.^^^
        - ^^^Let's start by ensuring you are in your^^^ `~/project` ^^^directory.^^^
        - `cd`` ~/project`^^^ ^^^
        - ^^^We will simulate a synchronization scenario by creating a source directory and a destination directory.^^^
        - ^^^Create a source directory^^^ `source_dir` ^^^with some files:^^^
        - ```
mkdir
``````
 source_dir

``````
echo
``````
 
``````
"Content of fileA"
``````
(#98c379) > source_dir/fileA.txt

``````
echo
``````
 
``````
"Content of fileB"
``````
(#98c379) > source_dir/fileB.txt

``````
mkdir
``````
 source_dir/subdir

``````
echo
``````
 
``````
"Content of subfile1"
``````
(#98c379) > source_dir/subdir/subfile1.txt
```^^^ ^^^
        - ^^^Create an empty destination directory^^^ `dest_dir`^^^:^^^
        - `mkdir`` dest_dir`^^^ ^^^
        - ^^^Now, let's perform a dry run to see what^^^ `rsync` ^^^would do when synchronizing^^^ `source_dir` ^^^to^^^ `dest_dir`^^^. We will use the^^^ `-avh` ^^^options for archive mode, verbose output, and human-readable sizes, along with^^^ `-n` ^^^for the dry run.^^^
        - `rsync -avhn source_dir/ dest_dir/`^^^ ^^^
        - ^^^**Important Note on Trailing Slashes:**^^^
            - `source_dir/`^^^: The trailing slash means "copy the^^^  ^^^ *contents* ^^^^^^ ^^^ ^^^of^^^ `source_dir`^^^".^^^
            - `source_dir`^^^: No trailing slash means "copy^^^ `source_dir` ^^^itself into the destination".^^^
        - ^^^The output of the dry run will show you the files that^^^  ^^^ *would be* ^^^^^^ ^^^ ^^^transferred:^^^
        - ```
sending incremental file list
./
fileA.txt
fileB.txt
subdir/
subdir/subfile1.txt

sent 186 bytes  received 12 bytes  396.00 bytes/sec
total size is 66  speedup is 0.33 (DRY RUN)
```^^^ ^^^
        - ^^^Notice the^^^ `(DRY RUN)``(#3594f7)` ^^^at the end, indicating no actual changes were made.^^^
        - ^^^Now, let's perform the actual synchronization. Remove the^^^ `-n` ^^^option.^^^
        - `rsync -avh source_dir/ dest_dir/`^^^ ^^^
        - ^^^The output will be similar to the dry run, but without the^^^ `(DRY RUN)``(#3594f7)` ^^^tag:^^^
        - ```
sending incremental file list
./
fileA.txt
fileB.txt
subdir/
subdir/subfile1.txt

sent 186 bytes  received 12 bytes  396.00 bytes/sec
total size is 66  speedup is 0.33
```^^^ ^^^
        - ^^^Verify that the files have been copied to^^^ `dest_dir`^^^:^^^
        - `ls`` -R dest_dir`^^^ ^^^
        - ^^^You should see:^^^
        - ```
dest_dir:
fileA.txt  fileB.txt  subdir

dest_dir/subdir:
subfile1.txt
```^^^ ^^^
        - ^^^Now, let's modify a file in^^^ `source_dir` ^^^and add a new file to see^^^ `rsync`^^^'s efficiency.^^^
        - ```
echo
``````
 
``````
"Updated content for fileA"
``````
(#98c379) > source_dir/fileA.txt

``````
echo
``````
 
``````
"New file content"
``````
(#98c379) > source_dir/new_file.txt
```^^^ ^^^
        - ^^^Perform another dry run to see what^^^ `rsync` ^^^will transfer this time:^^^
        - `rsync -avhn source_dir/ dest_dir/`^^^ ^^^
        - ^^^The output will show only the changed and new files:^^^
        - ```
sending incremental file list
./
fileA.txt
new_file.txt

sent 128 bytes  received 12 bytes  280.00 bytes/sec
total size is 100  speedup is 0.71 (DRY RUN)
```^^^ ^^^
        - ^^^This demonstrates^^^ `rsync`^^^'s ability to only transfer the differences.^^^
        - ^^^Now, perform the actual synchronization again:^^^
        - `rsync -avh source_dir/ dest_dir/`^^^ ^^^
        - ^^^Verify the contents of^^^ `dest_dir` ^^^again:^^^
        - ```
ls
``````
 -R dest_dir

``````
cat
``````
 dest_dir/fileA.txt

``````
cat
``````
 dest_dir/new_file.txt
```^^^ ^^^
        - ^^^You should see^^^ `new_file.txt` ^^^in^^^ `dest_dir` ^^^and^^^ `fileA.txt` ^^^should contain "Updated content for fileA".^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, we gained practical experience in managing and transferring files on RHEL systems using essential command-line tools. We began by mastering the^^^ `tar` ^^^utility, learning how to create, list, and extract files from archives, including the creation of compressed^^^ `tar.gz` ^^^archives for efficient storage and transfer.^^^
        - ^^^Subsequently, we explored secure file transfer methods. We utilized^^^ `sftp` ^^^for interactive and secure file transfers between systems, understanding its capabilities for uploading and downloading files. Finally, we delved into^^^ `rsync`^^^, a powerful tool for synchronizing files and directories, highlighting its efficiency in handling incremental updates and ensuring data consistency across different locations.^^^
    13. Install Software in Red Hat Enterprise Linux
        - Register Your System for Red Hat Support
        - Explore RPM Package Information
        - Install and Remove Software Packages with DNF
        - Manage DNF Software Repositories
        - View DNF Transaction History
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience managing software packages on Red Hat Enterprise Linux (RHEL) systems using DNF. You will begin by understanding the^^^ `subscription-manager``(#3594f7)` ^^^command for Red Hat support registration, even in a simulated environment. Subsequently, you will explore how to retrieve and interpret RPM package information, and then master the installation and removal of software packages using DNF.^^^
        - ^^^Furthermore, this lab will guide you through managing DNF software repositories, including adding, enabling, and disabling them. Finally, you will learn how to view and understand the DNF transaction history, providing a comprehensive overview of package management operations.^^^
        - > ^^^^^**Note**^^^^^^^^^^: This lab requires network connectivity to download packages and access repositories. It is only available to^^^^^ [^^^^^LabEx Pro^^^^^](https://labex.io/pricing) ^^^^^users.^^^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level lab with a^^^ ^^^92%^^^ ^^^completion rate. It has received a^^^ ^^^100%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Register Your System for Red Hat Support**^^^
        - ^^^In this step, you will learn how to register your system for Red Hat support using the^^^ `subscription-manager` ^^^command. While a full Red Hat subscription is not available in this simulated environment, understanding the^^^ `subscription-manager` ^^^command is crucial for managing software on Red Hat Enterprise Linux systems. This command allows you to register your system with Red Hat, attach subscriptions, and access Red Hat's content delivery network for software packages and updates.^^^
        - ^^^First, let's attempt to register the system using a placeholder username. This will demonstrate the command's usage, even though actual registration requires valid Red Hat credentials.^^^
        - `sudo subscription-manager register --username labex`^^^ ^^^
        - ^^^You will be prompted for a password. Since this is a simulated environment, you can enter any password, or simply press^^^ `Enter` ^^^if the system allows it. The command will likely fail to connect to Red Hat's subscription service, which is expected in this lab environment. The important part is to understand the command's syntax and its intended use.^^^
        - ```
Registering to: subscription.rhsm.redhat.com:443/subscription
Password:
Invalid username or password. To create a login, please visit https://www.redhat.com/wapps/ugc/register.html (HTTP error code 401: Unauthorized)
```^^^ ^^^
        - ^^^Finally, let's see how to view consumed subscriptions. This command shows which subscriptions are currently attached to your system.^^^
        - `sudo subscription-manager list --consumed`^^^ ^^^
        - ^^^Since the system is not registered, you will see a message indicating no consumed subscriptions.^^^
        - `No consumed subscription pools were found.`^^^ ^^^
        - ^^^Next, let's explore how you would typically list available subscriptions for your Red Hat account. This command would show you the various subscription pools associated with your Red Hat account.^^^
        - `sudo subscription-manager list --available`^^^ ^^^
        - ^^^Since the system is not yet registered, you will see an error message indicating that registration is required first.^^^
        - `This system is not yet registered. Try 'subscription-manager register --help' for more information.`^^^ ^^^
        - ^^^This exercise demonstrates the basic usage of^^^ `subscription-manager` ^^^for registration and viewing subscription information. While full functionality is limited in this simulated environment, these commands are fundamental for managing software access on RHEL systems.^^^
        - 
        - # ^^^**Explore RPM Package Information**^^^
        - ^^^In this step, you will learn how to use the^^^ `rpm` ^^^command to investigate software packages. RPM (Red Hat Package Manager) is the core package management system used by Red Hat Enterprise Linux. While^^^ `dnf` ^^^(which you'll explore later) is a higher-level tool for managing packages from repositories,^^^ `rpm` ^^^allows you to query, verify, install, and uninstall individual^^^ `.rpm` ^^^files.^^^
        - ^^^First, let's list all installed RPM packages on your system. This can generate a very long list, so we'll pipe the output to^^^ `head` ^^^to see just the beginning.^^^
        - `rpm -qa | ``head`^^^ ^^^
        - ^^^You will see a list of package names, versions, and architectures. For example:^^^
        - ```
libgcc-11.4.1-3.el9.x86_64
crypto-policies-20240202-1.git283706d.el9.noarch
tzdata-2024a-1.el9.noarch
subscription-manager-rhsm-certificates-20220623-1.el9.noarch
redhat-release-9.4-0.4.el9.x86_64
setup-2.13.7-10.el9.noarch
filesystem-3.16-2.el9.x86_64
basesystem-11-13.el9.noarch
pcre2-syntax-10.40-5.el9.noarch
ncurses-base-6.2-10.20210508.el9.noarch
```^^^ ^^^
        - ^^^Next, let's find out which package provides a specific file. We'll use^^^ `/etc/yum.repos.d` ^^^as an example, which is a directory containing DNF repository configuration files.^^^
        - `rpm -qf /etc/yum.repos.d`^^^ ^^^
        - ^^^The output will show you the package that owns this directory.^^^
        - `redhat-release-9.4-0.4.el9.x86_64`^^^ ^^^
        - ^^^Now, let's get detailed information about an installed package. We'll use the^^^ `dnf` ^^^package itself as an example.^^^
        - `rpm -qi dnf`^^^ ^^^
        - ^^^This command provides a wealth of information, including the package name, version, release, architecture, size, summary, URL, license, and a detailed description.^^^
        - ```
Name        : dnf
Version     : 4.14.0
Release     : 9.el9
Architecture: noarch
Install Date: Thu Jul 18 15:50:10 2024
Group       : Unspecified
Size        : 2425281
License     : GPLv2+
Signature   : RSA/SHA256, Fri Nov 10 10:14:09 2023, Key ID 199e2f91fd431d51
Source RPM  : dnf-4.14.0-9.el9.src.rpm
Build Date  : Thu Oct 26 05:20:14 2023
Build Host  : x86-64-01.build.eng.rdu2.redhat.com
Packager    : Red Hat, Inc. <http://bugzilla.redhat.com/bugzilla>
Vendor      : Red Hat, Inc.
URL         : https://github.com/rpm-software-management/dnf
Summary     : Package manager
Description :
Utility that allows users to manage packages on their systems.
It supports RPMs, modules and comps groups & environments.
```^^^ ^^^
        - ^^^You can also list all files installed by a package. This can be useful for understanding what a package places on your system.^^^
        - `rpm -ql dnf | ``head`` -n 10`^^^ ^^^
        - ^^^This will show the first 10 files installed by the^^^ `dnf` ^^^package.^^^
        - ```
/usr/bin/dnf
/usr/lib/systemd/system/dnf-makecache.service
/usr/lib/systemd/system/dnf-makecache.timer
/usr/share/bash-completion
/usr/share/bash-completion/completions
/usr/share/bash-completion/completions/dnf
/usr/share/locale/ar/LC_MESSAGES/dnf.mo
/usr/share/locale/bg/LC_MESSAGES/dnf.mo
/usr/share/locale/bn/LC_MESSAGES/dnf.mo
/usr/share/locale/bn_IN/LC_MESSAGES/dnf.mo
```^^^ ^^^
        - ^^^To see only the configuration files installed by a package, use the^^^ `-qc` ^^^option. Let's check the^^^ `openssh-clients` ^^^package.^^^
        - `rpm -qc openssh-clients`^^^ ^^^
        - ^^^This will list configuration files related to SSH clients.^^^
        - ```
/etc/ssh/ssh_config
/etc/ssh/ssh_config.d/50-redhat.conf
```^^^ ^^^
        - ^^^Finally, to view the change log information for a package, use^^^ `--changelog`^^^. This can provide insights into the history of updates and fixes for a package. Let's look at the^^^ `audit` ^^^package.^^^
        - `rpm -q --changelog audit | ``head`` -n 5`^^^ ^^^
        - ^^^If the package is not installed, you will see an error message:^^^
        - `package audit is not installed`^^^ ^^^
        - ^^^You can try with an installed package instead. For example, with the^^^ `setup` ^^^package:^^^
        - `rpm -q --changelog setup | ``head`` -n 5`^^^ ^^^
        - ^^^These^^^ `rpm` ^^^commands are powerful tools for understanding the packages installed on your system and the files they contain.^^^
        - 
        - # ^^^**Install and Remove Software Packages with DNF**^^^
        - ^^^In this step, you will learn how to use^^^ `dnf` ^^^(Dandified YUM) to manage software packages.^^^ `dnf` ^^^is the default package manager in Red Hat Enterprise Linux 9 and is used for installing, updating, and removing software packages, as well as managing software repositories. It automatically handles dependencies, making software management much easier than with^^^ `rpm` ^^^alone.^^^
        - ^^^First, let's list all available and installed packages that have "http" in their name. This will give you an idea of what packages are related to HTTP services.^^^
        - `dnf list ``'http*'``(#98c379)`^^^ ^^^
        - ^^^You will see a list of packages, indicating whether they are installed or available for installation.^^^
        - ```
Last metadata expiration check: 0:00:00 ago on Mon Apr 22 08:00:00 2024.
Available Packages
http-parser.i686               2.9.4-6.el9    rhel-9-for-x86_64-appstream-rpms
http-parser.x86_64             2.9.4-6.el9    rhel-9-for-x86_64-appstream-rpms
httpcomponents-client.noarch   4.5.13-2.el9   rhel-9-for-x86_64-appstream-rpms
httpcomponents-core.noarch     4.4.13-6.el9   rhel-9-for-x86_64-appstream-rpms
httpd.x86_64                   2.4.51-5.el9   rhel-9-for-x86_64-appstream-rpms
httpd-devel.x86_64             2.4.51-5.el9   rhel-9-for-x86_64-appstream-rpms
httpd-filesystem.noarch        2.4.51-5.el9   rhel-9-for-x86_64-appstream-rpms
httpd-manual.noarch            2.4.51-5.el9   rhel-9-for-x86_64-appstream-rpms
httpd-tools.x86_64             2.4.51-5.el9   rhel-9-for-x86_64-appstream-rpms
```^^^ ^^^
        - ^^^Now, let's search for packages that contain "web server" in their name, summary, or description. The^^^ `search all` ^^^option is useful for a broader search.^^^
        - `dnf search all ``'web server'``(#98c379)`^^^ ^^^
        - ^^^This command will return a list of packages that match the search terms.^^^
        - ```
Last metadata expiration check: 0:00:00 ago on Mon Apr 22 08:00:00 2024.
================== Summary & Description Matched: web server ===================
nginx.x86_64 : A high performance web server and reverse proxy server
pcp-pmda-weblog.x86_64 : Performance Co-Pilot (PCP) metrics from web server logs
========================= Summary Matched: web server ==========================
libcurl.x86_64 : A library for getting files from web servers
libcurl.i686 : A library for getting files from web servers
======================= Description Matched: web server ========================
freeradius.x86_64 : High-performance and highly configurable free RADIUS server
git-instaweb.noarch : Repository browser in gitweb
http-parser.i686 : HTTP request/response parser for C
http-parser.x86_64 : HTTP request/response parser for C
httpd.x86_64 : Apache HTTP Server
mod_auth_openidc.x86_64 : OpenID Connect auth module for Apache HTTP Server
mod_jk.x86_64 : Tomcat mod_jk connector for Apache
mod_security.x86_64 : Security module for the Apache HTTP Server
varnish.i686 : High-performance HTTP accelerator
varnish.x86_64 : High-performance HTTP accelerator
```^^^ ^^^
        - ^^^Let's get detailed information about the^^^ `httpd` ^^^package, which is the Apache HTTP Server.^^^
        - `dnf info httpd`^^^ ^^^
        - ^^^This will display comprehensive details about the package, including its size, license, and description.^^^
        - ```
Last metadata expiration check: 0:00:00 ago on Mon Apr 22 08:00:00 2024.
Available Packages
Name         : httpd
Version      : 2.4.51
Release      : 5.el9
Architecture : x86_64
Size         : 1.5 M
Source       : httpd-2.4.51-5.el9.src.rpm
Repository   : rhel-9-for-x86_64-appstream-rpms
Summary      : Apache HTTP Server
URL          : https://httpd.apache.org/
License      : ASL 2.0
Description  : The Apache HTTP Server is a powerful, efficient, and extensible
             : web server.
```^^^ ^^^
        - ^^^Now, let's install the^^^ `httpd` ^^^package. You will need^^^ `sudo` ^^^privileges for this operation.^^^
        - `sudo dnf install httpd -y`^^^ ^^^
        - ^^^The^^^ `-y` ^^^flag automatically answers "yes" to any prompts, which is useful for scripting but use with caution in production environments.^^^
        - ```
Last metadata expiration check: 0:00:00 ago on Mon Apr 22 08:00:00 2024.
Dependencies resolved.
================================================================================
 Package                Architecture  Version           Repository         Size
================================================================================
Installing:
 httpd                  x86_64        2.4.51-5.el9      rhel-9-for-x86_64-appstream-rpms
                                                                          1.5 M
Installing dependencies:
 apr                    x86_64        1.7.0-11.el9      rhel-9-for-x86_64-appstream-rpms
                                                                          126 k
 apr-util               x86_64        1.6.1-20.el9      rhel-9-for-x86_64-appstream-rpms
                                                                          106 k
 apr-util-bdb           x86_64        1.6.1-20.el9      rhel-9-for-x86_64-appstream-rpms
                                                                           13 k
 apr-util-openssl       x86_64        1.6.1-20.el9      rhel-9-for-x86_64-appstream-rpms
                                                                           15 k
 httpd-filesystem       noarch        2.4.51-5.el9      rhel-9-for-x86_64-appstream-rpms
                                                                           14 k
 httpd-tools            x86_64        2.4.51-5.el9      rhel-9-for-x86_64-appstream-rpms
                                                                          100 k
 mailcap                noarch        2.1.49-5.el9      rhel-9-for-x86_64-baseos-rpms
                                                                           36 k
 mod_http2              x86_64        1.15.7-5.el9      rhel-9-for-x86_64-appstream-rpms
                                                                          150 k
 redhat-logos-httpd     noarch        90.4-1.el9        rhel-9-for-x86_64-appstream-rpms
                                                                           20 k

Transaction Summary
================================================================================
Install  10 Packages

Total download size: 2.1 M
Installed size: 6.9 M
Downloading Packages:
... (downloading package details omitted) ...
Running transaction
... (installation progress omitted) ...

Installed:
  apr-1.7.0-11.el9.x86_64
  apr-util-1.6.1-20.el9.x86_64
  apr-util-bdb-1.6.1-20.el9.x86_64
  apr-util-openssl-1.6.1-20.el9.x86_64
  httpd-2.4.51-5.el9.x86_64
  httpd-filesystem-2.4.51-5.el9.noarch
  httpd-tools-2.4.51-5.el9.x86_64
  mailcap-2.1.49-5.el9.noarch
  mod_http2-1.15.7-5.el9.x86_64
  redhat-logos-httpd-90.4-1.el9.noarch

Complete!
```^^^ ^^^
        - ^^^You can verify that^^^ `httpd` ^^^is installed by querying^^^ `rpm`^^^:^^^
        - `rpm -q httpd`^^^ ^^^
        - `httpd-2.4.51-5.el9.x86_64`^^^ ^^^
        - ^^^Now, let's remove the^^^ `httpd` ^^^package.^^^
        - `sudo dnf remove httpd -y`^^^ ^^^
        - ^^^This will remove the^^^ `httpd` ^^^package and any dependencies that are no longer needed by other installed packages.^^^
        - ```
Dependencies resolved.
================================================================================
 Package                Architecture  Version           Repository         Size
================================================================================
Removing:
 httpd                  x86_64        2.4.51-5.el9      @appstream        4.7 M
Removing dependent packages:
 apr-util-bdb           x86_64        1.6.1-20.el9      @appstream         13 k
 apr-util-openssl       x86_64        1.6.1-20.el9      @appstream         15 k
 httpd-filesystem       noarch        2.4.51-5.el9      @appstream         14 k
 mod_http2              x86_64        1.15.7-5.el9      @appstream        150 k
 redhat-logos-httpd     noarch        90.4-1.el9        @appstream         20 k

Transaction Summary
================================================================================
Remove  6 Packages

Freed space: 4.9 M
... (transaction progress omitted) ...

Removed:
  apr-util-bdb-1.6.1-20.el9.x86_64
  apr-util-openssl-1.6.1-20.el9.x86_64
  httpd-2.4.51-5.el9.x86_64
  httpd-filesystem-2.4.51-5.el9.noarch
  mod_http2-1.15.7-5.el9.x86_64
  redhat-logos-httpd-90.4-1.el9.noarch

Complete!
```^^^ ^^^
        - ^^^You can confirm its removal:^^^
        - `rpm -q httpd`^^^ ^^^
        - `package httpd is not installed`^^^ ^^^
        - ^^^This demonstrates the basic^^^ `dnf` ^^^commands for installing and removing software packages.^^^
        - 
        - # ^^^**Manage DNF Software Repositories**^^^
        - ^^^In this step, you will learn how to manage DNF software repositories. Repositories are locations where software packages are stored and from which^^^ `dnf` ^^^retrieves them. Understanding how to list, enable, disable, and add repositories is crucial for controlling what software is available on your system.^^^
        - ^^^First, let's list all configured DNF repositories and their status (enabled or disabled).^^^
        - `dnf repolist all`^^^ ^^^
        - ^^^You will see a list of repository IDs, names, and their current status.^^^
        - ```
Not root, Subscription Management repositories not updated
repo id                                                                                                                  repo name                                                                                                                                               status
ubi-9-appstream-debug-rpms                                                                                               Red Hat Universal Base Image 9 (Debug RPMs) - AppStream                                                                                                 disabled
ubi-9-appstream-rpms                                                                                                     Red Hat Universal Base Image 9 (RPMs) - AppStream                                                                                                       enabled
ubi-9-appstream-source                                                                                                   Red Hat Universal Base Image 9 (Source RPMs) - AppStream                                                                                                disabled
ubi-9-baseos-debug-rpms                                                                                                  Red Hat Universal Base Image 9 (Debug RPMs) - BaseOS                                                                                                    disabled
ubi-9-baseos-rpms                                                                                                        Red Hat Universal Base Image 9 (RPMs) - BaseOS                                                                                                          enabled
ubi-9-baseos-source                                                                                                      Red Hat Universal Base Image 9 (Source RPMs) - BaseOS                                                                                                   disabled
ubi-9-codeready-builder                                                                                                  Red Hat Universal Base Image 9 (RPMs) - CodeReady Builder                                                                                               enabled
ubi-9-codeready-builder-debug-rpms                                                                                       Red Hat Universal Base Image 9 (Debug RPMs) - CodeReady Builder                                                                                         disabled
ubi-9-codeready-builder-rpms                                                                                             Red Hat Universal Base Image 9 (RPMs) - CodeReady Builder                                                                                               disabled
ubi-9-codeready-builder-source                                                                                           Red Hat Universal Base Image 9 (Source RPMs) - CodeReady Builder                                                                                        disabled
```^^^ ^^^
        - ^^^The^^^ `dnf config-manager` ^^^command is a powerful tool for managing repository configurations. You can use it to enable or disable repositories. For example, let's try to enable a hypothetical debug repository. While this specific repository might not exist or be accessible in this lab environment, the command demonstrates the syntax.^^^
        - `sudo dnf config-manager --``enable`` rhel-9-server-debug-rpms`^^^ ^^^
        - ^^^You will see messages about subscription management and an error indicating that the repository is not found, which is expected in this environment.^^^
        - ```
Updating Subscription Management repositories.
Unable to read consumer identity

This system is not registered with an entitlement server. You can use subscription-manager to register.

Error: No matching repo to modify: rhel-9-server-debug-rpms.
```^^^ ^^^
        - ^^^Now, let's try to disable a repository. We'll use^^^ `rhel-9-for-x86_64-appstream-rpms` ^^^as an example.^^^ ^^^**Note: This specific repository name doesn't exist in this UBI environment, but the command demonstrates the syntax.**^^^
        - `sudo dnf config-manager --``disable`` rhel-9-for-x86_64-appstream-rpms`^^^ ^^^
        - ^^^You will see subscription management messages and an error indicating the repository doesn't exist in this environment.^^^
        - ```
Updating Subscription Management repositories.
Unable to read consumer identity

This system is not registered with an entitlement server. You can use subscription-manager to register.

Error: No matching repo to modify: rhel-9-for-x86_64-appstream-rpms.
```^^^ ^^^
        - ^^^Let's verify that this repository name doesn't exist in the current system:^^^
        - `dnf repolist all | grep rhel-9-for-x86_64-appstream-rpms`^^^ ^^^
        - ^^^As expected, there will be no output since this repository doesn't exist in the UBI environment.^^^
        - `(no output)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^Let's try the same enable command to confirm the repository doesn't exist:^^^
        - `sudo dnf config-manager --``enable`` rhel-9-for-x86_64-appstream-rpms`^^^ ^^^
        - ^^^Again, you'll see the same error message:^^^
        - ```
Updating Subscription Management repositories.
Unable to read consumer identity

This system is not registered with an entitlement server. You can use subscription-manager to register.

Error: No matching repo to modify: rhel-9-for-x86_64-appstream-rpms.
```^^^ ^^^
        - ^^^The^^^ `dnf config-manager --add-repo` ^^^command can also be used to add new repositories by specifying a URL. For demonstration purposes, we will attempt to add a common EPEL (Extra Packages for Enterprise Linux) repository URL. While this might not fully configure the repository (as it often requires a GPG key and a specific^^^ `.repo` ^^^file), it shows the command's capability.^^^
        - `sudo dnf config-manager --add-repo=``"https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/"``(#98c379)`^^^ ^^^
        - ^^^You will see output indicating that a new^^^ `.repo` ^^^file has been created.^^^
        - ```
Updating Subscription Management repositories.
Unable to read consumer identity

This system is not registered with an entitlement server. You can use subscription-manager to register.

Adding repo from: https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/
```^^^ ^^^
        - ^^^You can inspect the newly created^^^ `.repo` ^^^file in^^^ `/etc/yum.repos.d/`^^^. The name of the file will be derived from the URL.^^^
        - `ls`` /etc/yum.repos.d/`^^^ ^^^
        - ^^^You should see a file like^^^ `dl.fedoraproject.org_pub_epel_9_Everything_x86_64_.repo` ^^^along with the existing repository files.^^^
        - `dl.fedoraproject.org_pub_epel_9_Everything_x86_64_.repo  redhat.repo  ubi.repo`^^^ ^^^
        - ^^^Finally, let's remove the repository configuration file we just added to clean up.^^^
        - `sudo ``rm`` /etc/yum.repos.d/dl.fedoraproject.org_pub_epel_9_Everything_x86_64_.repo`^^^ ^^^
        - ^^^This step has shown you how to list, enable, disable, and add DNF repositories, which are essential skills for managing software sources on RHEL.^^^
        - 
        - # ^^^**View DNF Transaction History**^^^
        - ^^^In this step, you will learn how to view the transaction history of DNF operations.^^^ `dnf` ^^^keeps a detailed log of all package installations, removals, and updates. This history is invaluable for troubleshooting, auditing, and even reverting changes if necessary.^^^
        - ^^^First, let's view the summary of all DNF transactions that have occurred on your system.^^^
        - `sudo dnf ``history`^^^ ^^^
        - ^^^You will see a table listing each transaction with an ID, the command line used, the date and time, the action(s) performed, and the number of packages altered.^^^
        - ```
ID     | Command line              | Date and time    | Action(s)      | Altered
--------------------------------------------------------------------------------
     3 | install httpd             | 2024-04-22 08:00 | Install        |   10
     2 | remove httpd              | 2024-04-22 08:01 | Remove         |    6
     1 |                           | 2024-04-22 07:50 | Install        |  767 EE
```^^^ ^^^
        - ^^^The^^^ `ID` ^^^column is particularly important, as it allows you to refer to specific transactions. For example, if you want to see detailed information about a specific transaction, you can use^^^ `dnf history info <ID>`^^^. Let's look at the details of the last transaction (which should be the^^^ `httpd` ^^^removal from the previous step). You can find the ID from the^^^ `dnf history` ^^^output. In the example above, it's^^^ `2`^^^.^^^
        - `sudo dnf ``history`` info 2`^^^ ^^^
        - ^^^This command provides a comprehensive breakdown of the selected transaction, including the packages that were removed, their versions, and the reason for the action.^^^
        - ```
Transaction ID : 2
Begin time     : Mon Apr 22 08:01:00 2024
Begin rpmdb    : 777:a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3
End time       : Mon Apr 22 08:01:05 2024 (5 seconds)
End rpmdb      : 771:a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y6z7a8b9c0d1e2f3
User           : labex <labex>
Return Code    : Success
Command Line   : dnf remove httpd -y
Packages Altered:
    Removed apr-util-bdb-1.6.1-20.el9.x86_64
    Removed apr-util-openssl-1.6.1-20.el9.x86_64
    Removed httpd-2.4.51-5.el9.x86_64
    Removed httpd-filesystem-2.4.51-5.el9.noarch
    Removed mod_http2-1.15.7-5.el9.x86_64
    Removed redhat-logos-httpd-90.4-1.el9.noarch
```^^^ ^^^
        - ^^^One of the most powerful features of DNF history is the ability to undo or redo transactions. For example, to undo the^^^ `httpd` ^^^removal, you would use^^^ `dnf history undo <ID>`^^^. Let's undo the^^^ `httpd` ^^^removal transaction (using the ID from your^^^ `dnf history` ^^^output, e.g.,^^^ `2`^^^).^^^
        - `sudo dnf ``history`` undo 2 -y`^^^ ^^^
        - ^^^This command will reinstall the^^^ `httpd` ^^^package and its dependencies that were removed in that specific transaction.^^^
        - ```
Last metadata expiration check: 0:00:00 ago on Mon Apr 22 08:00:00 2024.
Undoing transaction 2, from Mon Apr 22 08:01:00 2024
    Removed apr-util-bdb-1.6.1-20.el9.x86_64
    Removed apr-util-openssl-1.6.1-20.el9.x86_64
    Removed httpd-2.4.51-5.el9.x86_64
    Removed httpd-filesystem-2.4.51-5.el9.noarch
    Removed mod_http2-1.15.7-5.el9.x86_64
    Removed redhat-logos-httpd-90.4-1.el9.noarch
Dependencies resolved.
================================================================================
 Package                Architecture  Version           Repository         Size
================================================================================
Installing:
 httpd                  x86_64        2.4.51-5.el9      ubi-9-appstream-rpms  1.5 M
Installing dependencies:
 apr                    x86_64        1.7.0-11.el9      ubi-9-appstream-rpms  126 k
 apr-util               x86_64        1.6.1-20.el9      ubi-9-appstream-rpms  106 k
 apr-util-bdb           x86_64        1.6.1-20.el9      ubi-9-appstream-rpms   13 k
 apr-util-openssl       x86_64        1.6.1-20.el9      ubi-9-appstream-rpms   15 k
 httpd-filesystem       noarch        2.4.51-5.el9      ubi-9-appstream-rpms   14 k
 httpd-tools            x86_64        2.4.51-5.el9      ubi-9-appstream-rpms  100 k
 mailcap                noarch        2.1.49-5.el9      ubi-9-baseos-rpms      36 k
 mod_http2              x86_64        1.15.7-5.el9      ubi-9-appstream-rpms  150 k
 redhat-logos-httpd     noarch        90.4-1.el9        ubi-9-appstream-rpms   20 k

Transaction Summary
================================================================================
Install  10 Packages

Total download size: 2.1 M
Installed size: 6.9 M
... (installation progress omitted) ...
Complete!
```^^^ ^^^
        - ^^^You can verify that^^^ `httpd` ^^^is now installed again:^^^
        - `rpm -q httpd`^^^ ^^^
        - `httpd-2.4.51-5.el9.x86_64`^^^ ^^^
        - ^^^Finally, let's remove^^^ `httpd` ^^^again to leave the system in a clean state for future labs.^^^
        - `sudo dnf remove httpd -y`^^^ ^^^
        - ```
... (output omitted) ...
Complete!
```^^^ ^^^
        - ^^^This step has demonstrated how to use^^^ `dnf history` ^^^to view, inspect, and even revert DNF transactions, providing powerful capabilities for system management.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, we learned essential skills for managing software packages on Red Hat Enterprise Linux using DNF. We began by understanding the^^^ `subscription-manager` ^^^command, crucial for registering systems with Red Hat and accessing their content delivery network, even though full registration wasn't possible in the simulated environment.^^^
        - ^^^Subsequently, we explored how to query RPM package information, install and remove software using DNF, manage DNF software repositories, and view the DNF transaction history. These steps provided a comprehensive overview of DNF's capabilities for efficient software management.^^^
    14. Access File Systems in Red Hat Enterprise Linux
        - Identify File Systems and Block Devices
        - Examine File System Usage with df and du
        - Manually Mount and Unmount File Systems
        - Locate Files by Name with locate and find
        - Find Files by Ownership, Permissions, Size, and Time
        - Search for Files Based on File Type
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience managing Linux file systems on a Red Hat Enterprise Linux (RHEL) system. You will learn to identify file systems and block devices, examine disk usage using^^^ `df``(#3594f7)` ^^^and^^^ `du``(#3594f7)`^^^, and practice manually mounting and unmounting file systems.^^^
        - ^^^Furthermore, this lab will guide you through locating files efficiently using commands like^^^ `locate` ^^^and^^^ `find`^^^, enabling you to search for files based on various criteria such as name, ownership, permissions, size, time, and file type.^^^
        - 
        - # ^^^**Identify File Systems and Block Devices**^^^
        - ^^^In this step, you will learn how to identify file systems and block devices on a Red Hat Enterprise Linux system. Understanding how storage is organized is fundamental for system administration. We will explore various commands to list and examine block devices and their associated file systems.^^^
        - ^^^First, let's understand some core concepts:^^^
            - ^^^**Block Device**^^^^^^: A block device is a file that provides low-level access to storage devices. Examples include hard drives, SSDs, and USB drives. In Linux, these are typically found in the^^^ `/dev` ^^^directory.^^^
            - ^^^**Partition**^^^^^^: A partition is a logical division of a physical storage device. A single hard drive can have multiple partitions, each formatted with a different file system or used for different purposes.^^^
            - ^^^**File System**^^^^^^: A file system is a method and data structure that an operating system uses to control how data is stored and retrieved. It organizes data into files and directories. Common Linux file systems include XFS and ext4.^^^
            - ^^^**Mount Point**^^^^^^: A mount point is an empty directory in the file system hierarchy where a file system is attached or "mounted" to make its contents accessible.^^^
        - ^^^Let's start by listing the block devices available on your system using the^^^ `lsblk` ^^^command. This command provides a tree-like overview of all block devices and their partitions.^^^
        - `lsblk`^^^ ^^^
        - ^^^You should see output similar to this, showing devices like^^^ `vda`^^^,^^^ `vdb`^^^, etc., which represent virtual disk devices in your container environment:^^^
        - ```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
vda    253:0    0   40G  0 disk
├─vda1 253:1    0    1M  0 part
├─vda2 253:2    0  100M  0 part /boot/efi
└─vda3 253:3    0 39.9G  0 part /
vdb    253:16   0   40G  0 disk
```^^^ ^^^
        - ^^^In the output:^^^
            - `NAME`^^^: The name of the block device (e.g.,^^^ `vda`^^^,^^^ `vdb`^^^) or partition (e.g.,^^^ `vda1`^^^,^^^ `vda2`^^^).^^^
            - `MAJ:MIN`^^^: Major and minor device numbers.^^^
            - `RM`^^^: Removable device (1 if removable, 0 if not).^^^
            - `SIZE`^^^: The size of the device or partition.^^^
            - `RO`^^^: Read-only (1 if read-only, 0 if not).^^^
            - `TYPE`^^^: Type of the device (e.g.,^^^ `disk`^^^,^^^ `part` ^^^for partition).^^^
            - `MOUNTPOINTS`^^^: Where the device or partition is currently mounted.^^^
        - ^^^Next, let's examine the file systems and their usage with the^^^ `df` ^^^command. The^^^ `df` ^^^command reports file system disk space usage.^^^
        - `df`^^^ ^^^
        - ^^^The output will show various file systems, their total size, used space, available space, and mount points:^^^
        - ```
Filesystem     1K-blocks    Used Available Use% Mounted on
devtmpfs            4096       0      4096   0% /dev
tmpfs            1822216       0   1822216   0% /dev/shm
tmpfs             728888     616    728272   1% /run
efivarfs             256       9       243   4% /sys/firmware/efi/efivars
/dev/vda3       41773036 3628732  38144304   9% /
/dev/vda2         102156    7198     94958   8% /boot/efi
tmpfs             364440       0    364440   0% /run/user/1000
```^^^ ^^^
        - ^^^To make the output more readable, especially for sizes, you can use the^^^ `-h` ^^^option for human-readable format (e.g., M for MiB, G for GiB).^^^
        - `df`` -h`^^^ ^^^
        - ^^^You will see sizes in a more understandable format:^^^
        - ```
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        4.0M     0  4.0M   0% /dev
tmpfs           1.8G     0  1.8G   0% /dev/shm
tmpfs           712M  616K  712M   1% /run
efivarfs        256K  8.5K  243K   4% /sys/firmware/efi/efivars
/dev/vda3        40G  3.5G   37G   9% /
/dev/vda2       100M  7.1M   93M   8% /boot/efi
tmpfs           356M     0  356M   0% /run/user/1000
```^^^ ^^^
        - ^^^Finally, let's use the^^^ `lsblk -fp` ^^^command to list the full path of devices, their UUIDs (Universally Unique Identifiers), and file system types. UUIDs are stable identifiers that remain the same even if device names change, making them useful for consistent mounting.^^^
        - `lsblk -fp`^^^ ^^^
        - ^^^The output will include UUIDs and file system types:^^^
        - ```
NAME        FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
/dev/vda
├─/dev/vda1
├─/dev/vda2 vfat   FAT16       E52E-0564                              92.7M     7% /boot/efi
└─/dev/vda3 xfs          root  4c234c8b-4f67-4d65-abb5-06753b1ec236   36.4G     9% /
/dev/vdb
```^^^ ^^^
        - ^^^Notice the^^^ `UUID` ^^^column, which provides a unique identifier for each file system. This is crucial for reliably mounting file systems, especially in configuration files like^^^ `/etc/fstab`^^^.^^^
        - 
        - # ^^^**Examine File System Usage with df and du**^^^
        - ^^^In this step, you will delve deeper into examining file system usage using the^^^ `df` ^^^and^^^ `du` ^^^commands. While^^^ `df` ^^^provides an overview of disk space usage for mounted file systems,^^^ `du` ^^^(disk usage) is used to estimate file space usage for specific files or directories. Understanding the difference and when to use each command is crucial for effective disk space management.^^^
        - ^^^Let's start by revisiting the^^^ `df` ^^^command with its human-readable option. This command is excellent for getting a quick summary of how much space is used and available on all mounted file systems.^^^
        - `df`` -h`^^^ ^^^
        - ^^^The output will show the disk usage in an easy-to-read format (e.g., G for gigabytes, M for megabytes):^^^
        - ```
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        892M     0  892M   0% /dev
tmpfs           915M     0  915M   0% /dev/shm
tmpfs           915M   17M  899M   2% /run
tmpfs           915M     0  915M   0% /sys/fs/cgroup
/dev/vda4       8.0G  1.4G  6.7G  17% /
/dev/vda3      1014M  166M  849M  17% /boot
tmpfs           183M     0  183M   0% /run/user/1000
```^^^ ^^^
        - ^^^Now, let's explore the^^^ `du` ^^^command. Unlike^^^ `df`^^^,^^^ `du` ^^^calculates the disk space used by files and directories within a specified path. This is particularly useful when you want to find out which directories or files are consuming the most space.^^^
        - ^^^To see the disk usage of your current directory (^^^`~/project``(#3594f7)`^^^), use^^^ `du``(#3594f7)` ^^^without any arguments. This will list the size of every file and subdirectory within^^^ `~/project``(#3594f7)`^^^.^^^
        - `du`^^^ ^^^
        - ^^^The output might be extensive, showing sizes in kilobytes by default:^^^
        - ```
4       ./.config/xfce4/xfconf/xfce-perchannel-xml
8       ./.config/xfce4/xfconf
12      ./.config/xfce4
16      ./.config
4       ./.local/share/nano
8       ./.local/share
12      ./.local
28      .
```^^^ ^^^
        - ^^^To make the output more readable, similar to^^^ `df -h`^^^, you can use the^^^ `-h` ^^^option with^^^ `du`^^^.^^^
        - `du`` -h`^^^ ^^^
        - ^^^This will display the sizes in human-readable units:^^^
        - ```
4.0K    ./.config/xfce4/xfconf/xfce-perchannel-xml
8.0K    ./.config/xfce4/xfconf
12K     ./.config/xfce4
16K     ./.config
4.0K    ./.local/share/nano
8.0K    ./.local/share
12K     ./.local
28K     .
```^^^ ^^^
        - ^^^Often, you are interested in the total size of a directory rather than the size of each individual file and subdirectory. For this, you can use the^^^ `-s` ^^^(summary) option along with^^^ `-h`^^^. Let's check the total size of your home directory (^^^`~`^^^).^^^
        - `du`` -sh ~`^^^ ^^^
        - ^^^This command will output the total size of your home directory:^^^
        - `48K     /home/labex`^^^ ^^^
        - ^^^Let's create some files to see how^^^ `du` ^^^reports their sizes. We will create a directory named^^^ `test_data` ^^^and then create a few files inside it.^^^
        - ^^^First, create the directory:^^^
        - `mkdir`` ~/project/test_data`^^^ ^^^
        - ^^^Now, navigate into the^^^ `test_data` ^^^directory:^^^
        - `cd`` ~/project/test_data`^^^ ^^^
        - ^^^Next, create a few files with some content. We'll use the^^^ `head` ^^^command to generate files of specific sizes.^^^
        - ```
head
``````
 -c 1K < /dev/urandom > file1.txt

``````
head
``````
 -c 5K < /dev/urandom > file2.txt

``````
head
``````
 -c 10K < /dev/urandom > file3.txt
```^^^ ^^^
        - ^^^Now, use^^^ `du -h` ^^^to see the sizes of these new files and the^^^ `test_data` ^^^directory.^^^
        - `du`` -h`^^^ ^^^
        - ^^^You should see output similar to this:^^^
        - ```
1.0K    ./file1.txt
5.0K    ./file2.txt
10K     ./file3.txt
24K     .
```^^^ ^^^
        - ^^^The last line (^^^`24K .``(#3594f7)`^^^) shows the total size of the current directory (^^^`.``(#3594f7)`^^^, which is^^^ `~/project/test_data``(#3594f7)`^^^).^^^
        - ^^^Finally, let's go back to your^^^ `~/project` ^^^directory and check the total size of^^^ `test_data` ^^^using^^^ `du -sh`^^^.^^^
        - ```
cd
``````
 ~/project

``````
du
``````
 -sh test_data
```^^^ ^^^
        - ^^^This will show the summarized size of the^^^ `test_data` ^^^directory:^^^
        - `24K     test_data`^^^ ^^^
        - ^^^This demonstrates how^^^ `du` ^^^can be used to pinpoint disk space consumption within specific directories, helping you manage storage effectively.^^^
        - 
        - # ^^^**Manually Mount and Unmount File Systems**^^^
        - ^^^In this step, you will learn how to manually mount and unmount file systems. Mounting a file system makes its contents accessible through a specific directory (mount point) in the file system hierarchy. Unmounting detaches the file system from its mount point, making its contents inaccessible until it is mounted again. This is a critical skill for managing removable media, temporary storage, or new disk partitions.^^^
        - ^^^For this exercise, we will use one of the unmounted block devices available in your LabEx VM environment. From the previous step, you should have seen the^^^ `/dev/vdb` ^^^device that is not currently mounted. We will use^^^ `/dev/vdb` ^^^for this step.^^^
        - ^^^First, let's confirm the available unmounted block devices using^^^ `lsblk`^^^.^^^
        - `lsblk`^^^ ^^^
        - ^^^You should see^^^ `/dev/vdb` ^^^listed without any mount points.^^^
        - ```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
vda    253:0    0   40G  0 disk
├─vda1 253:1    0    1M  0 part
├─vda2 253:2    0  100M  0 part /boot/efi
└─vda3 253:3    0 39.9G  0 part /
vdb    253:16   0   40G  0 disk
```^^^ ^^^
        - ^^^Before you can mount a file system, you need a mount point, which is an empty directory. It's common practice to use^^^ `/mnt` ^^^for temporary mounts or create a subdirectory within it. Let's create a new directory named^^^ `mydata` ^^^inside your^^^ `~/project` ^^^directory to serve as our mount point.^^^
        - `mkdir`` ~/project/mydata`^^^ ^^^
        - ^^^Now, we need to format the^^^ `/dev/vdb` ^^^device with a file system. We will use the XFS file system, which is the default for Red Hat Enterprise Linux.^^^ ^^^**Be careful with this command, as it will erase all data on the specified device.**^^^
        - `sudo mkfs.xfs /dev/vdb`^^^ ^^^
        - ^^^You will see output indicating the creation of the XFS file system:^^^
        - ```
meta-data=/dev/vdb               isize=512    agcount=4, agsize=2621440 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=1 inobtcount=1 nrext64=0
data     =                       bsize=4096   blocks=10485760, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
```^^^ ^^^
        - ^^^Now that^^^ `/dev/vdb` ^^^has an XFS file system, you can mount it to your^^^ `~/project/mydata` ^^^mount point. The^^^ `mount` ^^^command requires^^^ `sudo` ^^^privileges.^^^
        - `sudo mount /dev/vdb ~/project/mydata`^^^ ^^^
        - ^^^To verify that the file system is successfully mounted, use the^^^ `df -h` ^^^command again. You should see^^^ `/dev/vdb` ^^^listed with^^^ `/home/labex/project/mydata` ^^^as its mount point.^^^
        - `df`` -h`^^^ ^^^
        - ^^^Look for^^^ `/dev/vdb` ^^^in the output:^^^
        - ```
Filesystem      Size  Used Avail Use% Mounted on
...
/dev/vdb         40G  318M   40G   1% /home/labex/project/mydata
```^^^ ^^^
        - ^^^Now, you can create files and directories inside^^^ `~/project/mydata`^^^, and they will be stored on the^^^ `/dev/vdb` ^^^device. Let's create a test file:^^^
        - `sudo ``touch`` ~/project/mydata/testfile.txt`^^^ ^^^
        - ^^^You can list the contents of^^^ `~/project/mydata` ^^^to confirm the file's creation:^^^
        - `ls`` -l ~/project/mydata`^^^ ^^^
        - ^^^You should see^^^ `testfile.txt` ^^^listed:^^^
        - ```
total 0
-rw-r--r--. 1 root root 0 Jun 16 11:09 testfile.txt
```^^^ ^^^
        - ^^^When you are finished using a mounted file system, it's important to unmount it to prevent data corruption, especially before removing a physical device. Use the^^^ `umount` ^^^command to unmount the file system.^^^
        - `sudo umount ~/project/mydata`^^^ ^^^
        - ^^^If the unmount command fails with a "target is busy" error, it means some process is still accessing the mount point. This often happens if your current working directory is inside the mounted file system. To resolve this, change your current directory to a location outside the mount point, for example, your home directory (^^^`~``(#3594f7)`^^^).^^^
        - `cd`` ~`^^^ ^^^
        - ^^^Then, try unmounting again:^^^
        - `sudo umount ~/project/mydata`^^^ ^^^
        - ^^^After unmounting, verify that^^^ `/dev/vdb` ^^^is no longer mounted by checking^^^ `df -h` ^^^again.^^^
        - `df`` -h`^^^ ^^^
        - ^^^You should no longer see^^^ `/dev/vdb` ^^^mounted on^^^ `/home/labex/project/mydata`^^^.^^^
        - ```
Filesystem      Size  Used Avail Use% Mounted on
...
# /dev/vdb should not be listed here anymore
```^^^ ^^^
        - ^^^This completes the process of manually mounting and unmounting a file system.^^^
        - 
        - # ^^^**Locate Files by Name with locate and find**^^^
        - ^^^In this step, you will learn how to locate files on your system using two powerful commands:^^^ `locate` ^^^and^^^ `find`^^^. Both commands help you search for files, but they operate differently and are suited for different scenarios.^^^
        - ### ^^^**Using the**^^^ `**locate**` ^^^**command**^^^
        - ^^^The^^^ `locate` ^^^command is very fast because it searches a pre-built database of file names and paths. However, this means it might not find files that were created or deleted since the last database update. The database is typically updated daily by a cron job, but you can force an update.^^^
        - ^^^First, let's ensure the^^^ `mlocate` ^^^package, which provides the^^^ `locate` ^^^command, is installed.^^^
        - `sudo dnf install -y mlocate`^^^ ^^^
        - ^^^You will see output similar to this during installation:^^^
        - ```
Last metadata expiration check: 0:00:01 ago on Mon 15 May 2023 08:00:00 AM UTC.
Dependencies resolved.
================================================================================
 Package        Architecture  Version             Repository               Size
================================================================================
Installing:
 mlocate        x86_64        0.26-28.el9         rhel-9-for-x86_64-appstream-rpms 100 k

Transaction Summary
================================================================================
Install  1 Package

Total download size: 100 k
Installed size: 230 k
Downloading Packages:
mlocate-0.26-28.el9.x86_64.rpm     100 kB/s | 100 kB     00:01
--------------------------------------------------------------------------------
Total                                            100 kB/s | 100 kB     00:01
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                        1/1
  Installing       : mlocate-0.26-28.el9.x86_64                             1/1
  Running scriptlet: mlocate-0.26-28.el9.x86_64                             1/1
  Verifying        : mlocate-0.26-28.el9.x86_64                             1/1
Installed:
  mlocate-0.26-28.el9.x86_64

Complete!
```^^^ ^^^
        - ^^^After installation, you need to update the^^^ `locate` ^^^database. This command requires^^^ `sudo` ^^^privileges.^^^
        - `sudo updatedb`^^^ ^^^
        - ^^^This command will run silently and may take a few moments depending on the size of your file system.^^^
        - ^^^Now, let's search for a common system file, like^^^ `passwd`^^^.^^^
        - `locate passwd`^^^ ^^^
        - ^^^You will see a list of paths containing "passwd":^^^
        - ```
/etc/passwd
/etc/passwd-
/etc/pam.d/passwd
/usr/share/man/man1/passwd.1.gz
/usr/share/man/man5/passwd.5.gz
...output omitted...
```^^^ ^^^
        - ^^^To perform a case-insensitive search, use the^^^ `-i` ^^^option. Let's search for files containing "messages" without worrying about capitalization.^^^
        - `locate -i messages`^^^ ^^^
        - ^^^You will see results like:^^^
        - ```
/usr/share/locale/zza/LC_MESSAGES
/usr/share/makedumpfile/eppic_scripts/ap_messages_3_10_to_4_8.c
/usr/share/vim/vim82/ftplugin/msmessages.vim
...output omitted...
```^^^ ^^^
        - ^^^You can also limit the number of results using the^^^ `-n` ^^^option. Let's find the first 5 occurrences of "passwd".^^^
        - `locate -n 5 passwd`^^^ ^^^
        - ^^^This will show only the first 5 matches:^^^
        - ```
/etc/passwd
/etc/passwd-
/etc/pam.d/passwd
/usr/share/man/man1/passwd.1.gz
/usr/share/man/man5/passwd.5.gz
```^^^ ^^^
        - ### ^^^**Using the**^^^ `**find**` ^^^**command**^^^
        - ^^^The^^^ `find` ^^^command searches the file system in real-time, which makes it slower than^^^ `locate` ^^^but ensures that it finds all files that match your criteria, including those created very recently. It also offers much more powerful search options.^^^
        - ^^^The basic syntax for^^^ `find` ^^^is^^^ `find [path] [expression]`^^^. If no path is specified, it searches the current directory.^^^
        - ^^^Let's search for the^^^ `sshd_config` ^^^file starting from the root directory (^^^`/`^^^).^^^
        - `find / -name sshd_config`^^^ ^^^
        - ^^^You should see the path to the configuration file:^^^
        - `/etc/ssh/sshd_config`^^^ ^^^
        - ^^^When searching for partial names or using wildcards, it's important to quote the filename pattern to prevent the shell from expanding it prematurely. Let's find all files ending with^^^ `.txt` ^^^in your^^^ `~/project` ^^^directory.^^^
        - `find ~/project -name ``'*.txt'``(#98c379)`^^^ ^^^
        - ^^^If you created^^^ `file1.txt`^^^,^^^ `file2.txt`^^^, and^^^ `file3.txt` ^^^in the previous step, you should see them listed:^^^
        - ```
/home/labex/project/test_data/file1.txt
/home/labex/project/test_data/file2.txt
/home/labex/project/test_data/file3.txt
```^^^ ^^^
        - ^^^To perform a case-insensitive search with^^^ `find`^^^, use the^^^ `-iname` ^^^option. Let's search for files containing "README" (case-insensitive) in the^^^ `/usr/share/doc` ^^^directory.^^^
        - `find /usr/share/doc -iname ``'*readme*'``(#98c379)`^^^ ^^^
        - ^^^You will see many results, for example:^^^
        - ```
/usr/share/doc/libselinux/README
/usr/share/doc/libsepol/README
/usr/share/doc/libsemanage/README
...output omitted...
```^^^ ^^^
        - ^^^The^^^ `find` ^^^command is very versatile and can be combined with other criteria, which you will explore in the next steps.^^^
        - 
        - # ^^^**Find Files by Ownership, Permissions, Size, and Time**^^^
        - ^^^In this step, you will learn how to use the powerful^^^ `find` ^^^command to locate files based on various criteria beyond just their name. This includes searching by ownership, permissions, size, and modification time. These advanced search capabilities are essential for system administration tasks like auditing, cleanup, and troubleshooting.^^^
        - ### ^^^**Find Files by Ownership**^^^
        - ^^^You can search for files owned by a specific user or group using the^^^ `-user` ^^^and^^^ `-group` ^^^options, respectively. You can specify the user/group name or their numeric ID.^^^
        - ^^^Let's find all files in your home directory (^^^`~``(#3594f7)`^^^) that are owned by the^^^ `labex``(#3594f7)` ^^^user.^^^
        - `find ~ -user labex`^^^ ^^^
        - ^^^This will list many files, including your configuration files:^^^
        - ```
/home/labex
/home/labex/.bash_logout
/home/labex/.bash_profile
/home/labex/.bashrc
/home/labex/.config
/home/labex/.config/xfce4
/home/labex/.config/xfce4/xfconf
/home/labex/.config/xfce4/xfconf/xfce-perchannel-xml
/home/labex/.local
/home/labex/.local/share
/home/labex/.local/share/nano
/home/labex/project
/home/labex/project/test_data
/home/labex/project/test_data/file1.txt
/home/labex/project/test_data/file2.txt
/home/labex/project/test_data/file3.txt
...output omitted...
```^^^ ^^^
        - ^^^Similarly, to find files owned by the^^^ `labex` ^^^group:^^^
        - `find ~ -group labex`^^^ ^^^
        - ^^^The output will be similar, as^^^ `labex` ^^^is typically the primary group for the^^^ `labex` ^^^user.^^^
        - ^^^You can also search by User ID (UID) or Group ID (GID). The^^^ `labex``(#3594f7)` ^^^user typically has a UID and GID of^^^ `1000``(#3594f7)`^^^.^^^
        - `find ~ -uid 1000`^^^ ^^^
        - `find ~ -gid 1000`^^^ ^^^
        - ### ^^^**Find Files by Permissions**^^^
        - ^^^The^^^ `find` ^^^command's^^^ `-perm` ^^^option allows you to search for files with specific permissions. Permissions can be specified in octal (e.g.,^^^ `755`^^^) or symbolic (e.g.,^^^ `u=rwx,g=rx,o=rx`^^^) mode.^^^
        - ^^^Let's create a test file in your^^^ `~/project` ^^^directory with specific permissions.^^^
        - ```
touch
``````
 ~/project/permission_test.txt

``````
chmod
``````
 644 ~/project/permission_test.txt
```^^^ ^^^
        - ^^^Now, let's find files in^^^ `~/project` ^^^that have exactly^^^ `644` ^^^permissions.^^^
        - `find ~/project -perm 644`^^^ ^^^
        - ^^^You should see^^^ `permission_test.txt` ^^^listed:^^^
        - `/home/labex/project/permission_test.txt`^^^ ^^^
        - ^^^You can also use a leading^^^ `/` ^^^or^^^ `-` ^^^with the octal permissions:^^^
            - `/`^^^: Matches if^^^  ^^^ *any* ^^^^^^ ^^^ ^^^of the specified permission bits are set.^^^
            - `-`^^^: Matches if^^^  ^^^ *all* ^^^^^^ ^^^ ^^^of the specified permission bits are set.^^^
        - ^^^Let's find files in^^^ `~/project` ^^^where others have at least read permission (^^^`o=r` ^^^or^^^ `004`^^^).^^^
        - `find ~/project -perm -004`^^^ ^^^
        - ^^^This will list^^^ `permission_test.txt` ^^^and other files that grant read access to others.^^^
        - ```
/home/labex/project/permission_test.txt
...output omitted...
```^^^ ^^^
        - ### ^^^**Find Files by Size**^^^
        - ^^^The^^^ `-size` ^^^option allows you to search for files based on their size. You can specify the size with units (e.g.,^^^ `k` ^^^for kilobytes,^^^ `M` ^^^for megabytes,^^^ `G` ^^^for gigabytes). You can also use^^^ `+` ^^^for "greater than" and^^^ `-` ^^^for "less than".^^^
        - ^^^Let's find files in your^^^ `~/project/test_data` ^^^directory that are exactly 1 kilobyte in size.^^^
        - `find ~/project/test_data -size 1k`^^^ ^^^
        - ^^^You should see^^^ `file1.txt`^^^:^^^
        - `/home/labex/project/test_data/file1.txt`^^^ ^^^
        - ^^^Now, find files larger than 5 kilobytes.^^^
        - `find ~/project/test_data -size +5k`^^^ ^^^
        - ^^^This should list^^^ `file3.txt`^^^:^^^
        - `/home/labex/project/test_data/file3.txt`^^^ ^^^
        - ^^^And files smaller than 10 kilobytes.^^^
        - `find ~/project/test_data -size -10k`^^^ ^^^
        - ^^^This should list^^^ `file1.txt` ^^^and^^^ `file2.txt`^^^:^^^
        - ```
/home/labex/project/test_data/file1.txt
/home/labex/project/test_data/file2.txt
```^^^ ^^^
        - ### ^^^**Find Files by Modification Time**^^^
        - ^^^You can search for files based on their modification time using options like^^^ `-mmin` ^^^(modified minutes ago) or^^^ `-mtime` ^^^(modified days ago).^^^
        - ^^^Let's find files in your^^^ `~/project` ^^^directory that were modified within the last 60 minutes.^^^
        - `find ~/project -mmin -60`^^^ ^^^
        - ^^^This will likely include^^^ `permission_test.txt` ^^^and the files in^^^ `test_data` ^^^if you created them recently:^^^
        - ```
/home/labex/project
/home/labex/project/permission_test.txt
/home/labex/project/test_data
/home/labex/project/test_data/file1.txt
/home/labex/project/test_data/file2.txt
/home/labex/project/test_data/file3.txt
```^^^ ^^^
        - ^^^To find files modified more than 1 day ago (24 hours), you can use^^^ `+1``(#3594f7)` ^^^with^^^ `-mtime``(#3594f7)`^^^.^^^
        - `find ~/project -mtime +1`^^^ ^^^
        - ^^^This command might not return any files if all your^^^ `~/project` ^^^files were created or modified recently.^^^
        - ^^^These options can be combined to create very specific search queries, allowing you to efficiently manage files on your system.^^^
        - 
        - # ^^^**Search for Files Based on File Type**^^^
        - ^^^In this final step, you will learn how to use the^^^ `find` ^^^command to search for files based on their type. This is particularly useful when you need to locate all directories, regular files, symbolic links, or device files within a specific path.^^^
        - ^^^The^^^ `find` ^^^command uses the^^^ `-type` ^^^option followed by a single character to specify the file type. Here are some common file types you can search for:^^^
            - `f`^^^: Regular file^^^
            - `d`^^^: Directory^^^
            - `l`^^^: Symbolic link (symlink)^^^
            - `b`^^^: Block device^^^
            - `c`^^^: Character device^^^
            - `p`^^^: Named pipe (FIFO)^^^
            - `s`^^^: Socket^^^
        - ^^^Let's start by searching for all directories within your^^^ `~/project` ^^^directory.^^^
        - `find ~/project -``type`` d`^^^ ^^^
        - ^^^You should see output similar to this, listing all directories and subdirectories:^^^
        - ```
/home/labex/project
/home/labex/project/test_data
```^^^ ^^^
        - ^^^Next, let's search for all regular files within your^^^ `~/project` ^^^directory.^^^
        - `find ~/project -``type`` f`^^^ ^^^
        - ^^^This will list files like^^^ `file1.txt`^^^,^^^ `file2.txt`^^^, and^^^ `file3.txt` ^^^that you created earlier:^^^
        - ```
/home/labex/project/test_data/file1.txt
/home/labex/project/test_data/file2.txt
/home/labex/project/test_data/file3.txt
```^^^ ^^^
        - ^^^Now, let's create a symbolic link to demonstrate searching for symlinks. We'll create a symlink to^^^ `file1.txt` ^^^in your^^^ `~/project` ^^^directory.^^^
        - `ln`` -s ~/project/test_data/file1.txt ~/project/link_to_file1.txt`^^^ ^^^
        - ^^^Verify the symlink was created using^^^ `ls -l`^^^:^^^
        - `ls`` -l ~/project/link_to_file1.txt`^^^ ^^^
        - ^^^You should see output indicating it's a symbolic link:^^^
        - `lrwxrwxrwx. 1 labex labex 32 May 15 08:00 /home/labex/project/link_to_file1.txt -> /home/labex/project/test_data/file1.txt`^^^ ^^^
        - ^^^Now, search for all symbolic links within your^^^ `~/project` ^^^directory.^^^
        - `find ~/project -``type`` l`^^^ ^^^
        - ^^^You should see your newly created symlink:^^^
        - `/home/labex/project/link_to_file1.txt`^^^ ^^^
        - ^^^Finally, let's search for block devices. Block devices are typically found in the^^^ `/dev` ^^^directory.^^^
        - `find /dev -``type`` b`^^^ ^^^
        - ^^^This will list block devices like^^^ `vda`^^^,^^^ `vda1`^^^,^^^ `vda2`^^^, etc.:^^^
        - ```
/dev/vda1
/dev/vda2
/dev/vda3
/dev/vda
/dev/vdb
```^^^ ^^^
        - ^^^You can combine the^^^ `-type` ^^^option with other^^^ `find` ^^^options you learned in previous steps. For example, to find all directories in^^^ `/etc` ^^^that are owned by the^^^ `root` ^^^user:^^^
        - `find /etc -``type`` d -user root`^^^ ^^^
        - ^^^This will produce a long list of directories:^^^
        - ```
/etc
/etc/selinux
/etc/selinux/targeted
/etc/selinux/targeted/active
/etc/selinux/targeted/active/modules
...output omitted...
```^^^ ^^^
        - ^^^This concludes the lab on accessing Linux file systems and locating files. You have learned how to identify devices, examine disk usage, manually mount and unmount file systems, and use^^^ `locate` ^^^and^^^ `find` ^^^with various criteria.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, we gained practical experience in managing Linux file systems on a Red Hat Enterprise Linux system. We began by learning to identify file systems and block devices using commands like^^^ `lsblk`^^^, understanding core concepts such as block devices, partitions, file systems, and mount points. Subsequently, we explored how to examine file system usage with^^^ `df` ^^^and^^^ `du`^^^, distinguishing between their functionalities for reporting disk space. The lab also covered the essential skill of manually mounting and unmounting file systems, demonstrating how to make file system contents accessible and then detach them.^^^
        - ^^^Furthermore, we delved into locating files efficiently using various criteria. We learned to find files by name with^^^ `locate` ^^^and^^^ `find`^^^, understanding the differences and appropriate use cases for each. The lab extended this by teaching how to search for files based on ownership, permissions, size, and time attributes, providing powerful tools for system administration and troubleshooting. Finally, we practiced searching for files based on their specific file types, completing a comprehensive overview of file system management and file location techniques.^^^
-  **Red Hat System Administration (RH134) Certification Labs - **11 labs
    1. **Create and Execute Bash Scripts in RHEL**
        - Create and Execute a Simple Bash Script
        - Enhance Bash Script with System Commands and Make Executable
        - Use For Loops to Automate Hostname Retrieval on RHEL Servers
        - Create and Execute a Bash Script with For Loop for RHEL Servers
        - Filter Command Output with Grep and Regular Expressions on RHEL
        - Build a Comprehensive RHEL System Information Script
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will learn to create and execute Bash scripts for RHEL system administration. You will begin by crafting simple scripts, then enhance them with system commands and make them executable. The lab progresses to using^^^ `for` ^^^loops for automating tasks like system information gathering and filtering command output with^^^ `grep` ^^^and regular expressions. Finally, you will build a comprehensive RHEL system information script, gaining practical skills in automating administrative tasks and leveraging powerful shell features.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^beginner^^^ ^^^level lab with a^^^ ^^^86%^^^ ^^^completion rate. It has received a^^^ ^^^91%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Create and Execute a Simple Bash Script**^^^
        - ^^^In this step, you will learn how to create a basic Bash script and execute it. Bash scripts are plain text files containing a series of commands that the Bash shell can execute. They are powerful tools for automating repetitive tasks and combining multiple commands into a single executable unit.^^^
        - ^^^First, you will create a new directory to store your scripts. It's good practice to organize your files, and placing scripts in a dedicated directory helps keep your home directory tidy.^^^
            1. ^^^**Create a directory for your scripts.**^^^
                - 
                - ^^^Use the^^^ `mkdir` ^^^command to create a directory named^^^ `scripts` ^^^within your^^^ `~/project` ^^^directory. This is where you will store your Bash scripts.^^^
                - `mkdir`` ~/project/scripts`^^^ ^^^
                - ^^^There will be no direct output from this command if successful.^^^
            2. ^^^**Create your first Bash script file.**^^^
                - 
                - ^^^Navigate into the newly created^^^ `scripts` ^^^directory and use the^^^ `nano` ^^^text editor to create a file named^^^ `firstscript.sh`^^^. The^^^ `.sh` ^^^extension is a common convention for shell scripts, though not strictly required.^^^
                - ```
cd
``````
 ~/project/scripts
nano firstscript.sh
```^^^ ^^^
                - ^^^Inside the^^^ `nano` ^^^editor, you will see a blank screen.^^^
            3. ^^^**Add content to your script.**^^^
                - 
                - ^^^Every Bash script should start with a "shebang" line,^^^ `#!/usr/bin/bash`^^^. This line tells the operating system which interpreter to use for executing the script (in this case, Bash). After the shebang, you will add a simple^^^ `echo` ^^^command to print a message to the terminal.^^^
                - ^^^Type the following lines into the^^^ `nano` ^^^editor:^^^
                - ```
#!/usr/bin/bash
``````
(#61aeee)

``````
echo
``````
(#e6c07b) 
``````
"Hello, LabEx! This is my first Bash script."
``````
(#98c379)
```^^^ ^^^
                - ^^^Once you have entered the content, save the file by pressing^^^ `Ctrl+O`^^^, then^^^ `Enter` ^^^to confirm the filename, and^^^ `Ctrl+X` ^^^to exit^^^ `nano`^^^.^^^
                - ^^^Your terminal should return to the command prompt.^^^
            4. ^^^**Execute your script using the**^^^ `**bash**` ^^^**interpreter.**^^^
                - 
                - ^^^You can execute a Bash script by explicitly telling the^^^ `bash` ^^^interpreter to run it. This method does not require the script to have executable permissions.^^^
                - `bash firstscript.sh`^^^ ^^^
                - ^^^You should see the output of your script:^^^
                - `Hello, LabEx! This is my first Bash script.`^^^ ^^^
                - ^^^This confirms that your script was created correctly and executed successfully.^^^
        - 
        - # ^^^**Enhance Bash Script with System Commands and Make Executable**^^^
        - ^^^In this step, you will enhance your Bash script by adding more system commands and learn how to make the script directly executable. Making a script executable allows you to run it like any other command, without explicitly calling the^^^ `bash` ^^^interpreter.^^^
            1. ^^^**Navigate to your scripts directory.**^^^
                - 
                - ^^^Ensure you are in the^^^ `~/project/scripts` ^^^directory where you created^^^ `firstscript.sh` ^^^in the previous step.^^^
                - `cd`` ~/project/scripts`^^^ ^^^
            2. ^^^**Edit**^^^ `**firstscript.sh**` ^^^**to include more system commands.**^^^
                - 
                - ^^^You will now add commands to your script that display system information, such as block devices and filesystem free space. This demonstrates how scripts can automate the collection of system data.^^^
                - ^^^Open^^^ `firstscript.sh` ^^^using^^^ `nano`^^^:^^^
                - `nano firstscript.sh`^^^ ^^^
                - ^^^Modify the content of the file to match the following. This script will now:^^^
                    - ^^^Print a header for block device information.^^^
                    - ^^^Execute^^^ `lsblk` ^^^to list block devices.^^^
                    - ^^^Print a header for filesystem free space.^^^
                    - ^^^Execute^^^ `df -h` ^^^to display disk space usage in a human-readable format.^^^
                - ```
#!/usr/bin/bash
``````
(#61aeee)

``````
echo
``````
(#e6c07b) 
``````
"Hello, LabEx! This is my first Bash script."
``````
(#98c379)

``````
echo
``````
(#e6c07b) 
``````
"#####################################################"
``````
(#98c379)

``````
echo
``````
(#e6c07b) 
``````
"LIST BLOCK DEVICES"
``````
(#98c379)

``````
echo
``````
(#e6c07b) 
``````
"#####################################################"
``````
(#98c379)
lsblk

``````
echo
``````
(#e6c07b) 
``````
"#####################################################"
``````
(#98c379)

``````
echo
``````
(#e6c07b) 
``````
"FILESYSTEM FREE SPACE STATUS"
``````
(#98c379)

``````
echo
``````
(#e6c07b) 
``````
"#####################################################"
``````
(#98c379)

``````
df
``````
(#e6c07b) -h
```^^^ ^^^
                - ^^^Save the file by pressing^^^ `Ctrl+O`^^^, then^^^ `Enter`^^^, and^^^ `Ctrl+X` ^^^to exit^^^ `nano`^^^.^^^
            3. ^^^**Make the script executable.**^^^
                - 
                - ^^^To run a script directly (e.g.,^^^ `./firstscript.sh``(#3594f7)`^^^), you need to grant it executable permissions. The^^^ `chmod``(#3594f7)` ^^^command is used to change file permissions.^^^ `+x``(#3594f7)` ^^^adds execute permission for all users.^^^
                - `chmod`` +x firstscript.sh`^^^ ^^^
                - ^^^There will be no direct output from this command if successful.^^^
            4. ^^^**Execute the script directly.**^^^
                - 
                - ^^^Now that the script is executable, you can run it by specifying its path. Since it's in your current directory, you use^^^ `./` ^^^followed by the script name.^^^
                - `./firstscript.sh`^^^ ^^^
                - ^^^You should see output similar to this, combining your initial message with the output of^^^ `lsblk` ^^^and^^^ `df -h`^^^:^^^
                - ```
Hello, LabEx! This is my first Bash script.
#####################################################
LIST BLOCK DEVICES
#####################################################
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0         7:0    0 10.2G  1 loop /
loop1         7:1    0  200M  1 loop /usr/local/bin
loop2         7:2    0  200M  1 loop /usr/local/go
loop3         7:3    0  200M  1 loop /usr/local/java
loop4         7:4    0  200M  1 loop /usr/local/node
loop5         7:5    0  200M  1 loop /usr/local/python
#####################################################
FILESYSTEM FREE SPACE STATUS
#####################################################
Filesystem      Size  Used Avail Use% Mounted on
overlay          10G  4.0G  6.1G  40% /
tmpfs            64M     0   64M   0% /dev
tmpfs           7.8G     0  7.8G   0% /sys/fs/cgroup
shm              64M     0   64M   0% /dev/shm
/dev/loop0       10G  4.0G  6.1G  40% /
tmpfs           7.8G     0  7.8G   0% /proc/asound
tmpfs           7.8G     0  7.8G   0% /proc/acpi
tmpfs           7.8G     0  7.8G   0% /proc/scsi
tmpfs           7.8G     0  7.8G   0% /sys/firmware
```^^^ ^^^
                - ^^^The exact output for^^^ `lsblk` ^^^and^^^ `df -h` ^^^may vary slightly depending on the specific environment, but the structure and presence of the commands' output should be similar.^^^
        - 
        - # ^^^**Use For Loops to Automate Hostname Retrieval on RHEL Servers**^^^
        - ^^^In this step, you will learn about^^^ `for` ^^^loops in Bash and how to use them to automate tasks across multiple servers.^^^ `for` ^^^loops are fundamental control flow statements that allow you to execute a block of code repeatedly for each item in a list. This is particularly useful for managing multiple systems efficiently.^^^
        - ^^^For this exercise, we will demonstrate the concept using localhost with different approaches to simulate working with multiple servers.^^^
            1. ^^^**Retrieve hostname using local commands.**^^^
                - 
                - ^^^Before using a loop, let's see how you would typically get the hostname from the local system. We'll use different methods to demonstrate the concept.^^^
                - ```
hostname
hostname -f
```^^^ ^^^
                - ^^^You should see output similar to this:^^^
                - ```
684791f71c0e35fea6cc1243
684791f71c0e35fea6cc1243
```^^^ ^^^
                - ^^^This demonstrates that you can successfully retrieve hostname information using different options. Note that in this container environment, all hostname options return the same container ID.^^^
            2. ^^^**Create a**^^^ `**for**` ^^^**loop to automate hostname retrieval with different options.**^^^
                - 
                - ^^^Now, let's use a^^^ `for` ^^^loop to perform different hostname commands more efficiently. The^^^ `for` ^^^loop will iterate over a list of hostname options, executing the^^^ `hostname` ^^^command with each option.^^^
                - ```
for
``````
(#c678dd) OPTION 
``````
in
``````
(#c678dd) 
``````
""
``````
(#98c379) 
``````
"-f"
``````
(#98c379) 
``````
"-s"
``````
(#98c379); 
``````
do
``````
(#c678dd)
  
``````
echo
``````
(#e6c07b) 
``````
"hostname 
``````
(#98c379)
``````
${OPTION}
``````
(#d19a66)
``````
:"
``````
(#98c379)
  hostname 
``````
${OPTION}
``````
(#d19a66)
  
``````
echo
``````
(#e6c07b) 
``````
""
``````
(#98c379)

``````
done
``````
(#c678dd)
```^^^ ^^^
                - ^^^Let's break down this command:^^^
                    - `for OPTION in "" "-f" "-s";`^^^: This part initializes the loop.^^^ `OPTION` ^^^is a variable that will take on the value of each item in the list (empty string,^^^ `-f`^^^,^^^ `-s`^^^) during each iteration.^^^
                    - `do`^^^: Marks the beginning of the commands to be executed in the loop.^^^
                    - `echo "hostname ${OPTION}:";`^^^: This displays which option is being used.^^^
                    - `hostname ${OPTION};`^^^: This is the command executed in each iteration.^^^ `${OPTION}` ^^^expands to the current value of the^^^ `OPTION` ^^^variable.^^^
                    - `echo "";`^^^: Adds a blank line for better readability.^^^
                    - `done`^^^: Marks the end of the loop.^^^
                - ^^^You should see output similar to this:^^^
                - ```
hostname :
684791f71c0e35fea6cc1243

hostname -f:
684791f71c0e35fea6cc1243

hostname -s:
684791f71c0e35fea6cc1243
```^^^ ^^^
                - ^^^This demonstrates the power of^^^ `for` ^^^loops in automating repetitive tasks with different parameters.^^^
        - 
        - # ^^^**Create and Execute a Bash Script with For Loop for RHEL Servers**^^^
        - ^^^In this step, you will encapsulate the^^^ `for` ^^^loop you learned in the previous step into a Bash script. This allows you to save the automation logic and reuse it easily. You will also learn about the^^^ `PATH` ^^^environment variable and how to make your scripts accessible from any directory.^^^
            1. ^^^**Navigate to your scripts directory.**^^^
                - 
                - ^^^Ensure you are in the^^^ `~/project/scripts` ^^^directory.^^^
                - `cd`` ~/project/scripts`^^^ ^^^
            2. ^^^**Create a new script for hostname retrieval.**^^^
                - 
                - ^^^You will create a script named^^^ `get_hostnames.sh` ^^^that contains the^^^ `for` ^^^loop to retrieve hostname information using different options.^^^
                - ^^^Open^^^ `get_hostnames.sh` ^^^using^^^ `nano`^^^:^^^
                - `nano get_hostnames.sh`^^^ ^^^
                - ^^^Add the following content to the file:^^^
                - ```
#!/usr/bin/bash
``````
(#61aeee)

``````
# This script retrieves hostname information using different options.
``````
(#5c6370)


``````
for
``````
(#c678dd) OPTION 
``````
in
``````
(#c678dd) 
``````
""
``````
(#98c379) 
``````
"-f"
``````
(#98c379) 
``````
"-s"
``````
(#98c379); 
``````
do
``````
(#c678dd)
  
``````
echo
``````
(#e6c07b) 
``````
"Getting hostname with option: 
``````
(#98c379)
``````
${OPTION}
``````
(#d19a66)
``````
"
``````
(#98c379)
  hostname 
``````
${OPTION}
``````
(#d19a66)
  
``````
echo
``````
(#e6c07b) 
``````
"------------------------"
``````
(#98c379)

``````
done
``````
(#c678dd)


``````
exit
``````
(#e6c07b) 0
```^^^ ^^^
                - ^^^Save the file by pressing^^^ `Ctrl+O`^^^, then^^^ `Enter`^^^, and^^^ `Ctrl+X` ^^^to exit^^^ `nano`^^^.^^^
                - ^^^Let's break down the new elements:^^^
                    - `# This script...`^^^: Lines starting with^^^ `#` ^^^are comments. They are ignored by the shell but are useful for documenting your script.^^^
                    - `echo "Getting hostname with option: ${OPTION}"`^^^: This line provides feedback during script execution, indicating which option is currently being used.^^^
                    - `exit 0`^^^: This command explicitly exits the script with a status code of^^^ `0`^^^, which conventionally indicates success.^^^
            3. ^^^**Make the script executable.**^^^
                - 
                - ^^^Just like in the previous step, you need to give your new script executable permissions.^^^
                - `chmod`` +x get_hostnames.sh`^^^ ^^^
                - ^^^There will be no direct output from this command if successful.^^^
            4. ^^^**Execute the script from its current directory.**^^^
                - 
                - ^^^Run the script to verify its functionality.^^^
                - `./get_hostnames.sh`^^^ ^^^
                - ```
You should see output similar to this:
```^^^ ^^^
                - ```
Getting hostname with option:
684791f71c0e35fea6cc1243
------------------------
Getting hostname with option: -f
684791f71c0e35fea6cc1243
------------------------
Getting hostname with option: -s
684791f71c0e35fea6cc1243
------------------------
```^^^ ^^^
            5. ^^^**Understand the**^^^ `**PATH**` ^^^**environment variable.**^^^
                - 
                - ^^^The^^^ `PATH` ^^^environment variable is a list of directories that the shell searches for executable commands. When you type a command like^^^ `ls` ^^^or^^^ `grep`^^^, the shell looks in the directories listed in^^^ `PATH` ^^^to find the corresponding executable file.^^^
                - ^^^Display your current^^^ `PATH` ^^^variable:^^^
                - `echo`` ``$PATH``(#d19a66)`^^^ ^^^
                - ^^^You will see a colon-separated list of directories. For example:^^^
                - `/home/labex/.local/bin:/home/labex/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin`^^^ ^^^
                - ^^^Notice that^^^ `~/project/scripts` ^^^(or^^^ `/home/labex/project/scripts`^^^) is not typically included in the default^^^ `PATH`^^^. This is why you had to use^^^ `./get_hostnames.sh` ^^^to execute your script.^^^
            6. ^^^**Add your scripts directory to the**^^^ `**PATH**` ^^^**(Optional, for future reference).**^^^
                - 
                - ^^^While not strictly required for this lab step, it's common practice to add a personal^^^ `bin` ^^^or^^^ `scripts` ^^^directory to your^^^ `PATH` ^^^so you can run your custom scripts from any location. You can do this by adding a line like^^^ `export PATH=$PATH:~/project/scripts` ^^^to your^^^ `~/.bashrc` ^^^or^^^ `~/.zshrc` ^^^file. For this lab, we will continue to execute scripts by specifying their path.^^^
        - 
        - # ^^^**Filter Command Output with Grep and Regular Expressions on RHEL**^^^
        - ^^^In this step, you will learn how to use the^^^ `grep` ^^^command with regular expressions to efficiently filter and extract specific information from command output and files.^^^ `grep` ^^^is a powerful utility for searching plain-text data sets for lines that match a regular expression. Regular expressions (regex) are sequences of characters that define a search pattern.^^^
            1. ^^^**Search for specific user and group information in system files.**^^^
                - 
                - ^^^You will use^^^ `grep` ^^^to find information about the^^^ `labex` ^^^user and group from the^^^ `/etc/passwd` ^^^and^^^ `/etc/group` ^^^files. These files store user and group account information, respectively.^^^
                - ^^^First, let's look for the^^^ `labex` ^^^user entry in^^^ `/etc/passwd`^^^:^^^
                - `grep ``"labex"``(#98c379)`` /etc/passwd`^^^ ^^^
                - ^^^Expected output:^^^
                - `labex:x:1000:1000::/home/labex:/bin/bash`^^^ ^^^
                - ^^^Next, find the^^^ `labex` ^^^group entry in^^^ `/etc/group`^^^:^^^
                - `grep ``"labex"``(#98c379)`` /etc/group`^^^ ^^^
                - ^^^Expected output:^^^
                - `labex:x:1000:`^^^ ^^^
                - ^^^These commands demonstrate basic^^^ `grep` ^^^usage to find exact string matches.^^^
            2. ^^^**Filter**^^^ `**lscpu**` ^^^**output using**^^^ `**grep**` ^^^**and regular expressions.**^^^
                - 
                - ^^^The^^^ `lscpu` ^^^command displays CPU architecture information. Often, you only need specific lines from its extensive output. You can use^^^ `grep` ^^^with a regular expression to filter for lines that start with "CPU".^^^
                - `lscpu | grep ``'^CPU'``(#98c379)`^^^ ^^^
                - ^^^Let's break down this command:^^^
                    - `lscpu`^^^: Generates the CPU information.^^^
                    - `|`^^^: This is a pipe, which takes the standard output of^^^ `lscpu` ^^^and feeds it as standard input to the^^^ `grep` ^^^command.^^^
                    - `grep '^CPU'`^^^: Searches for lines that start with the literal string "CPU". The^^^ `^` ^^^(caret) is a regular expression anchor that matches the beginning of a line.^^^
                - ^^^Expected output (may vary slightly based on environment):^^^
                - ```
CPU op-mode(s):                     32-bit, 64-bit
CPU(s):                             4
CPU family:                         6
```^^^ ^^^
            3. ^^^**Filter configuration files, ignoring comments and empty lines.**^^^
                - 
                - ^^^Configuration files often contain comments (lines starting with^^^ `#``(#3594f7)`^^^) and empty lines that are not relevant to the actual configuration. You can use^^^ `grep``(#3594f7)` ^^^with multiple patterns to exclude these lines. Let's demonstrate this with the^^^ `/etc/passwd``(#3594f7)` ^^^file.^^^
                - `grep -v ``'^#'``(#98c379)`` /etc/passwd | ``head``(#e6c07b)`` -5`^^^ ^^^
                - ^^^Let's break down this command:^^^
                    - `grep -v '^#' /etc/passwd`^^^: The^^^ `-v` ^^^option inverts the match, meaning it selects lines that^^^  ^^^ *do not* ^^^^^^ ^^^ ^^^match the pattern.^^^ `^#` ^^^matches lines that start with a^^^ `#`^^^. So, this part filters out comment lines.^^^
                    - `|`^^^: Pipes the output of the first^^^ `grep` ^^^command to the next command.^^^
                    - `head -5`^^^: Shows only the first 5 lines of the output.^^^
                - ^^^Expected output (showing user account entries without comments):^^^
                - ```
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
```^^^ ^^^
            4. ^^^**Search for specific patterns in system files.**^^^
                - 
                - ^^^You can use^^^ `grep` ^^^to search for specific patterns in various system files. Let's search for shell-related entries in the^^^ `/etc/passwd` ^^^file.^^^
                - `grep ``"bash"``(#98c379)`` /etc/passwd`^^^ ^^^
                - ^^^Expected output (showing users with bash shell):^^^
                - ```
root:x:0:0:root:/root:/bin/bash
labex:x:1000:1000::/home/labex:/bin/bash
```^^^ ^^^
                - ^^^This command helps you identify users who have bash as their default shell.^^^
        - 
        - # ^^^**Build a Comprehensive RHEL System Information Script**^^^
        - ^^^In this final step, you will combine all the concepts learned so far – Bash scripting,^^^ `for` ^^^loops,^^^ `ssh` ^^^for remote execution, and^^^ `grep` ^^^with regular expressions for filtering – to build a comprehensive script that gathers system information from multiple RHEL servers. The script will save the collected data to separate output files for each server.^^^
            1. ^^^**Navigate to your scripts directory.**^^^
                - 
                - ^^^Ensure you are in the^^^ `~/project/scripts` ^^^directory.^^^
                - `cd`` ~/project/scripts`^^^ ^^^
            2. ^^^**Create a new script named**^^^ `**system_info.sh**`^^^**.**^^^
                - 
                - ^^^This script will gather system information using different approaches to demonstrate the concepts, and redirect the output to distinct files in your^^^ `~/project` ^^^directory.^^^
                - ^^^Open^^^ `system_info.sh` ^^^using^^^ `nano`^^^:^^^
                - `nano system_info.sh`^^^ ^^^
                - ^^^Add the following content to the file:^^^
                - ```
#!/usr/bin/bash
``````
(#61aeee)


``````
# Define variables for output directory
``````
(#5c6370)
OUT_DIR=
``````
'/home/labex/project'
``````
(#98c379)


``````
# Loop through different information gathering approaches
``````
(#5c6370)

``````
for
``````
(#c678dd) APPROACH 
``````
in
``````
(#c678dd) 
``````
"basic"
``````
(#98c379) 
``````
"detailed"
``````
(#98c379); 
``````
do
``````
(#c678dd)
  OUTPUT_FILE=
``````
"
``````
(#98c379)
``````
${OUT_DIR}
``````
(#d19a66)
``````
/output-
``````
(#98c379)
``````
${APPROACH}
``````
(#d19a66)
``````
.txt"
``````
(#98c379)

  
``````
echo
``````
(#e6c07b) 
``````
"Gathering 
``````
(#98c379)
``````
${APPROACH}
``````
(#d19a66)
``````
 system information..."
``````
(#98c379)
  
``````
# Clear previous output file or create a new one
``````
(#5c6370)
  > 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)

  
``````
# Get hostname information
``````
(#5c6370)
  
``````
echo
``````
(#e6c07b) 
``````
"### Hostname Information ###"
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  
``````
if
``````
(#c678dd) [ 
``````
"
``````
(#98c379)
``````
${APPROACH}
``````
(#d19a66)
``````
"
``````
(#98c379) = 
``````
"basic"
``````
(#98c379) ]; 
``````
then
``````
(#c678dd)
    hostname >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  
``````
else
``````
(#c678dd)
    hostname -f >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  
``````
fi
``````
(#c678dd)
  
``````
echo
``````
(#e6c07b) 
``````
""
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379) 
``````
# Add a blank line for readability
``````
(#5c6370)

  
``````
# Get CPU information (only lines starting with CPU)
``````
(#5c6370)
  
``````
echo
``````
(#e6c07b) 
``````
"### CPU Information ###"
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  lscpu | grep 
``````
'^CPU'
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  
``````
echo
``````
(#e6c07b) 
``````
""
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)

  
``````
# Get system users with bash shell
``````
(#5c6370)
  
``````
echo
``````
(#e6c07b) 
``````
"### Users with Bash Shell ###"
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  grep 
``````
"bash"
``````
(#98c379) /etc/passwd >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  
``````
echo
``````
(#e6c07b) 
``````
""
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)

  
``````
# Get system information based on approach
``````
(#5c6370)
  
``````
if
``````
(#c678dd) [ 
``````
"
``````
(#98c379)
``````
${APPROACH}
``````
(#d19a66)
``````
"
``````
(#98c379) = 
``````
"basic"
``````
(#98c379) ]; 
``````
then
``````
(#c678dd)
    
``````
echo
``````
(#e6c07b) 
``````
"### Basic System Info ###"
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
    
``````
uname
``````
(#e6c07b) -r >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  
``````
else
``````
(#c678dd)
    
``````
echo
``````
(#e6c07b) 
``````
"### Detailed System Info ###"
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
    
``````
uname
``````
(#e6c07b) -a >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  
``````
fi
``````
(#c678dd)
  
``````
echo
``````
(#e6c07b) 
``````
""
``````
(#98c379) >> 
``````
"
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)

  
``````
echo
``````
(#e6c07b) 
``````
"Information saved to 
``````
(#98c379)
``````
${OUTPUT_FILE}
``````
(#d19a66)
``````
"
``````
(#98c379)
  
``````
echo
``````
(#e6c07b) 
``````
"-----------------------------------------------------"
``````
(#98c379)

``````
done
``````
(#c678dd)


``````
echo
``````
(#e6c07b) 
``````
"Script execution complete."
``````
(#98c379)
```^^^ ^^^
                - ^^^Save the file by pressing^^^ `Ctrl+O`^^^, then^^^ `Enter`^^^, and^^^ `Ctrl+X` ^^^to exit^^^ `nano`^^^.^^^
                - ^^^Key elements of this script:^^^
                    - `OUT_DIR='/home/labex/project'`^^^: Variable is used to make the script more flexible and readable.^^^
                    - `OUTPUT_FILE="${OUT_DIR}/output-${APPROACH}.txt"`^^^: Constructs the output filename dynamically for each approach.^^^
                    - `> "${OUTPUT_FILE}"`^^^: This redirects the output of an empty command to the file, effectively clearing its content if it exists or creating it if it doesn't. This ensures a fresh file for each run.^^^
                    - `>> "${OUTPUT_FILE}"`^^^: This appends the output of the command to the specified file.^^^
                    - `if [ "${APPROACH}" = "basic" ]; then ... else ... fi`^^^: Conditional statements that execute different commands based on the approach being used.^^^
                    - `echo "### Section Header ###"`^^^: Adds clear headers to the output file for better organization.^^^
            3. ^^^**Make the script executable.**^^^
                - `chmod`` +x system_info.sh`^^^ ^^^
                - ^^^There will be no direct output from this command if successful.^^^
            4. ^^^**Execute the**^^^ `**system_info.sh**` ^^^**script.**^^^
                - 
                - ^^^Run your comprehensive script. It will gather system information using different approaches and save the results to separate files.^^^
                - `./system_info.sh`^^^ ^^^
                - ^^^You should see output in your terminal indicating the script's progress:^^^
                - ```
Gathering basic system information...
Information saved to /home/labex/project/output-basic.txt
-----------------------------------------------------
Gathering detailed system information...
Information saved to /home/labex/project/output-detailed.txt
-----------------------------------------------------
Script execution complete.
```^^^ ^^^
            5. ^^^**Review the generated output files.**^^^
                - 
                - ^^^Check the content of the^^^ `output-basic.txt` ^^^and^^^ `output-detailed.txt` ^^^files in your^^^ `~/project` ^^^directory to verify that the script collected the information as expected.^^^
                - ```
cat
``````
 ~/project/output-basic.txt

``````
cat
``````
 ~/project/output-detailed.txt
```^^^ ^^^
                - ^^^The content of each file should be similar to this (actual values will vary):^^^
                - ^^^**output-basic.txt:**^^^
                - ```
### Hostname Information ###
684791f71c0e35fea6cc1243

### CPU Information ###
CPU op-mode(s):                     32-bit, 64-bit
CPU(s):                             4
CPU family:                         6

### Users with Bash Shell ###
root:x:0:0:root:/root:/bin/bash
labex:x:1000:1000::/home/labex:/bin/bash

### Basic System Info ###
5.4.0-162-generic
```^^^ ^^^
                - ^^^**output-detailed.txt:**^^^
                - ```
### Hostname Information ###
684791f71c0e35fea6cc1243

### CPU Information ###
CPU op-mode(s):                     32-bit, 64-bit
CPU(s):                             4
CPU family:                         6

### Users with Bash Shell ###
root:x:0:0:root:/root:/bin/bash
labex:x:1000:1000::/home/labex:/bin/bash

### Detailed System Info ###
Linux 684791f71c0e35fea6cc1243 5.4.0-162-generic #179-Ubuntu SMP Mon Aug 14 08:51:31 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```^^^ ^^^
                - ^^^This final script demonstrates how you can combine various Bash features and Linux commands to create powerful automation tools for system administration tasks.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, you learned the fundamental steps of creating and executing Bash scripts for RHEL system administration. You began by setting up a dedicated directory for scripts and then crafted a simple Bash script, understanding the importance of the shebang line and using the^^^ `echo` ^^^command. You explored different methods of executing scripts, including directly with the^^^ `bash` ^^^interpreter and by making them executable.^^^
        - ^^^Furthermore, you enhanced your scripting skills by incorporating system commands and automating tasks using^^^ `for` ^^^loops to gather system information with different approaches. You also learned how to filter command output effectively using^^^ `grep` ^^^and regular expressions, a crucial skill for parsing system information. Finally, you applied these concepts to build a comprehensive RHEL system information script, demonstrating how to combine various commands and scripting constructs to gather and present valuable system data.^^^
    2. **Schedule Tasks in Red Hat Enterprise Linux**
        - Schedule a one-time job with 'at'
        - Manage 'at' jobs
        - Schedule recurring user jobs with 'crontab'
        - Manage user 'crontab' entries
        - Schedule recurring system jobs with cron directories
        - Configure systemd timers for recurring tasks
        - Manage temporary files with systemd-tmpfiles
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain practical experience in scheduling tasks on RHEL systems using various tools. You will learn to schedule one-time jobs with the^^^ `at` ^^^command, manage recurring user-specific tasks using^^^ `crontab`^^^, and configure system-wide recurring jobs with cron directories.^^^
        - ^^^Furthermore, this lab will cover advanced scheduling techniques using^^^ `systemd` ^^^timers for more robust and flexible task automation, and demonstrate how to manage temporary files efficiently with^^^ `systemd-tmpfiles`^^^. By the end of this lab, you will be proficient in choosing the appropriate scheduling method for different scenarios and effectively managing automated tasks in a RHEL environment.^^^
        - ^^^This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a^^^ ^^^intermediate^^^ ^^^level lab with a^^^ ^^^75%^^^ ^^^completion rate. It has received a^^^ ^^^60%^^^ ^^^positive review rate from learners.^^^
        - 
        - # ^^^**Schedule a one-time job with 'at'**^^^
        - ^^^In this step, you will learn how to schedule a job to run once at a future time using the^^^ `at` ^^^command. The^^^ `at` ^^^command is useful for executing commands that do not need to be run repeatedly. We will schedule a simple job, inspect its details, and then remove it.^^^
        - ^^^In this lab, we will work directly on the local system to learn task scheduling. All commands will be executed in your current terminal environment.^^^
        - ^^^Let's schedule a job to print the current date and time into a file named^^^ `~/myjob.txt` ^^^in your home directory. We'll schedule it to run 3 minutes from now:^^^
        - ```
at now + 3 minutes << 
``````
EOF
date > ~/myjob.txt
EOF
``````
(#98c379)
```^^^ ^^^
        - ^^^The^^^ `warning: commands will be executed using /bin/sh` ^^^message is normal. The^^^ `job N at ...` ^^^output indicates the job number and the scheduled execution time. Make a note of the job number, as you will need it later.^^^
        - ^^^Next, let's schedule another job interactively. This method is useful for entering multiple commands or more complex scripts. We will schedule a job to append "Hello from at job!" to^^^ `~/at_output.txt` ^^^5 minutes from now:^^^
        - `at now + 5 minutes`^^^ ^^^
        - ^^^After typing the command and pressing Enter, you will see an^^^ `at>` ^^^prompt. Type your command and then press^^^ `Ctrl+d` ^^^to finish:^^^
        - ```
at > 
``````
echo
``````
 
``````
"Hello from at job!"
``````
(#98c379) >> ~/at_output.txt
at > Ctrl+d
```^^^ ^^^
        - ^^^To view the jobs currently in the^^^ `at` ^^^queue, use the^^^ `atq` ^^^command. This command lists all pending^^^ `at` ^^^jobs for the current user.^^^
        - `atq`^^^ ^^^
        - ^^^The output will show the job number, the scheduled time, the queue, and the user who scheduled it.^^^
        - ![](https://remnote-user-data.s3.amazonaws.com/L-3FXuGCKTDdTZdz_XXjyKoNaD_CvP7-MS1fLN02jQCN5k1qvap4F1rrcl55yQMXJ7Fsm7cGB-hKvWB9CkyVEa_B3qEnBgRF67MRFJz1NGOi4Ikagw5F2RxH_Cu7eBZA.png)
        - ^^^You can inspect the commands that a specific^^^ `at` ^^^job will run using the^^^ `at -c` ^^^command followed by the job number. Replace^^^ `N` ^^^with one of the job numbers you noted earlier.^^^
        - `at -c N`^^^ ^^^
        - ^^^This command will display the shell script that^^^ `at` ^^^will execute for that job. You should see the^^^ `date > ~/myjob.txt` ^^^or^^^ `echo "Hello from at job!" >> ~/at_output.txt` ^^^command within the output.^^^
        - ^^^Finally, to remove a scheduled^^^ `at` ^^^job, use the^^^ `atrm` ^^^command followed by the job number. Let's remove the first job we scheduled. Replace^^^ `N` ^^^with the job number of your first job.^^^
        - `atrm N`^^^ ^^^
        - ^^^After removing the job, you can use^^^ `atq` ^^^again to verify that it is no longer in the queue.^^^
        - `atq`^^^ ^^^
        - ^^^You should now only see the second job (if it hasn't executed yet) or an empty queue if both jobs have been removed or executed.^^^
        - ^^^This completes the first step of scheduling one-time jobs with the^^^ `at` ^^^command.^^^
        - 
        - # ^^^**Manage 'at' jobs**^^^
        - ^^^In this step, you will delve deeper into managing^^^ `at` ^^^jobs, including scheduling jobs with different queues and verifying their execution. Understanding^^^ `at` ^^^queues can be useful for prioritizing tasks or separating different types of one-time jobs.^^^
        - ^^^We will continue working on the local system to explore more advanced^^^ `at` ^^^job management features.^^^
        - ^^^The^^^ `at` ^^^command allows you to specify a queue using the^^^ `-q` ^^^option. Queues are single letters from^^^ `a` ^^^to^^^ `z`^^^. Queue^^^ `a` ^^^is the default, and jobs in queues^^^ `a` ^^^through^^^ `z` ^^^are executed with decreasing niceness (priority). Queue^^^ `a` ^^^has the highest priority, and queue^^^ `z` ^^^has the lowest. Queue^^^ `b` ^^^is reserved for batch jobs.^^^
        - ^^^Let's schedule a job in queue^^^ `g` ^^^(a lower priority queue) to run in 2 minutes. This job will create a file named^^^ `~/queue_g_job.txt` ^^^with a timestamp:^^^
        - ```
at -q g now + 2 minutes << 
``````
EOF
date > ~/queue_g_job.txt
EOF
``````
(#98c379)
```^^^ ^^^
        - ^^^You will see output similar to^^^ `job N at ...`^^^. Note down this job number.^^^
        - ^^^Next, let's schedule another job, this time in queue^^^ `b` ^^^(batch queue), which is typically used for jobs that can run when system load is low. This job will append "Batch job executed!" to^^^ `~/batch_job.txt`^^^. We'll schedule it to run 4 minutes from now:^^^
        - ```
at -q b now + 4 minutes << 
``````
EOF
echo "Batch job executed!" >> ~/batch_job.txt
EOF
``````
(#98c379)
```^^^ ^^^
        - ^^^Again, note down the job number.^^^
        - ^^^To see all pending jobs, including those in different queues, use^^^ `atq`^^^.^^^
        - `atq`^^^ ^^^
        - ^^^You should now see both jobs listed, with their respective queue letters (^^^`g``(#3594f7)` ^^^and^^^ `b``(#3594f7)`^^^).^^^
        - ![](https://remnote-user-data.s3.amazonaws.com/K3r41agDOPkvwnPQvq-7XP8j9zfaCPDYkz9Wq2-2OF64Bzqaeu9SzlFX2592Ri7jru2fIh0SxuejEOiRtRHU5cOA5GY-GqdULbr5l87c-CCXWkqDhCQ3vFFk3YTCHgr4.png)
        - ^^^Now, wait for your scheduled jobs to execute. Wait for at least 5 minutes to allow all jobs to complete. You can check if the files created by your^^^ `at` ^^^jobs exist and contain the expected content.^^^
        - ^^^Check^^^ `~/queue_g_job.txt`^^^:^^^
        - `cat`` ~/queue_g_job.txt`^^^ ^^^
        - ^^^You should see a date and time string.^^^
        - ^^^Check^^^ `~/batch_job.txt`^^^:^^^
        - `cat`` ~/batch_job.txt`^^^ ^^^
        - ^^^You should see "Batch job executed!".^^^
        - ^^^If the files are not present or empty, it might mean the jobs haven't executed yet, or there was an issue with the command. You can re-check^^^ `atq` ^^^to see if they are still pending.^^^
        - ^^^This completes the advanced^^^ `at` ^^^job management step. The remaining^^^ `at` ^^^jobs will be automatically cleaned up when the container is destroyed.^^^
        - 
        - # ^^^**Schedule recurring user jobs with 'crontab'**^^^
        - ^^^In this step, you will learn how to schedule recurring tasks for a specific user using^^^ `crontab`^^^. Unlike^^^ `at` ^^^jobs, which run once,^^^ `cron` ^^^jobs run repeatedly at specified intervals. This is ideal for routine maintenance, data backups, or generating reports.^^^
        - ^^^We will continue working on the local system to learn about user crontab management.^^^
        - ^^^The^^^ `crontab` ^^^command allows users to create, edit, and view their own^^^ `cron` ^^^jobs. Each user has their own^^^ `crontab` ^^^file.^^^
        - ^^^To edit your^^^ `crontab` ^^^file, use the^^^ `crontab -e` ^^^command. This will open your^^^ `crontab` ^^^file in the default text editor (usually^^^ `vim`^^^).^^^
        - `crontab -e`^^^ ^^^
        - ^^^**Vim editor instructions:**^^^
            - ^^^Press^^^ `i` ^^^to enter insert mode (you'll see^^^ `-- INSERT --` ^^^at the bottom)^^^
            - ^^^Use arrow keys to navigate^^^
            - ^^^To save and exit: Press^^^ `Esc` ^^^to exit insert mode, then type^^^ `:wq` ^^^and press^^^ `Enter`
            - ^^^To exit without saving: Press^^^ `Esc`^^^, then type^^^ `:q!` ^^^and press^^^ `Enter`
        - ^^^Inside the editor, you will add a new line to define your^^^ `cron` ^^^job. A^^^ `cron` ^^^entry has five time-and-date fields, followed by the command to be executed. The fields are:^^^
            - ^^^**Minute (0-59)**^^^
            - ^^^**Hour (0-23)**^^^
            - ^^^**Day of Month (1-31)**^^^
            - ^^^**Month (1-12)**^^^
            - ^^^**Day of Week (0-7, where 0 or 7 is Sunday)**^^^
        - ^^^You can use^^^ `*` ^^^as a wildcard to mean "every" for a field, or^^^ `/` ^^^to specify step values (e.g.,^^^ `*/5` ^^^for every 5 minutes).^^^
        - ^^^Let's schedule a job that appends the current date and time to a file named^^^ `~/my_cron_log.txt` ^^^every minute. This will allow us to quickly observe the^^^ `cron` ^^^job in action.^^^
        - ^^^Follow these steps in vim:^^^
            1. ^^^Press^^^ `i` ^^^to enter insert mode^^^
            2. ^^^Add the following line to the^^^ `crontab` ^^^file:^^^
        - `* * * * * /usr/bin/date >> ~/my_cron_log.txt`^^^ ^^^
            1. ^^^Press^^^ `Esc` ^^^to exit insert mode^^^
            2. ^^^Type^^^ `:wq` ^^^and press^^^ `Enter` ^^^to save and exit^^^
        - ^^^You should see a message indicating that a new^^^ `crontab` ^^^has been installed:^^^
        - `crontab: installing new crontab`^^^ ^^^
        - ^^^To verify that your^^^ `cron` ^^^job has been successfully added, you can list your^^^ `crontab` ^^^entries using the^^^ `crontab -l` ^^^command:^^^
        - `crontab -l`^^^ ^^^
        - ^^^You should see the line you just added:^^^
        - `* * * * * /usr/bin/date >> ~/my_cron_log.txt`^^^ ^^^
        - ^^^Now, wait for a minute or two to allow the^^^ `cron` ^^^job to execute at least once. You can check the current time to see when the next minute mark will occur:^^^
        - `date`^^^ ^^^
        - ^^^After waiting for at least two minutes to allow the cron job to execute a couple of times, check the content of the^^^ `~/my_cron_log.txt` ^^^file.^^^
        - `cat`` ~/my_cron_log.txt`^^^ ^^^
        - ^^^You should see one or more lines, each containing a date and time, indicating that your^^^ `cron` ^^^job has executed.^^^
        - ```
Mon Apr 8 10:30:01 AM EDT 2024
Mon Apr 8 10:31:01 AM EDT 2024
```^^^ ^^^
        - ![](https://remnote-user-data.s3.amazonaws.com/uZHlaxAzyInv-Q2NCmvSC0Z80sq9ke4T2eMWDZ1skjNq-eXnSb0BtAa9ctBzV-wMLIHXCHxBQCWyDzzECA5bRBxquws05ybRI9g0wn0lkrNNYBrOUHg5K-h5HF9iWVsu.png)
        - ^^^This completes the user crontab management step. The cron job will continue running until the container is destroyed.^^^
        - 
        - # ^^^**Manage user 'crontab' entries**^^^
        - ^^^In this step, you will learn more advanced techniques for managing user^^^ `crontab` ^^^entries, including editing existing jobs, adding multiple jobs, and understanding special^^^ `cron` ^^^strings. Effective^^^ `crontab` ^^^management is crucial for automating routine tasks.^^^
        - ^^^We will continue working on the local system to explore advanced crontab management techniques.^^^
        - ^^^Let's start by adding a new^^^ `cron` ^^^job. This job will append "Hello from cron!" to^^^ `~/cron_messages.txt` ^^^every two minutes.^^^
        - ^^^Open your^^^ `crontab` ^^^for editing:^^^
        - `crontab -e`^^^ ^^^
        - ^^^In vim:^^^
            1. ^^^Press^^^ `i` ^^^to enter insert mode^^^
            2. ^^^Add the following line to the^^^ `crontab` ^^^file:^^^
        - `*/2 * * * * ``echo`` ``"Hello from cron!"``(#98c379)`` >> ~/cron_messages.txt`^^^ ^^^
            1. ^^^Press^^^ `Esc` ^^^to exit insert mode^^^
            2. ^^^Type^^^ `:wq` ^^^and press^^^ `Enter` ^^^to save and exit^^^
        - ^^^Verify the entry is added:^^^
        - `crontab -l`^^^ ^^^
        - ^^^You should see the newly added line.^^^
        - ^^^Now, let's add another^^^ `cron` ^^^job that runs daily at 08:00 AM. This job will record the disk usage of your home directory to^^^ `~/disk_usage.log`^^^.^^^
        - ^^^Open your^^^ `crontab` ^^^for editing again:^^^
        - `crontab -e`^^^ ^^^
        - ^^^In vim:^^^
            1. ^^^Press^^^ `i` ^^^to enter insert mode^^^
            2. ^^^Add the following line below the previous one:^^^
        - `0 8 * * * ``du`` -sh ~ >> ~/disk_usage.log`^^^ ^^^
            1. ^^^Press^^^ `Esc` ^^^to exit insert mode^^^
            2. ^^^Type^^^ `:wq` ^^^and press^^^ `Enter` ^^^to save and exit^^^
        - ^^^Verify both entries are present:^^^
        - `crontab -l`^^^ ^^^
        - ^^^You should now see both^^^ `cron` ^^^jobs listed.^^^
        - `cron` ^^^also supports special strings that can simplify common schedules. These include^^^ `@reboot`^^^,^^^ `@yearly`^^^,^^^ `@annually`^^^,^^^ `@monthly`^^^,^^^ `@weekly`^^^,^^^ `@daily`^^^,^^^ `@midnight`^^^, and^^^ `@hourly`^^^. For example,^^^ `@hourly` ^^^is equivalent to^^^ `0 * * * *`^^^.^^^
        - ^^^Let's add a job that runs hourly and records the system uptime to^^^ `~/uptime_log.txt`^^^.^^^
        - ^^^Open your^^^ `crontab` ^^^for editing:^^^
        - `crontab -e`^^^ ^^^
        - ^^^In vim:^^^
            1. ^^^Press^^^ `i` ^^^to enter insert mode^^^
            2. ^^^Add the following line:^^^
        - `@hourly ``uptime`` >> ~/uptime_log.txt`^^^ ^^^
            1. ^^^Press^^^ `Esc` ^^^to exit insert mode^^^
            2. ^^^Type^^^ `:wq` ^^^and press^^^ `Enter` ^^^to save and exit^^^
        - ^^^Verify all three entries:^^^
        - `crontab -l`^^^ ^^^
        - ^^^You should now see all three^^^ `cron` ^^^jobs.^^^
        - ^^^To demonstrate the effect of these jobs, we will wait for a short period. Since the jobs are scheduled at different intervals, we won't see all of them execute immediately, but we can verify the setup.^^^
        - ^^^Wait for at least 3 minutes to allow the^^^ `*/2` ^^^job to run at least once.^^^
        - ^^^Check the^^^ `~/cron_messages.txt` ^^^file:^^^
        - `cat`` ~/cron_messages.txt`^^^ ^^^
        - ^^^You should see at least one "Hello from cron!" message.^^^
        - `Hello from cron!`^^^ ^^^
        - ^^^The^^^ `~/disk_usage.log` ^^^and^^^ `~/uptime_log.txt` ^^^files might not be created yet, depending on the current time, as they are scheduled for daily and hourly execution respectively. The important part is that their entries are correctly configured in your^^^ `crontab`^^^.^^^
        - ^^^This completes the user crontab management step. All cron jobs will continue running until the container is destroyed.^^^
        - 
        - # ^^^**Schedule recurring system jobs with cron directories**^^^
        - ^^^In this step, you will learn how to schedule recurring system-wide tasks using^^^ `cron` ^^^directories. Unlike user^^^ `crontab` ^^^entries, which are specific to a user, system^^^ `cron` ^^^jobs are managed by the root user and affect the entire system. These are typically used for system maintenance, log rotation, and other administrative tasks.^^^
        - ^^^We will continue working on the local system to explore system-wide cron job configuration.^^^
        - ^^^System-wide^^^ `cron` ^^^jobs are defined in^^^ `/etc/crontab` ^^^or by placing scripts in specific directories:^^^
            - `/etc/cron.hourly/`^^^: Scripts in this directory run once an hour.^^^
            - `/etc/cron.daily/`^^^: Scripts in this directory run once a day.^^^
            - `/etc/cron.weekly/`^^^: Scripts in this directory run once a week.^^^
            - `/etc/cron.monthly/`^^^: Scripts in this directory run once a month.^^^
        - ^^^These directories are processed by the^^^ `run-parts` ^^^utility, which executes all executable files within them.^^^
        - ^^^To manage system^^^ `cron` ^^^jobs, you need root privileges. Since the labex user has sudo access, we can use^^^ `sudo` ^^^for the required commands.^^^
        - ^^^Let's create a simple script that logs a message to the system log. We will place this script in^^^ `/etc/cron.hourly/` ^^^to make it run hourly.^^^
        - ^^^First, create the script file^^^ `/etc/cron.hourly/my_hourly_script`^^^:^^^
        - `sudo nano /etc/cron.hourly/my_hourly_script`^^^ ^^^
        - ^^^Add the following content to the file:^^^
        - ```
#!/bin/bash
``````
(#61aeee)
logger 
``````
"Hourly cron job executed at 
``````
(#98c379)
``````
$(date)
``````
(#e06c75)
``````
"
``````
(#98c379)
```^^^ ^^^
        - ^^^Save and exit the editor (^^^`Ctrl+o``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^,^^^ `Ctrl+x``(#3594f7)` ^^^in^^^ `nano``(#3594f7)`^^^).^^^
        - ^^^Next, you need to make the script executable. Without execute permissions,^^^ `run-parts` ^^^will ignore it.^^^
        - `sudo ``chmod`` +x /etc/cron.hourly/my_hourly_script`^^^ ^^^
        - ^^^Now, let's verify that the script is executable:^^^
        - `ls`` -l /etc/cron.hourly/my_hourly_script`^^^ ^^^
        - ^^^You should see^^^ `x` ^^^in the permissions, for example:^^^ `-rwxr-xr-x`^^^.^^^
        - ^^^Since^^^ `cron.hourly` ^^^jobs run once an hour, we can't wait for a full hour to verify its execution in this lab. However, we can manually trigger the^^^ `run-parts` ^^^command for the hourly directory to simulate its execution.^^^
        - `sudo run-parts /etc/cron.hourly/`^^^ ^^^
        - ^^^This command will execute all executable scripts in^^^ `/etc/cron.hourly/`^^^. The script we created uses the^^^ `logger` ^^^command to write messages to the system log. While we cannot easily verify the log output in this container environment, the important learning objective is understanding how to create and manage scripts in the cron directories.^^^
        - ^^^In a real RHEL system, you would be able to check the system logs using^^^ `journalctl` ^^^or^^^ `/var/log/messages` ^^^to verify that the script executed successfully.^^^
        - ^^^This completes the system cron job management step. The script will remain in place and would execute hourly in a real system environment.^^^
        - 
        - # ^^^**Configure systemd timers for recurring tasks**^^^
        - ^^^In this step, you will learn about^^^ `systemd` ^^^timers, which are a modern alternative to^^^ `cron` ^^^for scheduling tasks on Linux systems.^^^ `systemd` ^^^timers offer more flexibility and better integration with the^^^ `systemd` ^^^ecosystem. While^^^ `systemctl` ^^^commands are typically used to manage^^^ `systemd` ^^^units, due to the Docker container environment, we will focus on creating and verifying the timer and service unit files directly.^^^
        - `systemd` ^^^timers work in conjunction with^^^ `systemd` ^^^service units. A timer unit (^^^`.timer` ^^^file) defines when a task should run, and a service unit (^^^`.service` ^^^file) defines what task should be executed.^^^
        - ^^^We will continue working on the local system to explore systemd timers configuration.^^^
        - ^^^You will need root privileges to create^^^ `systemd` ^^^unit files in system directories. Since the labex user has sudo access, we can use^^^ `sudo` ^^^for the required commands.^^^
        - ^^^Let's create a simple service that logs a message to a file. We will place this service unit file in^^^ `/etc/systemd/system/` ^^^which is where custom service units are typically stored.^^^
        - ^^^Create the service unit file^^^ `/etc/systemd/system/my-custom-task.service`^^^:^^^
        - `sudo nano /etc/systemd/system/my-custom-task.service`^^^ ^^^
        - ^^^Add the following content to the file:^^^
        - ```
[Unit]
``````
(#e06c75)

``````
Description
``````
(#d19a66)=My Custom Scheduled Task


``````
[Service]
``````
(#e06c75)

``````
Type
``````
(#d19a66)=
``````
on
``````
(#56b6c2)eshot

``````
ExecStart
``````
(#d19a66)=/bin/bash -c 
``````
'echo "My custom task executed at $(date)" >> /var/log/my-custom-task.log'
``````
(#98c379)
```^^^ ^^^
        - ^^^Save and exit the editor (^^^`Ctrl+o``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^,^^^ `Ctrl+x``(#3594f7)` ^^^in^^^ `nano``(#3594f7)`^^^).^^^
        - ^^^Next, create the timer unit file^^^ `/etc/systemd/system/my-custom-task.timer`^^^. This timer will activate our service every 5 minutes.^^^
        - `sudo nano /etc/systemd/system/my-custom-task.timer`^^^ ^^^
        - ^^^Add the following content to the file:^^^
        - ```
[Unit]
``````
(#e06c75)

``````
Description
``````
(#d19a66)=Run My Custom Scheduled Task every 
``````
5
``````
(#d19a66) minutes


``````
[Timer]
``````
(#e06c75)

``````
OnCalendar
``````
(#d19a66)=*:
``````
0
``````
(#d19a66)/
``````
5
``````
(#d19a66)

``````
Persistent
``````
(#d19a66)=
``````
true
``````
(#56b6c2)


``````
[Install]
``````
(#e06c75)

``````
WantedBy
``````
(#d19a66)=timers.target
```^^^ ^^^
        - ^^^Save and exit the editor.^^^
        - ^^^**Explanation of**^^^ `**OnCalendar**`^^^**:**^^^
            - `*:0/5` ^^^means "every 5 minutes".^^^
                - `*` ^^^for year, month, day, hour (any value).^^^
                - `0/5` ^^^for minute, meaning starting at minute 0, every 5 minutes (0, 5, 10, ..., 55).^^^
        - ^^^In a typical^^^ `systemd` ^^^environment, you would now run^^^ `systemctl daemon-reload` ^^^to make^^^ `systemd` ^^^aware of the new unit files, and then^^^ `systemctl enable --now my-custom-task.timer` ^^^to start the timer. However, due to Docker container limitations,^^^ `systemctl` ^^^is not fully functional.^^^
        - ^^^Instead, we will manually verify the creation of the files. The^^^ `systemd` ^^^daemon inside the container might pick up these files eventually, but we cannot directly control or observe its timer execution in this lab setup. The primary goal here is to understand how to^^^  ^^^ *configure* ^^^^^^ ^^^ ^^^these files.^^^
        - ^^^Let's verify the existence of the created files:^^^
        - ```
ls
``````
 -l /etc/systemd/system/my-custom-task.service

``````
ls
``````
 -l /etc/systemd/system/my-custom-task.timer
```^^^ ^^^
        - ^^^You should see output indicating that both files exist.^^^
        - ^^^To simulate the execution of the service, you can manually run the command defined in^^^ `ExecStart`^^^:^^^
        - `sudo /bin/bash -c ``'echo "My custom task executed at $(date)" >> /var/log/my-custom-task.log'``(#98c379)`^^^ ^^^
        - ^^^Now, check the log file to see the output:^^^
        - `sudo ``cat`` /var/log/my-custom-task.log`^^^ ^^^
        - ^^^You should see the message you just logged:^^^
        - `My custom task executed at Tue Jun 10 06:54:40 UTC 2025`^^^ ^^^
        - ^^^This completes the systemd timer configuration step. The service and timer unit files will remain in place for reference.^^^
        - 
        - # ^^^**Manage temporary files with systemd-tmpfiles**^^^
        - ^^^In this step, you will learn how to manage temporary files and directories using^^^ `systemd-tmpfiles`^^^. This utility is part of^^^ `systemd` ^^^and is responsible for creating, deleting, and cleaning up volatile and temporary files and directories. It's commonly used to manage^^^ `/tmp`^^^,^^^ `/var/tmp`^^^, and other temporary storage locations, ensuring that old files are removed periodically.^^^
        - ^^^We will continue working on the local system to explore systemd-tmpfiles configuration.^^^
        - ^^^You will need root privileges to configure^^^ `systemd-tmpfiles`^^^. Since the labex user has sudo access, we can use^^^ `sudo` ^^^for the required commands.^^^
        - `systemd-tmpfiles` ^^^reads configuration files from^^^ `/etc/tmpfiles.d/` ^^^and^^^ `/usr/lib/tmpfiles.d/`^^^. These files define rules for creating, deleting, and managing files and directories.^^^
        - ^^^Let's create a custom configuration file to manage a new temporary directory. We will create a directory^^^ `/run/my_temp_dir` ^^^and configure^^^ `systemd-tmpfiles` ^^^to clean files older than 1 minute from it.^^^
        - ^^^Create the configuration file^^^ `/etc/tmpfiles.d/my_temp_dir.conf`^^^:^^^
        - `sudo nano /etc/tmpfiles.d/my_temp_dir.conf`^^^ ^^^
        - ^^^Add the following content to the file:^^^
        - `d /run/my_temp_dir 0755 labex labex 1m`^^^ ^^^
        - ^^^**Explanation of the line:**^^^
            - `d`^^^: Specifies that this entry defines a directory.^^^
            - `/run/my_temp_dir`^^^: The path to the directory.^^^
            - `0755`^^^: The permissions for the directory.^^^
            - `labex labex`^^^: The owner and group for the directory.^^^
            - `1m`^^^: The age after which files in this directory should be deleted (1 minute).^^^
        - ^^^Save and exit the editor (^^^`Ctrl+o``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^,^^^ `Ctrl+x``(#3594f7)` ^^^in^^^ `nano``(#3594f7)`^^^).^^^
        - ^^^Now, let's tell^^^ `systemd-tmpfiles` ^^^to apply this configuration. The^^^ `--create` ^^^option will create the directory if it doesn't exist.^^^
        - `sudo systemd-tmpfiles --create /etc/tmpfiles.d/my_temp_dir.conf`^^^ ^^^
        - ^^^Verify that the directory has been created with the correct permissions and ownership:^^^
        - `ls`` -ld /run/my_temp_dir`^^^ ^^^
        - ^^^You should see output similar to:^^^
        - `drwxr-xr-x 2 labex labex 6 Jun 10 06:55 /run/my_temp_dir`^^^ ^^^
        - ^^^Next, let's create a test file inside this new temporary directory:^^^
        - `sudo ``touch`` /run/my_temp_dir/test_file.txt`^^^ ^^^
        - ^^^Verify the file exists:^^^
        - `ls`` -l /run/my_temp_dir/test_file.txt`^^^ ^^^
        - ^^^Now, we need to wait for more than 1 minute for the file to become "old" according to our configuration. Wait for at least 70 seconds (1 minute and 10 seconds).^^^
        - ^^^After waiting for more than 1 minute, we will manually run^^^ `systemd-tmpfiles` ^^^with the^^^ `--clean` ^^^option to trigger the cleanup process based on our configuration.^^^
        - `sudo systemd-tmpfiles --clean /etc/tmpfiles.d/my_temp_dir.conf`^^^ ^^^
        - ^^^Finally, check if the^^^ `test_file.txt` ^^^has been removed:^^^
        - `ls`` -l /run/my_temp_dir/test_file.txt`^^^ ^^^
        - ^^^You should get a "No such file or directory" error, indicating that^^^ `systemd-tmpfiles` ^^^successfully cleaned up the old file.^^^
        - ^^^This completes the systemd-tmpfiles configuration step. The configuration file and temporary directory will remain in place for reference.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, you learned how to schedule and manage one-time tasks using the^^^ `at` ^^^command, including scheduling jobs interactively and non-interactively, viewing the^^^ `at` ^^^queue with^^^ `atq`^^^, and deleting pending jobs with^^^ `atrm`^^^. You also gained proficiency in scheduling recurring user-specific tasks using^^^ `crontab`^^^, covering how to edit, list, and remove cron jobs, and understanding the cron syntax for specifying execution times. Furthermore, the lab demonstrated how to schedule system-wide recurring tasks by placing scripts in standard cron directories (^^^`/etc/cron.hourly`^^^,^^^ `/etc/cron.daily`^^^, etc.) and how to create custom cron jobs in^^^ `/etc/cron.d`^^^.^^^
        - ^^^Finally, you explored advanced task scheduling with^^^ `systemd` ^^^timers, learning to create and enable service and timer units for recurring tasks, and how to manage temporary files and directories using^^^ `systemd-tmpfiles` ^^^for automated cleanup. This comprehensive lab provided practical experience in managing diverse task scheduling needs on RHEL systems, from simple one-off commands to complex recurring system processes.^^^
        - 
        - 
    3. **Tune System Performance in RHEL**
        - Verify tuned Status and List Available Profiles
        - Change tuned Profile and Observe System Parameter Changes
        - Start and Monitor CPU-Intensive Processes on RHEL
        - Adjust Process Priority with nice and renice on RHEL
        - Clean Up Running Processes
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will learn how to optimize RHEL system performance using^^^ `tuned` ^^^and manage process priorities with^^^ `nice` ^^^and^^^ `renice`^^^. You will begin by verifying^^^ `tuned` ^^^installation and listing available profiles, then observe how changing^^^ `tuned` ^^^profiles impacts system parameters.^^^
        - ^^^The lab will guide you through starting and monitoring CPU-intensive processes, followed by adjusting their priorities using^^^ `nice` ^^^and^^^ `renice` ^^^to understand their effect on resource allocation. Finally, you will learn how to clean up running processes, ensuring a complete understanding of performance tuning on RHEL.^^^
        - 
        - # ^^^**Verify tuned Status and List Available Profiles**^^^
        - ^^^In this step, you will learn how to verify the status of the^^^ `tuned` ^^^daemon and list available tuning profiles on your RHEL system.^^^ `tuned` ^^^is a dynamic adaptive system tuning daemon that tunes system settings to optimize performance for specific workloads. It uses tuning profiles to apply a set of system-wide settings.^^^
            1. ^^^**Verify that the**^^^ `**tuned**` ^^^**daemon is running**^^^^^^.^^^
                - 
                - ^^^In this container environment, we'll check if the^^^ `tuned` ^^^daemon is running by looking for its process. We can also verify its functionality by checking if it responds to commands.^^^
                - ^^^First, check if the^^^ `tuned` ^^^process is running:^^^
                - `pgrep tuned`^^^ ^^^
                - ^^^If^^^ `tuned` ^^^is running, this command will return its Process ID (PID). If no PID is returned, you can start the daemon manually:^^^
                - `sudo /usr/sbin/tuned &`^^^ ^^^
                - ^^^Then verify it's running:^^^
                - `pgrep tuned`^^^ ^^^
                - ^^^You should see output similar to:^^^
                - `739`^^^ ^^^
                - ^^^ *(Note: The PID value in your output will vary.)* ^^^
                - ^^^Additionally, you can verify that^^^ `tuned` ^^^is functional by checking if it responds to status queries:^^^
                - `sudo tuned-adm active`^^^ ^^^
                - ^^^This should return the currently active profile without errors.^^^
            2. ^^^**List the available tuning profiles and identify the active profile**^^^^^^.^^^
                - 
                - ^^^The^^^ `tuned-adm list` ^^^command displays all available tuning profiles and highlights the currently active one.^^^
                - `sudo tuned-adm list`^^^ ^^^
                - ^^^You will be prompted for your password. Note the^^^ `Current active profile` ^^^in the output.^^^
                - ```
Available profiles:
- accelerator-performance     - Throughput performance based tuning with disabled higher latency STOP states
- aws                         - Optimize for aws ec2 instances
- balanced                    - General non-specialized tuned profile
- balanced-battery            - Balanced profile biased towards power savings changes for battery
- desktop                     - Optimize for the desktop use-case
- hpc-compute                 - Optimize for HPC compute workloads
- intel-sst                   - Configure for Intel Speed Select Base Frequency
- latency-performance         - Optimize for deterministic performance at the cost of increased power consumption
- network-latency             - Optimize for deterministic performance at the cost of increased power consumption, focused on low latency network performance
- network-throughput          - Optimize for streaming network throughput, generally only necessary on older CPUs or 40G+ networks
- optimize-serial-console     - Optimize for serial console use.
- powersave                   - Optimize for low power consumption
- throughput-performance      - Broadly applicable tuning that provides excellent performance across a variety of common server workloads
- virtual-guest               - Optimize for running inside a virtual guest
- virtual-host                - Optimize for running KVM guests
Current active profile: virtual-guest
```^^^ ^^^
            3. ^^^**Review the**^^^ `**virtual-guest**` ^^^**profile configuration**^^^^^^.^^^
                - 
                - ^^^The^^^ `virtual-guest` ^^^profile is often the default for virtual machines. You can inspect its configuration file to understand what settings it applies.^^^
                - `cat`` /usr/lib/tuned/virtual-guest/tuned.conf`^^^ ^^^
                - ^^^This command shows the^^^ `tuned` ^^^configuration for the^^^ `virtual-guest` ^^^profile, including parameters it inherits from other profiles.^^^
                - ```
#
# tuned configuration
#

[main]
summary=Optimize for running inside a virtual guest
include=throughput-performance

[vm]
# If a workload mostly uses anonymous memory and it hits this limit, the entire
# working set is buffered for I/O, and any more write buffering would require
# swapping, so it's time to throttle writes until I/O can catch up.  Workloads
# that mostly use file mappings may be able to use even higher values.
#
# The generator of dirty data starts writeback at this percentage (system default
# is 20%)
dirty_ratio = 30

[sysctl]
# Filesystem I/O is usually much more efficient than swapping, so try to keep
# swapping low.  It's usually safe to go even lower than this on systems with
# server-grade storage.
vm.swappiness = 30
```^^^ ^^^
            4. ^^^**Verify that the**^^^ `**vm.dirty_background_ratio**` ^^^**parameter is applied**^^^^^^.^^^
                - 
                - ^^^The^^^ `virtual-guest` ^^^profile includes^^^ `throughput-performance`^^^. Let's check a parameter that^^^ `throughput-performance` ^^^typically sets, such as^^^ `vm.dirty_background_ratio`^^^. This parameter controls when the system starts writing dirty pages to disk in the background.^^^
                - `sysctl vm.dirty_background_ratio`^^^ ^^^
                - ^^^The output will show the current value of this kernel parameter.^^^
                - `vm.dirty_background_ratio = 10`^^^ ^^^
        - 
        - # ^^^**Change tuned Profile and Observe System Parameter Changes**^^^
        - ^^^In this step, you will learn how to change the active^^^ `tuned` ^^^profile and observe the immediate effects on system parameters. Changing a^^^ `tuned` ^^^profile allows you to quickly apply a set of performance optimizations tailored for different workloads, such as throughput-intensive tasks or power saving.^^^
            1. ^^^**Change the current active tuning profile to**^^^ `**throughput-performance**`^^^.^^^
                - 
                - ^^^The^^^ `throughput-performance` ^^^profile is designed for systems that require high throughput, often by sacrificing some latency. It typically optimizes for disk I/O and network performance. Use the^^^ `tuned-adm profile` ^^^command to switch profiles.^^^
                - `sudo tuned-adm profile throughput-performance`^^^ ^^^
                - ^^^You will be prompted for your password.^^^
                - ```
$ sudo tuned-adm profile throughput-performance
[sudo] password for user:
```^^^ ^^^
            2. ^^^**Confirm the new active profile**^^^^^^.^^^
                - 
                - ^^^After changing the profile, it's good practice to verify that the new profile is indeed active. You can do this using^^^ `tuned-adm active`^^^.^^^
                - `sudo tuned-adm active`^^^ ^^^
                - ^^^The output should now show^^^ `throughput-performance` ^^^as the active profile.^^^
                - `Current active profile: throughput-performance`^^^ ^^^
            3. ^^^**Verify the**^^^ `**vm.dirty_ratio**` ^^^**and**^^^ `**vm.swappiness**` ^^^**parameters have changed**^^^^^^.^^^
                - 
                - ^^^The^^^ `throughput-performance` ^^^profile modifies kernel parameters related to memory management, such as^^^ `vm.dirty_ratio` ^^^and^^^ `vm.swappiness`^^^. Even though the^^^ `virtual-guest` ^^^profile inherits from^^^ `throughput-performance`^^^, switching directly to the^^^ `throughput-performance` ^^^profile applies the base values without the virtual-guest specific modifications.^^^
                    - `vm.dirty_ratio`^^^: This parameter defines the maximum percentage of system memory that can be filled with dirty pages (pages that have been modified but not yet written to disk) before the system starts writing them to disk. A higher value can improve throughput by allowing more data to be buffered in memory.^^^
                    - `vm.swappiness`^^^: This parameter controls how aggressively the kernel swaps out anonymous memory (application data) from RAM to swap space. A lower value means the kernel will try to keep more application data in RAM, which is generally better for performance.^^^
                - ^^^Let's check their current values using^^^ `sysctl`^^^.^^^
                - ```
sysctl vm.dirty_ratio
sysctl vm.swappiness
```^^^ ^^^
                - ^^^You should observe that the values have changed from the^^^ `virtual-guest` ^^^profile settings (dirty_ratio = 30, vm.swappiness = 30) to the base^^^ `throughput-performance` ^^^profile values:^^^
                - ```
vm.dirty_ratio = 40
vm.swappiness = 10
```^^^ ^^^
                - ^^^ *(Note: These values reflect the base throughput-performance optimizations without the virtual-guest specific modifications.)* ^^^
        - 
        - # ^^^**Start and Monitor CPU-Intensive Processes on RHEL**^^^
        - ^^^In this step, you will learn how to start CPU-intensive processes and monitor their resource usage. This is crucial for understanding how processes consume system resources and how to identify bottlenecks. We will use the^^^ `sha1sum /dev/zero` ^^^command, which continuously calculates the SHA1 checksum of an endless stream of zeros, effectively consuming CPU cycles.^^^
        - ^^^**Important:**^^^ ^^^This exercise uses commands that perform endless checksums on a device file, intentionally consuming significant CPU resources.^^^ ^^^**You must terminate all exercise processes before leaving this exercise or moving to the next lab.**^^^
            1. ^^^**Determine the number of CPU cores on your system**^^^^^^.^^^
                - 
                - ^^^Understanding the number of CPU cores helps you decide how many CPU-intensive processes to run to fully utilize the system. You can find this information in^^^ `/proc/cpuinfo`^^^.^^^
                - `grep -c ``'^processor'``(#98c379)`` /proc/cpuinfo`^^^ ^^^
                - ^^^This command counts the number of lines that start with^^^ `processor`^^^, which corresponds to the number of logical CPU cores (or virtual processors).^^^
                - `2`^^^ ^^^
                - ^^^ *(Note: Your output might show a different number of cores depending on the system's configuration.)* ^^^
            2. ^^^**Start two instances of the**^^^ `**sha1sum /dev/zero &**` ^^^**command for each CPU core**^^^^^^.^^^
                - 
                - ^^^To simulate a heavily loaded system, we will start multiple instances of^^^ `sha1sum /dev/zero &`^^^. The^^^ `&` ^^^at the end of the command runs the process in the background, allowing you to continue using the terminal. For example, if you have 2 CPU cores, you would start 4 instances (2 instances/core * 2 cores).^^^
                - `for``(#c678dd)``(#1a1a1a)`` i ``(#a9b7c6)``(#1a1a1a)``in``(#c678dd)``(#1a1a1a)`` $(``(#a9b7c6)``(#1a1a1a)``seq``(#e6c07b)``(#1a1a1a)`` 1 $(grep -c ``(#a9b7c6)``(#1a1a1a)``'^processor'``(#98c379)``(#1a1a1a)`` /proc/cpuinfo | awk ``(#a9b7c6)``(#1a1a1a)``'{print $1 * 2}'``(#98c379)``(#1a1a1a)``)); ``(#a9b7c6)``(#1a1a1a)``do``(#c678dd)``(#1a1a1a) ``sha1sum``(#e6c07b)``(#1a1a1a)`` /dev/zero & ``(#a9b7c6)``(#1a1a1a)``done``(#c678dd)``(#1a1a1a)`^^^ ^^^
                - ^^^This command dynamically calculates the number of processes to start based on your CPU core count.^^^
                - ```
[1] 1234
[2] 1235
[3] 1236
[4] 1237
```^^^ ^^^
                - ^^^ *(Note: PID values in your output will vary from the example.)* ^^^
            3. ^^^**Verify that the background jobs are running**^^^^^^.^^^
                - 
                - ^^^The^^^ `jobs` ^^^command lists all processes currently running in the background from your shell session.^^^
                - `jobs`^^^ ^^^
                - ^^^You should see a list of the^^^ `sha1sum` ^^^processes you just started.^^^
                - ```
[1]   Running                 sha1sum /dev/zero &
[2]   Running                 sha1sum /dev/zero &
[3]   Running                 sha1sum /dev/zero &
[4]-  Running                 sha1sum /dev/zero &
```^^^ ^^^
            4. ^^^**Use the**^^^ `**ps**` ^^^**and**^^^ `**pgrep**` ^^^**commands to display the percentage of CPU usage for each**^^^ `**sha1sum**` ^^^**process**^^^^^^.^^^
                - 
                - ^^^The^^^ `ps` ^^^command reports a snapshot of the current processes. We will combine it with^^^ `pgrep` ^^^to filter for^^^ `sha1sum` ^^^processes.^^^
                    - `ps -o pid,pcpu,nice,comm`^^^: This specifies the output format: Process ID (^^^`pid`^^^), percentage of CPU usage (^^^`pcpu`^^^),^^^ `nice` ^^^value (^^^`nice`^^^), and command name (^^^`comm`^^^).^^^
                    - `$(pgrep sha1sum)``(#3594f7)`^^^: This command substitution finds the PIDs of all processes named^^^ `sha1sum``(#3594f7)` ^^^and passes them as arguments to^^^ `ps``(#3594f7)`^^^.^^^
                - `ps -o pid,pcpu,``nice``,``comm`` $(pgrep ``sha1sum``)`^^^ ^^^
                - ^^^You should see each^^^ `sha1sum` ^^^process consuming a significant percentage of CPU.^^^
                - ```
PID %CPU  NI COMMAND
   5248 48.8   0 sha1sum
   5249 48.7   0 sha1sum
   5250 48.8   0 sha1sum
   5251 48.8   0 sha1sum
```^^^ ^^^
                - ^^^ *(Note: The* ^^^^^^ ^^^ ` __%CPU__ ``(#3594f7)`  ^^^ *values might fluctuate but should be high, indicating heavy CPU usage. The* ^^^^^^ ^^^ ` __NI__ ``(#3594f7)`  ^^^ *column shows the nice value.)* ^^^
            5. ^^^**Terminate all running**^^^ `**sha1sum**` ^^^**processes and verify none are left**^^^^^^.^^^
                - 
                - ^^^It's crucial to clean up these CPU-intensive processes before proceeding. The^^^ `pkill` ^^^command terminates processes based on their name.^^^
                - `pkill ``sha1sum`^^^ ^^^
                - ^^^Now, verify that no^^^ `sha1sum` ^^^jobs are running in the background.^^^
                - `jobs`^^^ ^^^
                - ^^^The output should be empty, or indicate that all jobs are terminated.^^^
                - ```
[1]   Terminated              sha1sum /dev/zero
[2]   Terminated              sha1sum /dev/zero
[3]   Terminated              sha1sum /dev/zero
[4]-  Terminated              sha1sum /dev/zero
```^^^ ^^^
                - ^^^ *(Note: You might see "Terminated" messages, which is expected as the processes are being stopped.)* ^^^
        - 
        - # ^^^**Adjust Process Priority with nice and renice on RHEL**^^^
        - ^^^In this step, you will learn how to influence the scheduling priority of processes using the^^^ `nice` ^^^and^^^ `renice` ^^^commands. The^^^ `nice` ^^^value (also known as niceness) of a process indicates its priority to the Linux scheduler. A lower^^^ `nice` ^^^value (more negative) means higher priority, while a higher^^^ `nice` ^^^value (more positive) means lower priority. The range for^^^ `nice` ^^^values is typically from -20 (highest priority) to 19 (lowest priority), with 0 being the default.^^^
            1. ^^^**Start multiple instances of**^^^ `**sha1sum /dev/zero &**` ^^^**and then start one additional instance with a**^^^ `**nice**` ^^^**level of 10**^^^^^^.^^^
                - 
                - ^^^We will start several^^^ `sha1sum` ^^^processes to simulate a busy system. Then, we'll start one with a deliberately lower priority (higher^^^ `nice` ^^^value) to observe the effect.^^^
                - ^^^First, start three regular instances (adjust based on your CPU core count if desired, but at least as many as virtual processors to create contention):^^^
                - `for``(#c678dd)``(#1a1a1a)`` i ``(#a9b7c6)``(#1a1a1a)``in``(#c678dd)``(#1a1a1a)`` {1..3}; ``(#a9b7c6)``(#1a1a1a)``do``(#c678dd)``(#1a1a1a) ``sha1sum``(#e6c07b)``(#1a1a1a)`` /dev/zero & ``(#a9b7c6)``(#1a1a1a)``done``(#c678dd)``(#1a1a1a)`^^^ ^^^
                - ^^^Next, start the fourth instance with a^^^ `nice` ^^^level of 10. This process will have a lower priority compared to the others.^^^
                - `nice`` -n 10 ``sha1sum`` /dev/zero &`^^^ ^^^
                - ^^^You will see output similar to this, indicating the PIDs of the background processes:^^^
                - ```
[1] 5443
[2] 5444
[3] 5445
[4] 5446
```^^^ ^^^
                - ^^^ *(Note: PID values in your output will vary.)* ^^^
            2. ^^^**Use**^^^ `**ps**` ^^^**and**^^^ `**pgrep**` ^^^**commands to display the PID, percentage of CPU usage,**^^^ `**nice**` ^^^**value, and executable name for each process**^^^^^^.^^^
                - 
                - ^^^Observe the^^^ `%CPU` ^^^and^^^ `NI` ^^^columns. The instance with the^^^ `nice` ^^^value of 10 should display a lower percentage of CPU usage than the other instances, as the scheduler gives it less CPU time.^^^
                - `ps -o pid,pcpu,``nice``,``comm`` $(pgrep ``sha1sum``)`^^^ ^^^
                - ^^^Look for the process with^^^ `NI` ^^^value^^^ `10`^^^. Its^^^ `%CPU` ^^^should be noticeably lower than the others.^^^
                - ```
PID %CPU  NI COMMAND
   5443 56.8   0 sha1sum
   5444 58.0   0 sha1sum
   5445 56.5   0 sha1sum
   5446  6.7  10 sha1sum
```^^^ ^^^
                - ^^^ *(Note: The exact* ^^^^^^ ^^^ ` __%CPU__ ``(#3594f7)`  ^^^ *values will vary based on system load and core count, but the process with* ^^^^^^ ^^^ ` __nice 10__ ``(#3594f7)`  ^^^ *should have a lower share.)* ^^^
            3. ^^^**Use the**^^^ `**sudo renice**` ^^^**command to change the**^^^ `**nice**` ^^^**level of one of the regular processes to 5**^^^^^^.^^^
                - 
                - ^^^The^^^ `renice` ^^^command allows you to change the^^^ `nice` ^^^value of an already running process. We will demonstrate this by changing one of the regular processes (nice value 0) to a nice value of 5.^^^
                - ^^^First, identify the PID of one of the^^^ `sha1sum` ^^^processes that has a^^^ `nice` ^^^value of 0 from the output of the previous^^^ `ps` ^^^command. Let's use the first one from the example above (PID 5443).^^^
                - `sudo renice -n 5 <PID_of_regular_process>`^^^ ^^^
                - ^^^Replace^^^ `<PID_of_regular_process>` ^^^with the actual PID you identified. For example:^^^
                - `sudo renice -n 5 5443`^^^ ^^^
                - ^^^You should see output confirming the priority change:^^^
                - `5443 (process ID) old priority 0, new priority 5``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
            4. ^^^**Repeat the**^^^ `**ps**` ^^^**and**^^^ `**pgrep**` ^^^**commands to display the CPU percentage and**^^^ `**nice**` ^^^**level**^^^^^^.^^^
                - 
                - ^^^Observe the change in CPU usage for the process whose^^^ `nice` ^^^value you modified. The process with nice value 5 should now have slightly lower CPU usage compared to the processes with nice value 0, but higher than the process with nice value 10.^^^
                - `ps -o pid,pcpu,``nice``,``comm`` $(pgrep ``sha1sum``)`^^^ ^^^
                - ^^^You should see the^^^ `NI` ^^^value for the modified process is now^^^ `5`^^^, and its CPU usage reflects its new priority level.^^^
                - ```
PID %CPU  NI COMMAND
   5443 55.4   5 sha1sum
   5444 67.2   0 sha1sum
   5445 67.1   0 sha1sum
   5446  7.5  10 sha1sum
```^^^ ^^^
                - ^^^ *(Note: The exact* ^^^^^^ ^^^ ` __%CPU__ ``(#3594f7)`  ^^^ *values will vary, but you should observe that processes with lower nice values (higher priority) get more CPU time.)* ^^^
        - 
        - # ^^^**Clean Up Running Processes**^^^
        - ^^^In this final step, you will ensure that all background processes started during the lab are properly terminated. This is a critical cleanup step to prevent unintended resource consumption and ensure the lab environment is reset for future use.^^^
            1. ^^^**Use the**^^^ `**pkill**` ^^^**command to terminate all running processes with the**^^^ `**sha1sum**` ^^^**name pattern**^^^^^^.^^^
                - 
                - ^^^The^^^ `pkill` ^^^command is an efficient way to send a signal (by default,^^^ `SIGTERM`^^^) to processes based on their name. This will stop all^^^ `sha1sum` ^^^processes you started in the previous steps.^^^
                - `pkill ``sha1sum`^^^ ^^^
                - ^^^You might see messages indicating that processes have been terminated.^^^
                - ```
[3]-  Terminated              sha1sum /dev/zero
[2]-  Terminated              sha1sum /dev/zero
[4]+  Terminated              nice -n 10 sha1sum /dev/zero
[1]+  Terminated              sha1sum /dev/zero
```^^^ ^^^
            2. ^^^**Verify that no**^^^ `**sha1sum**` ^^^**processes are still running**^^^^^^.^^^
                - 
                - ^^^You can use^^^ `pgrep` ^^^to check if any^^^ `sha1sum` ^^^processes are still active. If^^^ `pgrep` ^^^returns no output, it means no such processes are running.^^^
                - `pgrep ``sha1sum`^^^ ^^^
                - ^^^This command should return no output, indicating that all^^^ `sha1sum` ^^^processes have been successfully terminated.^^^
                - ```
$ pgrep sha1sum
$
```^^^ ^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, we learned how to manage and utilize^^^ `tuned` ^^^for system performance optimization on RHEL. We began by verifying the installation and status of the^^^ `tuned` ^^^service and listing available tuning profiles, understanding that^^^ `tuned` ^^^dynamically adapts system settings for specific workloads using these profiles. We then practiced logging into a simulated^^^ `servera` ^^^environment via SSH as the^^^ `labex` ^^^user and confirmed the^^^ `tuned` ^^^package installation using^^^ `dnf list tuned`^^^.^^^
        - ^^^The lab further guided us through changing^^^ `tuned` ^^^profiles to observe their impact on system parameters, demonstrating how different profiles can alter system behavior. We also gained practical experience in starting and monitoring CPU-intensive processes, which is crucial for identifying performance bottlenecks. Finally, we learned to adjust process priorities using^^^ `nice` ^^^and^^^ `renice` ^^^commands to manage resource allocation effectively, and concluded by cleaning up running processes to restore the system to its initial state.^^^
    4. **Manage SELinux Security in RHEL**
        - Change SELinux Enforcement Mode
        - Configure Apache with Custom SELinux File Contexts
        - Adjust SELinux Policy for User Home Directories with Booleans
        - Troubleshoot SELinux Denials for Apache Web Server
        - Resolve SELinux Issues for Custom Web Content
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience managing SELinux security in RHEL. You will learn to change SELinux enforcement modes, both temporarily and persistently, and configure Apache with custom SELinux file contexts. The lab also covers adjusting SELinux policy for user home directories using booleans and provides practical steps for troubleshooting and resolving SELinux denials for Apache web servers and custom web content.^^^
        - 
        - # ^^^**Change SELinux Enforcement Mode**^^^
        - ^^^In this step, you will learn how to manage SELinux modes, both temporarily and persistently. SELinux (Security-Enhanced Linux) is a security mechanism that provides mandatory access control (MAC) for the Linux kernel. It defines the access rights for processes, files, and other system resources.^^^
        - ^^^SELinux operates in three primary modes:^^^
            - ^^^**Enforcing**^^^^^^: SELinux policy is enforced. Accesses denied by the policy are blocked and logged. This is the default and most secure mode.^^^
            - ^^^**Permissive**^^^^^^: SELinux policy is not enforced. Accesses denied by the policy are logged but not blocked. This mode is useful for troubleshooting and testing new policies.^^^
            - ^^^**Disabled**^^^^^^: SELinux is turned off. No policy is loaded or enforced. This mode is generally not recommended for production systems.^^^
        - ^^^You will practice changing the SELinux mode using command-line tools and by modifying configuration files.^^^
        - ^^^First, let's check the current SELinux enforcement mode.^^^
            1. ^^^**Check the current SELinux enforcement mode.**^^^
                - ^^^You can use the^^^ `getenforce` ^^^command to quickly see the current SELinux mode.^^^
                - `getenforce`^^^ ^^^
                - ^^^You should see^^^ `Enforcing` ^^^as the output, indicating that SELinux is currently enforcing its policies.^^^
                - `Enforcing`^^^ ^^^
            2. ^^^**Change the SELinux mode to**^^^ `**permissive**` ^^^**temporarily.**^^^
                - ^^^The^^^ `setenforce` ^^^command allows you to change the SELinux mode at runtime. A value of^^^ `0` ^^^sets the mode to^^^ `permissive`^^^, and^^^ `1` ^^^sets it to^^^ `enforcing`^^^. This change is temporary and will not persist across reboots.^^^
                - `sudo setenforce 0`^^^ ^^^
                - ^^^Now, verify the change using^^^ `getenforce` ^^^again.^^^
                - `getenforce`^^^ ^^^
                - ^^^The output should now be^^^ `Permissive`^^^.^^^
                - `Permissive`^^^ ^^^
            3. ^^^**Change the SELinux mode back to**^^^ `**enforcing**` ^^^**temporarily.**^^^
                - ^^^To revert the temporary change, use^^^ `setenforce 1`^^^.^^^
                - `sudo setenforce 1`^^^ ^^^
                - ^^^Verify the mode once more.^^^
                - `getenforce`^^^ ^^^
                - ^^^The output should be^^^ `Enforcing` ^^^again.^^^
                - `Enforcing`^^^ ^^^
            4. ^^^**Change the default SELinux mode to**^^^ `**permissive**` ^^^**persistently.**^^^
                - ^^^To make SELinux mode changes persistent across reboots, you need to modify the^^^ `/etc/selinux/config` ^^^file. This file defines the default SELinux mode for the system.^^^
                - ^^^Open the configuration file using^^^ `nano`^^^.^^^
                - `sudo nano /etc/selinux/config`^^^ ^^^
                - ^^^Inside the^^^ `nano` ^^^editor, find the line that starts with^^^ `SELINUX=` ^^^and change its value from^^^ `enforcing` ^^^to^^^ `permissive`^^^.^^^
                - ```
# This file controls the state of SELinux on the system.
``````
(#5c6370)

``````
# SELINUX= can take one of these three values:
``````
(#5c6370)

``````
#     enforcing - SELinux security policy is enforced.
``````
(#5c6370)

``````
#     permissive - SELinux prints warnings instead of enforcing.
``````
(#5c6370)

``````
#     disabled - No SELinux policy is loaded.
``````
(#5c6370)

``````
SELINUX
``````
(#d19a66)=permissive

``````
# SELINUXTYPE= can take one of these three values:
``````
(#5c6370)

``````
#     targeted - Targeted processes are protected,
``````
(#5c6370)

``````
#                for the majority of users.
``````
(#5c6370)

``````
#     minimum - Modification of targeted policy
``````
(#5c6370)

``````
#               uses current settings and adds to it.
``````
(#5c6370)

``````
#     mls - Multi Level Security protection.
``````
(#5c6370)

``````
SELINUXTYPE
``````
(#d19a66)=targeted
```^^^ ^^^
                - ^^^Press^^^ `Ctrl+X` ^^^to exit, then^^^ `Y` ^^^to confirm saving, and^^^ `Enter` ^^^to write to the same file.^^^
                - ^^^After saving the file, you can confirm the change in the configuration file using^^^ `grep`^^^.^^^
                - `grep ``'^SELINUX'``(#98c379)`` /etc/selinux/config`^^^ ^^^
                - ^^^The output should show^^^ `SELINUX=permissive`^^^.^^^
                - ```
SELINUX=permissive
SELINUXTYPE=targeted
```^^^ ^^^
                - ^^^**Important Note**^^^^^^: Changing^^^ `/etc/selinux/config` ^^^does not immediately change the active SELinux mode. It only sets the mode that will be applied after the next system reboot. To see the current active mode, you still need to use^^^ `getenforce`^^^.^^^
                - `getenforce`^^^ ^^^
                - ^^^It should still show^^^ `Enforcing` ^^^because the system has not been rebooted yet.^^^
                - `Enforcing`^^^ ^^^
            5. ^^^**Change the default SELinux mode back to**^^^ `**enforcing**` ^^^**in the configuration file.**^^^
                - ^^^Now, let's change the persistent mode back to^^^ `enforcing`^^^. This is the recommended and most secure setting for SELinux.^^^
                - ^^^Open the configuration file again.^^^
                - `sudo nano /etc/selinux/config`^^^ ^^^
                - ^^^Change the^^^ `SELINUX=` ^^^parameter back to^^^ `enforcing`^^^.^^^
                - ```
# This file controls the state of SELinux on the system.
``````
(#5c6370)

``````
# SELINUX= can take one of these three values:
``````
(#5c6370)

``````
#     enforcing - SELinux security policy is enforced.
``````
(#5c6370)

``````
#     permissive - SELinux prints warnings instead of enforcing.
``````
(#5c6370)

``````
#     disabled - No SELinux policy is loaded.
``````
(#5c6370)

``````
SELINUX
``````
(#d19a66)=enforcing

``````
# SELINUXTYPE= can take one of these three values:
``````
(#5c6370)

``````
#     targeted - Targeted processes are protected,
``````
(#5c6370)

``````
#                for the majority of users.
``````
(#5c6370)

``````
#     minimum - Modification of targeted policy
``````
(#5c6370)

``````
#               uses current settings and adds to it.
``````
(#5c6370)

``````
#     mls - Multi Level Security protection.
``````
(#5c6370)

``````
SELINUXTYPE
``````
(#d19a66)=targeted
```^^^ ^^^
                - ^^^Save and exit the file (^^^`Ctrl+X``(#3594f7)`^^^,^^^ `Y``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^).^^^
                - ^^^Confirm the change in the configuration file.^^^
                - `grep ``'^SELINUX'``(#98c379)`` /etc/selinux/config`^^^ ^^^
                - ^^^The output should now show^^^ `SELINUX=enforcing`^^^.^^^
                - ```
SELINUX=enforcing
SELINUXTYPE=targeted
```^^^ ^^^
                - ^^^At this point, the system's active SELinux mode is still^^^ `Enforcing` ^^^(if you didn't reboot after step 4), and the persistent setting is also^^^ `Enforcing`^^^.^^^
        - 
        - # ^^^**Configure Apache with Custom SELinux File Contexts**^^^
        - ^^^In this step, you will learn how to configure Apache to serve web content from a non-standard directory and manage its SELinux file contexts. By default, SELinux policies restrict Apache (httpd) to serving files only from specific directories, primarily^^^ `/var/www/html``(#3594f7)`^^^. If you place web content in a different location, SELinux will prevent Apache from accessing it, even if file system permissions are correct. This is where SELinux file contexts come into play.^^^
        - ^^^An SELinux file context is a label applied to a file or directory that defines its security attributes. For Apache to serve content from a custom location, that location and its contents must have the correct SELinux context, typically^^^ `httpd_sys_content_t`^^^. You will use^^^ `semanage fcontext` ^^^to define a persistent rule and^^^ `restorecon` ^^^to apply it.^^^
        - ^^^First, you need to install the Apache HTTP server.^^^
            1. ^^^**Install the Apache HTTP server.**^^^
                - ^^^Use the^^^ `dnf` ^^^package manager to install the^^^ `httpd` ^^^package.^^^
                - `sudo dnf install -y httpd`^^^ ^^^
                - ^^^You should see output indicating the successful installation of the^^^ `httpd` ^^^package and its dependencies.^^^
            2. ^^^**Create a custom directory for web content and an**^^^ `**index.html**` ^^^**file.**^^^
                - ^^^You will create a new directory named^^^ `/custom` ^^^and place a simple^^^ `index.html` ^^^file inside it. This will be your non-standard web document root.^^^
                - ```
sudo 
``````
mkdir
``````
 /custom

``````
echo
``````
 
``````
'This is custom web content.'
``````
(#98c379) | sudo 
``````
tee
``````
 /custom/index.html
```^^^ ^^^
                - ^^^Verify the content of the^^^ `index.html` ^^^file.^^^
                - `cat`` /custom/index.html`^^^ ^^^
                - `This is custom web content.`^^^ ^^^
            3. ^^^**Configure Apache to use the new document root.**^^^
                - ^^^Apache's main configuration file is^^^ `/etc/httpd/conf/httpd.conf`^^^. You need to edit this file to point Apache to your new^^^ `/custom` ^^^directory instead of the default^^^ `/var/www/html`^^^.^^^
                - ^^^Open the configuration file using^^^ `nano`^^^.^^^
                - `sudo nano /etc/httpd/conf/httpd.conf`^^^ ^^^
                - ^^^Inside the editor, find the lines^^^ `DocumentRoot "/var/www/html"` ^^^and^^^ `<Directory "/var/www/html">`^^^. Change both occurrences of^^^ `/var/www/html` ^^^to^^^ `/custom`^^^.^^^
                - ^^^The relevant sections should look like this after modification:^^^
                - ```
#
``````
(#5c6370)

``````
# DocumentRoot: The directory out of which you will serve your
``````
(#5c6370)

``````
# documents. By default, all requests are taken from this directory, but
``````
(#5c6370)

``````
# symbolic links and aliases may be used to point to other locations.
``````
(#5c6370)

``````
#
``````
(#5c6370)
DocumentRoot 
``````
"/custom"
``````
(#98c379)


``````
#
``````
(#5c6370)

``````
# Relax access to content within /var/www.
``````
(#5c6370)

``````
#
``````
(#5c6370)
<
``````
Directory
``````
(#e6c07b) 
``````
"/custom"
``````
(#98c379)>
    AllowOverride None
    
``````
# Allow open access:
``````
(#5c6370)
    Require all granted
</
``````
Directory
``````
(#e6c07b)>
```^^^ ^^^
                - ^^^Save and exit the file (^^^`Ctrl+X``(#3594f7)`^^^,^^^ `Y``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^).^^^
            4. ^^^**Start and enable the Apache web service.**^^^
                - ^^^After modifying the configuration, you need to start the^^^ `httpd` ^^^service. Since you are in a container environment,^^^ `systemctl` ^^^is not available. You will start^^^ `httpd` ^^^directly.^^^
                - `sudo /usr/sbin/httpd -DFOREGROUND &`^^^ ^^^
                - ^^^The^^^ `&` ^^^symbol runs the command in the background, allowing you to continue using the terminal. You should see output similar to this, indicating Apache is starting.^^^
                - ```
[1] 5094
AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using fe80::216:3eff:fe00:63b%eth0. Set the 'ServerName' directive globally to suppress this message
```^^^ ^^^
                - ^^^**Note**^^^^^^: The warning message about the server's fully qualified domain name is normal in this lab environment and can be safely ignored.^^^
                - ^^^To verify that Apache is running, you can check for the^^^ `httpd` ^^^process.^^^
                - `ps aux | grep httpd`^^^ ^^^
                - ^^^You should see several^^^ `httpd` ^^^processes running.^^^
                - ```
root        ... /usr/sbin/httpd -DFOREGROUND
apache      ... /usr/sbin/httpd -DFOREGROUND
...output omitted...
```^^^ ^^^
            5. ^^^**Attempt to access the web page.**^^^
                - ^^^Now, try to access your web page using^^^ `curl`^^^. Since you are on the same machine, you can use^^^ `localhost`^^^.^^^
                - `curl http://localhost/index.html`^^^ ^^^
                - ^^^**Note**^^^^^^: In this particular environment, you may find that the web page is accessible even with the^^^ `root_t` ^^^context. This demonstrates that while SELinux is enforcing, the^^^ `root_t` ^^^context may have broader permissions than expected. However, for security best practices and proper SELinux configuration, web content should still use the appropriate^^^ `httpd_sys_content_t` ^^^context.^^^
                - `This is custom web content.`^^^ ^^^
            6. ^^^**Check the current SELinux context of the custom directory.**^^^
                - ^^^Use the^^^ `ls -Z` ^^^command to view the SELinux context of your^^^ `/custom` ^^^directory and the^^^ `index.html` ^^^file.^^^
                - `ls`` -Zd /custom /custom/index.html`^^^ ^^^
                - ^^^You will notice that they have the^^^ `root_t` ^^^context, which is not the recommended context for Apache web content.^^^
                - ```
system_u:object_r:root_t:s0 /custom
system_u:object_r:root_t:s0 /custom/index.html
```^^^ ^^^
                - ^^^Compare this to the default Apache document root:^^^
                - `ls`` -Zd /var/www/html`^^^ ^^^
                - ^^^You will see that^^^ `/var/www/html` ^^^has the^^^ `httpd_sys_content_t` ^^^context. This is the context you need to apply to your custom directory.^^^
                - `system_u:object_r:httpd_sys_content_t:s0 /var/www/html`^^^ ^^^
            7. ^^^**Define a persistent SELinux file context rule for**^^^ `**/custom**`^^^**.**^^^
                - ^^^The^^^ `semanage fcontext` ^^^command is used to manage SELinux file context mapping rules. The^^^ `-a` ^^^option adds a new rule,^^^ `-t` ^^^specifies the target type, and the regular expression^^^ `'/custom(/.*)?'` ^^^matches the^^^ `/custom` ^^^directory itself and all files and subdirectories within it.^^^
                - `sudo semanage fcontext -a -t httpd_sys_content_t ``'/custom(/.*)?'``(#98c379)`^^^ ^^^
                - ^^^This command adds the rule to the SELinux policy, but it does not immediately change the contexts of existing files.^^^
            8. ^^^**Apply the new SELinux contexts to the files.**^^^
                - ^^^The^^^ `restorecon` ^^^command is used to restore the SELinux contexts of files and directories to their default values as defined by the policy. The^^^ `-R` ^^^option applies the change recursively, and^^^ `-v` ^^^provides verbose output.^^^
                - `sudo restorecon -Rv /custom`^^^ ^^^
                - ^^^You should see output indicating that the contexts of^^^ `/custom` ^^^and^^^ `/custom/index.html` ^^^have been relabeled.^^^
                - ```
Relabeled /custom from system_u:object_r:root_t:s0 to system_u:object_r:httpd_sys_content_t:s0
Relabeled /custom/index.html from system_u:object_r:root_t:s0 to system_u:object_r:httpd_sys_content_t:s0
```^^^ ^^^
                - ^^^Verify the contexts again using^^^ `ls -Z`^^^.^^^
                - `ls`` -Zd /custom /custom/index.html`^^^ ^^^
                - ^^^They should now have the^^^ `httpd_sys_content_t` ^^^context.^^^
                - ```
system_u:object_r:httpd_sys_content_t:s0 /custom
system_u:object_r:httpd_sys_content_t:s0 /custom/index.html
```^^^ ^^^
            9. ^^^**Access the web page again.**^^^
                - ^^^Now that the SELinux contexts are correct, try accessing the web page with^^^ `curl` ^^^again.^^^
                - `curl http://localhost/index.html`^^^ ^^^
                - ^^^You should now see the content of your^^^ `index.html` ^^^file.^^^
                - `This is custom web content.`^^^ ^^^
                - ^^^Finally, stop the Apache HTTP server process.^^^
                - `sudo pkill httpd`^^^ ^^^
                - ^^^Verify that no^^^ `httpd` ^^^processes are running.^^^
                - `ps aux | grep httpd`^^^ ^^^
                - ^^^You should only see the^^^ `grep` ^^^process itself.^^^
                - `labex     ... grep httpd`^^^ ^^^
        - 
        - # ^^^**Adjust SELinux Policy for User Home Directories with Booleans**^^^
        - ^^^In this step, you will learn how to adjust SELinux policy using Booleans to allow Apache to serve web content from users' home directories. By default, SELinux prevents services like Apache from accessing files in user home directories for security reasons. However, there are specific scenarios, such as personal web pages, where this functionality is desired.^^^
        - ^^^SELinux Booleans are true/false settings that allow administrators to modify the behavior of the SELinux policy without writing complex custom policies. They provide a flexible way to enable or disable certain security features. For example, there's a Boolean specifically for allowing Apache to access user home directories.^^^
            1. ^^^**Enable Apache's user directory feature.**^^^
                - ^^^Apache has a module called^^^ `mod_userdir` ^^^that allows users to publish web content from a^^^ `public_html` ^^^directory within their home directory (e.g.,^^^ `~/public_html`^^^). This feature is typically configured in^^^ `/etc/httpd/conf.d/userdir.conf`^^^. By default, this feature is often disabled.^^^
                - ^^^Open the configuration file using^^^ `nano`^^^.^^^
                - `sudo nano /etc/httpd/conf.d/userdir.conf`^^^ ^^^
                - ^^^Inside the editor, you will find lines related to^^^ `UserDir`^^^. You need to comment out the line that disables^^^ `UserDir` ^^^and uncomment the line that enables it for^^^ `public_html`^^^.^^^
                - ^^^Change:^^^
                - ```
UserDir disabled

``````
#UserDir public_html
``````
(#5c6370)
```^^^ ^^^
                - ^^^To:^^^
                - ```
#UserDir disabled
``````
(#5c6370)
UserDir public_html
```^^^ ^^^
                - ^^^Save and exit the file (^^^`Ctrl+X``(#3594f7)`^^^,^^^ `Y``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^).^^^
            2. ^^^**Create a**^^^ `**public_html**` ^^^**directory and an**^^^ `**index.html**` ^^^**file in your home directory.**^^^
                - ^^^You will create the^^^ `public_html` ^^^directory and an^^^ `index.html` ^^^file inside it. This is where your personal web content will reside.^^^
                - ```
mkdir
``````
 ~/public_html

``````
echo
``````
 
``````
'This is labex user content.'
``````
(#98c379) > ~/public_html/index.html
```^^^ ^^^
                - ^^^Verify the content of the^^^ `index.html` ^^^file.^^^
                - `cat`` ~/public_html/index.html`^^^ ^^^
                - `This is labex user content.`^^^ ^^^
                - ^^^**Informational**^^^^^^: When you created the^^^ `~/public_html` ^^^directory, it was automatically configured with^^^ `user_home_t` ^^^and^^^ `~/` ^^^(your home directory) with^^^ `home_dir_t` ^^^SELinux contexts. The Apache web server process (^^^`httpd_t`^^^) cannot read files labeled^^^ `user_home_t` ^^^or^^^ `home_dir_t` ^^^by default due to SELinux policy.^^^
            3. ^^^**Start the Apache web service.**^^^
                - ^^^Start the^^^ `httpd` ^^^service. Remember,^^^ `systemctl` ^^^is not available in this container environment, so you will start^^^ `httpd` ^^^directly.^^^
                - `sudo /usr/sbin/httpd -DFOREGROUND &`^^^ ^^^
                - ^^^You may see a warning message about the server's fully qualified domain name, which can be safely ignored in this lab environment.^^^
                - ^^^Verify that Apache is running.^^^
                - `ps aux | grep httpd`^^^ ^^^
                - ```
root        ... /usr/sbin/httpd -DFOREGROUND
apache      ... /usr/sbin/httpd -DFOREGROUND
...output omitted...
```^^^ ^^^
            4. ^^^**Attempt to access the user's web page and observe the SELinux denial.**^^^
                - ^^^Now, try to access your personal web page using^^^ `curl`^^^. The URL for user directories typically follows the format^^^ `http://localhost/~username/`^^^.^^^
                - `curl http://localhost/~labex/index.html`^^^ ^^^
                - ^^^You will likely receive a "Forbidden" error, indicating that Apache is still unable to access the content due to SELinux.^^^
                - ```
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access /~labex/index.html
on this server.<br />
</p>
</body></html>
```^^^ ^^^
            5. ^^^**Check SELinux Booleans related to home directories for**^^^ `**httpd**`^^^**.**^^^
                - ^^^The^^^ `getsebool` ^^^command allows you to view the current state of SELinux Booleans. You can filter the output using^^^ `grep` ^^^to find Booleans related to^^^ `httpd` ^^^and home directories.^^^
                - `sudo getsebool -a | grep httpd | grep home`^^^ ^^^
                - ^^^You should see^^^ `httpd_enable_homedirs --> off`^^^, indicating that this Boolean is currently disabled.^^^
                - `httpd_enable_homedirs --> off`^^^ ^^^
            6. ^^^**Enable the**^^^ `**httpd_enable_homedirs**` ^^^**Boolean persistently.**^^^
                - ^^^The^^^ `setsebool` ^^^command is used to change the state of SELinux Booleans. The^^^ `-P` ^^^option makes the change persistent across reboots.^^^
                - `sudo setsebool -P httpd_enable_homedirs on`^^^ ^^^
                - ^^^Verify that the Boolean is now^^^ `on`^^^.^^^
                - `sudo getsebool -a | grep httpd | grep home`^^^ ^^^
                - `httpd_enable_homedirs --> on`^^^ ^^^
            7. ^^^**Set the correct file permissions for the home directory.**^^^
                - ^^^Even with the SELinux boolean enabled, Apache needs proper file system permissions to access your home directory and the^^^ `public_html` ^^^directory. By default, user home directories are not accessible to the Apache user.^^^
                - ```
chmod
``````
 711 ~

``````
chmod
``````
 755 ~/public_html

``````
chmod
``````
 644 ~/public_html/index.html
```^^^ ^^^
            8. ^^^**Access the web page again.**^^^
                - ^^^Now that both the^^^ `httpd_enable_homedirs` ^^^Boolean is enabled and the file permissions are correct, try accessing your personal web page with^^^ `curl` ^^^again.^^^
                - `curl http://localhost/~labex/index.html`^^^ ^^^
                - ^^^You should now see the content of your^^^ `index.html` ^^^file.^^^
                - `This is labex user content.`^^^ ^^^
                - ^^^**Troubleshooting**^^^^^^: If you still encounter access issues even after enabling the boolean and setting file permissions, this demonstrates the multi-layered nature of Linux security. In some environments, additional factors such as:^^^
                    - ^^^Apache configuration directives in^^^ `/etc/httpd/conf.d/userdir.conf`
                    - ^^^SELinux file contexts on the home directory structure^^^
                    - ^^^Additional Apache modules or security settings^^^
                - ^^^may need to be addressed. The key learning point is understanding how SELinux booleans work in conjunction with traditional file permissions and application-specific configurations.^^^
            9. ^^^**Stop the Apache HTTP server process.**^^^
                - ^^^Finally, stop the Apache HTTP server process.^^^
                - `sudo pkill httpd`^^^ ^^^
                - ^^^Verify that no^^^ `httpd` ^^^processes are running.^^^
                - `ps aux | grep httpd`^^^ ^^^
                - `labex     ... grep httpd`^^^ ^^^
        - 
        - # ^^^**Troubleshoot SELinux Denials for Apache Web Server**^^^
        - ^^^In this step, you will learn how to identify and troubleshoot SELinux security denials, specifically focusing on issues that might prevent the Apache web server from functioning correctly. When SELinux blocks an operation, it logs an "Access Vector Cache" (AVC) denial message. These messages are crucial for understanding why an operation failed and how to resolve it.^^^
        - ^^^You will use tools like^^^ `auditd` ^^^(the Linux Auditing System daemon) and^^^ `sealert` ^^^to analyze these denial messages.^^^ `auditd` ^^^collects system calls and events, including SELinux denials, and stores them in^^^ `/var/log/audit/audit.log`^^^. The^^^ `sealert` ^^^tool, part of the^^^ `setroubleshoot-server` ^^^package, can parse these logs and provide human-readable explanations and suggested solutions for SELinux denials.^^^
        - ^^^First, you need to ensure^^^ `auditd` ^^^and^^^ `setroubleshoot-server` ^^^are installed.^^^
            1. ^^^**Install**^^^ `**auditd**` ^^^**and**^^^ `**setroubleshoot-server**`^^^**.**^^^
                - `sudo dnf install -y audit setroubleshoot-server`^^^ ^^^
                - ^^^You should see output indicating the successful installation of these packages.^^^
            2. ^^^**Start the Apache web server and create a problematic file.**^^^
                - ^^^To simulate an SELinux denial, you will create a file with an incorrect SELinux context and try to serve it with Apache.^^^
                - ^^^First, ensure Apache is running.^^^
                - `sudo /usr/sbin/httpd -DFOREGROUND &`^^^ ^^^
                - ^^^Now, create a new directory and an^^^ `index.html` ^^^file within it. This time, you will intentionally set an incorrect SELinux context for this file to trigger a denial.^^^
                - ```
sudo 
``````
mkdir
``````
 /testweb

``````
echo
``````
 
``````
'This is a test page.'
``````
(#98c379) | sudo 
``````
tee
``````
 /testweb/index.html
```^^^ ^^^
                - ^^^By default,^^^ `/testweb/index.html` ^^^will likely have the^^^ `root_t` ^^^context. Let's confirm.^^^
                - `ls`` -Z /testweb/index.html`^^^ ^^^
                - `system_u:object_r:root_t:s0 /testweb/index.html`^^^ ^^^
                - ^^^Now, let's configure Apache to serve from^^^ `/testweb`^^^. Open^^^ `/etc/httpd/conf/httpd.conf`^^^.^^^
                - `sudo nano /etc/httpd/conf/httpd.conf`^^^ ^^^
                - ^^^Change^^^ `DocumentRoot` ^^^and the^^^ `<Directory>` ^^^directive to^^^ `/testweb`^^^.^^^
                - ```
DocumentRoot 
``````
"/testweb"
``````
(#98c379)

<
``````
Directory
``````
(#e6c07b) 
``````
"/testweb"
``````
(#98c379)>
    AllowOverride None
    Require all granted
</
``````
Directory
``````
(#e6c07b)>
```^^^ ^^^
                - ^^^Save and exit (^^^`Ctrl+X``(#3594f7)`^^^,^^^ `Y``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^).^^^
                - ^^^Restart Apache to apply the configuration changes. Since you are in a container, you need to kill the old process and start a new one.^^^
                - ```
sudo pkill httpd
sudo /usr/sbin/httpd -DFOREGROUND &
```^^^ ^^^
            3. ^^^**Attempt to access the web page.**^^^
                - ^^^Try to access the web page using^^^ `curl`^^^.^^^
                - `curl http://localhost/index.html`^^^ ^^^
                - ^^^**Important Note**^^^^^^: In this environment, you may find that the web page is accessible even with the^^^ `root_t` ^^^context, similar to what we observed in Step 2. This demonstrates that while SELinux is enforcing, the^^^ `root_t` ^^^context has broader permissions than more restrictive contexts.^^^
                - `This is a test page.`^^^ ^^^
                - ^^^However, for the purpose of learning SELinux troubleshooting techniques, we will proceed as if there were a denial. In more restrictive SELinux environments or with different policy configurations, accessing files with inappropriate contexts would indeed generate denials.^^^
            4. ^^^**Learn about investigating SELinux denials using**^^^ `**ausearch**`^^^**.**^^^
                - ^^^The^^^ `ausearch` ^^^command is used to query the audit logs. You can search for SELinux AVC denials (^^^`-m AVC`^^^) that occurred today (^^^`-ts today`^^^).^^^
                - `sudo ausearch -m AVC -ts today`^^^ ^^^
                - ^^^**Note**^^^^^^: Since the web page was accessible in our environment, you may not see any recent AVC denials related to this specific test. However, this command would normally output detailed audit log entries if there were denials. In a typical denial scenario, you would look for entries related to^^^ `httpd` ^^^and^^^ `/testweb/index.html`^^^.^^^
                - ^^^A typical AVC denial entry would look like this:^^^
                - ```
----
time->...
type=AVC msg=audit(...): avc:  denied  { getattr } for  pid=... comm="httpd" path="/testweb/index.html" dev="overlay" ino=... scontext=system_u:system_r:httpd_t:s0 tcontext=system_u:object_r:root_t:s0 tclass=file permissive=0
...output omitted...
```^^^ ^^^
                - ^^^The key parts in an AVC denial would be:^^^
                    - `denied { getattr }`^^^: The operation that was denied (getting attributes of the file).^^^
                    - `comm="httpd"`^^^: The process that was denied (Apache HTTP server).^^^
                    - `path="/testweb/index.html"`^^^: The file that was accessed.^^^
                    - `scontext=system_u:system_r:httpd_t:s0`^^^: The SELinux context of the source (Apache).^^^
                    - `tcontext=system_u:object_r:root_t:s0`^^^: The SELinux context of the target (your^^^ `index.html` ^^^file).^^^
                    - `tclass=file`^^^: The type of target (a file).^^^
                - ^^^This output clearly shows that^^^ `httpd_t` ^^^(Apache) was denied^^^ `getattr` ^^^access to a file with^^^ `default_t` ^^^context.^^^
            5. ^^^**Learn about using**^^^ `**sealert**` ^^^**for SELinux analysis.**^^^
                - `sealert` ^^^can parse the audit logs and provide more user-friendly information. You can either run^^^ `sealert -a` ^^^to analyze all recent denials or use^^^ `sealert -l <UUID>` ^^^if you have a specific UUID from a^^^ `setroubleshoot` ^^^message in^^^ `/var/log/messages`^^^.^^^
                - `sudo sealert -a /var/log/audit/audit.log`^^^ ^^^
                - ^^^**Note**^^^^^^: Since we haven't encountered actual denials in this environment, running^^^ `sealert` ^^^may not show results related to our^^^ `/testweb` ^^^example. However, in a scenario where SELinux denials occur,^^^ `sealert` ^^^would analyze the audit log and present a summary.^^^
                - ^^^A typical^^^ `sealert` ^^^output for an httpd context issue would look like this:^^^
                - ```
SELinux is preventing /usr/sbin/httpd from getattr access on the file /testweb/index.html.

***** Plugin catchall_labels (83.8 confidence) suggests *******************
If you want to allow httpd to have getattr access on the index.html file
Then you need to change the label on /testweb/index.html
Do # semanage fcontext -a -t FILE_TYPE '/testweb/index.html'
where FILE_TYPE is one of the following:
httpd_sys_content_t, httpd_sys_script_exec_t, httpd_unconfined_script_exec_t, ...

***** Plugin httpd_can_network_connect (93.8 confidence) suggests *********
If you want to allow httpd to connect to the network (for example, to a database)
Then you must set the httpd_can_network_connect boolean to on.
Do # setsebool -P httpd_can_network_connect on
...output omitted...
```^^^ ^^^
                - ^^^The^^^ `sealert` ^^^output would be very helpful in real denial scenarios. It would explicitly state the problem and suggest solutions, such as changing the label with^^^ `semanage fcontext -a -t FILE_TYPE '/testweb/index.html'` ^^^and listing^^^ `httpd_sys_content_t` ^^^as a suitable^^^ `FILE_TYPE`^^^.^^^
                - ^^^Finally, stop the Apache HTTP server process.^^^
                - `sudo pkill httpd`^^^ ^^^
                - ^^^Verify that no^^^ `httpd` ^^^processes are running.^^^
                - `ps aux | grep httpd`^^^ ^^^
                - `labex     ... grep httpd`^^^ ^^^
        - 
        - # ^^^**Resolve SELinux Issues for Custom Web Content**^^^
        - ^^^In this final step, you will apply the knowledge gained from the previous troubleshooting exercise to resolve the SELinux denial that prevented Apache from serving content from the^^^ `/testweb` ^^^directory. You will use^^^ `semanage fcontext` ^^^to define the correct SELinux context for your custom web content and^^^ `restorecon` ^^^to apply it.^^^
        - ^^^This process reinforces the understanding of how SELinux contexts work and how to correctly configure them for services like Apache.^^^
            1. ^^^**Ensure Apache is running and the configuration is in place.**^^^
                - ^^^First, ensure that Apache is configured to serve from^^^ `/testweb` ^^^and is running. If you stopped Apache in the previous step, start it again.^^^
                - `sudo /usr/sbin/httpd -DFOREGROUND &`^^^ ^^^
                - ^^^Verify that the^^^ `DocumentRoot` ^^^in^^^ `/etc/httpd/conf/httpd.conf` ^^^is set to^^^ `/testweb`^^^. If not, modify it as done in the previous step.^^^
                - `grep ``"DocumentRoot"``(#98c379)`` /etc/httpd/conf/httpd.conf`^^^ ^^^
                - `DocumentRoot "/testweb"`^^^ ^^^
                - ^^^Also, confirm that^^^ `/testweb/index.html` ^^^exists and has the^^^ `root_t` ^^^context.^^^
                - `ls`` -Z /testweb/index.html`^^^ ^^^
                - `system_u:object_r:root_t:s0 /testweb/index.html`^^^ ^^^
            2. ^^^**Access the web page to confirm current behavior.**^^^
                - ^^^Let's verify that the web page is currently accessible with the^^^ `root_t` ^^^context.^^^
                - `curl http://localhost/index.html`^^^ ^^^
                - ^^^As we've seen before, the page is accessible even with the^^^ `root_t` ^^^context.^^^
                - `This is a test page.`^^^ ^^^
                - ^^^While this works, we will proceed to demonstrate the proper SELinux configuration for web content.^^^
            3. ^^^**Define the correct SELinux file context for**^^^ `**/testweb**`^^^**.**^^^
                - ^^^The correct SELinux context for web content served by Apache is^^^ `httpd_sys_content_t`^^^. You need to add a persistent rule using^^^ `semanage fcontext`^^^.^^^
                - `sudo semanage fcontext -a -t httpd_sys_content_t ``'/testweb(/.*)?'``(#98c379)`^^^ ^^^
                - ^^^This command tells SELinux that any files or directories within^^^ `/testweb` ^^^(including^^^ `/testweb` ^^^itself) should be labeled with^^^ `httpd_sys_content_t`^^^.^^^
            4. ^^^**Apply the new SELinux contexts to the files.**^^^
                - ^^^After defining the rule, you must apply it to the existing files using^^^ `restorecon`^^^.^^^
                - `sudo restorecon -Rv /testweb`^^^ ^^^
                - ^^^You should see output indicating that the contexts have been relabeled.^^^
                - ```
Relabeled /testweb from system_u:object_r:root_t:s0 to system_u:object_r:httpd_sys_content_t:s0
Relabeled /testweb/index.html from system_u:object_r:root_t:s0 to system_u:object_r:httpd_sys_content_t:s0
```^^^ ^^^
                - ^^^Verify the contexts again using^^^ `ls -Z`^^^.^^^
                - `ls`` -Z /testweb/index.html`^^^ ^^^
                - `system_u:object_r:httpd_sys_content_t:s0 /testweb/index.html`^^^ ^^^
            5. ^^^**Access the web page again to confirm proper configuration.**^^^
                - ^^^Now that the SELinux contexts are correctly applied according to best practices, try accessing the web page with^^^ `curl` ^^^one more time.^^^
                - `curl http://localhost/index.html`^^^ ^^^
                - ^^^The content should still be accessible, and now it's properly configured with the recommended SELinux context.^^^
                - `This is a test page.`^^^ ^^^
                - ^^^This demonstrates that while the^^^ `root_t` ^^^context may work in this environment, using the proper^^^ `httpd_sys_content_t` ^^^context follows SELinux best practices and ensures compatibility across different security configurations.^^^
                - ^^^Finally, stop the Apache HTTP server process.^^^
                - `sudo pkill httpd`^^^ ^^^
                - ^^^Verify that no^^^ `httpd` ^^^processes are running.^^^
                - `ps aux | grep httpd`^^^ ^^^
                - `labex     ... grep httpd`^^^ ^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, you learned to manage SELinux security in RHEL. You began by understanding and practicing how to change SELinux enforcement modes, both temporarily using^^^ `setenforce` ^^^and persistently by modifying^^^ `/etc/selinux/config`^^^. This included verifying the current mode with^^^ `getenforce` ^^^and understanding the implications of Enforcing, Permissive, and Disabled modes.^^^
        - ^^^Furthermore, you gained practical experience in configuring Apache with custom SELinux file contexts using^^^ `semanage fcontext` ^^^and^^^ `restorecon` ^^^to ensure proper web server operation. You also learned to adjust SELinux policy for user home directories by enabling specific SELinux booleans with^^^ `setsebool`^^^. Finally, the lab covered essential troubleshooting techniques for SELinux denials, specifically for the Apache web server, by analyzing audit logs with^^^ `ausearch` ^^^and^^^ `audit2allow` ^^^to identify and resolve access issues for custom web content.^^^
    5. **Manage RHEL Storage Partitions and Swap Space**
        - Inspect available storage devices
        - Create an XFS partition on /dev/vdb and mount it persistently
        - Create and activate a swap partition on /dev/vdb
        - Create additional partitions on /dev/vdb
        - Format the third partition and mount it persistently
        - Create additional swap partitions on /dev/vdb with priorities
        - Verify persistent mount configuration without reboot
        - 
        - # ^^^**Introduction**^^^
        - ^^^In this lab, you will gain hands-on experience managing storage partitions and swap space on Red Hat Enterprise Linux (RHEL) systems. You will learn to create and persistently mount XFS partitions, as well as configure and activate swap partitions with varying priorities. The lab uses the LabEx VM environment with available storage devices, allowing you to practice these essential system administration skills.^^^
        - ^^^You will begin by inspecting available disks, then proceed to create and manage partitions, including setting up GPT partition tables where necessary. The lab emphasizes ensuring persistent mounts and swap activation, providing a comprehensive understanding of disk management in a RHEL environment.^^^
        - 
        - # ^^^**Inspect available storage devices**^^^
        - ^^^In this step, you will inspect the available storage devices on your LabEx VM. The LabEx environment provides an additional storage device that you can use for partitioning practice.^^^
        - ^^^First, switch to the root user to perform disk management operations. You are currently logged in as the^^^ `labex` ^^^user with sudo privileges.^^^
        - `sudo su -`^^^ ^^^
        - ^^^Now, let's examine the available block devices on the system using the^^^ `lsblk` ^^^command:^^^
        - `lsblk`^^^ ^^^
        - ^^^You should see output similar to this, showing various storage devices:^^^
        - ```
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
vda    253:0    0   40G  0 disk
├─vda1 253:1    0    1M  0 part
├─vda2 253:2    0  100M  0 part /boot/efi
└─vda3 253:3    0 39.9G  0 part /
vdb    253:16   0   40G  0 disk
```^^^ ^^^
        - ^^^In this environment, you have access to an additional storage device^^^ `/dev/vdb` ^^^that is unpartitioned and ready for use. Let's inspect this device more closely.^^^
        - ^^^Use the^^^ `lsblk` ^^^command with the^^^ `-f` ^^^option to display filesystem information for^^^ `/dev/vdb`^^^:^^^
        - `lsblk -f /dev/vdb`^^^ ^^^
        - ^^^You should see output similar to this, indicating that^^^ `/dev/vdb` ^^^is a new, unformatted disk:^^^
        - ```
NAME FSTYPE FSVER LABEL UUID FSAVAIL FSUSE% MOUNTPOINTS
vdb
```^^^ ^^^
        - ^^^Next, use the^^^ `parted` ^^^command to get more detailed information about the disk, including its partition table:^^^
        - `parted /dev/vdb ``print`^^^ ^^^
        - ^^^The output should show that there is no partition table on^^^ `/dev/vdb` ^^^yet:^^^
        - ```
Error: /dev/vdb: unrecognised disk label
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: unknown
Disk Flags:
```^^^ ^^^
        - ^^^This confirms that^^^ `/dev/vdb` ^^^is a fresh disk ready for partitioning. The error message is normal for a disk that hasn't been initialized with a partition table yet.^^^
        - 
        - # ^^^**Create an XFS partition on /dev/vdb and mount it persistently**^^^
        - ^^^In this step, you will create a new partition on^^^ `/dev/vdb`^^^, format it with the XFS file system, and configure it to mount persistently.^^^
        - ^^^You will create a 1 GB primary partition on^^^ `/dev/vdb` ^^^and specify the file system type as XFS. It's good practice to align partitions to sector boundaries for optimal performance. Starting at sector 2048 is a common alignment.^^^
        - ^^^**First, you need to create a partition table on the uninitialized disk.**^^^ ^^^Use^^^ `parted` ^^^in interactive mode to create the partition table and partition:^^^
        - `parted /dev/vdb`^^^ ^^^
        - ```
GNU Parted 3.5
Using /dev/vdb
Welcome to GNU Parted! Type 'help' to view a list of commands.
(parted) mklabel msdos
(parted) mkpart
Partition type?  primary/extended? primary
File system type?  [ext2]? xfs
Start? 2048s
End? 1001MB
(parted) quit
Information: You may need to update /etc/fstab.
```^^^ ^^^
        - ^^^**Note:**^^^ ^^^The^^^ `mklabel msdos` ^^^command creates an MBR (Master Boot Record) partition table on the disk. This is required before you can create any partitions. After creating the partition table, you can proceed with^^^ `mkpart` ^^^to create the actual partition. Because the partition starts at sector 2048, setting the end position to^^^ `1001MB` ^^^will result in a partition size of approximately 1 GB. When you quit parted, you'll see an informational message about updating^^^ `/etc/fstab`^^^, which is normal.^^^
        - ^^^To verify that the partition has been created, use^^^ `parted` ^^^to print the partition table for^^^ `/dev/vdb`^^^:^^^
        - `parted /dev/vdb ``print`^^^ ^^^
        - ^^^You should see output similar to this, showing your newly created primary partition:^^^
        - ```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  1001MB  1000MB  primary
```^^^ ^^^
        - ^^^After creating a new partition, it's crucial to inform the kernel about the changes. The^^^ `udevadm settle` ^^^command waits for the system to register the new partition and create its corresponding device file (e.g.,^^^ `/dev/vdb1`^^^).^^^
        - `udevadm settle`^^^ ^^^
        - ^^^Now that the partition is created, you need to format it with the XFS file system. This prepares the partition to store data. Use the^^^ `mkfs.xfs` ^^^command for this:^^^
        - `mkfs.xfs /dev/vdb1`^^^ ^^^
        - ^^^The output will show details about the XFS file system creation:^^^
        - ```
meta-data=/dev/vdb1              isize=512    agcount=4, agsize=61056 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=1 inobtcount=1 nrext64=0
data     =                       bsize=4096   blocks=244224, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
```^^^ ^^^
        - ^^^To make the file system accessible, you need to mount it. First, create a mount point directory. You will mount this partition to^^^ `/archive`^^^.^^^
        - `mkdir`` /archive`^^^ ^^^
        - ^^^For persistent mounting (meaning the file system will automatically mount every time the system boots), you need to add an entry to the^^^ `/etc/fstab``(#3594f7)` ^^^file. It's best practice to use the Universally Unique Identifier (UUID) of the partition in^^^ `/etc/fstab``(#3594f7)` ^^^because device names like^^^ `/dev/vdb1``(#3594f7)` ^^^can change if new disks are added or removed.^^^
        - ^^^Discover the UUID of^^^ `/dev/vdb1` ^^^using^^^ `lsblk --fs`^^^:^^^
        - `lsblk --fs /dev/vdb1`^^^ ^^^
        - ^^^Note down the UUID from the output. It will look something like^^^ `881e856c-37b1-41e3-b009-ad526e46d987`^^^.^^^
        - ```
NAME FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
vdb1 xfs                2ee03827-6acf-4543-9a21-0fd031250b45
```^^^ ^^^
        - ^^^Now, open the^^^ `/etc/fstab` ^^^file using^^^ `nano` ^^^and add a new line for your partition. Replace^^^ `YOUR_UUID_HERE` ^^^with the actual UUID you just found.^^^
        - `nano /etc/fstab`^^^ ^^^
        - ^^^Add the following line to the end of the file:^^^
        - `UUID=YOUR_UUID_HERE /archive xfs defaults 0 0`^^^ ^^^
        - ^^^**Explanation of the**^^^ `**/etc/fstab**` ^^^**entry:**^^^
            - `UUID=YOUR_UUID_HERE`^^^: Specifies the device to mount using its UUID.^^^
            - `/archive`^^^: The mount point directory.^^^
            - `xfs`^^^: The file system type.^^^
            - `defaults`^^^: A common set of mount options (rw, suid, dev, exec, auto, nouser, async).^^^
            - `0`^^^:^^^ `dump` ^^^option (0 means no dump).^^^
            - `0`^^^:^^^ `fsck` ^^^order (0 means no fsck check at boot).^^^
        - ^^^Save the file by pressing^^^ `Ctrl+X`^^^, then^^^ `Y` ^^^to confirm, and^^^ `Enter` ^^^to write to the file.^^^
        - ^^^After modifying^^^ `/etc/fstab`^^^, you need to tell^^^ `systemd` ^^^to reload its configuration so it recognizes the new entry.^^^
        - `systemctl daemon-reload`^^^ ^^^
        - ^^^Finally, mount the new file system using the entry in^^^ `/etc/fstab`^^^. The^^^ `mount /archive` ^^^command will use the information from^^^ `/etc/fstab` ^^^to mount^^^ `/dev/vdb1` ^^^to^^^ `/archive`^^^.^^^
        - `mount /archive`^^^ ^^^
        - ^^^Verify that the new file system is mounted correctly by checking the^^^ `mount` ^^^command output and filtering for^^^ `/archive`^^^:^^^
        - `mount | grep /archive`^^^ ^^^
        - ^^^You should see output similar to this, confirming the successful mount:^^^
        - `/dev/vdb1 on /archive type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - 
        - # ^^^**Create and activate a swap partition on /dev/vdb**^^^
        - ^^^In this step, you will create a swap partition on the^^^ `/dev/vdb` ^^^disk. Swap space is a portion of a hard disk drive (HDD) or solid-state drive (SSD) used for temporary storage when the system runs out of physical RAM. It acts as an overflow for RAM, allowing the system to continue operating even when memory is scarce, though at a slower speed.^^^
        - ^^^First, let's inspect the current partition table on^^^ `/dev/vdb` ^^^to determine where to create the new swap partition.^^^
        - `parted /dev/vdb ``print`^^^ ^^^
        - ^^^You should see the existing XFS partition (^^^`/dev/vdb1``(#3594f7)`^^^) that you created in the previous step:^^^
        - ```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 5369MB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  1001MB  1000MB  primary  xfs
```^^^ ^^^
        - ^^^Now, you will add a new primary partition of 500 MB for use as swap space. You will set the partition file-system type to^^^ `linux-swap`^^^. The new partition will start immediately after the existing^^^ `/dev/vdb1` ^^^partition. The end of^^^ `/dev/vdb1` ^^^is at^^^ `1001MB`^^^. So, the new partition will start at^^^ `1001MB` ^^^and end at^^^ `1501MB` ^^^(1001MB + 500MB).^^^
        - ^^^Use^^^ `parted` ^^^in non-interactive mode to create this partition:^^^
        - `parted /dev/vdb mkpart primary linux-swap 1001MB 1501MB`^^^ ^^^
        - ^^^You might see the^^^ `Information: You may need to update /etc/fstab.` ^^^message again.^^^
        - ^^^Verify your work by listing the partitions on the^^^ `/dev/vdb` ^^^disk:^^^
        - `parted /dev/vdb ``print`^^^ ^^^
        - ^^^You should now see two partitions, with the second one being your new swap partition:^^^
        - ```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  1001MB  1000MB  primary  xfs
 2      1001MB  1501MB  499MB   primary               swap
```^^^ ^^^
        - ^^^As before, after creating a new partition, you must run^^^ `udevadm settle` ^^^to ensure the system registers the new partition and creates its device file (^^^`/dev/vdb2`^^^).^^^
        - `udevadm settle`^^^ ^^^
        - ^^^Now, format the new partition (^^^`/dev/vdb2``(#3594f7)`^^^) as swap space using the^^^ `mkswap``(#3594f7)` ^^^command. This command initializes the partition for use as swap.^^^
        - `mkswap /dev/vdb2`^^^ ^^^
        - ^^^The output will show details about the swap space creation, including its size and a generated UUID:^^^
        - ```
Setting up swapspace version 1, size = 476 MiB (499118080 bytes)
no label, UUID=4379b167-ab39-4c83-bf7c-b28fbdb38725
```^^^ ^^^
        - ^^^To configure the new swap space to activate persistently, you need to add an entry to the^^^ `/etc/fstab` ^^^file. First, discover the UUID of the^^^ `/dev/vdb2` ^^^device.^^^
        - `lsblk -o UUID /dev/vdb2`^^^ ^^^
        - ^^^Note down the UUID from the output. It will be similar to^^^ `4379b167-ab39-4c83-bf7c-b28fbdb38725`^^^.^^^
        - ```
UUID
4379b167-ab39-4c83-bf7c-b28fbdb38725
```^^^ ^^^
        - ^^^Open the^^^ `/etc/fstab` ^^^file using^^^ `nano` ^^^and add a new line for your swap partition. Replace^^^ `YOUR_SWAP_UUID_HERE` ^^^with the actual UUID you just found.^^^
        - `nano /etc/fstab`^^^ ^^^
        - ^^^Add the following line to the end of the file:^^^
        - `UUID=YOUR_SWAP_UUID_HERE swap swap defaults 0 0`^^^ ^^^
        - ^^^**Explanation of the**^^^ `**/etc/fstab**` ^^^**entry for swap:**^^^
            - `UUID=YOUR_SWAP_UUID_HERE`^^^: Specifies the device to use as swap.^^^
            - `swap`^^^: The mount point (for swap, this is always^^^ `swap`^^^).^^^
            - `swap`^^^: The file system type (for swap, this is always^^^ `swap`^^^).^^^
            - `defaults`^^^: Standard options for swap.^^^
            - `0`^^^:^^^ `dump` ^^^option (0 means no dump).^^^
            - `0`^^^:^^^ `fsck` ^^^order (0 means no fsck check for swap).^^^
        - ^^^Save the file by pressing^^^ `Ctrl+X`^^^, then^^^ `Y` ^^^to confirm, and^^^ `Enter` ^^^to write to the file.^^^
        - ^^^After modifying^^^ `/etc/fstab`^^^, reload the^^^ `systemd` ^^^daemon to recognize the new entry.^^^
        - `systemctl daemon-reload`^^^ ^^^
        - ^^^Finally, enable the swap space using the^^^ `swapon -a` ^^^command. The^^^ `-a` ^^^option tells^^^ `swapon` ^^^to enable all swap devices listed in^^^ `/etc/fstab`^^^.^^^
        - `swapon -a`^^^ ^^^
        - ^^^Verify that the new swap space is enabled using^^^ `swapon --show`^^^:^^^
        - `swapon --show`^^^ ^^^
        - ^^^You should see output similar to this, confirming your new swap partition is active:^^^
        - ```
NAME      TYPE      SIZE USED PRIO
/dev/vdb2 partition 476M   0B   -2
```^^^ ^^^
        - ^^^The output shows your newly created swap partition is active and ready to use.^^^
        - 
        - # ^^^**Create additional partitions on /dev/vdb**^^^
        - ^^^In this step, you will create additional partitions on^^^ `/dev/vdb`^^^. Since you have created one XFS partition and one swap partition using the MBR (msdos) partition table, you still have space available for more partitions. You will now create a third partition that will demonstrate managing larger partitions.^^^
        - ^^^First, let's check the current partition table and available space on^^^ `/dev/vdb`^^^:^^^
        - `parted /dev/vdb ``print`^^^ ^^^
        - ^^^You should see the two partitions you created earlier:^^^
        - ```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  1001MB  1000MB  primary  xfs
 2      1001MB  1501MB  500MB   primary  linux-swap
```^^^ ^^^
        - ^^^Now, you will create a third partition of 2 GB for additional storage. This partition will start at^^^ `1501MB` ^^^(the end of the swap partition) and end at^^^ `3501MB` ^^^(1501MB + 2000MB).^^^
        - `parted /dev/vdb mkpart primary xfs 1501MB 3501MB`^^^ ^^^
        - ^^^You might see the^^^ `Information: You may need to update /etc/fstab.` ^^^message.^^^
        - ^^^Verify the creation of the third partition:^^^
        - `parted /dev/vdb ``print`^^^ ^^^
        - ^^^You should now see three partitions:^^^
        - ```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  1001MB  1000MB  primary  xfs
 2      1001MB  1501MB  500MB   primary  linux-swap
 3      1501MB  3501MB  2000MB  primary
```^^^ ^^^
        - ^^^Run^^^ `udevadm settle` ^^^to ensure the system detects the new partition:^^^
        - `udevadm settle`^^^ ^^^
        - 
        - # ^^^**Format the third partition and mount it persistently**^^^
        - ^^^In this step, you will format the third partition (^^^`/dev/vdb3``(#3594f7)`^^^) with XFS file system and configure it for persistent mounting at^^^ `/backup``(#3594f7)`^^^.^^^
        - ^^^First, format the^^^ `/dev/vdb3` ^^^partition with the XFS file system:^^^
        - `mkfs.xfs /dev/vdb3`^^^ ^^^
        - ^^^The output will show details about the XFS file system creation:^^^
        - ```
meta-data=/dev/vdb3              isize=512    agcount=4, agsize=122880 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=1 inobtcount=1
data     =                       bsize=4096   blocks=491520, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
```^^^ ^^^
        - ^^^Now, create a mount point directory for this partition. You will mount it to^^^ `/backup`^^^.^^^
        - `mkdir`` /backup`^^^ ^^^
        - ^^^To ensure the file system mounts automatically, you need to add an entry to^^^ `/etc/fstab`^^^. First, find the UUID of the^^^ `/dev/vdb3` ^^^partition.^^^
        - `lsblk -o UUID /dev/vdb3`^^^ ^^^
        - ^^^Note down the UUID from the output. It will be a unique identifier like^^^ `f74ed805-b1fc-401a-a5ee-140f97c6757d`^^^.^^^
        - ```
UUID
f74ed805-b1fc-401a-a5ee-140f97c6757d
```^^^ ^^^
        - ^^^Open the^^^ `/etc/fstab` ^^^file using^^^ `nano` ^^^and add the new entry. Replace^^^ `YOUR_UUID_HERE` ^^^with the actual UUID you found.^^^
        - `nano /etc/fstab`^^^ ^^^
        - ^^^Add the following line to the end of the file:^^^
        - `UUID=YOUR_UUID_HERE /backup xfs defaults 0 0`^^^ ^^^
        - ^^^Save the file (^^^`Ctrl+X``(#3594f7)`^^^,^^^ `Y``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^).^^^
        - ^^^After modifying^^^ `/etc/fstab`^^^, reload the^^^ `systemd` ^^^daemon to apply the changes.^^^
        - `systemctl daemon-reload`^^^ ^^^
        - ^^^Finally, manually mount the^^^ `/backup` ^^^directory to verify that the configuration is correct.^^^
        - `mount /backup`^^^ ^^^
        - ^^^Confirm that the mount is successful by checking the^^^ `mount` ^^^command output:^^^
        - `mount | grep /backup`^^^ ^^^
        - ^^^You should see output similar to this:^^^
        - `/dev/vdb3 on /backup type xfs (rw,relatime,seclabel,attr2,inode64,noquota)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - 
        - # ^^^**Create additional swap partitions on /dev/vdb with priorities**^^^
        - ^^^In this step, you will create one additional swap partition on^^^ `/dev/vdb` ^^^and learn about partition table limitations. You will also learn how to assign priorities to swap partitions. When multiple swap partitions are active, the system uses the one with the highest priority first.^^^
        - ^^^**Understanding Partition Table Limitations:**^^^
        - ^^^The current setup uses an MBR (msdos) partition table, which has a limitation of only 4 primary partitions. Since you have already created 4 partitions, you cannot create additional primary partitions without converting to GPT or using extended partitions.^^^
        - ^^^First, check the current partition table on^^^ `/dev/vdb`^^^:^^^
        - `parted /dev/vdb ``print`^^^ ^^^
        - ^^^You should see the four partitions you created so far:^^^
        - ```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  1001MB  1000MB  primary  xfs
 2      1001MB  1501MB  500MB   primary  linux-swap
 3      1501MB  3501MB  2000MB  primary  xfs
```^^^ ^^^
        - ^^^Now, create the fourth partition as a 512 MB swap partition. It will start at^^^ `3501MB` ^^^(the end of the third partition) and end at^^^ `4013MB` ^^^(3501MB + 512MB).^^^
        - `parted /dev/vdb mkpart primary linux-swap 3501MB 4013MB`^^^ ^^^
        - ^^^You might see the^^^ `Information: You may need to update /etc/fstab.` ^^^message.^^^
        - ^^^**Note about MBR limitations:**^^^ ^^^At this point, you have reached the 4-partition limit for MBR partition tables. Attempting to create a fifth primary partition would result in an error:^^^ `Error: Can't create any more partitions.`
        - ^^^Display the partition table to verify your work:^^^
        - `parted /dev/vdb ``print`^^^ ^^^
        - ^^^You should now see four partitions:^^^
        - ```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  1001MB  1000MB  primary  xfs
 2      1001MB  1501MB  500MB   primary  linux-swap
 3      1501MB  3501MB  2000MB  primary  xfs
 4      3501MB  4013MB  512MB   primary  linux-swap
```^^^ ^^^
        - ^^^Run^^^ `udevadm settle` ^^^to ensure the system registers the new partition and creates its device file (^^^`/dev/vdb4`^^^).^^^
        - `udevadm settle`^^^ ^^^
        - ^^^Now, initialize the new partition as swap space using the^^^ `mkswap` ^^^command. Note down the UUID for^^^ `/dev/vdb4`^^^, as you will need it for^^^ `/etc/fstab`^^^.^^^
        - `mkswap /dev/vdb4`^^^ ^^^
        - ^^^Example output for^^^ `/dev/vdb4`^^^:^^^
        - ```
Setting up swapspace version 1, size = 488 MiB (511705088 bytes)
no label, UUID=87976166-4697-47b7-86d1-73a02f0fc803
```^^^ ^^^
        - ^^^To configure this swap space to activate with a specific priority, you need to add an entry to the^^^ `/etc/fstab` ^^^file. A higher^^^ `pri` ^^^(priority) value indicates a higher preference. You will set a higher priority for the new swap partition.^^^
        - ^^^Open^^^ `/etc/fstab` ^^^using^^^ `nano`^^^:^^^
        - `nano /etc/fstab`^^^ ^^^
        - ^^^Add the following line to the end of the file, replacing the UUID with the one you noted down:^^^
        - `UUID=UUID_OF_VDB4   swap    swap  pri=10    0 0`^^^ ^^^
        - ^^^**Explanation of**^^^ `**pri**` ^^^**option:**^^^
            - `pri=10`^^^: Assigns a priority of 10 to^^^ `/dev/vdb4`^^^. This is higher than the default priority (-2) of^^^ `/dev/vdb2`^^^, so the system will prefer to use^^^ `/dev/vdb4` ^^^before^^^ `/dev/vdb2`^^^.^^^
        - ^^^Save the file (^^^`Ctrl+X``(#3594f7)`^^^,^^^ `Y``(#3594f7)`^^^,^^^ `Enter``(#3594f7)`^^^).^^^
        - ^^^Reload the^^^ `systemd` ^^^daemon to recognize the new^^^ `/etc/fstab` ^^^entry.^^^
        - `systemctl daemon-reload`^^^ ^^^
        - ^^^Activate the new swap space using^^^ `swapon -a`^^^.^^^
        - `swapon -a`^^^ ^^^
        - ^^^Verify the correct activation and priority of the swap spaces using^^^ `swapon --show`^^^:^^^
        - `swapon --show`^^^ ^^^
        - ^^^You should see output showing all active swap partitions with their priorities. The^^^ `/dev/vdb2` ^^^will have default priority (-2), while^^^ `/dev/vdb4` ^^^will have the priority you assigned (10).^^^
        - ```
NAME      TYPE      SIZE USED PRIO
/dev/vdb2 partition 476M   0B   -2
/dev/vdb4 partition 488M   0B   10
```^^^ ^^^
        - ^^^**Learning Note:**^^^ ^^^In a production environment, if you needed more than 4 partitions, you would either:^^^
            1. ^^^Convert to GPT partition table (supports up to 128 partitions)^^^
            2. ^^^Use extended partitions with logical partitions within them^^^
            3. ^^^Use LVM (Logical Volume Manager) for more flexible storage management^^^
        - 
        - # ^^^**Verify persistent mount configuration without reboot**^^^
        - ^^^In this final step, you will test the persistent mount configuration without actually rebooting the system, since a reboot would disconnect you from the LabEx environment. Instead, you will use various commands to simulate and verify that your configurations would work correctly after a restart.^^^
        - ^^^First, let's verify that all your mount entries are correctly configured in^^^ `/etc/fstab`^^^. Display the contents of^^^ `/etc/fstab` ^^^to review your entries:^^^
        - `cat`` /etc/fstab`^^^ ^^^
        - ^^^You should see your entries for the XFS partitions and swap spaces similar to this:^^^
        - ```
# ... existing system entries ...
UUID=your-vdb1-uuid /archive xfs defaults 0 0
UUID=your-vdb2-uuid swap swap defaults 0 0
UUID=your-vdb3-uuid /backup xfs defaults 0 0
UUID=your-vdb4-uuid swap    swap  pri=10    0 0
UUID=your-vdb5-uuid swap    swap  pri=20    0 0
```^^^ ^^^
        - ^^^Now, let's test the mount configuration by unmounting and remounting the file systems to ensure they work correctly:^^^
        - ^^^First, unmount the^^^ `/archive` ^^^directory:^^^
        - `umount /archive`^^^ ^^^
        - ^^^Verify it's unmounted:^^^
        - `mount | grep /archive`^^^ ^^^
        - ^^^This should return no output.^^^
        - ^^^Now remount it using the^^^ `/etc/fstab` ^^^entry:^^^
        - `mount /archive`^^^ ^^^
        - ^^^Verify it's mounted again:^^^
        - `mount | grep /archive`^^^ ^^^
        - ^^^You should see:^^^
        - `/dev/vdb1 on /archive type xfs (rw,relatime,seclabel,attr2,inode64,logbufs=8,logbsize=32k,noquota)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^Repeat the same process for^^^ `/backup`^^^:^^^
        - ```
umount /backup
mount /backup
mount | grep /backup
```^^^ ^^^
        - ^^^You should see:^^^
        - `/dev/vdb3 on /backup type xfs (rw,relatime,seclabel,attr2,inode64,noquota)``(#a9b7c6)``(#1a1a1a)`^^^ ^^^
        - ^^^For swap spaces, let's test by turning them off and on again. First, turn off all swap:^^^
        - `swapoff -a`^^^ ^^^
        - ^^^Verify no swap is active:^^^
        - `swapon --show`^^^ ^^^
        - ^^^This should show only any system swap that might exist, but not your custom swap partitions.^^^
        - ^^^Now turn on all swap using^^^ `/etc/fstab`^^^:^^^
        - `swapon -a`^^^ ^^^
        - ^^^Verify all swap spaces are active with correct priorities:^^^
        - `swapon --show`^^^ ^^^
        - ^^^You should see output similar to this, with all your swap partitions active and correct priorities:^^^
        - ```
NAME       TYPE       SIZE USED PRIO
/dev/vda2  partition    2G   0B   -2
/dev/vdb2  partition  476M   0B   -2
/dev/vdc2  partition  244M   0B   10
/dev/vdc3  partition  244M   0B   20
```^^^ ^^^
        - ^^^Finally, let's test that^^^ `systemd` ^^^can process all your^^^ `/etc/fstab` ^^^entries without errors:^^^
        - `systemctl daemon-reload`^^^ ^^^
        - ^^^This should complete without any error messages.^^^
        - ^^^You can also use the^^^ `findmnt` ^^^command to verify that the kernel would be able to mount all file systems defined in^^^ `/etc/fstab`^^^:^^^
        - `findmnt --verify`^^^ ^^^
        - ^^^This command checks^^^ `/etc/fstab` ^^^for potential issues and should complete without errors.^^^
        - ^^^Display a final summary of all your work:^^^
        - ```
echo
``````
 
``````
"=== Final Storage Configuration Summary ==="
``````
(#98c379)

``````
echo
``````
 
``````
"Partition tables:"
``````
(#98c379)
parted /dev/vdb 
``````
print
``````


``````
echo
``````
 
``````
""
``````
(#98c379)

``````
echo
``````
 
``````
"Mounted filesystems:"
``````
(#98c379)
mount | grep -E 
``````
"/archive|/backup"
``````
(#98c379)

``````
echo
``````
 
``````
""
``````
(#98c379)

``````
echo
``````
 
``````
"Active swap spaces:"
``````
(#98c379)
swapon --show

``````
echo
``````
 
``````
""
``````
(#98c379)

``````
echo
``````
 
``````
"fstab entries for persistence:"
``````
(#98c379)
grep -E 
``````
"archive|backup|swap"
``````
(#98c379) /etc/fstab

``````
echo
``````
 
``````
""
``````
(#98c379)

``````
echo
``````
 
``````
"UUID verification:"
``````
(#98c379)

``````
echo
``````
 
``````
"Device UUIDs:"
``````
(#98c379)
lsblk -f /dev/vdb* | grep -E 
``````
"vdb[1-4]"
``````
(#98c379)
```^^^ ^^^
        - ^^^This concludes the lab on managing storage partitions and swap space. You have successfully created and configured multiple partitions with different file systems, set up persistent mounts, and configured swap spaces with priorities, all without requiring a system reboot.^^^
        - 
        - # ^^^**Summary**^^^
        - ^^^In this lab, participants learned to manage storage partitions and swap space on a RHEL 9 system within the LabEx VM environment. The lab began with inspecting the available storage device (^^^`/dev/vdb``(#3594f7)`^^^) and understanding its current state before proceeding with partitioning tasks.^^^
        - ^^^Participants worked with^^^ `/dev/vdb`^^^, creating an MBR partition table, then creating multiple partitions: an XFS partition for mounting at^^^ `/archive`^^^, a swap partition, another XFS partition for mounting at^^^ `/backup`^^^, and an additional swap partition with priority configuration. The lab also demonstrates the limitations of MBR partition tables (4 primary partition limit) and provides insights into alternatives like GPT for scenarios requiring more partitions.^^^
        - ^^^A crucial aspect of the lab was ensuring persistent configuration through proper^^^ `/etc/fstab` ^^^entries and testing the configuration without requiring a system reboot (which would disconnect the LabEx environment). The lab concluded with comprehensive verification procedures to confirm that all mounts and swap spaces would activate correctly, providing hands-on experience with essential RHEL storage management skills in a practical, cloud-based learning environment.^^^
    6. **Create and Extend LVM Logical Volumes in RHEL**
        - Prepare Physical Volumes with `parted` and `pvcreate`
        - Create a Volume Group from Physical Volumes with `vgcreate`
        - Create and Format a Logical Volume with `lvcreate` and `mkfs.xfs`
        - Persistently Mount the Logical Volume using `/etc/fstab`
        - Extend the Volume Group and Logical Volume with `vgextend` and `lvextend`
        - Resize the XFS Filesystem with `xfs_growfs`
        - 
        - # **Introduction**
        - In this lab, you will learn the fundamental process of creating and managing LVM (Logical Volume Manager) storage on a Red Hat Enterprise Linux system. You will start by preparing a physical disk, partitioning it with `parted`, and initializing it as an LVM Physical Volume (PV) using `pvcreate`. Following this, you will pool this PV into a Volume Group (VG) with `vgcreate`, and then create a flexible Logical Volume (LV) from that group using `lvcreate`. The initial setup concludes with formatting the new LV with an XFS filesystem and mounting it persistently for system use.
        - Building on the initial configuration, you will then explore one of LVM's key advantages: the ability to dynamically resize storage. You will learn how to extend an existing Volume Group by adding a new Physical Volume with `vgextend`. Subsequently, you will expand the Logical Volume to utilize this new space using `lvextend` and resize the XFS filesystem online with `xfs_growfs` to make the additional capacity immediately available to the operating system without downtime.
        - 
        - # **Prepare Physical Volumes with** `**parted**` **and** `**pvcreate**`
        - In this step, you will begin managing storage by preparing a physical disk for use with the Logical Volume Manager (LVM). This involves two key stages: first, partitioning the disk using the `parted` utility, and second, initializing these partitions as LVM Physical Volumes (PVs) with the `pvcreate` command.
        - **Logical Volume Manager (LVM) Overview**
        - LVM is a powerful storage management tool in Linux that provides a flexible layer over physical storage devices. Instead of using disks and partitions directly, LVM allows you to create abstract "volume groups" from one or more physical devices, and then carve out "logical volumes" from that pooled space. This makes it much easier to resize storage, replace disks, and manage your system's storage without downtime.
        - The most fundamental component in LVM is the **Physical Volume (PV)**. A PV is a physical storage device, such as a hard disk partition or a whole disk, that has been initialized for use by LVM.
        - ### **1. Create a Partition for LVM**
        - Before a disk can be used by LVM, you must create a partition on it and set its type to "LVM". We will use the `/dev/vdb` device for this exercise. You will need `sudo` privileges to modify disk partitions.
        - First, create a new GUID Partition Table (GPT) on the `/dev/vdb` device. A GPT is a modern standard for the layout of the partition table on a physical storage device.
        - `sudo parted /dev/vdb mklabel gpt` Explain Code
        - Next, create a single partition that is 512 MiB in size. We will name this partition `lvm-part1`.
        - `sudo parted /dev/vdb mkpart lvm-part1 1MiB 513MiB` Explain Code
        - Now, set the partition type to `lvm`. This flag tells the system that this partition is intended for use with the Logical Volume Manager.
        - `sudo parted /dev/vdb set 1 lvm on` Explain Code
        - To ensure the kernel recognizes the new partition immediately, run the `udevadm settle` command. This command waits for the `udev` daemon to process all device events, ensuring that the new partition `/dev/vdb1` is available.
        - `sudo udevadm settle` Explain Code
        - Finally, verify that the partition was created correctly by printing the partition table.
        - `sudo parted /dev/vdb print` Explain Code
        - You should see output similar to the following, showing one partition with the `lvm` flag enabled.
        - ```
Model: Virtio Block Device (virtblk)
Disk /dev/vdb: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags:

Number  Start   End    Size   File system  Name       Flags
 1      1049kB  538MB  537MB               lvm-part1  lvm
``` Explain Code
        - ### **2. Initialize the Partition as a Physical Volume**
        - With the partition created and correctly typed, the next step is to initialize it as an LVM Physical Volume using the `pvcreate` command. This command writes LVM metadata onto the partition, formally making it part of the LVM system.
        - Run the following command to initialize `/dev/vdb1`:
        - `sudo pvcreate /dev/vdb1` Explain Code
        - A successful operation will produce the following message:
        - ```
Physical volume "/dev/vdb1" successfully created.
  Creating devices file /etc/lvm/devices/system.devices
``` Explain Code
        - ### **3. Display Physical Volume Information**
        - You can now inspect the newly created Physical Volume. The `pvs` command provides a compact summary of all PVs on the system, while `pvdisplay` offers a more detailed view.
        - Use `pvs` to see a quick summary:
        - `sudo pvs` Explain Code
        - The output will list your new PV. Note that it does not yet belong to any Volume Group (VG).
        - ```
PV         VG Fmt  Attr PSize   PFree
  /dev/vdb1     lvm2 ---  512.00m 512.00m
``` Explain Code
        - For more details, use `pvdisplay`:
        - `sudo pvdisplay /dev/vdb1` Explain Code
        - This command shows detailed information, including the PV name, size, and unique identifier (UUID).
        - ```
"/dev/vdb1" is a new physical volume of "512.00 MiB"
  --- NEW Physical volume ---
  PV Name               /dev/vdb1
  VG Name
  PV Size               512.00 MiB
  Allocatable           NO
  PE Size               0
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
``` Explain Code
        - You have now successfully prepared a physical partition for LVM. In the next step, you will use this PV to create a Volume Group.
        - 
        - # **Create a Volume Group from Physical Volumes with** `**vgcreate**`
        - In this step, you will use the Physical Volume (PV) you prepared in the previous step to create a Volume Group (VG). A Volume Group is a central component of LVM, acting as a single, manageable pool of disk space from which you can create Logical Volumes.
        - **Understanding Volume Groups and Physical Extents**
        - A **Volume Group (VG)** aggregates one or more Physical Volumes into a single storage pool. Think of it as combining several smaller containers of water into one large tank. This abstraction is what gives LVM its flexibility.
        - This storage pool is divided into small, fixed-size chunks called **Physical Extents (PEs)**. By default, a PE is 4 MiB. When you create a Logical Volume later, you are essentially allocating a certain number of these PEs from the Volume Group.
        - ### **1. Create the Volume Group**
        - Now, you will create a Volume Group named `my_vg` using the `/dev/vdb1` Physical Volume. The command for this is `vgcreate`.
        - `sudo vgcreate my_vg /dev/vdb1` Explain Code
        - If the command is successful, you will see a confirmation message:
        - `Volume group "my_vg" successfully created` Explain Code
        - This command has created a new storage pool named `my_vg` that contains all the available space from `/dev/vdb1`.
        - ### **2. Display Volume Group Information**
        - Just as you did with Physical Volumes, you can display information about your new Volume Group. The `vgs` command provides a summary, and `vgdisplay` provides a detailed view.
        - To get a compact summary of all Volume Groups on the system, run:
        - `sudo vgs` Explain Code
        - The output will show your new VG, its size, and the amount of free space.
        - ```
VG    #PV #LV #SN Attr   VSize   VFree
  my_vg   1   0   0 wz--n- 508.00m 508.00m
``` Explain Code
        - For a more detailed report on your specific Volume Group, use `vgdisplay`:
        - `sudo vgdisplay my_vg` Explain Code
        - This output provides comprehensive details, including the PE size, the total number of PEs, and how many are still free.
        - ```
--- Volume group ---
  VG Name               my_vg
  System ID
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  1
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                0
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               508.00 MiB
  PE Size               4.00 MiB
  Total PE              127
  Alloc PE / Size       0 / 0
  Free  PE / Size       127 / 508.00 MiB
  VG UUID               xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
``` Explain Code
        - Notice the `PE Size` is 4.00 MiB and you have 127 `Free PE`, which corresponds to the total available space in the Volume Group. You have now successfully created a Volume Group and it is ready to have Logical Volumes created from it.
        - 
        - # **Create and Format a Logical Volume with** `**lvcreate**` **and** `**mkfs.xfs**`
        - In this step, you will carve out a usable block device, known as a Logical Volume (LV), from the Volume Group you created. Once the LV is created, it's still just raw storage space. To store files on it, you must format it with a filesystem.
        - **Understanding Logical Volumes and Filesystems**
        - A **Logical Volume (LV)** is the LVM equivalent of a traditional disk partition. It is created from the free space within a Volume Group and is presented to the operating system as a standard block device. You can create filesystems on LVs, mount them, and use them to store data. The key advantage is that LVs can be easily resized, which is much more difficult with physical partitions.
        - A **filesystem** is a data structure that the operating system uses to control how data is stored and retrieved. It organizes the raw space of a device like an LV into files and directories. For this lab, we will use **XFS**, which is a high-performance, journaling filesystem that is the default for Red Hat Enterprise Linux.
        - ### **1. Create the Logical Volume**
        - You will now create a 256 MiB Logical Volume named `my_lv` from the `my_vg` Volume Group. The command for this is `lvcreate`.
            - `-n my_lv`: Specifies the name for the new LV.
            - `-L 256M`: Sets the size of the LV to 256 Megabytes.
            - `my_vg`: The name of the Volume Group to create the LV from.
        - Execute the following command:
        - `sudo lvcreate -n my_lv -L 256M my_vg` Explain Code
        - A successful command will produce this output:
        - `Logical volume "my_lv" created.` Explain Code
        - ### **2. Verify the Logical Volume Creation**
        - You can inspect your new LV using the `lvs` and `lvdisplay` commands.
        - To see a summary of all LVs, run:
        - `sudo lvs` Explain Code
        - The output will show your new LV, `my_lv`, within the `my_vg` group.
        - ```
LV    VG    Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  my_lv my_vg -wi-a----- 256.00m
``` Explain Code
        - For a detailed view, you can specify the LV's full path. The path to an LV is typically `/dev/VG_NAME/LV_NAME`.
        - `sudo lvdisplay /dev/my_vg/my_lv` Explain Code
        - This provides detailed information, including the LV Path, which you will need for the next step.
        - ```
--- Logical volume ---
  LV Path                /dev/my_vg/my_lv
  LV Name                my_lv
  VG Name                my_vg
  LV UUID                xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
  LV Write Access        read/write
  LV Creation host, time host, 2023-10-27 10:30:00 +0000
  LV Status              available
  # open                 0
  LV Size                256.00 MiB
  Current LE             64
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           253:2
``` Explain Code
        - ### **3. Format the Logical Volume with an XFS Filesystem**
        - Now, you will format the `my_lv` Logical Volume with the XFS filesystem using the `mkfs.xfs` command. This prepares the volume to store files.
        - `sudo mkfs.xfs /dev/my_vg/my_lv` Explain Code
        - The command will output details about the filesystem it is creating.
        - ```
meta-data=/dev/my_vg/my_lv       isize=512    agcount=4, agsize=16384 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1
data     =                       bsize=4096   blocks=65536, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
``` Explain Code
        - Your Logical Volume is now formatted and ready to be mounted and used. You will do this in the next step.
        - 
        - # **Persistently Mount the Logical Volume using** `**/etc/fstab**`
        - In this step, you will make the Logical Volume you created and formatted accessible to the system. This involves two actions: creating a directory to serve as a "mount point" and then configuring the system to automatically attach the Logical Volume to this directory every time it boots.
        - **Understanding Mounting and** `**/etc/fstab**`
        - A formatted block device, like your `my_lv` Logical Volume, is not directly usable until it is **mounted**. Mounting is the process of attaching a filesystem to a specific directory in the main filesystem tree. Once mounted, you can navigate into that directory to read and write files on the device.
        - To ensure the filesystem is mounted automatically after a reboot, you must add an entry for it in the `/etc/fstab` (file system table) file. This file contains a list of all the disks and partitions that the system should mount at boot time.
        - ### **1. Create a Mount Point**
        - A mount point is simply an empty directory that will serve as the root of your new filesystem. We will create a directory named `/data` for this purpose.
        - `sudo mkdir /data` Explain Code
        - ### **2. Add an Entry to** `**/etc/fstab**` **for Persistent Mounting**
        - Now, you need to tell the system to mount your LV at the `/data` directory automatically. You will add a new line to the `/etc/fstab` file. Each line in this file has six fields:
            1. **Device**: The device to mount. In our case, `/dev/my_vg/my_lv`.
            2. **Mount Point**: The directory to mount it on. Here, it's `/data`.
            3. **Filesystem Type**: The type of the filesystem, which is `xfs`.
            4. **Mount Options**: Options for mounting. `defaults` is a standard set of options suitable for most cases.
            5. **Dump**: Used by the `dump` utility to decide whether to back up the filesystem. `0` means disable.
            6. **Pass**: Used by `fsck` to determine the order for checking filesystems at boot. `0` means do not check.
        - We will use the `echo` command combined with `sudo tee -a` to append the correct line to `/etc/fstab` without needing a text editor.
        - `echo '/dev/my_vg/my_lv /data xfs defaults 0 0' | sudo tee -a /etc/fstab` Explain Code
        - You can verify that the line was added correctly by viewing the contents of the file:
        - `cat /etc/fstab` Explain Code
        - ### **3. Mount the Filesystem**
        - Now that the entry exists in `/etc/fstab`, you can use the `mount` command to mount it immediately. Because the mount point `/data` is listed in `/etc/fstab`, you only need to provide the directory name.
        - `sudo mount /data` Explain Code
        - The system will read `/etc/fstab`, find the entry for `/data`, and mount the corresponding device.
        - ### **4. Verify the Mount**
        - To confirm that the filesystem is successfully mounted, you can use the `df` (disk free) command with the `-h` (human-readable) option.
        - `df -h /data` Explain Code
        - The output should show your logical volume mounted on `/data`, with its total size and available space.
        - ```
Filesystem                  Size  Used Avail Use% Mounted on
/dev/mapper/my_vg-my_lv     251M   28M  224M  11% /data
``` Explain Code
        - You can also create a test file to ensure you have write access:
        - `echo "My LVM is working!" | sudo tee /data/test.txt` Explain Code
        - Then, read the file back to confirm it was written:
        - `cat /data/test.txt` Explain Code
        - `My LVM is working!` Explain Code
        - Your Logical Volume is now mounted and will be available automatically every time the system starts.
        - 
        - # **Extend the Volume Group and Logical Volume with** `**vgextend**` **and** `**lvextend**`
        - In this step, you will experience one of the most powerful features of LVM: the ability to dynamically increase the size of your storage. You will add a new physical disk partition to your existing Volume Group to expand its total capacity, and then extend your Logical Volume to use some of that new space.
        - **Understanding Storage Extension**
        - A primary reason for using LVM is its flexibility. When you run out of space, you don't need to perform a complex data migration. Instead, you can simply add another physical disk (or partition) to the Volume Group and then grow your Logical Volumes as needed. This can all be done online, without unmounting the filesystem.
            - `vgextend`: This command adds one or more Physical Volumes to an existing Volume Group, increasing its total size.
            - `lvextend`: This command increases the size of a Logical Volume, drawing space from the free extents within its Volume Group.
        - ### **1. Prepare a New Physical Volume**
        - To extend the Volume Group, you first need a new Physical Volume. We will create a second partition on the `/dev/vdb` device, just like you did in the first step.
        - First, create a new 512 MiB partition. We'll place it immediately after the first one.
        - `sudo parted /dev/vdb mkpart lvm-part2 513MiB 1025MiB` Explain Code
        - Next, set the partition type to `lvm`.
        - `sudo parted /dev/vdb set 2 lvm on` Explain Code
        - Ensure the kernel recognizes the new partition, `/dev/vdb2`.
        - `sudo udevadm settle` Explain Code
        - Finally, initialize this new partition as a Physical Volume.
        - `sudo pvcreate /dev/vdb2` Explain Code
        - You should see the success message:
        - `Physical volume "/dev/vdb2" successfully created.` Explain Code
        - ### **2. Extend the Volume Group**
        - Now, add the new Physical Volume (`/dev/vdb2`) to your existing Volume Group (`my_vg`) using the `vgextend` command.
        - `sudo vgextend my_vg /dev/vdb2` Explain Code
        - The confirmation message will indicate success:
        - `Volume group "my_vg" successfully extended` Explain Code
        - You can verify the change with the `vgs` command. Notice that the `VSize` and `VFree` have increased significantly.
        - `sudo vgs my_vg` Explain Code
        - ```
VG    #PV #LV #SN Attr   VSize    VFree
  my_vg   2   1   0 wz--n- 1022.00m 766.00m
``` Explain Code
        - The `my_vg` Volume Group now spans two physical partitions and has more free space available.
        - ### **3. Extend the Logical Volume**
        - With more space available in the Volume Group, you can now extend your Logical Volume. Let's increase the size of `my_lv` from 256 MiB to a new total size of 400 MiB.
        - The `lvextend` command with the `-L` option sets the new absolute size of the volume.
        - `sudo lvextend -L 400M /dev/my_vg/my_lv` Explain Code
        - The output will confirm the resize operation.
        - ```
Size of logical volume my_vg/my_lv changed from 256.00 MiB (64 extents) to 400.00 MiB (100 extents).
  Logical volume my_vg/my_lv successfully resized.
``` Explain Code
        - Verify the new size of the Logical Volume with `lvs`:
        - `sudo lvs /dev/my_vg/my_lv` Explain Code
        - ```
LV    VG    Attr       LSize   Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  my_lv my_vg -wi-ao---- 400.00m
``` Explain Code
        - **Important:** You have successfully extended the Logical Volume (the block device), but the XFS filesystem living on it is not yet aware of this new space. If you check the mounted filesystem's size, it will still report the old size.
        - `df -h /data` Explain Code
        - ```
Filesystem                  Size  Used Avail Use% Mounted on
/dev/mapper/my_vg-my_lv     251M   28M  224M  11% /data
``` Explain Code
        - In the next step, you will resize the filesystem to fill the newly available space in the Logical Volume.
        - 
        - # **Resize the XFS Filesystem with** `**xfs_growfs**`
        - In this final step, you will complete the storage extension process by resizing the XFS filesystem to make it aware of the additional space you allocated to its underlying Logical Volume. This is the crucial last step that makes the new space usable for storing files.
        - **Understanding Filesystem Resizing**
        - When you extend a Logical Volume, you are only increasing the size of the container (the block device). The filesystem   *inside*   that container remains at its original size and is unaware of the new, unused space at the end of the device.
        - For an XFS filesystem, the `xfs_growfs` command is used to expand the filesystem to fill the underlying device. A major advantage of XFS is that this operation can be performed online, while the filesystem is mounted and in use, with no downtime required.
        - ### **1. Grow the XFS Filesystem**
        - The `xfs_growfs` command takes the mount point of the filesystem as its argument. In your case, the mount point is `/data`.
        - Run the following command to expand the filesystem:
        - `sudo xfs_growfs /data` Explain Code
        - The command will output information about the change, indicating the old and new number of data blocks.
        - ```
meta-data=/dev/mapper/my_vg-my_lv isize=512    agcount=4, agsize=16384 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1
data     =                       bsize=4096   blocks=65536, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 65536 to 102400
``` Explain Code
        - The key line is `data blocks changed from 65536 to 102400`, which confirms the filesystem has grown.
        - ### **2. Verify the New Filesystem Size**
        - Now, run the `df -h` command again to verify that the filesystem size reflects the change.
        - `df -h /data` Explain Code
        - The output should now show the new, larger size, which is approximately 400 MiB.
        - ```
Filesystem                  Size  Used Avail Use% Mounted on
/dev/mapper/my_vg-my_lv     395M   29M  367M   8% /data
``` Explain Code
        - You can also check that the test file you created earlier is still intact:
        - `cat /data/test.txt` Explain Code
        - `My LVM is working!` Explain Code
        - Congratulations! You have successfully completed the entire LVM workflow: from partitioning a physical disk and creating Physical Volumes, to building a Volume Group, creating a Logical Volume, formatting and mounting it, and finally, dynamically extending it online without any data loss.
        - 
        - # **Summary**
        - In this lab, you learned the fundamental workflow for setting up storage using the Logical Volume Manager (LVM) in RHEL. You started by preparing a physical disk, using `parted` to create a partition with the `lvm` flag set, and then initializing it as a Physical Volume (PV) with `pvcreate`. Following this, you pooled the PV into a new Volume Group (VG) using `vgcreate`. From this VG, you carved out a Logical Volume (LV) with `lvcreate`, formatted it with an XFS filesystem using `mkfs.xfs`, and configured it for persistent mounting by adding an entry to `/etc/fstab`.
        - The lab also demonstrated the flexibility of LVM by guiding you through the process of extending an existing logical volume. This involved preparing a new physical volume, adding it to the volume group with `vgextend` to increase the total available space, and then extending the logical volume itself with `lvextend`. Finally, you resized the XFS filesystem online using `xfs_growfs` to make the additional storage space usable by the operating system, completing the end-to-end process of dynamic storage management.
    7. **Configure NFS Client Access in RHEL**
        - Manually Mount an NFS Share Using the mount Command
        - Configure a Persistent NFS Mount in /etc/fstab
        - Set Up the Automounter by Installing and Enabling autofs
        - Create an Indirect Automount Map for Dynamic Directories
        - Create a Direct Automount Map for Static Mount Points
        - Verify Direct and Indirect Automounts as Different Users
        - 
        - # **Introduction**
        - In this lab, you will learn the essential skills for configuring NFS client access on a Red Hat Enterprise Linux (RHEL) system. You will start by manually mounting a network share using the `mount` command to understand the fundamental process. Following this, you will configure a persistent mount in `/etc/fstab` to ensure the NFS share is automatically available after a system reboot, providing a foundational understanding of static network file system integration.
        - Building on these core concepts, you will advance to a more dynamic and efficient method by setting up the automounter. This involves installing and enabling the `autofs` service, then creating both indirect maps for on-demand directory mounting and direct maps for static mount points. You will conclude the lab by verifying that both direct and indirect automounts function correctly for different users, solidifying your ability to manage robust NFS client configurations.
        - 
        - # **Manually Mount an NFS Share Using the mount Command**
        - In this step, you will learn how to manually access a network-shared directory using the Network File System (NFS) protocol. NFS allows a client system to access files over a computer network in a manner similar to how local storage is accessed. For this exercise, we will simulate both an NFS server and a client on your local machine to practice the necessary commands.
        - An NFS server has been pre-configured on your system to export (share) the directory `/srv/nfs/shared_data`. Your task is to mount this shared directory to a local folder, verify access, and then unmount it.
        - ### **Step 1.1: Create a Local Mount Point**
        - To access the shared NFS directory, you need a local directory to serve as a "mount point." This is essentially an empty folder on your client system where the contents of the remote share will appear once mounted. All operations will be performed within your `~/project` directory.
        - Create a directory named `nfs_mount` inside your project folder:
        - `mkdir ~/project/nfs_mount` Explain Code
        - You can verify that the directory was created by listing the contents of your project folder:
        - `ls -F ~/project` Explain Code
        - `nfs_mount/` Explain Code
        - ### **Step 1.2: Mount the NFS Share**
        - Now you can use the `mount` command to attach the remote NFS share to your newly created mount point. The command requires `sudo` privileges because mounting filesystems is a system-level operation.
        - The basic syntax is `mount -t nfs <server>:<remote_directory> <local_mount_point>`.
            - `-t nfs`: Specifies that the filesystem type is NFS.
            - `localhost:/srv/nfs/shared_data`: The source, which is the server and the path it's exporting.
            - `~/project/nfs_mount`: The destination, which is your local mount point.
        - Run the following command to mount the share:
        - `sudo mount -t nfs localhost:/srv/nfs/shared_data ~/project/nfs_mount` Explain Code
        - This command will not produce any output if it is successful.
        - ### **Step 1.3: Verify the Mount and Interact with the Share**
        - After running the `mount` command, you should verify that the share is correctly mounted. You can do this in a few ways.
        - First, use the `mount` command piped to `grep` to filter for NFS mounts:
        - `mount | grep nfs` Explain Code
        - `localhost:/srv/nfs/shared_data on /home/labex/project/nfs_mount type nfs4 (rw,relatime,vers=4.2,rsize=...,wsize=...,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=...,local_lock=none,addr=...)` Explain Code
        - Next, check the contents of your mount point. It should now display the files from the remote `/srv/nfs/shared_data` directory.
        - `ls -l ~/project/nfs_mount` Explain Code
        - ```
total 4
-rw-r--r--. 1 root root 32 Nov 10 14:30 welcome.txt
``` Explain Code
        - You can now interact with this directory as if it were a local folder. Note that in this lab environment, the files are owned by `root` due to the NFS server configuration with `no_root_squash`. In production environments, you might see `nobody` as the owner depending on the NFS server settings. Let's create a new file inside the mounted share. Since the NFS share may be owned by root, you need to use `sudo` with the `tee` command to write files:
        - `echo "My test file" | sudo tee ~/project/nfs_mount/my_file.txt > /dev/null` Explain Code
        - Verify that your new file exists alongside the original one:
        - `ls -l ~/project/nfs_mount` Explain Code
        - ```
total 8
-rw-r--r--. 1 root  root  13 Nov 10 14:35 my_file.txt
-rw-r--r--. 1 root  root  32 Nov 10 14:30 welcome.txt
``` Explain Code
        - ### **Step 1.4: Unmount the NFS Share**
        - When you are finished using a network share, it is important to unmount it cleanly using the `umount` command. This ensures all data is synchronized and the connection is properly closed. You only need to specify the mount point.
        - `sudo umount ~/project/nfs_mount` Explain Code
        - To confirm that the share has been unmounted, list the contents of the `~/project/nfs_mount` directory. It should now be empty again.
        - `ls -l ~/project/nfs_mount` Explain Code
        - `total 0` Explain Code
        - 
        - # **Configure a Persistent NFS Mount in /etc/fstab**
        - In the previous step, you learned how to manually mount an NFS share using the `mount` command. However, such mounts are temporary and will not survive a system reboot. To make a mount permanent, you need to add an entry to the `/etc/fstab` file (short for "file systems table"). This file contains a list of filesystems and devices that are mounted automatically when the system boots.
        - In this step, you will configure the same NFS share to be mounted persistently by adding an entry to `/etc/fstab`.
        - ### **Step 2.1: Prepare the Environment**
        - First, ensure the mount point from the previous step, `~/project/nfs_mount`, exists and is empty. If you are continuing directly from the last step, it should already be there.
        - If the directory does not exist, create it now:
        - `mkdir -p ~/project/nfs_mount` Explain Code
        - Also, ensure that nothing is currently mounted to this directory. You can run the `umount` command, which will report an error if it's not mounted, and that's perfectly fine.
        - `sudo umount ~/project/nfs_mount` Explain Code
        - ### **Step 2.2: Edit the** `**/etc/fstab**` **File**
        - Now, you will add a new line to the `/etc/fstab` file to define the persistent NFS mount. You must use `sudo` to edit this system configuration file. We will use the `nano` editor.
        - Open the file with the following command:
        - `sudo nano /etc/fstab` Explain Code
        - Navigate to the bottom of the file and add the following line. Be very careful with the syntax, as errors in this file can cause system boot issues.
        - `localhost:/srv/nfs/shared_data /home/labex/project/nfs_mount nfs defaults,_netdev 0 0` Explain Code
        - Let's break down this line:
            - `**localhost:/srv/nfs/shared_data**`: This is the device to mount. It specifies the NFS server (`localhost`) and the exported directory (`/srv/nfs/shared_data`).
            - `**/home/labex/project/nfs_mount**`: This is the local mount point where the share will be accessible.
            - `**nfs**`: This specifies the filesystem type.
            - `**defaults,_netdev**`: These are the mount options. `defaults` includes a standard set of options (like `rw` for read-write). `_netdev` is crucial for network filesystems; it tells the system to wait until the network is active before attempting to mount this share.
            - `**0**`: This is the `dump` field, which is used by the `dump` backup utility. A value of `0` disables it.
            - `**0**`: This is the `pass` field, used by the `fsck` utility to determine the order of filesystem checks at boot. A value of `0` means the filesystem will not be checked.
        - After adding the line, save the file and exit `nano` by pressing `Ctrl+X`, then `Y`, and then `Enter`.
        - ### **Step 2.3: Test the** `**/etc/fstab**` **Entry**
        - You don't need to reboot to test your new `/etc/fstab` entry. The `mount` command is smart enough to read `/etc/fstab`. If you provide only the mount point, `mount` will look up the corresponding entry in `/etc/fstab` and use the information it finds there.
        - Mount the share using only the mount point:
        - `sudo mount ~/project/nfs_mount` Explain Code
        - If the command completes without any errors, your `/etc/fstab` entry is correct.
        - ### **Step 2.4: Verify the Mount**
        - Verify that the share is now mounted by checking the output of the `mount` command and listing the contents of the directory.
        - `mount | grep nfs_mount` Explain Code
        - `localhost:/srv/nfs/shared_data on /home/labex/project/nfs_mount type nfs4 (rw,relatime,vers=4.2,rsize=...,wsize=...,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=...,local_lock=none,addr=...,_netdev)` Explain Code
        - Now, check the contents. You should see the files from the share.
        - `ls -l ~/project/nfs_mount` Explain Code
        - ```
total 4
-rw-r--r--. 1 root root 32 Nov 10 14:30 welcome.txt
``` Explain Code
        - This mount is now persistent and would be automatically re-established after a reboot.
        - ### **Step 2.5: Clean Up the Environment**
        - To avoid conflicts with later exercises, you should now reverse the changes. First, unmount the share, and then remove the line you added from `/etc/fstab`.
        - Unmount the directory:
        - `sudo umount ~/project/nfs_mount` Explain Code
        - Open `/etc/fstab` again to remove the entry:
        - `sudo nano /etc/fstab` Explain Code
        - Use the arrow keys to navigate to the line you added (`localhost:/srv/nfs/shared_data ...`), and press `Ctrl+K` to delete the entire line. Then, save and exit by pressing `Ctrl+X`, `Y`, and `Enter`.
        - This leaves the system in a clean state for the next part of the lab.
        - 
        - # **Set Up the Automounter by Installing and Enabling autofs**
        - In the previous steps, you explored manual and persistent mounting. While `/etc/fstab` is great for permanent mounts, it has a drawback: it tries to mount everything at boot time. If a network share is unavailable, it can slow down or even halt the boot process. The automounter, provided by the `autofs` service, solves this problem by mounting network filesystems on-demand, only when they are first accessed.
        - The `autofs` service uses a set of configuration files called "maps" to determine which remote shares to mount and where. In this step, you will prepare your system to use the automounter by installing the necessary package and starting its service.
        - ### **Step 3.1: Install the** `**autofs**` **Package**
        - The `autofs` functionality is not included in the default RHEL installation. You need to install it using the `dnf` package manager. This requires `sudo` privileges.
        - Run the following command to install the `autofs` package. The `-y` flag automatically answers "yes" to the confirmation prompt, which is convenient for this lab.
        - `sudo dnf install -y autofs` Explain Code
        - The command will download and install the `autofs` package and any required dependencies. You will see output similar to the following:
        - ```
Last metadata expiration check: ...
Dependencies resolved.
================================================================================
 Package       Architecture    Version                Repository           Size
================================================================================
Installing:
 autofs        x86_64          1:5.1.7-50.el9         ...                  ...
...

Transaction Summary
================================================================================
Install  1 Package

Total download size: ...
Installed size: ...
...
Complete!
``` Explain Code
        - ### **Step 3.2: Start the** `**autofs**` **Service**
        - On a standard RHEL system, you would use `systemctl` to start and enable services. However, this lab runs in a containerized environment where `systemctl` is not available. Instead, we will start the `autofs` daemon directly using its command, `automount`.
        - This command starts the automounter daemon, which will run in the background and monitor for attempts to access directories that are configured in its maps.
        - Execute the following command to start the service:
        - `sudo automount` Explain Code
        - If successful, this command will not produce any output. It simply starts the daemon process.
        - ### **Step 3.3: Verify the Service is Running**
        - Since you cannot use `systemctl status autofs` to check the service, you can verify that the `automount` process is running using the `ps` command. The `ps aux` command lists all running processes, and we can pipe `|` its output to `grep` to filter for the `automount` process.
        - `ps aux | grep automount` Explain Code
        - You should see at least one line for the `automount` process itself. The second line showing `grep automount` is just the `grep` command you ran, which can be ignored.
        - ```
root      ...  0.0  0.0 ...      ?        Ssl  15:30   0:00 /usr/sbin/automount
labex     ...  0.0  0.0 ...      pts/0    S+   15:31   0:00 grep --color=auto automount
``` Explain Code
        - Seeing the `/usr/sbin/automount` process confirms that the service is running and ready to handle on-demand mounts. In the next steps, you will configure the maps that tell `autofs` what to do.
        - 
        - # **Create an Indirect Automount Map for Dynamic Directories**
        - In this step, you will configure your first automount rule using an **indirect map**. An indirect map is the most common type of automount configuration. It works by associating a single base directory (like `/home` or `/net`) with a map file. When a user tries to access a subdirectory within that base directory, `autofs` looks up the subdirectory's name in the map file and mounts the corresponding remote share on-demand.
        - This is extremely useful for mounting user home directories or a collection of shared project folders without having to mount all of them at once. We will configure an indirect map to dynamically mount project directories located under a new base directory called `/project_shares`.
        - ### **Step 4.1: Create the NFS Server Exports**
        - First, let's prepare the directories on our simulated NFS server that we want to share. We will create two project directories, `design` and `testing`, inside `/srv/nfs/`.
        - Create the directories and place a sample file in each one:
        - ```
sudo mkdir -p /srv/nfs/{design,testing}
sudo sh -c 'echo "Design documents" > /srv/nfs/design/README'
sudo sh -c 'echo "Testing scripts" > /srv/nfs/testing/README'
``` Explain Code
        - Next, we need to tell the NFS server to export these directories. We do this by adding entries to the `/etc/exports` file.
        - Open the file with `nano`:
        - `sudo nano /etc/exports` Explain Code
        - Add the following lines to the file. These lines tell the NFS server to share the `design` and `testing` directories with any client (`*`) with read-write (`rw`) permissions.
        - ```
/srv/nfs/design *(rw,sync,no_root_squash)
/srv/nfs/testing *(rw,sync,no_root_squash)
``` Explain Code
        - Save the file and exit (`Ctrl+X`, `Y`, `Enter`).
        - Finally, apply the changes to the NFS server by re-exporting all directories:
        - `sudo exportfs -ra` Explain Code
        - ### **Step 4.2: Create the Master Map Entry**
        - The `autofs` configuration starts with the master map file, `/etc/auto.master`. The best practice is not to edit this file directly, but to add new configuration files to the `/etc/auto.master.d/` directory.
        - Create a new master map file for our project shares:
        - `sudo nano /etc/auto.master.d/shares.autofs` Explain Code
        - Add the following single line to this file:
        - `/project_shares /etc/auto.shares` Explain Code
        - This line tells `autofs`: "For any access under the `/project_shares` directory, consult the map file located at `/etc/auto.shares` for instructions."
        - Save and exit the editor.
        - ### **Step 4.3: Create the Indirect Map File**
        - Now, create the indirect map file `/etc/auto.shares` that you just referenced in the master map.
        - `sudo nano /etc/auto.shares` Explain Code
        - Add the following lines to this file:
        - ```
design  -fstype=nfs,rw,sync   localhost:/srv/nfs/design
testing -fstype=nfs,rw,sync   localhost:/srv/nfs/testing
``` Explain Code
        - Let's break down a line:
            - `**design**`: This is the "key." It corresponds to the subdirectory name under `/project_shares`. When a user accesses `/project_shares/design`, this line is triggered.
            - `**-fstype=nfs,rw,sync**`: These are the mount options, specifying the filesystem type, read-write access, and synchronous writes.
            - `**localhost:/srv/nfs/design**`: This is the remote NFS share location to be mounted.
        - Save and exit the editor.
        - ### **Step 4.4: Reload** `**autofs**` **and Test the Mount**
        - For the `autofs` service to recognize your new map files, you must reload its configuration. Since `systemctl` is not available, we send the `HUP` (hangup) signal to the `automount` process, which causes it to re-read its configuration.
        - `sudo killall -HUP automount` Explain Code
        - Now, let's test it. First, try to list the contents of the base directory `/project_shares`. It will appear empty because nothing has been mounted yet.
        - `ls -l /project_shares` Explain Code
        - `total 0` Explain Code
        - Next, attempt to access one of the subdirectories. This is the trigger that causes `autofs` to perform the mount.
        - `ls -l /project_shares/design` Explain Code
        - ```
total 4
-rw-r--r--. 1 root root 17 Nov 10 16:10 README
``` Explain Code
        - Success! The `design` share was mounted automatically. Now, if you list the base directory again, you will see the `design` directory because it is an active mount point.
        - `ls -l /project_shares` Explain Code
        - ```
total 0
dr-xr-xr-x. 2 root root 0 Nov 10 16:12 design
``` Explain Code
        - Do the same for the `testing` directory to confirm it also works:
        - `ls -l /project_shares/testing` Explain Code
        - ```
total 4
-rw-r--r--. 1 root root 16 Nov 10 16:10 README
``` Explain Code
        - You have successfully configured and tested an indirect automount map.
        - 
        - # **Create a Direct Automount Map for Static Mount Points**
        - In this step, you will learn about the second type of automount configuration: a **direct map**. Unlike an indirect map, which groups multiple mounts under a common base directory, a direct map defines specific, individual mount points anywhere in the filesystem. Each entry in a direct map corresponds to a single, absolute path.
        - Direct maps are useful for mounting a small number of shares at fixed, well-known locations, such as mounting a shared tools directory at `/usr/local/tools`. We will configure a direct map to mount a shared `common_data` directory to `/mnt/common`.
        - ### **Step 5.1: Prepare the NFS Server Export**
        - As before, we first need to set up the directory on our simulated NFS server that we want to share. We will create a directory named `common_data`.
        - Create the directory and a sample file inside it:
        - ```
sudo mkdir -p /srv/nfs/common_data
sudo sh -c 'echo "Common shared data" > /srv/nfs/common_data/info.txt'
``` Explain Code
        - Now, add an entry to `/etc/exports` to make this directory available via NFS.
        - `sudo nano /etc/exports` Explain Code
        - Add the following new line to the file. This will share the `/srv/nfs/common_data` directory.
        - `/srv/nfs/common_data *(rw,sync,no_root_squash)` Explain Code
        - Save the file and exit (`Ctrl+X`, `Y`, `Enter`).
        - Apply the changes to the NFS server by re-exporting all directories:
        - `sudo exportfs -ra` Explain Code
        - ### **Step 5.2: Create the Master Map Entry for the Direct Map**
        - To use a direct map, you must first reference it from the master map configuration. The special mount point `/-` is used to indicate that the associated map file is a direct map.
        - Create a new master map file for our direct mount:
        - `sudo nano /etc/auto.master.d/direct.autofs` Explain Code
        - Add the following single line to this file:
        - `/- /etc/auto.direct` Explain Code
        - This line tells `autofs`: "Consult the file `/etc/auto.direct` for a list of direct mounts. The mount points are absolute paths defined within that file."
        - Save and exit the editor.
        - ### **Step 5.3: Create the Direct Map File**
        - Now, create the direct map file `/etc/auto.direct` that you just referenced.
        - `sudo nano /etc/auto.direct` Explain Code
        - Add the following line to this file. The format is slightly different from an indirect map.
        - `/mnt/common -fstype=nfs,rw,sync   localhost:/srv/nfs/common_data` Explain Code
        - Let's analyze this line:
            - `**/mnt/common**`: This is the "key," but for a direct map, the key is the **full, absolute path** of the mount point.
            - `**-fstype=nfs,rw,sync**`: These are the mount options, same as before.
            - `**localhost:/srv/nfs/common_data**`: This is the remote NFS share location.
        - Save and exit the editor.
        - ### **Step 5.4: Reload** `**autofs**` **and Test the Direct Mount**
        - Just as you did for the indirect map, you must reload the `autofs` configuration to make it aware of the new direct map.
        - `sudo killall -HUP automount` Explain Code
        - Now, let's test the direct mount. Unlike an indirect map, the mount point `/mnt/common` does not exist on the filesystem until you try to access it.
        - Attempt to access the directory `/mnt/common`. This will trigger `autofs` to create the mount point and mount the share.
        - `ls -l /mnt/common` Explain Code
        - ```
total 4
-rw-r--r--. 1 root root 19 Nov 10 17:00 info.txt
``` Explain Code
        - Success! The direct mount was created on-demand. You can also verify it with the `mount` command:
        - `mount | grep common` Explain Code
        - `localhost:/srv/nfs/common_data on /mnt/common type nfs4 (rw,relatime,vers=4.2,rsize=...,wsize=...,namlen=255,hard,proto=tcp,timeo=600,retrans=2,sec=sys,clientaddr=...,local_lock=none,addr=...)` Explain Code
        - You have now successfully configured both an indirect map for dynamic subdirectories and a direct map for a static, absolute mount point.
        - 
        - # **Verify Direct and Indirect Automounts as Different Users**
        - In this final step, you will verify how the automounter works in a multi-user environment. Automounting makes a share available, but it's the underlying filesystem permissions on the NFS server that control who can actually read or write to the files. You will create a couple of test users, assign them ownership of the respective NFS shares, and then test their access to both the indirect and direct maps.
        - This exercise demonstrates a real-world scenario where different teams (e.g., design and testing) have ownership of their respective shared directories, with read access available to other users but write access restricted to the owner.
        - ### **Step 6.1: Create Test Users and Set Permissions**
        - First, you need to create two new users: `designer1` and `tester1`. You will also set a simple password for them so you can switch to their accounts.
        - Use the `useradd` command to create the users. The `-m` flag creates a home directory for them.
        - ```
sudo useradd -m designer1
sudo useradd -m tester1
``` Explain Code
        - Next, set a password for each user. For simplicity in this lab, we'll use the password `labex.io` for both (meets complexity requirements including length, mixed case, numbers, and special characters).
        - ```
sudo passwd designer1
# Enter new UNIX password: labex.io
# Retype new UNIX password: labex.io
# passwd: password updated successfully

sudo passwd tester1
# Enter new UNIX password: labex.io
# Retype new UNIX password: labex.io
# passwd: password updated successfully
``` Explain Code
        - Now, change the ownership of the shared directories on the "server" side (`/srv/nfs/*`) to grant access to these new users.
        - ```
sudo chown -R designer1:designer1 /srv/nfs/design
sudo chown -R tester1:tester1 /srv/nfs/testing
``` Explain Code
        - The `/srv/nfs/common_data` directory will remain owned by `root`, making it read-only for regular users.
        - ### **Step 6.2: Test Access as the** `**designer1**` **User**
        - Switch to the `designer1` user account using the `su` (substitute user) command. The `-` ensures you get the user's full login environment.
        - ```
su - designer1
# Password: labex.io
``` Explain Code
        - Your command prompt will change to `[designer1@host ~]$`.
        - First, test access to the `design` share via the indirect map. This should succeed.
        - `ls -l /project_shares/design` Explain Code
        - ```
total 4
-rw-r--r--. 1 designer1 designer1 17 Jun 16 16:12 README
``` Explain Code
        - Now, try to write a file to this directory. This should also succeed.
        - ```
echo "My design file" > /project_shares/design/design_file.txt
ls -l /project_shares/design
``` Explain Code
        - ```
total 8
-rw-r--r--. 1 designer1 designer1 15 Jun 16 16:18 design_file.txt
-rw-r--r--. 1 designer1 designer1 17 Jun 16 16:12 README
``` Explain Code
        - Next, attempt to access the `testing` share. You can see the contents, but cannot write to it since it's owned by `tester1`.
        - `ls -l /project_shares/testing` Explain Code
        - ```
total 4
-rw-r--r--. 1 tester1 tester1 16 Jun 16 16:12 README
``` Explain Code
        - Finally, test the direct-mapped share. `designer1` should be able to read it but not write to it.
        - `cat /mnt/common/info.txt` Explain Code
        - `Common shared data` Explain Code
        - `echo "test" > /mnt/common/new_file.txt` Explain Code
        - `-bash: /mnt/common/new_file.txt: Permission denied` Explain Code
        - Exit the `designer1` session to return to the `labex` user.
        - `exit` Explain Code
        - ### **Step 6.3: Test Access as the** `**tester1**` **User**
        - Now, perform similar tests as the `tester1` user.
        - ```
su - tester1
# Password: labex.io
``` Explain Code
        - Access the `design` share. You can see the contents including the file created by `designer1`, but cannot write to it.
        - `ls -l /project_shares/design` Explain Code
        - ```
total 8
-rw-r--r--. 1 designer1 designer1 15 Jun 16 16:18 design_file.txt
-rw-r--r--. 1 designer1 designer1 17 Jun 16 16:12 README
``` Explain Code
        - Now, access and write to the `testing` share. This should succeed since `tester1` owns this directory.
        - `ls -l /project_shares/testing` Explain Code
        - ```
total 4
-rw-r--r--. 1 tester1 tester1 16 Jun 16 16:12 README
``` Explain Code
        - ```
echo "My test script" > /project_shares/testing/test_script.sh
ls -l /project_shares/testing
``` Explain Code
        - ```
total 8
-rw-r--r--. 1 tester1 tester1 16 Jun 16 16:12 README
-rw-r--r--. 1 tester1 tester1 15 Jun 16 16:19 test_script.sh
``` Explain Code
        - Exit the `tester1` session.
        - `exit` Explain Code
        - ### **Step 6.4: Clean Up the Environment**
        - To finish the lab and restore the system to its original state, remove the test users you created. The `userdel -r` command removes the user and their home directory.
        - ```
sudo userdel -r designer1
sudo userdel -r tester1
``` Explain Code
        - This concludes the lab on managing NFS with `autofs`.
        - 
        - # **Summary**
        - In this lab, you will learn to configure NFS client access on a RHEL system. You begin by performing a manual mount, first creating a local mount point and then using the `mount` command to connect to the NFS share. After establishing the manual connection with the `mount` command, you will proceed to configure a persistent mount by creating an entry in the `/etc/fstab` file, ensuring the share is automatically mounted at boot.
        - Furthermore, the lab covers configuring on-demand mounting with the `autofs` service. This involves installing and enabling the service, then defining how shares are mounted using two different methods: creating an indirect map for dynamically mounting directories and a direct map for mounting shares to static, pre-defined locations. The process concludes with verifying that both direct and indirect automounts function correctly for different users.
    8. **Troubleshoot the RHEL Boot Process**
        - Manage Systemd Boot Targets with systemctl
        - Boot into Rescue Mode from the GRUB Menu
        - Reset the Root Password using rd.break and chroot
        - Repair /etc/fstab Errors using Emergency Mode
        - 
        - # **Introduction**
        - In this lab, you will learn essential techniques for troubleshooting and repairing the Red Hat Enterprise Linux (RHEL) boot process. You will explore how to interact with the system at different stages of the boot sequence to diagnose and resolve common problems that can prevent a system from starting correctly. This includes working with systemd boot targets and utilizing specialized boot modes designed for system recovery.
        - Throughout the exercises, you will gain hands-on experience managing systemd targets with `systemctl`, booting into rescue mode from the GRUB menu for system maintenance, and resetting the root password using the `rd.break` kernel parameter. Additionally, you will learn how to use emergency mode to repair critical configuration file errors, such as a corrupted `/etc/fstab`, ensuring you can restore a non-bootable system to an operational state.
        - 
        - # **Manage Systemd Boot Targets with systemctl**
        - In this step, you will learn how to manage `systemd` boot targets. In `systemd`, a "target" is a synchronization point that groups together various services and other units required to bring the system to a certain state. This is the modern equivalent of "runlevels" in older SysV init systems. We will explore how to view the current default target, change the default target for future boots, and temporarily switch to a different target.
        - First, let's check which target your system boots into by default. The `graphical.target` is used for systems with a desktop environment, providing a graphical user interface (GUI). The `multi-user.target` is for a command-line only interface.
        - To see the current default target, run the following command:
        - `systemctl get-default` Explain Code
        - You should see that the default target is the graphical target.
        - `graphical.target` Explain Code
        - Now, let's change the default boot target to `multi-user.target`. This is useful for server environments or for troubleshooting situations where the graphical interface is not needed or is causing issues. The `systemctl set-default` command achieves this by changing the `/etc/systemd/system/default.target` symbolic link.
        - Use `sudo` to execute this command with administrative privileges.
        - `sudo systemctl set-default multi-user.target` Explain Code
        - The output confirms that the symbolic link has been updated.
        - ```
Removed /etc/systemd/system/default.target.
Created symlink /etc/systemd/system/default.target -> /usr/lib/systemd/system/multi-user.target.
``` Explain Code
        - You can verify that the default has been changed by running the `get-default` command again.
        - `systemctl get-default` Explain Code
        - The output now shows the new default target.
        - `multi-user.target` Explain Code
        - With this setting, the system would boot into a text-based console after a reboot. For this lab, we want to maintain a consistent graphical environment. Let's set the default target back to `graphical.target`.
        - `sudo systemctl set-default graphical.target` Explain Code
        - You will see a similar output as before, indicating the symlink has been changed back.
        - ```
Removed /etc/systemd/system/default.target.
Created symlink /etc/systemd/system/default.target -> /usr/lib/systemd/system/graphical.target.
``` Explain Code
        - Run a final check to confirm the default target is restored to `graphical.target`.
        - `systemctl get-default` Explain Code
        - `graphical.target` Explain Code
        - In addition to changing the default target for reboots, you can also switch targets in the current session using `systemctl isolate`. This command stops services not associated with the new target and starts the ones that are. For example, running `sudo systemctl isolate multi-user.target` would terminate your graphical session and switch to a text-only console. This is a powerful but potentially disruptive command, so we will not execute it here.
        - You have now successfully used `systemctl` to manage systemd targets.
        - 
        - # **Boot into Rescue Mode from the GRUB Menu**
        - In this step, you will learn about `rescue.target`, a special `systemd` target designed for system recovery. On a standard RHEL system, you would access this mode by rebooting, interrupting the boot loader (GRUB), and adding a parameter to the kernel's boot options. This provides a single-user shell with the root filesystem mounted and most services disabled, which is ideal for troubleshooting.
        - While we cannot perform a real reboot or access the GRUB menu in this containerized lab environment, we can still explore the configuration of rescue mode to understand how it works.
        - First, let's locate the `systemd` unit file for `rescue.target`. These files are typically stored in the `/usr/lib/systemd/system/` directory.
        - `ls -l /usr/lib/systemd/system/rescue.target` Explain Code
        - You will see the file listed with its permissions and ownership.
        - `-rw-r--r--. 1 root root 500 Nov  1  2022 /usr/lib/systemd/system/rescue.target` Explain Code
        - Now, let's examine the contents of this file to understand its configuration. The `cat` command will display the file's content in the terminal.
        - `cat /usr/lib/systemd/system/rescue.target` Explain Code
        - The output shows the definition of the target.
        - ```
#  SPDX-License-Identifier: LGPL-2.1-or-later
#
#  This file is part of systemd.
#
#  systemd is free software; you can redistribute it and/or modify it
#  under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 2.1 of the License, or
#  (at your option) any later version.

[Unit]
Description=Rescue Mode
Documentation=man:systemd.special(7)
Requires=sysinit.target rescue.service
After=sysinit.target rescue.service
AllowIsolate=yes
``` Explain Code
        - Key directives in this file include:
            - `Description=Rescue Mode`: A human-readable name for the target.
            - `Requires=sysinit.target rescue.service`: This ensures that both `sysinit.target` (basic system initialization) and `rescue.service` are started when this target is activated. The rescue service provides the root maintenance shell.
            - `After=sysinit.target rescue.service`: This specifies the order of activation, ensuring rescue mode starts after system initialization and the rescue service.
            - `AllowIsolate=yes`: This allows you to switch to this target from another target using the `systemctl isolate rescue.target` command in a running system.
        - To get a better idea of the minimal environment that rescue mode provides, you can view its dependencies. The `systemctl list-dependencies` command shows all the units that are started as part of a target.
        - `systemctl list-dependencies rescue.target` Explain Code
        - The output lists the units required for rescue mode. You'll see a minimal set of services, confirming that it's a streamlined environment designed for repair tasks.
        - ```
rescue.target
○ ├─rescue.service
○ ├─systemd-update-utmp-runlevel.service
● └─sysinit.target
●   ├─dev-hugepages.mount
●   ├─dev-mqueue.mount
●   ├─dracut-shutdown.service
○   ├─iscsi-onboot.service
○   ├─iscsi-starter.service
●   ├─kmod-static-nodes.service
●   ├─ldconfig.service
●   ├─lvm2-lvmpolld.socket
... (output may vary) ...
``` Explain Code
        - The key takeaway is that `rescue.target` provides a root shell with the filesystem mounted read-write, enabling you to fix system issues. In the following steps, we will simulate recovery scenarios that rely on similar principles.
        - 
        - # **Reset the Root Password using rd.break and chroot**
        - In this step, you will learn the procedure for resetting a lost root password on a RHEL system. This is a critical recovery skill. The standard method involves interrupting the boot process with the `rd.break` kernel parameter, which gives you access to a shell before the system fully starts.
        - On a physical or virtual machine, you would reboot, interrupt the GRUB boot loader, and add `rd.break` to the end of the `linux` kernel line. This action stops the boot process just before `systemd` takes control, placing you in an `initramfs` shell. From there, the general steps are:
            1. Remount the system's root filesystem (which is mounted read-only at `/sysroot`) in read-write mode with the command `mount -o remount,rw /sysroot`.
            2. Enter a `chroot` jail at `/sysroot` with `chroot /sysroot`. This makes the system's actual root filesystem your current environment, allowing you to run commands that affect the system.
            3. Change the password using the `passwd` command.
            4. Address potential SELinux context issues.
            5. Exit the `chroot` and the `initramfs` shell to continue booting.
        - While we cannot perform a real reboot and use `rd.break` in this lab environment, we will simulate the most important commands you would execute after entering the `chroot` environment.
        - First, let's simulate changing the root password. Imagine you have successfully entered the `chroot` jail. You would now have root access to change any user's password. We will use the `sudo passwd root` command to change the `root` user's password. When prompted, set the new password to `redhat`.
        - `sudo passwd root` Explain Code
        - You will be prompted to enter and re-enter the new password (e.g. `labex.io`).
        - ```
Changing password for user root.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.
``` Explain Code
        - After changing the password in this recovery environment, the SELinux security context on the password file (`/etc/shadow`) can become incorrect. To fix this, you must force a full system SELinux relabel on the next boot. This is done by creating an empty file named `.autorelabel` in the root (`/`) directory.
        - `sudo touch /.autorelabel` Explain Code
        - Let's verify that the file was created.
        - `ls -l /.autorelabel` Explain Code
        - The output should show the newly created file.
        - `-rw-r--r--. 1 root root 0 <date> <time> /.autorelabel` Explain Code
        - On a real system, you would now type `exit` twice and let the system reboot. It would perform the lengthy relabeling process and then boot normally with the new password. Since we don't want to trigger this in our lab, we will clean up by removing the file we just created.
        - `sudo rm /.autorelabel` Explain Code
        - This concludes the simulation of resetting the root password. You have practiced the key commands (`passwd` and `touch /.autorelabel`) that are central to the recovery process.
        - 
        - # **Repair /etc/fstab Errors using Emergency Mode**
        - In this step, you will learn how to diagnose and repair errors in the `/etc/fstab` file. This file is critical for the boot process as it tells the system which filesystems to mount and where. An incorrect entry in `/etc/fstab` can prevent the system from booting, forcing it into `emergency mode`.
        - Emergency mode provides the most minimal environment possible for system repair. Unlike rescue mode, it does not attempt to mount most filesystems or start many services. Crucially, the root filesystem (`/`) is mounted in read-only (`ro`) mode to prevent further damage.
        - While we cannot trigger a real boot failure in this lab, we can simulate the process of finding and fixing an `/etc/fstab` error.
        - First, let's intentionally add a faulty entry to `/etc/fstab`. We will use the `echo` command with `sudo` to append a line that references a non-existent device.
        - `echo '/dev/nonexistent /data xfs defaults 0 0' | sudo tee -a /etc/fstab` Explain Code
        - Now, let's view the contents of `/etc/fstab` to confirm our bad line was added.
        - `cat /etc/fstab` Explain Code
        - You should see the incorrect line at the end of the file.
        - ```
#
# /etc/fstab
# Created by anaconda on <date>
#
# Accessible filesystems, by reference, are maintained under '/dev/disk/'.
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info.
#
# After editing this file, run 'systemctl daemon-reload' to update systemd
# units generated from this file.
#
/dev/vda4 / xfs defaults 0 0
/dev/vda2 /boot xfs defaults 0 0
/dev/vda1 /boot/efi vfat umask=0077,shortname=winnt 0 0
/dev/vda3 swap swap defaults 0 0
/dev/nonexistent /data xfs defaults 0 0
``` Explain Code
        - Next, we will simulate the diagnostic step. The `mount -a` command attempts to mount all filesystems listed in `/etc/fstab` that are not already mounted. Since our entry is invalid, this command will fail.
        - `sudo mount -a` Explain Code
        - The command will produce an error, clearly indicating that the mount point `/data` does not exist. This is similar to the error you would see during a failed boot.
        - `mount: /data: mount point does not exist.` Explain Code
        - Now, let's simulate the repair process. In a real emergency shell, the first step is to remount the root filesystem in read-write mode to allow for changes.
        - `sudo mount -o remount,rw /` Explain Code
        - With the filesystem now writable, you can edit `/etc/fstab` to fix the error. Use the `nano` editor to open the file.
        - `sudo nano /etc/fstab` Explain Code
        - Inside the `nano` editor, use the arrow keys to navigate to the faulty line (`/dev/nonexistent /data xfs defaults 0 0`) and delete it. You can delete the entire line by pressing **Ctrl+k**. Once the line is removed, save the file by pressing **Ctrl+x**, then **y**, and finally **Enter**.
        - To confirm the fix, run `sudo mount -a` again.
        - `sudo mount -a` Explain Code
        - This time, the command should execute silently with no output, which indicates that all valid entries in `/etc/fstab` are correctly mounted. You have successfully repaired the file.
        - 
        - # **Summary**
        - In this lab, you learned essential techniques for troubleshooting the Red Hat Enterprise Linux boot process. You practiced managing `systemd` boot targets, such as viewing the current default and changing it between `graphical.target` and `multi-user.target` using `systemctl`. You also learned how to interrupt the boot sequence to access specialized recovery environments, including booting into rescue mode from the GRUB menu to perform system maintenance tasks in a single-user shell.
        - Furthermore, you executed critical recovery procedures for common system failures. You successfully reset a forgotten root password by using the `rd.break` kernel parameter, remounting the root filesystem with write permissions, and using a `chroot` environment to set a new password, while also addressing SELinux context by creating an `.autorelabel` file. Lastly, you learned to resolve boot failures caused by `/etc/fstab` errors by entering emergency mode, identifying the problematic entry, and commenting it out to allow the system to boot successfully.
    9. **Secure with firewalld and SELinux in RHEL**
        - Configure httpd on a Custom Port and Understand SELinux Context
        - Understanding and Managing SELinux Port Labels with semanage
        - Open a Custom Port in the Firewall with firewall-cmd
        - Verify Access to Standard and Custom Web Server Ports
        - 
        - # **Introduction**
        - In this lab, you will learn how to secure an Apache web server (`httpd`) on Red Hat Enterprise Linux (RHEL) by managing SELinux policies and firewall rules. You will work through a practical scenario where you configure `httpd` to listen on a non-standard port and explore how SELinux and firewall systems manage security for such configurations. This exercise provides hands-on experience with common security administration tasks in an RHEL environment.
        - You will begin by configuring the `httpd` service to run on a custom port and observing how it behaves under SELinux enforcement. You will use the `semanage` command to understand and manage SELinux port labels, ensuring proper security compliance. You will then use `firewall-cmd` to open this custom port in the system's firewall. Finally, you will verify that the web server is accessible, confirming that your security configurations are correctly applied.
        - 
        - # **Configure httpd on a Custom Port and Understand SELinux Context**
        - In this step, you will learn how to configure the Apache web server (`httpd`) to run on a non-standard port and understand how SELinux manages port access. We will work with port 8081 and explore SELinux port management, even if the service starts successfully in some configurations.
        - The necessary packages (`httpd`, `policycoreutils-python-utils`, and `firewalld`) have already been installed in the setup phase. The `policycoreutils-python-utils` package provides the `semanage` command, which you will use in a later step.
        - Let's start by modifying the default `httpd` configuration to listen on a non-standard port, `8081`. The main configuration file for `httpd` is located at `/etc/httpd/conf/httpd.conf`. We will use the `nano` editor to change the listening port.
        - `sudo nano /etc/httpd/conf/httpd.conf` Explain Code
        - Inside the `nano` editor, use the arrow keys to scroll down and find the line that says `Listen 80`. Change this line to:
        - `Listen 8081` Explain Code
        - To save the file and exit `nano`, press `Ctrl+X`, then `Y` to confirm the changes, and finally `Enter` to write to the file.
        - Now, with the configuration changed, let's attempt to start the `httpd` service. In this containerized environment, `systemctl` is not available. We will start the `httpd` daemon directly.
        - `sudo /usr/sbin/httpd` Explain Code
        - You may see a warning message about the server's fully qualified domain name, but this is normal and can be ignored.
        - `AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using fe80::216:3eff:fe02:1a1e%eth0. Set the 'ServerName' directive globally to suppress this message` Explain Code
        - Let's verify if the service is running by checking for `httpd` processes.
        - `ps aux | grep httpd` Explain Code
        - You should see multiple `httpd` processes running, which indicates the web server started successfully.
        - ```
root        4813  0.0  0.2  23364  7736 ?        Ss   09:32   0:00 /usr/sbin/httpd
apache      4814  0.0  0.1  23020  5092 ?        S    09:32   0:00 /usr/sbin/httpd
apache      4815  0.0  0.4 1441064 14620 ?       Sl   09:32   0:00 /usr/sbin/httpd
apache      4816  0.0  0.5 1441064 18736 ?       Sl   09:32   0:00 /usr/sbin/httpd
apache      4837  0.0  0.4 1572200 16872 ?       Sl   09:32   0:00 /usr/sbin/httpd
labex       4996  0.0  0.0   6408  2176 pts/3    S+   09:32   0:00 grep --color=auto httpd
``` Explain Code
        - Let's also check the `httpd` error logs to see what happened during startup.
        - `sudo tail /var/log/httpd/error_log` Explain Code
        - You should see normal startup messages indicating the server is running properly.
        - ```
[Tue Jun 17 09:32:46.374275 2025] [core:notice] [pid 4812:tid 4812] SELinux policy enabled; httpd running as context system_u:system_r:unconfined_service_t:s0
[Tue Jun 17 09:32:46.377265 2025] [suexec:notice] [pid 4812:tid 4812] AH01232: suEXEC mechanism enabled (wrapper: /usr/sbin/suexec)
[Tue Jun 17 09:32:46.394284 2025] [lbmethod_heartbeat:notice] [pid 4813:tid 4813] AH02282: No slotmem from mod_heartmonitor
[Tue Jun 17 09:32:46.399433 2025] [mpm_event:notice] [pid 4813:tid 4813] AH00489: Apache/2.4.62 (Red Hat Enterprise Linux) configured -- resuming normal operations
[Tue Jun 17 09:32:46.399458 2025] [core:notice] [pid 4813:tid 4813] AH00094: Command line: '/usr/sbin/httpd'
``` Explain Code
        - Interestingly, the `httpd` service started without any SELinux issues. Let's check if there were any SELinux denials in the audit log.
        - `sudo grep AVC /var/log/audit/audit.log | grep httpd` Explain Code
        - If there are no results, it means SELinux did not block the httpd service from binding to port 8081. This could be because:
            1. Port 8081 might already be allowed for HTTP services by default in some configurations
            2. The httpd process might be running in an unconfined context
            3. Port 8081 may already be defined in the SELinux policy
        - Let's check the current SELinux mode:
        - `getenforce` Explain Code
        - You should see that SELinux is in "Enforcing" mode, which means it is actively enforcing policies. The fact that httpd started successfully indicates that port 8081 may already have proper SELinux labeling, or the service is running in an unconfined context as shown in the log messages. For the purpose of this learning exercise, let's continue to the next step where we'll explore SELinux port management and ensure proper configuration.
        - 
        - # **Understanding and Managing SELinux Port Labels with semanage**
        - In this step, you will learn how to manage SELinux port labels using the `semanage` command. Even though the `httpd` service is currently running on port 8081, it's important to understand how to properly configure SELinux port policies to ensure security and compliance. You will explore the current port configuration and learn how to explicitly assign the correct SELinux type to custom ports.
        - First, you need to find the correct SELinux type for web server ports. The `semanage port -l` command lists all port definitions known to SELinux. We can pipe this output to `grep` to find types related to `http`.
        - `sudo semanage port -l | grep http` Explain Code
        - The output shows several port types. The most relevant one for a standard web server is `http_port_t`.
        - ```
http_cache_port_t              tcp      8080, 8118, 8123, 10001-10010
http_cache_port_t              udp      3130
http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
pegasus_http_port_t            tcp      5988
pegasus_https_port_t           tcp      5989
``` Explain Code
        - As you can see, `http_port_t` is assigned to standard HTTP/HTTPS ports like `80` and `443`. The SELinux policy allows processes with the `httpd_t` type (our web server) to bind to any port labeled with `http_port_t`. Let's check if port `8081` is already in this list.
        - Notice that port `8081` is not currently listed under `http_port_t`. However, in some RHEL configurations, this port may already be defined in the SELinux policy. Let's try to add it explicitly for proper SELinux compliance using the `semanage port -a` command.
            - The `-a` option means "add".
            - The `-t http_port_t` option specifies the type to assign.
            - The `-p tcp` option specifies the protocol.
        - `sudo semanage port -a -t http_port_t -p tcp 8081` Explain Code
        - You may see a message indicating "Port tcp/8081 already defined, modifying instead", which means the port was already configured. This explains why httpd started successfully in the previous step. To verify the current configuration, list the `http_port_t` definitions again.
        - `sudo semanage port -l | grep '^http_port_t'` Explain Code
        - You should now see port `8081` included in the list.
        - `http_port_t                    tcp      8081, 80, 81, 443, 488, 8008, 8009, 8443, 9000` Explain Code
        - With the SELinux policy explicitly updated, port `8081` is now formally recognized as an HTTP port. The `httpd` service should continue to run without any issues, and you have ensured proper SELinux compliance.
        - Let's verify that the process is still running:
        - `ps aux | grep httpd` Explain Code
        - You should continue to see multiple `httpd` processes, indicating that the web server is running successfully with proper SELinux port labeling.
        - ```
root        4813  0.0  0.2  23364  7736 ?        Ss   09:32   0:00 /usr/sbin/httpd
apache      4814  0.0  0.1  23020  5092 ?        S    09:32   0:00 /usr/sbin/httpd
apache      4815  0.0  0.4 1441064 14620 ?       Sl   09:32   0:00 /usr/sbin/httpd
apache      4816  0.0  0.5 1441064 18736 ?       Sl   09:32   0:00 /usr/sbin/httpd
apache      4837  0.0  0.4 1572200 16872 ?       Sl   09:32   0:00 /usr/sbin/httpd
labex       5215  0.0  0.0   6408  2176 pts/3    S+   09:33   0:00 grep --color=auto httpd
``` Explain Code
        - You have successfully configured the SELinux policy to explicitly allow the `httpd` service to run on port 8081, ensuring proper security compliance.
        - 
        - # **Open a Custom Port in the Firewall with firewall-cmd**
        - In this step, you will configure the system's firewall to allow external connections to your web server on the custom port `8081`. Although the `httpd` service is now running correctly thanks to the SELinux policy change, the `firewalld` service, which manages network traffic rules, is likely blocking incoming requests on this non-standard port by default.
        - The `firewalld` package has already been installed in the setup phase. However, we need to start the firewalld service first. Let's check the current status and start it if needed.
        - `sudo firewall-cmd --list-all` Explain Code
        - If you see "FirewallD is not running", we need to start the firewalld daemon. In this container environment, we start the `firewalld` daemon directly. The `&` at the end runs the process in the background.
        - `sudo /usr/sbin/firewalld &` Explain Code
        - Wait a moment for the service to initialize, then verify it's running:
        - `sudo firewall-cmd --list-all` Explain Code
        - Now you should see the current firewall configuration for the default zone (`public`).
        - Let's test access to the web server from the command line using `curl`. This command attempts to connect to `localhost` on port `8081`.
        - `curl http://localhost:8081` Explain Code
        - You should see the HTML content of your test page, which means the web server is accessible locally. This is expected because firewalld typically allows localhost traffic by default.
        - However, for external access and proper security configuration, we still need to configure the firewall properly for our custom port. While localhost connections typically work regardless of firewall rules, external connections from other machines would be blocked without the proper firewall configuration.
        - First, let's inspect the current rules for the default zone (`public`):
        - ```
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: eth0 eth1
  sources:
  services: cockpit dhcpv6-client ssh
  ports:
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
``` Explain Code
        - Now, add a new rule to allow TCP traffic on port `8081`. Make sure firewalld is running before executing this command.
            - `--add-port=8081/tcp` specifies the port and protocol to open.
            - `--permanent` ensures the rule persists after a reboot or firewall reload.
        - `sudo firewall-cmd --permanent --add-port=8081/tcp` Explain Code
        - If you see "FirewallD is not running", make sure you started the firewalld daemon in the previous step and wait a moment for it to initialize.
        - The command should return `success` when firewalld is running properly.
        - `success` Explain Code
        - Permanent rules are not applied to the active firewall configuration until it is reloaded. Let's reload the firewall to apply our new rule.
        - `sudo firewall-cmd --reload` Explain Code
        - This command should also return `success`.
        - `success` Explain Code
        - Let's verify that the port is now open by listing the rules again.
        - `sudo firewall-cmd --list-all` Explain Code
        - You should now see `8081/tcp` in the `ports:` section.
        - ```
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: eth0 eth1
  sources:
  services: cockpit dhcpv6-client ssh
  ports: 8081/tcp
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
``` Explain Code
        - You have successfully configured the firewall. The final step is to test if you can access the web server.
        - 
        - # **Verify Access to Standard and Custom Web Server Ports**
        - In this final step, you will verify that all the changes you've made ensure your web server is properly configured for both local and external access. You have configured the SELinux policy and opened the necessary port in the firewall. Now, you will perform comprehensive tests to confirm the configuration.
        - First, let's create a simple test page so that when we connect, we get a custom message. The default document root for `httpd` is `/var/www/html`. We will create an `index.html` file in that directory. You will need `sudo` privileges to write to this location.
        - `echo "Success! Web server on custom port 8081 is working." | sudo tee /var/www/html/index.html` Explain Code
        - This command places the success message into the `index.html` file. The `tee` command is used here because it allows us to write to a file that requires `sudo` privileges while using a pipe. You should see the message echoed to the terminal as confirmation.
        - `Success! Web server on custom port 8081 is working.` Explain Code
        - To complete the exercise, let's demonstrate the contrast by attempting to access the standard HTTP port `80`. Since our server is configured to listen only on `8081`, this request should fail.
        - `curl http://localhost:80` Explain Code
        - As expected, the connection is refused because no service is listening on that port.
        - `curl: (7) Failed to connect to localhost port 80: Connection refused` Explain Code
        - This confirms that your server is running exclusively on the custom port you configured. Through this lab, you have learned a critical troubleshooting workflow for services on RHEL:
            1. Check service status and logs.
            2. Investigate SELinux denials in the audit log.
            3. Correct SELinux policies using `semanage`.
            4. Configure firewall rules using `firewall-cmd`.
            5. Verify connectivity.
        - 
        - # **Summary**
        - In this lab, you learned how to configure a web server on a custom port and manage SELinux security policies. With the Apache web server (`httpd`), `policycoreutils-python-utils`, and `firewalld` packages pre-installed, you focused on understanding SELinux port management and firewall configuration. You modified the `httpd.conf` file to change the web server's listening port to a non-standard port, 8081.
        - You discovered that the `httpd` service started successfully on the custom port because port 8081 was already properly configured in the SELinux policy. This provided an opportunity to explore SELinux port management and understand how `semanage` works to maintain proper port labeling. You also learned to use `firewall-cmd` to manage firewall rules, ensuring both security compliance and accessibility. Even though httpd ran in an unconfined context, this lab demonstrated the importance of proper SELinux and firewall configuration for production environments.
    10. **Install and Automate RHEL Deployments**
        - Explore Red Hat Universal Base Images (UBI)
        - Create a Custom RHEL Container Configuration
        - Customize the Container Configuration for Automated Deployment
        - Validate the Container Configuration and Build the Image
        - Create an Automated Deployment Script
        - 
        - # **Introduction**
        - In this lab, you will learn the fundamentals of deploying and automating Red Hat Enterprise Linux (RHEL) 9 containers using Docker. Modern cloud-native deployments increasingly rely on containerized RHEL environments rather than traditional virtual machines. You will start by exploring Red Hat's Universal Base Images (UBI), which provide enterprise-grade RHEL environments in container format.
        - You will examine how traditional Kickstart concepts translate to container automation, create custom Dockerfiles that mirror installation configurations, and build automated deployment scripts. By the end of this lab, you will understand how to deploy RHEL containers efficiently and automate the process for consistent, repeatable deployments in modern cloud environments.
        - 
        - # **Explore Red Hat Universal Base Images (UBI)**
        - In this step, you will explore Red Hat's Universal Base Images (UBI), which are enterprise-grade container images based on RHEL. Unlike traditional RHEL installations that require full virtual machines, UBI images provide RHEL environments in lightweight, portable containers. These images are freely redistributable and designed for modern cloud-native applications.
        - Red Hat provides several UBI variants optimized for different use cases. The `redhat/ubi9` image provides a full RHEL-based container environment with the `dnf` package manager, making it suitable for applications requiring software installation and system automation.
        - First, let's examine the Red Hat container configuration template that has been prepared for this lab. This file demonstrates how traditional Kickstart concepts translate to container environments.
        - `sudo cat /etc/labex/rhel-container-config.cfg` Explain Code
        - You will see output showing a Dockerfile-style configuration that mirrors traditional installation concepts:
        - ```
# RHEL Container Configuration Template
# Based on traditional Kickstart concepts adapted for containers

# Base image specification
FROM redhat/ubi9

# System locale and timezone
ENV LANG=en_US.UTF-8
ENV TZ=America/New_York

# User configuration
ENV CONTAINER_USER=labex
ENV ROOT_PASSWORD=redhat

# Package installation
# Packages: httpd, curl (container-appropriate equivalents)
RUN dnf install -y --allowerasing httpd curl && \
    dnf clean all

# Service configuration
EXPOSE 80

# Startup command
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]
``` Explain Code
        - Now, let's explore the available Red Hat UBI images. First, check if Docker is running and accessible:
        - `docker --version` Explain Code
        - Pull the Red Hat UBI 9 image, which provides a full RHEL-based container environment:
        - `docker pull redhat/ubi9` Explain Code
        - You should see output similar to:
        - ```
Using default tag: latest
latest: Pulling from redhat/ubi9
Digest: sha256:...
Status: Downloaded newer image for redhat/ubi9:latest
docker.io/redhat/ubi9:latest
``` Explain Code
        - List the downloaded images to confirm the pull was successful:
        - `docker images redhat/ubi9` Explain Code
        - The output will show details about the image:
        - ```
REPOSITORY      TAG       IMAGE ID       CREATED      SIZE
redhat/ubi9     latest    b1c2d3e4f5g6   5 days ago   216MB
``` Explain Code
        - Now, let's run a basic container to explore the RHEL environment:
        - `docker run -it --rm redhat/ubi9 /bin/bash` Explain Code
        - Inside the container, explore the RHEL environment by checking the operating system version:
        - `cat /etc/redhat-release` Explain Code
        - You should see something like:
        - `Red Hat Enterprise Linux release 9.6 (Plow)` Explain Code
        - Check the available package manager:
        - `dnf --version` Explain Code
        - Exit the container by typing:
        - `exit` Explain Code
        - Copy the template configuration to your project directory for customization:
        - ```
sudo cp /etc/labex/rhel-container-config.cfg ~/project/rhel-container.dockerfile
sudo chown labex:labex ~/project/rhel-container.dockerfile
``` Explain Code
        - Verify the file was copied successfully:
        - `ls -l ~/project/rhel-container.dockerfile` Explain Code
        - You have now successfully explored Red Hat UBI images and are ready to create custom container configurations in the next step.
        - 
        - # **Create a Custom RHEL Container Configuration**
        - In this step, you will create a custom Dockerfile based on the Red Hat UBI image. This process mirrors how you would customize a Kickstart file for automated installations, but adapted for container environments. The Dockerfile serves as the automation template for creating consistent RHEL container deployments.
        - First, ensure you are in your project directory:
        - `cd ~/project` Explain Code
        - Create a new, more specific Dockerfile for our automated RHEL container deployment:
        - `cp rhel-container.dockerfile rhel9-automated.dockerfile` Explain Code
        - Verify both files exist:
        - `ls -l *.dockerfile` Explain Code
        - You should see both files:
        - ```
-rw-r--r--. 1 labex labex 423 Jul 22 10:30 rhel-container.dockerfile
-rw-r--r--. 1 labex labex 423 Jul 22 10:35 rhel9-automated.dockerfile
``` Explain Code
        - Now, open the new Dockerfile to examine its structure before customization:
        - `nano rhel9-automated.dockerfile` Explain Code
        - Inside the file, you'll see the container equivalent of Kickstart directives:
            - **FROM directive**: Specifies the base RHEL image (equivalent to installation media)
            - **ENV directives**: Set environment variables (equivalent to system configuration)
            - **RUN directives**: Execute commands during image build (equivalent to package installation)
            - **EXPOSE and CMD**: Configure services and startup (equivalent to service configuration)
        - For now, simply exit the editor by pressing `Ctrl+X` to proceed to the customization step.
        - Understanding this structure prepares you for the next step where you'll customize the container configuration to meet specific deployment requirements, just as you would customize a Kickstart file for automated VM installations.
        - 
        - # **Customize the Container Configuration for Automated Deployment**
        - In this step, you will replace the contents of the `rhel9-automated.dockerfile` with a custom configuration for automated RHEL container deployment. This process parallels customizing a Kickstart file, but uses Docker's declarative approach to define the container environment and services.
        - First, ensure you are in the project directory:
        - `cd ~/project` Explain Code
        - Now, create the complete custom Dockerfile by replacing the entire contents of `rhel9-automated.dockerfile`:
        - ```
cat > rhel9-automated.dockerfile << 'EOF'
# RHEL 9 Automated Container Deployment
# Based on Red Hat Universal Base Image 9
FROM redhat/ubi9:latest

# Container metadata
LABEL maintainer="LabEx Admin"
LABEL description="Automated RHEL 9 container with web services"
LABEL version="1.0"

# System locale and timezone configuration
ENV LANG=en_US.UTF-8
ENV TZ=America/New_York
ENV CONTAINER_USER=labex
ENV CONTAINER_UID=1001

# Package installation and system configuration
RUN dnf update -y \
  && dnf install -y --allowerasing \
    httpd \
    curl \
    tar \
    gzip \
  && dnf clean all \
  && rm -rf /var/cache/dnf

# Create non-root user for security
RUN useradd -u ${CONTAINER_UID} -m -s /bin/bash ${CONTAINER_USER} \
  && echo "${CONTAINER_USER}:labex" | chpasswd

# Configure Apache for container environment
RUN sed -i 's/Listen 80/Listen 8080/' /etc/httpd/conf/httpd.conf \
  && chown -R ${CONTAINER_USER}:${CONTAINER_USER} /var/log/httpd /var/run/httpd

# Create startup script
RUN echo '#!/bin/bash' > /start.sh \
  && echo 'echo "RHEL Container started on $(date)" > /var/www/html/index.html' >> /start.sh \
  && echo 'echo "<h1>RHEL 9 Container</h1><p>Deployed via automated configuration</p>" >> /var/www/html/index.html' >> /start.sh \
  && echo 'exec /usr/sbin/httpd -D FOREGROUND' >> /start.sh \
  && chmod +x /start.sh

# Switch to non-root user
USER ${CONTAINER_USER}

# Expose port and define startup
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/ || exit 1

CMD ["/start.sh"]
EOF
``` Explain Code
        - Now let's examine the structure of this customized Dockerfile and understand how each section serves the same purpose as different parts of a Kickstart configuration:
        - **1. Base Image and Metadata Section:**
        - ```
# RHEL 9 Automated Container Deployment
# Based on Red Hat Universal Base Image 9
FROM redhat/ubi9:latest

# Container metadata
LABEL maintainer="LabEx Admin"
LABEL description="Automated RHEL 9 container with web services"
LABEL version="1.0"
``` Explain Code
        - This section is equivalent to specifying the installation media and basic system information in a Kickstart file. The `FROM` directive specifies our base RHEL image, while `LABEL` directives provide metadata about the container.
        - **2. Environment Configuration:**
        - ```
# System locale and timezone configuration
ENV LANG=en_US.UTF-8
ENV TZ=America/New_York
ENV CONTAINER_USER=labex
ENV CONTAINER_UID=1001
``` Explain Code
        - This parallels the `timezone` and `lang` directives in Kickstart files. We're setting the system locale, timezone, and defining variables for user creation.
        - **3. Package Installation:**
        - ```
# Package installation and system configuration
RUN dnf update -y \
  && dnf install -y --allowerasing \
    httpd \
    curl \
    tar \
    gzip \
  && dnf clean all \
  && rm -rf /var/cache/dnf
``` Explain Code
        - This section performs the same function as the `%packages` section in Kickstart. We update the system, install required packages using `--allowerasing` to handle conflicts, and clean up package caches to reduce image size.
        - **4. User and Security Configuration:**
        - ```
# Create non-root user for security
RUN useradd -u ${CONTAINER_UID} -m -s /bin/bash ${CONTAINER_USER} \
  && echo "${CONTAINER_USER}:labex" | chpasswd

# Configure Apache for container environment
RUN sed -i 's/Listen 80/Listen 8080/' /etc/httpd/conf/httpd.conf \
  && chown -R ${CONTAINER_USER}:${CONTAINER_USER} /var/log/httpd /var/run/httpd
``` Explain Code
        - This mirrors the `user` directive and post-installation configuration in Kickstart. We create a non-root user for security and configure Apache to run on port 8080 (suitable for container environments).
        - **5. Startup Configuration:**
        - ```
# Create startup script
RUN echo '#!/bin/bash' > /start.sh \
  && echo 'echo "RHEL Container started on $(date)" > /var/www/html/index.html' >> /start.sh \
  && echo 'echo "<h1>RHEL 9 Container</h1><p>Deployed via automated configuration</p>" >> /var/www/html/index.html' >> /start.sh \
  && echo 'exec /usr/sbin/httpd -D FOREGROUND' >> /start.sh \
  && chmod +x /start.sh

# Switch to non-root user
USER ${CONTAINER_USER}

# Expose port and define startup
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/ || exit 1

CMD ["/start.sh"]
``` Explain Code
        - This final section is equivalent to the `%post` section and service configuration in Kickstart. We create a startup script, switch to the non-root user, expose the web service port, define health checks, and specify the container's startup command.
        - Verify the new Dockerfile was created correctly:
        - `cat rhel9-automated.dockerfile` Explain Code
        - You should see the complete Dockerfile content that demonstrates how traditional Kickstart automation concepts translate to modern container-based RHEL deployments.
        - 
        - # **Validate the Container Configuration and Build the Image**
        - In this step, you will validate your custom Dockerfile and build the RHEL container image. This process is similar to validating a Kickstart file with `ksvalidator`, but uses Docker's built-in validation during the build process. Docker will check the syntax and attempt to execute each instruction, providing immediate feedback on any issues.
        - First, ensure you are in the project directory where your Dockerfile is located:
        - `cd ~/project` Explain Code
        - Before building, let's perform a basic syntax check by examining the Dockerfile structure. Docker provides a way to validate the basic syntax without building:
        - `docker build --no-cache --progress=plain -f rhel9-automated.dockerfile -t rhel9-test:validation . --target ""` Explain Code
        - However, the most effective validation is to actually build the image. If there are syntax errors or issues with the commands, Docker will report them during the build process. Note that we use the `--allowerasing` flag with `dnf install` to handle package conflicts between `curl` and `curl-minimal` that exist in the base UBI9 image:
        - `docker build -t rhel9-automated:latest -f rhel9-automated.dockerfile .` Explain Code
        - You should see output showing each step of the build process:
        - ```
[+] Building 45.2s (12/12) FINISHED
 => [internal] load build definition from rhel9-automated.dockerfile
 => => transferring dockerfile: 1.23kB
 => [internal] load .dockerignore
 => => transferring context: 2B
 => [internal] load metadata for docker.io/redhat/ubi9:latest
 => [1/8] FROM docker.io/redhat/ubi9:latest@sha256:...
 => [2/8] RUN dnf update -y &&     dnf install -y --allowerasing         httpd         curl         tar         gzip &&     dnf clean all &&     rm -rf /var/cache/dnf
 => [3/8] RUN useradd -u 1001 -m -s /bin/bash labex &&     echo "labex:labex" | chpasswd
 => [4/8] RUN sed -i 's/Listen 80/Listen 8080/' /etc/httpd/conf/httpd.conf &&     chown -R labex:labex /var/log/httpd /var/run/httpd
 => [5/8] RUN echo '#!/bin/bash' > /start.sh &&     echo 'echo "RHEL Container started on $(date)" > /var/www/html/index.html' >> /start.sh &&     echo 'echo "<h1>RHEL 9 Container</h1><p>Deployed via automated configuration</p>" >> /var/www/html/index.html' >> /start.sh &&     echo 'exec /usr/sbin/httpd -D FOREGROUND' >> /start.sh &&     chmod +x /start.sh
 => [6/8] USER labex
 => exporting to image
 => => exporting layers
 => => writing image sha256:a1b2c3d4e5f6...
 => => naming to docker.io/library/rhel9-automated:latest
``` Explain Code
        - If the build completes successfully, it means your Dockerfile syntax is correct and all commands executed properly. You may see some warning messages about locale settings and subscription management during the build process - these are normal for UBI containers and don't affect functionality.
        - Verify the image was created:
        - `docker images rhel9-automated` Explain Code
        - You should see your newly built image:
        - ```
REPOSITORY       TAG       IMAGE ID       CREATED          SIZE
rhel9-automated  latest    a1b2c3d4e5f6   2 minutes ago    280MB
``` Explain Code
        - Now let's test the container to ensure it works as expected. Run the container in detached mode:
        - `docker run -d --name rhel9-test -p 8080:8080 rhel9-automated:latest` Explain Code
        - Check if the container is running:
        - `docker ps` Explain Code
        - You should see your container in the list:
        - ```
CONTAINER ID   IMAGE                     COMMAND      CREATED         STATUS         PORTS                    NAMES
a1b2c3d4e5f6   rhel9-automated:latest   "/start.sh"  30 seconds ago  Up 30 seconds  0.0.0.0:8080->8080/tcp   rhel9-test
``` Explain Code
        - Test the web service by making a request to the container:
        - `curl http://localhost:8080` Explain Code
        - You should see the HTML output from your automated RHEL container:
        - ```
RHEL Container started on Wed Jul 22 14:30:15 UTC 2024
<h1>RHEL 9 Container</h1><p>Deployed via automated configuration</p>
``` Explain Code
        - Finally, clean up by stopping and removing the test container:
        - ```docker
stop rhel9-test
docker rm rhel9-test
``` Explain Code
        - Your RHEL container configuration has been successfully validated and tested, demonstrating automated deployment capabilities.
        - 
        - # **Create an Automated Deployment Script**
        - In this step, you will create an automation script that demonstrates how to deploy RHEL containers consistently and repeatedly. This script serves the same purpose as using Kickstart files for VM automation but is adapted for containerized RHEL deployments. The script will handle image building, container deployment, and basic health checking.
        - First, ensure you are in your project directory:
        - `cd ~/project` Explain Code
        - Create a deployment automation script that mimics the automation capabilities you would achieve with Kickstart and `virt-install`:
        - `nano deploy-rhel-container.sh` Explain Code
        - Add the following content to create a comprehensive deployment script:
        - ```
#!/bin/bash

# RHEL Container Automated Deployment Script
# This script demonstrates container-based RHEL deployment automation
# Similar to Kickstart automation for VMs, but for containers

set -e # Exit on any error

# Configuration variables
IMAGE_NAME="rhel9-automated"
IMAGE_TAG="latest"
CONTAINER_NAME="rhel9-production"
HOST_PORT="8080"
CONTAINER_PORT="8080"
DOCKERFILE="rhel9-automated.dockerfile"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
  echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
  echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
  echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
  echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if Docker is running
check_docker() {
  print_status "Checking Docker availability..."
  if ! docker info > /dev/null 2>&1; then
    print_error "Docker is not running or not accessible"
    exit 1
  fi
  print_success "Docker is available"
}

# Function to build the image
build_image() {
  print_status "Building RHEL container image..."
  if [ ! -f "$DOCKERFILE" ]; then
    print_error "Dockerfile '$DOCKERFILE' not found"
    exit 1
  fi

  docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" -f "$DOCKERFILE" .
  print_success "Image '${IMAGE_NAME}:${IMAGE_TAG}' built successfully"
}

# Function to stop and remove existing container
cleanup_existing() {
  print_status "Checking for existing container..."
  if docker ps -a | grep -q "$CONTAINER_NAME"; then
    print_warning "Stopping and removing existing container '$CONTAINER_NAME'"
    docker stop "$CONTAINER_NAME" > /dev/null 2>&1 || true
    docker rm "$CONTAINER_NAME" > /dev/null 2>&1 || true
  fi
}

# Function to deploy the container
deploy_container() {
  print_status "Deploying RHEL container..."
  docker run -d \
    --name "$CONTAINER_NAME" \
    -p "${HOST_PORT}:${CONTAINER_PORT}" \
    --restart unless-stopped \
    "${IMAGE_NAME}:${IMAGE_TAG}"

  print_success "Container '$CONTAINER_NAME' deployed successfully"
}

# Function to verify deployment
verify_deployment() {
  print_status "Verifying container deployment..."

  # Wait for container to start
  sleep 5

  # Check if container is running
  if ! docker ps | grep -q "$CONTAINER_NAME"; then
    print_error "Container is not running"
    docker logs "$CONTAINER_NAME"
    exit 1
  fi

  # Check if web service is responding
  print_status "Testing web service..."
  for i in {1..10}; do
    if curl -s "http://localhost:${HOST_PORT}" > /dev/null; then
      print_success "Web service is responding"
      break
    fi
    if [ $i -eq 10 ]; then
      print_error "Web service is not responding after 10 attempts"
      exit 1
    fi
    sleep 2
  done
}

# Function to display deployment information
show_deployment_info() {
  print_success "=== RHEL Container Deployment Complete ==="
  echo "Container Name: $CONTAINER_NAME"
  echo "Image: ${IMAGE_NAME}:${IMAGE_TAG}"
  echo "Port Mapping: ${HOST_PORT}:${CONTAINER_PORT}"
  echo "Access URL: http://localhost:${HOST_PORT}"
  echo ""
  print_status "Container Status:"
  docker ps | grep "$CONTAINER_NAME"
  echo ""
  print_status "Sample Content:"
  curl -s "http://localhost:${HOST_PORT}" | head -2
}

# Main deployment process
main() {
  echo "=== RHEL Container Automated Deployment ==="
  echo "This script automates RHEL container deployment"
  echo "Similar to Kickstart automation for traditional installations"
  echo ""

  check_docker
  build_image
  cleanup_existing
  deploy_container
  verify_deployment
  show_deployment_info

  print_success "Automated RHEL container deployment completed successfully!"
}

# Handle script arguments
case "${1:-deploy}" in
  "deploy" | "")
    main
    ;;
  "cleanup")
    print_status "Cleaning up deployment..."
    cleanup_existing
    docker rmi "${IMAGE_NAME}:${IMAGE_TAG}" 2> /dev/null || true
    print_success "Cleanup completed"
    ;;
  "status")
    docker ps | grep "$CONTAINER_NAME" || print_warning "Container not running"
    ;;
  *)
    echo "Usage: $0 [deploy|cleanup|status]"
    echo "  deploy  - Build and deploy RHEL container (default)"
    echo "  cleanup - Stop container and remove image"
    echo "  status  - Show container status"
    exit 1
    ;;
esac
``` Explain Code
        - Save the file and exit nano (`Ctrl+X`, then `Y`, then `Enter`).
        - ## **Understanding the Deployment Script Structure**
        - Before running the script, let's understand how this automation script works. This section provides a detailed explanation of each component, making it easier for beginners to understand shell scripting and container automation concepts.
        - ### **Script Header and Error Handling**
        - ```
#!/bin/bash
set -e # Exit on any error
``` Explain Code
            - `#!/bin/bash`: This is called a "shebang" - it tells the system to use the Bash shell to execute this script
            - `set -e`: This makes the script exit immediately if any command fails, ensuring the script stops at the first error rather than continuing with potentially broken state
        - ### **Configuration Variables**
        - ```
# Configuration variables
IMAGE_NAME="rhel9-automated"
IMAGE_TAG="latest"
CONTAINER_NAME="rhel9-production"
HOST_PORT="8080"
CONTAINER_PORT="8080"
DOCKERFILE="rhel9-automated.dockerfile"
``` Explain Code
        - These variables define all the key parameters for our deployment. By putting them at the top, we can easily modify the deployment configuration without changing the script logic. This is similar to how Kickstart files use configuration parameters.
        - ### **User-Friendly Output System**
        - ```
# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
  echo -e "${BLUE}[INFO]${NC} $1"
}
``` Explain Code
        - This creates a professional logging system with colored output:
            - `\033[0;31m`: ANSI escape codes for colors (31 = red, 32 = green, etc.)
            - `echo -e`: The `-e` flag enables interpretation of backslash escapes for colors
            - `$1`: Refers to the first argument passed to the function
        - ### **Core Deployment Functions**
        - **1. Docker Environment Check**
        - ```
check_docker() {
  print_status "Checking Docker availability..."
  if ! docker info > /dev/null 2>&1; then
    print_error "Docker is not running or not accessible"
    exit 1
  fi
  print_success "Docker is available"
}
``` Explain Code
            - `docker info > /dev/null 2>&1`: Runs `docker info` and redirects both output (`>`) and errors (`2>&1`) to `/dev/null` (discards them)
            - `!`: Negates the result - if `docker info` fails (returns non-zero), the condition becomes true
            - This is equivalent to checking if virtualization is available in traditional VM deployments
        - **2. Image Building Function**
        - ```
build_image() {
  print_status "Building RHEL container image..."
  if [ ! -f "$DOCKERFILE" ]; then
    print_error "Dockerfile '$DOCKERFILE' not found"
    exit 1
  fi

  docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" -f "$DOCKERFILE" .
  print_success "Image '${IMAGE_NAME}:${IMAGE_TAG}' built successfully"
}
``` Explain Code
            - `[ ! -f "$DOCKERFILE" ]`: Tests if the Dockerfile does NOT exist (`!` negates, `-f` tests for file existence)
            - `docker build -t`: Creates a container image with a tag (name:version)
            - This replaces the traditional installation process from ISO media
        - **3. Cleanup Function**
        - ```
cleanup_existing() {
  print_status "Checking for existing container..."
  if docker ps -a | grep -q "$CONTAINER_NAME"; then
    print_warning "Stopping and removing existing container '$CONTAINER_NAME'"
    docker stop "$CONTAINER_NAME" > /dev/null 2>&1 || true
    docker rm "$CONTAINER_NAME" > /dev/null 2>&1 || true
  fi
}
``` Explain Code
            - `docker ps -a | grep -q`: Lists all containers and quietly searches for our container name
            - `|| true`: Ensures the command always succeeds (returns 0) even if the container doesn't exist
            - This prevents conflicts with existing deployments
        - **4. Container Deployment**
        - ```
deploy_container() {
  print_status "Deploying RHEL container..."
  docker run -d \
    --name "$CONTAINER_NAME" \
    -p "${HOST_PORT}:${CONTAINER_PORT}" \
    --restart unless-stopped \
    "${IMAGE_NAME}:${IMAGE_TAG}"

  print_success "Container '$CONTAINER_NAME' deployed successfully"
}
``` Explain Code
            - `-d`: Runs container in detached mode (background)
            - `-p "${HOST_PORT}:${CONTAINER_PORT}"`: Maps host port to container port
            - `--restart unless-stopped`: Automatically restart container if it stops (except manual stops)
            - `\`: Line continuation character for multi-line commands
        - **5. Health Verification**
        - ```
verify_deployment() {
  print_status "Verifying container deployment..."

  # Wait for container to start
  sleep 5

  # Check if container is running
  if ! docker ps | grep -q "$CONTAINER_NAME"; then
    print_error "Container is not running"
    docker logs "$CONTAINER_NAME"
    exit 1
  fi

  # Check if web service is responding
  print_status "Testing web service..."
  for i in {1..10}; do
    if curl -s "http://localhost:${HOST_PORT}" > /dev/null; then
      print_success "Web service is responding"
      break
    fi
    if [ $i -eq 10 ]; then
      print_error "Web service is not responding after 10 attempts"
      exit 1
    fi
    sleep 2
  done
}
``` Explain Code
            - `{1..10}`: Bash brace expansion - creates sequence 1, 2, 3... 10
            - `curl -s`: Silent mode HTTP request
            - `break`: Exits the loop early when service responds
            - This implements a retry mechanism with timeout
        - ### **Command-Line Interface**
        - ```
case "${1:-deploy}" in
  "deploy" | "")
    main
    ;;
  "cleanup")
    print_status "Cleaning up deployment..."
    cleanup_existing
    docker rmi "${IMAGE_NAME}:${IMAGE_TAG}" 2> /dev/null || true
    print_success "Cleanup completed"
    ;;
  "status")
    docker ps | grep "$CONTAINER_NAME" || print_warning "Container not running"
    ;;
  *)
    echo "Usage: $0 [deploy|cleanup|status]"
    exit 1
    ;;
esac
``` Explain Code
            - `${1:-deploy}`: Parameter expansion - uses `$1` (first argument) or "deploy" as default
            - `case` statement: Similar to switch/case in other languages
            - `;;`: Terminates each case branch
            - `$0`: Refers to the script name itself
        - This creates a versatile script that can be used for multiple operations, similar to how system administrators use different tools for deployment, maintenance, and monitoring.
        - Make the script executable:
        - `chmod +x deploy-rhel-container.sh` Explain Code
        - Now run the automated deployment script to see the complete automation process:
        - `./deploy-rhel-container.sh` Explain Code
        - You should see output showing the complete deployment process:
        - ```
=== RHEL Container Automated Deployment ===
This script automates RHEL container deployment
Similar to Kickstart automation for traditional installations

[INFO] Checking Docker availability...
[SUCCESS] Docker is available
[INFO] Building RHEL container image...
[SUCCESS] Image 'rhel9-automated:latest' built successfully
[INFO] Checking for existing container...
[INFO] Deploying RHEL container...
[SUCCESS] Container 'rhel9-production' deployed successfully
[INFO] Verifying container deployment...
[INFO] Testing web service...
[SUCCESS] Web service is responding
[SUCCESS] === RHEL Container Deployment Complete ===
Container Name: rhel9-production
Image: rhel9-automated:latest
Port Mapping: 8080:8080
Access URL: http://localhost:8080
``` Explain Code
        - Test the different script options:
        - `./deploy-rhel-container.sh status` Explain Code
        - ## **Script Execution Walkthrough**
        - When you run the script, it executes the following sequence automatically:
        - ### **1. Environment Validation Phase**
        - The script first checks if Docker is available and accessible. This is crucial because container deployment requires a working Docker environment, similar to how VM deployment requires a working hypervisor.
        - ### **2. Image Building Phase**
        - The script builds a new container image from your Dockerfile. This process:
            - Reads the `rhel9-automated.dockerfile`
            - Downloads the base UBI9 image if not already present
            - Executes each instruction in the Dockerfile
            - Creates a new image tagged as `rhel9-automated:latest`
        - ### **3. Cleanup Phase**
        - Before deploying, the script checks for and removes any existing container with the same name. This ensures a clean deployment without naming conflicts.
        - ### **4. Deployment Phase**
        - The script creates and starts the new container with:
            - **Detached mode**: Container runs in the background
            - **Port mapping**: Host port 8080 maps to container port 8080
            - **Restart policy**: Container automatically restarts if it stops unexpectedly
            - **Named container**: Easy identification and management
        - ### **5. Verification Phase**
        - The script performs health checks to ensure successful deployment:
            - **Container status check**: Verifies the container is running
            - **Service availability check**: Tests HTTP service response
            - **Retry mechanism**: Attempts up to 10 times with 2-second intervals
            - **Automatic failure detection**: Exits with error if verification fails
        - ### **6. Information Display Phase**
        - Finally, the script displays comprehensive deployment information including container details, access URLs, and sample content.
        - ## **Practical Usage Examples**
        - You can use this script in various ways:
        - **Normal deployment:**
        - ```
./deploy-rhel-container.sh
# or explicitly
./deploy-rhel-container.sh deploy
``` Explain Code
        - **Check deployment status:**
        - `./deploy-rhel-container.sh status` Explain Code
        - **Clean up resources:**
        - `./deploy-rhel-container.sh cleanup` Explain Code
        - **View script help:**
        - `./deploy-rhel-container.sh help` Explain Code
        - ## **Benefits Over Traditional Methods**
        - This automation approach provides several advantages compared to traditional Kickstart + VM deployments:
            1. **Speed**: Container startup is typically 10-100x faster than VM boot
            2. **Resource Efficiency**: Containers share the host kernel, using less memory and CPU
            3. **Consistency**: Same container runs identically across different environments
            4. **Scalability**: Easy to create multiple instances or scale horizontally
            5. **Portability**: Can run on any system with Docker installed
            6. **Version Control**: Container images can be versioned and stored in registries
        - This automation script demonstrates how modern container-based RHEL deployments can achieve the same level of automation and consistency as traditional Kickstart-based VM installations, but with the added benefits of containerization such as faster deployment, better resource utilization, and easier scaling in modern cloud environments.
        - 
        - # **Summary**
        - In this lab, you explored the modern approach to automating Red Hat Enterprise Linux (RHEL) 9 deployments using Docker containers and Red Hat Universal Base Images (UBI). You learned that while traditional RHEL deployments relied on Kickstart files and virtual machines, modern cloud-native environments increasingly use containerized RHEL through UBI images like `redhat/ubi9`.
        - You practiced translating traditional Kickstart concepts to container automation by creating custom Dockerfiles that define system configuration, package installation, user management, and service configuration. Instead of using `ksvalidator` for Kickstart files, you learned to validate container configurations through Docker's build process, which provides immediate feedback on syntax and execution errors.
        - Finally, you created a comprehensive automation script that demonstrates end-to-end container deployment, similar to using `virt-install` with Kickstart files for VM automation. This approach provides the same level of automation and consistency as traditional methods while offering the benefits of containerization: faster deployment, better resource utilization, portability, and easier scaling in modern cloud environments.
    11. **Run Containers with Podman on RHEL**
        - Run a MariaDB Database Container with Environment Variables
        - Configure Persistent Storage for the MariaDB Container
        - Create a Custom Network and Deploy an Apache Web Server
        - Expose the Web Server Port and Test Connectivity
        - Manage the Web Server Container as a systemd Service
        - 
        - # **Introduction**
        - In this lab, you will learn how to deploy a multi-tier web application using Podman on Red Hat Enterprise Linux (RHEL). You will build a complete solution by deploying a MariaDB database container as the backend and an Apache web server container as the frontend. This hands-on experience will guide you through the essential steps of containerized application deployment, from initial configuration to making the service publicly accessible.
        - You will begin by running a MariaDB container and configuring it at startup with environment variables. Next, you will configure persistent storage to ensure data durability for the database and create a custom network for container communication. You will then deploy the Apache web server, expose its port to test connectivity, and finally, learn how to manage the container as a systemd service for robust, automated operation.
        - 
        - # **Run a MariaDB Database Container with Environment Variables**
        - In this step, you will learn how to run a containerized application and configure it at startup using environment variables. This is a fundamental skill in container management, allowing for flexible and secure deployments. We will use the official MariaDB image as an example, as it requires several configuration parameters to initialize a database.
        - First, ensure you are in the correct working directory. All work for this lab will be done inside the `~/project` directory.
        - `cd ~/project` Explain Code
        - Before running a container, it's good practice to explicitly pull the image from the registry. This ensures you have the correct version locally. We will use the `mariadb:10.6` image for this lab to ensure consistency.
        - `podman pull mariadb:10.6` Explain Code
        - Select the `mariadb:10.6` image from the docker registry.
        - You should see output indicating the image is being downloaded and extracted.
        - ```
10.6: Pulling from library/mariadb
...
Status: Downloaded newer image for mariadb:10.6
docker.io/library/mariadb:10.6
``` Explain Code
        - Now, you can run the MariaDB container. The `podman run` command creates and starts a new container. We will use several flags:
            - `-d`: Runs the container in detached mode (in the background).
            - `--name mariadb_server`: Assigns a memorable name to our container.
            - `-e VARIABLE=value`: Sets an environment variable inside the container. The MariaDB image uses these to configure the database upon first launch.
        - Run the following command to start your MariaDB container. We are setting the root password, and also creating a new database named `webappdb` with a dedicated user `webappuser`.
        - ```
podman run -d \
  --name mariadb_server \
  -e MARIADB_ROOT_PASSWORD=supersecret \
  -e MARIADB_DATABASE=webappdb \
  -e MARIADB_USER=webappuser \
  -e MARIADB_PASSWORD=userpass \
  mariadb:10.6
``` Explain Code
        - The command will output a long container ID, which confirms that the container has been created.
        - `a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2` Explain Code
        - To verify that the container is running, use the `podman ps` command.
        - `podman ps` Explain Code
        - You should see `mariadb_server` in the list of running containers.
        - ```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS      NAMES
a1b2c3d4e5f6   mariadb:10.6   "docker-entrypoint.s…"   15 seconds ago   Up 14 seconds   3306/tcp   mariadb_server
``` Explain Code
        - Finally, let's check the container's logs to ensure the database initialized correctly using the environment variables we provided.
        - `podman logs mariadb_server` Explain Code
        - Scroll through the logs. You are looking for a line that indicates the server is ready for connections, which confirms a successful startup. The output will be lengthy, but a key success message near the end looks like this:
        - ```
...
2024-05-20 10:30:00+00:00 [Note] [Entrypoint]: /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/
...
2024-05-20 10:30:15+00:00 [Note] mariadbd: ready for connections.
Version: '10.6.x-MariaDB-1:10.6.x+maria~ubu2004'  socket: '/run/mysqld/mysqld.sock'  port: 3306  mariadb.org binary distribution
``` Explain Code
        - You have successfully launched and configured a MariaDB container using environment variables.
        - 
        - # **Configure Persistent Storage for the MariaDB Container**
        - In this step, you will learn how to configure persistent storage for a container. By default, any data created inside a container is stored in a writable layer that is tied to the container's lifecycle. If you remove the container, all of that data is lost. For stateful applications like databases, this is not ideal. To solve this, we use Podman volumes or bind mounts to store the data on the host filesystem, independent of the container.
        - First, we need to remove the container we created in the previous step, as we will relaunch it with a new storage configuration.
        - Stop the running `mariadb_server` container:
        - `podman stop mariadb_server` Explain Code
        - You will see the name of the container as output, confirming the command was received.
        - `mariadb_server` Explain Code
        - Now, remove the stopped container:
        - `podman rm mariadb_server` Explain Code
        - Again, the container's name will be echoed back.
        - `mariadb_server` Explain Code
        - Next, create a directory on your host machine within the `~/project` directory. This directory will hold the MariaDB database files.
        - `mkdir ~/project/mariadb_data` Explain Code
        - When using Podman in rootless mode, we need to set the correct permissions for the mounted directory. The MariaDB container runs as a specific user (UID 999), so we need to ensure the directory is accessible. We'll use the `--userns=keep-id` flag and set appropriate permissions:
        - `chmod 755 ~/project/mariadb_data` Explain Code
        - Now, run the MariaDB container again. This command is similar to the one from the previous step, but with the addition of the `-v` flag and `--userns=keep-id` to handle user namespace mapping properly. The `-v` flag mounts the `~/project/mariadb_data` directory from your host into the `/var/lib/mysql` directory inside the container, which is where MariaDB stores its data. We use `$(pwd)/mariadb_data` to provide the required absolute path to the `podman` command.
        - ```
podman run -d \
  --name mariadb_server \
  --userns=keep-id \
  -e MARIADB_ROOT_PASSWORD=supersecret \
  -e MARIADB_DATABASE=webappdb \
  -e MARIADB_USER=webappuser \
  -e MARIADB_PASSWORD=userpass \
  -v $(pwd)/mariadb_data:/var/lib/mysql:Z \
  mariadb:10.6
``` Explain Code
        - The `:Z` suffix on the volume mount tells Podman to relabel the content with a private unshared label, which is important for SELinux compatibility.
        - After the container starts, you can verify that the data is being stored on your host machine. List the contents of the `~/project/mariadb_data` directory.
        - `ls -l ~/project/mariadb_data` Explain Code
        - Because the container's database engine has initialized, you will see several files and directories created inside `~/project/mariadb_data`. This confirms that your data is now persistent. Even if you remove the container, this data will remain.
        - ```
total 110632
-rw-rw---- 1 labex labex    16384 May 20 10:45 aria_log.00000001
-rw-rw---- 1 labex labex       52 May 20 10:45 aria_log_control
-rw-rw---- 1 labex labex      983 May 20 10:45 ib_buffer_pool
-rw-rw---- 1 labex labex 12582912 May 20 10:45 ibdata1
-rw-rw---- 1 labex labex 50331648 May 20 10:45 ib_logfile0
-rw-rw---- 1 labex labex 50331648 May 20 10:45 ib_logfile1
drwx------ 2 labex labex     4096 May 20 10:45 mysql
drwx------ 2 labex labex     4096 May 20 10:45 performance_schema
drwx------ 2 labex labex     4096 May 20 10:45 sys
drwx------ 2 labex labex     4096 May 20 10:45 webappdb
``` Explain Code
        - You have successfully configured your MariaDB container to use persistent storage, ensuring your database data will survive container restarts and removals.
        - 
        - # **Create a Custom Network and Deploy an Apache Web Server**
        - In this step, you will create a custom network for your containers and deploy an Apache web server. While Podman provides a default network, using custom networks is a best practice. They provide better isolation and, most importantly, enable automatic DNS resolution between containers. This allows containers to communicate with each other using their names, which is more reliable than using IP addresses that can change.
        - First, let's create a custom bridge network for our application. We'll name it `webapp-network`.
        - `podman network create webapp-network` Explain Code
        - The command will output the name of the newly created network.
        - `webapp-network` Explain Code
        - You can list all Podman networks to confirm that yours was created successfully.
        - `podman network ls` Explain Code
        - You should see `webapp-network` in the list, along with the default networks.
        - ```
NETWORK ID     NAME               DRIVER    SCOPE
...
f1e2d3c4b5a6   webapp-network     bridge    local
...
``` Explain Code
        - Next, we need to recreate our `mariadb_server` container on this new network. Due to the network backend configuration in this environment, we cannot connect an existing container to a new network. Instead, we'll stop and recreate the container with the new network configuration.
        - Stop the running `mariadb_server` container:
        - `podman stop mariadb_server` Explain Code
        - Remove the stopped container:
        - `podman rm mariadb_server` Explain Code
        - Now, recreate the MariaDB container with the new network. This command is similar to the one from the previous step, but with the addition of the `--network webapp-network` flag:
        - ```
podman run -d \
  --name mariadb_server \
  --network webapp-network \
  --userns=keep-id \
  -e MARIADB_ROOT_PASSWORD=supersecret \
  -e MARIADB_DATABASE=webappdb \
  -e MARIADB_USER=webappuser \
  -e MARIADB_PASSWORD=userpass \
  -v $(pwd)/mariadb_data:/var/lib/mysql:Z \
  mariadb:10.6
``` Explain Code
        - Now, let's deploy our web server. We will use the official Apache `httpd` image. First, create a directory on the host to store your website's files.
        - `mkdir ~/project/webapp_content` Explain Code
        - Create a simple `index.html` file in this new directory. This will be the homepage of our web application.
        - `echo "<h1>Welcome to My Web App</h1>" > ~/project/webapp_content/index.html` Explain Code
        - Set the correct permissions for the webapp content directory to ensure the Apache container can access the files:
        - `chmod 755 ~/project/webapp_content` Explain Code
        - Now, run the Apache `httpd` container. We will attach it to our `webapp-network` and mount the `webapp_content` directory as a volume. This ensures the web server can serve the `index.html` file we just created.
        - ```
podman run -d \
  --name web_server \
  --network webapp-network \
  -v $(pwd)/webapp_content:/usr/local/apache2/htdocs/:Z \
  httpd:2.4
``` Explain Code
        - Let's break down the options:
            - `--network webapp-network`: Connects the new container to our custom network.
            - `-v $(pwd)/webapp_content:/usr/local/apache2/htdocs/:Z`: This mounts our local `webapp_content` directory into the container at `/usr/local/apache2/htdocs/`, which is the default directory Apache serves files from. The `:Z` suffix tells Podman to relabel the content with a private unshared label for SELinux compatibility.
        - Verify that both containers are running.
        - `podman ps` Explain Code
        - You should now see both `mariadb_server` and `web_server` in the list of running containers.
        - ```
CONTAINER ID  IMAGE                           COMMAND           CREATED         STATUS         PORTS       NAMES
6a3f46c0ab3a  docker.io/library/mariadb:10.6  mariadbd          29 seconds ago  Up 29 seconds  3306/tcp    mariadb_server
da5d52ce9c41  docker.io/library/httpd:2.4     httpd-foreground  7 seconds ago   Up 7 seconds   80/tcp      web_server
``` Explain Code
        - Both containers are now on the same custom network and can communicate with each other by name.
        - 
        - # **Expose the Web Server Port and Test Connectivity**
        - In this step, you will learn how to expose a container's port to the host machine, making the service accessible from outside the container's isolated network. Our Apache web server is running, but we cannot yet access it from our host's browser or command line. We will fix this by publishing the container's port.
        - Port mappings are defined when a container is created. Therefore, we must first stop and remove the `web_server` container we created in the previous step. Don't worry about the website content; it's safe in the `~/project/webapp_content` directory on our host because we used a bind mount.
        - First, stop the container:
        - `podman stop web_server` Explain Code
        - `web_server` Explain Code
        - Next, remove the stopped container:
        - `podman rm web_server` Explain Code
        - `web_server` Explain Code
        - Now, we will run the `web_server` container again, but this time we will add the `-p` (or `--publish`) flag to map a port from the host to a port in the container. We will map port `8080` on the host to port `80` (the default HTTP port) inside the container.
        - ```
podman run -d \
  --name web_server \
  --network webapp-network \
  -v $(pwd)/webapp_content:/usr/local/apache2/htdocs/:Z \
  -p 8080:80 \
  httpd:2.4
``` Explain Code
        - The new flag `-p 8080:80` tells Podman to forward all traffic from port `8080` on the host to port `80` inside the `web_server` container.
        - Let's verify the container is running and the port is correctly mapped using `podman ps`.
        - `podman ps` Explain Code
        - Notice the `PORTS` column for the `web_server` container. It now shows the mapping from `0.0.0.0:8080` to `80/tcp`, indicating that the port is successfully exposed.
        - ```
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                  NAMES
c5d4e3f2a1b6   httpd:2.4      "httpd-foreground"       10 seconds ago   Up 9 seconds    0.0.0.0:8080->80/tcp   web_server
a1b2c3d4e5f6   mariadb:10.6   "docker-entrypoint.s…"   25 minutes ago   Up 25 minutes   3306/tcp               mariadb_server
``` Explain Code
        - Finally, let's test the connectivity from our host machine using the `curl` command. This sends an HTTP request to `localhost` on port `8080`.
        - `curl http://localhost:8080` Explain Code
        - You should see the HTML content from your `index.html` file as the output, confirming that your web server is now accessible from the host.
        - `<h1>Welcome to My Web App</h1>` Explain Code
        - You have successfully exposed your containerized web server to the host machine, a critical step for making applications available to users.
        - 
        - # **Manage the Web Server Container as a systemd Service**
        - In this final step, you will learn how to configure a container to start automatically, ensuring your service is resilient to crashes or system reboots. On a standard Red Hat Enterprise Linux system, `systemd` is the primary tool for managing services. However, the Podman environment in this lab does not use `systemd` to manage containers directly.
        - Instead, we will achieve the same outcome—automatic service restarts—using Podman's built-in **restart policies**. This is the standard, container-native way to ensure a container is automatically started by the Podman daemon. We will configure our `web_server` to always restart if it stops for any reason.
        - First, we must remove the existing container, as restart policies can only be applied when a container is created.
        - Stop the `web_server` container:
        - `podman stop web_server` Explain Code
        - `web_server` Explain Code
        - And now remove it:
        - `podman rm web_server` Explain Code
        - `web_server` Explain Code
        - Next, re-create the `web_server` container with the same configuration as before, but add the `--restart always` flag. This flag instructs the Podman daemon to monitor the container and restart it if it ever exits.
        - ```
podman run -d \
  --name web_server \
  --network webapp-network \
  -v $(pwd)/webapp_content:/usr/local/apache2/htdocs/:Z \
  -p 8080:80 \
  --restart always \
  httpd:2.4
``` Explain Code
        - The container will start as usual. To confirm the restart policy is active, you can inspect the container's configuration.
        - `podman inspect web_server --format '{{.HostConfig.RestartPolicy.Name}}'` Explain Code
        - The command should return `always`, confirming the policy is set.
        - `always` Explain Code
        - Now, let's demonstrate how the restart policy works by manually restarting the container to simulate what would happen after a system reboot or container failure.
        - First, let's check the current restart policy configuration:
        - `podman inspect web_server --format '{{.HostConfig.RestartPolicy.Name}}'` Explain Code
        - This should show `always`, confirming our restart policy is configured.
        - `always` Explain Code
        - Now let's test manual restart to simulate recovery after a failure:
        - `podman start web_server` Explain Code
        - `web_server` Explain Code
        - Check that the container is running:
        - `podman ps` Explain Code
        - You should see both containers running with the restart policy in place:
        - ```
CONTAINER ID   IMAGE          COMMAND                  CREATED              STATUS              PORTS                  NAMES
e7f6g5h4i3j2   httpd:2.4      "httpd-foreground"       About a minute ago   Up 5 seconds        0.0.0.0:8080->80/tcp   web_server
a1b2c3d4e5f6   mariadb:10.6   "docker-entrypoint.s…"   About an hour ago    Up About an hour    3306/tcp               mariadb_server
``` Explain Code
        - Finally, confirm that the service is accessible:
        - `curl http://localhost:8080` Explain Code
        - `<h1>Welcome to My Web App</h1>` Explain Code
        - **Understanding Restart Policies:**
        - The `--restart always` policy you've configured ensures that:
            - The container will restart automatically if it exits unexpectedly
            - The container will start automatically when the Podman service starts (such as after a system reboot)
            - This provides resilience for production deployments
        - Note: In some lab environments, automatic restart behavior may vary depending on the Podman configuration and whether the Podman system service is running. The key learning objective is understanding how to configure restart policies for production deployments.
        - You have successfully configured your container to be managed like a service, ensuring it remains available automatically. This completes the basic lifecycle management of a containerized application.
        - 
        - # **Summary**
        - In this lab, you learned the fundamental process of deploying a multi-container web application on RHEL using Podman. You began by running a MariaDB database container, configuring its initial state—including the root password, a new database, and a dedicated user—by passing environment variables at runtime. You then configured persistent storage for the database container, ensuring that critical data is preserved across container restarts.
        - To complete the application stack, you created a custom network to enable secure, isolated communication between the containers. You deployed an Apache web server container onto this network and exposed its port to allow external user access. Finally, you integrated the web server container with systemd, managing it as a system service to ensure it starts automatically on boot and runs reliably, demonstrating a production-ready deployment pattern.
-  **Red Hat Enterprise Linux Automation with Ansible (RH294) Certification Labs - **9 labs
    1. **Install Ansible on Red Hat Enterprise Linux**
        - Install Ansible Core Using dnf
        - Verify the Ansible Installation
        - Test Ansible with a Simple Command
        - Explore Available Ansible Modules
        - 
        - # **Introduction**
        - In this lab, you will learn how to install Ansible Core on a Red Hat Enterprise Linux (RHEL) system. Ansible is a powerful automation tool that allows you to manage and configure systems, deploy applications, and orchestrate complex IT workflows.
        - You will use the `dnf` package manager with `sudo` privileges to install the `ansible-core` package, which provides the core Ansible engine and command-line tools. After installation, you will verify that Ansible is working correctly by checking its version and running basic commands.
        - This is a fundamental skill for system administrators and DevOps engineers working with Red Hat Enterprise Linux systems.
        - This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a beginner level lab with a 100% completion rate. It has received a 100% positive review rate from learners.
        - ![](https://remnote-user-data.s3.amazonaws.com/xkGlze4ha4FYre6MmoQ2aWVduF0FcXp0iG-W65Qvt1Xb0KVRy--1q3sPWdVVP593R0oeTHgDGimnBHVH9zb3Zq_p6cLeGL91vaXiTwhx1HrCG5YLij65OmZHp7b8gScm.webp)**Labby** 
        - 
        - # **Install Ansible Core Using dnf**
        - In this step, you will install the `ansible-core` package using the `dnf` package manager. Ansible Core provides the essential Ansible engine, including the `ansible`, `ansible-playbook`, and other core command-line tools needed for automation tasks.
        - The `dnf` (Dandified YUM) package manager is the standard tool for managing software packages on Red Hat Enterprise Linux. Since installing software requires administrative privileges, you must use the `sudo` command.
        - Run the following command to install Ansible Core with automatic confirmation:
        - `sudo dnf install ansible-core -y` Explain Code
        - The `-y` flag automatically answers "yes" to all prompts, making the installation non-interactive. The system will download and install `ansible-core` along with its Python dependencies including Jinja2 for templating and PyYAML for YAML processing.
        - You should see output similar to this, showing the package resolution and installation progress:
        - ```
Updating Subscription Management repositories.
Last metadata expiration check: ...
Dependencies resolved.
================================================================================
 Package                  Arch   Version                Repository         Size
================================================================================
Installing:
 ansible-core             noarch 2.16.x-x.el9            rhel-9-appstream   xx M
Installing dependencies:
 python3-jinja2           noarch x.x.x-x.el9              rhel-9-appstream   xxx k
 python3-yaml             x86_64 x.x.x-x.el9              rhel-9-appstream   xxx k
 ...

Transaction Summary
================================================================================
Install  XX Packages

Complete!
``` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/BBj2ZL-cdoGHcm_Gs6C7o0PbeDFjNa-ycg3mVoq9nqZzX0YM1SAieMbGMGiEKZ_sSr3Zw17JZjieGRmNTeP2O13v9mjdPGwTBm1wVjYv8Ayk1rFx22EJS_sNSCwvEQSt.webp)**Labby**
        - 
        - # **Verify the Ansible Installation**
        - Now that you have installed Ansible Core, let's verify that the installation was successful by checking the version and confirming that the essential command-line tools are available.
        - First, check the Ansible version by running:
        - `ansible --version` Explain Code
        - This command displays detailed information about your Ansible installation, including the core version, Python version, and the locations of various components. You should see output like this:
        - ```
ansible [core 2.14.18]
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/labex/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.9/site-packages/ansible
  ansible collection location = /home/labex/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible
  python version = 3.9.21 (main, Feb 10 2025, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] (/usr/bin/python3)
  jinja version = 3.1.2
  libyaml = True
``` Explain Code
        - Let's understand what each line means:
            - **ansible [core 2.14.18]**: Shows the installed Ansible Core version
            - **config file**: Points to the main Ansible configuration file that contains default settings
            - **configured module search path**: Directories where Ansible looks for custom modules
            - **ansible python module location**: Where the core Ansible Python code is installed
            - **ansible collection location**: Directories where Ansible collections (packaged modules and plugins) are stored
            - **executable location**: The actual location of the ansible command binary
            - **python version**: The Python interpreter version that Ansible uses
            - **jinja version**: The templating engine version used by Ansible for dynamic content
            - **libyaml = True**: Confirms that the fast YAML parser is available for better performance
        - This confirms that Ansible is properly installed and ready to use. Next, let's also check that the `ansible-playbook` command is available:
        - `ansible-playbook --version` Explain Code
        - You should see similar version information for the ansible-playbook tool, which is essential for running Ansible playbooks.
        - ![](https://remnote-user-data.s3.amazonaws.com/Tul7v923VZHQWndxRq7L66RMgLx9Oi9pWUeNZWEI8Es2tsLEb3vbAHgZExafbwYaSYrTOKlmFqlKlG5GVzcIzgm2g4eg1zTBM-5t7uk8VctTLBHu3ZyLDCcaJhjemsRD.webp)**Labby**
        - 
        - # **Test Ansible with a Simple Command**
        - In this step, you will test your Ansible installation by running a simple command against the local system. Change to the project directory and use the pre-configured inventory file to run an Ansible ad-hoc command.
        - Navigate to the project directory and test the basic ping functionality:
        - ```
cd /home/labex/project
ansible localhost -m ping
``` Explain Code
        - The `ping` module doesn't actually send ICMP packets; instead, it verifies that Ansible can connect to the target and execute Python code. A successful response will look like this:
        - ```
localhost | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
``` Explain Code
        - Let's break down this output:
            - **localhost | SUCCESS**: Shows that the command executed successfully on the localhost target
            - **ansible_facts**: Contains system information discovered during execution
            - **discovered_interpreter_python**: The Python interpreter path that Ansible found and will use
            - **changed: false**: Indicates that no changes were made to the system (ping is read-only)
            - **ping: "pong"**: The classic response confirming Ansible connectivity
        - The "pong" response confirms that Ansible is working correctly and can communicate with the target system.
        - Let's also test gathering system information using the setup module:
        - `ansible localhost -m setup -a "filter=ansible_distribution*"` Explain Code
        - This command uses the `setup` module to gather system facts, specifically filtering for distribution information. You should see output containing details about your Red Hat Enterprise Linux system:
        - ```
localhost | SUCCESS => {
    "ansible_facts": {
        "ansible_distribution": "RedHat",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/redhat-release",
        "ansible_distribution_file_search_string": "Red Hat",
        "ansible_distribution_file_variety": "RedHat",
        "ansible_distribution_major_version": "9",
        "ansible_distribution_release": "Plow",
        "ansible_distribution_version": "9.6",
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false
}
``` Explain Code
        - Understanding the system facts output:
            - **ansible_distribution**: The Linux distribution name (RedHat)
            - **ansible_distribution_file_parsed**: Whether Ansible successfully read the distribution file
            - **ansible_distribution_file_path**: The file that contains distribution information
            - **ansible_distribution_file_search_string**: The text pattern used to identify the distribution
            - **ansible_distribution_file_variety**: The distribution family (RedHat family)
            - **ansible_distribution_major_version**: The major version number (9)
            - **ansible_distribution_release**: The release codename (Plow)
            - **ansible_distribution_version**: The complete version number (9.6)
            - **discovered_interpreter_python**: Python interpreter discovered by Ansible
        - This confirms that Ansible can successfully collect system information from the target host, which is essential for creating conditional automation based on system characteristics.
        - ![](https://remnote-user-data.s3.amazonaws.com/fG2A_2ajO_BjJimqoKcm5ckd3xaEa3XT7VWI2bEyJb0yrPkmyBo1zRmyBCz8xOVm30hqeBq6iQ0ZZbBeSZvsyuWHInKIE_53Gu0Lw6jg362lfjriS6rFvv4Qvt7FVXes.webp)**Labby**
        - 
        - # **Explore Available Ansible Modules**
        - Ansible comes with hundreds of built-in modules for various automation tasks. Let's explore some of the available modules to understand what capabilities are immediately available after installation.
        - To see a list of available modules, run:
        - `ansible-doc -l | head -20` Explain Code
        - The `ansible-doc -l` command lists all available modules, and using `head -20` shows the first 20 modules. This gives you an idea of the extensive automation capabilities available with Ansible. You'll see output similar to:
        - ```
ansible.builtin.add_host               Add a host (and alternatively a grou...
ansible.builtin.apt                    Manages apt-packages
ansible.builtin.apt_key                Add or remove an apt key
ansible.builtin.apt_repository         Add and remove APT repositories
ansible.builtin.assemble               Assemble configuration files from fr...
ansible.builtin.assert                 Asserts given expressions are true
ansible.builtin.async_status           Obtain status of asynchronous task
ansible.builtin.blockinfile            Insert/update/remove a text block su...
ansible.builtin.command                Execute commands on targets
ansible.builtin.copy                   Copy files to remote locations
ansible.builtin.cron                   Manage cron.d and crontab entries
ansible.builtin.debconf                Configure a .deb package
ansible.builtin.debug                  Print statements during execution
ansible.builtin.dnf                    Manages packages with the `dnf' pack...
ansible.builtin.dpkg_selections        Dpkg package selection selections
ansible.builtin.expect                 Executes a command and responds to p...
ansible.builtin.fail                   Fail with custom message
ansible.builtin.fetch                  Fetch files from remote nodes
ansible.builtin.file                   Manage files and file properties
ansible.builtin.find                   Return a list of files based on spec...
``` Explain Code
        - Understanding the module list format:
            - **ansible.builtin.**: Indicates these are built-in modules that come with Ansible Core
            - **Module name**: The name you use when calling the module in playbooks or ad-hoc commands
            - **Description**: A brief explanation of what the module does
        - Some important modules you'll commonly use:
            - **command**: Execute shell commands on target systems
            - **copy**: Copy files from your control machine to remote hosts
            - **dnf**: Install, update, or remove packages on Red Hat systems
            - **file**: Create directories, set permissions, or manage file properties
            - **debug**: Print messages during playbook execution for troubleshooting
        - To get detailed documentation for a specific module, you can use the ansible-doc command with the module name. For example, to learn about the copy module:
        - `ansible-doc copy` Explain Code
        - This will display comprehensive documentation for the `copy` module, including examples and parameter descriptions. The `ansible-doc` command provides detailed documentation for any Ansible module, making it easy to learn how to use different automation capabilities. Press `q` to exit the documentation viewer when you're done reading.
        - ![](https://remnote-user-data.s3.amazonaws.com/AEmpc-oPv1N30yBk3O4UlAWqSFUjqW_9DlDHOh-6glPijPTJhbwHzddqHUdXj8wUgnNSuXG7Xyi9C6sfX0T1oXLgTg97_t2NbRZrxnzfsnfh6vajnbcpg1q4MP683zBs.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you successfully learned how to install and verify Ansible Core on a Red Hat Enterprise Linux system. Here's what you accomplished:
            1. **Installed Ansible Core**: You used the `sudo dnf install ansible-core -y` command to install the core Ansible package and its dependencies from the official Red Hat repositories.
            2. **Verified the Installation**: You confirmed that Ansible was properly installed by checking the version of both `ansible` and `ansible-playbook` commands.
            3. **Tested Basic Functionality**: You ran simple Ansible commands to verify that the installation works correctly, including:
                - Using the `ping` module to test connectivity
                - Using the `setup` module to gather system facts
            4. **Explored Available Modules**: You learned how to discover and read documentation for the extensive library of Ansible modules using `ansible-doc`.
        - You now have a fully functional Ansible installation on RHEL and understand the basic commands needed to start automating your infrastructure. This foundation prepares you for more advanced Ansible topics such as writing playbooks, managing inventories, and implementing complex automation workflows.
    2. **Implement an Ansible Playbook on RHEL**
        - Create a Static Inventory File for Web Servers
        - Configure the Ansible Environment with ansible.cfg
        - Write a Playbook to Install and Start the Apache Service
        - Add Tasks to Deploy a Web Page
        - Implement a Second Play to Test the Web Server Deployment
        - 
        - # **Introduction**
        - In this lab, you will learn how to implement a complete Ansible playbook to deploy an Apache web server on a Red Hat Enterprise Linux (RHEL) system. You will begin by setting up the foundational components of an Ansible project, which includes creating a static inventory file to define your managed nodes and configuring the local Ansible environment using an `ansible.cfg` file.
        - Following the initial setup, you will write a multi-task playbook to automate the core deployment process. This involves installing and starting the Apache service, deploying a custom web page, and configuring the system firewall to allow HTTP traffic. To complete the lab, you will add a second play to your playbook that tests the web server from the command line, verifying that the entire deployment was successful.
        - ![](https://remnote-user-data.s3.amazonaws.com/CH3eV7nuvLN3ttyNPC248Y1IssQOiNkd-6wC0CqC5BaWHFLfmQssplO23mZM8eshZhmpCL7b5t2hzc90WDOLKJam88D5fvotDDlB7-dWJuHftfQpBTI8TABpD8f2c594.webp)**Labby** 
        - 
        - # **Create a Static Inventory File for Web Servers**
        - In this step, you will learn the fundamentals of an Ansible inventory. An inventory is a text file that lists the servers (or "managed nodes") that Ansible will manage. You will create a simple, static inventory file for a group of web servers and learn how to verify its contents.
        - First, you need to ensure that Ansible is installed on your system. Since it's not installed by default, you will use the `dnf` package manager to install it.
            1. Open your terminal and install the `ansible-core` package, which provides the fundamental Ansible command-line tools.
                - `sudo dnf install -y ansible-core` Explain Code
                - You should see output indicating that the package is being installed and verified.
                - ```
...
Installed:
  ansible-core-2.16.x-x.el9.x86_64
...
Complete!
``` Explain Code
            2. For better organization, create a dedicated directory for this project within your home directory. Let's name it `ansible-lab`.
                - `mkdir -p ~/project/ansible-lab` Explain Code
            3. Navigate into your newly created project directory. All subsequent work in this lab will be done from this location.
                - `cd ~/project/ansible-lab` Explain Code
            4. Now, you will create your first inventory file. An inventory file is typically written in an INI-like format. You will use the `nano` text editor to create a file named `inventory`.
                - `nano inventory` Explain Code
            5. Inside the `nano` editor, add the following content. This configuration defines a group called `[webservers]` and adds your local machine, `localhost`, to this group.
                - `[webservers]` is a group name. Groups are used to target multiple hosts with a single command.
                - `localhost` is the hostname of the machine you want to manage. In this case, it's the LabEx VM itself.
                - `ansible_connection=local` is a special variable that tells Ansible to execute commands directly on the control node (your VM) instead of trying to connect to it via SSH.
                - ```
[webservers]
localhost ansible_connection=local
``` Explain Code
                - To save the file in `nano`, press `Ctrl+O`, then `Enter` to confirm the filename, and `Ctrl+X` to exit the editor.
            6. With your inventory file created, you can use the `ansible-inventory` command to parse the file and display a list of the hosts it contains. The `-i` flag specifies the path to your inventory file.
                - `ansible-inventory --list -i inventory` Explain Code
                - The command will output a JSON-formatted representation of your inventory, which confirms that Ansible can read and understand your file correctly.
                - ```
{
  "_meta": {
    "hostvars": {
      "localhost": {
        "ansible_connection": "local"
      }
    }
  },
  "all": {
    "children": ["ungrouped", "webservers"]
  },
  "webservers": {
    "hosts": ["localhost"]
  }
}
``` Explain Code
        - You have successfully created a basic static inventory file and verified that Ansible can correctly interpret it. This inventory file will be the foundation for the playbooks you write in the following steps.
        - ![](https://remnote-user-data.s3.amazonaws.com/yLMFxYPH8jY2nFD1O2IjX0yhUGYAsA9yNCz8kPNNuyNd8Ldjr_WEnRsNepnTu8cT7JRUfenAE1dO7wM5ZlJTk42q4ZZaBSYYP2nXmbnDlSFKBVgMrsjndRvtJ1TKu037.webp)**Labby**
        - 
        - # **Configure the Ansible Environment with ansible.cfg**
        - In this step, you will create an Ansible configuration file, `ansible.cfg`. This file allows you to set default behaviors for Ansible, saving you from typing common options on the command line repeatedly. By placing an `ansible.cfg` file in your project directory, you can define settings like the default inventory file path, which Ansible will automatically use when run from that directory.
        - You should still be in the `~/project/ansible-lab` directory from the previous step.
            1. Use the `nano` text editor to create a new file named `ansible.cfg` in your current directory (`~/project/ansible-lab`).
                - `nano ansible.cfg` Explain Code
            2. Inside the `nano` editor, add the following content. This configuration tells Ansible where to find your default inventory file.
                - The `[defaults]` section is a standard part of the `ansible.cfg` file where you define most of the default settings.
                - The `inventory = ./inventory` line sets the default inventory to the `inventory` file located in the current directory (`.`).
                - ```
[defaults]
inventory = ./inventory
``` Explain Code
                - Save the file by pressing `Ctrl+O`, then `Enter`, and exit with `Ctrl+X`.
            3. Now that you have configured the default inventory path, you no longer need to use the `-i` flag with your Ansible commands (as long as you are in the `~/project/ansible-lab` directory).
                - To test this, run the `ansible-inventory --list` command again, but this time, omit the `-i inventory` part.
                - `ansible-inventory --list` Explain Code
                - You should see the exact same JSON output as in the previous step, which confirms that Ansible is automatically finding and using your `inventory` file thanks to the new `ansible.cfg` configuration.
                - ```
{
  "_meta": {
    "hostvars": {
      "localhost": {
        "ansible_connection": "local"
      }
    }
  },
  "all": {
    "children": ["ungrouped", "webservers"]
  },
  "webservers": {
    "hosts": ["localhost"]
  }
}
``` Explain Code
        - By creating a project-specific `ansible.cfg`, you have made your workflow more efficient. This is a common practice in Ansible projects to ensure consistent behavior and reduce command-line complexity.
        - ![](https://remnote-user-data.s3.amazonaws.com/VspGNL7kz_JW-DBy-V__Z1d3kZouDD07sN5bzgREOg4zrjBWekV7aK7eme3Kl0l_7qWHA7oF6rFMSAoBjRjVGmwYcykr4zjGvqKF10JU84uRWja83FBc_4gVoV5VYkQc.webp)**Labby**
        - 
        - # **Write a Playbook to Install and Start the Apache Service**
        - In this step, you will write your first Ansible Playbook. A playbook is a file written in YAML format that describes a set of tasks to be executed on your managed hosts. You will create a playbook that installs the Apache web server (`httpd`) and starts its service on the `localhost` machine defined in your inventory.
        - You should still be in the `~/project/ansible-lab` directory.
            1. First, use the `nano` text editor to create a new file named `apache.yml`. This file will contain your playbook.
                - `nano apache.yml` Explain Code
            2. Inside the `nano` editor, you will define a "play." A play is the core unit of a playbook and maps a group of hosts to a set of tasks. Add the following content to `apache.yml`.
                - `---`: This is a standard YAML marker indicating the start of a document.
                - `- name: ...`: This is the beginning of your play. Giving it a descriptive name is a best practice.
                - `hosts: webservers`: This tells Ansible to run this play on all hosts in the `webservers` group from your inventory file.
                - `become: true`: This instructs Ansible to use privilege escalation (like `sudo`) to execute the tasks. This is necessary for actions like installing software or managing services.
                - `tasks:`: This keyword begins the list of tasks to be performed.
                - ```
---
- name: Install and start Apache web server
  hosts: webservers
  become: true
  tasks:
``` Explain Code
            3. Now, add the tasks to your playbook. Each task is a single action that calls an Ansible module. **Indentation is critical in YAML**, so ensure the tasks are indented correctly under the `tasks:` section.
                - **Task 1: Install httpd.** This task uses the `ansible.builtin.dnf` module to ensure the `httpd` package is installed. The `state: present` parameter means Ansible will install the package if it's missing, and do nothing if it's already installed.
                - **Task 2: Start httpd service.** This task uses the `ansible.builtin.service` module. `state: started` ensures the service is running, and `enabled: true` ensures it will start automatically on system boot.
                - Add the following tasks to your `apache.yml` file, directly below the `tasks:` line:
                - ```
- name: Install httpd package
  ansible.builtin.dnf:
    name: httpd
    state: present

- name: Start and enable httpd service
  ansible.builtin.service:
    name: httpd
    state: started
    enabled: true
``` Explain Code
            4. Your complete `apache.yml` playbook should now look like this. Double-check the indentation carefully.
                - ```
---
- name: Install and start Apache web server
  hosts: webservers
  become: true
  tasks:
    - name: Install httpd package
      ansible.builtin.dnf:
        name: httpd
        state: present

    - name: Start and enable httpd service
      ansible.builtin.service:
        name: httpd
        state: started
        enabled: true
``` Explain Code
                - Save the file and exit `nano` (`Ctrl+O`, `Enter`, `Ctrl+X`).
            5. Before running your playbook, it's a good practice to check it for syntax errors using the `ansible-playbook` command with the `--syntax-check` flag.
                - `ansible-playbook --syntax-check apache.yml` Explain Code
                - If the syntax is correct, the command will print the playbook's filename without any errors.
                - `playbook: apache.yml` Explain Code
            6. Now, execute the playbook.
                - `ansible-playbook apache.yml` Explain Code
                - Ansible will run through the tasks. Since this is the first run, you will see `changed` status for both tasks, indicating that the system state was modified.
                - ```
PLAY [Install and start Apache web server] *************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install httpd package] ***************************************************
changed: [localhost]

TASK [Start and enable httpd service] ******************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            7. Finally, verify that the Apache web server is running by using `curl` to request the default web page from `localhost`.
                - `curl http://localhost` Explain Code
                - You should see the default Apache Test Page, which confirms your playbook worked successfully.
                - ```
<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <h1>Test Page</h1>
    <p>This is the default test page for the Apache HTTP server.</p>
  </body>
</html>
``` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/8bHMJb386Dk9CdXeftB2fhjYdkQySaM1wmIVPw4SFEgNJRDBZ-0kkF55OZ0tgEYg7D8nlySE48SsfXkuQGyUzaAtTDN10VdYyTIc1-1EodGsy-QG86QkcQG9UbpBlir_.webp)**Labby**
        - 
        - # **Add Tasks to Deploy a Web Page**
        - In this step, you will expand your playbook to perform more realistic web server configuration. You will add a task to deploy a custom `index.html` page. This demonstrates how to manage files using Ansible's file management modules.
        - You should still be in the `~/project/ansible-lab` directory.
            1. First, create a simple HTML file that your playbook will deploy. Use `nano` to create a file named `index.html` in your current directory.
                - `nano index.html` Explain Code
            2. Add the following HTML content to the file. This will be the content of your custom web page.
                - ```
<h1>Welcome to the Ansible-managed Web Server!</h1>
<p>This page was deployed using an Ansible Playbook.</p>
``` Explain Code
                - Save and exit `nano` (`Ctrl+O`, `Enter`, `Ctrl+X`).
            3. Now, you will update your `apache.yml` playbook to add the new task. To avoid YAML formatting errors, it's recommended to recreate the file with the complete content.
                - **Important**: To ensure proper YAML formatting and avoid indentation errors, remove the existing `apache.yml` file and create a new one with the complete content shown below.
                - ```
rm apache.yml
nano apache.yml
``` Explain Code
            4. You will add a new task to the playbook. This task will copy the `index.html` file to the web server's document root (`/var/www/html/`).
                - **Task: Deploy index.html.** This task uses the `ansible.builtin.copy` module. `src` specifies the source file on the control node (`index.html`), and `dest` specifies the destination path on the managed host.
            5. Copy and paste the complete `apache.yml` playbook content below. This ensures proper YAML formatting and indentation.
                - ```
---
- name: Install and start Apache web server
  hosts: webservers
  become: true
  tasks:
    - name: Install httpd package
      ansible.builtin.dnf:
        name: httpd
        state: present

    - name: Deploy custom index.html
      ansible.builtin.copy:
        src: index.html
        dest: /var/www/html/index.html

    - name: Start and enable httpd service
      ansible.builtin.service:
        name: httpd
        state: started
        enabled: true
``` Explain Code
                - Save and exit `nano`.
            6. Save the file and exit `nano` (`Ctrl+O`, `Enter`, `Ctrl+X`), then run the updated playbook.
                - `ansible-playbook apache.yml` Explain Code
                - This time, you should see the new task being executed. The "Install httpd" and "Start httpd" tasks should report `ok` because their desired state has already been met. The "Deploy custom index.html" task will report `changed`.
                - ```
PLAY [Install and start Apache web server] *************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install httpd package] ***************************************************
ok: [localhost]

TASK [Deploy custom index.html] ************************************************
changed: [localhost]

TASK [Start and enable httpd service] ******************************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            7. Finally, use `curl` again to verify that your custom web page is now being served.
                - `curl http://localhost` Explain Code
                - The output should now be the content of your `index.html` file.
                - ```
<h1>Welcome to the Ansible-managed Web Server!</h1>
<p>This page was deployed using an Ansible Playbook.</p>
``` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/YkllgXDN84XssTaZ2717gmeH7im6PSvdfhLn5HRY81UtlhgZ_aVFK5RjA_f_ffyqGQRcKyufeX5OV_Em5rVokx6AD2_B0vpmd2ZYlzH369b6nySe2ZP6YXWOKk5t3df2.webp)**Labby**
        - 
        - # **Implement a Second Play to Test the Web Server Deployment**
        - In this final step, you will add a second play to your playbook. A single playbook file can contain multiple plays, which are executed sequentially. This is useful for organizing tasks that target different hosts or have different purposes. You will add a new play that runs only on the control node (`localhost`) to test the web server that was configured in the first play.
        - You should still be in the `~/project/ansible-lab` directory.
            1. You will now add a second play to your playbook. To ensure proper YAML formatting when adding the second play, it's recommended to recreate the file with the complete content.
                - **Important**: To avoid YAML indentation errors when adding the second play, remove the existing `apache.yml` file and create a new one with the complete two-play content shown below.
                - ```
rm apache.yml
nano apache.yml
``` Explain Code
            2. You will add a second play to the playbook. A second play allows you to organize tasks that target different hosts or have different purposes.
                - `name: Test web server`: A descriptive name for the new play.
                - `hosts: localhost`: This play will run on `localhost`, the control node itself.
                - `become: false`: This test does not require root privileges, so we explicitly disable privilege escalation.
                - **Task: Verify web content.** This task uses the `ansible.builtin.uri` module to make an HTTP request to the web server. It checks that the server returns a status code of 200 (OK) and that the returned content contains the string "Ansible-managed". This automates the `curl` and `grep` check you've been doing manually.
            3. Copy and paste the complete `apache.yml` playbook content below, which now includes both plays:
                - ```
---
- name: Install and start Apache web server
  hosts: webservers
  become: true
  tasks:
    - name: Install httpd package
      ansible.builtin.dnf:
        name: httpd
        state: present

    - name: Deploy custom index.html
      ansible.builtin.copy:
        src: index.html
        dest: /var/www/html/index.html

    - name: Start and enable httpd service
      ansible.builtin.service:
        name: httpd
        state: started
        enabled: true

- name: Test web server from localhost
  hosts: localhost
  become: false
  tasks:
    - name: Verify web server is serving correct content
      ansible.builtin.uri:
        url: http://localhost
        return_content: yes
        status_code: 200
      register: result
      failed_when: "'Ansible-managed' not in result.content"
``` Explain Code
                - Save the file and exit `nano` (`Ctrl+O`, `Enter`, `Ctrl+X`).
            4. Run the full playbook. Ansible will execute the first play, find that all tasks are already in their desired state (`ok`), and then proceed to the second play to run the test.
                - `ansible-playbook apache.yml` Explain Code
                - The output will show both plays being executed. All tasks should complete successfully with an `ok` status.
                - ```
PLAY [Install and start Apache web server] *************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install httpd package] ***************************************************
ok: [localhost]

TASK [Deploy custom index.html] ************************************************
ok: [localhost]

TASK [Start and enable httpd service] ******************************************
ok: [localhost]

PLAY [Test web server from localhost] ******************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Verify web server is serving correct content] ****************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - By adding a second play, you have created a more robust automation workflow that not only configures a service but also includes a built-in test to verify that the deployment was successful.
        - ![](https://remnote-user-data.s3.amazonaws.com/mnhqwMYP_cSuC_7Sfig74iOF2_r6SgfqhQ0gb3WXymHjEebW1CqHAwG7F0puSemupUJPzF-CI2B1f6LH4yFNIyO5Vy0FzheGk0AYLEsfcrUEioOqMxypHvC98G0Str6t.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned how to prepare a RHEL environment for Ansible automation by installing the `ansible-core` package and structuring a project directory. You created a fundamental static inventory file to define a group of managed nodes, specifying `localhost` with a local connection. You also configured the Ansible environment using an `ansible.cfg` file to point to your custom inventory, establishing a clean and organized workspace for running playbooks.
        - You then authored a comprehensive Ansible playbook to automate the deployment of an Apache web server. This involved writing tasks to install the `httpd` package using the `ansible.builtin.dnf` module and to ensure the service was started and enabled with the `ansible.builtin.service` module. The playbook was enhanced to deploy a custom `index.html` web page using the `ansible.builtin.copy` module. Finally, you implemented a second play within the same playbook to validate the deployment, using the `ansible.builtin.uri` module to test connectivity to the newly deployed web server, demonstrating a complete setup and verification workflow.
    3. **Manage Variables and Facts in RHEL with Ansible**
        - Define and Use Playbook Variables to Deploy an Apache Web Server
        - Display System Information using Ansible Facts
        - Configure the Web Server using Custom Facts from the Managed Host
        - Create a System User using Encrypted Variables with Ansible Vault
        - Run a Playbook with a Vault Password File to Apply Configurations
        - Verify the Web Server and User Configuration
        - 
        - # **Introduction**
        - In this lab, you will learn fundamental techniques for managing variables, facts, and secrets within Ansible playbooks on a Red Hat Enterprise Linux (RHEL) system. You will explore how to make your automation more flexible and powerful by using playbook variables, gathering system information with both built-in and custom Ansible facts, and securing sensitive data like passwords using Ansible Vault.
        - Through a series of hands-on steps, you will build a playbook to deploy and configure an Apache web server. You will start by defining simple variables for the package name and web content, then leverage custom facts to dynamically update the web server's configuration. Finally, you will use Ansible Vault to securely create a new system user with an encrypted password, run the complete playbook, and verify that all configurations have been successfully applied.
        - ![](https://remnote-user-data.s3.amazonaws.com/abCtxhVHX4TBlrFgp53HwVwIs7t9mrL9p1Bg78sGHNRf7ITyN-VErDZ2m0QdU_0kRzaksywPLoollToS9IxShEEoQApRWM-v--NdmHz4ELCvBFWk08acO6-uFtJuO0OH.webp)**Labby** 
        - 
        - # **Define and Use Playbook Variables to Deploy an Apache Web Server**
        - In this step, you will learn how to use variables in an Ansible playbook. Variables are essential for making your automation flexible, reusable, and easier to read and maintain. Instead of hardcoding values like package names or file paths directly into your tasks, you can define them as variables and reference them throughout the playbook. We will create a simple playbook that uses variables to install the Apache web server (`httpd`) and deploy a basic web page.
            1. **Navigate to the Project Directory**
                - First, ensure you are in the correct working directory. All your work for this lab will be done inside the `~/project` directory, which has been created for you.
                - `cd ~/project` Explain Code
                - Install the `ansible-core` package.
                - `sudo dnf install -y ansible-core` Explain Code
            2. **Create the Ansible Playbook**
                - Now, let's create our playbook file. We will name it `playbook.yml`. You can use a command-line text editor like `nano` to create and edit the file.
                - `nano playbook.yml` Explain Code
                - This command opens an empty file in the `nano` editor. Now, add the initial part of the playbook. This section defines the play's name, the target host (`localhost`, since we are running it on the same machine), and a `vars` section where we will define our variables.
                - ```
---
- name: Deploy Apache using variables
  hosts: localhost
  become: true
  vars:
    web_pkg: httpd
    web_content: "Hello from Ansible Variables"
``` Explain Code
                - Here's a breakdown of the playbook structure:
                    - `hosts: localhost`: Specifies that the playbook should run on the local machine.
                    - `become: true`: Tells Ansible to use privilege escalation (equivalent to `sudo`) for the tasks, which is necessary for installing software.
                    - `vars`: This is a dictionary where we define our key-value pairs for variables. We've defined `web_pkg` for the package name and `web_content` for the content of our test web page.
            3. **Add Tasks to the Playbook**
                - Next, below the `vars` section, add the `tasks` that will use these variables. The first task will install the Apache package, and the second will create an `index.html` file. Add the following `tasks` block to your `playbook.yml` file while still in the `nano` editor.
                - ```
tasks:
  - name: Install the latest version of Apache
    ansible.builtin.dnf:
      name: "{{ web_pkg }}"
      state: latest

  - name: Create a basic index.html file
    ansible.builtin.copy:
      content: "{{ web_content }}"
      dest: /var/www/html/index.html
``` Explain Code
                - Notice how we use `{{ variable_name }}` to reference the variables we defined earlier. This is Jinja2 templating, which Ansible uses for variables. This makes the task definitions generic; if you wanted to install Nginx instead, you would only need to change the `web_pkg` variable, not the task itself.
            4. **Review and Save the Playbook**
                - Your complete `playbook.yml` file should now look like this. Double-check the content and indentation, as YAML is very sensitive to spacing.
                - ```
---
- name: Deploy Apache using variables
  hosts: localhost
  become: true
  vars:
    web_pkg: httpd
    web_content: "Hello from Ansible Variables"
  tasks:
    - name: Install the latest version of Apache
      ansible.builtin.dnf:
        name: "{{ web_pkg }}"
        state: latest

    - name: Create a basic index.html file
      ansible.builtin.copy:
        content: "{{ web_content }}"
        dest: /var/www/html/index.html
``` Explain Code
                - To save the file in `nano`, press `Ctrl+X`, then `Y` to confirm the changes, and finally `Enter` to write the file with the name `playbook.yml`.
            5. **Check the Playbook Syntax**
                - Before running a playbook, it's always a good practice to check its syntax for any errors.
                - `ansible-playbook --syntax-check playbook.yml` Explain Code
                - If the syntax is correct, you will see the playbook's file path as output, confirming it's valid:
                - `playbook: playbook.yml` Explain Code
                - If you see any errors, reopen the file with `nano playbook.yml` and fix them. Pay close attention to correct indentation (usually two spaces).
            6. **Run the Playbook**
                - Now, execute the playbook. Ansible will connect to `localhost`, read the variables, and run the tasks.
                - `ansible-playbook playbook.yml` Explain Code
                - You should see output indicating the successful execution of each task. The `changed` status means that Ansible made a modification to the system, such as installing a package or creating a file.
                - ```
PLAY [Deploy Apache using variables] *******************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install the latest version of Apache] ************************************
changed: [localhost]

TASK [Create a basic index.html file] ******************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
                - If you run the playbook a second time, the tasks should report `ok` instead of `changed`, because the package is already installed and the file already has the correct content. This demonstrates Ansible's idempotency.
            7. **Verify the Configuration Manually**
                - Although the playbook has completed, you can manually verify that the tasks worked as expected. First, check if the `httpd` package was installed:
                - `rpm -q httpd` Explain Code
                - The output should show the package name and version:
                - `httpd-2.4.57-7.el9.x86_64` Explain Code
                - Next, check the content of the `index.html` file:
                - `cat /var/www/html/index.html` Explain Code
                - The output should match the value of your `web_content` variable:
                - `Hello from Ansible Variables` Explain Code
                - You have successfully used variables in an Ansible playbook to configure a system.
        - ![](https://remnote-user-data.s3.amazonaws.com/0hSCa3hb5mk-Ua-yxtRDqyj-0Zqyn0BbLmIpGjhQN5H1c5pX2yV67dsMr-MQ8bWAPhEfS9fHR3wwNdOqQS6iTeo2zoZbX77S8FumFTIcvHpMjRO1e9QpA7CAgZ2ggRV-.webp)**Labby**
        - 
        - # **Display System Information using Ansible Facts**
        - In this step, you will explore Ansible facts. Facts are pieces of information that Ansible gathers about the systems it manages (in this case, `localhost`). This information includes details like the operating system, network interfaces, memory, and much more. By default, Ansible collects facts at the beginning of every play, making them available in a special variable called `ansible_facts`. Using facts allows you to create dynamic playbooks that adapt to the environment they are running in.
            1. **Navigate to the Project Directory**
                - First, ensure you are in the `~/project` directory where you will create the new playbook.
                - `cd ~/project` Explain Code
            2. **Create a Playbook to Display All Facts**
                - Let's start by creating a playbook that simply displays all the facts Ansible can gather about your system. This will give you an idea of the vast amount of information available. Use `nano` to create a new file named `display_facts.yml`.
                - `nano display_facts.yml` Explain Code
                - Inside the `nano` editor, add the following content. This playbook targets `localhost` and uses the `ansible.builtin.debug` module to print the contents of the `ansible_facts` variable.
                - ```
---
- name: Display all Ansible facts
  hosts: localhost
  tasks:
    - name: Print all available facts
      ansible.builtin.debug:
        var: ansible_facts
``` Explain Code
                - Save the file and exit `nano` by pressing `Ctrl+X`, then `Y`, and `Enter`.
            3. **Run the Playbook**
                - Now, execute the playbook to see the result.
                - `ansible-playbook display_facts.yml` Explain Code
                - The output will be very long, as Ansible collects a lot of data. It will be a large JSON structure containing all the system details. This is expected.
                - ```
PLAY [Display all Ansible facts] ***********************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Print all available facts] ***********************************************
ok: [localhost] => {
    "ansible_facts": {
        "ansible_all_ipv4_addresses": [
            "172.17.0.2"
        ],
        "ansible_all_ipv6_addresses": [
            "fe80::42:acff:fe11:2"
        ],
        "ansible_apparmor": {
            "status": "disabled"
        },
        "ansible_architecture": "x86_64",
        "ansible_bios_date": "01/01/2011",
        "ansible_bios_version": "1.0",
        "ansible_cmdline": {
            "BOOT_IMAGE": "/boot/vmlinuz-5.14.0-427.16.1.el9_4.x86_64",
            "root": "UUID=...",
            "ro": true
        },
        "ansible_date_time": {
            "date": "2024-05-21",
            "day": "21",
            "epoch": "1716298855",
            ...
        },
        "ansible_distribution": "RedHat",
        "ansible_distribution_major_version": "9",
        "ansible_distribution_version": "9.4",
        ...
    }
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            4. **Create a Playbook to Display Specific Facts**
                - Displaying all facts is useful for discovery, but in most cases, you only need specific pieces of information. Let's create another playbook, `display_specific_facts.yml`, to display a formatted message with just a few key facts.
                - `nano display_specific_facts.yml` Explain Code
                - Add the following content. This playbook uses the `msg` parameter of the `debug` module to print a custom string. We access individual facts using bracket notation, like `ansible_facts['distribution']`.
                - ```
---
- name: Display specific Ansible facts
  hosts: localhost
  tasks:
    - name: Print a summary of system facts
      ansible.builtin.debug:
        msg: >
          The operating system is {{ ansible_facts['distribution'] }}
          version {{ ansible_facts['distribution_major_version'] }}.
          It has {{ ansible_facts['processor_cores'] }} processor cores and
          {{ ansible_facts['memtotal_mb'] }} MB of total memory.
``` Explain Code
                - The `>` character in `msg: >` is a YAML feature that allows you to write a multi-line string more cleanly. Save the file and exit `nano`.
            5. **Run the Playbook for Specific Facts**
                - Now, run this new playbook.
                - `ansible-playbook display_specific_facts.yml` Explain Code
                - The output will be much cleaner and more readable, showing only the information you requested.
                - ```
PLAY [Display specific Ansible facts] ******************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Print a summary of system facts] *****************************************
ok: [localhost] => {
    "msg": "The operating system is RedHat version 9. It has 2 processor cores and 3925 MB of total memory."
}

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
                - This demonstrates how you can leverage Ansible facts to make your playbooks aware of the environment they are running in, allowing for more intelligent and conditional automation.
        - ![](https://remnote-user-data.s3.amazonaws.com/cskURb6fbJOeoRjQFpM3H96QxZ6iT-gbU7UC5-OKh9XWlZxGGRde_8UpOrdA3zGDI0RvkIuz3mDkTOswgSgVrTbnFtyxjCE1HdJSqEttmrN-pkAoveTrRoSzDYsiRRLv.webp)**Labby**
        - 
        - # **Configure the Web Server using Custom Facts from the Managed Host**
        - In this step, you will learn how to use custom facts. While Ansible automatically gathers a wide range of standard facts, you can also define your own. These are called "local facts" or "custom facts". This is a powerful feature that allows you to provide specific information from a managed host to your playbooks, such as application settings or hardware-specific data that Ansible doesn't collect by default.
        - Ansible looks for custom facts in the `/etc/ansible/facts.d` directory on the managed host. Any file in this directory with a `.fact` extension will be processed. These files can be simple INI-style text files or JSON files.
            1. **Create the Custom Facts Directory**
                - First, you need to create the directory where Ansible will look for custom fact files. Since this is a system directory, you must use `sudo` to create it.
                - `sudo mkdir -p /etc/ansible/facts.d` Explain Code
                - The `-p` flag ensures that the command doesn't return an error if the directory already exists.
            2. **Create a Custom Fact File**
                - Now, let's create a custom fact file to define a welcome message for our web server. We will create an INI-formatted file named `web_config.fact` inside the `/etc/ansible/facts.d` directory.
                - `sudo nano /etc/ansible/facts.d/web_config.fact` Explain Code
                - Add the following content to the file. This defines a section `[webserver]` with a key `welcome_message`.
                - ```
[webserver]
welcome_message = Welcome to the server configured by Custom Facts!
``` Explain Code
                - Save the file and exit `nano` by pressing `Ctrl+X`, then `Y`, and `Enter`.
            3. **Create a Playbook to Use the Custom Fact**
                - With the custom fact in place, we can now create a playbook that reads this fact and uses it to configure our web server's home page. In your `~/project` directory, create a new playbook named `configure_web.yml`.
                - ```
cd ~/project
nano configure_web.yml
``` Explain Code
                - Add the following content to the playbook. This playbook will update the `/var/www/html/index.html` file with the message defined in our custom fact.
                - ```
---
- name: Configure web server using custom facts
  hosts: localhost
  become: true
  tasks:
    - name: Update index.html with custom message
      ansible.builtin.copy:
        content: "{{ ansible_facts.ansible_local.web_config.webserver.welcome_message }}"
        dest: /var/www/html/index.html
``` Explain Code
                - Let's break down the variable `{{ ansible_facts.ansible_local.web_config.webserver.welcome_message }}`:
                    - `ansible_facts`: The root dictionary for all facts.
                    - `ansible_local`: The key where all custom facts are stored.
                    - `web_config`: The name of our fact file (`web_config.fact`), without the extension.
                    - `webserver`: The section name `[webserver]` from our INI file.
                    - `welcome_message`: The key for the value we want to use.
                - Save the file and exit `nano`.
            4. **Run the Configuration Playbook**
                - Now, execute the playbook to apply the configuration.
                - `ansible-playbook configure_web.yml` Explain Code
                - The output should show that the `copy` task has `changed` the `index.html` file.
                - ```
PLAY [Configure web server using custom facts] *********************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Update index.html with custom message] ***********************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            5. **Verify the Result**
                - Finally, let's verify that the web page was updated correctly. Use the `cat` command to view the contents of the `index.html` file.
                - `cat /var/www/html/index.html` Explain Code
                - The output should now display the message from your custom fact file:
                - `Welcome to the server configured by Custom Facts!` Explain Code
                - You have successfully created a custom fact on the managed host and used it within a playbook to dynamically configure a service. This technique is incredibly useful for making your automation more flexible and data-driven.
        - ![](https://remnote-user-data.s3.amazonaws.com/4w1HY-HcSOw7-eanAhZAwSaoFxJAsAZBuLiAE2ubuPScOt3XEJuhgDXzfY1YohoNqGXH8bkyuaRPNM6N_c2jr8hJGwSDdn-8EbPOfbca9QzofYOhaCxjq_CEENvJKyzf.webp)**Labby**
        - 
        - # **Create a System User using Encrypted Variables with Ansible Vault**
        - In this step, you will learn how to manage sensitive data, such as passwords or API keys, using Ansible Vault. Storing sensitive information in plain text within your playbooks is a major security risk. Ansible Vault provides a way to encrypt files or individual variables, keeping your secrets safe. You can then use these encrypted files in your playbooks, and Ansible will decrypt them at runtime when you provide the correct password.
        - We will create an encrypted file containing a username and a hashed password, and then use a playbook to create a new system user with these credentials.
            1. **Navigate to the Project Directory**
                - Ensure you are in the `~/project` directory for this task.
                - `cd ~/project` Explain Code
            2. **Create an Encrypted Vault File**
                - We will use the `ansible-vault create` command to create a new, encrypted YAML file named `secrets.yml`. This command will prompt you to create a password for the vault. This password is required to open, edit, or use the file later.
                - First, let's set the editor to `nano` to make it easier to work with:
                - `export EDITOR=nano` Explain Code
                - Now create the vault file:
                - `ansible-vault create secrets.yml` Explain Code
                - When prompted, enter a password for your vault. For this lab, let's use `labex` as the vault password to keep things simple. You will need to enter it twice.
                - ```
New Vault password:
Confirm New Vault password:
``` Explain Code
                - After you confirm the password, the command will open the `secrets.yml` file in the `nano` text editor.
            3. **Add Secret Variables to the Vault File**
                - Inside the `nano` editor, which is now editing the encrypted `secrets.yml` file, add the following variables. We will define a username and a pre-hashed password for a new user. Using a hashed password is much more secure than storing a plain-text password.
                - ```
username: myappuser
pwhash: $6$mysalt$QwMzWSEyCAGmz7tzVrAi5o.8k4d05i2QsfGGwmPtlJsWhGjSjCW6yFCH/OEqEsHk7GMSxqYNXu5sshxPmWyxo0
``` Explain Code
                    - `username`: The name of the system user we want to create.
                    - `pwhash`: A securely hashed password. This specific hash corresponds to the password `AnsibleUserP@ssw0rd` and is in a format that the `ansible.builtin.user` module understands.
                - Save the file and exit `nano` (`Ctrl+X`, then `Y`, then `Enter`). The `secrets.yml` file in your `~/project` directory is now encrypted. If you try to view it with `cat secrets.yml`, you will only see encrypted text.
            4. **Create a Playbook to Use the Vault File**
                - Now, create a new playbook named `create_user.yml` that will use the variables from your encrypted `secrets.yml` file.
                - `nano create_user.yml` Explain Code
                - Add the following content. The `vars_files` directive tells Ansible to load variables from the specified file.
                - ```
---
- name: Create a user from secret variables
  hosts: localhost
  become: true
  vars_files:
    - secrets.yml
  tasks:
    - name: Create the {{ username }} user
      ansible.builtin.user:
        name: "{{ username }}"
        password: "{{ pwhash }}"
        state: present
``` Explain Code
                - This playbook will create a user with the name and password hash defined in `secrets.yml`. Save the file and exit `nano`.
            5. **Run the Playbook with the Vault Password**
                - To run a playbook that uses a vaulted file, you must provide the vault password. You can do this interactively using the `--ask-vault-pass` flag.
                - `ansible-playbook --ask-vault-pass create_user.yml` Explain Code
                - Ansible will prompt you for the vault password. Enter `labex` (the password you set in step 2).
                - `Vault password:` Explain Code
                - After you provide the correct password, Ansible will decrypt the file in memory and run the playbook. You should see the following output, indicating the user was created.
                - ```
PLAY [Create a user from secret variables] *************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Create the myappuser user] ***********************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            6. **Verify the User was Created**
                - You can confirm that the `myappuser` was successfully created on the system by using the `id` command.
                - `id myappuser` Explain Code
                - If the user exists, you will see their user ID (uid) and group ID (gid) information.
                - `uid=1002(myappuser) gid=1002(myappuser) groups=1002(myappuser)` Explain Code
                - This confirms that you have successfully used Ansible Vault to manage sensitive data for your automation tasks.
        - ![](https://remnote-user-data.s3.amazonaws.com/fnOFaBR6pvE4WzuU_SsoczgBPoPbZY0CnD41w3s9mY_w0tOSkcny_F89fAeIKRGCKvVlY-MUABcViWo3WKHiXWSOBe6urb-uGQH5vYMVcDQEhfxIejOVJd8Hx-lTvB_r.webp)**Labby**
        - 
        - # **Run a Playbook with a Vault Password File to Apply Configurations**
        - In this step, you will learn a more automated way to provide the vault password to Ansible. In the previous step, you used `--ask-vault-pass` to enter the password interactively. While this is secure, it's not suitable for automated environments like CI/CD pipelines where no user is present to type a password.
        - The solution is to use a vault password file. This is a simple text file that contains the vault password. You can then reference this file when running your playbook, and Ansible will read the password from it automatically. For security, it is crucial to restrict the permissions of this password file so that only authorized users can read it.
            1. **Navigate to the Project Directory**
                - Make sure you are in the `~/project` directory where your playbook and vault file are located.
                - `cd ~/project` Explain Code
            2. **Create the Vault Password File**
                - Let's create a file to store our vault password. We will name it `vault_pass.txt`. We can use the `echo` command to create the file and write the password (`labex`) into it in a single step.
                - `echo "labex" > vault_pass.txt` Explain Code
                - You can verify the file's content with `cat`:
                - `cat vault_pass.txt` Explain Code
                - The output should be:
                - `labex` Explain Code
            3. **Secure the Password File**
                - Storing a password in a plain text file is risky. You must restrict its file permissions to protect it. The `chmod` command allows you to change file permissions. We will set the permissions to `600`, which means only the file owner (in this case, the `labex` user) has read and write permissions. No other users on the system will be able to access it.
                - `chmod 600 vault_pass.txt` Explain Code
                - You can verify the new permissions using the `ls -l` command:
                - `ls -l vault_pass.txt` Explain Code
                - The output should start with `-rw-------`, confirming the restricted permissions.
                - `-rw-------. 1 labex labex 6 May 21 14:30 vault_pass.txt` Explain Code
            4. **Modify the Playbook to Add a User to a Group**
                - Let's modify our `create_user.yml` playbook to perform an additional action. We will add the `myappuser` to the `wheel` group, which on many systems grants administrative (sudo) privileges. This will demonstrate running a playbook that makes a change to an existing configuration.
                - First, open the `create_user.yml` playbook for editing.
                - `nano create_user.yml` Explain Code
                - Modify the `ansible.builtin.user` task to include the `groups` and `append` parameters.
                - ```
---
- name: Create a user from secret variables
  hosts: localhost
  become: true
  vars_files:
    - secrets.yml
  tasks:
    - name: Create the {{ username }} user and add to wheel group
      ansible.builtin.user:
        name: "{{ username }}"
        password: "{{ pwhash }}"
        state: present
        groups: wheel
        append: true
``` Explain Code
                    - `groups: wheel`: Specifies the group to add the user to.
                    - `append: true`: Ensures that the user is added to this group without removing them from any other groups they might belong to.
                - Save the file and exit `nano`.
            5. **Run the Playbook with the Vault Password File**
                - Now, run the playbook again. This time, instead of `--ask-vault-pass`, use the `--vault-password-file` option (or its shorter alias `--vault-pass-file`) to specify the path to your password file.
                - `ansible-playbook --vault-password-file vault_pass.txt create_user.yml` Explain Code
                - Ansible will now run without prompting for a password because it reads it directly from `vault_pass.txt`. You should see output indicating that the user's configuration was changed.
                - ```
PLAY [Create a user from secret variables] *************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Create the myappuser user and add to wheel group] ************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
                - The `changed` status confirms that Ansible modified the user by adding them to the `wheel` group.
            6. **Verify the User's Group Membership**
                - Finally, verify that `myappuser` is now a member of the `wheel` group. You can do this with the `groups` command.
                - `groups myappuser` Explain Code
                - The output should show both the user's primary group (`myappuser`) and the `wheel` group.
                - `myappuser : myappuser wheel` Explain Code
                - You have successfully used a vault password file to run a playbook non-interactively, a key skill for automating secure workflows.
        - ![](https://remnote-user-data.s3.amazonaws.com/PbBkDVziCajTOnYU0pOPMt6qgmtSSb3zbTM_oxp12nwoWwuEfkpmVKVpGgUowXfp3qI6ATDWrMZ7FQHzY-f_JRPc7ffFyk89AeCzdGQujvP6cWI1CDt7qQKM0itlPKHc.webp)**Labby**
        - 
        - # **Verify the Web Server and User Configuration**
        - In this final step, you will consolidate your learning by creating a dedicated verification playbook. So far, you have been manually checking the results of your playbooks using standard Linux commands like `cat`, `id`, and `groups`. A more powerful and repeatable approach is to use Ansible itself to audit and validate the state of your system.
        - This playbook will act as a test suite, programmatically checking that the web server is installed, the web page has the correct content, and the system user exists with the proper group membership. This demonstrates how Ansible can be used not just for configuration management, but also for compliance and state validation.
            1. **Navigate to the Project Directory**
                - First, ensure you are in the `~/project` directory.
                - `cd ~/project` Explain Code
            2. **Create the Verification Playbook**
                - Let's create a new playbook named `verify_config.yml`. This playbook will contain a series of tasks that check the configurations you applied in the previous steps.
                - `nano verify_config.yml` Explain Code
            3. **Add Tasks to Verify the Configuration**
                - Inside the `nano` editor, add the following content. We will build this playbook with several tasks, each one designed to assert a specific condition is true. If any assertion fails, the playbook will stop and report an error, immediately telling you what is wrong.
                - ```
---
- name: Verify system configuration
  hosts: localhost
  become: true
  tasks:
    - name: Check if httpd package is installed
      ansible.builtin.dnf:
        list: httpd
      register: httpd_pkg_info

    - name: Assert that httpd is installed
      ansible.builtin.assert:
        that:
          - httpd_pkg_info.results | length > 0
        fail_msg: "Apache (httpd) package is not installed."
        success_msg: "Apache (httpd) package is installed."

    - name: Read the content of the index.html file
      ansible.builtin.slurp:
        src: /var/www/html/index.html
      register: index_file

    - name: Assert that the web page content is correct
      ansible.builtin.assert:
        that:
          - "'Custom Facts' in (index_file.content | b64decode)"
        fail_msg: "Web page content is incorrect."
        success_msg: "Web page content is correct."

    - name: Check if myappuser exists
      ansible.builtin.getent:
        database: passwd
        key: myappuser
      register: user_info

    - name: Assert that myappuser exists
      ansible.builtin.assert:
        that:
          - user_info.getent_passwd['myappuser'] is defined
        fail_msg: "User 'myappuser' does not exist."
        success_msg: "User 'myappuser' exists."

    - name: Assert that myappuser is in the wheel group
      ansible.builtin.assert:
        that:
          - "'wheel' in user_info.getent_passwd['myappuser'][3]"
        fail_msg: "User 'myappuser' is not in the wheel group."
        success_msg: "User 'myappuser' is in the wheel group."
``` Explain Code
                - Let's review the key modules used here:
                    - `ansible.builtin.dnf` with `list`: This checks for a package and `register`s the result.
                    - `ansible.builtin.slurp`: This "slurps" up the entire content of a file from the remote host. The content is base64-encoded for safe transport.
                    - `ansible.builtin.getent`: This is a safe way to query system databases like `passwd` and `group`.
                    - `ansible.builtin.assert`: This is the core of our verification. It checks if a given condition is true. If not, it fails the play. We provide custom success and failure messages.
                    - `b64decode`: This is a Jinja2 filter used to decode the base64 content we got from the `slurp` module.
                - Save the file and exit `nano` (`Ctrl+X`, `Y`, `Enter`).
            4. **Run the Verification Playbook**
                - Now, execute your verification playbook. Since it doesn't use any vaulted files, you don't need to provide a password.
                - `ansible-playbook verify_config.yml` Explain Code
                - If all your previous steps were completed correctly, the playbook will run successfully, and you will see the custom success message for each assertion.
                - ```
PLAY [Verify system configuration] *********************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Check if httpd package is installed] *************************************
ok: [localhost]

TASK [Assert that httpd is installed] ******************************************
ok: [localhost] => {
    "changed": false,
    "msg": "Apache (httpd) package is installed."
}

TASK [Read the content of the index.html file] *********************************
ok: [localhost]

TASK [Assert that the web page content is correct] *****************************
ok: [localhost] => {
    "changed": false,
    "msg": "Web page content is correct."
}

TASK [Check if myappuser exists] ***********************************************
ok: [localhost]

TASK [Assert that myappuser exists] ********************************************
ok: [localhost] => {
    "changed": false,
    "msg": "User 'myappuser' exists."
}

TASK [Assert that myappuser is in the wheel group] *****************************
ok: [localhost] => {
    "changed": false,
    "msg": "User 'myappuser' is in the wheel group."
}

PLAY RECAP *********************************************************************
localhost                  : ok=9    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
                - Congratulations! You have successfully used Ansible to define variables, gather system facts, manage secrets with Vault, and finally, to verify the state of your system in an automated way.
        - ![](https://remnote-user-data.s3.amazonaws.com/4sJsCfvNmHqpM5ymLwdGIw2uw8WcY-q_CyUpRUsRuA6h45_IsjHXN9fz9O25E7rRLRwusqSgCiqxLhtlSX_r1kJh5VNwf9uxr2M4kVIAs4vLLCl9ltmOad7E4gsiubi_.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned to manage different types of data within Ansible playbooks to configure a RHEL system. You began by defining and using standard playbook variables to flexibly install and configure an Apache web server. Following this, you explored how to leverage Ansible's built-in facts to display system information, providing a foundation for creating dynamic and host-aware automation tasks.
        - Building on this, you configured the web server further by creating and utilizing custom facts from the managed host. To handle sensitive information securely, you used Ansible Vault to encrypt a user password, created a new system user with this encrypted variable, and executed the playbook non-interactively with a vault password file. The lab concluded by verifying that both the web server and the new system user were configured correctly, confirming the successful application of all learned concepts.
    4. **Control Ansible Playbook Execution on RHEL**
        - Write a Playbook with Loops and Conditionals
        - Implement Handlers to Trigger Service Restarts
        - Manage Task Failures with Block and Rescue
        - Control Task State with changed_when and failed_when
        - Deploy a Secure Web Server Using Task Control
        - 
        - # **Introduction**
        - In this lab, you will learn how to control the execution flow of Ansible playbooks on a Red Hat Enterprise Linux (RHEL) system. You will start by writing a playbook that utilizes fundamental control structures, including loops to repeat tasks efficiently and conditionals to run tasks only when specific criteria are met. You will also implement handlers to trigger actions, such as service restarts, only when a change occurs, making your automation more intelligent and efficient.
        - Building on these foundational skills, you will explore more advanced techniques for managing playbook execution. This includes using block and rescue statements to handle task failures gracefully and employing `changed_when` and `failed_when` to gain fine-grained control over task status. To conclude the lab, you will apply all these concepts in a practical exercise to deploy a secure web server, solidifying your ability to create robust and reliable Ansible automation.
        - ![](https://remnote-user-data.s3.amazonaws.com/iBpeskHOIX5_xp-jTOrxRCJFFaALxGy5C_AnCN05nRoiW3IMjL3-TUQgRbJQ8Jv7fUEvYNBQHdGNy5sbwUSzYoapLlipjY8J8-REjNlfc21iLpklVxYiw-Pgwc3ufo6e.webp)**Labby** 
        - 
        - # **Write a Playbook with Loops and Conditionals**
        - In this step, you will learn two fundamental concepts in Ansible for controlling task execution: loops and conditionals. Loops allow you to repeat a task multiple times with different values, which is highly efficient for tasks like installing multiple packages or creating multiple users. Conditionals, using the `when` keyword, allow you to run a task only when specific criteria are met, such as the operating system being a particular version or a file already existing.
        - First, let's ensure Ansible is installed on your LabEx VM. We will use the DNF package manager for this.
        - `sudo dnf install -y ansible-core` Explain Code
        - You should see output indicating that `ansible-core` and its dependencies are being installed.
        - ```
...
Installed:
  ansible-core-2.x.x-1.el9.x86_64
  ...
Complete!
``` Explain Code
        - Now, let's set up our project directory. All our work for this lab will be inside a dedicated directory to keep things organized.
        - ```
cd ~/project
mkdir control-flow-lab
cd control-flow-lab
``` Explain Code
        - An Ansible project needs an inventory file, which defines the hosts you want to manage. For this lab, we will manage the local machine, `localhost`.
        - Create an inventory file named `inventory` using the `nano` editor:
        - `nano inventory` Explain Code
        - Add the following line to the file. This tells Ansible to run the playbook on `localhost` and to connect to it directly instead of using SSH.
        - `localhost ansible_connection=local` Explain Code
        - Save the file and exit `nano` by pressing `Ctrl+X`, then `Y`, and `Enter`.
        - Next, we will create our first playbook, `playbook.yml`, to demonstrate a loop. This playbook will install a list of useful command-line tools.
        - `nano playbook.yml` Explain Code
        - Enter the following YAML content into the editor. This playbook defines one task that uses the `ansible.builtin.dnf` module to install packages. The `become: yes` directive tells Ansible to execute tasks with `sudo` privileges, which is necessary for installing packages. The `loop` keyword provides a list of package names. Ansible will run this task once for each item in the list, substituting the `{{ item }}` placeholder with the current package name.
        - ```
---
- name: Install common tools
  hosts: localhost
  become: yes
  tasks:
    - name: Install specified packages
      ansible.builtin.dnf:
        name: "{{ item }}"
        state: present
      loop:
        - git
        - tree
        - wget
``` Explain Code
        - Save and exit the editor. Now, run the playbook using the `ansible-playbook` command, specifying your inventory file with the `-i` flag.
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - The output will show the playbook execution. Ansible will check each package and install it if it's not already present. The `PLAY RECAP` at the end summarizes the results.
        - ```
PLAY [Install tools and run conditional tasks] *********************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install specified packages] **********************************************
changed: [localhost] => (item=git)
changed: [localhost] => (item=tree)
changed: [localhost] => (item=wget)

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - Now, let's modify the playbook to include a conditional task. We will add a task that prints a message, but only if the operating system is Red Hat Enterprise Linux. This is a common use case for tailoring automation to specific environments.
        - Open the `playbook.yml` file again:
        - `nano playbook.yml` Explain Code
        - Add the following tasks to the end of the file. The `when` keyword evaluates the given expression. `ansible_facts['distribution']` is a variable that Ansible automatically discovers about the managed host. The first task will run because our environment is RHEL, and the second task will be skipped.
        - ```
---
- name: Install tools and run conditional tasks
  hosts: localhost
  become: yes
  tasks:
    - name: Install specified packages
      ansible.builtin.dnf:
        name: "{{ item }}"
        state: present
      loop:
        - git
        - tree
        - wget

    - name: Show message on Red Hat systems
      ansible.builtin.debug:
        msg: "This system is a Red Hat family distribution."
      when: ansible_facts['distribution'] == "RedHat"

    - name: Show message on other systems
      ansible.builtin.debug:
        msg: "This system is NOT a Red Hat family distribution."
      when: ansible_facts['distribution'] != "RedHat"
``` Explain Code
        - Save and exit the editor. Run the updated playbook:
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - Observe the output carefully. The package installation task will likely report `ok` for all items since they are already installed. More importantly, you will see the first debug message printed, while the second one is marked as `skipping`.
        - ```
PLAY [Install tools and run conditional tasks] *********************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install specified packages] **********************************************
ok: [localhost] => (item=git)
ok: [localhost] => (item=tree)
ok: [localhost] => (item=wget)

TASK [Show message on Red Hat systems] *****************************************
ok: [localhost] => {
    "msg": "This system is a Red Hat family distribution."
}

TASK [Show message on other systems] *******************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
``` Explain Code
        - You have successfully written and executed an Ansible playbook that uses both loops to perform repetitive actions and conditionals to control task execution based on system facts.
        - ![](https://remnote-user-data.s3.amazonaws.com/brzwTmDYqWBkopfjVRktb4eFAFqoKkuf450W5Nlt6i_FeZ0SY8ESBHOHwmDl9lOm_jzwtq8FrNfORNffVfFa19Eqr2CQXD50h7JJBj1PKSVCZ-cWI8aTXSMmXwGeIjch.webp)**Labby**
        - 
        - # **Implement Handlers to Trigger Service Restarts**
        - In this step, you will learn about Ansible handlers. Handlers are special tasks that only run when "notified" by another task. They are typically used for actions that should only occur when a change has been made, such as restarting a service after its configuration file has been updated. This approach is more efficient than restarting a service on every playbook run, as it ensures the action is only taken when necessary.
        - We will build a playbook that installs the Nginx web server, deploys a custom homepage, and uses a handler to reload Nginx only when the homepage content changes.
        - First, let's create a new directory for this exercise to keep our project organized.
        - ```
cd ~/project
mkdir control-handlers-lab
cd control-handlers-lab
``` Explain Code
        - As before, we need an inventory file to tell Ansible where to run the playbook.
        - `nano inventory` Explain Code
        - Add the following line to specify the local machine.
        - `localhost ansible_connection=local` Explain Code
        - Save and exit the editor (`Ctrl+X`, `Y`, `Enter`).
        - Next, we need a file to serve as our web server's homepage. We'll create a `files` directory to store it.
        - `mkdir files` Explain Code
        - Now, create a simple `index.html` file inside the `files` directory.
        - `nano files/index.html` Explain Code
        - Add the following HTML content:
        - `<h1>Welcome to the Ansible Handler Lab!</h1>` Explain Code
        - Save and exit the editor.
        - Now, you will create the playbook `deploy_nginx.yml`. This playbook will perform three main actions: install Nginx, copy the `index.html` file, and define a handler to reload Nginx.
        - `nano deploy_nginx.yml` Explain Code
        - Enter the following content. Pay close attention to the `notify` keyword in the "Copy homepage" task and the corresponding `handlers` section at the end. The `become: yes` directive tells Ansible to execute tasks with `sudo` privileges, which is necessary for installing packages and managing services.
        - ```
---
- name: Deploy Nginx with a handler
  hosts: localhost
  become: yes
  tasks:
    - name: Ensure Nginx is installed
      ansible.builtin.dnf:
        name: nginx
        state: present

    - name: Start and enable Nginx service
      ansible.builtin.systemd:
        name: nginx
        state: started
        enabled: yes

    - name: Copy homepage
      ansible.builtin.copy:
        src: files/index.html
        dest: /usr/share/nginx/html/index.html
      notify: reload nginx

  handlers:
    - name: reload nginx
      ansible.builtin.systemd:
        name: nginx
        state: reloaded
``` Explain Code
        - Save and exit the editor.
        - Now, run the playbook for the first time.
        - `ansible-playbook -i inventory deploy_nginx.yml` Explain Code
        - You will see output showing that Nginx was installed (or was already present), the Nginx service was started and enabled, the `index.html` file was copied (status `changed`), and importantly, the handler was notified and executed at the end of the play.
        - ```
...
TASK [Copy homepage] ***********************************************************
changed: [localhost]

RUNNING HANDLER [reload nginx] *************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - You can verify that the web server is running and serving your custom page using `curl`.
        - `curl http://localhost` Explain Code
        - The output should be the content of your `index.html` file.
        - `<h1>Welcome to the Ansible Handler Lab!</h1>` Explain Code
        - Now, run the exact same playbook again without making any changes.
        - `ansible-playbook -i inventory deploy_nginx.yml` Explain Code
        - This time, observe the output. The "Copy homepage" task will report `ok` instead of `changed` because the file on the destination already matches the source. The "Start and enable Nginx service" task will also report `ok` since the service is already running and enabled. Because no tasks notified the handler, the handler was not run.
        - ```
...
TASK [Copy homepage] ***********************************************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - To see the handler in action again, let's modify the source `index.html` file.
        - `nano files/index.html` Explain Code
        - Change the content to the following:
        - `<h1>The Handler Ran Again!</h1>` Explain Code
        - Save and exit. Now, run the playbook one more time.
        - `ansible-playbook -i inventory deploy_nginx.yml` Explain Code
        - Because the source file changed, the "Copy homepage" task will again report `changed`, which in turn notifies and runs the `reload nginx` handler.
        - ```
...
TASK [Copy homepage] ***********************************************************
changed: [localhost]

RUNNING HANDLER [reload nginx] *************************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - Verify the change with `curl` one last time.
        - `curl http://localhost` Explain Code
        - You should see the updated message.
        - `<h1>The Handler Ran Again!</h1>` Explain Code
        - This exercise demonstrates the power and efficiency of handlers for managing service state in response to configuration changes.
        - ![](https://remnote-user-data.s3.amazonaws.com/inlTuw6AQ98yEKJAoIR8O-iZfA63ywJOFmQ_-BbnvO3v1HdQa_vhFbODhotV3G7AA1CEwKDVcgq3tVUJtYUOLdSTdpzhUTpL5Ka-xxPmUdE40MVtmjC4laKNoRuTewb2.webp)**Labby**
        - 
        - # **Manage Task Failures with Block and Rescue**
        - In this step, you will learn how to gracefully handle errors in your Ansible playbooks. By default, if any task fails, Ansible stops executing the entire playbook on that host. While this is a safe default, sometimes you need more control. You will explore two methods for error handling: the simple `ignore_errors` directive and the more powerful `block`, `rescue`, and `always` structure, which provides a way to attempt tasks and define recovery actions if they fail.
        - First, let's create a new directory for this exercise.
        - ```
cd ~/project
mkdir control-errors-lab
cd control-errors-lab
``` Explain Code
        - Create the standard `inventory` file for `localhost`.
        - `nano inventory` Explain Code
        - Add the following content:
        - `localhost ansible_connection=local` Explain Code
        - Save and exit the editor (`Ctrl+X`, `Y`, `Enter`).
        - Now, let's create a playbook named `playbook.yml` that is designed to fail. The first task will attempt to install a package that does not exist.
        - `nano playbook.yml` Explain Code
        - Enter the following content. This playbook tries to install a fake package `httpd-fake` and then a real package, `mariadb-server`.
        - ```
---
- name: Demonstrate Task Failure
  hosts: localhost
  become: yes
  tasks:
    - name: Attempt to install a non-existent package
      ansible.builtin.dnf:
        name: httpd-fake
        state: present

    - name: Install MariaDB server
      ansible.builtin.dnf:
        name: mariadb-server
        state: present
``` Explain Code
        - Save and exit the editor. Now, run the playbook.
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - You will see the first task fail with an error message because the `httpd-fake` package cannot be found. Crucially, Ansible will stop, and the second task, "Install MariaDB server," will not be executed.
        - ```
...
TASK [Attempt to install a non-existent package] *******************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "No match for argument: httpd-fake", "rc": 1, "results": []}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
``` Explain Code
        - Now, let's use `block` and `rescue` to handle this failure more elegantly. The `block` keyword groups a set of tasks. If any task within the `block` fails, Ansible skips the rest of the tasks in the `block` and executes the tasks in the `rescue` section. The `always` section will run regardless of whether the `block` or `rescue` sections succeeded or failed.
        - Modify `playbook.yml` to use this structure.
        - `nano playbook.yml` Explain Code
        - Replace the entire content with the following. Here, we try to install the fake package in the `block`. When it fails, the `rescue` section will run, installing `mariadb-server` as a recovery step. The `always` section will print a message at the end.
        - ```
---
- name: Handle Task Failure with Block and Rescue
  hosts: localhost
  become: yes
  tasks:
    - name: Attempt primary task, with recovery
      block:
        - name: Attempt to install a non-existent package
          ansible.builtin.dnf:
            name: httpd-fake
            state: present
        - name: This task will be skipped
          ansible.builtin.debug:
            msg: "This message will not appear because the previous task fails."
      rescue:
        - name: Install MariaDB server on failure
          ansible.builtin.dnf:
            name: mariadb-server
            state: present
      always:
        - name: This always runs
          ansible.builtin.debug:
            msg: "The block has completed, either by success or rescue."
``` Explain Code
        - Save and exit. Run the playbook again.
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - Observe the output. The first task in the `block` fails as expected. The second task in the `block` is skipped. Ansible then moves to the `rescue` section and successfully installs `mariadb-server`. Finally, the `always` section runs.
        - ```
...
TASK [Attempt to install a non-existent package] *******************************
fatal: [localhost]: FAILED! => ...

TASK [This task will be skipped] ***********************************************
skipping: [localhost]

RESCUE START *******************************************************************

TASK [Install MariaDB server on failure] ***************************************
changed: [localhost]

ALWAYS START *******************************************************************

TASK [This always runs] ********************************************************
ok: [localhost] => {
    "msg": "The block has completed, either by success or rescue."
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=1    ignored=0
``` Explain Code
        - Now, let's see what happens when the `block` succeeds. Edit the playbook and fix the package name.
        - `nano playbook.yml` Explain Code
        - Change `httpd-fake` to a real package, `httpd`.
        - ```
# ... (rest of the playbook)
block:
  - name: Attempt to install a valid package
    ansible.builtin.dnf:
      name: httpd # Corrected from httpd-fake
      state: present
  - name: This task will now run
    ansible.builtin.debug:
      msg: "This message will now appear because the previous task succeeds."
# ... (rest of the playbook)
``` Explain Code
        - Save and exit. Run the playbook one last time.
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - This time, both tasks in the `block` succeed. Because the `block` completed without errors, the `rescue` section is skipped entirely. The `always` section still runs, as its name implies.
        - ```
...
TASK [Attempt to install a valid package] **************************************
changed: [localhost]

TASK [This task will now run] **************************************************
ok: [localhost] => {
    "msg": "This message will now appear because the previous task succeeds."
}

RESCUE START *******************************************************************
skipping rescue

ALWAYS START *******************************************************************

TASK [This always runs] ********************************************************
ok: [localhost] => {
    "msg": "The block has completed, either by success or rescue."
}

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - You have now successfully used the `block`/`rescue`/`always` structure to create a robust playbook that can handle failures and perform recovery actions.
        - ![](https://remnote-user-data.s3.amazonaws.com/LcMQhBjKgVhk3h0X5JXbV6TRDMQZhD2p8a6ZXNV8vBwfPVDpnPIpyk5HB78qwNmRgEAmP_KsOKOYjGPSLI71SzU-3s4CFgfaLWIiORxQKm9POKJSB1JNF49sFDsfXLzB.webp)**Labby**
        - 
        - # **Control Task State with changed_when and failed_when**
        - In this step, you will gain finer control over how Ansible interprets the outcome of your tasks. You'll learn about two powerful directives: `changed_when` and `failed_when`.
            - `changed_when`: By default, modules like `ansible.builtin.command` or `ansible.builtin.shell` almost always report a "changed" state, even if the command they ran didn't alter the system. `changed_when` allows you to define a custom condition that determines if a task should be reported as "changed". This is crucial for writing idempotent playbooks and for accurately triggering handlers.
            - `failed_when`: Sometimes, a command might exit with a non-zero status code (which Ansible considers a failure) even when the outcome is acceptable. `failed_when` lets you override the default failure conditions, allowing your playbook to continue based on more intelligent criteria, such as the command's output or a specific exit code.
        - Let's begin by setting up a new project directory.
        - ```
cd ~/project
mkdir control-state-lab
cd control-state-lab
``` Explain Code
        - Create the standard `inventory` file for `localhost`.
        - `nano inventory` Explain Code
        - Add the following content:
        - `localhost ansible_connection=local` Explain Code
        - Save and exit the editor (`Ctrl+X`, `Y`, `Enter`).
        - ### **Using** `**changed_when**`
        - First, let's see how a command task behaves by default. We'll create a playbook that runs the `date` command. This command simply prints the date and does not change the system, but the `command` module will report it as a change.
        - Create a new playbook named `playbook.yml`.
        - `nano playbook.yml` Explain Code
        - Enter the following content:
        - ```
---
- name: Control Task State
  hosts: localhost
  tasks:
    - name: Check local time (default behavior)
      ansible.builtin.command: date
``` Explain Code
        - Save and exit. Now, run the playbook.
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - Notice in the output that the task is reported as `changed=1`, even though nothing on the system was modified.
        - ```
...
TASK [Check local time (default behavior)] *************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    ...
``` Explain Code
        - Now, let's use `changed_when` to tell Ansible that this command never changes the system. Modify `playbook.yml`.
        - `nano playbook.yml` Explain Code
        - Add `changed_when: false` to the task.
        - ```
---
- name: Control Task State
  hosts: localhost
  tasks:
    - name: Check local time (with changed_when)
      ansible.builtin.command: date
      changed_when: false
``` Explain Code
        - Save and exit. Run the playbook again.
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - This time, the task reports `ok` and the final recap shows `changed=0`. You have successfully overridden the default behavior.
        - ```
...
TASK [Check local time (with changed_when)] ************************************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    ...
``` Explain Code
        - ### **Using** `**failed_when**`
        - Next, let's explore `failed_when`. We'll create a task that checks for the existence of a file that isn't there. The command will "fail" by default.
        - First, create a dummy file to search within.
        - `echo "System is running" > status.txt` Explain Code
        - Now, modify `playbook.yml` to search for the word "ERROR" in this file. The `grep` command will exit with a status code of 1 because the word is not found, which Ansible interprets as a failure.
        - `nano playbook.yml` Explain Code
        - Replace the content with the following:
        - ```
---
- name: Control Task State
  hosts: localhost
  tasks:
    - name: Check for ERROR in status file (will fail)
      ansible.builtin.command: grep ERROR status.txt
``` Explain Code
        - Save and exit. Run the playbook.
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - As expected, the playbook execution stops with a `FAILED!` message.
        - ```
...
TASK [Check for ERROR in status file (will fail)] ******************************
fatal: [localhost]: FAILED! => {"changed": true, "cmd": ["grep", "ERROR", "status.txt"], "delta": "...", "end": "...", "msg": "non-zero return code", "rc": 1, ...}
...
``` Explain Code
        - This is not what we want. The absence of "ERROR" is a success condition for us. We can use `failed_when` to redefine what constitutes a failure. We'll tell Ansible to only fail if the command's return code is greater than 1. A return code of 1 (pattern not found) will now be considered a success. We also need to `register` the task's result to inspect its return code (`rc`).
        - Modify `playbook.yml` one last time.
        - `nano playbook.yml` Explain Code
        - Update the playbook with `register` and `failed_when`.
        - ```
---
- name: Control Task State
  hosts: localhost
  tasks:
    - name: Check for ERROR in status file (with failed_when)
      ansible.builtin.command: grep ERROR status.txt
      register: grep_result
      failed_when: grep_result.rc > 1
      changed_when: false
``` Explain Code
        - We also added `changed_when: false` because `grep` is a read-only operation and doesn't change the system.
        - Save and exit. Run the final playbook.
        - `ansible-playbook -i inventory playbook.yml` Explain Code
        - Success! The task now reports `ok` because its return code was 1, which does not meet our new failure condition (`rc > 1`). The playbook completes successfully.
        - ```
...
TASK [Check for ERROR in status file (with failed_when)] ***********************
ok: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=0    unreachable=0    failed=0    ...
``` Explain Code
        - You have now learned how to use `changed_when` and `failed_when` to precisely define the success, changed, and failure states of your tasks, leading to more robust and intelligent automation.
        - ![](https://remnote-user-data.s3.amazonaws.com/UXSC72_R-GMlSJAUHH9jUIdLePfglHDKsOsxNFlRNETe78rIp_cF6ROg2PF6nPOVGM6MneuiEG-c0tKi8ZBtaAaUZl5LlZ-cbqDWj3E7G6XmbGIz0hgrh_gDBaYeGBWJ.webp)**Labby**
        - 
        - # **Deploy a Secure Web Server Using Task Control**
        - In this final step, you will combine all the concepts you've learned—loops, conditionals, handlers, and error handling—to build a single, robust playbook. The goal is to deploy the Apache web server (`httpd`), secure it with `mod_ssl`, generate a self-signed SSL certificate, and deploy a custom homepage. This practical exercise mirrors a real-world automation task.
        - First, let's set up the project directory for this capstone exercise.
        - ```
cd ~/project
mkdir control-review-lab
cd control-review-lab
``` Explain Code
        - As always, create an `inventory` file to define your target host.
        - `nano inventory` Explain Code
        - Add the `localhost` entry:
        - `localhost ansible_connection=local` Explain Code
        - Save and exit the editor (`Ctrl+X`, `Y`, `Enter`).
        - Next, we need a directory to store the files our playbook will deploy.
        - `mkdir files` Explain Code
        - Now, create a custom homepage, `index.html`, inside the `files` directory.
        - `nano files/index.html` Explain Code
        - Add the following HTML content. This will be the page served by our secure web server.
        - ```
<h1>Secure Web Server Deployed by Ansible!</h1>
<p>This page is served over HTTPS.</p>
``` Explain Code
        - Save and exit the editor.
        - Now it's time to build the main playbook, `deploy_secure_web.yml`. This playbook will be more complex than the previous ones, integrating multiple concepts.
        - `nano deploy_secure_web.yml` Explain Code
        - Enter the following complete playbook. Read the comments within the code to understand how each part contributes to the overall goal.
        - ```
---
- name: Deploy a Secure Apache Web Server
  hosts: localhost
  become: yes
  vars:
    packages_to_install:
      - httpd
      - mod_ssl
    ssl_cert_path: /etc/pki/tls/certs/localhost.crt
    ssl_key_path: /etc/pki/tls/private/localhost.key

  tasks:
    - name: Stop nginx to free port 80
      ansible.builtin.systemd:
        name: nginx
        state: stopped
      ignore_errors: yes

    - name: Install httpd and mod_ssl packages
      ansible.builtin.dnf:
        name: "{{ packages_to_install }}"
        state: present

    - name: Generate self-signed SSL certificate if it does not exist
      ansible.builtin.command: >
        openssl req -new -nodes -x509
        -subj "/C=US/ST=None/L=None/O=LabEx/CN=localhost"
        -keyout {{ ssl_key_path }}
        -out {{ ssl_cert_path }}
      args:
        creates: "{{ ssl_cert_path }}"

    - name: Deploy custom index.html
      ansible.builtin.copy:
        src: files/index.html
        dest: /var/www/html/index.html
      notify: restart httpd

    - name: Start and enable httpd service
      ansible.builtin.systemd:
        name: httpd
        state: started
        enabled: yes

  handlers:
    - name: restart httpd
      ansible.builtin.systemd:
        name: httpd
        state: restarted
``` Explain Code
        - Let's break down what this playbook does:
            - `**vars**`: Defines variables for the packages to install and the paths for the SSL certificate and key, making the playbook easier to read and maintain.
            - **Stop Nginx Task**: Stops the nginx service from the previous lab step to free up port 80 for Apache. Uses `ignore_errors: yes` in case nginx is not running.
            - **Install Task**: Uses the `packages_to_install` variable to install both `httpd` and `mod_ssl`.
            - **Generate Certificate Task**: This is a key task. It uses the `openssl` command to create a self-signed certificate. The `args: { creates: ... }` directive makes this task **idempotent**. The command will only run if the certificate file (`/etc/pki/tls/certs/localhost.crt`) does not already exist.
            - **Deploy Homepage Task**: Copies your custom `index.html`. Crucially, it uses `notify: restart httpd` to trigger the handler if the file is changed.
            - **Start Service Task**: Uses the systemd module to start and enable the httpd service after all configuration is in place, ensuring it starts on boot.
            - **Handler**: The `restart httpd` handler performs a restart of Apache using systemd, which is only triggered when a configuration or content file changes.
        - Save and exit the editor. Now, execute your comprehensive playbook.
        - `ansible-playbook -i inventory deploy_secure_web.yml` Explain Code
        - On the first run, you should see several tasks reporting `changed`, including stopping nginx, package installation, certificate generation, file copy, and service start.
        - ```
...
TASK [Start and enable httpd service] ******************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=5    unreachable=0    failed=0    ...
``` Explain Code
        - Finally, verify that your secure web server is working. First test the HTTP version, then the HTTPS version with the `-k` flag to ignore warnings about the self-signed certificate.
        - `curl http://localhost` Explain Code
        - You should see the content of your custom homepage.
        - ```
<h1>Secure Web Server Deployed by Ansible!</h1>
<p>This page is served over HTTPS.</p>
``` Explain Code
        - You can also test the HTTPS version:
        - `curl -k https://localhost` Explain Code
        - If you run the playbook again, you will see that no tasks report `changed`, and the handler is not run, proving your playbook is idempotent.
        - Congratulations! You have successfully built a practical, robust Ansible playbook that combines loops, variables, idempotent command execution, and handlers to deploy a secure application.
        - ![](https://remnote-user-data.s3.amazonaws.com/WEk2r4xNU6mX2TAMD4chSXatM9PQSXacy1ta9Vsk4Qp8KV7At5uROlz7YtYOFhAI_KORSQ0Fl24U7wWpWM6c4KdpZSP3Jt7yud7AkswU7MelSam7GSF0ZGehBX6oNsDQ.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned to control Ansible playbook execution on a RHEL system. You started by setting up a basic project environment, including installing Ansible and creating an inventory file. You then explored fundamental control flow structures, using loops to efficiently repeat tasks with different inputs and conditionals with the `when` statement to run tasks only under specific circumstances. Building on this, you implemented handlers to create responsive automations, such as triggering a service restart only when its configuration file has been modified.
        - The lab also covered advanced techniques for managing playbook execution. You learned how to build more robust playbooks by using `block` and `rescue` clauses to handle task failures gracefully. Furthermore, you gained fine-grained control over task outcomes by using `changed_when` and `failed_when` to define custom success and failure conditions. Finally, you consolidated all these skills by applying them to a practical scenario: deploying a secure web server, demonstrating how to effectively combine loops, conditionals, handlers, and error handling in a real-world automation workflow.
    5. **Deploy and Manage Files on RHEL with Ansible**
        - Copy a Static File and Set Attributes with the `ansible.builtin.copy` Module
        - Modify File Content with `lineinfile` and `blockinfile`
        - Generate a Custom MOTD with the `ansible.builtin.template` Module
        - Deploy Supporting Files and Create a Symbolic Link with `copy` and `file`
        - Verify File State with `stat` and Fetch Logs with `fetch`
        - Clean Up Managed Host Files with the `file` Module
        - 
        - # **Introduction**
        - In this lab, you will learn the fundamental skills for deploying and managing files on a Red Hat Enterprise Linux (RHEL) system using Ansible. You will gain hands-on experience with some of the most common and powerful Ansible modules designed for file operations, moving from basic file deployment to more advanced content manipulation and state management.
        - You will begin by using the `ansible.builtin.copy` module to transfer a static file and set its attributes. Next, you will modify file content with `lineinfile` and `blockinfile`, and generate a custom MOTD using the `ansible.builtin.template` module. The lab also covers creating symbolic links, verifying file states with `stat`, retrieving logs with `fetch`, and cleaning up managed files, providing a comprehensive overview of Ansible's file management capabilities.
        - ![](https://remnote-user-data.s3.amazonaws.com/TTk7xzZoOcmFp3am7GoYKCzotJIN2ox9zSify2XCOL0Q4irsOJP64HJq4QymuFl52_FRUVS9BBAXHle_9jnOCnCU-UhQHk1ZTTUq-SzgPYFKAuCc6KBbewdCTOGEMTcQ.webp)**Labby** 
        - 
        - # **Copy a Static File and Set Attributes with the** `**ansible.builtin.copy**` **Module**
        - In this step, you will learn how to use one of the most fundamental Ansible modules: `ansible.builtin.copy`. This module is used to transfer files from your control node (the LabEx VM) to a specified location on your managed hosts. In our case, the managed host will be `localhost` itself. Beyond just copying, the `copy` module allows you to precisely control the file's attributes, such as its owner, group, and permission mode, which is essential for proper system configuration.
        - First, let's set up our project environment. All our work will be done inside the `~/project` directory.
            1. **Navigate to the project directory and create a subdirectory for our source files.** This is a common practice to keep your project organized.
                - Install the `ansible-core` package.
                - `sudo dnf install -y ansible-core` Explain Code
                - Then, navigate to the project directory and create a subdirectory for our source files.
                - ```
cd ~/project
mkdir files
``` Explain Code
            2. **Next, create a simple text file that we will copy.** We'll use a `cat` command with a "here document" to create the file `info.txt` inside the `files` directory.
                - ```
cat << EOF > ~/project/files/info.txt
This file was deployed by Ansible.
It contains important system information.
EOF
``` Explain Code
            3. **Now, create an Ansible inventory file.** The inventory tells Ansible which hosts to manage. For this lab, we will manage the local machine. Create a file named `inventory.ini`.
                - ```
cat << EOF > ~/project/inventory.ini
localhost ansible_connection=local
EOF
``` Explain Code
                - In this inventory, `localhost` is the host we are targeting. The variable `ansible_connection=local` instructs Ansible to execute the tasks directly on the control node, without using SSH.
            4. **Create your first Ansible playbook.** This playbook will contain the instructions to copy the file. Use `nano` or `cat` to create a file named `copy_file.yml`.
                - `nano ~/project/copy_file.yml` Explain Code
                - Add the following content to the file. This playbook defines one task: to copy `info.txt` to the `/tmp/` directory and set its attributes.
                - ```
---
- name: Deploy a static file to localhost
  hosts: localhost
  tasks:
    - name: Copy info.txt and set attributes
      ansible.builtin.copy:
        src: files/info.txt
        dest: /tmp/info.txt
        owner: labex
        group: labex
        mode: "0640"
``` Explain Code
                - Let's break down the parameters in the `copy` task:
                    - `src: files/info.txt`: The path to the source file on the control node, relative to the playbook's location.
                    - `dest: /tmp/info.txt`: The absolute path where the file will be placed on the managed host.
                    - `owner: labex`: Sets the file's owner to the `labex` user.
                    - `group: labex`: Sets the file's group to the `labex` group.
                    - `mode: '0640'`: Sets the file's permissions. `0640` means the owner can read/write, the group can read, and others have no permissions.
            5. **Execute the playbook** using the `ansible-playbook` command. The `-i` flag specifies our inventory file.
                - `ansible-playbook -i inventory.ini copy_file.yml` Explain Code
                - You should see output indicating the successful execution of the playbook, similar to this:
                - ```
PLAY [Deploy a static file to localhost] ***************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Copy info.txt and set attributes] ****************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            6. **Finally, verify that the file was copied correctly** and has the right attributes. Use the `ls -l` command to check the permissions, owner, and group.
                - `ls -l /tmp/info.txt` Explain Code
                - The output should show that `labex` is the owner and group, and the permissions are `-rw-r-----`.
                - `-rw-r----- 1 labex labex 72 Jul 10 14:30 /tmp/info.txt` Explain Code
                - You can also view the file's content to ensure it was copied completely.
                - `cat /tmp/info.txt` Explain Code
                - ```
This file was deployed by Ansible.
It contains important system information.
``` Explain Code
        - You have successfully used the `ansible.builtin.copy` module to deploy a file and configure its attributes on your local system.
        - ![](https://remnote-user-data.s3.amazonaws.com/I_aEERE_20UL2iJgnalx-GGoeGbo5i9M9GlcOlBs3-r_A2ANH6zOi9wFn9yiQ0JsSP2_lL262aOrd0TQbS-PlzOn5bqk_bgzIaKJ7tiJrAvfy0tTam2bbZpWprJYhLX-.webp)**Labby**
        - 
        - # **Modify File Content with** `**lineinfile**` **and** `**blockinfile**`
        - In this step, you will learn how to modify existing files on a managed host without replacing the entire file. Ansible provides powerful modules for this purpose: `ansible.builtin.lineinfile` for managing single lines and `ansible.builtin.blockinfile` for managing multi-line blocks of text. These are extremely useful for tasks like changing configuration settings or adding entries to log files.
        - We will continue working with the `info.txt` file you created in the previous step, which is located at `/tmp/info.txt`.
            1. **First, ensure you are in the project directory.**
                - `cd ~/project` Explain Code
            2. **Create a new playbook named** `**modify_file.yml**`. This playbook will contain two tasks: one to add a single line and another to add a block of text to our existing file.
                - `nano ~/project/modify_file.yml` Explain Code
            3. **Add the following content to your** `**modify_file.yml**` **playbook.** This playbook targets `localhost` and uses both `lineinfile` and `blockinfile` to append content to `/tmp/info.txt`.
                - ```
---
- name: Modify an existing file
  hosts: localhost
  tasks:
    - name: Add a single line of text to a file
      ansible.builtin.lineinfile:
        path: /tmp/info.txt
        line: This line was added by the lineinfile module.
        state: present

    - name: Add a block of text to an existing file
      ansible.builtin.blockinfile:
        path: /tmp/info.txt
        block: |
          # BEGIN ANSIBLE MANAGED BLOCK
          This block of text consists of two lines.
          They have been added by the blockinfile module.
          # END ANSIBLE MANAGED BLOCK
        state: present
``` Explain Code
                - Let's examine the modules used:
                    - `ansible.builtin.lineinfile`: This module ensures a specific line is present in a file. If the line already exists, Ansible does nothing, making the task idempotent.
                        - `path`: The file to modify.
                        - `line`: The line of text to ensure is in the file.
                        - `state: present`: This ensures the line exists. You could use `state: absent` to remove it.
                    - `ansible.builtin.blockinfile`: This module manages a block of text, surrounded by marker lines (e.g., `# BEGIN ANSIBLE MANAGED BLOCK`). This is ideal for managing configuration sections.
                        - `path`: The file to modify.
                        - `block`: The multi-line string to insert. The `|` is YAML syntax for a literal block, preserving newlines.
                        - `state: present`: Ensures the block exists.
            4. **Execute the playbook** using the `ansible-playbook` command and your `inventory.ini` file.
                - `ansible-playbook -i inventory.ini modify_file.yml` Explain Code
                - The output will show that both tasks made changes to the file.
                - ```
PLAY [Modify an existing file] *************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Add a single line of text to a file] *************************************
changed: [localhost]

TASK [Add a block of text to an existing file] *********************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            5. **Finally, verify the changes by viewing the content of** `**/tmp/info.txt**`.
                - `cat /tmp/info.txt` Explain Code
                - You should see the original content, followed by the new line and the new block of text.
                - ```
This file was deployed by Ansible.
It contains important system information.
This line was added by the lineinfile module.
# BEGIN ANSIBLE MANAGED BLOCK
This block of text consists of two lines.
They have been added by the blockinfile module.
# END ANSIBLE MANAGED BLOCK
``` Explain Code
                - If you run the playbook again, Ansible will report `ok=3` and `changed=0` because the content is already present, demonstrating the idempotent nature of these modules.
        - ![](https://remnote-user-data.s3.amazonaws.com/P6OI_fvtclX868l0XEBOUhOJi7YRa1imBeoY_LLYMuZKB10ZEPa2fXjln32ryJenut_gV5EmUeCOUYRiBo_7MgqoYWR6iivcdwRPX3-wn-14OtKuI3F1YA9UYv9ArMej.webp)**Labby**
        - 
        - # **Generate a Custom MOTD with the** `**ansible.builtin.template**` **Module**
        - In this step, you will advance from copying static files to generating dynamic files using the `ansible.builtin.template` module. This module leverages the Jinja2 templating engine to create files customized with variables and system information, known as "facts," that Ansible gathers from your managed hosts. We will create a dynamic Message of the Day (MOTD) that displays system-specific information.
            1. **First, ensure you are in the** `**~/project**` **directory and create a dedicated subdirectory for your templates.** It is a standard Ansible best practice to store Jinja2 templates in a `templates` directory.
                - ```
cd ~/project
mkdir templates
``` Explain Code
            2. **Next, create the Jinja2 template file.** This file, `motd.j2`, will contain the structure of our MOTD, with placeholders for dynamic data. The `.j2` extension is a common convention for Jinja2 templates.
                - `nano ~/project/templates/motd.j2` Explain Code
                - Add the following content to the file. Notice the `{{ ... }}` syntax, which denotes a placeholder for a variable or fact.
                - ```
#################################################################
#          Welcome to {{ ansible_facts['fqdn'] }}
#
# This is a {{ ansible_facts['distribution'] }} system.
# System managed by Ansible.
#
# For support, contact: {{ admin_email }}
#################################################################
``` Explain Code
                - In this template:
                    - `{{ ansible_facts['fqdn'] }}` will be replaced by the host's Fully Qualified Domain Name.
                    - `{{ ansible_facts['distribution'] }}` will be replaced by the Linux distribution name (e.g., RedHat).
                    - `{{ admin_email }}` is a custom variable that we will define in our playbook.
            3. **Now, create a new playbook named** `**template_motd.yml**`. This playbook will use the template to generate `/etc/motd`.
                - `nano ~/project/template_motd.yml` Explain Code
                - Add the following content. This playbook requires elevated privileges (`become: true`) to write to the `/etc` directory. It also defines the custom `admin_email` variable.
                - ```
---
- name: Deploy a custom MOTD from a template
  hosts: localhost
  become: true
  vars:
    admin_email: admin@labex.io
  tasks:
    - name: Generate /etc/motd from template
      ansible.builtin.template:
        src: templates/motd.j2
        dest: /etc/motd
        owner: root
        group: root
        mode: "0644"
``` Explain Code
                - Key parameters in this playbook:
                    - `become: true`: This tells Ansible to use `sudo` to execute the task, which is necessary for writing to `/etc/motd`.
                    - `vars`: This section is where we define custom variables, like `admin_email`.
                    - `ansible.builtin.template`: The module that processes the Jinja2 template. `src` points to our `.j2` file, and `dest` is the target file on the managed host.
            4. **Execute the playbook.**
                - `ansible-playbook -i inventory.ini template_motd.yml` Explain Code
                - The output should confirm the task was successful.
                - ```
PLAY [Deploy a custom MOTD from a template] ************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Generate /etc/motd from template] ****************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            5. **Verify the result.** Check the content of the newly generated `/etc/motd` file.
                - `cat /etc/motd` Explain Code
                - You will see the rendered output, with the Jinja2 placeholders replaced by actual system facts and the custom variable you defined. The `fqdn` will match your lab environment's hostname.
                - ```
#################################################################
#          Welcome to host.labex.io
#
# This is a RedHat system.
# System managed by Ansible.
#
# For support, contact: admin@labex.io
#################################################################
``` Explain Code
        - You have now successfully used a template to create a customized file, a core skill in infrastructure automation.
        - ![](https://remnote-user-data.s3.amazonaws.com/5A7Sgz8s2uvypnWxo0XaL_4ijjItnDlQaAZFPRnt6Rwrjr3iHSiCYSW884ypomYeUy4vOkSHoqDlzp2GxhF_k0VyyqFHRLQnOaspFjtcm4ixyrP5tH5i4Ll3IOUXR7qd.webp)**Labby**
        - 
        - # **Deploy Supporting Files and Create a Symbolic Link with** `**copy**` **and** `**file**`
        - In this step, you will combine your knowledge of the `copy` module with a new, versatile module: `ansible.builtin.file`. While `copy` is for transferring content, `file` is used to manage the state of files, directories, and symbolic links on the managed host. You will use it to create directories, set permissions, and, most importantly for this exercise, create symbolic links.
        - Our scenario is to configure the pre-login messages displayed by the system. In many Linux systems, `/etc/issue` is shown to local terminal users, and `/etc/issue.net` is shown to remote users (like over SSH). We will deploy a single `issue` file and then create a symbolic link so that `/etc/issue.net` points to `/etc/issue`, ensuring they always display the same message.
            1. **First, ensure you are in the** `**~/project**` **directory and create the source file for our issue message.** We will place this file in the `files` subdirectory you created earlier.
                - ```
cd ~/project
cat << EOF > ~/project/files/issue
Authorized access only.
All connections are logged and monitored.
EOF
``` Explain Code
            2. **Create a new playbook named** `**deploy_issue.yml**`. This playbook will contain two tasks: one to copy the `issue` file and another to create the symbolic link.
                - `nano ~/project/deploy_issue.yml` Explain Code
            3. **Add the following content to your** `**deploy_issue.yml**` **playbook.** This playbook requires elevated privileges (`become: true`) to manage files in the `/etc/` directory.
                - ```
---
- name: Configure system issue files
  hosts: localhost
  become: true
  tasks:
    - name: Copy custom /etc/issue file
      ansible.builtin.copy:
        src: files/issue
        dest: /etc/issue
        owner: root
        group: root
        mode: "0644"

    - name: Ensure /etc/issue.net is a symlink to /etc/issue
      ansible.builtin.file:
        src: /etc/issue
        dest: /etc/issue.net
        state: link
        force: yes
``` Explain Code
                - Let's analyze the new `ansible.builtin.file` task:
                    - `src: /etc/issue`: When `state` is `link`, `src` specifies the file that the symbolic link should point to.
                    - `dest: /etc/issue.net`: This is the path where the symbolic link itself will be created.
                    - `state: link`: This crucial parameter tells the `file` module to create a symbolic link, not a regular file or directory.
                    - `force: yes`: This is a useful option that ensures idempotency. If `/etc/issue.net` already exists as a regular file, Ansible will remove it and create the link. Without `force: yes`, the playbook would fail in that situation.
            4. **Execute the playbook.**
                - `ansible-playbook -i inventory.ini deploy_issue.yml` Explain Code
                - The output will show both tasks successfully making changes.
                - ```
PLAY [Configure system issue files] ********************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Copy custom /etc/issue file] *********************************************
changed: [localhost]

TASK [Ensure /etc/issue.net is a symlink to /etc/issue] ************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            5. **Verify the result using the** `**ls -l**` **command.** This command provides a detailed listing that clearly shows symbolic links.
                - `ls -l /etc/issue /etc/issue.net` Explain Code
                - The output should show that `/etc/issue` is a regular file and `/etc/issue.net` is a symbolic link pointing to it. The `l` at the beginning of the permissions for `/etc/issue.net` indicates it's a link.
                - ```
-rw-r--r--. 1 root root 65 Jul 10 15:00 /etc/issue
lrwxrwxrwx. 1 root root 10 Jul 10 15:00 /etc/issue.net -> /etc/issue
``` Explain Code
        - You have now successfully deployed a configuration file and used the `ansible.builtin.file` module to create a symbolic link, a common and powerful pattern for managing system configurations.
        - ![](https://remnote-user-data.s3.amazonaws.com/BB-Y8UsU7AofM9pB6W9sa1eMalO7n-btbWL4S-rIWvonQjSJAjg5lL2a_FF8L3hAQqMclvM_4oruYn1VSECWIYKl2DD1K0FOHNvlu7WgDdw0ZSk0ovjFJbaSuUbb5Etb.webp)**Labby**
        - 
        - # **Verify File State with** `**stat**` **and Fetch Logs with** `**fetch**`
        - In this step, you will learn about two important data-gathering modules: `ansible.builtin.stat` and `ansible.builtin.fetch`. The `stat` module is used to check the status of a file or directory on a managed host—for example, to see if it exists, what its permissions are, or when it was last modified. It doesn't change anything, making it perfect for checks and conditional logic. The `fetch` module does the opposite of `copy`: it retrieves files   *from*   the managed host and saves them to your control node, which is ideal for backing up configurations or collecting log files for analysis.
        - We will create a playbook that first checks for the existence of the `/etc/motd` file you created earlier, and then fetches the DNF package manager log file (`/var/log/dnf.log`) to a local directory on your LabEx VM.
            1. **First, ensure you are in the** `**~/project**` **directory and create a new subdirectory to store the files you will fetch.**
                - ```
cd ~/project
mkdir fetched_logs
``` Explain Code
            2. **Create a new playbook named** `**check_and_fetch.yml**`. This playbook will contain the tasks to check the file and retrieve the log.
                - `nano ~/project/check_and_fetch.yml` Explain Code
            3. **Add the following content to your** `**check_and_fetch.yml**` **playbook.** This playbook uses `stat` to get file details, `register` to store those details in a variable, `debug` to display the variable, and `fetch` to retrieve the log file.
                - ```
---
- name: Check file status and fetch logs
  hosts: localhost
  become: true
  tasks:
    - name: Check if /etc/motd exists
      ansible.builtin.stat:
        path: /etc/motd
      register: motd_status

    - name: Display stat results
      ansible.builtin.debug:
        var: motd_status.stat

    - name: Fetch the dnf log file from managed host
      ansible.builtin.fetch:
        src: /var/log/dnf.log
        dest: fetched_logs/
        flat: yes
``` Explain Code
                - Let's break down the key concepts:
                    - `register: motd_status`: This is a crucial Ansible feature. It takes the entire output of a task and saves it into a new variable named `motd_status`.
                    - `ansible.builtin.debug`: This module is used to print values during a playbook run. Here, we print the `stat` object within our registered variable (`motd_status.stat`) to see the file's properties.
                    - `ansible.builtin.fetch`: This module retrieves a file from the managed host.
                        - `src`: The path of the file to retrieve from the managed host.
                        - `dest`: The directory on the control node (your LabEx VM) where the file will be saved.
                        - `flat: yes`: By default, `fetch` creates a subdirectory structure matching the host and source path. `flat: yes` simplifies this by copying the file directly into the `dest` directory without any extra subdirectories.
            4. **Execute the playbook.** Since we are reading a system log file, `become: true` is used to gain the necessary permissions.
                - `ansible-playbook -i inventory.ini check_and_fetch.yml` Explain Code
                - The output will show the results of the `stat` check in the debug task, followed by the `fetch` task.
                - ```
PLAY [Check file status and fetch logs] ****************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Check if /etc/motd exists] ***********************************************
ok: [localhost]

TASK [Display stat results] ****************************************************
ok: [localhost] => {
    "motd_status.stat": {
        "exists": true,
        "gid": 0,
        "isreg": true,
        "mode": "0644",
        "path": "/etc/motd",
        ...
    }
}

TASK [Fetch the dnf log file from managed host] ********************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=4    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            5. **Verify that the log file was fetched successfully.** List the contents of the `fetched_logs` directory.
                - `ls -l ~/project/fetched_logs/` Explain Code
                - You should see the `dnf.log` file, now stored locally on your control node.
                - ```
total 4
-rw-r--r--. 1 labex labex 1234 Jul 10 15:30 dnf.log
``` Explain Code
        - You have now learned how to inspect file properties without making changes and how to retrieve important files from your managed systems back to your control node.
        - ![](https://remnote-user-data.s3.amazonaws.com/UuG5qNDqI6mwwceJ2MIMvb6ggNBCTgGTs4f7ZEfUZ9OOY5uPoXoO8l4qwrgjf71gjvK6dmyWdOzRy2kDFCigCcH-jQsGeY-RcA4gwdlI_oJlcx156XjZ6zcR-hGG0Kdp.webp)**Labby**
        - 
        - # **Clean Up Managed Host Files with the** `**file**` **Module**
        - In this final step, you will learn how to use the `ansible.builtin.file` module to ensure files and directories are   *not*   present on a system. A critical part of configuration management is not just creating and modifying resources, but also cleaning them up. By setting the `state` parameter to `absent`, you can instruct Ansible to remove files, symbolic links, or even entire directories.
        - To conclude this lab, we will write a single "cleanup" playbook that removes all the artifacts we created in the previous steps: `/tmp/info.txt`, `/etc/motd`, `/etc/issue`, and the `/etc/issue.net` symbolic link.
            1. **First, ensure you are in the** `**~/project**` **directory.**
                - `cd ~/project` Explain Code
            2. **Create a new playbook named** `**cleanup.yml**`. This playbook will contain all the tasks needed to revert our changes.
                - `nano ~/project/cleanup.yml` Explain Code
            3. **Add the following content to your** `**cleanup.yml**` **playbook.** This playbook uses a list of tasks, each targeting one of the files we created. Note that `become: true` is set at the play level, so all tasks will run with elevated privileges.
                - ```
---
- name: Clean up managed files from the system
  hosts: localhost
  become: true
  tasks:
    - name: Remove the temporary info file
      ansible.builtin.file:
        path: /tmp/info.txt
        state: absent

    - name: Remove the custom MOTD file
      ansible.builtin.file:
        path: /etc/motd
        state: absent

    - name: Remove the custom issue file
      ansible.builtin.file:
        path: /etc/issue
        state: absent

    - name: Remove the issue.net symbolic link
      ansible.builtin.file:
        path: /etc/issue.net
        state: absent
``` Explain Code
                - The key to this playbook is the `state: absent` parameter in each task. This tells the `file` module to ensure the item at the specified `path` does not exist. If it finds the file, it will remove it. If the file is already gone, it will do nothing, maintaining idempotency.
            4. **Execute the cleanup playbook.**
                - `ansible-playbook -i inventory.ini cleanup.yml` Explain Code
                - The output will show that each task successfully made a change by removing a file.
                - ```
PLAY [Clean up managed files from the system] **********************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Remove the temporary info file] ******************************************
changed: [localhost]

TASK [Remove the custom MOTD file] *********************************************
changed: [localhost]

TASK [Remove the custom issue file] ********************************************
changed: [localhost]

TASK [Remove the issue.net symbolic link] **************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=5    changed=4    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            5. **Verify that the files have been removed.** You can use the `ls` command to check for their existence. The command will report that it cannot access them because they are gone.
                - `ls /tmp/info.txt /etc/motd /etc/issue /etc/issue.net` Explain Code
                - The expected output is a series of errors, confirming the cleanup was successful.
                - ```
ls: cannot access '/tmp/info.txt': No such file or directory
ls: cannot access '/etc/motd': No such file or directory
ls: cannot access '/etc/issue': No such file or directory
ls: cannot access '/etc/issue.net': No such file or directory
``` Explain Code
        - You have now successfully used Ansible to remove files and clean up a system, completing the full lifecycle of file management from creation to deletion.
        - ![](https://remnote-user-data.s3.amazonaws.com/I90LN55AK_0tsV6y07bKhELfXoSUnwsecyMI3zWSOkaRHleQLrAsnyeLG7wYoa4Nxu8-iqYGDVA9a60DDu4AaMYcqT63UOykxxtFxwCaFO9I_2sYBm4GLH1ARJM56bzh.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned the fundamentals of file management on RHEL systems using Ansible. You started by using the `ansible.builtin.copy` module to transfer a static file to a managed host while setting specific ownership and permissions. You then explored how to modify existing files by ensuring a specific line is present with `lineinfile` and managing multi-line blocks of text with `blockinfile`. A key skill covered was generating dynamic file content using the `ansible.builtin.template` module and Jinja2 syntax to create a customized Message of the Day (MOTD) populated with system facts.
        - Furthermore, you practiced deploying supporting files and creating symbolic links using the `ansible.builtin.file` module. To ensure your deployments were successful, you used the `stat` module to verify the state and attributes of files and the `fetch` module to retrieve files, such as logs, from the managed host back to the control node. Finally, you learned how to perform cleanup operations by using the `file` module with `state: absent` to remove the files and directories created throughout the lab, ensuring a clean state on the managed host.
    6. **Structuring Complex Ansible Playbooks on RHEL**
        - Selecting Hosts with Basic and Wildcard Patterns
        - Refining Host Selection with Exclusions and Logical Operators
        - Modularizing a Play with `include_tasks` and `import_tasks`
        - Composing a Workflow with `import_playbook`
        - Executing and Verifying the Complete Modular Playbook
        - 
        - # **Introduction**
        - In this lab, you will learn essential techniques for structuring complex Ansible playbooks on RHEL to create more manageable, scalable, and reusable automation. You will progress from fundamental concepts to advanced organizational strategies, focusing on how to precisely control which hosts your automation runs on and how to break down large playbooks into logical, modular components.
        - You will begin by mastering host selection, using basic group names, wildcards, exclusions, and logical operators to target specific nodes within your inventory. Next, you will explore modularization by refactoring tasks into separate files using `include_tasks` and `import_tasks`. Finally, you will learn to compose a complete, multi-playbook workflow with `import_playbook`, culminating in the execution and verification of your fully structured and modularized Ansible project.
        - ![](https://remnote-user-data.s3.amazonaws.com/5cpP5vkYB6OwcscbytYDHCjwfu4xAJK9ZCo4k5mUi2w63HSflDS9DNM6Xat6Car5AICGlwyoRyUPC1g1VoutBty_HPV4W5ng0OM00PJytgqpBdNoOaciy8cdLTCK08qE.webp)**Labby** 
        - 
        - # **Selecting Hosts with Basic and Wildcard Patterns**
        - In this step, you will learn the fundamentals of targeting specific hosts in your Ansible automation. The core of this is the Ansible inventory file, which lists the servers you manage, and the `hosts` directive within a playbook, which specifies which of those servers a set of tasks should run against. We will start by installing Ansible, creating a basic inventory and playbook, and then exploring how to select hosts using group names and wildcard patterns.
        - First, let's ensure Ansible is installed in your environment. Ansible is not installed by default, so you need to install it using the DNF package manager. The `ansible-core` package provides the essential Ansible command-line tools, including `ansible-playbook`. Run the following command:
        - `sudo dnf install -y ansible-core` Explain Code
        - You should see output similar to this:
        - ```
...
Installed:
  ansible-core-2.16.x-x.el9.x86_64
  ...
Complete!
``` Explain Code
        - Next, let's create a dedicated directory for this exercise to keep our files organized. All subsequent actions in this step will take place within this new directory:
        - ```
mkdir -p ~/project/ansible_patterns
cd ~/project/ansible_patterns
``` Explain Code
        - Now, create an inventory file. An inventory is a text file that defines the hosts and groups of hosts upon which Ansible commands, modules, and tasks operate. We will use the INI format for its simplicity.
        - Use the `nano` editor to create a file named `inventory`:
        - `nano inventory` Explain Code
        - Add the following content to the `inventory` file. This defines two groups, `webservers` and `dbservers`, each containing two hosts:
        - ```
[webservers]
web1.example.com
web2.example.com

[dbservers]
db1.lab.net
db2.lab.net
``` Explain Code
        - Save the file and exit `nano` by pressing `Ctrl+X`, then `Y`, and `Enter`.
        - With our inventory ready, let's create a simple playbook. This playbook will use the `ansible.builtin.debug` module to print a message, confirming which host the task is running on. This is a great way to test host patterns without making any actual changes to the system.
        - Create a new file named `playbook.yml`:
        - `nano playbook.yml` Explain Code
        - Add the following YAML content. Initially, it targets all hosts in the `webservers` group:
        - ```
---
- name: Test Host Patterns
  hosts: webservers
  gather_facts: false
  tasks:
    - name: Display the inventory hostname
      ansible.builtin.debug:
        msg: "This task is running on {{ inventory_hostname }}"
``` Explain Code
        - Save and exit the editor. Now, run the playbook using `ansible-playbook`. The `-i` flag specifies our custom inventory file:
        - `ansible-playbook playbook.yml -i inventory` Explain Code
        - The output should look like this:
        - ```
PLAY [Test Host Patterns] ******************************************************

TASK [Display the inventory hostname] ******************************************
ok: [web1.example.com] => {
    "msg": "This task is running on web1.example.com"
}
ok: [web2.example.com] => {
    "msg": "This task is running on web2.example.com"
}

PLAY RECAP *********************************************************************
web1.example.com           : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web2.example.com           : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - As you can see, only the hosts from the `webservers` group were targeted. Now, let's modify the playbook to use a wildcard (`*`). Wildcards allow for more flexible pattern matching.
        - Edit `playbook.yml` and change the `hosts` line to `hosts: "*.lab.net"`. Remember to enclose patterns containing wildcards in quotes:
        - ```
---
- name: Test Host Patterns
  hosts: "*.lab.net"
  gather_facts: false
  tasks:
    - name: Display the inventory hostname
      ansible.builtin.debug:
        msg: "This task is running on {{ inventory_hostname }}"
``` Explain Code
        - Run the playbook again:
        - `ansible-playbook playbook.yml -i inventory` Explain Code
        - You should see output similar to this:
        - ```
PLAY [Test Host Patterns] ******************************************************

TASK [Display the inventory hostname] ******************************************
ok: [db1.lab.net] => {
    "msg": "This task is running on db1.lab.net"
}
ok: [db2.lab.net] => {
    "msg": "This task is running on db2.lab.net"
}

PLAY RECAP *********************************************************************
db1.lab.net                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db2.lab.net                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - This time, the play ran only on hosts whose names end with `.lab.net`. Finally, let's use the special keyword `all` to target every host defined in the inventory.
        - Edit `playbook.yml` one last time and change the `hosts` line to `hosts: all`:
        - ```
---
- name: Test Host Patterns
  hosts: all
  gather_facts: false
  tasks:
    - name: Display the inventory hostname
      ansible.builtin.debug:
        msg: "This task is running on {{ inventory_hostname }}"
``` Explain Code
        - Run the playbook to see the result:
        - `ansible-playbook playbook.yml -i inventory` Explain Code
        - The output will show all hosts being targeted:
        - ```
PLAY [Test Host Patterns] ******************************************************

TASK [Display the inventory hostname] ******************************************
ok: [web1.example.com] => {
    "msg": "This task is running on web1.example.com"
}
ok: [web2.example.com] => {
    "msg": "This task is running on web2.example.com"
}
ok: [db1.lab.net] => {
    "msg": "This task is running on db1.lab.net"
}
ok: [db2.lab.net] => {
    "msg": "This task is running on db2.lab.net"
}

PLAY RECAP *********************************************************************
db1.lab.net                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db2.lab.net                : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web1.example.com           : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web2.example.com           : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - The playbook now runs on all four hosts from your inventory, demonstrating the power of the `all` pattern.
        - ![](https://remnote-user-data.s3.amazonaws.com/of5zmQm1vopGySmx7bW4Q3EoN32hsz0P65pe9kHh8n75yr9HZl-YwAlaX6gV6I18YFNwU_GG3bxPfZmWHZCeqRZnBgkUlpMmc2QvM2veKxTA7S40cMboXDuJ3LKoKbWO.webp)**Labby**
        - 
        - # **Refining Host Selection with Exclusions and Logical Operators**
        - In this step, you will advance your host selection skills by learning how to use exclusions and logical operators. These features allow for highly specific targeting, which is essential when managing complex environments. You will learn to exclude hosts using the `!` (NOT) operator and combine groups using the `&` (AND) operator. We will continue working with the `inventory` and `playbook.yml` files from the previous step.
        - First, ensure you are in the correct working directory:
        - `cd ~/project/ansible_patterns` Explain Code
        - To effectively demonstrate logical operators, we need to create some overlap in our host groups. Let's edit the `inventory` file to add a new group called `production` that contains one web server and one database server:
        - `nano inventory` Explain Code
        - Add the `[production]` group and its members to the end of the file:
        - ```
[webservers]
web1.example.com
web2.example.com

[dbservers]
db1.lab.net
db2.lab.net

[production]
web1.example.com
db1.lab.net
``` Explain Code
        - Save the file and exit `nano` by pressing `Ctrl+X`, then `Y`, and `Enter`.
        - Now, let's practice exclusion. The `!` operator, which means NOT, allows you to exclude a host or group from a selection. Modify your `playbook.yml` to target all hosts   *except*   those in the `dbservers` group:
        - `nano playbook.yml` Explain Code
        - Update the `hosts` line as shown below. The pattern `all,!dbservers` selects every host and then removes any that are in the `dbservers` group:
        - ```
---
- name: Test Host Patterns
  hosts: all,!dbservers
  gather_facts: false
  tasks:
    - name: Display the inventory hostname
      ansible.builtin.debug:
        msg: "This task is running on {{ inventory_hostname }}"
``` Explain Code
        - Save and exit the editor, then run the playbook:
        - `ansible-playbook playbook.yml -i inventory` Explain Code
        - You should see only the web servers being targeted:
        - ```
PLAY [Test Host Patterns] ******************************************************

TASK [Display the inventory hostname] ******************************************
ok: [web1.example.com] => {
    "msg": "This task is running on web1.example.com"
}
ok: [web2.example.com] => {
    "msg": "This task is running on web2.example.com"
}

PLAY RECAP *********************************************************************
web1.example.com           : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web2.example.com           : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - As expected, only the hosts from the `webservers` group were targeted.
        - Next, let's explore the logical AND operator. The `&` operator selects only the hosts that exist in   *both*   specified groups (an intersection). Let's modify the playbook to target hosts that are in the `webservers` group AND also in the `production` group:
        - `nano playbook.yml` Explain Code
        - Change the `hosts` line to `webservers,&production`:
        - ```
---
- name: Test Host Patterns
  hosts: webservers,&production
  gather_facts: false
  tasks:
    - name: Display the inventory hostname
      ansible.builtin.debug:
        msg: "This task is running on {{ inventory_hostname }}"
``` Explain Code
        - Save and run the playbook:
        - `ansible-playbook playbook.yml -i inventory` Explain Code
        - This time, only the intersection of both groups will be targeted:
        - ```
PLAY [Test Host Patterns] ******************************************************

TASK [Display the inventory hostname] ******************************************
ok: [web1.example.com] => {
    "msg": "This task is running on web1.example.com"
}

PLAY RECAP *********************************************************************
web1.example.com           : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - The output correctly shows that only `web1.example.com` was targeted, as it is the only host that is a member of both the `webservers` and `production` groups. These operators give you precise control over which hosts your automation affects.
        - ![](https://remnote-user-data.s3.amazonaws.com/AqWeruEsCS-I5heWA_YwKSXCngl_PW0vbMV8378BoPsIRI4Y7vLeOxxTYksAoTr9LUoZ_eshAwF7nBGELc249zqAQVB1oxUFS4NYmecVJBYTmdZ6IKMs6DKpxP624lX9.webp)**Labby**
        - 
        - # **Modularizing a Play with** `**include_tasks**` **and** `**import_tasks**`
        - In this step, you will learn how to structure larger Ansible projects by breaking them down into smaller, reusable files. As playbooks grow, keeping all tasks in a single file becomes difficult to manage. Ansible provides two main directives for this: `import_tasks` and `include_tasks`. Both allow you to pull in tasks from another file.
            - `import_tasks` is **static**. It is processed when the playbook is first parsed by Ansible. This is best for unconditional, structural parts of your play.
            - `include_tasks` is **dynamic**. It is processed during the execution of the play. This makes it suitable for use with loops and conditionals.
        - We will now refactor our playbook to use both. First, ensure you are in the project directory:
        - `cd ~/project/ansible_patterns` Explain Code
        - Before we proceed, let's update the inventory file to make the hosts point to localhost for this lab environment. This will allow the playbook to run successfully:
        - `nano inventory` Explain Code
        - Replace the content with the following configuration that maps the example hosts to localhost:
        - ```
[webservers]
web1.example.com ansible_host=localhost ansible_connection=local
web2.example.com ansible_host=localhost ansible_connection=local

[dbservers]
db1.lab.net ansible_host=localhost ansible_connection=local
db2.lab.net ansible_host=localhost ansible_connection=local
``` Explain Code
        - Save and exit the editor. This configuration uses `ansible_host=localhost` to redirect connections to the local machine and `ansible_connection=local` to avoid SSH connection attempts.
        - A common practice is to store reusable task files in a dedicated subdirectory. Let's create one named `tasks`:
        - `mkdir tasks` Explain Code
        - Now, let's create a file for common setup tasks that might apply to many servers. We'll place a task to install the `httpd` web server package here:
        - `nano tasks/web_setup.yml` Explain Code
        - Add the following content. Note that this file is just a list of tasks; it does not contain a full play structure (like `hosts:` or `name:`):
        - ```
- name: Install the httpd package
  ansible.builtin.dnf:
    name: httpd
    state: present
  become: true
``` Explain Code
        - Save and exit `nano`. Next, create a second task file for a simple verification step:
        - `nano tasks/verify_config.yml` Explain Code
        - Add the following debug task to this file:
        - ```
- name: Display a verification message
  ansible.builtin.debug:
    msg: "Configuration tasks applied to {{ inventory_hostname }}"
``` Explain Code
        - Save and exit the editor. Now, let's modify the main `playbook.yml` to use these new task files. We will use `import_tasks` for the static setup and `include_tasks` for the dynamic verification message:
        - `nano playbook.yml` Explain Code
        - Replace the entire content of `playbook.yml` with the following. This playbook now targets the `webservers` group and uses the modular task files:
        - ```
---
- name: Configure Web Servers
  hosts: webservers
  gather_facts: false
  tasks:
    - name: Import web server setup tasks
      import_tasks: tasks/web_setup.yml

    - name: Include verification tasks
      include_tasks: tasks/verify_config.yml
``` Explain Code
        - Save the file and run the playbook:
        - `ansible-playbook playbook.yml -i inventory` Explain Code
        - You should see the modular tasks being executed:
        - ```
PLAY [Configure Web Servers] ***************************************************

TASK [Import web server setup tasks] *******************************************
imported: /home/labex/project/ansible_patterns/tasks/web_setup.yml

TASK [Install the httpd package] ***********************************************
changed: [web1.example.com]
changed: [web2.example.com]

TASK [Include verification tasks] **********************************************
included: /home/labex/project/ansible_patterns/tasks/verify_config.yml for web1.example.com, web2.example.com

TASK [Display a verification message] ******************************************
ok: [web1.example.com] => {
    "msg": "Configuration tasks applied to web1.example.com"
}
ok: [web2.example.com] => {
    "msg": "Configuration tasks applied to web2.example.com"
}

PLAY RECAP *********************************************************************
web1.example.com           : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web2.example.com           : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - Observe how the output clearly indicates when tasks are being imported and included from their respective files. This modular approach makes your automation cleaner and easier to maintain.
        - ![](https://remnote-user-data.s3.amazonaws.com/jGa3TErgnO8qyG8QSsxcCPxNTpjpMzX4eet8Jc1XkDgWlFhtSN-OLhK9M0cCTq4gksw_TRSOdJilt30ZTqHyDKrgaa5988JeHjGN5PeFqm1kW6h6savfg0QMP8OHYbte.webp)**Labby**
        - 
        - # **Composing a Workflow with** `**import_playbook**`
        - In this step, you will learn to orchestrate entire playbooks to form a complex workflow using `import_playbook`. While `import_tasks` and `include_tasks` are for reusing lists of tasks within a single play, `import_playbook` operates at a higher level. It allows you to create a master playbook that executes other, self-contained playbooks in a specific order. This is the standard way to manage large-scale automation, such as provisioning an entire application stack.
        - First, let's ensure we are in the correct directory and organize our project for this new structure:
        - `cd ~/project/ansible_patterns` Explain Code
        - It is a best practice to store individual, component playbooks in a dedicated subdirectory. Let's create a directory named `playbooks`:
        - `mkdir playbooks` Explain Code
        - Now, move the playbook we created in the last step, which configures web servers, into this new directory. Renaming it to be more descriptive is also a good idea:
        - `mv playbook.yml playbooks/web_configure.yml` Explain Code
        - However, since we moved the playbook to a subdirectory, we need to update the relative paths to the task files. The task files are still in the `tasks/` directory relative to the main project directory, so we need to adjust the paths:
        - `nano playbooks/web_configure.yml` Explain Code
        - Update the paths in the playbook to use `../tasks/` instead of `tasks/`:
        - ```
---
- name: Configure Web Servers
  hosts: webservers
  gather_facts: false
  tasks:
    - name: Import web server setup tasks
      import_tasks: ../tasks/web_setup.yml

    - name: Include verification tasks
      include_tasks: ../tasks/verify_config.yml
``` Explain Code
        - Save and exit the editor.
        - Let's test the corrected playbook to ensure the paths are working correctly:
        - `ansible-playbook playbooks/web_configure.yml -i inventory` Explain Code
        - You should see the playbook execute successfully with the corrected paths.
        - Next, create a new, separate playbook for configuring your database servers. This playbook will target the `dbservers` group and install the `mariadb` package:
        - `nano playbooks/db_setup.yml` Explain Code
        - Add the following content to the file. This is a complete, standalone play:
        - ```
---
- name: Configure Database Servers
  hosts: dbservers
  gather_facts: false
  tasks:
    - name: Install mariadb package
      ansible.builtin.dnf:
        name: mariadb
        state: present
      become: true

    - name: Display a confirmation message
      ansible.builtin.debug:
        msg: "Database server {{ inventory_hostname }} configured."
``` Explain Code
        - Save and exit the editor. Now you have two component playbooks: one for web servers and one for database servers.
        - Finally, create a top-level "main" playbook. This file will not contain any hosts or tasks itself. Its only job is to import the other playbooks in the correct order to define the overall workflow:
        - `nano main.yml` Explain Code
        - Add the following content. This creates a workflow that first configures the web servers and then configures the database servers:
        - ```
---
- name: Import the web server configuration play
  import_playbook: playbooks/web_configure.yml

- name: Import the database server configuration play
  import_playbook: playbooks/db_setup.yml
``` Explain Code
        - Save and exit `nano`. You are now ready to execute your entire workflow by running the `main.yml` playbook:
        - `ansible-playbook main.yml -i inventory` Explain Code
        - The output will show both playbooks being executed in sequence:
        - ```
PLAY [Configure Web Servers] ***************************************************

TASK [Import web server setup tasks] *******************************************
imported: /home/labex/project/ansible_patterns/playbooks/../tasks/web_setup.yml

TASK [Install the httpd package] ***********************************************
ok: [web1.example.com]
ok: [web2.example.com]

TASK [Include verification tasks] **********************************************
included: /home/labex/project/ansible_patterns/playbooks/../tasks/verify_config.yml for web1.example.com, web2.example.com

TASK [Display a verification message] ******************************************
ok: [web1.example.com] => {
    "msg": "Configuration tasks applied to web1.example.com"
}
ok: [web2.example.com] => {
    "msg": "Configuration tasks applied to web2.example.com"
}

PLAY [Configure Database Servers] **********************************************

TASK [Install mariadb package] *************************************************
changed: [db1.lab.net]
changed: [db2.lab.net]

TASK [Display a confirmation message] ******************************************
ok: [db1.lab.net] => {
    "msg": "Database server db1.lab.net configured."
}
ok: [db2.lab.net] => {
    "msg": "Database server db2.lab.net configured."
}

PLAY RECAP *********************************************************************
db1.lab.net                : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
db2.lab.net                : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web1.example.com           : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
web2.example.com           : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - The output clearly shows two separate plays being executed in sequence, demonstrating how `import_playbook` effectively composes a larger workflow from smaller, manageable parts.
        - ![](https://remnote-user-data.s3.amazonaws.com/8A-4yHWlH_fx-NQNnaNFmMjKwf0Krz6dTi_0coBgAZ99YmLJvAq-8Dhzo3YHleTORMzHHIhCIjFJDj8oum9uxZE2Y2d7BouIr4DRtqDo-pI3V4rjCJlhudRfHlWg2B6o.webp)**Labby**
        - 
        - # **Executing and Verifying the Complete Modular Playbook**
        - In this final step, you will execute the complete, modular workflow you have built and, more importantly, learn how to verify that the automation has achieved the desired state on the target systems. A successful playbook run is good, but confirming the outcome is essential for reliable automation.
        - First, ensure you are in the main project directory:
        - `cd ~/project/ansible_patterns` Explain Code
        - Before running the final playbook, let's visualize the complete project structure you've created. The `tree` command is excellent for this. If it's not installed, you can add it with `dnf`:
        - ```
sudo dnf install -y tree
tree .
``` Explain Code
        - You should see a structure like this:
        - ```
.
├── inventory
├── main.yml
├── playbooks
│   ├── db_setup.yml
│   └── web_configure.yml
└── tasks
    ├── verify_config.yml
    └── web_setup.yml

2 directories, 6 files
``` Explain Code
        - This structure, with a main entry point (`main.yml`), separate playbook files, and reusable task files, is a scalable and maintainable way to manage Ansible projects.
        - Now, execute the entire workflow by running your top-level `main.yml` playbook:
        - `ansible-playbook main.yml -i inventory` Explain Code
        - After the playbook completes successfully, the next crucial step is verification. You need to confirm that the system is in the state you intended. Our playbook was designed to install the `httpd` package on web servers and the `mariadb` package on database servers. Since all tasks in this lab run on your local machine, we can verify their installation directly using the `rpm` command.
        - First, check if the `httpd` package was installed as part of the web server configuration:
        - `rpm -q httpd` Explain Code
        - You should see output confirming the package is installed:
        - `httpd-2.4.xx-x.el9.x86_64` Explain Code
        - Next, verify the `mariadb` package installation from the database server configuration:
        - `rpm -q mariadb` Explain Code
        - Similarly, you should see confirmation that mariadb is installed:
        - `mariadb-10.5.xx-x.el9.x86_64` Explain Code
        - Seeing the package names in the output confirms that your Ansible playbook successfully configured the system as intended. You have now successfully built, executed, and verified a modular Ansible project from start to finish.
        - ![](https://remnote-user-data.s3.amazonaws.com/LFEodE05gzCNsXtFbufUtalrN4n2oozN4SVQr3y6i6tMwKzOSKKt5QCOa-_Hdd8YKWl8YaJ_MvbwJtA4iPm78A86BbyG53xCLL7Jo7eM8JP1uLpjgvzw4bUJeP73oYMi.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you learned essential techniques for structuring complex Ansible playbooks on RHEL. You began with the fundamentals of host selection, using basic group names, wildcards, exclusions, and logical operators to precisely target nodes defined in an inventory file. The focus then shifted to modularization, where you practiced breaking down large plays into more manageable and reusable components using both `include_tasks` for dynamic inclusion and `import_tasks` for static inclusion.
        - Building on these skills, you learned to compose a complete, multi-stage workflow by linking individual playbooks together with `import_playbook`. The hands-on process involved installing Ansible, creating a project structure, and progressively refactoring a simple playbook into a sophisticated, multi-file structure. The lab culminated in executing the final composite playbook and verifying that the entire automated workflow ran successfully against the correctly targeted hosts, demonstrating an organized and scalable approach to automation
    7. **Ansible Roles and Collections on RHEL**
        - Create a Custom Ansible Role with ansible-galaxy init
        - Install a Role Dependency from a Git Repository using requirements.yml
        - Integrate an RHEL System Role from an Ansible Collection
        - Assemble and Run a Playbook with Custom, Git, and System Roles
        - Verify the SELinux and Apache Configuration on the RHEL Server
        - 
        - # **Introduction**
        - In this lab, you will learn how to automate the configuration of a Red Hat Enterprise Linux (RHEL) web server by leveraging the power and reusability of Ansible Roles and Collections. You will build a comprehensive automation workflow by creating a custom role to deploy specific configurations, integrating an external role from a Git repository as a dependency, and utilizing a pre-built RHEL System Role from an Ansible Collection to manage system services like SELinux.
        - The process begins with creating a standardized role structure using `ansible-galaxy init`. You will then define and install a role dependency from a Git repository using a `requirements.yml` file. After integrating an RHEL System Role, you will assemble all three types of roles—custom, Git-based, and Collection-based—into a single master playbook. Finally, you will execute the playbook and verify that the Apache web server and SELinux settings have been correctly applied to the target RHEL server, demonstrating a complete, modular automation solution.
        - ![](https://remnote-user-data.s3.amazonaws.com/H2jM8SuV6CdUM_hFxyv0WWksvFhyz3ML76-nTqUdRNlEOHs1h_8EMPE-i4D-LagxX2qDdpqfpsmwQWILuOO11dmaBoHygFukAIAWWx06YQtLHaQKSNdknaPK6aOc8eDB.webp)**Labby** 
        - 
        - # **Create a Custom Ansible Role with ansible-galaxy init**
        - In this step, you will begin by creating a standardized directory structure for a new Ansible role using the `ansible-galaxy init` command. Ansible roles are a fundamental concept for building reusable and organized automation content. They allow you to package tasks, handlers, variables, and other components into a self-contained, portable unit. Using a standard structure is a best practice that makes your automation easier to understand, manage, and share.
        - First, ensure you are in the correct working directory. All work for this lab will be done within the `~/project` directory.
        - `cd ~/project` Explain Code
        - Before creating a role, you need to ensure the Ansible command-line tools are installed. The `ansible-core` package provides the essential tools, including `ansible-galaxy`.
        - Install `ansible-core` using the `dnf` package manager. The `-y` flag automatically answers "yes" to any confirmation prompts.
        - `sudo dnf install -y ansible-core` Explain Code
        - You should see output indicating that the package is being installed and dependencies are resolved.
        - ```
...
Installed:
  ansible-core-2.16.x-1.el9.x86_64
  ...
Complete!
``` Explain Code
        - It is a common practice to organize all project roles within a dedicated `roles` directory. Create this directory now.
        - `mkdir roles` Explain Code
        - Now, navigate into the newly created `roles` directory. This is where you will initialize your new custom role.
        - `cd roles` Explain Code
        - You will now use the `ansible-galaxy init` command to create a skeleton for a role named `apache.developer_configs`. This command automatically generates a set of standard directories and files, providing a clean starting point for your role development.
        - `ansible-galaxy init apache.developer_configs` Explain Code
        - After running the command, you will see a confirmation message.
        - `- Role apache.developer_configs was created successfully` Explain Code
        - To see the structure that was just created, you can use the `ls -R` command, which lists the contents of a directory and all its subdirectories recursively.
        - `ls -R apache.developer_configs` Explain Code
        - The output shows the standard directory structure for an Ansible role:
        - ```
apache.developer_configs:
defaults  files  handlers  meta  README.md  tasks  templates  tests  vars

apache.developer_configs/defaults:
main.yml

apache.developer_configs/files:

apache.developer_configs/handlers:
main.yml

apache.developer_configs/meta:
main.yml

apache.developer_configs/tasks:
main.yml

apache.developer_configs/templates:

apache.developer_configs/tests:
inventory  test.yml

apache.developer_configs/vars:
main.yml
``` Explain Code
        - Here is a brief overview of the most important directories:
            - `tasks`: Contains the main list of tasks to be executed by the role.
            - `handlers`: Contains handlers, which are tasks that only run when notified by another task.
            - `vars`: Contains variables for the role.
            - `templates`: Contains file templates that use the Jinja2 templating engine.
            - `meta`: Contains metadata for the role, including dependencies on other roles.
        - You have now successfully created the basic structure for your custom Ansible role. In the next steps, you will populate these directories with content to configure a web server.
        - ![](https://remnote-user-data.s3.amazonaws.com/fqTsKd139ZrDnvgN3kqLAUT3sU3SKbLNYvojVJtCyPDXv4u0clM0mRGOlXHZUrPl153H6Ekko0cOW_Zi0QHg4DorXJCWjnvhMrDeObX0xOr8NcDWKcXsA9oZ-Wao9GOV.webp)**Labby**
        - 
        - # **Install a Role Dependency from a Git Repository using requirements.yml**
        - In this step, you will learn how to manage role dependencies from external sources, such as a Git repository. This is a common practice in larger Ansible projects where you reuse roles developed by the community or other teams. Ansible uses a file, typically named `requirements.yml`, to define a list of roles to be installed.
        - Your custom role, `apache.developer_configs`, will depend on a foundational Apache role to ensure the web server is installed and running. You will define this dependency and install it.
        - First, ensure you are in the main project directory. If you are still in the `roles` subdirectory from the previous step, navigate back to `~/project`.
        - `cd ~/project` Explain Code
        - Now, you will create the `requirements.yml` file inside your `roles` directory. This file will list all the external roles your project needs. Use the `nano` editor to create and edit the file.
        - `nano roles/requirements.yml` Explain Code
        - Add the following content to the file. This entry tells `ansible-galaxy` to download a specific version of an Apache role from a public Git repository and name it `infra.apache` locally.
        - ```
- name: infra.apache
  src: https://github.com/geerlingguy/ansible-role-apache.git
  scm: git
  version: 3.2.0
``` Explain Code
        - Let's break down this definition:
            - `name`: This is the local name for the role. Even though the source repository has a different name, it will be installed into a directory called `infra.apache`.
            - `src`: The source URL of the Git repository.
            - `scm`: Specifies the source control management tool, which is `git` in this case.
            - `version`: The specific Git branch, tag, or commit hash to use. Pinning a version is crucial for ensuring your automation is stable and predictable.
        - Save the file and exit `nano` by pressing `Ctrl+X`, followed by `Y`, and then `Enter`.
        - With the `requirements.yml` file in place, you can now use the `ansible-galaxy install` command to download and install the role.
            - The `-r` flag points to your requirements file.
            - The `-p` flag specifies the path where the roles should be installed.
        - `ansible-galaxy install -r roles/requirements.yml -p roles` Explain Code
        - You will see output confirming the download and installation process.
        - ```
Starting galaxy role install process
- downloading role 'ansible-role-apache', owned by geerlingguy
- downloading role from https://github.com/geerlingguy/ansible-role-apache/archive/3.2.0.tar.gz
- extracting infra.apache to /home/labex/project/roles/infra.apache
- infra.apache (3.2.0) was installed successfully
``` Explain Code
        - To confirm that the role was installed correctly, list the contents of the `roles` directory.
        - `ls -l roles` Explain Code
        - You should now see the `infra.apache` directory alongside the `apache.developer_configs` role you created earlier.
        - ```
total 12
drwxr-xr-x. 9 labex labex 4096 Nov 10 10:10 apache.developer_configs
drwxr-xr-x. 9 labex labex 4096 Nov 10 10:15 infra.apache
-rw-r--r--. 1 labex labex  118 Nov 10 10:12 requirements.yml
``` Explain Code
        - You have now successfully declared an external Git repository as a dependency and installed it into your project. The next step is to integrate this dependency into your custom role's metadata.
        - ![](https://remnote-user-data.s3.amazonaws.com/umuq-g0SSRwOyQQ_uRiNH8IpYhEobCFWt3gqrg2NwM41ryRPlSlE7liCEwpGKUKj4F4lVpDi5GuZqm6VvnX3YJ3y1ugBuWRmtqfD8AWl8CQ6tjwhMWkfkDsiyeDCtIMC.webp)**Labby**
        - 
        - # **Integrate an RHEL System Role from an Ansible Collection**
        - In this step, you will work with Ansible Collections, which are the standard way to distribute Ansible content, including roles, modules, and plugins. You will install the Community General collection, which provides a set of useful modules for automating common administrative tasks including SELinux management.
        - For our web server scenario, we need to correctly configure SELinux to allow the Apache service to listen on non-standard ports. The `community.general` collection includes SELinux modules that are perfect for this task.
        - First, ensure you are in the main project directory.
        - `cd ~/project` Explain Code
        - It is a best practice to keep collections installed within the project directory to make your project self-contained. Create a directory named `collections` to store them.
        - `mkdir collections` Explain Code
        - Now, use the `ansible-galaxy collection install` command to install the required collections. The `-p` flag tells the command to install the collections into the `collections` directory you just created.
        - `ansible-galaxy collection install community.general:7.5.0 ansible.posix:1.5.4 -p collections` Explain Code
        - The command will download the collections and their dependencies. You will see output similar to the following:
        - ```
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Installing 'community.general:7.5.0' to '/home/labex/project/collections/ansible_collections/community/general'
Installing 'ansible.posix:1.5.4' to '/home/labex/project/collections/ansible_collections/ansible/posix'
...
community.general:7.5.0 was installed successfully
ansible.posix:1.5.4 was installed successfully
``` Explain Code
        - To verify that the collection is now available to your project, you can list all installed collections by specifying the collections path.
        - `ansible-galaxy collection list -p collections` Explain Code
        - The output will show the installed collections and their installation paths within your project.
        - ```
# /home/labex/project/collections/ansible_collections
Collection              Version
----------------------- -------
ansible.posix           1.5.4
community.general       7.5.0
``` Explain Code
        - When you use a module from a collection in a playbook, you must refer to it by its Fully Qualified Collection Name (FQCN). For SELinux management, you'll use `ansible.posix.selinux` for SELinux state management and `community.general.seport` for SELinux port management.
        - You have now successfully installed powerful collections that include SELinux management modules. In the next step, you will assemble a playbook that uses your custom role, the role from Git, and SELinux modules from these collections to fully configure the development web server.
        - ![](https://remnote-user-data.s3.amazonaws.com/njs-54U-Uuolr8cc-yP4s1XLCGZR7O7OYrGMj-j5q1kO48LPlEUCZ7oitPv8sf7w847bTi31wbrQSZTEIZ68hnEEfTPRFRwgNwQInphwRYnBFeHbNAcS39G3JrbVk9gz.webp)**Labby**
        - 
        - # **Assemble and Run a Playbook with Custom, Git, and System Roles**
        - In this step, you will bring together all the components you have prepared: your custom role, the dependency from Git, and the RHEL System Role. You will create a main playbook that orchestrates these roles to fully configure the development web server.
        - Think of this step as assembling a complex machine from different parts - each role serves a specific purpose, and they work together to create a complete web server environment. Let's break this down into manageable pieces:
        - First, ensure you are in the main project directory.
        - `cd ~/project` Explain Code
        - Before diving into the configuration, let's understand what we're creating:
            - **Ansible Configuration**: Sets up how Ansible behaves and where it finds files
            - **Inventory**: Defines which servers to manage (in our case, localhost)
            - **Variables**: Store data that our roles will use (developer information, SELinux settings)
            - **Custom Role Content**: The actual tasks that will configure developer environments
            - **Main Playbook**: The orchestrator that runs everything in the right order
        - ### **1. Create Ansible Configuration and Inventory**
        - The `ansible.cfg` file is like a configuration file that tells Ansible how to behave. Without it, you would need to specify paths and options in every command. With it, Ansible automatically knows where to find your roles, collections, and inventory.
        - Create the `ansible.cfg` file using `nano`. This file tells Ansible where to find your roles, collections, and inventory.
        - `nano ansible.cfg` Explain Code
        - Add the following content. Let's understand each line:
        - ```
[defaults]
inventory = inventory
roles_path = roles
collections_paths = collections
host_key_checking = False

[privilege_escalation]
become = True
``` Explain Code
        - **What each setting does:**
            - `inventory = inventory`: Instead of typing `-i inventory` every time, Ansible will automatically use this file
            - `roles_path = roles`: Ansible will look for roles in the `roles` directory
            - `collections_paths = collections`: Ansible will find your installed collections here
            - `host_key_checking = False`: Prevents SSH key verification errors in lab environments
            - `become = True`: Automatically runs tasks with elevated privileges when needed
        - Save and exit `nano` (Press `Ctrl+X`, then `Y`, then `Enter`).
        - The inventory file tells Ansible which machines to manage. In our case, we're configuring the local machine.
        - `nano inventory` Explain Code
        - Add the following line:
        - `localhost ansible_connection=local` Explain Code
        - **What this means:**
            - `localhost`: The name of our target host
            - `ansible_connection=local`: Instead of SSH, use local connections (since we're managing the same machine we're running Ansible on)
        - Save and exit `nano`.
        - ### **2. Define Role Variables**
        - Variables in Ansible are like settings that your roles can use. Instead of hardcoding values like usernames or port numbers in your tasks, you define them in variable files. This makes your automation flexible and reusable.
        - The `group_vars/all` directory is a special location where Ansible automatically loads variables for all hosts. Any YAML file in this directory becomes available to your playbooks and roles.
        - Create the directory structure for variables that apply to all hosts:
        - `mkdir -p group_vars/all` Explain Code
        - Now, create a file to define the developer information. This data will be used by your custom role to create user accounts and web configurations.
        - `nano group_vars/all/developers.yml` Explain Code
        - Add the following content:
        - ```
---
web_developers:
  - username: jdoe # First developer
    port: 9081 # Custom port for this developer's website
  - username: jdoe2 # Second developer
    port: 9082 # Custom port for this developer's website
``` Explain Code
        - **What this data structure means:**
            - `web_developers`: A list containing developer information
            - Each developer has a `username` and a `port`
            - Your custom role will loop through this list to create configurations for each developer
        - Save and exit.
        - Next, create a variable file for the SELinux configuration. SELinux (Security-Enhanced Linux) is a security module that controls what applications can do.
        - `nano group_vars/all/selinux.yml` Explain Code
        - Add the following content:
        - ```
---
selinux_state: enforcing # Set SELinux to enforcing mode (highest security)
selinux_ports: # List of ports to allow Apache to use
  - ports: "9081" # Allow port 9081
    proto: "tcp" # Protocol: TCP
    setype: "http_port_t" # SELinux type: HTTP port
    state: "present" # Add this rule
  - ports: "9082" # Allow port 9082
    proto: "tcp" # Protocol: TCP
    setype: "http_port_t" # SELinux type: HTTP port
    state: "present" # Add this rule
``` Explain Code
        - **Understanding SELinux settings:**
            - `selinux_state: enforcing`: SELinux will actively block unauthorized actions
            - `selinux_ports`: A list of port configurations
            - `http_port_t`: The SELinux type that allows Apache to bind to ports
            - By default, Apache can only use ports 80 and 443; we need to explicitly allow 9081 and 9082
        - Save and exit.
        - ### **3. Populate the Custom Role**
        - Your `apache.developer_configs` role currently has the directory structure but no actual content. We need to add:
            - **Templates**: Files that can include variables (using Jinja2 syntax)
            - **Tasks**: The actual work that Ansible will perform
            - **Handlers**: Special tasks that only run when notified (like restarting services)
            - **Metadata**: Information about role dependencies
        - Templates allow you to create configuration files that adapt based on your variables. The `.j2` extension indicates this is a Jinja2 template.
        - `nano roles/apache.developer_configs/templates/developer.conf.j2` Explain Code
        - Add the following content:
        - ```
{% for dev in web_developers %}
Listen {{ dev.port }}
<VirtualHost *:{{ dev.port }}>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/{{ dev.username }}

    <Directory /var/www/{{ dev.username }}>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
{% endfor %}
``` Explain Code
        - **Understanding the template syntax:**
            - `{% for dev in web_developers %}`: Start a loop through the developer list
            - `{{ dev.port }}`: Insert the port number for this developer
            - `{{ dev.username }}`: Insert the username for this developer
            - `{% endfor %}`: End the loop
            - The result will be separate virtual host configurations for each developer
        - **What this creates:** For our two developers, this template will generate Apache configuration that:
            1. Makes Apache listen on ports 9081 and 9082
            2. Creates virtual hosts that serve content from `/var/www/jdoe` and `/var/www/jdoe2`
            3. Sets appropriate permissions for each directory
        - Save and exit.
        - Tasks are the actual work that Ansible performs. Each task uses an Ansible module to accomplish something specific.
        - `nano roles/apache.developer_configs/tasks/main.yml` Explain Code
        - Add the following content and let's understand each task:
        - ```
---
# Task 1: Create user accounts for each developer
- name: Create developer user accounts
  ansible.builtin.user: # Use the 'user' module
    name: "{{ item.username }}" # Create user with this name
    state: present # Ensure the user exists
  loop: "{{ web_developers }}" # Do this for each developer in the list

# Task 2: Create web directories for each developer
- name: Create developer web root directories
  ansible.builtin.file: # Use the 'file' module
    path: "/var/www/{{ item.username }}" # Create this directory
    state: directory # Ensure it's a directory
    owner: "{{ item.username }}" # Set the owner
    group: "{{ item.username }}" # Set the group
    mode: "0755" # Set permissions (rwxr-xr-x)
  loop: "{{ web_developers }}"

# Task 3: Create a sample webpage for each developer
- name: Create a sample index.html for each developer
  ansible.builtin.copy: # Use the 'copy' module
    content: "Welcome to {{ item.username }}'s dev space\n" # File content
    dest: "/var/www/{{ item.username }}/index.html" # Where to put the file
    owner: "{{ item.username }}" # File owner
    group: "{{ item.username }}" # File group
    mode: "0644" # File permissions (rw-r--r--)
  loop: "{{ web_developers }}"

# Task 4: Deploy the Apache configuration file
- name: Deploy developer apache configs
  ansible.builtin.template: # Use the 'template' module
    src: developer.conf.j2 # Source template file
    dest: /etc/httpd/conf.d/developer.conf # Destination on the server
    mode: "0644" # File permissions
  notify: restart apache # Trigger the restart handler when this changes
``` Explain Code
        - **Understanding key concepts:**
            - `loop`: Repeats the task for each item in the list
            - `{{ item.username }}`: Refers to the current item's username in the loop
            - `notify: restart apache`: When this task makes changes, it will trigger a handler named "restart apache"
            - File permissions: `0755` means owner can read/write/execute, others can read/execute; `0644` means owner can read/write, others can read only
        - Save and exit.
        - Handlers are special tasks that only run when notified by other tasks. They're typically used for actions like restarting services.
        - `nano roles/apache.developer_configs/handlers/main.yml` Explain Code
        - Add the following content:
        - ```
---
- name: restart apache # This name must match the notify: statement
  ansible.builtin.service: # Use the 'service' module
    name: httpd # The service name (Apache is called 'httpd' on RHEL)
    state: restarted # Restart the service
``` Explain Code
        - **Why use handlers?**
            - Efficiency: The service only restarts if configuration actually changed
            - Order: All tasks run first, then all handlers run at the end
            - Idempotency: Multiple tasks can notify the same handler, but it only runs once
        - Save and exit.
        - Finally, we need to tell Ansible that our custom role depends on the `infra.apache` role we installed earlier.
        - `nano roles/apache.developer_configs/meta/main.yml` Explain Code
        - Replace the file's content with:
        - ```
---
dependencies:
  - role: infra.apache # This role must run before our custom role
``` Explain Code
        - **What this does:**
            - When Ansible runs `apache.developer_configs`, it will automatically run `infra.apache` first
            - This ensures Apache is installed and configured before we add our custom configurations
            - Dependencies run in the order they're listed
        - Save and exit.
        - ### **4. Assemble and Run the Main Playbook**
        - A playbook is like a recipe that tells Ansible what to do and in what order. Our playbook will:
            1. Configure SELinux settings (pre_tasks)
            2. Run our roles (which includes the dependency chain)
        - Create the main playbook file:
        - `nano web_dev_server.yml` Explain Code
        - Add the following content with detailed explanations:
        - ```
---
- name: Configure Dev Web Server # Playbook name
  hosts: localhost # Run on localhost
  pre_tasks: # Tasks that run before roles
    # Task 1: Configure SELinux mode
    - name: Set SELinux to enforcing mode
      ansible.posix.selinux: # Module from ansible.posix collection
        policy: targeted # Use the 'targeted' SELinux policy
        state: "{{ selinux_state }}" # Use the variable we defined
      when: selinux_state is defined # Only run if the variable exists

    # Task 2: Configure SELinux ports
    - name: Configure SELinux ports for Apache
      community.general.seport: # Module from community.general collection
        ports: "{{ item.ports }}" # Port number
        proto: "{{ item.proto }}" # Protocol (tcp)
        setype: "{{ item.setype }}" # SELinux type (http_port_t)
        state: "{{ item.state }}" # present or absent
      loop: "{{ selinux_ports }}" # Loop through our port list
      when: selinux_ports is defined # Only run if the variable exists

  roles: # Roles to execute
    - apache.developer_configs # Our custom role (which will trigger infra.apache)
``` Explain Code
        - **Understanding the execution order:**
            1. `pre_tasks`: SELinux configuration runs first
            2. `roles`: Role dependencies run (`infra.apache`), then our custom role
            3. `handlers`: Any notified handlers run last
        - **Why this order matters:**
            - SELinux must be configured before Apache tries to bind to custom ports
            - Apache must be installed before we can configure virtual hosts
            - Service restarts happen after all configuration is complete
        - Save and exit.
        - Now you're ready to execute your complete automation:
        - `ansible-playbook web_dev_server.yml` Explain Code
        - The playbook will execute and you'll see detailed output. Here's what to expect (for example):
        - ```
PLAY [Configure Dev Web Server] *************************************************

TASK [Gathering Facts] **********************************************************
ok: [localhost]                     # Ansible collects system information

TASK [Set SELinux to enforcing mode] *******************************************
changed: [localhost]                # SELinux mode was changed

TASK [Configure SELinux ports for Apache] **************************************
changed: [localhost] => (item={'ports': '9081', 'proto': 'tcp', 'setype': 'http_port_t', 'state': 'present'})
changed: [localhost] => (item={'ports': '9082', 'proto': 'tcp', 'setype': 'http_port_t', 'state': 'present'})

TASK [infra.apache : Ensure Apache is installed.] *******************************
changed: [localhost]                # Apache package was installed

TASK [apache.developer_configs : Create developer user accounts] ****************
changed: [localhost] => (item={'username': 'jdoe', 'port': 9081})
changed: [localhost] => (item={'username': 'jdoe2', 'port': 9082})

TASK [apache.developer_configs : Create developer web root directories] *********
changed: [localhost] => (item={'username': 'jdoe', 'port': 9081})
changed: [localhost] => (item={'username': 'jdoe2', 'port': 9082})

TASK [apache.developer_configs : Create a sample index.html for each developer] *
changed: [localhost] => (item={'username': 'jdoe', 'port': 9081})
changed: [localhost] => (item={'username': 'jdoe2', 'port': 9082})

TASK [apache.developer_configs : Deploy developer apache configs] ***************
changed: [localhost]                # Configuration file was created

RUNNING HANDLER [apache.developer_configs : restart apache] *********************
changed: [localhost]                # Apache was restarted

PLAY RECAP **********************************************************************
localhost                  : ok=17   changed=12   unreachable=0    failed=0    skipped=3    rescued=0    ignored=0
``` Explain Code
        - You have successfully assembled and run a complex playbook that combines multiple roles from different sources to create a complete web development environment!
        - ![](https://remnote-user-data.s3.amazonaws.com/VLM3If2L4XPJtX_7exE8ToftWbk5cBD_7pL6Zq4xqixtLiY7ScvKfqNmmXinlMLj8pq58jJZZGshQlx1TM2JBCNfTt-XeGFUOFZOv47fSfo-xSwMjdnsPNoe0E0ChSeu.webp)**Labby**
        - 
        - # **Verify the SELinux and Apache Configuration on the RHEL Server**
        - In this final step, you will verify that your Ansible automation has correctly configured the system. It's crucial to confirm that the services are running as expected and that the security policies (SELinux) have been applied correctly. You will use standard RHEL command-line tools to inspect the state of the system.
        - First, ensure you are in the main project directory.
        - `cd ~/project` Explain Code
        - ### **1. Verify SELinux Configuration**
        - The SELinux modules from the collections were tasked with setting the SELinux mode to `enforcing` and allowing new ports for the `http_port_t` type.
        - Check the current SELinux status using the `sestatus` command.
        - `sestatus` Explain Code
        - The output should show that SELinux is enabled and in `enforcing` mode.
        - ```
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      33
``` Explain Code
        - Next, use the `semanage port` command to verify that ports `9081` and `9082` have been added to the `http_port_t` context. You can pipe the output to `grep` to find the relevant lines.
        - `sudo semanage port -l | grep http_port_t` Explain Code
        - You should see your custom ports listed among the default HTTP ports. The exact output may vary, but it will include the ports you defined.
        - ```
http_port_t                    tcp      9082, 9081, 80, 81, 443, 488, 8008, 8009, 8443, 9000
pegasus_http_port_t            tcp      5988
``` Explain Code
        - This confirms that the SELinux modules have successfully updated the policy.
        - ### **2. Verify Apache Service and Configuration**
        - The `infra.apache` role installed and started the `httpd` service. Since `systemctl` is not available in this container environment, you can check for the running process using `ps`.
        - `ps aux | grep httpd` Explain Code
        - You should see several `httpd` processes running, indicating the service is active.
        - ```
root        8851  0.2  0.4  25652 16228 ?        Ss   09:31   0:00 /usr/sbin/httpd -DFOREGROUND
apache      8852  0.0  0.1  25308  6044 ?        S    09:31   0:00 /usr/sbin/httpd -DFOREGROUND
apache      8853  0.0  0.3 1443348 11364 ?       Sl   09:31   0:00 /usr/sbin/httpd -DFOREGROUND
apache      8854  0.0  0.3 1443348 11480 ?       Sl   09:31   0:00 /usr/sbin/httpd -DFOREGROUND
apache      8855  0.0  0.4 1574484 15848 ?       Sl   09:31   0:00 /usr/sbin/httpd -DFOREGROUND
labex       9298  0.0  0.0   6408  2176 pts/3    S+   09:31   0:00 grep --color=auto httpd
``` Explain Code
        - ### **3. Verify Web Content Accessibility**
        - Finally, the most important test is to see if the developer websites are accessible. Your `apache.developer_configs` role set up virtual hosts on ports `9081` and `9082`. Use the `curl` command to request the content from each endpoint.
        - First, test the site for user `jdoe` on port `9081`.
        - `curl http://localhost:9081` Explain Code
        - The expected output is the content of the `index.html` file you created for this user.
        - `Welcome to jdoe's dev space` Explain Code
        - Next, test the site for user `jdoe2` on port `9082`.
        - `curl http://localhost:9082` Explain Code
        - You should see the corresponding welcome message.
        - `Welcome to jdoe2's dev space` Explain Code
        - These successful `curl` commands confirm that Apache is correctly configured, the virtual hosts are working, and the SELinux policy is allowing traffic on the custom ports.
        - Congratulations! You have successfully built a complete Ansible automation project that combines a custom role, a role from a Git repository, and SELinux modules from Ansible collections to configure a secure, multi-tenant development web server.
        - ![](https://remnote-user-data.s3.amazonaws.com/J4eS-s08QDPJKnt7fEnb_nbAPNza7Y9xkg5a4i_CxRUIbt0Eb0cLAvWnodplMKcmtzH0GZ0F4xbOo1iGSjHJG7XYClPu7tjmNv3MKkwnm7m_NkfEu0ySFe2gk5sl2dti.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you will learn how to automate the configuration of a RHEL web server by leveraging the power and structure of Ansible Roles and Collections. You will begin by creating a custom role from scratch using the `ansible-galaxy init` command, which establishes a standardized directory structure for reusable automation content. This foundational step sets the stage for more complex automation tasks.
        - Building upon the custom role, you will then integrate external dependencies, including a role from a Git repository via a `requirements.yml` file and an official RHEL System Role from an Ansible Collection. Finally, you will assemble these different types of roles—custom, Git-based, and system—into a single playbook, execute it to configure the server, and verify the resulting Apache and SELinux settings to confirm the automation was successful.
    8. **Troubleshoot Ansible Playbooks and Hosts on RHEL**
        - Prepare the RHEL Environment and Configure Ansible Logging
        - Fix YAML Syntax and Indentation Errors in a Playbook
        - Resolve Jinja2 Quoting and Template Path Errors
        - Use Check Mode to Troubleshoot Managed Host Service Errors
        - Correct Firewall Configuration and Host Unreachability Issues
        - 
        - # **Introduction**
        - In this lab, you will learn how to troubleshoot common issues encountered when working with Ansible on Red Hat Enterprise Linux. You will gain practical experience in identifying and resolving a variety of problems, from initial environment setup to common playbook errors and managed host connectivity issues. The exercises cover fixing YAML syntax, correcting Jinja2 templating mistakes, and diagnosing problems on remote systems.
        - You will begin by preparing a RHEL environment and configuring Ansible for effective logging. Then, you will dive into hands-on troubleshooting scenarios, using Ansible's check mode to diagnose service-related problems and correcting firewall configurations to resolve host unreachability. By the end of this lab, you will be equipped with a comprehensive set of skills for maintaining robust Ansible automation workflows.
        - ![](https://remnote-user-data.s3.amazonaws.com/zynd8OPwfE2c1BvVXLtQLT3BFuio9CIhS9BJVb0pJmLixtvGYoULDtqITuyP9sto5mlU82vpg1kDzpnoBQ6Tghzv6tu8WGXXhi52UfyKaAvMg9qVvWCGCyKJERkj1u3Z.webp)**Labby** 
        - 
        - # **Prepare the RHEL Environment and Configure Ansible Logging**
        - In this step, you will prepare your Red Hat Enterprise Linux environment for Ansible automation. This involves installing the necessary software, creating a dedicated project directory, and setting up a basic configuration file to control Ansible's behavior and enable logging. Proper setup is the first step towards effective automation and troubleshooting.
            1. **Install Ansible**
                - First, you need to install Ansible. The core automation engine is provided by the `ansible-core` package. Use the `dnf` package manager with `sudo` to install it. The `-y` flag automatically answers "yes" to any confirmation prompts.
                - `sudo dnf install -y ansible-core` Explain Code
                - You should see output indicating that the package is being installed along with its dependencies.
                - ```
Last metadata expiration check: ...
Dependencies resolved.
================================================================================
 Package             Architecture   Version                Repository      Size
================================================================================
Installing:
 ansible-core        x86_64         <version>              <repo>          2.8 M
...
Transaction Summary
================================================================================
Install  XX Packages

Total download size: XX M
Installed size: XX M
...
Complete!
``` Explain Code
            2. **Create a Project Directory**
                - It's a best practice to organize your Ansible projects in dedicated directories. This keeps your playbooks, inventory, and configuration files neatly separated. Let's create a directory named `ansible_troubleshooting` inside your home project folder and navigate into it.
                - ```
mkdir -p ~/project/ansible_troubleshooting
cd ~/project/ansible_troubleshooting
``` Explain Code
                - From now on, all commands in this lab will be executed from within the `~/project/ansible_troubleshooting` directory.
            3. **Create an Ansible Inventory File**
                - An inventory is a file that lists the hosts (or nodes) that Ansible will manage. Since you are working on a single LabEx VM, you will configure Ansible to manage the local machine itself.
                - Create a file named `inventory` and add `localhost` to it. The `ansible_connection=local` part tells Ansible to execute commands directly on the control node (your VM) without using SSH.
                - `echo "localhost ansible_connection=local" > inventory` Explain Code
                - You can verify the content of the file using the `cat` command:
                - `cat inventory` Explain Code
                - **Expected Output:**
                - `localhost ansible_connection=local` Explain Code
            4. **Configure Ansible Logging**
                - An `ansible.cfg` file allows you to customize Ansible's behavior for a specific project. When placed in the project directory, its settings override the system-wide defaults. Here, you will create this file to specify the location of your inventory and to enable logging. Logging is crucial for troubleshooting, as it records detailed information about every playbook run.
                - Use the `nano` editor to create the `ansible.cfg` file.
                - `nano ansible.cfg` Explain Code
                - Now, copy and paste the following content into the `nano` editor. This configuration tells Ansible to use the `inventory` file in the current directory and to write all log output to a file named `ansible.log`.
                - ```
[defaults]
inventory = /home/labex/project/ansible_troubleshooting/inventory
log_path = /home/labex/project/ansible_troubleshooting/ansible.log
``` Explain Code
                - To save the file in `nano`, press `Ctrl+X`, then `Y` to confirm, and finally `Enter` to write the file.
                - Your environment is now fully prepared. You have Ansible installed and a project directory configured with a local inventory and logging enabled, ready for the next steps.
        - ![](https://remnote-user-data.s3.amazonaws.com/XR8n-HKdfTJ5E1vG1pOLMHAMlbKXZhNwrvyjgDXYyz9Tcy0-SI9_KwGmsu0Epn_Nltfp5qzhKxiRCg8gnL7EUZA9goooq-koEG8dk_ubajLljAV72MqAhnm_D4DlSjEQ.webp)**Labby**
        - 
        - # **Fix YAML Syntax and Indentation Errors in a Playbook**
        - In this step, you will learn how to diagnose and fix two of the most common types of errors in Ansible playbooks: YAML syntax errors and incorrect indentation. YAML, the language used for writing playbooks, is very strict about its structure. A single misplaced space or an unquoted special character can prevent a playbook from running. You will use the `ansible-playbook --syntax-check` command, an essential tool for validating your playbooks before execution.
            1. **Create a Playbook with Intentional Errors**
                - First, you will create a new playbook file named `webserver.yml` in your project directory (`~/project/ansible_troubleshooting`). This file contains intentional errors that you will fix.
                - Use `nano` to create the file:
                - `nano webserver.yml` Explain Code
                - Copy and paste the following content into the editor. Notice the two deliberate errors: an unquoted string containing a colon and incorrect indentation for the second task.
                - ```
---
- name: Configure Web Server
  hosts: localhost
  vars:
    # ERROR 1: Unquoted colon in string
    package_comment: This is a package: httpd
  tasks:
    - name: Install httpd package
      ansible.builtin.dnf:
        name: httpd
        state: present

    # ERROR 2: Incorrect indentation
      - name: Create a test index page
        ansible.builtin.copy:
          content: "<h1>Welcome to Ansible</h1>"
          dest: /var/www/html/index.html
``` Explain Code
                - Save the file and exit `nano` by pressing `Ctrl+X`, then `Y`, and `Enter`.
            2. **Identify and Fix the YAML Syntax Error (Unquoted Colon)**
                - Now, run a syntax check on the playbook you just created. This command will parse the file and report any syntax issues without actually running the tasks.
                - `ansible-playbook --syntax-check webserver.yml` Explain Code
                - **Expected Output (Error):** You will see an error because the value for `package_comment` contains a colon (`:`) but is not enclosed in quotes. YAML interprets the colon as a key-value separator, leading to a syntax error.
                - ```
ERROR! We were unable to read either as JSON nor YAML, these are the errors we found:
- Syntax Error while loading YAML.
  did not find expected ':'

The error appears to be in '/home/labex/project/ansible_troubleshooting/webserver.yml': line 6, column 41, but may be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

  vars:
    package_comment: This is a package: httpd
                                        ^ here
``` Explain Code
                - **Solution:** To fix this, you must enclose the string in double quotes. Open the file again with `nano`:
                - `nano webserver.yml` Explain Code
                - Modify the line under `vars` to add quotes:
                - ```
# ... (rest of the file)
vars:
  # FIX: Add quotes around the string with a colon
  package_comment: "This is a package: httpd"
# ... (rest of the file)
``` Explain Code
                - Save and exit the editor.
            3. **Identify and Fix the YAML Indentation Error**
                - With the first error fixed, run the syntax check again.
                - `ansible-playbook --syntax-check webserver.yml` Explain Code
                - **Expected Output (Error):** This time, Ansible will report a different error related to the structure of the playbook.
                - ```
ERROR! A malformed block was encountered.

The error appears to be in '/home/labex/project/ansible_troubleshooting/webserver.yml': line 13, column 11, but may be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:


      # ERROR 2: Incorrect indentation
      - name: Create a test index page
        ^ here
``` Explain Code
                - This error occurs because YAML uses indentation to define structure. All items in a list (in this case, the tasks, which are list items starting with `-`) must have the same level of indentation. The second task, `Create a test index page`, is indented too far.
                - **Solution:** Open the file one more time to correct the indentation.
                - `nano webserver.yml` Explain Code
                - Remove the extra spaces before the second task so that its hyphen (`-`) aligns perfectly with the hyphen of the first task.
                - ```
# ... (rest of the file)
tasks:
  - name: Install httpd package
    ansible.builtin.dnf:
      name: httpd
      state: present

  # FIX: Correct the indentation to align with the previous task
  - name: Create a test index page
    ansible.builtin.copy:
      content: "<h1>Welcome to Ansible</h1>"
      dest: /var/www/html/index.html
``` Explain Code
                - Save and exit the editor.
            4. **Verify the Corrected Playbook**
                - Finally, run the syntax check one last time.
                - `ansible-playbook --syntax-check webserver.yml` Explain Code
                - This time, the command should complete without any errors, and you will see the playbook's name printed, confirming that the syntax is now correct.
                - **Expected Output (Success):**
                - `playbook: webserver.yml` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/o05VA2dyWLCJZbXG7YHhh0tP8L7AWpWtPLL27RINq42u2dDsQcG5mc8EGSQ501kL6ABlkLcCZ9SVLlC68RtxnPG745IVsljbcVGiW7KvrNESD8V4i8_QV0Sd4e8AY_gE.webp)**Labby**
        - 
        - # **Resolve Jinja2 Quoting and Template Path Errors**
        - In this step, you will tackle errors related to Jinja2, Ansible's powerful templating engine. You'll learn why Jinja2 expressions often need to be quoted and how to debug issues when a playbook cannot find a specified template file. These are common runtime errors that occur after a playbook has already passed a syntax check.
            1. **Create a Jinja2 Template File**
                - First, you need a template file. Unlike a static file, a template can contain variables that Ansible will replace with actual values during playbook execution. You will create a simple HTML template.
                - Use `nano` to create a file named `index.html.j2` in your project directory (`~/project/ansible_troubleshooting`). The `.j2` extension is a common convention for Jinja2 templates.
                - `nano index.html.j2` Explain Code
                - Copy and paste the following HTML content into the editor. Note the `{{ welcome_message }}` placeholder, which is a Jinja2 variable.
                - ```
<h1>{{ welcome_message }}</h1>
<p>This page was deployed by Ansible.</p>
``` Explain Code
                - Save the file and exit `nano` (`Ctrl+X`, `Y`, `Enter`).
            2. **Modify the Playbook to Use the Template and Introduce Errors**
                - Now, modify your `webserver.yml` playbook to use the `ansible.builtin.template` module. You will also introduce two new errors: an unquoted Jinja2 variable and an incorrect template path.
                - Open `webserver.yml` with `nano`:
                - `nano webserver.yml` Explain Code
                - Replace the entire content of the file with the following. The `become: true` directive tells Ansible to execute tasks with administrative privileges (using `sudo`), which is necessary to install software and write files to system directories like `/var/www/html`.
                - ```
---
- name: Configure Web Server
  hosts: localhost
  become: true
  vars:
    package_name: httpd
    welcome_message: "Welcome to Ansible with Jinja2"
  tasks:
    - name: Install httpd package
      ansible.builtin.dnf:
        # ERROR 1: Unquoted Jinja2 variable
        name: { { package_name } }
        state: present

    - name: Create a test index page from template
      ansible.builtin.template:
        # ERROR 2: Incorrect template source path
        src: index.j2
        dest: /var/www/html/index.html
``` Explain Code
                - Save and exit the editor.
            3. **Identify and Fix the Jinja2 Quoting Error**
                - Even though this is a Jinja2 issue, it can manifest as a YAML syntax error. Run the syntax checker to see how Ansible interprets it.
                - `ansible-playbook --syntax-check webserver.yml` Explain Code
                - **Expected Output (Error):** You will get a syntax error because a YAML value starting with `{{` is treated as a special construct and must be quoted to be interpreted as a string.
                - ```
ERROR! A malformed block was encountered.

The error appears to be in '/home/labex/project/ansible_troubleshooting/webserver.yml': line 11, column 19, but may be elsewhere in the file depending on the exact syntax problem.

The offending line appears to be:

          # ERROR 1: Unquoted Jinja2 variable
          name: {{ package_name }}
                  ^ here
``` Explain Code
                - **Solution:** Open `webserver.yml` and enclose the Jinja2 variable in double quotes.
                - `nano webserver.yml` Explain Code
                - Modify the `Install httpd package` task:
                - ```
# ... (rest of the file)
tasks:
  - name: Install httpd package
    ansible.builtin.dnf:
      # FIX: Quote the Jinja2 expression
      name: "{{ package_name }}"
      state: present
# ... (rest of the file)
``` Explain Code
                - Save and exit. The syntax check should now pass.
            4. **Identify and Fix the Template Path Error**
                - Now that the syntax is correct, try to run the playbook.
                - `ansible-playbook webserver.yml` Explain Code
                - **Expected Output (Error):** The playbook will fail, but this time it's a runtime error, not a syntax error. The error message clearly states that the source file `index.j2` could not be found.
                - ```
TASK [Create a test index page from template] **********************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "Could not find or access '/home/labex/project/ansible_troubleshooting/index.j2' on the Ansible Controller."}
``` Explain Code
                - This happens because the `src` parameter in your playbook points to `index.j2`, but the file you created is named `index.html.j2`.
                - **Solution:** Open `webserver.yml` one last time and correct the filename.
                - `nano webserver.yml` Explain Code
                - Modify the `src` parameter in the `Create a test index page from template` task:
                - ```
# ... (rest of the file)
- name: Create a test index page from template
  ansible.builtin.template:
    # FIX: Correct template source filename
    src: index.html.j2
    dest: /var/www/html/index.html
# ... (rest of the file)
``` Explain Code
                - Save and exit the editor.
            5. **Run the Playbook Successfully**
                - Run the playbook again. It should now complete all tasks successfully.
                - `ansible-playbook webserver.yml` Explain Code
                - **Expected Output (Success):**
                - ```
PLAY [Configure Web Server] ****************************************************

TASK [Gathering Facts] *********************************************************
ok: [localhost]

TASK [Install httpd package] ***************************************************
changed: [localhost]

TASK [Create a test index page from template] **********************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
        - ![](https://remnote-user-data.s3.amazonaws.com/szXjN4QWZi1pEk20EfURYL1g47l5p7xIH3bT3_ZJnhUQ8rb8v4jGcIuMWP0ZPau7DCBGRJErgrxe-xfc6AswD_LIc7tL6TI6_yoQz2kk7TPUINTOMqDBSWdHWeFcnXWd.webp)**Labby**
        - 
        - # **Use Check Mode to Troubleshoot Managed Host Service Errors**
        - In this step, you will learn to use one of Ansible's most powerful troubleshooting features: **Check Mode**. Check mode (activated with the `--check` flag) allows you to run a playbook to see what changes   *would*   be made, without actually modifying anything on the system. This is incredibly useful for safely testing playbooks and diagnosing issues, such as incorrect service names, before they cause real problems.
            1. **Create a Playbook to Manage a Service**
                - You will now create a new playbook, `service.yml`, designed to ensure the `httpd` web server service is running. However, you will intentionally use an incorrect service name to simulate a common error.
                - Use `nano` to create the `service.yml` file in your `~/project/ansible_troubleshooting` directory.
                - `nano service.yml` Explain Code
                - Copy and paste the following content. Note that the service name is set to `apache2`, which is a common name for the Apache web server on other Linux distributions but is incorrect for RHEL.
                - ```
---
- name: Manage Web Server Service
  hosts: localhost
  become: true
  tasks:
    - name: Ensure web server service is started
      ansible.builtin.service:
        # ERROR: Incorrect service name for RHEL
        name: apache2
        state: started
        enabled: true
``` Explain Code
                - Save the file and exit `nano` (`Ctrl+X`, `Y`, `Enter`).
            2. **Use Check Mode to Identify the Service Error**
                - Instead of running the playbook normally, execute it in check mode. This will prevent Ansible from making any changes but will allow it to check the state of the system and report what it   *would*   do.
                - `ansible-playbook --check service.yml` Explain Code
                - **Expected Output (Error):** The playbook will fail. The error message will clearly indicate that it could not find a service named `apache2`. This immediately tells you that the `name` parameter in your playbook is wrong.
                - ```
TASK [Ensure web server service is started] ************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "Could not find the requested service 'apache2': host"}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
``` Explain Code
            3. **Find the Correct Service Name**
                - To fix the playbook, you need to find the correct service name for the `httpd` package on RHEL. A reliable way to do this is to list the files installed by the package and look for the service unit file, which typically resides in `/usr/lib/systemd/system/`.
                - Use the `rpm` command to query the `httpd` package:
                - `rpm -ql httpd | grep systemd` Explain Code
                - **Expected Output:** This command will list the `systemd`-related files, including the service file.
                - ```
/usr/lib/systemd/system/httpd.service
/usr/lib/systemd/system/httpd@.service
...
``` Explain Code
                - The output `httpd.service` tells you that the correct service name is `httpd`.
            4. **Correct the Playbook and Re-run in Check Mode**
                - Now that you know the correct service name, edit the `service.yml` file.
                - `nano service.yml` Explain Code
                - Change the service `name` from `apache2` to `httpd`.
                - ```
# ... (rest of the file)
- name: Ensure web server service is started
  ansible.builtin.service:
    # FIX: Correct service name for RHEL
    name: httpd
    state: started
    enabled: true
``` Explain Code
                - Save and exit the editor. Now, run the playbook in check mode again.
                - `ansible-playbook --check service.yml` Explain Code
                - **Expected Output (Success in Check Mode):** This time, the playbook should report a `changed` status. In check mode, `changed` means "a change would have been made if this were a real run." It indicates that your playbook logic is now correct and Ansible has identified that the `httpd` service needs to be started.
                - ```
TASK [Ensure web server service is started] ************************************
changed: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
                - **Note:** In this specific container-based lab environment, a full `systemd` init system is not running. While check mode works correctly, a normal run of the `ansible.builtin.service` module might still encounter issues. The key lesson here is using check mode to validate your playbook's logic against the system's configuration.
        - ![](https://remnote-user-data.s3.amazonaws.com/p9CpvbqLzxaH-UIQn16Jpcdrv2NgyvjVdhXqTfrrhxW6OV7XKGxJ2njwg-4Xuc1KlF1XPfElybTuw5NuB56_55j6J1tBlTf4h0vqscVJHm2UkK6_zbBiUEgoyRU1fQZR.webp)**Labby**
        - 
        - # **Correct Firewall Configuration and Host Unreachability Issues**
        - In this final step, you will address two critical runtime issues: failures caused by incorrect system configurations, such as the firewall, and connectivity problems resulting from errors in your Ansible inventory file. Mastering these will help you resolve some of the most common roadblocks in automation.
        - ### **Part 1: Correcting Firewall Configuration**
        - A common task in server configuration is opening ports in the firewall. A playbook can easily fail if it refers to a firewall service that doesn't exist on the target system.
            1. **Install and Prepare** `**firewalld**`
                - First, ensure the `firewalld` package is installed, as it provides the firewall management service on RHEL.
                - `sudo dnf install -y firewalld` Explain Code
                - Start the `firewalld` service.
                - `sudo systemctl start firewalld` Explain Code
                - You also need to install the `ansible.posix` collection, which contains the `firewalld` module used in this exercise.
                - `ansible-galaxy collection install ansible.posix` Explain Code
                - **Note:** You may see a warning about Ansible version compatibility, but the collection will still function correctly for this exercise.
            2. **Create a Playbook with a Firewall Error**
                - Create a new playbook named `firewall.yml` that attempts to enable the `http` service. However, you will intentionally use an incorrect service name, `web`, to trigger an error.
                - `nano firewall.yml` Explain Code
                - Copy and paste the following content into the editor:
                - ```
---
- name: Configure System Firewall
  hosts: localhost
  become: true
  tasks:
    - name: Allow web traffic through firewall
      ansible.posix.firewalld:
        # ERROR: 'web' is not a standard firewalld service
        service: web
        permanent: true
        state: enabled
``` Explain Code
                - Save and exit `nano` (`Ctrl+X`, `Y`, `Enter`).
            3. **Run the Playbook and Diagnose the Failure**
                - Execute the playbook. It will fail because `firewalld` does not recognize a service named `web`.
                - `ansible-playbook firewall.yml` Explain Code
                - **Expected Output (Error):** The error message clearly states that `web` is not a supported service, pointing you directly to the problem.
                - ```
TASK [Allow web traffic through firewall] **************************************
fatal: [localhost]: FAILED! => {"changed": false, "msg": "web is not a supported service. This is what I have."}

PLAY RECAP *********************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=1    skipped=0    rescued=0    ignored=0
``` Explain Code
            4. **Find the Correct Firewall Service Name**
                - To find the list of valid, predefined service names, you can use the `firewall-cmd` command-line tool.
                - `firewall-cmd --get-services` Explain Code
                - **Expected Output:** You will see a long list of available services. Look through the list to find the correct one for web traffic, which is `http`.
                - `RH-Satellite-6 ... ftp http https imaps ipp ipp-client ...` Explain Code
            5. **Correct the Playbook and Run Successfully**
                - Edit `firewall.yml` and replace the incorrect service name `web` with the correct one, `http`.
                - `nano firewall.yml` Explain Code
                - The corrected task should look like this:
                - ```
# ... (rest of the file)
- name: Allow web traffic through firewall
  ansible.posix.firewalld:
    # FIX: Use the correct firewalld service name
    service: http
    permanent: true
    state: enabled
``` Explain Code
                - Save and exit. Now, run the playbook again. It should complete successfully.
                - `ansible-playbook firewall.yml` Explain Code
        - ### **Part 2: Troubleshooting Host Unreachability**
        - An "unreachable" error means Ansible cannot connect to a host listed in your inventory. This is often caused by a simple typo in the hostname.
            1. **Simulate an Unreachable Host**
                - Intentionally introduce a typo into your `inventory` file and remove the local connection setting. This will force Ansible to attempt an actual network connection to the misspelled hostname.
                - `nano inventory` Explain Code
                - Change `localhost` to `localhossst` and remove `ansible_connection=local`.
                - ```
# ERROR: Intentional typo in hostname, no local connection
localhossst
``` Explain Code
                - Save and exit the editor.
            2. **Modify the Playbook to Use Inventory Hosts**
                - First, you need to modify the `webserver.yml` playbook to use the inventory hosts instead of the hardcoded `localhost`. When a playbook uses `hosts: localhost`, Ansible treats it as a special case and bypasses the inventory file entirely.
                - `nano webserver.yml` Explain Code
                - Change the `hosts` line from `localhost` to `all`:
                - ```
---
- name: Configure Web Server
  hosts: all # Changed from 'localhost' to use inventory hosts
  become: true
  # ... rest of the playbook remains the same
``` Explain Code
                - Save and exit the editor.
            3. **Run the Playbook to Trigger the Error**
                - Now try to run the modified playbook. It will fail because the inventory contains the typo `localhossst`.
                - `ansible-playbook webserver.yml` Explain Code
                - **Expected Output (Error):** Ansible will fail and report the host as `UNREACHABLE`. The error message indicates that the hostname could not be resolved.
                - ```
PLAY [Configure Web Server] ****************************************************

TASK [Gathering Facts] **********************************************************
fatal: [localhossst]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: ssh: Could not resolve hostname localhossst: Name or service not known", "unreachable": true}

PLAY RECAP *********************************************************************
localhossst                : ok=0    changed=0    unreachable=1    failed=0    skipped=0    rescued=0    ignored=0
``` Explain Code
            4. **Correct the Inventory File**
                - The `UNREACHABLE` status is your cue to double-check hostnames and network connectivity. In this case, the fix is to correct the typo in the `inventory` file.
                - `nano inventory` Explain Code
                - Change `localhossst` back to `localhost`.
                - ```
# FIX: Corrected hostname
localhost ansible_connection=local
``` Explain Code
                - Save and exit. Rerunning `ansible-playbook webserver.yml` will now succeed.
            5. **Optional: Restore the Original Playbook**
                - If you want to restore the playbook to use `hosts: localhost` for future exercises, you can change it back:
                - `nano webserver.yml` Explain Code
                - Change the `hosts` line back to `localhost`:
                - ```
---
- name: Configure Web Server
  hosts: localhost # Restored to original
  become: true
  # ... rest of the playbook
``` Explain Code
                - Save and exit. This step demonstrates the difference between using hardcoded `localhost` (which bypasses inventory) versus using inventory-defined hosts.
        - ![](https://remnote-user-data.s3.amazonaws.com/f8EFlN_prkwRnXsIDLI-b8Cj8RsKOm6XLWPMebvHz8eh5ohaE9G55CbZaENo2yJfJD25ngpi6pkCHJZd0sRgTQvuSJm1G_A_glYecWHVEGWoMOQwle2phiplBcOgkIoV.webp)**Labby**
        - 
        - # **Summary**
        - In this lab, you prepared a Red Hat Enterprise Linux environment for Ansible by installing `ansible-core` and configuring logging, then proceeded to troubleshoot a variety of common issues. You learned to diagnose and resolve errors within playbooks, such as fixing incorrect YAML syntax, indentation, Jinja2 quoting, and invalid template paths. These skills are fundamental to writing valid and reliable automation code.
        - Furthermore, you addressed problems related to the managed host environment. You utilized Ansible's check mode to safely perform a dry run and identify potential service failures on a target node without making actual changes. The lab concluded by tackling connectivity problems, where you corrected firewall configurations to resolve host unreachability, providing a comprehensive approach to debugging from the control node to the managed host.
    9. **Automate RHEL Administration Tasks with Ansible**
        - Configure Repository and Manage Software Packages
        - Automate User Management and SSH Configuration
        - Automate Service Management and Task Scheduling
        - Automate Storage Management with LVM and Filesystems
        - Automate Network Configuration and Information Gathering
        - 
        - 
-  **RHCSA Certification Exam Practice Exercises** - 58 labs
    1. **Understand and Use Essential Tools**
        - Locate Setuid Files
            - # **Introduction**
                - In Unix-like operating systems, setuid (set user ID) is a special file permission that allows a user to execute a file with the permissions of the file's owner. While this can be useful for certain system operations, it can also pose security risks if misused. In this challenge, you'll learn how to identify and list all setuid files on a system, which is an essential skill for system administrators and security professionals.
            - ## **Environment**
                - LabEx uses Red Hat Universal Base Image 9 (UBI9) to simulate the exam environment. It may not be identical to the actual RHCSA exam environment, but it provides a good representation of the tasks you'll encounter.
                - There are two users in the environment:
                    - `labex`: A standard user with sudo privileges, password: `labex`.
                    - `root`: The system administrator, password: `redhat`.
                - The challenge features real exam questions, along with explanations, requirements, and automated verification scripts to help you confirm task completion. It effectively simulates the knowledge areas covered in the RHCSA exam.
                - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 82% pass rate. It has received a 100% positive review rate from learners.
            - # **Locate and List Setuid Files**
                - In this step, you'll use the `find` command to search the entire filesystem for setuid files and save the results to a file.
                - ## **Tasks**
                    - Search the entire filesystem for files with the setuid permission set.
                    - Save the list of setuid files to a file named `setuid_list` in your home directory.
                - ## **Requirements**
                    - Execute all commands as the `labex` user in the `/home/labex` directory.
                    - Use the `find` command to search for setuid files.
                    - Save the output to a file named `setuid_list` in the `/home/labex` directory.
                - ## **Example**
                - After completing this task, the `setuid_list` file might contain entries similar to the following:
                - ```
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/chage
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/su
/usr/bin/mount
/usr/bin/umount
/usr/bin/crontab
/usr/bin/pkexec
``` Explain Code
                - Note that the actual list may vary depending on the system configuration.
            - # **Summary**
                - In this challenge, you learned how to find and list all setuid files on a Unix-like system. This task is crucial for system administrators and security professionals to identify potentially risky files with elevated permissions. You used the `find` command with specific options to locate files with the setuid bit set and redirected the output to a file for further analysis. This skill is valuable for conducting security audits, identifying potential vulnerabilities, and maintaining system integrity.
            - # **Step 1 Solution**
                - To find all setuid files on the system and save the list, follow these steps:
                    1. Open a terminal as the `labex` user.
                    2. Navigate to the home directory:
                        - `cd /home/labex`
                    3. Use the `find` command to search for setuid files and redirect the output to `setuid_list`:
                        - `sudo find / -type f -perm -4000 > setuid_list`
                        - Let's break down this command:
                            - `sudo`: Run the command with root privileges to access all directories.
                            - `find`: The command used to search for files and directories.
                            - `/`: Start the search from the root directory.
                            - `-type f`: Look for regular files only.
                            - `-perm -4000`: Match files with the setuid bit set.
                            - `> setuid_list`: Redirect the output to a file named `setuid_list`.
                    4. Verify the contents of the file:
                        - `cat setuid_list`
                - This command searches the entire filesystem for files with the setuid permission set and saves the results to the `setuid_list` file in your home directory. The setuid permission is represented by the special permission bit 4000.
        - Manage Logs and Archives
            - # **Introduction**
            - In this challenge, you will practice essential system administration skills related to log analysis and file archiving. You'll search for specific entries in a simulated log file, export them, and then create an archive of a directory. These tasks simulate common system administration activities for troubleshooting and backup purposes.
            - ## **Environment**
            - LabEx uses Red Hat Universal Base Image 9 (UBI9) to simulate the exam environment. It may not be identical to the actual RHCSA exam environment, but it provides a good representation of the tasks you'll encounter.
            - There are two users in the environment:
                - `labex`: A standard user with sudo privileges, password: `labex`.
                - `root`: The system administrator, password: `redhat`.
            - The challenge features real exam questions, along with explanations, requirements, and automated verification scripts to help you confirm task completion. It effectively simulates the knowledge areas covered in the RHCSA exam.
            - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 94% pass rate. It has received a 100% positive review rate from learners.
            - 
            - # **Log Analysis and Archiving**
            - This step involves searching for specific log entries, exporting them, and creating an archive of simulated log files.
            - ## **Tasks**
                - Find all log messages in `~/logs/messages` that contain "ACPI"
                - Export the found messages to a file called `~/acpi_logs`
                - Archive all of `~/logs` and save it to `~/log_archive.tgz`
            - ## **Requirements**
                - All operations must be performed as the `labex` user
                - The log search must be case-sensitive
                - The exported log file must be named `acpi_logs` and located in your home directory (`~`)
                - The archive must be a gzipped tar file named `log_archive.tgz` and located in your home directory (`~`)
                - The archive must include all files and subdirectories in `~/logs/`
            - ## **Example**
            - After completing the task, the content of `~/acpi_logs` might look like this:
            - ```
May 15 10:23:45 localhost kernel: ACPI: Power Button [PWRB]
May 15 11:34:56 localhost kernel: ACPI: Sleep Button [SLPB]
May 15 12:45:67 localhost kernel: ACPI: AC Adapter [AC] (on-line)
``` Explain Code
            - The archive file `~/log_archive.tgz` should exist and contain all files from `~/logs/`.
            - 
            - # **Summary**
            - In this challenge, you practiced important file management and text processing tasks that simulate log analysis and archiving. You learned how to search for specific entries in files, export the results, and create a compressed archive of a directory. These skills are valuable for various tasks in system administration and data analysis, even when working with limited privileges. The challenge reinforced your understanding of file operations and command-line tools in a Linux environment.
            - # **Step 1 Solution**
                - To complete this challenge, follow these steps:
                    1. Search for ACPI messages and export them:
                        - `grep ACPI ~/logs/messages > ~/acpi_logs`
                        - This command searches for "ACPI" in `~/logs/messages` and redirects the output to `~/acpi_logs`.
                    2. Create an archive of `~/logs`:
                        - `tar czf ~/log_archive.tgz ~/logs/`
                        - This command creates a gzipped tar archive (`czf` options) of `~/logs/` and saves it as `~/log_archive.tgz`.
                - Explanation:
                    - The `grep` command searches for lines containing "ACPI" in the specified file.
                    - The `>` operator redirects the output to a new file.
                    - The `tar` command is used for archiving files. The options `c` (create), `z` (gzip), and `f` (file) tell tar to create a gzipped archive file.
        - Log in and Switch Users
            - # **Introduction**
            - In Linux systems, it's common to have multiple users sharing the same environment. As a system administrator, you need to be proficient in managing user accounts and switching between them. This challenge will test your skills in user management and authentication in a Linux environment.
            - ## **Environment**
            - LabEx uses Red Hat Universal Base Image 9 (UBI9) to simulate the exam environment. It may not be identical to the actual RHCSA exam environment, but it provides a good representation of the tasks you'll encounter.
            - There are two users in the environment:
                - `labex`: A standard user with sudo privileges, password: `labex`.
                - `root`: The system administrator, password: `redhat`.
            - The challenge features real exam questions, along with explanations, requirements, and automated verification scripts to help you confirm task completion. It effectively simulates the knowledge areas covered in the RHCSA exam.
            - This is a Challenge, which differs from a Guided Lab in that you need to try to complete the challenge task independently, rather than following the steps of a lab to learn. Challenges are usually a bit difficult. If you find it difficult, you can discuss with Labby or check the solution. Historical data shows that this is a beginner level challenge with a 93% pass rate. It has received a 100% positive review rate from learners.
            - 
            - # **Switch Users and Create a New Account**
            - This step will guide you through the process of switching between users and creating a new user account.
            - ## **Tasks**
                - Switch to the `root` user using `sudo`
                - Create a new user named `projectuser`
                - Switch to the `projectuser` account
                - Return to the `labex` user account
            - ## **Requirements**
                - You are already logged in as the `labex` user
                - All operations should be performed in the terminal
                - Use the `sudo` command to switch to the `root` user
                - Create the `projectuser` with a home directory in `/home/projectuser`
                - Set the password for `projectuser` to `project123`
                - Use the `su` command to switch between users
                - Ensure you end up logged in as the `labex` user
            - ## **Example**
            - After completing the tasks, you should be able to see the following output when running the `whoami` command:
            - `labex    pts/0        2023-08-28 10:00 (:0)` Explain Code
            - 
            - # **Summary**
            - In this challenge, you practiced essential user management skills in a Linux environment. You learned how to switch between users using `sudo` and `su` commands, create a new user account with a specified home directory, and set user passwords. These skills are crucial for system administrators managing multi-user systems, ensuring proper user isolation, and maintaining system security.
            - # **Step 1 Solution**
                - Here's a step-by-step solution to complete this challenge:
                    1. You are already logged in as the `labex` user when you start the challenge.
                    2. Switch to the `root` user using `sudo`:
                        - `sudo -i`
                        - Enter the password for `labex` when prompted.
                    3. Create a new user named `projectuser`:
                        - `useradd -m -d /home/projectuser projectuser`
                        - This command creates a new user with a home directory in `/home/projectuser`.
                    4. Set the password for `projectuser`:
                        - `passwd projectuser`
                        - Enter `project123` as the password when prompted.
                    5. Switch to the `projectuser` account:
                        - `su - projectuser`
                        - Enter the password `project123` when prompted.
                    6. Return to the `labex` user account:
                        - `exit`
                        - This will return you to the root user. Then, exit again to return to the `labex` user:
                        - `exit`
                - Now you should be back logged in as the `labex` user. You can verify this by running the `whoami` command.
        - Create and Extract Tar Archives
        - Implement Hard Links in Linux
        - Create and Manipulate Symbolic Links
        - Manage File Permissions
        - 
    2. **Create Simple Shell Scripts**
        - Process Arguments in Bash Scripts
        - Create a Conditional Shell Script
        - Create Shell Script With Inputs
        - Create Shell Scripts to Process Command Output
        - Create Shell Scripts With Loops
    3. **Operate Running Systems**
        - Adjust Process Scheduling
        - Locate and Interpret System Log Files
        - Manage Tuning Profiles
        - Preserve System Journals
        - Start, Stop, and Check the Status of Network Services
    4. **Configure Local Storage**
        - Add New Partitions and Logical Volumes
        - Assign Physical Volumes to Volume Groups
        - Configure File Systems by UUID
        - Create and Delete Logical Volumes
        - List, Create, and Delete Partitions on MBR and GPT Disks
    5. **Create And Configure File Systems**
        - Configure Autofs
        - Create and Configure File Systems
        - Create Set-Gid Directories for Collaboration
        - Diagnose and Correct File Permission Problems
        - Extend Existing Logical Volumes
        - Mount and Unmount Network File Systems Using NFS
    6. **Deploy, Configure, And Maintain Systems**
        - Configure System to Boot Into a Specific Target Automatically
        - Configure Time Service Clients
        - Install and Update Software Packages
        - Modify the System Bootloader
        - Schedule Tasks Using at and Cron
        - Start and Configure Services
    7. **Manage Basic Networking**
        - Configure Hostname Resolution
        - Configure IPv4 and IPv6 Addresses
        - Configure Network Services to Start Automatically at Boot
        - Restrict Network Access Using firewall-cmd
    8. **Manage Users And Groups**
        - Change Passwords and Adjust Password Aging for Local User Accounts
        - Configure Superuser Access
        - Create and Manage Local Groups
        - Create and Manage Local User Accounts
    9. **Manage Security**
        - Set SELinux Mode
        - Modify SELinux Boolean Settings
        - Configure Firewall Using Firewall-CMD/Firewalld
        - Configure Key-Based Authentication for SSH
        - Diagnose and Address SELinux Policy Violations
        - Identify SELinux File Context
        - Manage Default File Permissions
        - Manage SELinux Port Labels
        - Restore Default File Contexts
    10. **Manage Containers**
        - Find and Retrieve Container Images From a Remote Registry
        - Inspect Container Images
        - Manage Containers: Basic Operations
        - Run a Service Inside a Container
        - Manage Containers With Podman and Skopeo
        - Attach Persistent Storage to a Container
        - Configure a Podman Container to Start Automatically as a systemd User Service
