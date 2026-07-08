---
name: "HCS Skill File Converter"
description: "HCS Skill File Converter v1.0 — Autonomous Skill File Conversion & Calculation Engine. Converts skill files between formats, extracts calculations, and validates skill structures."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Skill File Converter

## Purpose

Convert skill files between formats, extract and validate calculations within skill files, and transform skill structures for different platforms.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| **Format Conversion** | Convert between SKILL.md formats |
| **Calculation Extraction** | Extract calculations from skills |
| **Calculation Validation** | Validate calculation logic |
| **Calculation Conversion** | Convert calculations to code |

## Calculation Types

| Type | Description | Example |
|------|-------------|---------|
| **Formula** | Mathematical formulas | `price = quantity × unit_price` |
| **Conditional** | If/else logic | `discount = isVip ? 0.2 : 0.1` |
| **Aggregation** | Sum, average, count | `total = sum(items.map(i => i.price))` |
| **Transformation** | Data conversion | `celsius = (fahrenheit - 32) × 5/9` |
| **Validation** | Input validation | `isValid = email.includes('@')` |
| **Lookup** | Reference data | `taxRate = taxTable[state]` |

## Conversion Formats

| From | To | Use Case |
|------|----|----------|
| **SKILL.md** | JSON | Parse skill files |
| **JSON** | TypeScript | Generate TS code |
| **JSON** | Python | Generate Python code |
| **JSON** | Documentation | Generate docs |
| **JSON** | Tests | Generate test cases |

## Calculation Extraction

```typescript
// Example: Extract from SKILL.md
const skillMarkdown = `
## CALCULATIONS

### Price Calculation
\`\`\`
formula: price = quantity × unit_price
variables:
  - quantity: number (required)
  - unit_price: number (required)
  - discount: number (default: 0)
output: price (number)
\`\`\`
`;

// Extracted calculation:
{
  name: "Price Calculation",
  formula: "price = quantity × unit_price",
  variables: [
    { name: "quantity", type: "number", required: true },
    { name: "unit_price", type: "number", required: true },
    { name: "discount", type: "number", required: false, default: "0" }
  ],
  output: { name: "price", type: "number" }
}
```

## Generated Code Examples

### TypeScript
```typescript
interface PriceCalculation {
  quantity: number;
  unit_price: number;
  discount?: number;
}

function calculatePrice(data: PriceCalculation): number {
  const { quantity, unit_price, discount = 0 } = data;
  const subtotal = quantity * unit_price;
  const discountAmount = subtotal * discount;
  return subtotal - discountAmount;
}
```

### Python
```python
def calculate_price(quantity: float, unit_price: float, discount: float = 0) -> float:
    subtotal = quantity * unit_price
    discount_amount = subtotal * discount
    return subtotal - discount_amount
```

## Validation Rules

| Rule | Description |
|------|-------------|
| **Formula Syntax** | Must contain assignment (=) |
| **Variable Usage** | All declared vars used in formula |
| **Type Consistency** | Variables match expected types |
| **Required Check** | Required vars have no defaults |
| **Output Type** | Output matches formula result |

## Final Instructions

### Domain Rules
1. Parse skill file structure correctly
2. Extract all calculations with variables
3. Validate calculation logic
4. Convert between formats accurately
5. Preserve calculation semantics

### Fabel5 Quality Rules
6. Be skeptical — Find issues, don't confirm everything
7. Be thorough — Check every claim
8. Be honest — Say clearly if wrong
9. Be specific — Provide exact findings
10. Be constructive — Suggest fixes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## FABEL5 DISCIPLINE (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**This skill follows the Fabel5 six-phase senior-engineer loop.**

### Core Principle: THE MAKER IS NEVER THE GRADER

| Phase | Action |
|-------|--------|
| **1. THINK** | Map system, find source of truth, diagnose from real artifact |
| **2. DECOMPOSE** | Split into ONE bounded units, parallel where possible |
| **3. PROVE IT** | Build, run tests, validate — never claim without evidence |
| **4. RESPECT INTENT** | Never reverse decisions silently, surface recommendations |
| **5. VERIFY DELIVERY** | Confirm change landed, skeptic pass, fix critical issues first |
| **6. LEAVE NAVIGABLE** | Update notes, codify rules, write STATE.md |

### Evidence-Based Claims

| Type | Definition |
|------|------------|
| **CONFIRMED** | Verified with evidence source |
| **INFERRED** | Reasonable assumption (flag risk) |
| **UNVERIFIED** | Needs checking (note method) |
