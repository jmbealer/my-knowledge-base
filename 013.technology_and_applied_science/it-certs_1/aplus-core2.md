# CompTIA A+ Core 2 (220-1202) V15 Objectives

## About the Exam

Candidates are encouraged to use this document to help prepare for the CompTIA
A+ 220-1202 certification exam. In order to receive the CompTIA A+
certification, you must pass two exams: Core 1 (220-1201) and Core 2 (220-1202).
The CompTIA A+ Core 1 (220-1201) and Core 2 (220-1202) certification exams will
verify the successful candidate has the knowledge and skills required to: • • •
• • •

Install, configure, and maintain computer equipment, mobile devices, and
software for end users Service components based on customer requirements
Understand networking basics and apply basic cybersecurity methods to mitigate
threats Properly and safely diagnose, resolve, and document common hardware and
software issues Apply troubleshooting skills and provide customer support using
appropriate communication skills Understand the basics of scripting, cloud
technologies, virtualization, and multi-OS deployments in corporate environments

## 1.0 Operating Systems 28%

### 1.1 Explain common operating system (OS) types and their purposes

- **{{Operating System (OS)}}**: Software managing *hardware resources and providing services*.
  - **{{Kernel}}**: Core component *managing CPU, memory, and devices*.
- **Workstation systems (OSs)**
  - **{{Windows}}**: Proprietary OS from *Microsoft dominating the desktop market*.
  - **{{Linux}}**: Open-source OS kernel *used in servers and desktops*.
  - **{{macOS}}**: Proprietary Unix-based OS *designed for Apple Macintosh computers*.
  - **{{Chrome OS}}**: Lightweight OS based *on the Chrome web browser*.
- **Mobile OSs**
  - **{{iPadOS}}**: Specialized OS optimized *for Apple tablet devices*.
  - **{{iOS}}**: Proprietary mobile OS *running on Apple iPhone devices*.
  - **{{Android}}**: Open-source mobile OS *developed by Google for various devices*.
- **Various filesystem types**
  - **{{New Technology File System (NTFS)}}**: Proprietary Windows filesystem *supporting ACLs and encryption*.
  - **{{Resilient File System (ReFS)}}**: Windows filesystem optimized *for data integrity and availability*.
  - **{{File Allocation Table 32 (FAT32)}}**: Legacy filesystem with *broad compatibility but file size limits*.
  - **{{Fourth Extended Filesystem (ext4)}}**: Standard journaling filesystem *default for many Linux distributions*.
  - **{{Extended Filesystem (XFS)}}**: High-performance 64-bit *journaling filesystem for Linux*.
  - **{{Apple File System (APFS)}}**: Optimized filesystem for *flash storage on Apple devices*.
  - **{{Extensible File Allocation Table (exFAT)}}**: Filesystem optimized for *flash drives with large files*.
  - **{{HFS+}}**: Legacy Apple filesystem *preceding APFS*.
- **Vendor life-cycle limitations**
  - **{{End-of-Life (EOL)}}**: Date when vendor *stops selling or supporting* a product.
  - **{{Update Limitations}}**: Restrictions on *receiving patches based on hardware* age.
- **{{Compatibility Concerns}}**: Issues arising when *software/hardware lacks OS support*.
  - **{{32-bit vs 64-bit}}**: Architecture difference affecting *memory addressing and app compatibility*.

### 1.2 Given a scenario, perform OS installations and upgrades in a diverse environment

- **Boot methods**
  - **{{Universal Serial Bus (USB)}}**: Booting from *removable flash storage* devices.
  - **{{Preboot Execution Environment (PXE)}}**: Booting from *network via a server* (Network boot).
  - **{{Solid-State / Flash Drives}}**: Booting from *fast non-volatile storage* media.
  - **{{Internet-Based}}**: Recovery or installation *directly from vendor cloud* servers.
  - **{{External / Hot-Swappable Drive}}**: Booting from *drives connected while system* runs.
  - **{{Internal Hard Drive (Partition)}}**: Booting from a *segmented section of local* disk.
  - **{{Multiboot}}**: Configuration allowing *selection of multiple OSs* at startup.
- **Types of installations**
  - **{{Clean Install}}**: Installation deleting *all existing data and settings*.
  - **{{In-Place Upgrade}}**: Installing newer OS *preserving files and settings*.
  - **{{Image Deployment}}**: Cloning a *pre-configured OS to multiple* machines.
  - **{{Remote Network Installation}}**: Installing OS *over the network to a client*.
  - **{{Unattended Installation}}**: Deployment using *answer files to automate* setup.
  - **{{Zero-Touch Deployment}}**: Fully automated *install requiring no user interaction*.
  - **{{Recovery Partition}}**: Dedicated drive section *containing factory restore data*.
  - **{{Repair Installation}}**: Reinstalling OS files *to fix corruption without data loss*.
  - **Other considerations**
    - **{{Third-Party Drivers}}**: Software needed for *hardware not natively supported*.
- **Partitioning**
  - **{{GUID Partition Table (GPT)}}**: Modern partitioning standard *supporting large drives and UEFI*.
  - **{{Master Boot Record (MBR)}}**: Legacy partitioning standard *limited to 2TB and 4 partitions*.
- **{{Formatting}}**: Preparing a drive *partition with a specific filesystem*.
  - **{{Full Format}}**: Wipes data and *checks drive for bad sectors*.
  - **{{Quick Format}}**: Creates filesystem *without checking for bad sectors*.
- **Upgrade considerations**
  - **{{Backup}}**: Copying data *to safe location before modifying* system.
  - **{{Compatibility Check}}**: Verifying *hardware and software meet requirements*.
- **Feature updates**
  - **{{Product Life Cycle}}**: Stages of *software from release to EOL*.

### 1.3 Compare and contrast basic features of Microsoft Windows editions

- **Windows 10 / 11 editions**
  - **{{Home}}**: Consumer edition *lacking domain and management* features.
  - **{{Pro}}**: Business edition *supporting domains, BitLocker, and RDP*.
  - **{{Pro for Workstations}}**: Optimized for *high-performance hardware and file* systems.
  - **{{Enterprise}}**: Corporate edition *with advanced security and management* (DirectAccess, AppLocker).
  - **{{N Versions}}**: Editions *without pre-installed multimedia* capabilities (Europe).
- **Feature differences**
  - **{{Domain vs. Workgroup}}**: Centralized *corporate management vs peer-to-peer* networking.
  - **{{Desktop Styles / UI}}**: Visual *interface changes between OS versions*.
  - **{{Remote Desktop Protocol (RDP)}}**: Protocol allowing *remote control of Windows systems*.
    - **Note**: Home edition can be client, but not host.
  - **{{RAM Support Limitations}}**: Maximum *memory capacity varies by edition* (e.g., Home < Pro).
  - **{{BitLocker}}**: Full-disk *encryption feature available in Pro/Enterprise*.
  - **{{Group Policy Editor (gpedit.msc)}}**: Tool for *managing local or domain* policies.
    - **Note**: Not available in Home edition.
- **Upgrade paths**
  - **{{In-Place Upgrade}}**: Moving to newer *edition while keeping files* intact.
  - **{{Clean Install}}**: Installing fresh *OS on wiped partition*.
- **Hardware requirements**
  - **{{Trusted Platform Module (TPM) 2.0}}**: Security chip *required for Windows 11*.
  - **{{Unified Extensible Firmware Interface (UEFI)}}**: Modern firmware *required for Secure Boot*.
  - **{{Processor Requirements}}**: Specific *CPU generations supported by OS*.
  - **{{Storage / RAM Minimums}}**: Baseline *resources needed to run OS*.

### 1.4 Given a scenario, use Microsoft Windows operating system features and tools

- **{{Task Manager (taskmgr.exe)}}**: Tool for *monitoring apps, services, and performance*.
  - **{{Services}}**: Managing *background processes supporting system* functions.
  - **{{Startup}}**: Managing *programs launching automatically* at boot.
  - **{{Performance}}**: Real-time *graphs of CPU, RAM, and disk* usage.
  - **{{Processes}}**: Viewing *active applications and background* tasks.
  - **{{Users}}**: Monitoring *active sessions and resource* consumption.
- **{{Microsoft Management Console (MMC)}}**: Framework for *hosting administrative tools* called snap-ins.
  - **{{Event Viewer (eventvwr.msc)}}**: Viewing *system, security, and application* logs.
  - **{{Disk Management (diskmgmt.msc)}}**: Managing *drives, partitions, and volumes*.
  - **{{Task Scheduler (taskschd.msc)}}**: Automating *tasks to run at specific* times.
  - **{{Device Manager (devmgmt.msc)}}**: Managing *hardware drivers and device* status.
  - **{{Certificate Manager (certmgr.msc)}}**: Managing *digital certificates for users* and systems.
  - **{{Local Users and Groups (lusrmgr.msc)}}**: Managing *local accounts and permissions* (Pro+).
  - **{{Performance Monitor (perfmon.msc)}}**: Advanced *tracking of system performance* metrics.
  - **{{Group Policy Editor (gpedit.msc)}}**: Managing *configuration settings for users* and computers.
- **Additional tools**
  - **{{System Information (msinfo32.exe)}}**: Detailed *report of hardware and software* specs.
  - **{{Resource Monitor (resmon.exe)}}**: Detailed *view of CPU, disk, network, and memory* usage.
  - **{{System Configuration (msconfig.exe)}}**: Managing *boot options and startup* services.
  - **{{Disk Cleanup (cleanmgr.exe)}}**: Removing *temporary and unnecessary files* from drives.
  - **{{Disk Defragmenter (dfrgui.exe)}}**: Optimizing *file placement on HDDs* for speed.
  - **{{Registry Editor (regedit.exe)}}**: Viewing and *editing the Windows configuration* database.
  - **{{Open Database Connectivity (ODBC)}}**: Tool for *configuring database connections* and drivers.

### 1.5 Given a scenario, use the appropriate Microsoft command-line tools

- **Navigation**
  - **{{cd (chdir)}}**: Command to *change the current directory*.
  - **{{dir}}**: Command to *list files and subdirectories*.
  - **{{..}}**: Command to *move up one directory* level.
- **Network**
  - **{{ipconfig}}**: Displays *IP address and network* configurations.
    - **{{ipconfig /all}}**: Shows *detailed network information* including MAC.
    - **{{ipconfig /release /renew}}**: Manually *request new IP from DHCP*.
  - **{{ping}}**: Tests *connectivity between two network* nodes.
  - **{{netstat}}**: Displays *active network connections and ports*.
  - **{{nslookup}}**: Queries *DNS to resolve domain* names.
  - **{{net use}}**: Command to *connect to shared network* resources.
  - **{{tracert}}**: Traces *the path packets take* to destination.
  - **{{pathping}}**: Combines * ping and tracert* for performance.
- **Disk management**
  - **{{chkdsk}}**: Checks *drive for file system* errors.
    - **{{chkdsk /f}}**: Fixes *errors found on the* disk.
    - **{{chkdsk /r}}**: Locates *bad sectors and recovers* data.
  - **{{format}}**: Prepares *a disk for a specific* filesystem.
  - **{{diskpart}}**: Interactive *command-line disk partitioning* tool.
