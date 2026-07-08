# Tester — Logic Tester & Logic Analyzer

> **The permanent Testing & Logic Analysis Engine for OpenCode**

---

## Overview

Tester is an autonomous testing and logic analysis engine that:

- Tests links and websites
- Analyzes and debugs logic
- Fixes errors automatically
- Suggests improvements
- Triggers deployment on success
- Learns from errors to prevent future issues

---

## Features

### Link Testing
- HTTP status verification
- Response time measurement
- SSL certificate validation
- Content verification
- Asset loading checks

### Logic Analysis
- Code flow analysis
- Error detection
- Logic validation
- Performance analysis
- Security checks

### Error Debugging
- Root cause analysis
- Automatic fixing
- Prevention rules
- Error history tracking
- Self-learning system

### Improvement Suggestions
- Code optimization
- Better error handling
- Enhanced security
- Improved readability
- Performance improvements

### Auto-Deployment
- Triggers on test success
- Deploys to any platform
- Verifies deployment
- Reports status

---

## Installation

The Tester skill is installed at:
```
~/.config/opencode/skills/tester/
```

---

## Usage

### Test a Link

```
"Test this link: https://example.com"
"Check if the site is working"
"Verify the URL"
```

### Analyze Logic

```
"Analyze the logic in this code"
"Test the login function"
"Check the checkout logic"
```

### Debug Code

```
"Debug the error in checkout"
"Fix the bug in login"
"Find the error in calculation"
```

### Get Improvements

```
"Suggest improvements"
"Optimize this code"
"How can I improve this?"
```

---

## Auto-Trigger Keywords

| Category | Keywords |
|----------|----------|
| Testing | test, check, verify, validate, run tests |
| Link Testing | test link, check site, verify url, test site |
| Logic Testing | test logic, check logic, verify logic, analyze logic |
| Debugging | debug, fix bug, find error, troubleshoot |
| Analysis | analyze, review, audit, inspect, examine |
| Improvement | improve, optimize, enhance, upgrade, refactor |
| Logic Fixes | fix logic, correct logic, repair logic |
| Suggestions | suggest, recommendation, advice, improve |

---

## How It Works

### 10-Stage Pipeline

1. **Request Understanding** — Analyze user request
2. **Link/Logic Analysis** — Analyze target
3. **Test Generation** — Create test cases
4. **Test Execution** — Run all tests
5. **Error Detection** — Identify failures
6. **Logic Analysis** — Analyze logic flow
7. **Error Fixing** — Fix errors
8. **Improvement Suggestions** — Suggest improvements
9. **Re-testing** — Verify fixes work
10. **Deployment Trigger** — Deploy on success

---

## Error Learning

### Learning Process

1. Capture error details
2. Analyze root cause
3. Generate fix
4. Add prevention rule
5. Add test case
6. Update knowledge base

### Prevention Rules

| Error | Prevention |
|-------|------------|
| Null Reference | Check for null |
| Type Error | Validate types |
| Division by Zero | Check denominator |
| Array Bounds | Check index |
| Timeout | Handle timeout |
| Network Error | Add retry |

---

## Quality Standards

### Testing Checklist

- [ ] All scenarios tested
- [ ] Edge cases covered
- [ ] Error handling verified
- [ ] Performance acceptable
- [ ] Security checked
- [ ] Accessibility verified
- [ ] Tests documented
- [ ] Fixes verified
- [ ] No regressions
- [ ] Deployer triggered

---

## Agent Integration

### Deployer Agent

When all tests pass, the Tester Agent automatically triggers the Deployer Agent:

1. Generates test report
2. Triggers Deployer Agent
3. Provides deployment context
4. Monitors deployment
5. Verifies deployment success

### Other Agents

The Tester Agent works with:
- **Universal Prompt Builder** — For initial development
- **Deployer Agent** — For deployment
- **UI Designer Agent** — For UI testing
- **Skill Builder Agent** — For skill testing

---

## Configuration

### Test Configuration

```json
{
  "test_settings": {
    "timeout": 30000,
    "retries": 3,
    "parallel": true,
    "report_format": "markdown"
  }
}
```

### Deployment Settings

```json
{
  "deployment": {
    "auto_deploy": true,
    "platform": "github-pages",
    "verify": true,
    "notify": true
  }
}
```

---

## Error History

The Tester maintains a JSON error history:

```json
{
  "error_history": [
    {
      "timestamp": "2026-07-07T22:50:00Z",
      "error_type": "logic",
      "error_message": "Division by zero",
      "fix_applied": "Added zero check",
      "prevention": "Added input validation",
      "test_added": "test_divide_by_zero"
    }
  ]
}
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Tests not running | Check test configuration |
| Deployment fails | Check deployment settings |
| Logic errors | Analyze code flow |
| Performance issues | Optimize code |

---

## Support

For issues or questions:
1. Check the SKILL.md file
2. Review test reports
3. Check error history
4. Contact support

---

## License

MIT License

---

**Remember:** Always test before deploy. Always analyze logic. Always suggest improvements. Always trigger deployer on success.
