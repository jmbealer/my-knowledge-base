# What Python Line Structure: WIP

A Python program is divided into a number of logical lines and every logical line is terminated by the token NEWLINE.

.Physical lines
A physical line is a sequence of characters terminated by an end-of-line sequence.
Physical Line terminated (end-of-line) sequences; ASCII LF (linefeed), ASCII CR LF (return followed linefeed), ASCII CR (return) character.
The end of input also serves as an implicit terminator for the final physical line.

.Logical lines
The end of a logical line is represented by the token NEWLINE.
Statements cannot cross logical line boundaries except where NEWLINE is allowed by the syntax (e.g., between statements in compound statements).
A logical line is constructed from one or more physical lines by following the explicit or implicit line joining rules.

.Explicit line joining
Two or more physical lines may be joined into logical lines using backslash characters (\).

if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        return 1

A line ending in a backslash cannot carry a comment.
A backslash does not continue a comment.
A backslash does not continue a token except for string literals.
str = 'This is a \
  string example' # This is a string example
(i.e., tokens other than string literals cannot be split across physical lines using a backslash).
A backslash is illegal elsewhere on a line outside a string literal.

.Implicit line joining
Expressions in parentheses, square brackets or curly braces can be split over more than one physical line without using backslashes.

month_names=['January', 'Feb', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December']

Implicitly continued lines can carry comments.
The indentation of the continuation lines is not important.
Blank continuation lines are allowed.
There is no NEWLINE token between implicit continuation lines.
Implicitly continued lines can also occur within docstrings

str = """This is
    a string
    example""" # 'This is \na string \nexample'

Docstrings cannot carry comments.

.Blank lines
Blank logical lines are ignored (no NEWLINE token is generated).
Blank logical line contains only spaces, tabs, form-feeds and possibly a comment.

