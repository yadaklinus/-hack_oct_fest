# Student Code Mentor Skill

This skill helps students and developers write clean, secure, and efficient code tailored to any programming language of their choice, including JavaScript, Python, TypeScript, and more. It also coaches users on safe Git practices, ensuring code is reviewed before committing and never pushed without explicit permission.

---

## Example Prompts That Trigger This Skill

You can ask your AI agent any of the following to trigger this skill:

- *"Review my code for security issues and suggest best practices."*
- *"I am using Python for this project. Tailor your advice and code checks to Python."*
- *"Can you explain how this code works behind the scenes in simple words?"*
- *"Help me review and commit my changes to Git."*
- *"Audit my script before I run it on my server."*

---

## What Is in This Repository

This repository follows the official Agent Skill standard:

- **`SKILL.md`**: The instruction card that your AI agent reads first. It instructs the agent to detect your programming language, explain concepts gently, run audits, and follow safe Git rules.
- **`scripts/`**: Contains small, focused programs that the AI agent runs directly to complete exact jobs.
  - **`scripts/audit_code.py`**: A multi-language code inspector that scans JavaScript, Python, and other files for security vulnerabilities, secret leaks, performance bottlenecks, and bad patterns.
- **`references/`**: Contains in-depth reference documentation opened only when extra guidance is needed.
  - **`references/best_practices.md`**: A beginner-friendly guide covering universal security standards, language-specific rules, and the Conventional Commit standard.

---

## Installation

### 1. One-Command Install (Recommended)

You can install this skill into your AI agent with a single command using `npx`:

```bash
npx skills add yadaklinus/-hack_oct_fest
```

### 2. Preview Before Installing

To inspect the skill's contents before installing:

```bash
npx skills add yadaklinus/-hack_oct_fest --list
```

### 3. Manual Install for Claude Code

If you prefer to install manually for Claude Code:

1. Clone this repository:
   ```bash
   git clone https://github.com/yadaklinus/-hack_oct_fest.git
   ```
2. Copy the entire folder into your skills directory:
   - **For a single project**: `.claude/skills/student-code-mentor/`
   - **For personal / global use**: `~/.claude/skills/student-code-mentor/`

### 4. Support for Other Agents

Other AI agents and coding tools (such as Cursor, OpenCode, and compatible tools) are supported directly through the `npx skills add` command.

---

## How to Test That It Works

1. Install the skill using the command above.
2. Open your AI agent chat in your project.
3. Ask the agent:
   > *"I'm working in Python. Can you audit my code for security issues and help me commit the changes?"*
4. The agent will read `SKILL.md`, run `scripts/audit_code.py` on your code, explain the findings in plain English, and ask for your confirmation before running any Git push.

---

## Hacktoberfest Note

This project was built for the **Hacktoberfest** hackathon! Open-source contributions, suggestions, and improvements from developers and students of all experience levels are warmly welcomed. Please feel free to open an issue or submit a pull request!