- **File management**
  - **{{md (mkdir)}}**: Command to *create a new directory*.
  - **{{rd (rmdir)}}**: Command to *remove an empty directory*.
  - **{{copy}}**: Command to *copy files to another* location.
  - **{{xcopy}}**: Command to *copy files and directory* trees.
  - **{{robocopy}}**: Advanced *robust file and folder* copying.
  - **{{del (erase)}}**: Command to *delete one or more* files.
- **Informational**
  - **{{hostname}}**: Displays *the name of the* computer.
  - **{{net user}}**: Command to *manage local user accounts*.
  - **{{winver}}**: Displays *detailed Windows version information*.
  - **{{whoami}}**: Displays *current user and group* information.
  - **{{[command] /?}}**: Displays *help and usage instructions* for command.
- **OS management**
  - **{{gpupdate}}**: Manually *refreshes local and domain* policies.
  - **{{gpresult}}**: Displays *Resultant Set of Policy (RSoP)* information.
  - **{{sfc (System File Checker)}}**: Verifies *and repairs critical system* files.
  - **{{shutdown}}**: Command to *restart or power off* system.
  - **{{dism (Deployment Image Servicing and Management)}}**: Tool for *repairing and managing Windows* images.

### 1.6 Given a scenario, configure Microsoft Windows settings

- **Control Panel Applets**
  - **{{Internet Options}}**: Settings for *managing Internet Explorer/Edge* behavior (Security zones, Privacy).
  - **{{Devices and Printers}}**: Interface for *managing connected hardware* peripherals.
  - **{{Programs and Features}}**: Tool for *uninstalling or repairing* software applications.
  - **{{Network and Sharing Center}}**: Hub for *viewing and configuring network* connections.
  - **{{System}}**: View basic *hardware specifications and OS* information.
  - **{{Windows Defender Firewall}}**: Configuring *rules to block or allow* network traffic.
  - **{{Mail}}**: Configuring *Outlook profiles and email* accounts.
  - **{{Sound}}**: Managing *audio devices and playback* settings.
  - **{{User Accounts}}**: Managing *local users and account* types.
  - **{{Device Manager}}**: Managing *drivers and troubleshooting hardware* issues.
  - **{{Indexing Options}}**: Configuring *search service for faster* file retrieval.
  - **{{Administrative Tools}}**: Collection of *advanced system management* utilities.
  - **{{File Explorer Options}}**: Customizing *how files and folders* are displayed.
    - **{{View Hidden Files}}**: Toggling visibility of *system and hidden* items.
    - **{{Hide Extensions}}**: Option to *mask file type suffixes* (e.g., .txt).
  - **{{Power Options}}**: Managing *energy consumption and sleep* settings.
    - **{{Hibernate}}**: Saving state to *disk and powering off* completely.
    - **{{Sleep / Suspend}}**: Low-power state *keeping session in RAM*.
    - **{{Standby}}**: Legacy term *synonymous with Sleep* mode.
    - **{{Fast Startup}}**: Hybrid sleep mode *speeding up boot* times.
    - **{{USB Selective Suspend}}**: Disabling power to *idle USB ports*.
  - **{{Ease of Access Center}}**: Settings for *accessibility and assistive* technology.
- **Windows Settings (Modern UI)**
  - **{{Time and Language}}**: Configuring *date, time, and region* preferences.
  - **{{Update and Security}}**: Managing *Windows Update, Defender, and Backup*.
  - **{{Personalization}}**: Customizing *desktop background, colors, and themes*.
  - **{{Apps}}**: Managing *installed software and default* applications.
  - **{{Privacy}}**: Controlling *app permissions and data* sharing.
  - **{{System}}**: Display, *sound, notifications, and power* settings.
  - **{{Devices}}**: Bluetooth, *printers, and mouse* settings.
  - **{{Network and Internet}}**: Wi-Fi, *Ethernet, VPN, and proxy* settings.
  - **{{Gaming}}**: Configuring *Game Mode and Game Bar* features.
  - **{{Accounts}}**: Managing *sign-in options and sync* settings.

### 1.7 Given a scenario, configure Microsoft Windows networking features on a client/desktop

- **{{Domain Joined vs. Workgroup}}**: Centralized *management via Active Directory* vs decentralized peer-to-peer.
  - **{{Shared Resources}}**: Folders and devices *accessible to other network* users.
  - **{{Printers}}**: Networked devices *available for shared output*.
  - **{{File Servers}}**: Dedicated systems *hosting shared data storage*.
  - **{{Mapped Drives}}**: Assigning a *local drive letter* to a network share.
- **{{Local OS Firewall Settings}}**: Controlling traffic *entering and leaving the* computer.
  - **{{Application Restrictions}}**: Rules blocking *specific programs from network* access.
  - **{{Exceptions}}**: Rules allowing *traffic that is normally* blocked.
  - **{{Configuration}}**: Setting rules *via Control Panel or* PowerShell.
- **Client network configuration**
  - **{{IP Addressing Scheme}}**: Structure defining *host and network ID* allocation.
  - **{{DNS Settings}}**: Configuring *servers used for name* resolution.
  - **{{Subnet Mask}}**: Bitmask separating *IP address into network* and host.
  - **{{Gateway}}**: Router providing *access to external networks*.
  - **{{Static vs. Dynamic}}**: Manual *IP assignment vs automated* DHCP.
- **Establish network connections**
  - **{{Virtual Private Network (VPN)}}**: Encrypted tunnel *providing secure remote access*.
  - **{{Wireless (Wi-Fi)}}**: Connecting via *radio waves to an* Access Point.
  - **{{Wired (Ethernet)}}**: Connecting via *physical cables to a* switch.
  - **{{WWAN (Cellular)}}**: Connecting via *mobile carrier data networks*.
- **{{Proxy Settings}}**: Configuring an *intermediary server for internet* access.
- **{{Public Network vs. Private Network}}**: Profiles determining *discovery and sharing settings*.
- **{{File Explorer Navigation}}**: Browsing network *shares via UNC paths* (\\Server\Share).
- **{{Metered Connections}}**: Setting limits *to restrict background data* usage.

### 1.8 Explain common features and tools of the macOS/desktop operating system

- **Installation and uninstallation of applications**
  - **File types**
    - **{{.dmg (Disk Image)}}**: Mountable virtual *disk containing software installers*.
    - **{{.pkg (Package)}}**: Installer script *automating file placement* and config.
    - **{{.app (Application Bundle)}}**: Directory appearing *as a single executable* file.
  - **{{App Store}}**: Official platform *for distributing Apple-verified* software.
  - **{{Uninstallation Process}}**: Dragging app *to Trash or using* uninstaller.
- **System folders**
  - **{{/Applications}}**: Default directory *where installed software resides*.
  - **{{/Users}}**: Directory containing *home folders for each* user.
  - **{{/Library}}**: Shared resource *files accessible to all* users.
  - **{{/System}}**: Critical files *required for macOS operation*.
  - **{{/Users/[User]/Library}}**: User-specific *preferences and application support* files.
- **{{Apple ID}}**: User account *linking all Apple services* and devices.
- **{{Corporate Restrictions}}**: Limitations managed *via MDM or configuration* profiles.
- **Best practices**
  - **{{Time Machine}}**: Built-in *utility for automated system* backups.
  - **{{Antivirus}}**: Software protecting *against macOS-specific malware*.
  - **{{Updates / Patches}}**: Installing *OS improvements via System* Settings.
  - **{{Rapid Security Response (RSR)}}**: Quick updates *addressing critical security* issues.
- **{{System Settings (Preferences)}}**: Central hub *for configuring OS options*.
  - **{{Displays}}**: Configuring *resolution, arrangement, and scaling*.
  - **{{Network}}**: Managing *Wi-Fi, Ethernet, and VPN* connections.
  - **{{Printers & Scanners}}**: Adding and *managing imaging devices*.
  - **{{Privacy & Security}}**: Controlling *app permissions and data* access.
  - **{{Accessibility}}**: Options assisting *users with disabilities*.
- **Features**
  - **{{Mission Control}}**: Overview of *all open windows and* desktops.
  - **{{Keychain}}**: System-wide *password and certificate management*.
  - **{{Spotlight}}**: System-wide *search for files and* information.
  - **{{iCloud}}**: Cloud service *syncing data across Apple* devices.
  - **{{Gestures}}**: Multi-touch *inputs on trackpad for* navigation.
  - **{{Finder}}**: Default file *manager and graphical user* interface.
  - **{{Dock}}**: Bar at *screen edge for launching* apps.
  - **{{Continuity}}**: Seamless *integration between Mac and* iOS devices.
- **Tools**
  - **{{Disk Utility}}**: Tool for *managing drives, partitions, and* volumes.
  - **{{FileVault}}**: Full-disk *encryption protecting data at* rest.
  - **{{Terminal}}**: Interface for *executing command-line* instructions.
  - **{{Force Quit}}**: Menu to *terminate unresponsive applications* immediately.

### 1.9 Identify common features and tools of the Linux client/desktop operating system

- **{{Shell}}**: Software interface *interpreting user commands* for the kernel.
  - **{{Redirection ( > )}}**: Directing *command output to a* file.
  - **{{Piping ( | )}}**: Passing *output of one command* to another.
- **File management**
  - **{{ls}}**: Command to *list directory contents*.
  - **{{pwd}}**: Displays *full path of current* working directory.
  - **{{mv}}**: Command to *move or rename* files and directories.
  - **{{cp}}**: Command to *copy files or directories*.
  - **{{rm}}**: Command to *remove files or directories* from system.
  - **{{chmod}}**: Command to *change file access permissions*.
  - **{{chown}}**: Command to *change file owner and group* assignment.
  - **{{grep}}**: Search for *text patterns within files* or output.
  - **{{find}}**: Search for *files based on specific* criteria.
- **Filesystem management**
  - **{{fsck}}**: Utility for *checking and repairing* Linux filesystems.
  - **{{mount}}**: Process of *attaching a filesystem* to the tree.
- **Administrative**
  - **{{su}}**: Command to *switch to another user* account.
  - **{{sudo}}**: Execute *commands with administrative* (root) privileges.
- **Package management**
  - **{{apt}}**: Package *manager for Debian and Ubuntu* distributions.
  - **{{dnf (yum)}}**: Package *manager for Red Hat and Fedora* distributions.
- **Network**
  - **{{ip}}**: Utility for *configuring network interfaces* and routing.
  - **{{ping}}**: Tests *connectivity to another network* host.
  - **{{curl}}**: Command-line *tool for transferring data* with URLs.
  - **{{dig}}**: Utility for *querying DNS name* servers for info.
  - **{{traceroute}}**: Displays *path packets take* to a network host.
- **Informational**
  - **{{man}}**: Displays *the manual page* for a specific command.
  - **{{cat}}**: Displays *the entire contents* of a text file.
  - **{{top}}**: Displays *real-time system resource* and process activity.
  - **{{ps}}**: Displays *information about currently active* processes.
  - **{{du}}**: Estimates *file and directory disk* space usage.
  - **{{df}}**: Displays *available and used disk* space on filesystems.
- **Text editors**
  - **{{nano}}**: Simple, *user-friendly terminal-based* text editor.
  - **{{vi / vim}}**: Advanced, *modal terminal-based* text editor.
- **Common configuration files**
  - **{{/etc/passwd}}**: Stores *local user account* information.
  - **{{/etc/shadow}}**: Stores *encrypted user passwords* and aging data.
  - **{{/etc/hosts}}**: Static *table lookup for hostnames* and IPs.
  - **{{/etc/fstab}}**: Configuration *defining filesystems to mount* at boot.
  - **{{/etc/resolv.conf}}**: Configuration *for DNS name server* resolution.
