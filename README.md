# JS & Node.js Student Mentor Skill

This skill teaches students how to write secure, clean, and high-performance JavaScript and Node.js code. It also guides students through safe Git version control practices, ensuring code is reviewed before committing and never pushed without permission.

---

## Example Prompts That Trigger This Skill

You can ask your AI agent any of the following questions to trigger this skill:

- *"How do I make sure my JavaScript code is secure and properly structured?"*
- *"Can you explain how the Node.js event loop works in simple words?"*
- *"Review my server.js file for performance bottlenecks or security risks."*
- *"Help me commit my changes to Git and write a good commit message."*
- *"Check my Node.js script for dangerous functions before I run it."*

---

## What Is in This Repository

This repository is built with a simple, standard Agent Skill layout:

- **`SKILL.md`**: The main instruction card that your AI agent always reads first. It tells the agent how to teach concepts gently, when to run audit scripts, and how to safely handle Git commits.
- **`scripts/`**: Holds small programs that the agent can run directly to perform exact jobs.
  - **`scripts/audit_code.py`**: A Python scanner that checks JavaScript/Node.js files for dangerous methods (`eval`), hardcoded secrets, blocking synchronous file calls, and outdated syntax.
- **`references/`**: Contains extra reading material that the agent opens only when in-depth guidance is needed.
  - **`references/best_practices.md`**: A student-friendly handbook explaining Node.js architecture, security rules, performance tips, and the Conventional Commit standard.

---

## Installation

### 1. One-Command Install (Recommended)

You can install this skill into your agent with a single command using `npx`:

```bash
npx skills add YOUR_GITHUB_USERNAME/REPO_NAME
```

*(Replace `YOUR_GITHUB_USERNAME` and `REPO_NAME` with your actual GitHub username and repository name.)*

### 2. Preview Before Installing

To check the contents of the skill before adding it:

```bash
npx skills add YOUR_GITHUB_USERNAME/REPO_NAME --list
```

### 3. Manual Install for Claude Code

If you prefer a manual setup in Claude Code:

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/REPO_NAME.git
   ```
2. Copy the entire folder into your skills directory:
   - **For a single project**: `.claude/skills/js-node-mentor/`
   - **For personal / global use**: `~/.claude/skills/js-node-mentor/`

### 4. Support for Other Agents

Other AI agents and coding tools (such as Cursor, OpenCode, and compatible tools) are supported directly through the `npx skills add` command.

---

## How to Test That It Works

1. Install the skill using the command above.
2. Open your AI agent chat in your project.
3. Ask the agent:
   > *"Can you audit my JavaScript code for security issues and help me commit the changes?"*
4. The agent will read `SKILL.md`, run `scripts/audit_code.py`, point out any issues with simple explanations, and prompt you before running any Git push.

---

## Hacktoberfest Note

This project was built for the **Hacktoberfest** hackathon! Open-source contributions, suggestions, and improvements from developers and students of all experience levels are warmly welcomed. Please check the issues or submit a pull request!
"# -hack_oct_fest" 
