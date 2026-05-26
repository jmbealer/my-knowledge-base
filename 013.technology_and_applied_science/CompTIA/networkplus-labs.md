# Network+ Labs

## 1.0 Explaining Network Topologies

- 1.1 Networking Overview
- 1.1.7 Lab: Create Network Topologies

Explanation - Complete this lab as follows:

- Move Marketing's five computers and switch to the canvas.
  - In the tools tray, select the End Devices icon.
  - Drag the five computers to the modeler canvas.
  - In the tools tray, select the Switches icon.
  - Drag the Mktg_Switch switch to the canvas.
- Connect the devices to create a star topology.
  - In the tools tray, select the Create Link icon.
  - Select Mktg1 and select the Ethernet port.
  - Select Mktg_Switch and select an open port.
  - Repeat the process for Mktg2-Mktg5.

- 1.3 SOHO Networks

- 1.3.8 Lab: Explore a Single Location in a Lab

Explanation Complete this lab as follows:

1. Add a monitor to the Office 2 computer.

- Under Office 2, select Hardware to go to the workstation.
- Under Shelf, expand Monitors.
- Drag the monitor from the Shelf to the bench next to the computer.

1. Connect the monitor to the computer.

- Above the monitor, select Back to switch to the back view of the monitor.
- Above the computer, select Back to switch to the back view of the computer.
- Under Shelf, expand Cables.
- Select HDMI to HDMI Cable.
- From the Selected Component pane:
  - Drag an HDMI Connector to the HDMI port on the back of the computer.
  - Drag the other HDMI Connector to the HDMI port on the back of the monitor.

1. Plug in the monitor.

- Under Shelf, select AC Power Cable.
- From the Selected Component pane:
  - Drag the AC Power Connector (Female) to the monitor power port.
  - Drag the AC Power Connector (Male) to the unused power port on the wall
    plate.

1. Add the keyboard and mouse.

- Under Shelf, expand Input Devices.
- Drag the Keyboard to an empty USB port on the back of the computer.
- Drag the Mouse to an empty USB port on the back of the computer.

1. Power on the monitor and computer.

- Above the monitor, select Front to switch to the front view of the monitor.
- Above the computer, select Front to switch to the front view of the computer.
- Select the power button on the monitor.
- Select the power button on the computer.
- The computer startup process begins, and you are automatically signed into
  Windows 11.
- Right-click Start and then select Settings to explore the operating system
  simulator's capabilities.
- From the top menu (left side), select Office 2 to switch back to the Hardware
  view.

- 1.3.9 Lab: Create a Home Wireless Network Explanation Complete this lab as
  follows:

- Add the wireless access point to the workspace.
  - Under Shelf, expand Wireless Access Points.
  - Drag the Wireless Access Point, 802.11b/g/n wireless access point to the
    workspace.
    - For convenience, place the access point next to the existing router.
  - Above the router, select Back to view the back of the router.
  - Above the access point, select Back to view the back of the wireless access
    point.
- Connect power to the wireless access point.
  - Under Shelf, expand Cables.
  - Select Power Adapter, AC to DC.
  - From the Selected Component pane:
    - Drag the DC power connector to the port on the wireless access point.
    - Drag the AC power adapter end to an empty outlet on the wall outlet or the
      surge protector.
- Connect the Ethernet cable to the wireless access point and existing router.
  - Under Shelf, select the Cat6a Cable, RJ45 Ethernet cable.
  - From the Selected Component pane:
    - Drag an RJ45 Ethernet connector to the back of the access point.
    - Drag the unconnected RJ45 Ethernet connector to one of the free LAN ports
      on the router.
- Configure the homeowner's laptop to connect to a wireless network.
  - From the front of the laptop, slide the wireless switch to the ON position
    (right) to enable the integrated wireless network interface.
- Configure the homeowner's laptop to connect automatically to the HomeNet-AC
  wireless network.
  - On the Home-Laptop monitor, select Click to view Windows 11.
  - In the notification area, select the globe icon, then select the arrow next
    to the wireless icon.
  - Select the HomeNet-AC wireless network.
  - Select Connect automatically and then select Connect.

- To confirm the connection, right-click the wireless networking icon in the
  notification area again and select Network and Internet settings. The image on
  the Status page shows a connection to the internet.

- 1.3.10 Lab: Create a SOHO Network Explanation Complete this lab as follows:

- Add the computers to the canvas
  - In the tools tray, select the End Devices icon.
  - Drag all three computers to the modeler canvas.