- **OS components**
  - **{{systemd}}**: The *init system and service* manager for Linux.
  - **{{Kernel}}**: Core component *managing hardware and* system processes.
  - **{{Bootloader (GRUB)}}**: Program *loading the operating system* into memory.
- **{{Root Account}}**: The *foundational administrative user* with total system access.
- **{{Desktop Environment (DE)}}**: Graphical *user interface for Linux* (GNOME, KDE).

### 1.10 Given a scenario, install applications according to requirements.

- **System requirements for applications**
  - **{{Architecture (32-bit vs. 64-bit)}}**: Ensuring software *matches the OS and hardware* architecture.
  - **{{Dedicated vs. Integrated Graphics}}**: Need for *separate GPU vs CPU-based* rendering.
  - **{{Video Random-Access Memory (VRAM)}}**: Memory dedicated *to storing image data* for GPU.
  - **{{RAM Requirements}}**: Minimum *system memory needed to run* the app.
  - **{{CPU Requirements}}**: Minimum *processing speed and core* count.
  - **{{External Hardware Tokens}}**: Physical *device required for software* authorization (Dongle).
  - **{{Storage Requirements}}**: Amount of *disk space needed for* installation.
  - **{{OS Compatibility}}**: Ensuring app *runs on specific operating system* version.
- **Distribution methods**
  - **{{Physical Media}}**: Installing from *CD, DVD, or USB* drives.
  - **{{ISO File}}**: Virtual *disk image mounted as* a drive.
  - **{{Downloadable Package}}**: Installer files *retrieved from the internet* (.exe, .msi).
  - **{{Image Deployment}}**: Applying a *pre-configured OS and app* snapshot.
- **Impact considerations**
  - **{{Device}}**: Effect on *local hardware resources and* performance.
  - **{{Network}}**: Bandwidth usage *during installation and operation*.
  - **{{Operation}}**: Effect on *workflows and user productivity*.
  - **{{Business}}**: Cost, licensing, *and compliance implications*.
- **{{Sideloading}}**: Installing apps *from outside the official* app store.

### 1.11 Given a scenario, install and configure cloud-based productivity tools

- **{{Email Systems}}**: Digital *communication platforms like Outlook* or Gmail.
- **{{Cloud Storage}}**: Off-site *data retention managed by a* provider.
  - **{{Sync / Folder Settings}}**: Mirroring *local files to the cloud* automatically.
- **{{Collaboration Tools}}**: Software *enabling multiple users to work* together.
  - **{{Spreadsheets}}**: Data *organization and analysis in rows* and columns.
  - **{{Videoconferencing}}**: Real-time *video and audio communication* over network.
  - **{{Presentation Tools}}**: Creating *visual slide decks for information* delivery.
  - **{{Word Processing Tools}}**: Creating *and editing text-based documents* digitally.
  - **{{Instant Messaging}}**: Real-time *text-based communication between users*.
- **{{Identity Synchronization}}**: Linking *on-premises identities to cloud* services.
  - **{{Single Sign-On (SSO)}}**: Using *one set of credentials* for apps.
- **{{Licensing Assignment}}**: Managing *user access to software features* based on seats.
- **{{Software as a Service (SaaS)}}**: Delivering *applications over the internet* via subscription.
- **{{Multitenancy}}**: Single *infrastructure serving multiple independent* customers.

## 2.0 Security 28%

### 2.1 Summarize various security measures and their purposes

- **Physical security**
  - **{{Bollard}}**: Sturdy *vertical post preventing vehicle* ramming.
  - **{{Access Control Vestibule (Mantrap)}}**: Double-door *system preventing unauthorized tailgating* entry.
  - **{{Badge Reader}}**: Scanner *authenticating access via ID* cards.
  - **{{Video Surveillance (CCTV)}}**: Monitoring *cameras recording physical activity* in areas.
  - **{{Alarm System}}**: Sensors *alerting to unauthorized entry* or events.
  - **{{Motion Sensor}}**: Detector *triggering response upon physical* movement.
  - **{{Door Lock}}**: Physical *mechanism restricting access to* rooms.
  - **{{Equipment Lock (Cable Lock)}}**: Securing *hardware to fixed objects* to prevent theft.
  - **{{Security Guard}}**: Personnel *physically monitoring and protecting* premises.
  - **{{Fence}}**: Perimeter *barrier defining boundaries and* deterring entry.
  - **{{Lighting}}**: Illuminating *areas to deter and* detect intruders.
  - **{{Magnetometer}}**: Device *detecting metal objects* (metal detector).
- **Physical access security**
  - **{{Key Fob}}**: Hardware *token granting access via* proximity.
  - **{{Smart Card}}**: Card *containing chip for authentication* and access.
  - **{{Mobile Digital Key}}**: Smartphone *app functioning as an* access credential.
  - **{{Key}}**: Traditional *physical object for mechanical* locks.
  - **{{Biometrics}}**: Authentication *using unique physiological characteristics*.
    - **{{Retina Scanner}}**: Scans *blood vessel patterns in* the eye.
    - **{{Fingerprint Scanner}}**: Captures *friction ridge patterns of* the finger.
    - **{{Palm Print Scanner}}**: Scans *vein patterns and ridges* of the hand.
    - **{{Facial Recognition (FRT)}}**: Analyzes *geometric features of the* face.
    - **{{Voice Recognition}}**: Analyzes *unique vocal characteristics* for identity.
- **Logical security**
  - **{{Principle of Least Privilege}}**: Granting *minimum necessary access rights* for tasks.
  - **{{Zero Trust Model}}**: Security *framework assuming breach and* verifying every request.
  - **{{Access Control List (ACL)}}**: Rules *defining permissions for users* and resources.
  - **{{Multifactor Authentication (MFA)}}**: Requiring *two or more verification* methods.
    - **{{Email / SMS / Voice Call}}**: Receiving *verification codes via communication* channels.
    - **{{Hardware Token}}**: Physical *device generating time-based* codes.
    - **{{Authenticator App}}**: Software *generating codes on a* mobile device.
    - **{{TOTP / OTP}}**: One-time *passwords valid for a* single session.
  - **{{Security Assertions Markup Language (SAML)}}**: XML standard *for exchanging authentication and* authorization data.
  - **{{Single Sign-On (SSO)}}**: Using *one set of credentials* for multiple apps.
  - **{{Just-in-Time Access (JIT)}}**: Granting *temporary privileges only when* needed.
  - **{{Privileged Access Management (PAM)}}**: Securing *and monitoring administrative accounts*.
  - **{{Mobile Device Management (MDM)}}**: Administering *mobile devices via centralized* policies.
  - **{{Data Loss Prevention (DLP)}}**: Preventing *unauthorized data exfiltration or* leakage.
  - **{{Identity and Access Management (IAM)}}**: Managing *user identities and their* access rights.
  - **{{Directory Services}}**: Centralized *database of network resources* (e.g., AD).

### 2.2 Given a scenario, configure and apply basic Microsoft Windows OS security settings

- **{{Defender Antivirus}}**: Integrated Windows *malware detection and removal* tool.
  - **{{Activate / Deactivate}}**: Enabling or *disabling real-time virus* protection.
  - **{{Update Definitions}}**: Downloading *latest virus signatures for* detection.
- **{{Firewall}}**: Network *security system filtering incoming and* outgoing traffic.
  - **{{Activate / Deactivate}}**: Enabling or *disabling network traffic* filtering.
  - **{{Port Security}}**: Blocking or *allowing specific communication* endpoints.
  - **{{Application Security}}**: Rules *governing network access for* specific programs.
- **User and groups**
  - **{{Local vs. Microsoft Account}}**: Computer-specific *login vs cloud-synced* identity.
  - **{{Standard Account}}**: User *account with limited system* privileges.
  - **{{Administrator}}**: User *account with full system* control.
  - **{{Guest User}}**: Restricted *account for temporary* system access.
  - **{{Power User}}**: Legacy *account type with intermediate* privileges.
- **Log-in OS options**
  - **{{Username and Password}}**: Traditional *knowledge-based authentication* method.
  - **{{Personal Identification Number (PIN)}}**: Numeric *code used for local* device access.
  - **{{Fingerprint / Facial Recognition}}**: Biometric *authentication for secure and* fast login.
  - **{{Single Sign-On (SSO)}}**: Using *one credential for multiple* applications.
  - **{{Passwordless / Windows Hello}}**: Modern *authentication using biometrics or* a PIN.
- **{{NTFS vs. Share Permissions}}**: File-level *security vs network access* control.
  - **{{File and Folder Attributes}}**: Properties *like Read-only, Hidden, or* System.
  - **{{Inheritance}}**: Permissions *flowing from parent to* child folders.
- **{{Run as Administrator}}**: Executing *tasks with elevated administrative* privileges.
- **{{User Account Control (UAC)}}**: Feature *prompting for permission before* system changes.
- **{{BitLocker}}**: Full-disk *encryption feature for Windows* drives.
  - **{{BitLocker-To-Go}}**: BitLocker *encryption for removable flash* storage.
- **{{Encrypting File System (EFS)}}**: Encrypting *individual files and folders* on NTFS.
- **{{Active Directory (AD)}}**: Microsoft *service for managing network* resources.
  - **{{Joining Domain}}**: Connecting *a computer to centralized* management.
  - **{{Log-in Script}}**: Automated *tasks executed during user* login.
  - **{{Organizational Unit (OU)}}**: Container *used to organize AD* objects.
  - **{{Home Folder}}**: Personal *network storage assigned to* a user.
  - **{{Group Policy (GPO)}}**: Infrastructure *used to manage configuration* settings.
  - **{{Security Groups}}**: Collection *of users for simplified* permission management.
  - **{{Folder Redirection}}**: Storing *user profile folders on* a server.

### 2.3 Compare and contrast wireless security protocols and authentication methods

- **Protocols and encryption**
  - **{{Wired Equivalent Privacy (WEP)}}**: Legacy *vulnerable wireless security* protocol.
  - **{{Wi-Fi Protected Access 2 (WPA2)}}**: Secure *protocol using CCMP and AES* encryption.
  - **{{WPA3}}**: Latest *protocol using SAE and GCMP* encryption.
  - **{{Temporal Key Integrity Protocol (TKIP)}}**: Legacy *encryption used with WPA* protocols.
  - **{{Advanced Encryption Standard (AES)}}**: Strong *symmetric block cipher used for* encryption.
  - **{{Counter Mode Cipher Block Chaining Message Authentication Code Protocol (CCMP)}}**: Encryption *mechanism used in WPA2* networks.
  - **{{Simultaneous Authentication of Equals (SAE)}}**: Key *exchange protocol preventing offline* attacks.
- **Authentication**
  - **{{Pre-Shared Key (PSK)}}**: Authentication *using a common shared password*.
  - **{{802.1X (Enterprise)}}**: Authentication *using a centralized server* framework.
  - **{{Remote Authentication Dial-In User Service (RADIUS)}}**: Client/server *protocol for centralized authentication* and authorization.
  - **{{Terminal Access Controller Access-Control System Plus (TACACS+)}}**: Cisco *proprietary protocol for centralized* administration.
  - **{{Kerberos}}**: Ticket-based *authentication protocol for trusted* networks.
  - **{{Multifactor Authentication (MFA)}}**: Requiring *multiple independent credentials for* access.

