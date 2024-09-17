---
title: CompTIA-IT-Fundamentals
author: Justin Bealer
date_created: 2023-11-16, 04-00-39
date_modified: 2024-09-17, 09-29-55
reference: 
description: 
aliases: 
tags: 
---
# CompTIA-IT-Fundamentals
= CompTIA IT Fundamentals (ITF+) Exam FC0-U61
   
== 1.0 IT Concepts and Terminology 17%
        
=== 1.1 Compare and Contrast Notational(numeral) Systems
            
            Binary (Base-2) is a positional numeral (notation) system with a radix (base) of two (2^x) that uses two distinct symbols (digits) "0" (zero)(off) and "1" (one)(on) 
            is fundamental building block of all computer operation and data storage
            
                
                bit (binary digit) is the smallest (basic) unit of information (data) storage 
                a bit is the symbols (digits) 0 (off) or 1 (on) in binary
                
                can be in one of two states off or on like a light bulb anything with two separate states can store 1 bit
                
                Nibble is four-bits (e.g. 0101) or half-byte (half a byte) 2^4=16 can represent a hex digit (hexadecimal digit) 
                
                byte (binary terms) is eight-bits (8-bits = 1-byte) (e.g. 0101 0101) 
                a single character in a plain-text file requires a byte to store it (e.g.  'A' or 'x' or '$')
                all larger units of information uses multiples of a byte to measure
                
                x bits = 2^x values Im general add 1-bit double the number of values
                    1 bits = 2^1 values = 0 1 (0-1) 2 different values
                    2 bits = 2^2 values = 00 01 10 11 (0-3) 4 different values
                    3 bits = 2^3 values = 000 001 010 011 100 101 110 111 (0-7) 8 different values
                    4 bits = 2^4 values = 0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111(0-15) 16 different values
                    5 bits = 2^5 values = (0-31) 32 different values
                    6 bits = 2^6 values = (0-63) 64 different values
                    7 bits = 2^7 values = (0-127) 128 different values
                    8 bits = 2^8 values = (0-255) 256 different values
                binary number, follow it with a little 2 like this: 1012
            
            Hexadecimal (Base-16) (hex) is a positional numeral (notation) system with a radix (base) of sixteen (16^n) that uses sixteen distinct symbol (digits) 0-9 (equivalent to values 0–9 in decimal notation) and a–f or A–F (equivalent to values 10–15 in decimal notation). 
            Thus, a very long binary value can be represented by a much shorter hex value
            a few places where hex values are used 
                expressing (hex) color values in HTML (Hypertext Markup Language), (CSS) Cascading Style Sheets, and X Window System
                Internet Protocol version 6 (IPv6) addresses
                Media Access Control (MAC) addresses for networking devices
                
                Hex Color Values (web colors) are display colors (RGB) expressed in hex triplet (three-byte hexadecimal number) e.g. #00-00-00 three groups of two hex digits.
                Byte-1 represents the red value #"00"0000
                    red is #"FF"0000 (100%red 0%green 0%blue) (maximum red, no green, no blue)
                Byte-2 represents the green values #00"00"00
                    green is #00"FF"00 (0%red 100%green 0%blue) (no red, maximum green, no blue)
                Byte-3 represents the blue values #0000"00"
                    blue is #0000"FF" (0%red 0%green 100%blue) (no red, no green, maximum blue)
                white is #FFFFFF (100%red 100%green 100%blue)(maximum red, maximum green, and maximum blue)
                black is #000000 (0%red 0%green 0%blue) (no red, no blue, and no green)
                orange is #FFA500 (100%red 64.8%green 0%blue)
                
                Internet Protocol version 6 (IPv6) addresses are replacing the older Internet Protocol version 4 (IPv4) addresses
                IPv6 addresses are represented as eight groups of four hexadecimal digits (two-bytes hexadecimal number) with the groups being separated by colons e.g. 2001:0db8:0000:0042:0000:8a2e:0370:7334
                offering 128-bit addresses comprising eight 16-bit sections to prevent address exhaustion and easier configuration
            
            Decimal (Base-10) is a positional numeral (notation) system with a radix (base) of ten (10^n) that uses ten distinct symbols (digits) 0-9 
            is the standard system for denoting integer and non-integer numbers
            
            Data Representation in computer is text stored as numeric codes mapped to characters to make them understandable
            two common character sets data representation is ASCII and Unicode
                
                (standard) ASCII (American Standard for Information Interchange) encoding, representation, and handling of text expressed in Latin (English)'s writing systems. encodes 128 specified characters into seven-bit integers. Includes uppercase (A-Z), lowercase (a-z) Latin (English) alphabet, number (0-9), punctuation characters (marks), and some nonprintable control characters
                    
                    Extended ASCII includes the standard ASCII character set (values 0-127) plus an extended character set (values 128-255) sometimes refer as (ANSI) which stand for American National Standards Institute
                    
                    To enter an ASCII or ANSI character directly from the keyboard, press and hold down an Alt key and type the character’s number on the keypad (you cannot use the numbers at the top of the keyboard)
                    
                    The problem with both standard and extended ASCII character sets is that they cannot display characters used by languages that don’t use the Latin (English) alphabet (A–Z).
                
                Unicode encoding, representation, and handling of text expressed in most of the world's writing systems
                    
                    Replaced (supports) ASCII and extended ASCII character sets (both Latin and non-Latin alphabets and special characters)
                    Unicode Transformation Format (UTF) 
                    Universal Coded Character Set (UCS)
                
