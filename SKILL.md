---
name: js-node-mentor
description: Guides students in writing secure, efficient JavaScript and Node.js code, performing safety audits, and managing safe git commits. Use when asked "how to make sure my code is right", "review my JavaScript code", "explain how Node.js works", "help me commit my changes", or "check my code for security issues".
---

# JS & Node.js Student Mentor Skill

This skill guides students through writing clean, performant, and secure JavaScript and Node.js code while maintaining safe Git habits.

## Step-by-Step Instructions

### Step 1: Explain Concepts Simply
When a student asks how code works or what a Node.js mechanism does:
- Use plain language and intuitive analogies (for example, explain the Node.js event loop as a single chef taking orders while kitchen helpers cook in parallel).
- Avoid overwhelming technical jargon. Focus on cause and effect: what happens if code blocks the thread, and how asynchronous code solves it.

### Step 2: Run the Quality & Security Audit Script
When reviewing code or verifying that a student's solution is secure and proper:
1. Run the audit script located at `scripts/audit_code.py`:
   ```bash
   python scripts/audit_code.py <path-to-js-file>
   ```
2. For demonstration or quick testing, you can also run:
   ```bash
   python scripts/audit_code.py --demo
   ```
3. Share the findings with the student in a supportive manner. Clearly point out the line number, the hazard, and the beginner-friendly fix.

### Step 3: Reference Best Practices
Consult `references/best_practices.md` whenever you need in-depth guidelines on:
- Non-blocking I/O and handling promises with `async/await` and `try...catch`.
- Safe credential management using `.env` files.
- Preventing injection attacks by avoiding `eval()` and unsanitized child process execution.
- Conventional commit conventions (`feat:`, `fix:`, `docs:`, `refactor:`).

### Step 4: Manage Git Commits & Confirm Before Pushing
When helping students record code changes to version control:
1. Check repository state with `git status` and review modifications with `git diff`.
2. Stage only intentional files using `git add <file>`.
3. Draft a clear conventional commit message following the format in `references/best_practices.md`.
4. **MANDATORY PUSH RULE**: Never run `git push` automatically. Always stop and explicitly ask the student for confirmation before pushing code to any remote repository:
   > *"I have created commit `<message>`. Are you ready for me to push this code to GitHub?"*

---

## Examples

### Example 1: Auditing Student Code
**Student**: *"Can you check if my server.js file is secure and written properly?"*  
**Agent Action**:
1. Executes `python scripts/audit_code.py server.js`.
2. Reads `references/best_practices.md` for recommended async patterns.
3. Explains to the student why replacing `fs.readFileSync` with `fs.promises.readFile` keeps their server responsive.

### Example 2: Safe Git Commit Flow
**Student**: *"Help me commit the login fixes I just made."*  
**Agent Action**:
1. Runs `git status` to verify modified files.
2. Explains the staged changes in simple words.
3. Creates a commit: `git commit -m "fix: sanitize user input in login route"`.
4. Prompts the student: *"Your changes are committed locally. Would you like me to push them to GitHub now?"*