### 2.4 Summarize types of malware and tools/methods for detection, removal, and prevention

- **Malware**
  - **{{Trojan (Trojan Horse)}}**: Malicious *program disguised as legitimate* software.
  - **{{Rootkit}}**: Malware *concealing its presence with* administrative privileges.
  - **{{Virus}}**: Malicious code *attaching to files to* replicate.
  - **{{Spyware}}**: Malware *secretly recording user activity* and data.
  - **{{Ransomware}}**: Malware *encrypting data and demanding* payment.
  - **{{Keylogger}}**: Software *recording keystrokes to steal* credentials.
  - **{{Boot Sector Virus}}**: Malware *infecting the master boot* record.
  - **{{Cryptominer}}**: Malware *using system resources to* mine cryptocurrency.
  - **{{Stalkerware}}**: Spyware *used to monitor specific* individuals secretly.
  - **{{Fileless Malware}}**: Attack *running in memory without* file artifacts.
  - **{{Worm}}**: Self-replicating *malware spreading independently across* networks.
- **{{Adware}}**: Software *displaying unwanted advertising for* revenue.
- **{{Potentially Unwanted Program (PUP)}}**: Software *installed without clear user* consent.
- **Tools and methods**
  - **{{Recovery Console}}**: Command-line *interface for repairing system* issues.
  - **{{Endpoint Detection and Response (EDR)}}**: Monitoring *host activities to detect* threats.
  - **{{Managed Detection and Response (MDR)}}**: Outsourced *security monitoring and incident* handling.
  - **{{Extended Detection and Response (XDR)}}**: Integrating *security data across multiple* layers.
  - **{{Antivirus / Anti-malware}}**: Software *scanning for and removing* malicious code.
  - **{{Email Security Gateway}}**: Appliance *filtering incoming and outgoing* mail.
  - **{{Software Firewall}}**: Application *controlling network traffic on* a host.
  - **{{User Education}}**: Training *users to recognize and* avoid threats.
    - **{{Anti-Phishing Training}}**: Teaching *users to identify deceptive* emails.
  - **{{OS Reinstallation}}**: Wiping *system to ensure complete* malware removal.
  - **{{Safe Mode}}**: Diagnostic *boot mode loading minimal* drivers.

### 2.5 Compare and contrast common social engineering attacks, threats, and vulnerabilities

- **Social engineering**
  - **{{Social Engineering}}**: Manipulating *people into performing actions or* divulging info.
  - **{{Phishing}}**: Deceptive *emails inducing users to reveal* information.
    - **{{Vishing}}**: Phishing *attempts conducted via voice* calls.
    - **{{Smishing}}**: Phishing *attempts conducted via SMS* messages.
    - **{{QR Code Phishing (Quishing)}}**: Deceptive *scans leading to malicious* sites.
    - **{{Spear Phishing}}**: Targeted *phishing aimed at specific* individuals.
    - **{{Whaling}}**: Targeted *phishing aimed at high-level* executives.
  - **{{Shoulder Surfing}}**: Observing *sensitive information by looking* over someone.
  - **{{Tailgating / Piggybacking}}**: Following *an authorized person into* a building.
  - **{{Impersonation}}**: Pretending *to be another person* or entity.
  - **{{Dumpster Diving}}**: Searching *trash for discarded sensitive* information.
- **Threats**
  - **{{Denial of Service (DoS)}}**: Attack *disrupting availability of a* single system.
  - **{{Distributed Denial of Service (DDoS)}}**: Attack *from multiple sources overwhelming* a target.
  - **{{Evil Twin}}**: Fake *access point mimicking a* legitimate network.
  - **{{Zero-Day Attack}}**: Attack *exploiting a previously unknown* vulnerability.
  - **{{Spoofing}}**: Falsifying *data like IP or* MAC addresses.
  - **{{On-Path Attack (MitM)}}**: Intercepting *and altering communication between* two parties.
  - **{{Brute-Force Attack}}**: Trying *all possible combinations to* guess credentials.
  - **{{Dictionary Attack}}**: Using *a list of common* words for passwords.
  - **{{Insider Threat}}**: Trusted *users exploiting authorized access* to harm.
  - **{{SQL Injection (SQLi)}}**: Injecting *queries to manipulate databases* via input.
  - **{{Cross-Site Scripting (XSS)}}**: Injecting *malicious scripts into trusted* websites.
  - **{{Business Email Compromise (BEC)}}**: Compromising *legitimate email accounts for* fraud.
  - **{{Supply Chain / Pipeline Attack}}**: Attacking *third-party vendors to compromise* targets.
- **Vulnerabilities**
  - **{{Non-compliant Systems}}**: Devices *not meeting established security* standards.
  - **{{Unpatched Systems}}**: Software *missing critical security updates*.
  - **{{Unprotected Systems}}**: Devices *lacking antivirus or firewall* protection.
  - **{{End-of-Life (EOL)}}**: Products *no longer receiving security* updates.
  - **{{Bring Your Own Device (BYOD)}}**: Risks *inherited from unmanaged personal* hardware.
  - **{{Default Configurations}}**: Leaving *vendor-set credentials or settings* unchanged.

### 2.6 Given a scenario, implement procedures for basic small office/home office (SOHO) malware removal

- **{{Step 1: Identify Malware Symptoms}}**: Observing *unusual behavior to confirm* an infection.
- **{{Step 2: Quarantine Infected System}}**: Disconnecting *infected hosts from the* network.
  - **{{Air Gap}}**: Physically *isolating a computer from* all networks.
- **{{Step 3: Disable System Restore}}**: Preventing *malware from hiding within* system snapshots.
- **{{Step 4: Remediate Infected Systems}}**: Process of *cleaning and repairing compromised* systems.
  - **{{Step 4a: Update Anti-malware Software}}**: Downloading *latest virus signatures for* effective scanning.
  - **{{Step 4b: Scan and Removal Techniques}}**: Using *Safe Mode or WinPE* to delete malware.
    - **{{Windows Preinstallation Environment (WinPE)}}**: Lightweight *OS used for system* recovery tasks.
- **{{Step 5: Schedule Scans and Run Updates}}**: Configuring *automated future checks and* OS patches.
- **{{Step 6: Enable System Restore}}**: Re-enabling *the snapshot feature after* cleaning.
  - **{{Restore Point}}**: Saved *state of system files* and registry.
- **{{Step 7: Educate the End User}}**: Training *users to avoid future* malware infections.
- **{{Reimage / Reinstall}}**: Final *remedy if malware cannot* be removed.

### 2.7 Given a scenario, apply workstation security options and hardening techniques

- **{{Data-at-Rest Encryption}}**: Protecting *stored information from unauthorized* physical access.
  - **{{Full-Disk Encryption (FDE)}}**: Encrypting *an entire storage volume* automatically.
- **Password considerations**
  - **{{Length}}**: Total *number of characters in* a password.
  - **{{Character Types}}**: Using *letters, numbers, and symbols* for strength.
  - **{{Uniqueness}}**: Prohibiting *use of previously used* passwords.
  - **{{Complexity}}**: Combining *diverse characters to resist* brute force.
  - **{{Expiration}}**: Mandatory *periodic changing of user* credentials.
- **Firmware passwords**
  - **{{BIOS / UEFI Passwords}}**: Restricting *access to low-level system* settings.
- **End-user best practices**
  - **{{Screensaver Lock}}**: Automated *password prompt after period* of inactivity.
  - **{{Log Off}}**: Terminating *user session when not* in use.
  - **{{Secure Critical Hardware}}**: Physically *protecting assets from theft* or damage.
  - **{{PII and Password Security}}**: Safeguarding *identifiable data and credentials* from exposure.
  - **{{Password Managers}}**: Tools *securely storing and generating* complex credentials.
- **Account management**
  - **{{Restrict User Permissions}}**: Granting *access based on job* requirements.
  - **{{Restrict Log-in Times}}**: Limiting *system access to specific* hours.
  - **{{Disable Guest Account}}**: Removing *unauthenticated access to the* local system.
  - **{{Failed Attempts Lockout}}**: Disabling *accounts after multiple incorrect* login attempts.
  - **{{Timeout / Screen Lock}}**: Forcing *re-authentication after idle* time.
  - **{{Account Expiration}}**: Setting *dates when accounts automatically* become inactive.
- **{{Default Credentials}}**: Changing *factory-set usernames and passwords* immediately.
- **{{Disable AutoRun / AutoPlay}}**: Preventing *automated execution of code* from media.
- **{{Disable Unused Services}}**: Reducing *attack surface by stopping* unnecessary processes.
- **{{Hardening}}**: Process *of securing a system* by reducing vulnerabilities.

### 2.8 Given a scenario, apply common methods for securing mobile devices

- **Hardening techniques**
  - **{{Device Encryption}}**: Encrypting *storage to prevent unauthorized* data access.
  - **Screen locks**
    - **{{Facial Recognition}}**: Biometric *authentication using facial geometry*.
    - **{{PIN Codes}}**: Numeric *passwords for device access*.
    - **{{Fingerprint}}**: Biometric *authentication using dermal ridges*.
    - **{{Pattern}}**: Graphical *password connecting specific dots*.
    - **{{Swipe}}**: Basic *gesture unlocking device without* authentication.
  - **{{Configuration Profiles}}**: XML files *distributing settings to Apple* devices.
- **Patch management**
  - **{{OS Updates}}**: System-level *patches fixing vulnerabilities and* bugs.
  - **{{Application Updates}}**: Software *patches improving functionality and* security.
- **Endpoint security software**
  - **{{Antivirus / Anti-malware}}**: Software *detecting and removing malicious* code.
  - **{{Content Filtering}}**: Blocking *access to specific websites* or categories.
- **{{Locator Applications}}**: GPS-based *tools for finding lost* devices.
- **{{Remote Wipe}}**: Sending *command to erase data* on lost devices.
- **{{Remote Backup}}**: Automatically *saving data to cloud* storage.
- **{{Failed Log-in Attempts Restrictions}}**: Locking *device after incorrect credentials* entered.
- **Policies and procedures**
  - **{{Mobile Device Management (MDM)}}**: Enterprise *software controlling enrolled mobile* devices.
  - **{{BYOD vs. Corporate-Owned}}**: Policies *governing personal vs company* hardware use.
  - **{{Profile Security Requirements}}**: Enforcing *minimum standards like passcodes* via MDM.
  - **{{Jailbreaking / Rooting}}**: Removing *manufacturer restrictions on OS* (Security Risk).

### 2.9 Compare and contrast common data destruction and disposal methods

- **{{Physical Destruction}}**: Rendering storage media *physically and permanently unreadable*.
  - **{{Drilling}}**: Boring holes *through drive platters and heads*.
  - **{{Shredding}}**: Reducing media *to tiny pieces via machines*.
  - **{{Degaussing}}**: Eliminating data *using strong electromagnetic fields*.
  - **{{Incineration}}**: Exposing media *to high heat until destroyed*.
- **{{Recycling or Repurposing}}**: Process of *sanitizing media for safe reuse*.
  - **{{Erasing / Wiping}}**: Software process *overwriting data with random bits*.
    - **{{Overwrite}}**: Replacing existing *bits with zeros or ones*.
  - **{{Low-Level Formatting}}**: Initializing *disks with sector markings*.
  - **{{Standard Formatting}}**: Building *a filesystem on a partition*.
