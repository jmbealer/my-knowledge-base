# The Power of Checklists

> Likely reference: _The Checklist Manifesto_ by Atul Gawande.

## Core Philosophy

Checklists are not just about "ticking boxes"; they are cognitive safety nets.
In a complex world, the volume of knowledge and the complexity of tasks exceed
the ability of any individual to get it right every time, solely from memory.

Checklists protect against two types of errors:

1. **Ignorance**: We don't know enough.
2. **Ineptitude**: We know what to do, but we fail to apply it correctly (due to
   forgetfulness, distraction, or rushing).

## General Application

### When to Use

- **High Stakes**: Situations where a simple error leads to catastrophe (e.g.,
  surgery, airplane takeoff, `rm -rf` commands).
- **High Complexity**: Processes with many dependencies where missing one step
  breaks the chain.
- **Repetitive Tasks**: Mundane tasks where the brain goes on autopilot and
  might skip a step.
- **Coordination**: When multiple people need to verify they are on the same
  page (e.g., "Have we all agreed on the rollback plan?").

### When NOT to Use

- **Creative Exploration**: Brainstorming or initial design phases where
  rigidity stifles innovation.
- **Over-reliance on "Scripts"**: When the situation is novel and requires
  first-principles thinking. A checklist cannot replace professional judgment;
  it aids it.
- **Micromanagement**: Don't checklist every single obvious keystroke ("Type
  'ls', then press Enter"). Focus on the "killer" steps—the ones that, if
  missed, cause failure.

### Types of Checklists

1. **Read-Do**: Read a step, perform it, check it off. Best for new procedures
   or critical, rarely performed tasks.
2. **Do-Confirm**: Perform the task from memory/experience, then stop and run
   through the checklist to verify everything was done. Best for experienced
   professionals doing routine work.

---

## Application in Tech & System Administration

In IT, checklists are the difference between a "routine maintenance window" and
a "3 AM outage."

### 1. Pre-Flight / Pre-Change Checks

Before hitting "Enter" on a major change.

- [ ] Am I on the correct server? (Verify hostname/IP)
- [ ] Am I in the correct directory? (`pwd`)
- [ ] Do I have a fresh, verified backup?
- [ ] Do I have a rollback command ready in my clipboard or notes?
- [ ] Is there an active incident or freeze period I should be aware of?

### 2. Deployments (CI/CD is automated checklists)

Even with automation, manual verify steps often remain.

- [ ] Database migrations applied successfully?
- [ ] Environment variables updated?
- [ ] Smoke test critical paths (login, checkout, search).
- [ ] Monitoring alerts are not firing (or are firing as expected).

### 3. Incident Response (The "Panic" Checklist)

When things are on fire, IQ drops. Rely on a list.

- [ ] **Containment**: Stop the bleeding (block traffic, isolate server).
- [ ] **Communication**: Notify stakeholders/status page.
- [ ] **Assessment**: What changed recently?
- [ ] **Resolution**: Apply fix.
- [ ] **Review**: Post-mortem scheduled.

### 4. Routine Maintenance (The "Boring" Stuff)

- [ ] SSL certificates renewal status.
- [ ] Disk space usage trends.
- [ ] User access review (remove former employees).
- [ ] Backup restore test (a backup is only real if you've restored it).

---

## Personal Machine Administration

Managing your own workstation is often where "bad habits" start. Use checklists to maintain a clean, stable environment.

### 1. The "Weekly Tune-up"
- [ ] **System Updates**: Run OS and package manager updates (`apt update`, `brew upgrade`, etc.).
- [ ] **Firmware**: Check for UEFI/BIOS or peripheral firmware updates.
- [ ] **Backup Sync**: Ensure local files are synced to external/cloud storage.
- [ ] **Disk Cleanup**: Clear temp files, empty trash, and check large files taking up space.

### 2. The "New Machine" Checklist
When setting up a new OS or laptop, a checklist ensures consistency.
- [ ] **Security**: Enable disk encryption (FileVault/LUKS), set up firewall, and disable root SSH login.
- [ ] **SSH/GPG**: Generate/import keys and add to GitHub/GitLab.
- [ ] **Dotfiles**: Clone your `.bashrc`, `.vimrc`, or `zsh` configs.
- [ ] **Tooling**: Install the "must-haves" (VS Code, Docker, Obsidian, CLI tools).
- [ ] **Privacy**: Opt-out of OS telemetry and adjust browser privacy settings.

### 3. Before a Major OS Upgrade
- [ ] **Full Image Backup**: Create a clone or snapshot of the current drive.
- [ ] **Export Configs**: Export browser bookmarks, application settings, and VPN profiles.
- [ ] **Compatibility Check**: Verify that critical software (drivers, kernels, specialized apps) supports the new version.
- [ ] **Cleanup**: Uninstall apps you haven't used in 6 months to reduce migration friction.
