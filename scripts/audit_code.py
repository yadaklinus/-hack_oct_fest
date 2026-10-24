#!/usr/bin/env python3
"""
scripts/audit_code.py

Purpose:
  A customizable, beginner-friendly static checker for code quality and security.
  Supports JavaScript, TypeScript, Python, and general code files.
  Users can specify their language or let the script auto-detect from file extension.

How to run:
  python scripts/audit_code.py <file-path> [--lang <language>]
  python scripts/audit_code.py --demo [--lang <javascript|python>]

Examples:
  python scripts/audit_code.py app.js
  python scripts/audit_code.py main.py
  python scripts/audit_code.py script.txt --lang python
  python scripts/audit_code.py --demo --lang javascript
  python scripts/audit_code.py --demo --lang python
"""

import sys
import re
import os

# Universal rules (apply to any language)
UNIVERSAL_RULES = [
    {
        "id": "SEC-SECRET",
        "category": "Security",
        "severity": "HIGH",
        "pattern": r"(api[_-]?key|secret|password|private[_-]?key|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{8,}['\"]",
        "message": "Possible hardcoded secret or credential detected in source code.",
        "fix": "Store credentials in an external .env file and load them via environment variables."
    },
    {
        "id": "SEC-INJECT",
        "category": "Security",
        "severity": "HIGH",
        "pattern": r"\b(exec|system|popen)\s*\([^)]*\+",
        "message": "String concatenation inside command execution may allow Command Injection.",
        "fix": "Pass arguments as a safe array/list instead of concatenating raw shell strings."
    }
]

# Language-specific rules
LANGUAGE_RULES = {
    "javascript": [
        {
            "id": "JS-SEC-001",
            "category": "Security",
            "severity": "CRITICAL",
            "pattern": r"\beval\s*\(",
            "message": "Dangerous 'eval()' detected. It can execute arbitrary malicious code.",
            "fix": "Use JSON.parse() or dedicated parsing libraries instead of eval()."
        },
        {
            "id": "JS-PERF-001",
            "category": "Performance",
            "severity": "WARNING",
            "pattern": r"\bfs\.(readFileSync|writeFileSync)\s*\(",
            "message": "Synchronous file system call detected. This blocks the single-threaded Node.js event loop.",
            "fix": "Use fs.promises (e.g., await fs.promises.readFile) so other requests are not blocked."
        },
        {
            "id": "JS-STYLE-001",
            "category": "Code Quality",
            "severity": "INFO",
            "pattern": r"\bvar\s+[a-zA-Z_$]",
            "message": "'var' is function-scoped and hoisted, which often leads to accidental bugs.",
            "fix": "Replace 'var' with 'const' (default) or 'let' (if the value reassigns)."
        },
        {
            "id": "JS-STYLE-002",
            "category": "Code Quality",
            "severity": "INFO",
            "pattern": r"[^!=]==[^=]",
            "message": "Loose equality '==' performs unexpected type coercion in JavaScript.",
            "fix": "Use strict equality '===' to verify both type and value."
        }
    ],
    "python": [
        {
            "id": "PY-SEC-001",
            "category": "Security",
            "severity": "CRITICAL",
            "pattern": r"\b(eval|exec)\s*\(",
            "message": "Dynamic execution with eval()/exec() is unsafe when handling user input.",
            "fix": "Use ast.literal_eval() for safe literal evaluation or dedicated serializers."
        },
        {
            "id": "PY-STYLE-001",
            "category": "Code Quality",
            "severity": "WARNING",
            "pattern": r"except\s*:",
            "message": "Bare 'except:' catches all exceptions, including KeyboardInterrupt and SystemExit.",
            "fix": "Specify the exact exception type (e.g., 'except ValueError:') or 'except Exception:'."
        },
        {
            "id": "PY-STYLE-002",
            "category": "Code Quality",
            "severity": "WARNING",
            "pattern": r"def\s+[a-zA-Z0-9_]+\s*\([^)]*=\s*(\[\]|\{\})",
            "message": "Mutable default argument (list/dict) detected. It retains state across calls.",
            "fix": "Use None as the default argument (e.g., arg=None) and initialize inside the function."
        }
    ]
}

# Aliases for file extensions
EXT_MAP = {
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "javascript",
    ".tsx": "javascript",
    ".mjs": "javascript",
    ".cjs": "javascript",
    ".py": "python"
}

DEMO_SNIPPETS = {
    "javascript": """// JavaScript sample demonstration
const fs = require('fs');

var role = "guest";
const apiKey = "DEMO_KEY_abc123456789_dummy_token";

function runAction(command) {
  if (role == "admin") {
    eval(command);
  }
  const config = fs.readFileSync('config.json', 'utf8');
  return config;
}
""",
    "python": """# Python sample demonstration
import os

api_token = "DEMO_TOKEN_abc123456789_dummy_token"

def add_item(item, items=[]):
    items.append(item)
    return items

def execute_user_script(user_code):
    try:
        eval(user_code)
    except:
        pass
"""
}

def detect_language(file_path: str, forced_lang: str = None) -> str:
    if forced_lang:
        cleaned = forced_lang.lower().strip()
        if "js" in cleaned or "node" in cleaned or "javascript" in cleaned or "typescript" in cleaned:
            return "javascript"
        if "py" in cleaned or "python" in cleaned:
            return "python"
        return cleaned

    _, ext = os.path.splitext(file_path)
    return EXT_MAP.get(ext.lower(), "universal")

def audit_code(content: str, language: str):
    findings = []
    lines = content.splitlines()

    active_rules = list(UNIVERSAL_RULES)
    if language in LANGUAGE_RULES:
        active_rules.extend(LANGUAGE_RULES[language])

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()
        # Skip pure comments
        if stripped.startswith("//") or stripped.startswith("#") or stripped.startswith("*"):
            continue

        for rule in active_rules:
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

def print_report(findings, source_label, language):
    print("=" * 65)
    print(f" Code Audit Report: {source_label} (Language: {language.upper()})")
    print("=" * 65)

    if not findings:
        print("[SUCCESS] No critical security or quality issues detected!")
        print("Your code looks clean and adheres to recommended student best practices.")
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

    print("\nTip: Refer to 'references/best_practices.md' for guidelines tailored to your language.")
    print("=" * 65)
    return 1 if (critical_count + high_count) > 0 else 0

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("--help", "-h"):
        print("Usage: python scripts/audit_code.py <file-path> [--lang <language>]")
        print("       python scripts/audit_code.py --demo [--lang <javascript|python>]")
        print("\nSupported languages: JavaScript, TypeScript, Python, and general code.")
        sys.exit(0)

    forced_lang = None
    if "--lang" in sys.argv:
        idx = sys.argv.index("--lang")
        if idx + 1 < len(sys.argv):
            forced_lang = sys.argv[idx + 1]

    if sys.argv[1] == "--demo":
        lang = detect_language("", forced_lang or "javascript")
        demo_text = DEMO_SNIPPETS.get(lang, DEMO_SNIPPETS["javascript"])
        findings = audit_code(demo_text, lang)
        exit_code = print_report(findings, f"Demo {lang.capitalize()} Sample", lang)
        sys.exit(exit_code)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File not found: '{file_path}'")
        sys.exit(2)

    lang = detect_language(file_path, forced_lang)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(2)

    findings = audit_code(content, lang)
    exit_code = print_report(findings, file_path, lang)
    sys.exit(exit_code)

if __name__ == "__main__":
    main()