=== 1.2 Compare and Contrast Fundamental Data Types and their Characteristics
            
            Char (character) is a data type that refers to a single character or a single-character variable e.g. 1 2 A Z x # !
            a char is equal to 1 byte
            
            String is a series of character (char) that is interpreted literally by a script, such as "Abraham Lincoln" or "THX1138"
            computers programs usually connect a string to a variable
            if a string is composed of only numbers such as 1138, is usually classified as an integer
            
            Numbers the common data types used for numbers Integers and Floats
                
                Integer (int) is a positive or negative whole number (a number with no decimal points or fractions) 
                
                Float (float-point number) is a number that contains up to seven digits and has at least one decimal place
                
                    a float is a single-precision, floating-point, 32-bit value.
                
                    Floats can also be expressed using powers of ten or powers of two. This way, a fixed number of digits can be used to express a very wide range of numeric values
                    
                    Numbers with floating-point decimals that contain more than seven digits, up to 15 digits total, are known as doubles, or double-precision floating-point numbers. A double is a 64-bit double-precision data type.
                    
                    Singe-precision and double-precision floating point numbers are actually approximations of the true value of a number because of the rounding that takes place when non-integer numbers are used.
            
            Boolean values are used in Boolean Logic, which evaluates whether a given condition is true (1) or false (0)
                these values are binary
                In computers and other electronics devices, Boolean Logic is used to determine if a circuit is charged or on (1) or not charged or off (0)
                Boolean logic can be used for searches 
                Boolean logic includes the following comparisons: AND, OR, NOT, and XOR, among others.
                AND, OR, NOT, and XOR are used to compare two values.
                    
                    AND: If both values 1 and 2 exist in a statement, the statement is TRUE. If only value 1 or value 2 exists in a statement, the statement is FALSE.

                    OR: If either value 1 or 2 exists in a statement, the statement is TRUE.
                    
                    NOT: If neither value 1 nor 2 exists in a statement, the statement is TRUE. If either or both exist, the statement is FALSE.
                    
                    XOR: If either value 1 or value 2 exists in a statement, the statement is true. If both exist, or if neither exists, the statement is FALSE.
                
                Boolean logic is often used in performing searches online and elsewhere. Here are the results of a search of a local library’s book and media holdings
                
                Boolean algebra applies Boolean logic to solve equations, such as the following:
                Boolean logic can be visualized using Venn diagrams.
                
=== 1.3 Illustrate the Basics of Computing and Processing
=== 1.4 Explain the Value of Data and Information
=== 1.5 Compare and Contrast Units of Measure
=== 1.6 Explain the Troubleshooting Methodology
== 2.0 Infrastructure 22%
== 3.0 Application and Software 18%
== 4.0 Software Development 12%
== 5.0 Database Fundamentals 11%
== 6.0 Security 20%
== Acronym
What is ?
What are ?