- **{{Outsourcing}}**: Entrusting *data destruction to external entities*.
  - **{{Third-Party Vendor}}**: Specialized *company performing secure media disposal*.
  - **{{Certificate of Destruction (CoD)}}**: Legal *document proving secure data erasure*.
- **{{Regulatory and Environmental Requirements}}**: Laws *governing data privacy and waste*.
  - **{{Electronic Waste (E-waste)}}**: Discarded *electronics requiring specialized recycling*.

### 2.10 Given a scenario, apply security settings on SOHO wireless and wired networks

- **Router settings**
  - **{{Change Default Passwords}}**: Replacing *vendor-set credentials* to prevent access.
  - **{{IP Filtering}}**: Permitting or *blocking traffic based on address*.
  - **{{Firmware Updates}}**: Installing *manufacturer software patches* for security.
  - **{{Content Filtering}}**: Restricting *access to specific web categories*.
  - **{{Physical Placement}}**: Locating hardware *in secure, monitored areas*.
  - **{{Universal Plug and Play (UPnP)}}**: Protocol *allowing devices to discover network*.
    - **Note:** Often disabled due to security vulnerabilities.
  - **{{Screened Subnet (DMZ)}}**: Buffer zone *separating internal and external* networks.
  - **{{Secure Management Access}}**: Restricting *administrative interface to specific hosts*.
- **Wireless specific**
  - **{{Service Set Identifier (SSID)}}**: The *human-readable name* of wireless network.
  - **{{SSID Broadcast}}**: Feature *announcing network name to clients*.
  - **{{Encryption Settings}}**: Securing *wireless traffic using WPA2 / WPA3*.
  - **{{Guest Access}}**: Providing *isolated network for temporary users*.
  - **{{MAC Filtering}}**: Permitting *access based on hardware address*.
- **Firewall settings**
  - **{{Disabling Unused Ports}}**: Closing *logical endpoints to reduce risk*.
  - **{{Port Forwarding}}**: Directing *external traffic to internal hosts*.
  - **{{Port Mapping}}**: Synonymous *with port forwarding for NAT*.
  - **{{Network Address Translation (NAT)}}**: Mapping *private IP addresses to public* IP.

### 2.11 Given a scenario, configure relevant security settings in a browser

- **Browser download / installation**
  - **{{Trusted Sources}}**: Official vendor websites *or verified application stores*.
    - **{{Hashing}}**: Mathematical *algorithm verifying file integrity* and authenticity.
  - **{{Untrusted Sources}}**: Unverified *third-party websites or unofficial* repositories.
- **{{Browser Patching}}**: Process of *installing updates to fix* security vulnerabilities.
- **{{Extensions and Plug-ins}}**: Software *add-ons extending browser functionality* and features.
  - **{{Trusted vs. Untrusted}}**: Verifying *source and permissions before* installation.
- **{{Password Managers}}**: Tools for *securely storing and generating* complex credentials.
- **{{Secure Connections (HTTPS)}}**: Encrypted *communication between browser and* web server.
  - **{{Valid Certificates}}**: Digital *documents proving a website's* identity.
- **Settings**
  - **{{Pop-up Blocker}}**: Feature *preventing unwanted windows from* opening automatically.
  - **{{Clearing Browsing Data}}**: Removing *history, form data, and* temporary files.
  - **{{Clearing Cache}}**: Deleting *locally stored web files* to refresh content.
  - **{{Private-Browsing Mode (Incognito)}}**: Session *where history and cookies* are not saved.
  - **{{Sign-in / Sync}}**: Synchronizing *browser data across multiple* user devices.
  - **{{Ad Blockers}}**: Software *preventing advertisements from being* displayed.
  - **{{Proxy}}**: Intermediary *server filtering or hiding* network traffic.
  - **{{Secure DNS}}**: Encrypting *DNS queries to prevent* redirection attacks.
- **{{Browser Feature Management}}**: Enabling *or disabling specific web* technologies.
  - **{{Cookies}}**: Small *files storing user preferences* and session data.
  - **{{Script Blockers}}**: Disabling *JavaScript to prevent malicious* code execution.

## 3.0 Software Troubleshooting 23%

### 3.1 Given a scenario, troubleshoot common Windows OS issues

- **{{Blue Screen of Death (BSOD)}}**: Critical *stop error indicating a system* crash.
- **{{Degraded Performance}}**: Reduced *system speed due to resource* bottlenecks.
- **{{Boot Issues}}**: Errors *preventing the OS from loading* correctly.
- **{{Frequent Shutdowns}}**: Sudden *power loss often from heat* issues.
- **{{Services Not Starting}}**: Failure *of background processes to initialize* correctly.
- **{{Applications Crashing}}**: Software *terminating unexpectedly during active use*.
- **{{Low Memory Warnings}}**: Insufficient *RAM available for active system* processes.
- **{{USB Controller Resource Warnings}}**: Exceeding *bandwidth or power limits on* bus.
- **{{System Instability}}**: Unreliable *system behavior and frequent errors*.
- **{{No OS Found}}**: BIOS *failure to locate bootable drive* data.
- **{{Slow Profile Load}}**: Delays *during user login due to* size.
- **{{Time Drift}}**: Inaccurate *clock often caused by failing* battery.
- **{{Safe Mode}}**: Minimal *diagnostic environment for troubleshooting drivers*.
- **{{System File Checker (SFC)}}**: Command *utility for repairing corrupt system* files.
- **{{Event Viewer}}**: Logs *recording hardware and software error* details.
- **{{System Restore}}**: Reverting *system files to a previous* state.

### 3.2 Given a scenario, troubleshoot common mobile OS and application issues

- **{{Application Fails to Launch}}**: Software *refusing to start or load* initially.
- **{{Application Fails to Close / Crashes}}**: App *unresponsive or terminating unexpectedly* during use.
- **{{Application Fails to Update}}**: Inability *to install latest software patches* or versions.
- **{{Application Fails to Install}}**: Error *preventing new software from being* added.
- **{{Slow to Respond}}**: Significant *lag in touch or system* interface.
- **{{OS Fails to Update}}**: Failure *to download or install system* upgrades.
- **{{Battery Life Issues}}**: Rapid *power drain shortening device usage* time.
- **{{Random Reboots}}**: Device *restarting unexpectedly without user* command.
- **Connectivity issues**
  - **{{Bluetooth}}**: Problems *pairing or maintaining connection with* devices.
  - **{{Wi-Fi}}**: Difficulty *connecting to wireless networks or* internet.
  - **{{Near-Field Communication (NFC)}}**: Failure *of short-range contactless payment* features.
- **{{Screen Does Not Autorotate}}**: Failure *of accelerometer to detect orientation* changes.
- **{{Soft Reset}}**: Restarting *device via software without data* loss.
- **{{Hard Reset (Factory Reset)}}**: Wiping *device to original state to* fix issues.
- **{{Safe Mode (Mobile)}}**: Booting *without third-party apps to diagnose* issues.
- **{{Uninstall / Reinstall}}**: Removing *and restoring app to fix* corruption.

### 3.3 Given a scenario, troubleshoot common mobile OS and application security issues

- **Security concerns**
  - **{{Application Source}}**: Installing *apps from unverified third-party repositories*.
  - **{{Developer Mode}}**: Advanced *OS state allowing sideloading and* debugging.
  - **{{Root Access / Jailbreak}}**: Removing *manufacturer OS restrictions for full* control.
  - **{{Unauthorized / Malicious Application}}**: Software *designed to harm or steal* data.
    - **{{Application Spoofing}}**: App *mimicking legitimate software to deceive* users.
- **Common symptoms**
  - **{{High Network Traffic}}**: Unusual *data spikes indicating background exfiltration* activity.
  - **{{Degraded Response Time}}**: System *slowness often caused by malware* overhead.
  - **{{Data-Usage Limit Notification}}**: Alert *indicating background apps consuming mobile* data.
  - **{{Limited / No Connectivity}}**: Network *access blocked by malicious configuration* changes.
  - **{{High Number of Ads}}**: Frequent *pop-ups indicating adware or spyware* infection.
  - **{{Fake Security Warnings}}**: Deceptive *alerts designed to trick users* into action.
  - **{{Unexpected Application Behavior}}**: Programs *opening, closing, or acting independently*.
  - **{{Leaked Personal Files / Data}}**: Unauthorized *disclosure of sensitive user information*.
- **{{Remote Wipe}}**: Security *command erasing all data on* lost devices.
- **{{Mobile Device Management (MDM)}}**: Enterprise *system enforcing security policies on* devices.

### 3.4 Given a scenario, troubleshoot common personal computer (PC) security issues

- **Common symptoms**
  - **{{Unable to Access the Network}}**: Security *software or malware blocking* network connectivity.
  - **{{Desktop Alerts}}**: Pop-ups *warning of potential security* threats.
  - **{{False Antivirus Alerts}}**: Deceptive *notifications tricking users into* downloading malware.
  - **{{Altered System or Personal Files}}**: Files *encrypted, renamed, or deleted* by malware.
    - **{{Missing / Renamed Files}}**: Indicators *of unauthorized file manipulation* activity.
    - **{{Inability to Access Files}}**: Permissions *changed or files locked* by ransomware.
  - **{{Unwanted Notifications}}**: Persistent *messages indicating unauthorized system* changes.
  - **{{OS Update Failures}}**: Malware *preventing security patches from* being installed.
- **Browser-related symptoms**
  - **{{Random / Frequent Pop-ups}}**: Browser *windows appearing without user* interaction.
    - **{{Pop-up Blocker}}**: Software *preventing unwanted browser windows* from appearing.
  - **{{Certificate Warnings}}**: Alerts *indicating issues with site* encryption identity.
    - **{{Trusted Root CA}}**: Trusted *entities that verify digital* site certificates.
  - **{{Redirection}}**: Browser *sending users to unintended* malicious websites.
  - **{{Degraded Browser Performance}}**: Significant *slowdown in page loading* or response.
- **{{Indicators of Compromise (IoC)}}**: Evident *signs that a system* is breached.
- **{{Quarantine}}**: Isolating *infected files to prevent* further spread.
- **{{Remediation}}**: The *process of fixing security* vulnerabilities.

## 4.0 Operational Procedures 21%

### 4.1 Given a scenario, implement best practices associated with documentation and support systems information management

- **{{Ticketing System}}**: Software *managing user requests and* technical issues.
  - **{{User Information}}**: Contact *details identifying the person* reporting issues.
  - **{{Device Information}}**: Specifics *identifying the hardware requiring* service.
  - **{{Description of Issues}}**: Detailed *explanation of the problem* reported.
  - **{{Category}}**: Classification *used for grouping similar* technical issues.
  - **{{Severity}}**: Measure *of impact on business* operations.
  - **{{Escalation Levels}}**: Moving *tickets to higher-tier technical* support.
  - **Written communication**
    - **{{Issue Description}}**: Initial *statement of the technical* problem.
    - **{{Progress Notes}}**: Log *of actions taken during* troubleshooting.
    - **{{Issue Resolution}}**: Documentation *of the final fix* applied.
