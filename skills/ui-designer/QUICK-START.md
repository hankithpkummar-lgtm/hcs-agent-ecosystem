# Quick Start: Universal Master Development Agent v3.0

## Installation (2 Minutes)

### Step 1: Download the Skill File
Download: [MASTER-SKILL-v3.md](sandbox:///mnt/agents/output/master-skill-v3/MASTER-SKILL-v3.md)

### Step 2: Create Project Folder
```bash
mkdir my-project
cd my-project
mkdir -p src docs skills .github/workflows scripts .backups
```

### Step 3: Copy Skill File
```bash
cp /path/to/MASTER-SKILL-v3.md skills/
```

### Step 4: Load in OpenCode
In OpenCode chat, paste:
```
Load the Master Skill from skills/MASTER-SKILL-v3.md.
I want to build [your project description].
```

## Example Usage

### Example: Astrology Website
```
You: "Load the Master Skill. I want to build an astrology website 
      with Lo Shu Grid calculator from my PDF guide."

Agent: "I'll help you build an astrology website. Let me start with 
       the Router to classify your request..."

[Agent 0: Router]
-> "Classified as: Build request, Domain: Astrology, Source: PDF"

[Agent 1: Architecture Designer]
-> "What tech stack? React + Python? Database? Hosting?"
-> Generates ARCHITECTURE.md, ADRs, DATA-FLOW.md

[Agent 2: Gatekeeper]
-> "What problem does Lo Shu Grid solve? Which PDF page?"
-> Researches best practices
-> Generates Master Prompt
-> "Approve?"

You: "Approve"

[Agent 3: Context Manager]
-> Summarizes session, prunes old messages

[Agent 2: Execution]
-> Writes code per Master Prompt

[Agent 4: Tester]
-> Backup -> Test -> Debug -> Fix -> Re-test
-> "All tests pass"

[Agent 5: Code Reviewer]
-> Reviews code quality
-> "Code review pass"

[Agent 6: Security Auditor]
-> Scans for vulnerabilities
-> "Birth data encrypted. No critical issues."

[Agent 7: Dependency Auditor]
-> Checks packages for CVEs
-> "All dependencies safe"

[Agent 8: Performance Optimizer]
-> "Bundle: 180KB. API: 120ms. Lighthouse: 92."

[Agent 9: Accessibility Validator]
-> "WCAG 2.1 AA compliant. Screen reader ready."

[Agent 10: Documentation Co-Author]
-> Auto-generates API docs, user guide, README updates

[Agent 11: Human-in-the-Loop]
-> "Production deployment requires your approval."

You: "Approve"

[Agent 12: Cost Controller]
-> "Total cost: X tokens. Within budget."

[Agent 13: Deployer]
-> Deploys to Vercel + Render
-> "Live at https://..."

[Agent 14: Monitoring & Incident Response]
-> Sets up Sentry, health checks, alerts

[Self-Evolution]
-> "Knowledge base updated. Version 1.0 -> 1.1"
-> "Learned: Birth data = PII. Cache planetary positions."

You: "Done!"
```

## Commands

```bash
# One-command full pipeline
npm run ship        # Architecture -> Test -> Security -> Deploy

# Individual phases
npm run test:all    # Run all tests
npm run audit       # Security + Dependency audit
npm run perf        # Performance check
npm run a11y        # Accessibility check
npm run deploy      # Deploy only
npm run backup      # Manual backup
npm run rollback    # Emergency rollback
npm run monitor     # Check monitoring status
```

## File Structure After Setup

```
my-project/
├── skills/
│   └── MASTER-SKILL-v3.md       # This skill file
├── src/                          # Your code
├── tests/                        # Test files
├── docs/                         # Auto-generated docs
│   ├── calculations/
│   ├── features/
│   ├── api/
│   ├── architecture/
│   ├── security/
│   ├── performance/
│   ├── accessibility/
│   ├── deployment/
│   └── sources/                  # Original PDFs, links, texts
├── .backups/                     # Automatic backups
├── .github/workflows/            # CI/CD
│   └── master-pipeline.yml       # Full 15-agent pipeline
├── scripts/                      # Helper scripts
│   ├── deploy.sh
│   ├── test.sh
│   ├── backup.sh
│   └── rollback.sh
├── monitoring/                   # Monitoring configs
│   ├── sentry.properties
│   ├── health-checks.yml
│   └── alert-rules.yml
├── vercel.json / render.yaml     # Platform configs
├── .env.example                  # Environment variables template
├── .gitignore
├── package.json / requirements.txt
└── README.md
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Skill not loading" | Check file path, ensure YAML frontmatter |
| "Agent skipped a phase" | Say: "Please follow the Master Skill workflow" |
| "Tests failing" | Tester auto-fixes, or escalate to you |
| "Security audit failed" | Fix critical issues, or override with documented risk |
| "Deployment failed" | Deployer auto-fixes common issues |
| "Cost too high" | Cost Controller suggests optimizations |
| "Want to skip workflow" | System enforces it -- trust the process |

## Next Steps

1. Download MASTER-SKILL-v3.md
2. Set up project folder
3. Load skill in OpenCode
4. Say: "Let's build my project"
5. Follow the 15-agent pipeline
6. Watch it self-evolve

**Happy building!**
