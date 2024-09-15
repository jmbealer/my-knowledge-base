== Python Datetime WIP
Python Dates

A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
Example

Import the datetime module and display the current date:
import datetime

x = datetime.datetime.now()
print(x)
Date Output

When we execute the code from the example above the result will be:
2020-11-01 02:04:15.900099

The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:
Example

Return the year and name of weekday:
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
Creating Date Objects

To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.
Example

Create a date object:
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
The strftime() Method

The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
Example

Display the name of the month:
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

A reference of all the legal format codes:
Directive 	Description 	Example 	Try it
%a 	Weekday, short version 	Wed 	
%A 	Weekday, full version 	Wednesday 	
%w 	Weekday as a number 0-6, 0 is Sunday 	3 	
%d 	Day of month 01-31 	31 	
%b 	Month name, short version 	Dec 	
%B 	Month name, full version 	December 	
%m 	Month as a number 01-12 	12 	
%y 	Year, short version, without century 	18 	
%Y 	Year, full version 	2018 	
%H 	Hour 00-23 	17 	
%I 	Hour 00-12 	05 	
%p 	AM/PM 	PM 	
%M 	Minute 00-59 	41 	
%S 	Second 00-59 	08 	
%f 	Microsecond 000000-999999 	548513 	
%z 	UTC offset 	+0100 	
%Z 	Timezone 	CST 	
%j 	Day number of year 001-366 	365 	
%U 	Week number of year, Sunday as the first day of week, 00-53 	52 	
%W 	Week number of year, Monday as the first day of week, 00-53 	52 	
%c 	Local version of date and time 	Mon Dec 31 17:41:00 2018 	
%x 	Local version of date 	12/31/18 	
%X 	Local version of time 	17:41:00 	
%% 	A % character 	% 	

There are various ways Python supplies date and time feature to add to the program. Python's Time and calendar module help in tracking date and time. Also, the 'DateTime' provides classes for controlling date and time in both simple and complex ways.
There are two different date and time objects in Python. These are:

    naive
    aware

The differences between 'naive' and 'aware' objects are:

    The 'aware' object holds the details about time-zone and daylight saving information, whereas naïve objects do not have that feature.
    Naive objects are easy to understand and to work with.

Table of Contents
1. Defining Tick
2. Timetuple In Python
3. Timedelta Object
4. Program To Get Current Time
5. Calendar Of A Month

As we all can make an idea that time intervals have to be represented in floating-point numbers. Tick signifies the floating-point numbers in units of seconds in Python. Particular instants of time are represented in seconds from 12:00 am, 1st of January, of the year 1990. A popular module name 'time' is available, which provides functions that let's programmer work with the time and made conversion between time-representation possible.

The pre-defined function time.time() is used to return the current time of the system.

The daytime module exports the constants listed below:

    MINYEAR
    MAXYEAR

Two programs are shown showing the use of two different modules:

import time;

ticktock = time.time();

print("Number of ticks:", ticktock)

Number of ticks: 1465927104.951356

Another program showing datetime module:

from datetime import datetime

presentime = datetime.now()

print(" NOW THE TIME IS:", presentime)

print("Todays Date is:", presentime.strftime('%Y-%m-%d') )

print("Year is:", presentime.year)

print("MOnth is:", presentime.month)

print("Day is:", presentime.day)

NOW THE TIME IS: 2016-06-14 18:01:25.831269
Todays Date is: 2016-06-14
Year is: 2016
MOnth is: 6
Day is: 14

Python usually handles time's function as a tuple with nine numbers starting from zero (0) to eight (8).
0	Four digit number (year)	2016
1	Months	1 - 12
2	Day	1 - 31
3	Hour	0 - 23
4	Minute	0 - 59
5	Second	0 - 60
6	Days of the week	0 - 6 (where Zero designates Monday)
7	Days of a year	1 - 366
8	Daylight saving	-1, 0, 1, -1

It is used to represent duration, i.e., the difference between two dates and or times.  For invoking this, the syntax is:

datetime.timedelta([days, [,seconds [,microseconds [,milliseconds [, minutes [,hours [,weeks]]]]]])

In the above scenario, all arguments are optional, and their default value is zero (0).

import time;

curtime = time.localtime(time.time())

print("Current Time is:", curtime)

Current Time is: time.struct_time(tm_year=2016, tm_mon=6, tm_mday=14, tm_hour=0, tm_min=4, tm_sec=49, tm_wday=1, tm_yday=166, tm_isdst=0)

This facility is provided by the "calendar" module, which offers a wide range of methods to deal with monthly calendars. A simple program showing how to use:

import calendar

calndr = calendar.month(2016, 6)

print("The calendar for the month June of Year 2016 is:")

print (calndr)

The calendar for the month June of Year 2016 is:
     June 2016
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30


