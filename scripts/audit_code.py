#!/usr/bin/env python3
"""
scripts/audit_code.py

Purpose:
  A fast, beginner-friendly static checker for JavaScript and Node.js files.
  It inspects code for common security vulnerabilities, performance anti-patterns,
  and outdated syntax, then outputs plain-English suggestions and fixes.

How to run:
  python scripts/audit_code.py <path-to-javascript-file>

Examples:
  python scripts/audit_code.py server.js
  python scripts/audit_code.py --demo
"""

import sys
import re
import os

RULES = [
    {
        "id": "SEC-001",
        "category": "Security",
        "severity": "CRITICAL",
        "pattern": r"\beval\s*\(",
        "message": "Dangerous 'eval()' detected. It can execute malicious arbitrary code.",
        "fix": "Use safer alternatives such as JSON.parse() or dedicated parser libraries."
    },
    {
        "id": "SEC-002",
        "category": "Security",
        "severity": "HIGH",
        "pattern": r"(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{8,}['\"]",
        "message": "Possible hardcoded secret or credential detected in source code.",
        "fix": "Store secrets in an external .env file and access them with process.env.SECRET_NAME."
    },
    {
        "id": "SEC-003",
        "category": "Security",
        "severity": "HIGH",
        "pattern": r"\bchild_process\b.*\bexec\s*\([^)]*\+",
        "message": "String concatenation inside child_process.exec() can lead to Command Injection.",
        "fix": "Use execFile() or spawn() with argument arrays instead of concatenated shell strings."
    },
    {
        "id": "PERF-001",
        "category": "Performance",
        "severity": "WARNING",
        "pattern": r"\bfs\.(readFileSync|writeFileSync|existsSync)\s*\(",
        "message": "Synchronous file system call detected. This blocks the single-threaded Node.js event loop.",
        "fix": "Use fs.promises (e.g., await fs.promises.readFile) so other requests are not blocked."
    },
    {
        "id": "PERF-002",
        "category": "Performance",
        "severity": "WARNING",
        "pattern": r"for\s*\([^)]+\)\s*\{[^}]*await\s+",
        "message": "Sequential 'await' inside a standard loop may slow down batch operations.",
        "fix": "If iterations are independent, consider Promise.all(items.map(...)) for concurrent execution."
    },
    {
        "id": "STYLE-001",
        "category": "Code Quality",
        "severity": "INFO",
        "pattern": r"\bvar\s+[a-zA-Z_$]",
        "message": "'var' has function-scoping and hoisting behaviors that cause confusing bugs for beginners.",
        "fix": "Replace 'var' with 'const' (default) or 'let' (if the value reassigns)."
    },
    {
        "id": "STYLE-002",
        "category": "Code Quality",
        "severity": "INFO",
        "pattern": r"[^!=]==[^=]",
        "message": "Loose equality '==' performs unexpected type coercion in JavaScript.",
        "fix": "Use strict equality '===' to verify both type and value."
    }
]

DEMO_CODE = """// Sample beginner JavaScript code for demonstration
const fs = require('fs');

var userRole = "guest";
const apiKey = "DEMO_KEY_abc123456789_dummy_token";

function authenticateUser(input) {
  if (userRole == "admin") {
    eval(input); // Dangerous dynamic execution
  }
  const config = fs.readFileSync('config.json', 'utf8');
  return config;
}
"""

def audit_code(content: str, filename: str = "snippet"):
    findings = []
    lines = content.splitlines()

    for line_num, line in enumerate(lines, start=1):
        # Skip commented lines
        stripped = line.strip()
        if stripped.startswith("//") or stripped.startswith("*"):
            continue

        for rule in RULES:
            if re.search(rule["pattern"], line, re.IGNORECASE):
                findings.append({
                    "id": rule["id"],
                    "category": rule["category"],
                    "severity": rule["severity"],
                    "line_num": line_num,
                    "code_snippet": line.strip(),
                    "message": rule["message"],
                    "fix": rule["fix"]
                })

    return findings

def print_report(findings, source_label):
    print("=" * 65)
    print(f" JS/Node.js Code Audit Report: {source_label}")
    print("=" * 65)

    if not findings:
        print("[SUCCESS] No critical security or quality issues detected!")
        print("Your JavaScript code looks clean and adheres to student best practices.")
        print("=" * 65)
        return 0

    critical_count = sum(1 for f in findings if f["severity"] == "CRITICAL")
    high_count = sum(1 for f in findings if f["severity"] == "HIGH")
    warn_count = sum(1 for f in findings if f["severity"] == "WARNING")
    info_count = sum(1 for f in findings if f["severity"] == "INFO")

    print(f"Found {len(findings)} suggestion(s): "
          f"{critical_count} Critical, {high_count} High, {warn_count} Warning, {info_count} Info\n")

    for idx, item in enumerate(findings, start=1):
        badge = f"[{item['severity']}] [{item['category']}]"
        print(f"{idx}. {badge} Line {item['line_num']}: {item['id']}")
        print(f"   Code:    {item['code_snippet']}")
        print(f"   Why:     {item['message']}")
        print(f"   Fix:     {item['fix']}")
        print("-" * 65)

    print("\nTip: Refer to 'references/best_practices.md' for complete examples and explanations.")
    print("=" * 65)
    return 1 if (critical_count + high_count) > 0 else 0

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("--help", "-h"):
        print("Usage: python scripts/audit_code.py <file.js> | --demo")
        print("Runs a beginner-friendly security and quality audit on JavaScript/Node.js files.")
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "--demo":
        findings = audit_code(DEMO_CODE, "Built-in Demo Snippet")
        exit_code = print_report(findings, "Demo Sample File")
        sys.exit(exit_code)

    file_path = arg
    if not os.path.exists(file_path):
        print(f"Error: File not found: '{file_path}'")
        sys.exit(2)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(2)

    findings = audit_code(content, file_path)
    exit_code = print_report(findings, file_path)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
