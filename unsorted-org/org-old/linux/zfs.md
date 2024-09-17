---
title: Zfs
author: Justin Bealer
date_created: 2023-11-16, 04-00-30
date_modified: 2024-09-17, 09-29-54
reference: 
description: 
aliases: 
tags: 
---
# Zfs
INST_LINVAR=$(sed 's|.*linux|linux|' /proc/cmdline | sed 's|.img||g' | awk '{ print $1 }')
pacman -Sy --needed --noconfirm ${INST_LINVAR} ${INST_LINVAR}-headers zfs-${INST_LINVAR} zfs-utils
<!--ID: 1639528993421-->


linux-zen
https://archive.archlinux.org/packages/l/linux-zen/linux-zen-5.14.4.zen3-1-x86_64.pkg.tar.zst.sig
linux-zen-headers
https://archive.archlinux.org/packages/l/linux-zen-headers/linux-zen-headers-5.14.4.zen3-1-x86_64.pkg.tar.zst.sig
zfs-linux-zen
zfs-linux-zen-headers

pacman -R zfs-linux-zen zfs-linux-zen-headers
pacman -U https://archive.archlinux.org/packages/l/linux-zen/linux-zen-5.14.4.zen3-1-x86_64.pkg.tar.zst https://archive.archlinux.org/packages/l/linux-zen-headers/linux-zen-headers-5.14.4.zen3-1-x86_64.pkg.tar.zst zfs-linux-zen zfs-linux-zen-headers zfs-utils
pacman -U
https://archive.archlinux.org/packages/l/linux-zen/linux-zen-5.14.4.zen3-1-x86_64.pkg.tar.zst
https://archive.archlinux.org/packages/l/linux-zen-headers/linux-zen-headers-5.14.6.zen1-1-x86_64.pkg.tar.zst
