---
title: LPI LPIC-3 Virtualization and Containerization
author: Justin Bealer
date_created: 2024-08-30, 02-06-49
date_modified: 2024-09-17, 09-29-59
reference: 
description: 
aliases: 
tags: 
---
# LPI LPIC-3 Virtualization and Containerization

## Links

[LPIC-3 Virtualization and Containerization](https://www.lpi.org/our-certifications/lpic-3-305-overview/)
[LPIC-3 Virtualization and Containerization Exam 305 Objectives](https://www.lpi.org/our-certifications/exam-305-objectives/)

## Books

## Objectives

        4.1 Topic 351: Full Virtualization
            4.1.1 351.1 Virtualization Concepts and Theory (weight: 6)
            4.1.2 351.2 Xen (weight: 3)
            4.1.3 351.3 QEMU (weight: 4)
            4.1.4 351.4 Libvirt Virtual Machine Management (weight: 9)
            4.1.5 351.5 Virtual Machine Disk Image Management (weight: 3)
        4.2 Topic 352: Container Virtualization
            4.2.1 352.1 Container Virtualization Concepts (weight: 7)
            4.2.2 352.2 LXC (weight: 6)
            4.2.3 352.3 Docker (weight: 9)
            4.2.4 352.4 Container Orchestration Platforms (weight: 3)
        4.3 Topic 353: VM Deployment and Provisioning
            4.3.1 353.1 Cloud Management Tools (weight: 2)
            4.3.2 353.2 Packer (weight: 2)
            4.3.3 353.3 cloud-init (weight: 3)
            4.3.4 353.4 Vagrant (weight: 3)

Introduction

The description of the entire LPIC-3 program is listed here.

Version Information

These objectives are for version 3.0.

This exam results from a split of version 2.0 of the exam 304.

There is also a summary and detailed information on the changes from version 2.0 of exam 304 to 3.0 of these objectives.

The version 2.x objectives can be found here.

Translations of Objectives

The following translations of the objectives are available on this wiki:

    English
    Japanese

Objectives
Topic 351: Full Virtualization
351.1 Virtualization Concepts and Theory (weight: 6)
Weight  6
Description  Candidates should know and understand the general concepts, theory and terminology of virtualization. This includes Xen, QEMU and libvirt terminology.

**Key Knowledge Areas:**

    Understand virtualization terminology
    Understand the pros and cons of virtualization
    Understand the various variations of Hypervisors and Virtual Machine Monitors
    Understand the major aspects of migrating physical to virtual machines
    Understand the major aspects of migrating virtual machines between host systems
    Understand the features and implications of virtualization for a virtual machine, such as snapshotting, pausing, cloning and resource limits
    Awareness of oVirt, Proxmox, systemd-machined and VirtualBox
    Awareness of Open vSwitch

**The following is a partial list of the used files, terms and utilities:**

    Hypervisor
    Hardware Virtual Machine (HVM)
    Paravirtualization (PV)
    Emulation and Simulation
    CPU flags
    /proc/cpuinfo
    Migration (P2V, V2V)

351.2 Xen (weight: 3)
Weight  3
Description  Candidates should be able to install, configure, maintain, migrate and troubleshoot Xen installations. The focus is on Xen version 4.x.

**Key Knowledge Areas:**

    Understand architecture of Xen, including networking and storage
    Basic configuration of Xen nodes and domains
    Basic management of Xen nodes and domains
    Basic troubleshooting of Xen installations
    Awareness of XAPI
    Awareness of XenStore
    Awareness of Xen Boot Parameters
    Awareness of the xm utility

**The following is a partial list of the used files, terms and utilities:**

    Domain0 (Dom0), DomainU (DomU)
    PV-DomU, HVM-DomU
    /etc/xen/
    xl
    xl.cfg
    xl.conf
    xentop

351.3 QEMU (weight: 4)
Weight  4
Description  Candidates should be able to install, configure, maintain, migrate and troubleshoot QEMU installations.

**Key Knowledge Areas:**

    Understand the architecture of QEMU, including KVM, networking and storage
    Start QEMU instances from the command line
    Manage snapshots using the QEMU monitor
    Install the QEMU Guest Agent and VirtIO device drivers
    Troubleshoot QEMU installations, including networking and storage
    Awareness of important QEMU configuration parameters

**The following is a partial list of the used files, terms and utilities:**

    Kernel modules: kvm, kvm-intel and kvm-amd
    /dev/kvm
    QEMU monitor
    qemu
    qemu-system-x86_64
    ip
    brctl
    tunctl

351.4 Libvirt Virtual Machine Management (weight: 9)
Weight  9
Description  Candidates should be able to manage virtualization hosts and virtual machines (‘libvirt domains’) using libvirt and related tools.

**Key Knowledge Areas:**

    Understand the architecture of libvirt
    Manage libvirt connections and nodes
    Create and manage QEMU and Xen domains, including snapshots
    Manage and analyze resource consumption of domains
    Create and manage storage pools and volumes
    Create and manage virtual networks
    Migrate domains between nodes
    Understand how libvirt interacts with Xen and QEMU
    Understand how libvirt interacts with network services such as dnsmasq and radvd
    Understand libvirt XML configuration files
    Awareness of virtlogd and virtlockd

**The following is a partial list of the used files, terms and utilities:**

    libvirtd
    /etc/libvirt/
    virsh (including relevant subcommands)

351.5 Virtual Machine Disk Image Management (weight: 3)
Weight  3
Description  Candidates should be able to manage virtual machines disk images. This includes converting disk images between various formats and hypervisors and accessing data stored within an image.

**Key Knowledge Areas:**

    Understand features of various virtual disk image formats, such as raw images, qcow2 and VMDK
    Manage virtual machine disk images using qemu-img
    Mount partitions and access files contained in virtual machine disk images using libguestfish
    Copy physical disk content to a virtual machine disk image
    Migrate disk content between various virtual machine disk image formats
    Awareness of Open Virtualization Format (OVF)

**The following is a partial list of the used files, terms and utilities:**

    qemu-img
    guestfish (including relevant subcommands)
    guestmount
    guestumount
    virt-cat
    virt-copy-in
    virt-copy-out
    virt-diff
    virt-inspector
    virt-filesystems
    virt-rescue
    virt-df
    virt-resize
    virt-sparsify
    virt-p2v
    virt-p2v-make-disk
    virt-v2v
    virt-sysprep

Topic 352: Container Virtualization
352.1 Container Virtualization Concepts (weight: 7)
Weight  7
Description  Candidates should understand the concept of container virtualization. This includes understanding the Linux components used to implement container virtualization as well as using standard Linux tools to troubleshoot these components.

**Key Knowledge Areas:**

    Understand the concepts of system and application container
    Understand and analyze kernel namespaces
    Understand and analyze control groups
    Understand and analyze capabilities
    Understand the role of seccomp, SELinux and AppArmor for container virtualization
    Understand how LXC and Docker leverage namespaces, cgroups, capabilities, seccomp and MAC
    Understand the principle of runc
    Understand the principle of CRI-O and containerd
    Awareness of the OCI runtime and image specifications
    Awareness of the Kubernetes Container Runtime Interface (CRI)
    Awareness of podman, buildah and skopeo
    Awareness of other container virtualization approaches in Linux and other free operating systems, such as rkt, OpenVZ, systemd-nspawn or BSD Jails

**The following is a partial list of the used files, terms and utilities:**

    nsenter
    unshare
    ip (including relevant subcommands)
    capsh
    /sys/fs/cgroups
    /proc/[0-9]+/ns
    /proc/[0-9]+/status

352.2 LXC (weight: 6)
Weight  6
Description  Candidates should be able to use system containers using LXC and LXD. The version of LXC covered is 3.0 or higher.

**Key Knowledge Areas:**

    Understand the architecture of LXC and LXD
    Manage LXC containers based on existing images using LXD, including networking and storage
    Configure LXC container properties
    Limit LXC container resource usage
    Use LXD profiles
    Understand LXC images
    Awareness of traditional LXC tools

Partial list of the used files, terms and utilities:

    lxd
    lxc (including relevant subcommands)

352.3 Docker (weight: 9)
Weight  9
Description  Candidate should be able to manage Docker nodes and Docker containers. This include understand the architecture of Docker as well as understanding how Docker interacts with the node’s Linux system.

**Key Knowledge Areas:**

    Understand the architecture and components of Docker
    Manage Docker containers by using images from a Docker registry
    Understand and manage images and volumes for Docker containers
    Understand and manage logging for Docker containers
    Understand and manage networking for Docker
    Use Dockerfiles to create container images
    Run a Docker registry using the registry Docker image

Partial list of the used files, terms and utilities:

    dockerd
    /etc/docker/daemon.json
    /var/lib/docker/
    docker
    Dockerfile

352.4 Container Orchestration Platforms (weight: 3)
Weight  3
Description  Candidates should understand the importance of container orchestration and the key concepts Docker Swarm and Kubernetes provide to implement container orchestration.

**Key Knowledge Areas:**

    Understand the relevance of container orchestration
    Understand the key concepts of Docker Compose and Docker Swarm
    Understand the key concepts of Kubernetes and Helm
    Awareness of OpenShift, Rancher and Mesosphere DC/OS 

Topic 353: VM Deployment and Provisioning
353.1 Cloud Management Tools (weight: 2)
Weight  2
Description  Candidates should understand common offerings in public clouds and have basic feature knowledge of commonly available cloud management tools.

**Key Knowledge Areas:**

    Understand common offerings in public clouds
    Basic feature knowledge of OpenStack
    Basic feature knowledge of Terraform
    Awareness of CloudStack, Eucalyptus and OpenNebula

Partial list of the used files, terms and utilities:

    IaaS, PaaS, SaaS
    OpenStack
    Terraform

353.2 Packer (weight: 2)
Weight  2
Description  Candidates should be able to use Packer to create system images. This includes running Packer in various public and private cloud environments as well as building container images for LXC/LXD.

**Key Knowledge Areas:**

    Understand the functionality and features of Packer
    Create and maintain template files
    Build images from template files using different builders

Partial list of the used files, terms and utilities:

    packer

353.3 cloud-init (weight: 3)
Weight  3
Description  Candidates should able to use cloud-init to configure virtual machines created from standardized images. This includes adjusting virtual machines to match their available hardware resources, specifically, disk space and volumes. Additionally, candidates should be able to configure instances to allow secure SSH logins and install a specific set of software packages. Furthermore, candidates should be able to create new system images with cloud-init support.

**Key Knowledge Areas:**

    Understanding the features and concepts of cloud-init, including user-data, initializing and configuring cloud-init
    Use cloud-init to create, resize and mount file systems, configure user accounts, including login credentials such as SSH keys and install software packages from the distribution’s repository
    Integrate cloud-init into system images
    Use config drive datasource for testing

Partial list of the used files, terms and utilities:

    cloud-init
    user-data
    /var/lib/cloud/

353.4 Vagrant (weight: 3)
Weight  3
Description  Candidate should be able to use Vagrant to manage virtual machines, including provisioning of the virtual machine.

**Key Knowledge Areas:**

    Understand Vagrant architecture and concepts, including storage and networking
    Retrieve and use boxes from Atlas
    Create and run Vagrantfiles
    Access Vagrant virtual machines
    Share and synchronize folder between a Vagrant virtual machine and the host system
    Understand Vagrant provisioning, i.e. File and Shell provisioners
    Understand multi-machine setup

Partial list of the used files, terms and utilities:

    vagrant
    Vagrantfile

Navigation menu

    Page Discussion View source History 

    Log in 

Exam Objectives

    Linux Essentials v1.6
    Security Essentials v1.0
    Web Development Essentials v1.0
    Open Source Essentials v1.0
    LPIC-1 v5.0
    LPIC-2 v4.5
    300 Objectives v3.0
    303 Objectives v3.0
    305 Objectives v3.0
    306 Objectives v3.0
    DevOps Tools Engineer Objectives v1.0
    BSD Specialist Objectives v1.0

Search

Navigation

    Main page
    Recent changes
    LPI Website

Tools

    What links here
    Related changes
    Special pages
    Printable version
    Permanent link
    Page information

Powered by MediaWiki

    This page was last modified on 19 April 2021, at 17:25. About LPI Wiki 
