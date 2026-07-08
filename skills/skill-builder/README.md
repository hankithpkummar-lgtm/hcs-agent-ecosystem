# OpenCode Skill Builder

**Version:** 1.0.0  
**Trigger:** `skill-builder`  
**Category:** Development, Automation, Prompt Engineering, AI

---

## Overview

The OpenCode Skill Builder is an autonomous skill factory responsible for designing, researching, generating, testing, deploying, updating, and maintaining OpenCode Skills. It handles the complete skill lifecycle from initial requirements to production deployment.

## Installation

### Automatic Installation

This skill is automatically installed when the `skill-builder` trigger is activated for the first time.

### Manual Installation

1. Create the skill directory:
   ```bash
   mkdir -p ~/.config/opencode/skills/skill-builder
   ```

2. Copy all skill files to the directory:
   - `SKILL.md` (main skill file)
   - `README.md` (this file)
   - `CHANGELOG.md` (version history)
   - `config.json` (configuration)
   - `examples.md` (usage examples)
   - `prompts.md` (prompt templates)

3. Restart OpenCode to load the new skill.

## Usage

### Basic Usage

Simply type the trigger keyword in OpenCode:

```
skill-builder
```

Or use any alias:
- `builder`
- `create-skill`
- `new-skill`
- `edit-skill`
- `update-skill`
- `skill-manager`
- `skill-factory`

### Example Prompts

**Create a new skill:**
```
skill-builder: Create a skill for analyzing CSV data and generating reports
```

**Update an existing skill:**
```
skill-builder: Update the ui-designer skill to support dark mode
```

**Get help with skill development:**
```
skill-builder: What are best practices for creating OpenCode skills?
```

## Features

### Complete Skill Lifecycle

1. **Requirement Collection** — Interview-based requirement gathering
2. **Requirement Expansion** — Automatic feature suggestions
3. **Research Engine** — Best practices and existing solutions
4. **Architecture Design** — Complete skill structure planning
5. **Prompt Engineering** — Optimized AI prompts
6. **Skill Generation** — Production-ready skill files
7. **Validation** — Comprehensive quality checks
8. **Testing** — Normal, edge, and failure cases
9. **Optimization** — Performance and token efficiency
10. **Documentation** — README, CHANGELOG, examples
11. **Deployment** — Automatic installation
12. **Version Management** — Semantic versioning
13. **Continuous Improvement** — Monitoring and updates

### Automatic Features

- **Interview Protocol** — Never builds without requirements
- **Research Integration** — Investigates best practices
- **Architecture Planning** — Designs complete structure
- **Quality Validation** — Tests before deployment
- **Auto-Documentation** — Generates complete docs
- **Auto-Deployment** — Installs to correct directory
- **Version Control** — Tracks all changes
- **Compatibility Checks** — Ensures model support

## Configuration

### config.json

```json
{
  "name": "OpenCode Skill Builder",
  "version": "1.0.0",
  "settings": {
    "auto_deploy": true,
    "auto_document": true,
    "auto_test": true,
    "validate_before_deploy": true,
    "preserve_customizations": true,
    "skills_directory": "~/.config/opencode/skills/"
  }
}
```

### Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `auto_deploy` | boolean | `true` | Automatically deploy skills after generation |
| `auto_document` | boolean | `true` | Automatically generate documentation |
| `auto_test` | boolean | `true` | Automatically test skills before deployment |
| `validate_before_deploy` | boolean | `true` | Validate skills before deployment |
| `preserve_customizations` | boolean | `true` | Preserve user customizations when updating |
| `skills_directory` | string | `~/.config/opencode/skills/` | Default skills directory |

## Examples

### Example 1: Create a Data Analysis Skill

```
User: skill-builder

AI: I'll help you create a new OpenCode skill. Let me start by collecting requirements.

What is the skill name?
User: data-analyzer

What is the purpose?
User: Analyze CSV data and generate insights

What input does it accept?
User: CSV files

What output does it produce?
User: Markdown reports with charts

[... interview continues ...]

[Skill is generated, tested, and deployed]
```

### Example 2: Update an Existing Skill

```
User: skill-builder: Update the ui-designer skill to add support for Vue.js

AI: I'll update the ui-designer skill. Let me first read the existing skill.

[Reads existing skill files]
[Identifies current architecture]
[Plans Vue.js integration]
[Merges changes carefully]
[Preserves existing features]
[Updates documentation]
[Deploys updated skill]
```

## Troubleshooting

### Common Issues

**Issue:** Skill trigger not recognized
**Solution:** Restart OpenCode after installation. Verify files are in the correct directory.

**Issue:** Skill not appearing in skill list
**Solution:** Check that `SKILL.md` exists in the skill directory. Verify frontmatter is valid YAML.

**Issue:** Deployment fails
**Solution:** Check filesystem permissions. Verify the skills directory exists and is writable.

**Issue:** Skill conflicts with existing skill
**Solution:** Use a different trigger name. Check existing triggers before deployment.

## Best Practices

1. **Always interview first** — Never start building without complete requirements
2. **Research before building** — Investigate best practices and existing solutions
3. **Expand requirements** — Suggest missing features and improvements
4. **Validate everything** — Test before deployment
5. **Document thoroughly** — Every skill needs README, CHANGELOG, and examples
6. **Version properly** — Use semantic versioning for all changes
7. **Preserve customizations** — Never overwrite user modifications blindly
8. **Monitor after deployment** — Track usage and feedback for improvements

## Contributing

Contributions to the OpenCode Skill Builder are welcome. Please follow the existing code style and include tests for new features.

## License

MIT

## Support

For issues and questions, please refer to the main OpenCode documentation or open an issue in the repository.
