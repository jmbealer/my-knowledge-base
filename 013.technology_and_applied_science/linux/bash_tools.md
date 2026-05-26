# Bash Linters & Style Guides

## Top Tools

1.  **ShellCheck** (The Essential Linter)
    *   **What it is:** The industry standard. Finds syntax errors, security holes, and subtle bugs (like missing quotes).
    *   **Usage:** `shellcheck myscript.sh` or VS Code extension.
    *   **Goal:** Catching "gotchas" before they break your system.

2.  **shfmt** (The Formatter)
    *   **What it is:** Auto-formats your code (indentation, spacing).
    *   **Usage:** `shfmt -w myscript.sh`.
    *   **Goal:** Making your scripts look professional and readable.

## Essential Style Guide (The "Safe" Way)

### 1. The Header (Defensive Bash)
Always start with these lines to prevent scripts from running when things fail.
```bash
#!/bin/bash
set -euo pipefail
# -e: Exit on error
# -u: Exit on unset variables
# -o pipefail: Catch errors in pipes (ls | grep)
```

### 2. Quoting Everything
Always wrap variables in double quotes to prevent spaces from breaking your script.
*   **Bad:** `rm $filename` (If filename is "My File", it tries to delete "My" and "File")
*   **Good:** `rm "$filename"`

### 3. Use `[[ ]]` instead of `[ ]`
The double bracket is safer and more powerful in Bash.
*   **Good:** `if [[ $status == "ok" ]]; then`

### 4. Command Substitution
Use `$()` instead of backticks.
*   **Good:** `DATE=$(date)`

## Major Style Guides

1.  **Google Shell Style Guide**
    *   The most famous guide. Very strict (e.g., indent by 2 spaces, use `local` variables in functions).
    *   [Link](https://google.github.io/styleguide/shellguide.html)

2.  **Common Sense / Community Standards**
    *   Avoid scripts longer than 100 lines (use Python if it gets complex).
    *   Use `local` for all variables inside functions.
    *   Use `long-flags` in scripts for readability (e.g., `curl --silent` instead of `curl -s`).

## Recommended Setup for You

1.  **VS Code Extension:** `shell-format` (for `shfmt`) and `ShellCheck`.
2.  **CLI:** Install `shellcheck` (`sudo dnf install shellcheck` on RHEL/Fedora).
