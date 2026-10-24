# Multi-Language Best Practices & Customization Guide

This reference guide is designed for students and developers learning to write secure, clean, and efficient code in **any programming language** of their choice.

---

## 1. Tailoring This Skill to Your Programming Language

This skill adapts to the language you are actively using. When working with your AI agent, you can tell it:

> *"I am working in Python (or JavaScript, TypeScript, Go, Java). Tailor your tips and audits to this language."*

The AI agent will adjust its explanations, syntax suggestions, and audit rules to match your language.

---

## 2. Universal Security & Quality Principles (All Languages)

No matter what programming language you write in, these golden rules keep your code safe:

### Never Hardcode Secrets or Credentials
- **The Risk**: Hardcoding API keys, passwords, or tokens in source files risks leaking them publicly when you push to GitHub.
- **The Solution**: Store credentials in a local `.env` file and add `.env` to your `.gitignore`. Load them at runtime via environment variables (e.g., `process.env.KEY` in JS, `os.environ.get("KEY")` in Python).

### Avoid Dynamic Code Execution (`eval`)
- **The Risk**: Functions like `eval()` execute arbitrary strings as code. If user input enters `eval()`, malicious actors can hijack your application.
- **The Solution**: Always parse structured data using safe formats like JSON (`JSON.parse` or Python's `json.loads`), or safe abstract syntax trees (`ast.literal_eval`).

### Prevent Command Injection
- **The Risk**: Concatenating user strings directly into system shell commands (`exec("ping " + ip)`) allows attackers to execute unauthorized commands.
- **The Solution**: Use parameterized arguments and process spawners that do not invoke an intermediate shell.

---

## 3. Language-Specific Quick Reference

### JavaScript / Node.js
- **Event Loop & Async**: Node.js is single-threaded. Avoid synchronous blocking operations (e.g., use `fs.promises.readFile` instead of `fs.readFileSync`).
- **Variables**: Always use `const` (default) or `let`. Avoid `var` to prevent scope leakage.
- **Equality**: Always use strict equality (`===`) instead of loose equality (`==`).
- **Error Handling**: Wrap asynchronous `await` calls in `try...catch` blocks to prevent unhandled rejections.

### Python
- **Clean Exceptions**: Never write bare `except:`. Always catch specific exceptions (e.g., `except ValueError:` or `except Exception:`).
- **Default Arguments**: Never use mutable default arguments (`def add(item, lst=[])`). Use `lst=None` and initialize inside the function.
- **Virtual Environments**: Always use `venv` or `poetry` to isolate project dependencies.
- **Code Style**: Follow PEP 8 guidelines for naming and readability.

---

## 4. Safe Git and Commit Workflow

Maintaining safe version control habits is essential regardless of language.

### Step 1: Check Changes Before Staging
```bash
git status
git diff
```

### Step 2: Stage Specific Files
Stage only files you deliberately worked on:
```bash
git add file1.ext file2.ext
```

### Step 3: Write Conventional Commit Messages
Use standardized prefixes:
- `feat:` A new feature or functionality (e.g., `feat: add user registration endpoint`)
- `fix:` A bug fix (e.g., `fix: resolve null pointer in payment handler`)
- `docs:` Documentation updates (e.g., `docs: add setup instructions to README`)
- `refactor:` Code improvements that do not alter behavior (e.g., `refactor: extract helper function`)
- `test:` Adding or updating tests (e.g., `test: add unit tests for login`)

### Step 4: The Push Confirmation Rule
- **NEVER** push code to a remote repository automatically.
- **ALWAYS** stop and ask the developer for confirmation before executing `git push`:
  > *"I have created commit `<message>`. Would you like me to push these changes to GitHub now?"*
