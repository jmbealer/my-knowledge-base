# guix<sub>refermanual</sub>

## Skeleton

### 1 Introduction

GNU Guix is a package management tool Guix makes it easy for:
unprivileged user to install, upgrade, or remove software packages to
roll back to a previous package set to build packages from sources
generally assist with the creation and maintenance of software
environments

1.  Managing Software the Guix Way

2.  GNU Distribution

### 2 Installation

1.  Binary Installation

2.  Requirements

3.  Running the Test Suite

4.  Setting Up the Daemon

    1.  Build Environment Setup

    2.  Using the Offload Facility

    3.  SELinux Support

        1.  Installing the SELinux policy

        2.  Limitations

5.  Invoking guix-daemon

6.  Application Setup

    1.  Locales

    2.  Name Service Switch

    3.  X11 Fonts

    4.  X.509 Certificates

    5.  Emacs Packages

7.  Upgrading Guix

### 3 System Installation

1.  Limitations

2.  Hardware Considerations

3.  USB Stick and DVD Installation

    1.  Copying to a USB Stick

    2.  Burning on a DVD

    3.  Booting

4.  Preparing for Installation

5.  Guided Graphical Installation

6.  Manual Installation

    1.  Keyboard Layout, Networking, and Partitioning

        1.  Keyboard Layout

        2.  Networking

        3.  Disk Partitioning

    2.  Proceeding with the Installation

7.  After System Installation

8.  Installing Guix in a Virtual Machine

9.  Building the Installation Image

10. Building the Installation Image for ARM Boards

### 4 Getting Started

### 5 Package Management

1.  Features

2.  Invoking guix package

3.  Substitutes

    1.  Official Substitute Servers

    2.  Substitute Server Authorization

    3.  Getting Substitutes from Other Servers

    4.  Substitute Authentication

    5.  Proxy Settings

    6.  Substitution Failure

    7.  On Trusting Binaries

4.  Packages with Multiple Outputs

5.  Invoking guix gc

6.  Invoking guix pull

7.  Invoking guix time-machine

8.  Inferiors

9.  Invoking guix describe

10. Invoking guix archive

### 6 Channels

1.  Specifying Additional Channels

2.  Using a Custom Guix Channel

3.  Replicating Guix

4.  Channel Authentication

5.  Channels with Substitutes

6.  Creating a Channel

7.  Package Modules in a Sub-directory

8.  Declaring Channel Dependencies

9.  Specifying Channel Authorizations

10. Primary URL

11. Writing Channel News

### 7 Development

1.  Invoking guix shell

2.  Invoking guix environment

3.  Invoking guix pack

4.  The GCC toolchain

5.  Invoking guix git authenticate

### 8 Programming Interface

1.  Package Modules

2.  Defining Packages

    1.  package Reference

    2.  origin Reference

3.  Defining Package Variants

4.  Build Systems

5.  Build Phases

6.  Build Utilities

    1.  Dealing with Store File Names

    2.  File Types

    3.  File Manipulation

    4.  File Search

    5.  Program Invocation

    6.  Build Phases

    7.  Wrappers

7.  Search Paths

8.  The Store

9.  Derivations

10. The Store Monad

11. G-Expressions

12. Invoking guix repl

### 9 Utilities

1.  Invoking guix build

    1.  Common Build Options

    2.  Package Transformation Options

    3.  Additional Build Options

    4.  Debugging Build Failures

2.  Invoking guix edit

3.  Invoking guix download

4.  Invoking guix hash

5.  Invoking guix import

6.  Invoking guix refresh

7.  Invoking guix style

8.  Invoking guix lint

9.  Invoking guix size

10. Invoking guix graph

11. Invoking guix publish

12. Invoking guix challenge

13. Invoking guix copy

14. Invoking guix container

15. Invoking guix weather

16. Invoking guix processes

### 10 System Configuration

1.  Using the Configuration System

    1.  Bootloader

    2.  Globally-Visible Packages

    3.  System Services

    4.  Instantiating the System

    5.  The Programming Interface

2.  operating-system Reference

3.  File Systems

    1.  Btrfs file system

4.  Mapped Devices

5.  Swap Space

6.  User Accounts

7.  Keyboard Layout

8.  Locales

    1.  Locale Data Compatibility Considerations

9.  Services

    1.  Base Services

    2.  Scheduled Job Execution

    3.  Log Rotation

    4.  Networking Setup

    5.  Networking Services

    6.  Unattended Upgrades

    7.  X Window

    8.  Printing Services

    9.  Desktop Services

    10. Sound Services

    11. Database Services

    12. Mail Services

    13. Messaging Services

    14. Telephony Services

    15. File-Sharing Services

    16. Monitoring Services

    17. Kerberos Services

    18. LDAP Services

    19. Web Services

    20. Certificate Services

    21. DNS Services

    22. VPN Services

    23. Network File System

    24. Continuous Integration

    25. Power Management Services

    26. Audio Services

    27. Virtualization Services

    28. Version Control Services

    29. Game Services

    30. PAM Mount Service

    31. Guix Services

    32. Linux Services

    33. Hurd Services

    34. Miscellaneous Services

10. Setuid Programs

11. X.509 Certificates

12. Name Service Switch

13. Initial RAM Disk

14. Bootloader Configuration

15. Invoking guix system

16. Invoking guix deploy

17. Running Guix in a Virtual Machine

    1.  Connecting Through SSH

    2.  Using virt-viewer with Spice

18. Defining Services

    1.  Service Composition

    2.  Service Types and Services

    3.  Service Reference

    4.  Shepherd Services

    5.  Complex Configurations

### 11 Home Configuration

1.  Declaring the Home Environment

2.  Configuring the Shell

3.  Home Services

    1.  Essential Home Services

    2.  Shells

    3.  Scheduled User's Job Execution

    4.  Managing User Daemons

    5.  Desktop Home Services

4.  Invoking guix home

### 12 Documentation

### 13 Installing Debugging Files

1.  Separate Debug Info

2.  Rebuilding Debug Info

### 14 Security Updates

### 15 Bootstrapping

1.  The Reduced Binary Seed Bootstrap

2.  Preparing to Use the Bootstrap Binaries

3.  Building the Build Tools

4.  Building the Bootstrap Binaries

5.  Reducing the Set of Bootstrap Binaries

### 16 Porting to a New Platform

### 17 Contributing

1.  Building from Git

2.  Running Guix Before It Is Installed

3.  The Perfect Setup

4.  Packaging Guidelines

    1.  Software Freedom

    2.  Package Naming

    3.  Version Numbers

    4.  Synopses and Descriptions

    5.  Snippets versus Phases

    6.  Emacs Packages

    7.  Python Modules

        1.  Specifying Dependencies

    8.  Perl Modules

    9.  Java Packages

    10. Rust Crates

    11. Fonts

5.  Coding Style

    1.  Programming Paradigm

    2.  Modules

    3.  Data Types and Pattern Matching

    4.  Formatting Code

6.  Submitting Patches

    1.  Configuring Git

    2.  Sending a Patch Series

7.  Tracking Bugs and Patches

    1.  The Issue Tracker

    2.  Debbugs User Interfaces

    3.  Debbugs Usertags

8.  Commit Access

    1.  Applying for Commit Access

    2.  Commit Policy

    3.  Addressing Issues

    4.  Commit Revocation

    5.  Helping Out

9.  Updating the Guix Package

10. Translating Guix

### 18 Acknowledgments

### A GNU Free Documentation License

### Concept Index

### Programming Index