- Add the switch to the canvas
  - In the tools tray, select the Switches icon.
  - Drag the switch to the modeler canvas.
- Add the router to the canvas
  - In the tools tray, select the Routers icon.
  - Drag the router to the modeler canvas.
- Connect the switch to the router
  - In the tools tray select the Create Link icon.
  - Click on the Router and select Port 0.
  - Click on the switch and select an open port.
- Connect the computers to the switch
  - In the tools tray, make sure the Create Link icon is selected.
  - Click on Home-PC1 and select the Ethernet port.
  - Click on the Switch and select an open port.
  - Click on Home-PC2 and select the Ethernet port.
  - Click on the switch and select an open port.
  - Click on Home-Laptop and select the Ethernet port.
  - Click on the switch and select an open port.
  - Select Create Link to end the link tool.
- Verify that a DHCP address is assigned
  - Right-click Home-PC1 and select Launch Windows.
  - In the system tray, right-click the network icon and select Network and
    Internet Settings.
  - Select Ethernet and scroll down to the assigned IP address.
  - Select Questions and answer the questions.
  - Minimize the Lab Questions dialog.
  - If the network is still not showing a proper connection, restart the
    Home-PC1 computer. This will force the computer to request an updated IP
    address from the router.
- Verify connectivity by pinging the gateway
  - Right-click Start and select Terminal (Admin).
  - In the terminal window type ping 192.168.1.1.
  - Press Enter.

- 1.4 Troubleshooting Methodology
- 1.4.10 Lab: Troubleshooting Methodology Explanation Complete this lab as
  follows:

- First, connect the two computers to the switch using the Create Link tool.
  - In the tools tray, select Create Link.
  - Select the Office1 computer and Ethernet, then select the Switch and any
    port.
  - Select the Home-Laptop computer and select Ethernet, then select the Switch
    and select any available port.
  - Select Create Link to end the link tool.
- Verify that Office1 can reach an external website.
  - Right-click Office1 and select Launch Windows.
  - Launch Chrome from the taskbar. Type in rmksupplies.com and press Enter.
  - The browser says, "This site can't be reached."
  - Something isn't working as expected. Let's identify the problem.
- Verify that Home-Laptop can reach an external website.
  - In the upper left, select Network Modeler.
  - Right-click Home-Laptop and select Launch Windows.
  - Launch Chrome from the taskbar. Type in rmksupplies.com and press Enter.
  - Notice that the website loads correctly. Internet access is working for this
    computer.
  - The connectivity problem seems to be localized to the Office1 computer.
- Let's theorize what might be causing the problem.
  - The IP configuration of Office1 might not be correct.
  - The cable might be bad that we plugged into Office1.
  - The NIC in Office1 might be bad.
  - The port on the switch might be bad.
  - Let's test our theories until we find one that appears to be the problem.
- Compare the IP configuration of the machine that is working to the one that is
  not working.
  - On Home-Laptop, right-click the network icon and select Network & Internet
    settings.
  - Select Ethernet and scroll down to view the IP assignment information.
  - Note that Home-Laptop is configured for DHCP (Automatic configuration).
  - In the upper left, select Network Modeler.
  - Right-click Office1 and select Launch Windows.
  - On Office1, right-click the network icon and select Network & Internet
    settings.
  - Select Ethernet and scroll down to view the IP assignment information.
  - Note that Office1 has a manually assigned IP address.
- Implement a fix.
  - Let's try changing the IP configuration of Office1 to match Home-Laptop.
  - Under IP assignment, select Edit.
  - Under Edit IP settings, select Automatic (DHCP) and select Save.
- Test the fix.
  - On Office1, try browsing to rmksupplies.com.
  - Did that fix the problem?

## 2.0 Supporting Cabling and Physical Installations

- 2.1 Ethernet
  - 2.1.8 Lab: Reconnect to an Ethernet Network Task Summary Required Actions
    - Install the 1000BaseTX PCIe network adapter
    - Connect the computer to the network using Cat5e cable
    - Verify that Office2 can communicate with the local network and the
      internet Explanation Complete this lab as follows:

    - Add the 1000Base TX adapter to the Office 2 computer.
      - Above the computer, select Motherboard to switch to the motherboard view
        of the computer.
      - Under Shelf, expand Network Adapters. Identify the network adapter that
        has the fastest Ethernet speed.
      - Under Shelf, drag the Network adapter, Ethernet 1000BaseTX, PCIe network
        adapter to a free PCIe slot on the computer.
    - Connect the computer to the network.
      - Above the computer, select Back to switch to the back view of the
        computer.
      - Drag the RJ45 Shielded Connector from the motherboard's NIC to the port
        of the 1000BaseTX network adapter.
    - Verify the connection to the local network and the internet.
      - Above the computer, select Front to switch to the front view of the
        computer.
      - Select the power button on the computer case. Wait for the operating
        system to start.
      - Right-click Start and then select Settings.
      - Select Network & Internet. The diagram should indicate an active
        connection.