- **{{Asset Management}}**: Tracking *the lifecycle of organizational* property.
  - **{{Inventory List}}**: Database *of all physical hardware* and software.
  - **{{Configuration Management Database (CMDB)}}**: Repository *storing information about IT* assets (CIs).
    - **{{Configuration Item (CI)}}**: Any *component that needs management* in IT.
  - **{{Asset Tags / IDs}}**: Unique *identifiers physically attached to* equipment.
  - **{{Procurement Lifecycle}}**: Stages *from purchase to final* asset disposal.
  - **{{Warranty}}**: Manufacturer *guarantee to repair or* replace hardware.
  - **{{Licensing}}**: Legal *agreement defining software usage* rights.
  - **{{Assigned User}}**: Individual *responsible for using specific* company assets.
- **Types of documents**
  - **{{Incident Report}}**: Document *recording details of a* security event.
  - **{{Standard Operating Procedure (SOP)}}**: Step-by-step *instructions for routine technical* tasks.
  - **{{New User / Onboarding Checklist}}**: Procedures *managing new user entry* and setup.
  - **{{User Off-boarding Checklist}}**: Procedures *managing user exit and* asset recovery.
  - **{{Service-Level Agreement (SLA)}}**: Contract *defining expected service performance* levels.
  - **{{Knowledge Base (KB)}}**: Repository *of articles for self-service* troubleshooting.

### 4.2 Given a scenario, apply change management procedures

- **{{Documented Business Processes}}**: Written *procedures ensuring consistent and predictable* results.
  - **{{Rollback Plan}}**: Procedures *to revert systems if change* fails.
  - **{{Backup Plan}}**: Strategy *to protect data before implementing* changes.
  - **{{Sandbox Testing}}**: Verifying *changes in isolated test environments* first.
  - **{{Responsible Staff Members}}**: Individuals *accountable for executing specific change* steps.
- **{{Change Management}}**: Process *minimizing disruption during system modifications* and updates.
  - **{{Request Form}}**: Formal *document initiating the change control* process.
  - **{{Purpose of Change}}**: Justification *explaining why the modification is* necessary.
  - **{{Scope of Change}}**: Definition *of specific systems and components* affected.
  - **{{Change Type}}**: Classification *based on urgency and potential* impact.
    - **{{Standard Change}}**: Low-risk *pre-approved routine modification task*.
    - **{{Normal Change}}**: Planned *modification requiring standard review process*.
    - **{{Emergency Change}}**: Urgent *fix addressing critical system failures*.
  - **{{Schedule}}**: Defining *the timing for change execution*.
    - **{{Change Freeze}}**: Period *where no system modifications are* permitted.
    - **{{Maintenance Window}}**: Scheduled *timeframe authorized for performing changes*.
  - **{{Affected Systems / Impact}}**: Analysis *of how changes influence infrastructure*.
  - **{{Risk Analysis}}**: Assessing *potential negative consequences of change*.
    - **{{Risk Level}}**: Numerical *or qualitative rating of change* danger.
  - **{{Change Advisory Board (CAB)}}**: Committee *approving high-risk or normal changes*.
  - **{{Implementation}}**: The *actual execution of the planned* change.
  - **{{Peer Review}}**: Technical *evaluation of change by another* specialist.
  - **{{End-User Acceptance}}**: Verification *by users that systems work* correctly.
  - **{{Post-Implementation Review (PIR)}}**: Assessing *the success and lessons learned* after change.

### 4.3 Given a scenario, implement workstation backup and recovery methods

- **{{Backup}}**: Copying *data to secondary storage for recovery* purposes.
  - **{{Full Backup}}**: Copying *all selected data to backup media*.
  - **{{Incremental Backup}}**: Copying *only data changed since last backup*.
  - **{{Differential Backup}}**: Copying *data changed since the last full* backup.
  - **{{Synthetic Full Backup}}**: Creating *full backup from previous incremental data*.
- **{{Recovery}}**: Process *of restoring data from backup media*.
  - **{{In-place / Overwrite}}**: Restoring *data to its original storage location*.
  - **{{Alternative Location}}**: Restoring *data to a different storage target*.
- **{{Backup Testing}}**: Verifying *integrity and usability of backup data*.
  - **{{Frequency}}**: How *often backups and tests are performed*.
- **Backup rotation schemes**
  - **{{Onsite vs. Offsite}}**: Local *fast recovery vs remote disaster protection*.
  - **{{Grandfather-Father-Son (GFS)}}**: Tiered *rotation for daily, weekly, monthly backups*.
  - **{{3-2-1 Backup Rule}}**: Strategy *maintaining three copies on two media*.
- **{{Recovery Time Objective (RTO)}}**: Maximum *acceptable time to restore system functionality*.
- **{{Recovery Point Objective (RPO)}}**: Maximum *acceptable amount of data loss duration*.
- **{{Immutable Backup}}**: Data *that cannot be changed or deleted*.

### 4.4 Given a scenario, use common safety procedures

- **{{Safety Procedures}}**: Guidelines *protecting personnel and equipment from harm*.
- **Electrostatic Discharge (ESD)**
  - **{{ESD Strap}}**: Device *grounding technician to prevent static buildup*.
  - **{{ESD Mat}}**: Surface *dissipating static from components and tools*.
  - **{{Antistatic Bag}}**: Shielded *packaging preventing static damage to components*.
- **Electrical safety**
  - **{{Equipment Grounding}}**: Path *diverting excess electricity safely to earth*.
  - **{{Power Disconnection}}**: Removing *source energy before performing hardware repairs*.
- **Proper component handling and storage**
  - **{{Handling}}**: Grasping *components by edges to avoid contamination*.
- **{{Cable Management}}**: Organizing *wires to improve airflow and safety*.
- **{{Government Regulations}}**: Mandatory *safety and environmental standards (OSHA, etc.)*.
- **Personal Safety**
  - **{{Lifting Techniques}}**: Using *legs to prevent back injury during* transport.
  - **{{Fire Safety}}**: Procedures *and equipment for extinguishing electrical fires*.
  - **{{Personal Protective Equipment (PPE)}}**: Specialized *gear worn to minimize health risks*.
    - **{{Safety Goggles}}**: Eye *protection from flying debris or chemicals*.
    - **{{Air Filter Mask}}**: Respiratory *protection from dust and toxic particles*.

### 4.5 Summarize environmental impacts and local environment controls

- **{{Safety Data Sheet (SDS / MSDS)}}**: Documentation *outlining hazards and safe handling of chemicals*.
  - **Proper disposal**
    - **{{Battery Disposal}}**: Recyling *lead-acid or lithium batteries to prevent* pollution.
    - **{{Toner Disposal}}**: Proper *handling of carcinogenic powder and cartridges*.
    - **{{Device Disposal}}**: Securely *recycling electronics to prevent e-waste pollution*.
- **Environmental controls**
  - **{{Temperature / Humidity Awareness}}**: Monitoring *ambient conditions to prevent hardware failure*.
  - **{{Ventilation}}**: Airflow *preventing heat buildup in confined spaces*.
  - **{{Location / Equipment Placement}}**: Strategic *positioning for optimal cooling and access*.
  - **{{Dust Cleanup}}**: Removing *debris to prevent cooling system failures*.
    - **{{Compressed Air / Vacuums}}**: Tools *for safely cleaning electronic component interiors*.
- **Power protection**
  - **{{Power Surge}}**: Sudden *voltage spike potentially damaging electronic circuits*.
  - **{{Brownout}}**: Temporary *voltage drop causing system instability or* reboots.
  - **{{Blackout}}**: Complete *loss of electrical power from source*.
  - **{{Uninterruptible Power Supply (UPS)}}**: Battery *backup providing power during source failure*.
  - **{{Surge Suppressor}}**: Device *limiting voltage delivered to electronic hardware*.

### 4.6 Explain the importance of prohibited content/activity and privacy, licensing, and policy concepts

- **{{Incident Response (IR)}}**: Structured *method for managing security breach consequences*.
  - **{{Chain of Custody}}**: Documented *handling of evidence to ensure integrity*.
  - **{{Data Preservation}}**: Creating *bit-stream copies of drives for forensics*.
  - **{{Incident Documentation}}**: Formal *records of discovery, response, and resolution*.
  - **{{Order of Volatility}}**: Priority *list for collecting evidence based on* lifespan.
- **Licensing and Compliance**
  - **{{End-User License Agreement (EULA)}}**: Contract *defining software usage rights and restrictions*.
  - **{{Digital Rights Management (DRM)}}**: Technology *controlling access to copyrighted digital content*.
  - **{{Perpetual License}}**: Right *to use software indefinitely after purchase*.
  - **{{Open-Source License}}**: Software *distributed with source code for modification*.
  - **{{Non-Disclosure Agreement (NDA / MNDA)}}**: Legal *contract protecting confidential information from disclosure*.
- **Regulated data**
  - **{{Personally Identifiable Information (PII)}}**: Any *data that can uniquely identify individuals*.
  - **{{Protected Health Information (PHI)}}**: Medical *records and health-related personal information*.
  - **{{PCI DSS}}**: Security *standard for credit card data protection*.
  - **{{Data Retention Requirements}}**: Policies *defining how long data is stored*.
- **{{Acceptable Use Policy (AUP)}}**: Set *of rules for using organizational assets*.
- **{{Regulatory Compliance}}**: Adherence *to laws governing specific data types*.
  - **{{Splash Screen}}**: Legal *notice displayed before granting system access*.

### 4.7 Given a scenario, use proper communication techniques and professionalism

- **{{Professionalism}}**: Maintaining *standards of conduct and technical competence*.
  - **{{Attire}}**: Matching *clothing to the required workspace environment*.
    - **{{Formal vs. Business Casual}}**: Traditional *suit and tie vs relaxed professional* wear.
  - **{{Communication}}**: Using *clear language without jargon or slang*.
  - **{{Active Listening}}**: Giving *undivided attention and confirming understanding*.
  - **{{Cultural Sensitivity}}**: Respecting *diverse backgrounds and using proper titles*.
  - **{{Punctuality}}**: Being *on time for scheduled customer appointments*.
  - **{{Distraction Management}}**: Avoiding *personal calls and social media during* work.
- **Customer Interaction**
  - **{{Difficult Situations}}**: Managing *conflict without being defensive or judgmental*.
  - **{{Clarification}}**: Asking *open-ended questions to verify the issue*.
  - **{{Expectation Management}}**: Setting *realistic timelines for technical service completion*.
  - **{{Documentation}}**: Providing *written records of the services performed*.
  - **{{Follow-up}}**: Verifying *customer satisfaction after the technical fix*.
  - **{{Data Privacy}}**: Protecting *confidential customer materials during the repair*.
- **{{Emotional Intelligence (EQ)}}**: Ability *to perceive and manage customer emotions*.
- **{{Soft Skills}}**: Interpersonal *abilities enhancing technical service delivery*.

### 4.8 Explain the basics of scripting

- **{{Scripting}}**: Writing *automated instructions for computer task execution*.
- **Script file types**
  - **{{.bat (Batch)}}**: Windows *command-line scripts for basic automation*.
  - **{{.ps1 (PowerShell)}}**: Advanced *Windows scripts using cmdlets and objects*.
  - **{{.vbs (VBScript)}}**: Legacy *Windows scripting language for administration*.
  - **{{.sh (Shell Script)}}**: Unix / Linux *command-line automation using Bash*.
  - **{{.js (JavaScript)}}**: Scripting *language for web and system automation*.
  - **{{.py (Python)}}**: High-level *cross-platform language for complex scripting*.
