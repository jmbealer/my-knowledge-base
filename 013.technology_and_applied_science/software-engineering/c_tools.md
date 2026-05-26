# C Linters & Style Guides

## Top Tools

1.  **Cppcheck** (The Standard Static Analyzer)
    *   **What it is:** Specifically designed for C/C++. Focuses on detecting undefined behavior (memory leaks, null pointer dereferences, out-of-bounds errors).
    *   **Goal:** Finding bugs that the compiler misses.
    *   **Usage:** `cppcheck main.c`.

2.  **Clang-Tidy** (The Modern Linter)
    *   **What it is:** A "linter" framework based on the Clang compiler. It checks for style violations, performance issues, and modernization (if using C++).
    *   **Goal:** Enforcing specific coding patterns.

3.  **Clang-Format** (The Formatter)
    *   **What it is:** Automatically formats code according to a style guide (indentation, brace placement).
    *   **Goal:** Zero-effort consistency. Use a `.clang-format` file in your project.

4.  **Valgrind** (The Memory Detective)
    *   **What it is:** A dynamic analysis tool. You run your program *inside* Valgrind, and it tells you exactly where you leaked memory or accessed invalid addresses at runtime.
    *   **Usage:** `valgrind --leak-check=full ./my_program`.

## Major Style Guides

1.  **Linux Kernel Coding Style**
    *   **Vibe:** Very strict, "old school" but robust. 8-character tabs, 80-character lines.
    *   **Why:** If you want to do system-level programming or contribute to the kernel.
    *   [Link](https://www.kernel.org/doc/html/latest/process/coding-style.html)

2.  **MISRA C** (The "Safety/Military" Choice)
    *   **Vibe:** Extremely restrictive. Used in aerospace, automotive, and medical fields. Prohibits "dangerous" features like `malloc` or certain types of pointers.
    *   **Why:** If you want to write code that *cannot* fail (high stakes).

3.  **NASA/JPL C Style Guide**
    *   **Vibe:** Focused on mission-critical software. Famous for "The Power of 10" rules (e.g., no recursion, no heap memory after initialization).

4.  **Google C Style Guide**
    *   **Vibe:** Modern, readable, focused on large-scale maintainability.
    *   [Link](https://google.github.io/styleguide/cppguide.html) (C is a subset).

## Recommended Setup for You

1.  **VS Code Extensions:** `C/C++` (Microsoft) and `clang-tidy` integration.
2.  **CLI Tools:** `cppcheck` and `valgrind` (Essential for C development on Linux).
3.  **Workflow:**
    *   Write code.
    *   Format with `clang-format`.
    *   Lint with `cppcheck`.
    *   Compile with `-Wall -Wextra -Werror` (treat warnings as errors).
    *   Run with `valgrind` to check for leaks.
