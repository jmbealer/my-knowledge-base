# Robust Problem Solving Models

> "We cannot solve our problems with the same thinking we used when we created
> them." — Albert Einstein

To be a robust problem solver, you cannot rely on just one tool. You need a
mental toolkit drawn from multiple disciplines.

## 1. Universal / General Models

### The "First Principles" Thinking

**Origin:** Physics / Philosophy **Concept:** Boil things down to the most
fundamental truths and reason up from there. Do not reason by analogy ("It's
like X"). **Application:**

- _Analogy:_ "I can't build this feature because no other plugin does it."
- _First Principles:_ "What is required? A database write and a UI trigger. Can
  I do those two things? Yes. Then it is possible."

### The "5 Whys"

**Origin:** Toyota Production System **Concept:** Ask "Why?" five times to find
the root cause, not just the symptom. **Application:**

1. **Server crashed.** (Why?) -> Out of memory.
2. **Why?** -> The app leaked memory.
3. **Why?** -> A loop didn't close connections.
4. **Why?** -> The developer didn't use a connection pool.
5. **Why?** -> We have no code review standards for DB connections. (FIX THIS).

---

## 2. Mathematics (Rigorous Logic)

### Polya’s 4 Steps

**Source:** _How to Solve It_ by George Polya **Concept:** The gold standard for
structured solving.

1. **Understand the Problem:** What is the unknown? What are the data? What are
   the conditions? Draw a figure.
2. **Devise a Plan:** Have you seen it before? Can you solve a simpler part of
   it? (Reduction).
3. **Carry out the Plan:** Check each step. Can you prove it is correct?
4. **Look Back:** Can you derive the result differently? Can you use the method
   for other problems?

### Inversion (Jacobi)

**Concept:** "Invert, always invert." Instead of asking how to solve X, ask how
to _cause_ not-X (or failure). **Application:**

- _Standard:_ "How do I make this server secure?"
- _Inversion:_ "How would I break into this server?" (Open ports, weak
  passwords, old kernel). Fix those.

---

## 3. Computer Science & System Administration

### Binary Search (Half-Splitting)

**Concept:** Divide the search space by half at every step. **Application:**

- **Debugging Logs:** The error occurred between 10:00 and 11:00. Check 10:30.
  If the error is there, check 10:15. If not, check 10:45.
- **Network Cable:** Internet is down. Ping the router (halfway). If yes, the
  issue is WAN. If no, the issue is LAN/PC.

### The OSI Model Approach (Layered Troubleshooting)

**Concept:** Networking has 7 layers. Troubleshoot them in order (usually
Bottom-Up or Top-Down).

1. **Physical:** Is the cable plugged in?
2. **Data Link:** Is the link light on?
3. **Network:** Can I ping the gateway (IP)?
4. **Transport:** Is the port open (TCP/UDP)?
5. **Application:** Is the web server returning a 500 error? **Rule:** Never
   debug Layer 7 (App) if Layer 1 (Cable) is broken.

### Rubber Ducking

**Concept:** Explain the code/problem line-by-line to an inanimate object (a
rubber duck). **Why it works:** forcing your brain to slow down and articulate
the logic often reveals the obvious flaw you skipped over.

---

## 4. Engineering

### Constraints & Trade-offs

**Concept:** There are no perfect solutions, only trade-offs. **Trilemma:**
Fast, Good, Cheap (Pick two). **Application:** When "solving" a storage problem,
explicitly state: "I am optimizing for _read speed_ at the cost of _storage
space_."

### Failure Mode and Effects Analysis (FMEA)

**Concept:** Proactively list everything that _could_ fail and its impact.

- **Component:** Hard Drive.
- **Failure Mode:** Disk full.
- **Effect:** Database crashes.
- **Mitigation:** Monitoring alert at 80%.

---

## 5. The Scientific Method

### Hypothesis Testing

**Concept:** Don't just "try things." Form a hypothesis.

1. **Observation:** Web server is slow.
2. **Hypothesis:** It is the database.
3. **Experiment:** Stop the web server and run a raw DB query.
   - _Result A (Slow):_ Hypothesis confirmed. It's the DB.
   - _Result B (Fast):_ Hypothesis rejected. It's the App code, not the DB.

---

## 6. Medical / Emergency (Triage)

### Differential Diagnosis

**Concept:** List all possible causes, ordered by probability and danger. Rule
them out one by one. **Application:** "Computer won't boot."

1. _Power Supply (High prob, easy check):_ Check cable.
2. _RAM (Med prob, easy check):_ Reseat RAM.
3. _Motherboard (Low prob, hard check):_ Test last.

### Triage (START)

**Concept:** In a crisis, categorize problems to maximize survival.

1. **Critical (Red):** Fix immediately or system dies (e.g., Security Breach,
   Data Loss).
2. **Urgent (Yellow):** Needs attention but stable (e.g., High Latency).
3. **Minor (Green):** Can wait (e.g., Typo on homepage). **Rule:** Don't fix a
   typo while the database is on fire.

---

## 7. Military

### OODA Loop

**Source:** Col. John Boyd **Concept:** Observe, Orient, Decide, Act. Speed is
key.

1. **Observe:** Gather raw data (logs, graphs).
2. **Orient:** Update your mental model (Is this an attack? A bug? A user
   surge?).
3. **Decide:** Choose a course of action.
4. **Act:** Execute.

- _Loop:_ Immediately Observe the result of your Action.

### Red Teaming

**Concept:** Have someone (or yourself) explicitly play the "enemy" or "chaos."
**Application:** Before launching a script, ask: "If I wanted to destroy the
system with this script, how would I do it?" (e.g., `rm -rf $VAR/` where `$VAR`
is empty).