- 2.2 Copper Cables and Connectors
  - 2.2.7 Lab: Connect to an Ethernet Network Task Summary Required Actions
    - Connect the Ethernet cable connected to computer
    - Connect the Ethernet cable to the wall outlet Explanation Complete this
      lab as follows:

    - Access the back view of the computer in Office 1.
      - Under Office 1, select Hardware.
      - Above the computer, select Back to switch to the back view of the
        computer.
    - Connect the RJ45 cable to the computer and the wall plate.
      - Under Shelf, expand Cables.
      - Select the Cat6a Cable, RJ45 cable.
      - From the Selected Component window:
        - Drag an RJ45 Shielded Connector to the Ethernet port on the computer.
        - Drag the other RJ45 Shielded Connector to the Ethernet port on the
          wall outlet.
    - Test the connection to the internet.
      - On the computer monitor, select Click to view Windows 11 to view the
        running operating system.
      - Right-click Start and then select Settings.
      - Select Network & internet
      - The diagram should indicate an active connection.

  - 2.2.8 Lab: Connect a Cable Modem Task Summary Required Actions
    - Connect the cable modem to the internet using the RG-6 cable
    - Connect the computer to the cable modem using the Ethernet cable Plug in
      the cable modem Confirm that the computer is properly connected to the
      internet Explanation Complete this lab as follows:

    - Add the cable modem to the workspace.
      - Under Shelf, expand Routers.
      - Drag the Cable Modem/Router from the shelf to the workspace.
      - Select Back to switch to the back view of the cable modem.
    - Connect the modem to the WAN connection.
      - Under Shelf, expand the Cables category.
      - Select the Coaxial Cable, RG-6 cable.
      - From the Selected Component pane:
        - Drag a Coaxial Type F connector to the applicable port on the cable
          modem.
        - Drag the other Coaxial Type F connector to the applicable port on the
          wall plate.
    - Connect the computer to the cable modem.
      - Over the computer, select Back to switch to the back view of the
        computer.
      - Under Shelf, select the Cat6a Cable, RJ45 cable.
      - From the Selected Component pane:
        - Drag an RJ45 Shielded Connector to the Ethernet port on the cable
          modem.
        - Drag the other RJ45 Shielded Connector to the Ethernet port on the
          computer (not the Ethernet card in the slot).
    - Provide power to the modem.
      - Under Shelf, select the Power Adapter, AC to DC.
      - From the Selected Component pane:
        - Drag the DC Power Connector to the port on the cable modem.
        - Drag the AC Power Adapter end to the power outlet.
    - Verify that the computer is connected to the internet.
      - On the monitor, select Click to view Windows 11.
      - From the notification area, right-click the Network icon and select
        Network and Internet settings.
      - The diagram should indicate an active connection.

