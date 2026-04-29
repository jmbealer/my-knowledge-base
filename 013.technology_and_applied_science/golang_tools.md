# Go Linters & Style Guides

## Top Tools

1.  **gofmt** (The Official Formatter)
    *   **What it is:** The gold standard. Go is famous for having one official way to format code. There are no "tabs vs spaces" debates in Go.
    *   **Usage:** `gofmt -w .`. Most editors run this on save.
    *   **Goal:** Perfect consistency across every Go project in the world.

2.  **golangci-lint** (The Meta-Linter)
    *   **What it is:** A single tool that runs dozens of linters in parallel (including `staticcheck`, `errcheck`, `unused`, etc.).
    *   **Goal:** The only linting tool you need to install. Highly configurable via `.golangci.yml`.
    *   **Usage:** `golangci-lint run`.

3.  **go vet** (The Logic Checker)
    *   **What it is:** Built into the Go toolchain. Checks for suspicious constructs like mismatched `Printf` arguments or unreachable code.
    *   **Usage:** `go vet ./...`.

4.  **staticcheck** (The Advanced Analyzer)
    *   **What it is:** Part of `golangci-lint` but can be used standalone. Extremely high-quality checks for performance and bugs.

## Essential Style & Idioms

### 1. "Effective Go"
The primary document for learning how to write idiomatic Go.
*   **Key Idea:** Clear, simple, and predictable code is better than "clever" code.
*   [Link](https://go.dev/doc/effective_go)

### 2. Error Handling (The "Go Way")
In Go, errors are values, not exceptions.
*   **Pattern:** Always check the error immediately.
```go
f, err := os.Open("filename.ext")
if err != nil {
    return err
}
defer f.Close()
```

### 3. Naming Conventions
*   **MixedCaps:** Use `MixedCaps` or `mixedCaps` rather than underscores (`snake_case`).
*   **Short Names:** Variable names should be short, especially for short-lived variables (e.g., `i` instead of `index`).
*   **Packages:** Short, lowercase, single-word names.

### 4. Visibility (Exporting)
*   **Upper Case:** Starts with a capital letter? It is **Exported** (public).
*   **Lower Case:** Starts with lowercase? It is **Unexported** (private).

## Detailed Style Guide Comparison

While `gofmt` handles whitespace, these guides dictate *how* to use the language.

### 1. Effective Go (The Bible)
*   **Status:** Official.
*   **Focus:** The philosophy of Go. It explains *why* the language works this way.
*   **Best For:** Beginners to Intermediates learning "The Go Way".
*   **Key Rules:**
    *   Errors are values.
    *   Use `defer` for cleanup.
    *   Interfaces should be small (often one method).

### 2. Uber Go Style Guide (The Engineer's Choice)
*   **Status:** Community Favorite.
*   **Focus:** Performance and robustness in large codebases. Very prescriptive ("Do this, don't do that").
*   **Best For:** Teams building high-performance services.
*   **Key Rules:**
    *   **Avoid `init()`:** It causes side effects and hard-to-read code paths.
    *   **Zero Values:** Prefer using `var s sync.Mutex` (zero value is usable) over `s := &sync.Mutex{}`.
    *   **Pointers:** Don't pass pointers to interfaces.

### 3. Google Go Style Guide
*   **Status:** The "Upgraded" Standard.
*   **Focus:** Consistency at massive scale.
*   **Best For:** Large organizations needing strict uniformity.
*   **Key Rules:**
    *   **Panic:** Do not use panic in normal code (only for unrecoverable startup errors).
    *   **Getters:** Name getters `Field()`, not `GetField()`.

## Recommended Setup for You

1.  **VS Code Extension:** `Go` (Google). It comes with `gopls` (Language Server) which handles linting and formatting automatically.
2.  **CLI Tools:** Install `golangci-lint` for your CI/CD or pre-commit checks.
3.  **Workflow:**
    *   Let the editor auto-format with `gofmt` (or `goimports`).
    *   Run `go vet` and `staticcheck` (via `golangci-lint`) to find logic errors.
    *   Follow the **Effective Go** principles for structure.
