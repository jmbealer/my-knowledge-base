# RHCSA Study Guide (EX200)

- Site: [Red Hat Certified System Administrator (RHCSA)](https://www.redhat.com/en/services/certification/rhcsa)

## 1. Understand and Use Essential Tools

### Shell & Commands
- **Syntax**: `command [-options] [arguments]`
- **History**: Use `history` to see commands. `!n` to run command n. `ctrl+r` to search.
- **Escaping**: Use `\` to escape special characters.

### Redirection & Pipes
- `>`: Redirect STDOUT to file (overwrite). `echo "hi" > file`
- `>>`: Redirect STDOUT to file (append). `echo "hi" >> file`
- `2>`: Redirect STDERR to file. `ls fakefile 2> errors.txt`
- `&>`: Redirect STDOUT and STDERR to file.
- `|`: Pipe. Passes STDOUT of command 1 to STDIN of command 2. `ls | grep txt`

### Grep & Regex
- **Grep**: `grep [options] "pattern" file`
  - `-i` (ignore case), `-r` (recursive), `-v` (invert match).
- **Regex**:
  - `^`: Start of line. `^root`
  - `$`: End of line. `bash$`
  - `.`: Any single character.

### Remote Access (SSH)
- **Connect**: `ssh user@hostname`
- **Keys**: `ssh-keygen -t rsa` (Generate), `ssh-copy-id user@host` (Install).
- **Config**: `/etc/ssh/sshd_config` (Server), `~/.ssh/config` (Client).

### Multiuser Targets (Switching Users)
- **Login**: `ssh`, GUI, or TTY (`ctrl+alt+F1-F6`).
- **Switch User**:
  - `su - user`: Switch with full login environment (Recommended).
  - `su user`: Switch but keep current environment vars.
  - `sudo -i`: Get a root shell.

### Archives (tar)
- **Create**: `c`, **Extract**: `x`, **List**: `t`.
- **File**: `f` (always required).
- **Compression**: `z` (gzip), `j` (bzip2), `J` (xz).
- **Examples**:
  - Create Gzip: `tar -czvf archive.tar.gz /folder`
  - Extract: `tar -xzvf archive.tar.gz`

### File Management
- **Create**: `touch file`, `mkdir -p dir/subdir`
- **Copy**: `cp source dest`, `cp -r dir dest`
- **Move/Rename**: `mv source dest`
- **Delete**: `rm file`, `rm -rf dir` (Careful!)
- **Links**:
  - **Hard Link**: `ln file link` (Same inode, cannot span filesystems).
  - **Soft Link**: `ln -s /path/to/target link` (Pointer, can span filesystems).

### Permissions (UGO/RWX)
- **Structure**: `rwx` (User) - `rwx` (Group) - `rwx` (Other).
- **Values**: Read (4), Write (2), Execute (1).
- **Chmod**:
  - Symbolic: `chmod u+x file`, `chmod g-w file`.
  - Numeric: `chmod 755 file` (rwxr-xr-x), `chmod 644 file` (rw-r--r--).
- **Chown**: `chown user:group file`.
- **Umask**: Default permissions. `0022` results in 755 (dirs) and 644 (files).

### Documentation
- **Man**: `man command`. `man -k keyword` (search).
- **Info**: `info command`.
- **Doc Paths**: `/usr/share/doc/`.

---

## 2. Manage Software

### RPM / YUM / DNF
- **Repositories**: Configured in `/etc/yum.repos.d/`.
- **Manage Repos**: `dnf config-manager --add-repo=URL`.
- **Install/Remove**: `dnf install package`, `dnf remove package`.
- **Update**: `dnf update`.
- **Query**: `rpm -qa` (list all), `rpm -qi package` (info), `rpm -ql package` (list files).
- **Modules**: `dnf module list`, `dnf module install name:stream`.

### Flatpak
- **Remotes**: `flatpak remote-add --if-not-exists flathub URL`.
- **Install**: `flatpak install flathub org.app.Name`.
- **Run**: `flatpak run org.app.Name`.

---

## 3. Create Simple Shell Scripts

### Shebang & Execution
- Start file with `#!/bin/bash`.
- Make executable: `chmod +x script.sh`.

### Variables & Inputs
- **Assign**: `VAR="value"` (No spaces).
- **Access**: `echo $VAR`.
- **Arguments**: `$1` (First arg), `$2` (Second), `$@` (All args), `$#` (Count).

### Conditionals (If/Else)
```bash
if [[ $1 == "test" ]]; then
  echo "Matches"
elif [ -f "/etc/passwd" ]; then
  echo "File exists"
else
  echo "No match"
fi
```

### Loops
- **For Loop**:
  ```bash
  for user in $(cat users.txt); do
    echo "Creating $user"
  done
  ```
- **While Loop**: `while [[ condition ]]; do ... done`.

### Processing Output
- **Command Substitution**: `DATE=$(date +%F)` captures output of `date`.

---

## 4. Operate Running Systems

### Boot & Reboot
- **Power**: `systemctl reboot`, `systemctl poweroff`.
- **Targets**:
  - `graphical.target` (GUI).
  - `multi-user.target` (CLI).
  - Get/Set: `systemctl get-default`, `systemctl set-default multi-user.target`.
- **Boot Process Interrupt**:
  - Press `e` at GRUB.
  - Append `rd.break` to line starting with `linux`.
  - `ctrl+x` to boot.
  - `mount -o remount,rw /sysroot` -> `chroot /sysroot`.
  - Reset root password -> `touch /.autorelabel` -> `exit` -> `exit`.

### Processes
- **Monitor**: `top` (live), `ps aux` (snapshot).
- **Kill**: `kill -9 PID` (Force), `kill -15 PID` (Terminate). `pkill name`.
- **Scheduling**:
  - **Nice**: Start with priority. `nice -n -5 command` (Higher priority).
  - **Renice**: Change running. `renice -n 10 PID` (Lower priority).
  - Range: -20 (High) to 19 (Low).

### Tuning
- **Service**: `tuned`.
- **Commands**: `tuned-adm list`, `tuned-adm active`, `tuned-adm profile virtual-guest`.

### Logs
- **Journal**: `journalctl`.
  - `-xe` (Errors/End), `-u service` (Specific Unit), `-f` (Follow).
- **Files**: `/var/log/messages`, `/var/log/secure`.
- **Preserve Journals**: Ensure `/var/log/journal` exists. `mkdir -p /var/log/journal && chown root:systemd-journal /var/log/journal && chmod 2755 /var/log/journal`.

---

## 5. Configure Local Storage

### Partitions (MBR & GPT)
- **Tools**: `fdisk` (MBR/GPT), `gdisk` (GPT), `parted`.
- **Type Codes**: Linux LVM (`8e00` in gdisk, `8e` in fdisk).

### LVM (Logical Volume Manager)
**Hierarchy**: Physical Volume (PV) -> Volume Group (VG) -> Logical Volume (LV).
1. **PV**: `pvcreate /dev/vda1`
2. **VG**: `vgcreate myvg /dev/vda1`
3. **LV**: `lvcreate -n mylv -L 500M myvg`
- **Resize**: `lvextend -L +200M /dev/myvg/mylv`.

### Swap
- **Create**: `mkswap /dev/partition`
- **Activate**: `swapon /dev/partition`
- **Persist**: Add to `/etc/fstab`.

---

## 6. Create and Configure File Systems

### Formatting & Mounting
- **Format**: `mkfs.xfs /dev/myvg/mylv`, `mkfs.ext4 /dev/partition`.
- **Mount**: `mount /dev/device /mnt/point`.
- **Persist (/etc/fstab)**:
  - `UUID=...  /data  xfs  defaults  0 0`
  - Get UUIDs with `lsblk -f`.

### NFS (Network File System)
- **Mount**: `mount -t nfs server:/share /mnt`.
- **Fstab**: `server:/share  /mnt  nfs  defaults  0 0`.

### AutoFS (Automounter)
- **Install**: `dnf install autofs`.
- **Config**:
  1. `/etc/auto.master`: `/data  /etc/auto.data`
  2. `/etc/auto.data`: `share  -rw  server:/share`
  3. `systemctl enable --now autofs`.

### SGID (Collaboration)
- **Effect**: Files created in directory inherit the *directory's group*, not the user's primary group.
- **Set**: `chmod g+s /shared/dir`.
- **Verify**: `drwxr-s---

---

## 7. Deploy, Configure, and Maintain Systems

### Scheduling (Cron & At)
- **Cron**: Recurring tasks.
  - `crontab -e -u user`.
  - Format: `Min Hour Day Month DayOfWeek Command`.
- **At**: One-time task.
  - `at 14:00` -> enter commands -> `ctrl+d`.

### Services (Systemd)
- **Start/Stop**: `systemctl start service`, `systemctl stop service`.
- **Enable/Disable**: `systemctl enable service` (Boot), `systemctl disable service`.
- **Status**: `systemctl status service`.

### Time (Chrony)
- **Status**: `chronyc sources`, `timedatectl`.
- **Config**: `/etc/chrony.conf`.
- **Set Timezone**: `timedatectl set-timezone America/New_York`.

---

## 8. Manage Basic Networking

### NetworkManager (nmcli)
- **Show**: `nmcli con show`.
- **Add Connection**:
  ```bash
  nmcli con add type ethernet con-name "MyConn" ifname eth0 \
  ipv4.addresses 192.168.1.10/24 ipv4.gateway 192.168.1.1 ipv4.dns 8.8.8.8 \
  ipv4.method manual
  ```
- **Modify**: `nmcli con mod "MyConn" ipv4.addresses 10.0.0.5/24`.
- **Apply**: `nmcli con up "MyConn"`.

### Hostname
- `hostnamectl set-hostname server1.example.com`.

---

## 9. Manage Users and Groups

### Users
- **Create**: `useradd -m -s /bin/bash user`.
- **Modify**: `usermod -aG group user` (Append to group).
- **Password**: `passwd user`.
- **Delete**: `userdel -r user` (Remove home).

### Groups
- **Create**: `groupadd group`.
- **Modify**: `groupmod`.

### Password Aging
- **Command**: `chage`.
- **List**: `chage -l user`.
- **Expire**: `chage -d 0 user` (Force change on next login).
- **Set Max Days**: `chage -M 90 user`.

---

## 10. Manage Security

### Firewall (firewalld)
- **Zones**: `public` (default), `home`, `work`.
- **Add Service**: `firewall-cmd --permanent --add-service=http`.
- **Add Port**: `firewall-cmd --permanent --add-port=8080/tcp`.
- **Reload**: `firewall-cmd --reload` (Required after --permanent).

### SELinux
- **Modes**: Enforcing, Permissive, Disabled.
  - View: `getenforce`.
  - Set: `setenforce 0` (Permissive), `setenforce 1` (Enforcing).
  - Config: `/etc/selinux/config` (Persistent).
- **Contexts**: `user:role:type:level`.
  - File Type is most important (e.g., `httpd_sys_content_t`).
  - View: `ls -Z`.
- **Management (semanage)**:
  - **Set Context**: `semanage fcontext -a -t httpd_sys_content_t "/web(/.*)?"`.
  - **Apply**: `restorecon -Rv /web`.
- **Booleans**:
  - Switches for functionality.
  - List: `getsebool -a | grep http`.
  - Set: `setsebool -P httpd_can_network_connect 1`.