- 2.3 Wiring Implementation
  - 2.3.6 Lab: Explore Multiple Locations in a Lab

    Task Summary Required Actions
    - Install the PCIe network adapter.Hide Details
    - Ensure the computer is unplugged if any internal components are modified
      or added.
    - Installed PCIe 1x network card.
    - Connect the networking cable between the wall plate and the computer.Hide
      Details
    - Connect the Ethernet cable to the wall plate.
    - On the computer, connect the cable to the built-in network adapter on the
      motherboard or one of the recently installed network adapters in the
      expansion slots.
    - Turn the computer on after installing the network adapters.
    - In the Networking Closet, remove the power cable from the wall plate.
      Explanation Complete this lab as follows:

    - For safety, power off the Office 2 computer and unplug the computer from
      the power source before working with internal components.
      - Under Office 2, select Hardware to view the hardware for this office.
      - On the computer, select the power button to turn the computer off.
      - Select Back to switch to the back view of the computer.
      - Unplug the AC power cable.
    - Install the PCIe network adapter in the Office 2 computer's free PCIe (x1)
      slot.
      - Above the computer, select Motherboard to switch to the motherboard view
        of the computer.
      - Under Shelf, expand Network Adapters.
      - Drag the PCIe Network Adapter to the applicable free PCIe (x1) slot on
        the motherboard.
      - Select Back to switch to the back view of the computer.
      - Reconnect the AC power cable.
    - Connect an Ethernet cable to the network card in the computer and to the
      wall plate.
      - Ensure you are using the Back view of the Office 2 computer.
      - Under Shelf, expand Cables.
      - Select the Networking Cable.
      - From the Selected Component pane:
        - Drag an RJ45 Connector to the built-in port or the port on the PCIe
          network card.
        - Drag the unconnected RJ45 Connector to the network port on the wall
          plate (the left port).
    - Turn the computer on and test for network and internet connectivity.
      - Above the computer, select Front.
      - Select the power button on the computer.
      - The computer startup process begins and you are automatically logged
        into Windows.
      - Right-click Start and select Settings to open the Microsoft Settings
        app.
      - Select Network & Internet.
      - Notice that in the Status pane, the image shown indicates a connection
        to the network.
    - Test to see if the uninterruptable power supply is functioning properly in
      the networking closet.
      - From the top left navigation tabs, select Floor 1.
      - Under Networking Closet, select Hardware.
      - From the wall outlets, unplug the AC power connectors (Male) by dragging
        them to the side.
      - Notice that the power and activity lights on the rack-mounted networking
        devices are still flickering (zoom in if necessary). Also notice that
        the monitors are still on.

  - 2.3.7 Lab: Connect Network Devices

Task Summary Required Actions

- Connect the fiber network on Floor 1Hide Details
  - Connect the SFP transceiver (LC) to the switch
  - Connect the LC connector to the SFP transceiver on the switch
  - Connect the SC connector A to port 3 on the fiber patch panel
  - Connect the SC connector B to port 4 on the fiber patch panel
- Connect the fiber network on Floor 2Hide Details
  - Connect the SFP transceiver (LC) to the switch
  - Connect the LC connector to the SFP transceiver on the switch
  - Connect the SC A connector to port 1 on the fiber patch panel
  - Connect the SC B connector to port 2 on the fiber patch panel
- Plug the switch on Floor 2 into a Critical Load outlet
- Computers on Floor 2 are connected to the internet

Explanation While completing this lab, use the following information:

- SC connectors have square connectors that are pushed in to connect.
  - Fiber white SC connector
  - Fiber black SC connector
- LC connectors have both connectors linked together.
  - Fiber LC connectors

Complete this lab as follows:

- Install the SFP Transceiver (LC) in the networking closet on Floor 1.
  - Under Shelf, expand the Adapters.
  - Drag the SFP Transceiver (LC) to the SFP 2 port on the switch.
- Connect the fiber cable to the switch.
  - Under Shelf, expand Cables.
  - Select Cable, Fiber, SC to LC.
  - From the Selected Component pane:
    - Drag Connector, Fiber, Duplex LC Multi-mode, Male to the SFP LC port
      (plugged into SFP2) on the switch.
    - Drag the Fiber Optic SC Connector (A) to port 3 on the fiber patch panel.
    - Drag the Fiber Optic SC Connector (B) to port 4 on the fiber patch panel.
- Access the networking closet on floor 2.
  - From the top left, select Floor 1.
  - Under Building A, select Floor 2.
  - Under Networking Closet 2, select Hardware.
- Connect the fiber cable to switches on Floor 2.
  - Under Shelf, expand Adapters.
  - Drag SFP Transceiver (LC) to an open SFP port on the switch.
  - Under Shelf, expand Cables.
  - Select Cable, Fiber, SC to LC.
  - From the Selected Component pane:
    - Drag the Connector, Fiber, Duplex LC, Multi-mode, Male to the SFP port.
    - Drag the Fiber Optic SC Connector (A) to port 1 on the fiber patch panel.
    - Drag the Fiber Optic SC Connector (B) to port 2 on the fiber patch panel.
- Plug the switch on Floor 2 into a bank 1 critical load outlet on the UPS.
  - Above the rack, select Back to switch to the back view of the rack.
  - Under Shelf, select AC Power Cable.
  - From the Select Connector pane:
    - Drag AC Power Connector (Female) to the AC port on the back of the switch.
    - Drag the AC Power Connector (Male) to an open bank 1 critical load outlet.
  - Above the rack, select Front to switch to the front view and confirm that
    the network switch has power.
