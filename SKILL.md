---
name: student-code-mentor
description: Guides students and developers in writing clean, secure, and efficient code tailored to any programming language, auditing code for common pitfalls, and managing safe git commits. Use when asked "review my code", "check my code for security issues", "help me commit my changes", "tailor this to Python/JavaScript", or "explain how this code works".
---

# Student Code Mentor Skill

This customizable skill guides students and developers in writing clean, high-performance, and secure code in any programming language (JavaScript, Python, TypeScript, and more) while maintaining safe Git habits.

## Step-by-Step Instructions

### Step 1: Detect or Ask for the Programming Language
1. Inspect the user's project files to detect the active language (for example, `.js` for JavaScript, `.py` for Python, `.ts` for TypeScript).
2. If the language is not clear or if the user requests a specific language, tailor all explanations, examples, and checks to that language.

### Step 2: Explain Concepts Simply
- Use plain language and beginner-friendly analogies tailored to the language mechanism (such as explaining the Node.js event loop or Python's GIL).
- Avoid unnecessary jargon. Focus on cause and effect: explain why an approach is unsafe or slow and how the cleaner pattern works.

### Step 3: Run the Multi-Language Audit Script
When auditing code or checking if a solution is safe and properly structured:
1. Run the audit script located at `scripts/audit_code.py`:
   ```bash
   python scripts/audit_code.py <path-to-file>
   ```
2. You can also specify the target language explicitly:
   ```bash
   python scripts/audit_code.py <path-to-file> --lang <language>
   ```
3. To run a built-in demo check:
   ```bash
   python scripts/audit_code.py --demo --lang <javascript|python>
   ```
4. Present the audit findings in a friendly, constructive way: highlight line numbers, explain the risk, and provide the fix.

### Step 4: Consult Language & Git Best Practices
Open `references/best_practices.md` whenever you need in-depth guidance on:
- Universal security standards (preventing secret leaks and injection).
- Language-specific patterns for JavaScript, Python, and other stacks.
- Conventional Commit conventions (`feat:`, `fix:`, `docs:`, `refactor:`).

### Step 5: Safe Git Commits & Confirmation Rule
When helping users record changes with Git:
1. Review status with `git status` and inspect modifications with `git diff`.
2. Stage only intentional files using `git add <file>`.
3. Draft a conventional commit message following `references/best_practices.md`.
4. **MANDATORY PUSH CONFIRMATION**: Never run `git push` automatically. Always stop and explicitly ask the developer for confirmation:
   > *"I have created commit `<message>`. Would you like me to push these changes to GitHub now?"*

---

## Examples

### Example 1: Tailoring to Python
**Student**: *"I'm working in Python. Can you check my main.py script for bad habits?"*  
**Agent Action**:
1. Runs `python scripts/audit_code.py main.py --lang python`.
2. Identifies a mutable default argument (`def add(item, items=[])`) and a bare `except:`.
3. Explains to the student why `items=None` avoids shared state bugs across function calls.

### Example 2: Safe Git Commit Flow
**Student**: *"I finished my changes. Help me commit them to Git."*  
**Agent Action**:
1. Checks modified files using `git status`.
2. Stages the files and creates commit: `git commit -m "feat: add secure authentication handler"`.
3. Prompts the student: *"Your changes are committed locally. Are you ready for me to push them to GitHub?"*
