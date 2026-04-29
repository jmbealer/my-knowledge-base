# Documentation Strategies for Knowledge Retention

> "The only difference between screwing around and science is writing it down."
> — Adam Savage (Mythbusters)

## The Core Problem: The Amnesiac SysAdmin

We have all been there: You spend 4 hours debugging an obscure Linux error. You
finally fix it. Six months later, it breaks again. You remember _fixing_ it, but
you have zero memory of _how_.

Documentation is not just for teams; it is a time machine for your future self.

## Approaches by Field

Different disciplines document for different reasons. We can steal from all of
them to build a personal "Knowledge Engine."

### 1. System Administration (The Runbook & Incident Log)

**Goal:** Reproducibility & Recovery.

- **The Runbook:** Step-by-step instructions for routine tasks (like the
  Checklist).
- **The Incident Log:** When things break, SysAdmins write "Post-Mortems."
  - _What_ was the symptom?
  - _What_ was the root cause?
  - _How_ was it fixed?
  - _How_ do we prevent it next time?
- **Application:** For every "weird" error you solve, create a note titled
  `Error: <Error Message>`. Paste the command and the fix.

### 2. Software Engineering (Context & Decisions)

**Goal:** Understanding _Why_.

- **Code Comments:** Explain the _why_, not the _what_ (the code shows _what_).
- **ADRs (Architecture Decision Records):** "We chose Postgres over Mongo
  because X, Y, Z."
- **Application:** When configuring your system (e.g., choosing `zsh` over
  `bash`), write a quick note explaining _why_. When you question yourself a
  year later, you'll know.

### 3. Engineering (Specs & Trade-offs)

**Goal:** Constraints & Optimization.

- **Specifications:** Defining the operating limits. "Max RAM: 64GB", "Operating
  Temp: <80C".
- **Trade-offs:** Engineering is the art of compromise. You chose Solution A
  over Solution B for a reason.
- **Application:** When building a server or choosing a tool.
  - "Why did I use `rsync` instead of `scp`? Because `rsync` handles resume
    (Spec) and I have a flaky connection (Constraint)."
  - "Why this $500 GPU? It balances cost vs. the specific CUDA performance I
    need for local LLMs."

### 4. Science (The Lab Notebook)

**Goal:** Provenance & Truth.

- **Methodology:** Scientists record _everything_, including failed experiments.
  A failed experiment is data.
- **Chronological:** "10:00 AM: Added reagent X. 10:15 AM: Sample exploded."
- **Application:** When debugging a hard problem, open a "scratchpad" note. Log
  every command you run and its output _as you do it_.
  - "Tried `systemctl restart`, didn't work."
  - "Tried editing config, syntax error."
  - "Found this StackOverflow thread..."
  - _Why?_ Because when you finally fix it, you need to know which of the 50
    things you did actually worked.

### 5. Military (The After Action Review - AAR)

**Goal:** Improvement & Learning.

- **Structure:**
  1. What was supposed to happen?
  2. What actually happened?
  3. Why was there a difference?
  4. What will we do differently next time?
- **Application:** After a major upgrade or project, spend 5 minutes reviewing.
  "I spent 3 hours on this because I didn't read the docs first. Next time, read
  docs."

### 6. Medical / Aviation (The Audit Trail)

**Goal:** Safety & Continuity.

- **Handover:** "Patient was given 5mg of X at 14:00."
- **Application:** Treat your computer like a patient. "Updated Nvidia drivers
  to v550 on Jan 31." If the screen goes black tomorrow, you know exactly what
  changed.

---

## The "Fix-It" Workflow for Linux

Combine these into a simple workflow for your personal machine.

### Phase 1: The "Scratchpad" (While Debugging)

Don't worry about formatting. Just dump info.

- Copy/paste error messages (crucial for searching later).
- Paste URLs of pages you are reading.
- Paste commands you run.

### Phase 2: The "Solution Note" (After Fixing)

Once fixed, create a clean, searchable note.

**Template:**

```markdown
# Issue: [Error Message / Symptom]

**Date:** 2026-01-31 **System:** Arch Linux / Ubuntu 24.04 **Tags:** #linux
#networking #fix

## Symptom

Describe what happened. "Wifi drops every time I connect Bluetooth headphones."

## Root Cause

"Conflict between `iwlwifi` driver and Bluetooth coexistence settings."

## The Solution

Edit `/etc/modprobe.d/iwlwifi.conf` and add: `options iwlwifi bt_coex_active=0`

## References

- [Link to Arch Wiki section]
- [Link to Reddit thread]
```

### Phase 3: Automation (The "Lazy" Logger)

If you forget to write notes, force your computer to help.

- **Shell History:** Configure your shell (`.zshrc` / `.bashrc`) to save history
  _forever_ and include timestamps.
- **`script` command:** Run `script session.log` before doing risky work. It
  records _everything_ printed to the terminal to a file.