- Verify that there is an internet connection for any Floor 2 computer.
  - From the top left, select Floor 2.
  - Select any of the computers on Floor 2.
  - Right-click Start and then select Settings.
  - Select Network & Internet.
  - The image shown should indicate a connection to the internet.

  - 2.3.8 Lab: Connect Patch Panel Cables 1

Task Summary Required Actions

- In the Networking Closet, connect an Ethernet twisted-pair cable between the
  Off 1 port on the patch panel and port 3 on the switch
- In Office 1, connect an Ethernet twisted-pair cable between the workstation
  and the wall outlet
- In Office 1, configure the workstation to obtain IP and DNS addresses
  automaticallyHide Details
  - Obtain the IP address automatically through DHCP
  - Obtain the DNS address automatically

Explanation Complete this lab as follows:

- From the Networking Closet, connect the patch panel and switch.
  - Under Shelf, expand Cables.
  - Select the Cat6a Cable, RJ45 cable.
  - From the Selected Component pane:
    - Drag an RJ45 Shielded Connector to the Off 1 (Office 1) port on the patch
      panel.
    - Drag the other RJ45 Shielded Connector to port 3 on the Cisco switch (top
      row, third port from the left).
- Connect the Office1 workstation to the local area network.
  - From the top left, select Floor 1 Overview.
  - In Office 1, select Hardware.
  - Above the computer, select Back to switch to the back view of the computer.
  - Under Shelf, expand Cables.
  - Select Cat6a Cable, RJ45.
  - From the Selected Component pane:
    - Drag an RJ45 Shielded Connector to the Ethernet port on the computer.
    - Drag the other RJ45 Shielded Connector to the open Ethernet port on the
      wall outlet.
- Configure the workstation to obtain IP and DNS addresses automatically from
  the server on the network.
  - On the Office1 monitor, select Click to view Windows 11.
  - From the Windows taskbar, right-click Start and then select Settings.
  - Select Network & internet.
  - Select Ethernet and then next to IP assignment, select Edit.
  - Change the Edit IP settings drop-down to Automatic (DHCP), then click Save.
  - At the top of the Settings dialog, select Network & internet.
  - The globe icon next to the word Connected indicates the machine is now
    connected to the network and can access the internet.

  - 2.3.9 Lab: Connect Patch Panel Cables 2

Task Summary Required Actions

- In the Networking Closet, connect a patch cable between the Exec 1 port on the
  patch panel and port 1 on the switch
- In the Networking Closet, connect a patch cable between the Supp port on the
  patch panel and port 6 on the switch
- In the Networking Closet, connect a patch cable between the Lobby port on the
  patch panel and port 8 on the switch

Explanation While completing this lab, use the following port information.

Patch Panel Port	Cisco Switch Port Exec 1	Port 1 Supp	Port 6 Lobby	Port 8

Complete this lab as follows:

- From the Networking Closet, attach an Ethernet cable from the patch panel to
  the switch port.
  - Under Shelf, expand Cables.
  - Select the Cat6a Cable, RJ45.
  - From the Selected Component pane:
    - Drag an RJ45 Shielded Connector to the Exec 1 port on the patch panel.
    - Drag the other RJ45 Shielded Connector to the correct port on the Cisco
      switch (top row).
    - 28 port switch
- Repeat steps 1b-1c for the Supp and Lobby ports.

- 2.4 Fiber Optic Cables and Connectors
  - 2.4.8 Lab: Connect Fiber Optic Cables

- Connect the LC connector to the SFP module on the switch
- Connect the ST A connector to the Tx port on the computer
- Connect the ST B connector to the Rx port on the computer
- Disconnect the Ethernet cable from the CorpiSCSI serverHide Details
  - Removed from the switch and the server
    - Removed RJ45 cable from the Cisco switch
    - Removed RJ45 cable from the server
  - Place RJ45 cable on shelf

Explanation

- To determine which network components to use, examine the ports on the switch
  and the CorpiSCSI server.
  - The SFP module installed in the switch uses LC connectors.
  - SFP Front
  - The fiber optic NIC installed in the CorpiSCSI server uses ST connectors.
  - RX plugTX plug
- The ST to LC fiber cable is the only cable that can be used to connect the
  switch and the server.
  - LC connectors have two connectors linked together. LC connectors can only be
    inserted one way.
  - Fiber LC cable
  -
  - ST connectors twist on using a BNC connector. An ST cable has two
    color-coded ST connectors. They have one for transmit (Tx) and one for
    receive (Rx).
  - Fiber ST red connector
  - Fiber ST black connector

Complete this lab as follows:

