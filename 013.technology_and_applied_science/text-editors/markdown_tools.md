# Markdown Linters & Style Guides

## Top Linters

1. **markdownlint** (Standard)
   - **What it is:** The de facto standard. Checks for common issues like header
     levels, trailing spaces, and blank lines.
   - **Usage:** Node.js CLI or VS Code Extension.
   - **Config:** `.markdownlint.json` allows you to enable/disable rules.

2. **Prettier** (Formatter)
   - **What it is:** An opinionated code formatter. It doesn't just "lint"
     (warn); it _rewrites_ your Markdown to be perfectly consistent (wrapping
     text, fixing indentation).
   - **Pro:** Zero-config consistency.
   - **Con:** Can be aggressive with line wrapping.

3. **Vale** (Prose/Grammar)
   - **What it is:** Lints the _English language_, not just the Markdown syntax.
     Checks for passive voice, insensitive language, or brand guidelines (e.g.,
     "Use 'Red Hat', not 'redhat'").
   - **Usage:** Great for technical documentation.

## Common Style Guides

1. **Google Developer Documentation Style Guide**
   - Focus: Clarity, tone, and formatting for technical docs.
   - [Link](https://developers.google.com/style)

2. **Microsoft Writing Style Guide**
   - Focus: Accessibility, bias-free communication, and consistent terminology.
   - [Link](https://learn.microsoft.com/en-us/style-guide/welcome/)

3. **GitHub Flavored Markdown (GFM)**
   - The technical spec used by GitHub (and most devs). Defines how tables, task
     lists, and code blocks should look.

## Recommended Setup for You

For a personal knowledge base, use this combo:

1. **VS Code Extension:** `markdownlint` (David Anson) to catch syntax errors as
   you type.
2. **Formatter:** `Prettier` to auto-format tables and indentation on save.
