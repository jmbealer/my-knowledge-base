# RHCE Study Guide (EX294)

- Site: [Red Hat Certified Engineer (RHCE) - EX294](https://www.redhat.com/en/services/training/ex294-red-hat-certified-engineer-rhce-exam-red-hat-enterprise-linux-9)

> **Note:** The current EX294 exam is based on RHEL 9 and Ansible Core. It requires using `ansible-navigator` and execution environments, moving away from the legacy `ansible-playbook` command in some contexts, though both are important.

## 1. Install and Configure Ansible

### Installation
- **Packages**: `dnf install ansible-core ansible-navigator rhel-system-roles`
- **Verification**: `ansible --version`, `ansible-navigator --version`

### Configuration (`ansible.cfg`)
- **Location Priority**: `ANSIBLE_CONFIG` env > `./ansible.cfg` > `~/.ansible.cfg` > `/etc/ansible/ansible.cfg`
- **Basic Setup**:
  ```ini
  [defaults]
  inventory = ./inventory
  remote_user = devops
  ask_pass = false
  
  [privilege_escalation]
  become = true
  become_method = sudo
  become_user = root
  become_ask_pass = false
  ```

### Ansible Navigator (`ansible-navigator.yml`)
- Used to run playbooks inside containerized execution environments (EE).
- **Basic Config**:
  ```yaml
  ansible-navigator:
    execution-environment:
      image: registry.redhat.io/ansible-automation-platform-22/ee-supported-rhel8:latest
      pull: missing
    playbook-artifact:
      enable: false
  ```

### Inventories
- **Static Inventory** (`inventory` file):
  ```ini
  [webservers]
  servera.lab.example.com
  serverb.lab.example.com
  
  [dbservers]
  db1.lab.example.com
  
  [prod:children]
  webservers
  dbservers
  ```
- **Verification**: `ansible-navigator inventory --list -m stdout`

---

## 2. Configure Managed Nodes

### SSH Key Setup
1.  **Generate Key**: `ssh-keygen -t rsa -b 4096`
2.  **Distribute**: `ssh-copy-id user@managed-node`
3.  **Verify**: `ssh user@managed-node` (should not ask for password)

### Privilege Escalation (Sudoers)
- On managed nodes, ensure the user has sudo rights without password:
  - File: `/etc/sudoers.d/devops`
  - Content: `devops ALL=(ALL) NOPASSWD: ALL`

---

## 3. Run Playbooks & Ad-Hoc Commands

### Ad-Hoc Commands
- **Syntax**: `ansible host-pattern -m module -a "arguments"`
- **Examples**:
  - Ping: `ansible all -m ping`
  - Command: `ansible webservers -m command -a "uptime"`
  - Shell (allows pipes): `ansible webservers -m shell -a "echo hi > /tmp/hi"`

### Ansible Navigator
- **Run Playbook**: `ansible-navigator run playbook.yml`
- **Interactive Mode**: Just type `ansible-navigator` to browse inventory, collections, and docs.
- **Doc Lookup**: `ansible-navigator doc module_name` (e.g., `ansible-navigator doc user`).

---

## 4. Create Ansible Plays and Playbooks

### Structure
```yaml
---
- name: Configure Web Servers
  hosts: webservers
  become: true
  tasks:
    - name: Install Apache
      ansible.builtin.dnf:
        name: httpd
        state: present
```

### Variables
- **Definition**:
  - In playbook: `vars: { key: value }`
  - In inventory: `[webservers:vars]`
  - In separate files: `group_vars/webservers.yml`, `host_vars/servera.yml`
- **Usage**: `{{ variable_name }}`
- **Register (Capture Output)**:
  ```yaml
  - name: Check file
    command: cat /etc/redhat-release
    register: release_out
  
  - name: Print output
    debug:
      msg: "System is {{ release_out.stdout }}"
  ```

### Conditionals (`when`)
```yaml
- name: Install MariaDB only on RedHat
  dnf:
    name: mariadb-server
    state: present
  when: ansible_facts['os_family'] == "RedHat"
```

### Loops (`loop`)
```yaml
- name: Create multiple users
  user:
    name: "{{ item }}"
    state: present
  loop:
    - user1
    - user2
    - user3
```

### Handlers (Triggered Actions)
- Used for restarting services only when a change occurs.
```yaml
tasks:
  - name: Update config
    copy:
      src: httpd.conf
      dest: /etc/httpd/conf/httpd.conf
    notify: Restart Apache

handlers:
  - name: Restart Apache
    service:
      name: httpd
      state: restarted
```

### Error Handling (`block`, `rescue`, `always`)
```yaml
- name: Attempt dangerous task
  block:
    - command: /bin/false
  rescue:
    - debug:
        msg: "It failed, but we recovered."
```

---

## 5. Use Roles and Content Collections

### Roles
- **Structure**: `roles/role_name/{tasks,handlers,templates,vars,defaults,meta}/main.yml`
- **Create**: `ansible-galaxy init roles/myrole`
- **Use in Playbook**:
  ```yaml
  - hosts: all
    roles:
      - myrole
  ```
- **System Roles**: Install `rhel-system-roles`. found in `/usr/share/ansible/roles/`.

### Ansible Galaxy / Collections
- **Install Collection**: `ansible-galaxy collection install community.general`
- **Use**: `ansible.builtin.copy` vs `community.general.xml`.
- **Requirements File** (`requirements.yml`):
  ```yaml
  collections:
    - name: community.general
    - name: redhat.rhel_system_roles
  ```
  Install: `ansible-galaxy install -r requirements.yml`

---

## 6. Automate Standard RHCSA Tasks

### Software Packages
```yaml
- name: Install group of packages
  dnf:
    name: "@Development Tools"
    state: present

- name: Enable Repo
  yum_repository:
    name: myrepo
    description: My Repo
    baseurl: http://repo.example.com
    gpgcheck: no
```

### Services
```yaml
- name: Start and enable Firewall
  service:
    name: firewalld
    state: started
    enabled: yes
```

### Firewall
```yaml
- name: Open HTTP port
  firewalld:
    service: http
    permanent: yes
    state: enabled
    immediate: yes
```

### File Systems & Storage
- **Partitions**: `community.general.parted`
- **LVM**: `community.general.lvg`, `community.general.lvol`
- **Filesystem**: `community.general.filesystem`
- **Mount**: `ansible.posix.mount`

```yaml
- name: Create partition
  parted:
    device: /dev/vdb
    number: 1
    state: present

- name: Create Volume Group
  lvg:
    vg: data_vg
    pvs: /dev/vdb1

- name: Create Logical Volume
  lvol:
    vg: data_vg
    lv: data_lv
    size: 1G

- name: Format XFS
  filesystem:
    fstype: xfs
    dev: /dev/data_vg/data_lv

- name: Mount
  mount:
    path: /data
    src: /dev/data_vg/data_lv
    fstype: xfs
    state: mounted
```

### File Content & Archiving
- **Copy**: `copy` (local to remote).
- **Fetch**: `fetch` (remote to local).
- **Lineinfile**: Ensure a specific line exists.
- **Archive**: `community.general.archive` (tar/zip).
- **Unarchive**: `ansible.builtin.unarchive`.

### Users & Groups
```yaml
- name: Create Group
  group:
    name: developers
    gid: 2000

- name: Create User
  user:
    name: devops
    uid: 2001
    group: developers
    password: "{{ 'password' | password_hash('sha512') }}"
```

### Scheduled Tasks (Cron)
```yaml
- name: Run backup daily
  cron:
    name: "Daily backup"
    minute: "0"
    hour: "2"
    job: "/usr/local/bin/backup.sh"
```

### Security (SELinux)
- Requires `python3-libselinux` on managed nodes.
```yaml
- name: Set Enforcing
  selinux:
    policy: targeted
    state: enforcing

- name: Set file context
  sefcontext:
    target: '/web(/.*)?'
    setype: httpd_sys_content_t
    state: present
  notify: Restorecon Web

handlers:
  - name: Restorecon Web
    command: restorecon -Rv /web
```

---

## 7. Manage Content (Templates & Vault)

### Templates (Jinja2)
- **Module**: `template`
- **Source** (`file.j2`):
  ```ini
  PORT={{ http_port }}
  ADMIN={{ admin_email }}
  {% for host in groups['webservers'] %}
  SERVER={{ host }}
  {% endfor %}
  ```
- **Task**:
  ```yaml
  - name: Deploy config
    template:
      src: config.conf.j2
      dest: /etc/app/config.conf
  ```

### Ansible Vault
- **Encrypt**: `ansible-vault encrypt secret.yml`
- **Edit**: `ansible-vault edit secret.yml`
- **View**: `ansible-vault view secret.yml`
- **Use in Playbook**:
  - `ansible-navigator run playbook.yml --vault-id @prompt` (ask for pass)
  - `ansible-navigator run playbook.yml --vault-password-file pass.txt`