- **Use cases for scripting**
  - **{{Automation}}**: Performing *repetitive tasks without manual user input*.
  - **{{Information Gathering}}**: Querying *system properties and logging hardware data*.
  - **{{System Management}}**: Restarting *machines and remapping network drives automatically*.
- **Considerations**
  - **{{Malware Introduction}}**: Risk *of scripts executing malicious code artifacts*.
  - **{{Configuration Drift}}**: Inadvertently *changing system settings away from baseline*.
  - **{{System Crash}}**: Improper *resource handling leading to OS failure*.
- **{{Logic Structures}}**: Programming *constructs like loops and conditional statements*.
- **{{Environment Variables}}**: Dynamic *values affecting the behavior of processes*.
- **{{Interpreter}}**: Software *executing script instructions directly without compiling*.

### 4.9 Given a scenario, use remote access technologies

- **{{Remote Access}}**: Technology *enabling users to connect to distant systems*.
- **Methods and Tools**
  - **{{Remote Desktop Protocol (RDP)}}**: Proprietary *Microsoft protocol for graphical remote access*.
  - **{{Virtual Private Network (VPN)}}**: Encrypted *tunnel providing secure access over public* networks.
  - **{{Virtual Network Computing (VNC)}}**: Platform-independent *graphical desktop sharing system using RFB*.
  - **{{Secure Shell (SSH)}}**: Encrypted *network protocol for secure command execution*.
  - **{{Remote Monitoring and Management (RMM)}}**: Tools *used by MSPs to manage clients*.
  - **{{Simple Protocol for Independent Computing Environments (SPICE)}}**: Open *protocol for accessing virtualized remote desktops*.
  - **{{Windows Remote Management (WinRM)}}**: Management *protocol for local and remote systems*.
  - **Third-party tools**
    - **{{Screen-Sharing Software}}**: Collaborative *tools for viewing or controlling desktops*.
    - **{{Desktop Management Software}}**: Centralized *tools for software and policy deployment*.
- **{{Security Considerations}}**: Evaluating *encryption, authentication, and port vulnerability risks*.
  - **{{Tunneling}}**: Encapsulating *one network protocol within another packet*.
  - **{{Port Forwarding}}**: Directing *external traffic to specific internal hosts*.
  - **{{Telnet}}**: Legacy *unencrypted protocol for remote command access*. (Insecure).

### 4.10 Explain basic concepts related to artificial intelligence (AI)

- **{{Artificial Intelligence (AI)}}**: Systems *simulating human intelligence to perform complex tasks*.
- **{{Application Integration}}**: Embedding *AI capabilities into existing software workflows*.
- **Policy**
  - **{{Appropriate Use}}**: Rules *defining ethical and professional AI tool usage*.
  - **{{Plagiarism}}**: Using *AI-generated content without proper source attribution*.
- **Limitations**
  - **{{Bias}}**: Prejudiced *results originating from flawed training data sets*.
  - **{{Hallucination}}**: AI *generating confident but incorrect or nonsensical* information.
  - **{{Accuracy}}**: The *reliability and factual correctness of AI outputs*.
- **Private vs. Public**
  - **{{Data Security}}**: Protecting *sensitive information from unauthorized AI access*.
  - **{{Data Source}}**: The *origin of information used to train AI*.
  - **{{Data Privacy}}**: Ensuring *personal information is not stored by AI*.
- **{{Large Language Model (LLM)}}**: AI *trained on vast text data for conversation*.
- **{{Generative AI}}**: AI *capable of creating new content like text*.
- **{{Prompt Engineering}}**: Crafting *specific inputs to get optimal AI results*.

## CompTIA A+ Core 2 (220-1202) Acronym List

The following is a list of acronyms that appears on the CompTIA A+ Core 2
(2201202) exam. Candidates are encouraged to review the complete list and attain
a working knowledge of all listed acronyms as part of a comprehensive exam
preparation program