- Connect the fiber ST to LC cable to the SFP port.
  - Under Shelf, expand Cables.
  - Drag the Cable, Fiber, ST to LC cable to the SFP 1 LC port on the switch.
  - In the Select Connector window, select the Connector, Fiber, Duplex LC,
    Multi-mode, Male.
- Connect the fiber ST to LC cable to the TX and RX ports.
  - Above the rack, select Back to switch to the back view.
  - From the Selected Component pane:
    - Drag the ST Connector (A) to the TX port on the CorpiSCSI server (the
      bottom server).
    - Drag the ST Connector (B) to the RX port on the CorpiSCSI server.
- Disconnect the Cat6a RJ45 cable from the CorpiSCSI server and switch.
  - Drag the RJ45 connector from the back of the server to the Shelf.
  - Above the rack, select Front to view the front of the rack.
  - Drag the highlighted RJ45 connector from the switch to the Shelf.
- Verify that the CorpiSCSI server is connected to the network.
  - On the CorpiSCSI's monitor, select Click to view Windows Server 2019.
  - Right-click Start and select Settings.
  - Select Network & Internet.
  - Verify that Ethernet 3 is connected to CorpNet.local.

- 2.6 Cable Troubleshooting
  - 2.6.10 Lab: Explore Physical Connectivity 1
  - 2.6.11 Lab: Explore Physical Connectivity 2
  - 2.6.12 Lab: Troubleshoot Physical Connectivity 1
  - 2.6.13 Lab: Troubleshoot Physical Connectivity 2
  - 2.6.14 Lab: Troubleshoot Physical Connectivity 3
  - 2.6.15 Lab: Troubleshoot Physical Connectivity 4

## 3.0 Configuring Interfaces and Switches

- 3.1 Network Interfaces
- 3.1.8 Lab: Select and Install a Network Adapter
- 3.1.9 Lab: Connect a Media Converter
- 3.2 Ethernet Switches
- 3.2.7 Lab: Install a Switch in the Rack
- 3.2.8 Lab: Secure a Switch
- 3.2.9 Lab: Cisco IOS Basics
- 3.3 Switch Port Configuration
- 3.3.6 Lab: Configure Port Aggregation
- 3.3.7 Lab: Enable Jumbo Frame Support
- 3.3.8 Lab: Configure PoE
- 3.4 Switch Troubleshooting
- 3.4.8 Lab: Troubleshoot Disabled Ports
- 3.4.9 Lab: Switching Loop

## 4.0 Configuring Network Addressing

- 4.1 Internet Protocol Basics
- 4.1.6 Lab: Explore Packets and Frames
- 4.1.7 Lab: Explore ARP in Wireshark
- 4.2 IP Version 4 Addressing
- 4.2.9 Lab: Configure IP Addresses
- 4.2.10 Lab: Configure IP Addresses on Mobile Devices
- 4.2.11 Lab: Configure IP Addresses on Linux
- 4.3 IP Version 4 Subnetting
- 4.3.7 Lab: Configure IP Networks and Subnets
- 4.4 IP Troubleshooting Tools
- 4.4.5 Lab: IPv4 Troubleshooting Tools
- 4.4.6 Lab: IPv4 Troubleshooting tools for Linux
- 4.4.7 Lab: Use IPv4 Test Tools
- 4.5 IP Version 6
- 4.5.9 Lab: Configure an IPv6 Address
- 4.6 IP Troubleshooting
- 4.6.4 Lab: Use ping and tracert on Windows
- 4.6.5 Lab: Use ping and traceroute on Linux
- 4.6.6 Lab: Assisted Troubleshooting 1
- 4.6.7 Lab: Assisted Troubleshooting 2
- 4.6.8 Lab: Assisted Troubleshooting 3
- 4.6.9 Live Lab: Explore the VM Lab Environment
- 4.6.10 Applied Live Lab: Troubleshoot IP Configuration

## 5.0 Configuring Routing and Advanced Switching

- 5.1 Routing Technologies
- 5.1.9 Lab: Install an Enterprise Router
- 5.1.10 Lab: Cisco Troubleshooting Tools
- 5.3 Network Address Translation
- 5.3.4 Lab: Configure NAT
- 5.5 Enterprise Network Topologies
- 5.5.4 Lab: Create a Three-Tier Network
- 5.6 Virtual LANs
- 5.6.8 Lab: Configure Switch IP and VLAN - GUI
- 5.6.9 Lab: Create VLANs - GUI
- 5.6.10 Lab: Configure Trunking
- 5.6.11 Lab: Configure Switch IP Settings - CLI
- 5.6.12 Lab: Configure Management VLAN Settings - CLI

