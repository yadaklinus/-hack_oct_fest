# JavaScript & Node.js Best Practices Guide for Students

This reference guide provides foundational principles, security rules, and code patterns to help students build reliable, efficient, and secure Node.js applications.

---

## 1. How JavaScript & Node.js Work (The Core Mechanism)

Node.js executes JavaScript on a single main thread powered by the V8 engine and the **libuv Event Loop**.

### The Event Loop & Concurrency
- **Single-Threaded Execution**: Your JavaScript code runs on one thread. If you execute a heavy computation or a blocking synchronous call, the entire server freezes.
- **Non-Blocking I/O**: Network requests, file reading, and database queries are delegated to the operating system or worker threads. Once ready, their callbacks return to the event loop.
- **Rule of Thumb**: Never block the event loop. Always use asynchronous methods (`async/await`) for operations involving files, databases, or external APIs.

---

## 2. Code Quality & Modern JavaScript Standards

### Use `const` and `let` Instead of `var`
- `const`: Use by default for any variable whose reference does not change.
- `let`: Use when variable reassignment is required (such as counter variables).
- *Avoid `var`*: `var` is function-scoped and hoisted, which creates accidental leaks and unexpected bugs.

### Strict Equality (`===`)
- Always use strict equality (`===` and `!==`) to verify both data type and value.
- Avoid loose equality (`==`), which attempts hidden type coercion (e.g., `"" == 0` evaluates to `true`).

### Asynchronous Error Handling
Always guard asynchronous operations using `try...catch` blocks to prevent unhandled promise rejections that crash Node.js applications:

```javascript
// Good practice
async function loadUserData(userId) {
  try {
    const user = await database.findUser(userId);
    if (!user) {
      throw new Error(`User ${userId} not found`);
    }
    return user;
  } catch (error) {
    console.error("Failed to load user:", error.message);
    throw error;
  }
}
```

---

## 3. Essential Security Rules for Students

### Never Use `eval()`
- `eval()` converts incoming strings into executable code. If an attacker injects code into user input, they gain full control over your server.
- **Alternative**: For JSON data, use `JSON.parse()`. For mathematical formulas, use specialized parsing packages.

### Protect Secrets and API Keys
- Never write API keys, passwords, or connection strings directly inside source code.
- Store sensitive values in a `.env` file and add `.env` to your `.gitignore`.
- Access values via `process.env.VARIABLE_NAME` using the `dotenv` package:

```javascript
// In your code:
require('dotenv').config();
const apiKey = process.env.PAYMENT_API_KEY;
```

### Prevent Command Injection
Avoid passing dynamic strings into `child_process.exec()`:

```javascript
// Dangerous: vulnerable to command injection
const { exec } = require('child_process');
exec(`ping -c 1 ${userInput}`);

// Secure: use spawn or execFile with arguments array
const { spawn } = require('child_process');
spawn('ping', ['-c', '1', userInput]);
```

---

## 4. Performance Tips: Asynchronous File & Network Operations

### Avoid Synchronous File System Methods
- Do not use `fs.readFileSync` or `fs.writeFileSync` in request handlers or production server code.
- Use `fs.promises` instead:

```javascript
// Avoid in servers:
// const data = fs.readFileSync('data.json', 'utf8');

// Preferred:
const fs = require('fs/promises');
const data = await fs.readFile('data.json', 'utf8');
```

### Run Independent Tasks Concurrently
When fetching multiple items that do not depend on one another, use `Promise.all`:

```javascript
// Slower: runs sequentially
const user = await getUser();
const posts = await getPosts();

// Faster: runs concurrently
const [user, posts] = await Promise.all([getUser(), getPosts()]);
```

---

## 5. Safe Git and Commit Workflow for Students

When collaborating on code or working with an AI assistant, maintain a clean and safe Git workflow.

### 1. Inspect Status and Diffs First
Always verify what changed before staging:
```bash
git status
git diff
```

### 2. Stage Changes Deliberately
Stage specific files instead of blindly adding everything:
```bash
git add app.js package.json
```

### 3. Write Conventional Commit Messages
Structure commit messages clearly using conventional prefixes:
- `feat:` A new feature or capability (e.g., `feat: add user authentication route`)
- `fix:` A bug fix (e.g., `fix: handle null response in payment webhook`)
- `docs:` Documentation updates (e.g., `docs: clarify installation steps in README`)
- `refactor:` Code improvements that do not change external behavior (e.g., `refactor: convert callbacks to async/await`)
- `test:` Adding or updating tests (e.g., `test: add unit tests for token validator`)

### 4. The Golden Rule of Git Push
- **NEVER** push code to a remote repository automatically.
- **ALWAYS** ask for explicit confirmation from the human developer before executing `git push`.
- Example confirmation prompt:
  > *"I have committed your changes with message: `feat: add secure auth middleware`. Would you like me to push this commit to branch `main` now?"*