- **{{AAA}}**: Authentication, Authorization, and Accounting. *Framework for access control*.
- **{{ACL}}**: Access Control List. *Rules determining access rights*.
- **{{ADF}}**: Automatic Document Feeder. *Device feeding multiple pages*.
- **{{AES}}**: Advanced Encryption Standard. *Symmetric encryption algorithm*.
- **{{AMD}}**: Advanced Micro Devices. *CPU and GPU manufacturer*.
- **{{AP}}**: Access Point. *Device creating wireless network*.
- **{{APFS}}**: Apple File System. *File system for macOS/iOS*.
- **{{APIPA}}**: Automatic Private IP Addressing. *Link-local address assignment*.
- **{{ARM}}**: Advanced RISC Machine. *RISC-based processor architecture*.
- **{{ATX}}**: Advanced Technology Extended. *Standard motherboard form factor*.
- **{{AUP}}**: Acceptable Use Policy. *Rules for network usage*.
- **{{BEC}}**: Business Email Compromise. *Fraud using compromised email*.
- **{{BIOS}}**: Basic Input/Output System. *Legacy firmware interface*.
- **{{BNC}}**: Bayonet Neill-Concelman. *Connector for coaxial cable*.
- **{{BSOD}}**: Blue Screen of Death. *Windows critical error screen*.
- **{{BYOD}}**: Bring Your Own Device. *Policy for personal devices*.
- **{{CAC}}**: Common Access Card. *US DoD smart card*.
- **{{CAS}}**: Column Address Strobe. *Memory timing parameter*.
- **{{CIFS}}**: Common Internet File System. *Dialect of SMB protocol*.
- **{{CMDB}}**: Configuration Management Database. *Repository of IT assets*.
- **{{CMOS}}**: Complementary Metal-Oxide Semiconductor. *Technology for BIOS settings*.
- **{{CNAME}}**: Canonical Name. *DNS alias record*.
- **{{CPU}}**: Central Processing Unit. *Main processing chip*.
- **{{DB-9}}**: D-subminiature 9. *Connector for serial ports*.
- **{{DDoS}}**: Distributed Denial of Service. *Attack from multiple sources*.
- **{{DDR}}**: Double Data Rate. *Memory transfer technology*.
- **{{DHCP}}**: Dynamic Host Configuration Protocol. *Automated IP assignment*.
- **{{DIMM}}**: Dual In-line Memory Module. *Desktop memory module*.
- **{{DKIM}}**: DomainKeys Identified Mail. *Email authentication method*.
- **{{DLP}}**: Data Loss Prevention. *Protection against data leaks*.
- **{{DMARC}}**: Domain-based Message Authentication, Reporting, and Conformance. *Email validation policy*.
- **{{DNS}}**: Domain Name System. *Resolves hostnames to IPs*.
- **{{DoS}}**: Denial of Service. *Attack disrupting service availability*.
- **{{DRM}}**: Digital Rights Management. *Copyright protection technology*.
- **{{DSL}}**: Digital Subscriber Line. *Internet via telephone lines*.
- **{{DVI}}**: Digital Visual Interface. *Digital video connector*.
- **{{ECC}}**: Error Correcting Code. *Memory detecting/fixing errors*.
- **{{EDR}}**: Endpoint Detection and Response. *Host-based security monitoring*.
- **{{EFS}}**: Encrypting File System. *Windows file encryption*.
- **{{EOL}}**: End of Life. *Product support termination*.
- **{{eSATA}}**: External Serial Advanced Technology Attachment. *External storage interface*.
- **{{ESD}}**: Electrostatic Discharge. *Sudden flow of electricity*.
- **{{eSIM}}**: Embedded Subscriber Identity Module. *Programmable built-in SIM*.
- **{{EULA}}**: End User License Agreement. *Software usage contract*.
- **{{exFAT}}**: Extended File Allocation Table. *Optimized flash drive filesystem*.
- **{{FaaS}}**: Function as a Service. *Serverless computing model*.
- **{{FAT32}}**: File Allocation Table 32-bit. *Legacy compatible filesystem*.
- **{{FRT}}**: Face Recognition Technology. *Biometric identification using faces*.
- **{{FTP}}**: File Transfer Protocol. *Unencrypted file transfer*.
- **{{GFS}}**: Grandfather-Father-Son. *Backup rotation scheme*.
- **{{GPS}}**: Global Positioning System. *Satellite-based navigation*.
- **{{GPT}}**: GUID Partition Table. *Modern partitioning standard*.
- **{{GPU}}**: Graphics Processing Unit. *Circuit for image rendering*.
- **{{GUI}}**: Graphical User Interface. *Visual user interface*.
- **{{GUID}}**: Globally Unique Identifier. *Unique reference number*.
- **{{HD}}**: High Definition. *Video resolution of 720p/1080p*.
- **{{HDD}}**: Hard Disk Drive. *Magnetic storage device*.
- **{{HDMI}}**: High-Definition Multimedia Interface. *Digital video/audio interface*.
- **{{HSM}}**: Hardware Security Module. *Physical crypto processing device*.
- **{{HTTP}}**: Hypertext Transfer Protocol. *Unsecured web traffic protocol*.
- **{{HTTPS}}**: Hypertext Transfer Protocol Secure. *Encrypted web traffic protocol*.
- **{{IaaS}}**: Infrastructure as a Service. *Cloud virtualized hardware resources*.
- **{{IAM}}**: Identity and Access Management. *Managing user digital identities*.
- **{{IMAP}}**: Internet Mail Access Protocol. *Email retrieval with syncing*.
- **{{IOPS}}**: Input/Output Operations Per Second. *Storage performance metric*.
- **{{IoT}}**: Internet of Things. *Network of connected physical objects*.
- **{{IP}}**: Internet Protocol. *Routing packets across networks*.
- **{{IPS}}**: Intrusion Prevention System. *Active threat blocking device*.
- **{{IR}}**: Infrared. *Line-of-sight wireless communication*.
- **{{ISO}}**: International Organization for Standardization. *Global standard setting body*.
- **{{ISP}}**: Internet Service Provider. *Company providing internet access*.
- **{{ITX}}**: Information Technology eXtended. *Compact motherboard form factor*.
- **{{KVM}}**: Keyboard-Video-Mouse. *Switch controlling multiple PCs*.
- **{{LAN}}**: Local Area Network. *Network in limited area*.
- **{{LC}}**: Lucent Connector. *Small form-factor fiber connector*.
- **{{LCD}}**: Liquid Crystal Display. *Flat panel display technology*.
- **{{LDAP}}**: Lightweight Directory Access Protocol. *Directory service protocol*.
- **{{LED}}**: Light Emitting Diode. *Semiconductor light source*.
- **{{LTE}}**: Long Term Evolution. *4G mobile communication standard*.
- **{{MAC}}**: Media Access Control. *Unique physical network address*.
- **{{MAN}}**: Metropolitan Area Network. *City-wide computer network*.
- **{{MBR}}**: Master Boot Record. *Legacy boot sector standard*.
- **{{MDM}}**: Mobile Device Management. *Device administration software*.
- **{{MDR}}**: Managed Detection and Response. *Outsourced security monitoring*.
- **{{MFA}}**: Multifactor Authentication. *Using multiple auth methods*.
- **{{MFP}}**: Multifunction Product / Printer. *All-in-one printer device*.
- **{{MMC}}**: MultiMediaCard. *Flash memory card standard*.
- **{{MNDA}}**: Mutual Non-Disclosure Agreement. *Contract protecting shared secrets*.
- **{{mSATA}}**: Mini-SATA. *Small form factor SSD interface*.
- **{{MX}}**: Mail Exchanger. *DNS record for email*.
- **{{NAC}}**: Network Access Control. *Managing device network admission*.
- **{{NAS}}**: Network Attached Storage. *File-level storage server*.
- **{{NAT}}**: Network Address Translation. *Mapping private to public IPs*.
- **{{NDA}}**: Non-Disclosure Agreement. *Confidentiality contract*.
- **{{NetBIOS}}**: Network Basic Input/Output System. *Legacy local network API*.
- **{{NFC}}**: Near Field Communication. *Short-range contactless communication*.
- **{{NIC}}**: Network Interface Card. *Hardware for network connection*.
- **{{NTFS}}**: New Technology File System. *Default Windows file system*.
- **{{NTP}}**: Network Time Protocol. *Clock synchronization protocol*.
- **{{NVMe}}**: Non-Volatile Memory Express. *High-speed SSD interface*.
- **{{OEM}}**: Original Equipment Manufacturer. *Maker of components/software*.
- **{{OLED}}**: Organic Light Emitting Diode. *Display with self-lit pixels*.
- **{{ONT}}**: Optical Network Terminal. *Fiber-to-copper interface*.
- **{{OS}}**: Operating System. *System software managing hardware*.
- **{{OTP}}**: One-Time Password. *Single-use authentication code*.
- **{{PaaS}}**: Platform as a Service. *Cloud development environment*.
- **{{PAM}}**: Privileged Access Management. *Securing admin accounts*.
- **{{PAN}}**: Personal Area Network. *Device network near person*.
- **{{PC}}**: Personal Computer. *General use computer*.
- **{{PCI}}**: Peripheral Component Interconnect. *Legacy expansion bus*.
- **{{PCIe}}**: Peripheral Component Interconnect Express. *High-speed serial expansion bus*.
- **{{PCL}}**: Printer Control Language. *Standard printer page description language*.
- **{{PII}}**: Personally Identifiable Information. *Data identifying a specific individual*.
- **{{PIN}}**: Personal Identification Number. *Numeric password for authentication*.
- **{{PIV}}**: Personal Identity Verification. *US federal smart card standard*.
- **{{PoE}}**: Power over Ethernet. *Power delivery via network cables*.
- **{{POP}}**: Post Office Protocol. *Email retrieval protocol*.
- **{{POST}}**: Power-On Self-Test. *Hardware check during startup*.
- **{{PSU}}**: Power Supply Unit. *Converts AC to DC power*.
- **{{PUP}}**: Potentially Unwanted Program. *Software installed without clear consent*.
- **{{PXE}}**: Preboot Execution Environment. *Booting OS from network*.
- **{{QoS}}**: Quality of Service. *Prioritizing network traffic*.
- **{{RADIUS}}**: Remote Authentication Dial-In User Service. *Centralized authentication protocol*.
- **{{RAID}}**: Redundant Array of Independent Disks. *Storage performance/redundancy*.
- **{{RAM}}**: Random Access Memory. *Volatile system memory*.
- **{{RDP}}**: Remote Desktop Protocol. *GUI remote access protocol*.
- **{{ReFS}}**: Resilient File System. *Microsoft proprietary file system*.
- **{{RFID}}**: Radio Frequency Identification. *Wireless tracking technology*.
- **{{RGB}}**: Red-Green-Blue. *Color model for displays*.
- **{{RISC}}**: Reduced Instruction Set Computer. *Simplified CPU architecture*.
- **{{RJ11}}**: Registered Jack 11. *Connector for telephone lines*.
- **{{RJ45}}**: Registered Jack 45. *Connector for Ethernet cables*.
- **{{RMM}}**: Remote Monitoring and Management. *IT management software*.
- **{{RPM}}**: Revolutions Per Minute. *Hard drive speed unit*.
- **{{RSR}}**: Rapid Security Response. *Quick security updates*.
- **{{SaaS}}**: Software as a Service. *Cloud-hosted applications*.
- **{{SAML}}**: Security Assertions Markup Language. *SSO data exchange format*.
- **{{SAN}}**: Storage Area Network. *Network dedicated to storage*.
- **{{SAS}}**: Serial Attached SCSI. *Enterprise storage interface*.
- **{{SATA}}**: Serial Advanced Technology Attachment. *Computer bus interface for storage*.
- **{{SC}}**: Subscriber Connector. *Square fiber optic connector*.
- **{{SCADA}}**: Supervisory Control and Data Acquisition. *Industrial control system*.
- **{{SCSI}}**: Small Computer System Interface. *Legacy parallel interface*.
- **{{SD}}**: Secure Digital. *Memory card format*.
- **{{SDS}}**: Software-Defined Storage. *Storage managed by software*.
- **{{SFTP}}**: Secure File Transfer Protocol. *File transfer over SSH*.
- **{{SIM}}**: Subscriber Identity Module. *Card storing mobile subscriber info*.
- **{{SLA}}**: Service Level Agreement. *Contract defining service standards*.
- **{{S.M.A.R.T}}**: Self-Monitoring, Analysis, and Reporting Technology. *Drive health monitoring*.
- **{{SMB}}**: Server Message Block. *Network file sharing protocol*.
- **{{SMS}}**: Short Message Service. *Text messaging service*.
- **{{SMTP}}**: Simple Mail Transfer Protocol. *Email sending protocol*.
- **{{SNMP}}**: Simple Network Management Protocol. *Network device monitoring*.
- **{{SODIMM}}**: Small Outline Dual In-line Memory Module. *Laptop memory form factor*.
- **{{SOHO}}**: Small Office/Home Office. *Small business network environment*.
- **{{SOP}}**: Standard Operating Procedure. *Step-by-step instructions*.
- **{{SPF}}**: Sender Policy Framework. *Email spoofing prevention*.
- **{{SPICE}}**: Simple Protocol for Independent Computing Environments. *Virtual desktop protocol*.
- **{{SQL}}**: Structured Query Language. *Database management language*.
- **{{SSD}}**: Solid State Drive. *Flash-based storage device*.
- **{{SSH}}**: Secure Shell. *Encrypted remote command interface*.
- **{{SSID}}**: Service Set Identifier. *Wireless network name*.
- **{{SSO}}**: Single Sign-On. *One login for multiple services*.
- **{{ST}}**: Straight Tip. *Bayonet fiber optic connector*.
- **{{TACACS}}**: Terminal Access Controller Access-Control System. *Authentication protocol*.
- **{{TCP}}**: Transmission Control Protocol. *Reliable connection-oriented protocol*.
- **{{TKIP}}**: Temporal Key Integrity Protocol. *Legacy WPA encryption*.
- **{{TN}}**: Twisted Nematic. *Fast LCD panel type*.
- **{{TOTP}}**: Time-based One-Time Password. *Dynamic 2FA code*.
- **{{TPM}}**: Trusted Platform Module. *Hardware security chip*.
- **{{TXT}}**: Text. *DNS record type*.
- **{{UAC}}**: User Account Control. *Windows security feature*.
- **{{UDP}}**: User Datagram Protocol. *Fast connectionless protocol*.
- **{{UEFI}}**: Unified Extensible Firmware Interface. *Modern BIOS replacement*.
- **{{UPnP}}**: Universal Plug and Play. *Automatic device discovery*.
- **{{UPS}}**: Uninterruptible Power Supply. *Battery backup power*.
- **{{USB}}**: Universal Serial Bus. *Standard peripheral interface*.
- **{{USB-C}}**: Universal Serial Bus Type-C. *Reversible USB connector*.
- **{{UTM}}**: Unified Threat Management. *All-in-one security appliance*.
- **{{VA}}**: Vertical Alignment. *High-contrast LCD panel*.
- **{{VDI}}**: Virtual Desktop Infrastructure. *Centralized desktop virtualization*.
- **{{VGA}}**: Video Graphics Array. *Legacy analog video standard*.
- **{{VLAN}}**: Virtual Local Area Network. *Logical network segmentation*.
- **{{VM}}**: Virtual Machine. *Emulated computer system*.
- **{{VNC}}**: Virtual Network Computing. *Remote desktop sharing system*.
- **{{VoIP}}**: Voice over Internet Protocol. *Voice calls over network*.
- **{{VPN}}**: Virtual Private Network. *Encrypted network tunnel*.
- **{{VRAM}}**: Video Random Access Memory. *Graphics card memory*.
- **{{WAN}}**: Wide Area Network. *Large geographic network*.
- **{{WAP}}**: Wireless Access Point. *Device creating Wi-Fi network*.
- **{{WEP}}**: Wired Equivalent Privacy. *Deprecated wireless security*.
- **{{WinRM}}**: Windows Remote Management. *Windows management protocol*.
- **{{WISP}}**: Wireless Internet Service Provider. *Internet via wireless link*.
- **{{WLAN}}**: Wireless Local Area Network. *Local network using radio*.
- **{{WPA}}**: Wi-Fi Protected Access. *Wireless security standard*.
- **{{WWAN}}**: Wireless Wide Area Network. *Cellular network data*.
- **{{XaaS}}**: Anything as a Service. *General cloud service model*.
- **{{XDR}}**: Extended Detection and Response. *Cross-platform threat detection*.
- **{{XFS}}**: XFS. *High-performance 64-bit journaling file system*.
- **{{XSS}}**: Cross-Site Scripting. *Injection of malicious scripts*.

## CompTIA A+ Core 2 (220-1202) Hardware and Software List

CompTIA has included this sample list of hardware and software to assist
candidates as they prepare for the A+ Core 2 (220-1202) certification exam. This
list may also be helpful for training companies that wish to create a lab
component for their training offering. The bulleted lists below each topic are
sample lists and are not exhaustive

EQUIPMENT

- Apple tablet/smartphone
- Android tablet/smartphone
- Windows tablet
- Chromebook
- Windows laptop/Mac laptop/Linux laptop
- Windows desktop/Mac desktop/Linux desktop
- Windows server with Active Directory and Print Manager
- Monitors
- Projectors
- SOHO router/switch
- Access point (AP)
- Voice over Internet Protocol (VoIP) phone
- Printer
  - Laser/inkjet
  - Wireless
  - 3-D printer
  - Thermal
- Surge suppressor
- UPS
- Smart devices [Internet of Things (IoT) devices]
- Server with a hypervisor
- Punchdown block
- Patch panel
- Webcams
- Speakers
- Microphones

SPARE PARTS/HARDWARE

- Motherboards
- RAM
- Hard drives
- Power supplies
- Video cards
- Sounds cards
- Network cards
- Wireless network interface cards (NICs)
- Fans/cooling devices/heat sink
- CPUs
- Assorted connectors/cables
  - USB
  - High-Definition Multimedia Interface (HDMI)
  - DisplayPort
  - Digital Visual Interface (DVI)
  - Video Graphics Array (VGA)
- Adapters
  - Bluetooth adapter
- Network cables
- Unterminated network cable/connectors
- AC adapters
- Optical drives
- Screws/stand-offs
- Cases
- Maintenance kit
- Mice/keyboards
- Keyboard-Video-Mouse (KVM)
- Console cable
- Solid-state drive (SSD)

TOOLS

- Screwdrivers
- Multimeter
- Wire cutters
- Punchdown tool
- Crimper
- Power supply tester
- Cable stripper
- Standard technician toolkit
- ESD strap
- Thermal paste
- Cable tester
- Cable toner
- Wi-Fi analyzer
- Serial Advanced Technology Attachment (SATA) to USB connectors

SOFTWARE

- Operating systems
  - Linux