## 6.0 Implementing Network Services

- 6.1 Transport and Application Layer Protocols
- 6.1.7 Lab: Explore Three-Way Handshake in Wireshark
- 6.1.8 Lab: View Open Ports with netstat
- 6.2 Dynamic Host Configuration Protocol
- 6.2.5 Lab: Configure a DHCP Server
- 6.2.6 Lab: Configure DHCP Server Options
- 6.2.7 Lab: Create DHCP Exclusions
- 6.2.8 Lab: Create DHCP Client Reservations
- 6.2.10 Lab: Configure Client Addressing for DHCP
- 6.3 APIPA and SLAAC
- 6.3.4 Lab: Explore APIPA Addressing
- 6.3.5 Lab: Explore APIPA Addressing in Network Modeler
- 6.4 DHCP Relay and Troubleshooting
- 6.4.4 Lab: Configure a DHCP Relay Agent
- 6.4.5 Lab: Add a DHCP Server on Another Subnet
- 6.4.6 Lab: Troubleshoot Address Pool Exhaustion
- 6.4.7 Applied Live Lab: Troubleshoot Address Pool Exhaustion
- 6.4.8 Lab: Explore DHCP Troubleshooting
- 6.4.9 Lab: Troubleshoot IP Configuration 1
- 6.4.10 Lab: Troubleshoot IP Configuration 2
- 6.4.11 Lab: Troubleshoot IP Configuration 3
- 6.5 Domain Name System
- 6.5.11 Lab: Configure DNS Addresses
- 6.5.12 Lab: Create Standard DNS Zones
- 6.5.13 Lab: Create Host Records
- 6.5.14 Lab: Create CNAME Records
- 6.5.15 Lab: Troubleshoot DNS Records
- 6.5.17 Applied Live Lab: Configure DNS Records
- 6.6 DNS Troubleshooting
- 6.6.5 Lab: Explore nslookup
- 6.6.6 Lab: Use nslookup
- 6.6.7 Applied Live Lab: Report DNS Configuration

## 7.0 Explaining Application Services

- 7.1 Application Security and Time Synchronization
- 7.1.4 Lab: Configure NTP on Linux
- 7.1.5 Applied Live Lab: Troubleshoot Time Synchronization Issues
- 7.2 Web, File, Print, and Database Services
- 7.2.8 Live Lab: Verify Secure Web Services
- 7.2.9 Lab: Scan for Web Services with Nmap
- 7.3 Email and Voice Services
- 7.3.6 Lab: Connect VoIP 1
- 7.3.7 Lab: Connect VoIP 2
- 7.4 Disaster Recovery and High Availability
- 7.4.8 Lab: Configure NIC Teaming
- 7.4.9 Live Lab: Configure First Hop Redundancy

## 8.0 Supporting Network Management

- 8.1 Organizational Policies and Documentation
- 8.1.3 Live Lab: Backup and Restore Network Appliances
- 8.1.12 Lab: Update Firmware
- 8.1.13 Live Lab: Update Network Documentation
- 8.2 Host Discovery and Monitoring
- 8.2.8 Lab: Scan Using Zenmap
- 8.2.9 Applied Live Lab: Perform Network Discovery
- 8.3 Simple Network Management Protocol
- 8.3.6 Applied Live Lab: Configure SNMP
- 8.4 Event Management
- 8.4.6 Lab: Configure Logging in pfSense
- 8.4.7 Lab: Evaluate Event Logs in pfSense
- 8.4.8 Lab: Auditing Device Logs on a Cisco Switch
- 8.4.9 Lab: Configure Logging on Linux
- 8.4.10 Lab: View Event Logs
- 8.4.11 Live Lab: Configure Log Collection
- 8.5 Packet Capture and Analysis
- 8.5.5 Lab: Troubleshoot with Wireshark
- 8.5.6 Lab: Configure Port Mirroring
- 8.6 Traffic Monitoring
- 8.6.7 Lab: Configure QoS
- 8.6.9 Live Lab: Configure Flow Collection and Analysis
- 8.6.10 Applied Live Lab: Troubleshoot Network Service Issues

## 9.0 Explaining Network Security Concepts

- 9.1 Security Concepts
- 9.1.7 Lab: Create a Honeypot
- 9.2 Network Threats and Attacks
- 9.2.5 Lab: Analyze a DoS Attack
- 9.2.6 Lab: Analyze a DDoS Attack
- 9.3 Spoofing Attacks
- 9.3.7 Lab: Poison ARP and Analyze with Wireshark
- 9.3.8 Lab: Spoof MAC Addresses with SMAC
- 9.3.9 Lab: Perform a DHCP Spoofing On-Path Attack
- 9.4 Rogue System Attacks
- 9.4.6 Lab: Discover a Rogue DHCP Server
- 9.4.7 Lab: Configure DHCP Snooping
- 9.4.8 Lab: Poison DNS
- 9.4.9 Lab: Analyze DNS Spoofing
- 9.4.10 Applied Live Lab: Analyze Network Attacks
- 9.5 Social Engineering
- 9.5.3 Lab: Respond to Social Engineering Exploits
- 9.5.4 Lab: Crack a Password with John the Ripper

## 10.0 Applying Network Security Features

- 10.1 Authentication
- 10.1.9 Live Lab: Deploy a Digital Certificate
- 10.2 Authorization and Account Management
- 10.2.5 Lab: Manage Account Policies
- 10.2.6 Live Lab: Configure Management Privileges
- 10.3 Network Hardening
- 10.3.3 Lab: View Linux Services
- 10.3.5 Lab: Scan for Unsecure Protocols
- 10.3.6 Lab: Enable and Disable Linux Services
- 10.3.7 Lab: Disable Network Service
- 10.4 Switch Security
- 10.4.2 Lab: Secure Access to a Switch
- 10.4.3 Lab: Secure Access to a Switch 2
- 10.4.4 Lab: Disable Switch Ports - GUI
- 10.4.7 Lab: Harden a Switch
- 10.5 Network Security Rules
- 10.5.6 Lab: Configure Network Security Appliance Access
- 10.5.7 Lab: Configure a Security Appliance
- 10.5.8 Lab: Configure a Perimeter Firewall
- 10.5.9 Lab: Restrict Telnet and SSH Access
- 10.5.10 Lab: Permit Traffic
- 10.5.11 Lab: Block Source Hosts
- 10.5.12 Applied Live Lab: Troubleshoot Service and Security Issues

## 11.0 Supporting Network Security Design

- 11.1 Zone-based Security
- 11.1.5 Lab: Configure a Screened Subnet (DMZ)
- 11.1.6 Lab: Configure Screened Subnets
- 11.1.9 Lab: Implement Intrusion Prevention
- 11.2 Internet of Things
- 11.2.5 Lab: Scan for IoT Devices
- 11.3 Physical Security
- 11.3.4 Lab: Implement Physical Security

## 12.0 Configuring Wireless Networks

- 12.1 Wireless Concepts and Standards
- 12.1.9 Lab: Configure Wireless Profiles
- 12.2 Enterprise Wireless Network Design
- 12.2.8 Lab: Design an Indoor Wireless Network
- 12.2.9 Lab: Design an Outdoor Wireless Network
- 12.2.10 Lab: Implement an Enterprise Wireless Network
- 12.3 Wireless Security
- 12.3.7 Lab: Configure a Captive Portal
- 12.3.8 Lab: Create a Guest Network for BYOD
- 12.3.9 Lab: Secure an Enterprise Wireless Network
- 12.3.10 Lab: Secure a Home Wireless Network
- 12.3.11 Lab: Enable Wireless Intrusion Prevention
- 12.4 Wireless Troubleshooting
- 12.4.7 Lab: Explore Wireless Network Problems
- 12.4.8 Lab: Troubleshoot Wireless Network Problems
- 12.4.9 Lab: Optimize a Wireless Network

## 13.0 Comparing Remote Access Methods

- 13.2 Virtual Private Networks
- 13.2.8 Lab: Configure a Remote Access VPN
- 13.2.9 Lab: Configure an iPad VPN Connection
- 13.2.10 Lab: Configure a RADIUS Solution
- 13.3 Remote Management
- 13.3.8 Lab: Allow Remote Desktop Connections
- 13.3.9 Lab: Use PowerShell Remote
- 13.3.10 Live Lab: Configure a Jump Box

## 14.0 Summarizing Cloud Concepts

- 14.1 Datacenter and Storage Networks
- 14.1.5 Lab: Configure an iSCSI Target
- 14.1.6 Lab: Configure an iSCSI Initiator
- 14.2 Cloud Concepts
- 14.2.5 Live Lab: Deploy a Cloud VM
- 14.3 Cloud Networking
- 14.3.7 Live Lab: Configure Cloud Networking
