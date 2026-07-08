# Google Apps Script Builder

> **The permanent Google Apps Script & Sheet Builder for OpenCode**

---

## Overview

Google Apps Script Builder is an autonomous Google Apps Script and Sheet Builder that:

- Builds Google Apps Script for any purpose
- Creates professionally designed Google Sheets
- Adds self-check and validation systems
- Provides automation and triggers
- Maintains sheets with scheduled tasks
- Suggests improvements before building

---

## Features

### Sheet Design

- **Professional Design** — Clean, modern look
- **Color Schemes** — Multiple professional themes
- **Typography** — Clear, readable fonts
- **Borders & Alignment** — Clean formatting
- **Conditional Formatting** — Status indicators
- **Auto-Filters** — Quick data filtering

### Self-Check Systems

- **Data Validation** — Validate all inputs
- **Duplicate Detection** — Find duplicates
- **Missing Data** — Highlight empty cells
- **Format Check** — Verify formats
- **Range Validation** — Check value ranges
- **Reference Check** — Verify linked data

### Automation

- **On-Edit Triggers** — React to edits
- **Time-Driven Tasks** — Scheduled automation
- **Custom Menus** — Easy access to tools
- **Form Integration** — Form submissions
- **Email Notifications** — Send alerts
- **Data Sync** — Keep data updated

### Apps Script

- **Custom Functions** — Sheet formulas
- **Sidebars** — Custom UI panels
- **Dialogs** — Popup windows
- **Properties Service** — Store settings
- **Cache Service** — Cache data
- **UrlFetchApp** — HTTP requests

---

## Installation

The Google Apps Script Builder skill is installed at:
```
~/.config/opencode/skills/google-apps-script-builder/
```

---

## Usage

### Build a Google Sheet

```
"Build a project management Google Sheet"
"Create a financial tracking spreadsheet"
"Make a data entry form in Google Sheets"
```

### Add Self-Checks

```
"Add data validation to my sheet"
"Find duplicates in my spreadsheet"
"Highlight empty cells in my sheet"
```

### Automate Tasks

```
"Add a custom menu to my sheet"
"Create a daily report automation"
"Send email when data changes"
```

### Design Sheets

```
"Apply professional design to my sheet"
"Add color coding to my spreadsheet"
"Make my sheet look modern"
```

---

## Auto-Trigger Keywords

| Category | Keywords |
|----------|----------|
| Google Apps Script | google apps script, apps script, script |
| Google Sheets | google sheet, spreadsheet, sheet, sheets |
| Automation | automate, automation, trigger, schedule |
| Self-Check | validate, validation, check, verify |
| Design | design, format, style, theme |
| Maintenance | maintain, maintenance, cleanup, archive |

---

## How It Works

### Workflow

1. **Request Understanding** — Analyze user request
2. **Gather Details** — Ask for sheet information
3. **Suggest Improvements** — Provide enhancement ideas
4. **Wait for Approval** — Build only when user says so
5. **Design Sheet** — Apply professional design
6. **Build Script** — Create Apps Script
7. **Add Self-Checks** — Implement validation
8. **Test & Verify** — Ensure everything works
9. **Deploy & Document** — Publish and document

### Before Building

**ALWAYS:**
1. Ask for sheet details
2. Suggest improvements
3. Wait for user approval
4. Then build

---

## Sheet Design Templates

### Data Tracking Sheet

```
| ID | Name | Status | Date | Notes |
|----|------|--------|------|-------|
| Auto | Text | Dropdown | Auto | Text |
```

### Project Management Sheet

```
| Task | Assignee | Priority | Due Date | Status | Notes |
|------|----------|----------|----------|--------|-------|
| Text | Dropdown | Dropdown | Date | Dropdown | Text |
```

### Financial Tracking Sheet

```
| Date | Description | Category | Income | Expense | Balance |
|------|-------------|----------|--------|---------|---------|
| Date | Text | Dropdown | Currency | Currency | Formula |
```

---

## Self-Check Systems

### Data Validation

```javascript
// Add data validation to a range
function addValidation(sheet, range, rule) {
  const rangeObj = sheet.getRange(range);
  const validation = SpreadsheetApp.newDataValidation()
    .requireValueInList(rule.values)
    .setAllowInvalid(false)
    .build();
  rangeObj.setDataValidation(validation);
}
```

### Duplicate Detection

```javascript
// Find duplicates in a column
function findDuplicates(sheet, column) {
  const data = sheet.getRange(column + ":" + column).getValues();
  const seen = new Set();
  const duplicates = [];
  
  data.forEach((row, index) => {
    if (seen.has(row[0])) {
      duplicates.push(index + 1);
    } else {
      seen.add(row[0]);
    }
  });
  
  return duplicates;
}
```

### Missing Data Detection

```javascript
// Find empty cells
function findEmptyCells(sheet, range) {
  const rangeObj = sheet.getRange(range);
  const values = rangeObj.getValues();
  const emptyCells = [];
  
  values.forEach((row, rowIndex) => {
    row.forEach((cell, colIndex) => {
      if (cell === "" || cell === null) {
        emptyCells.push({
          row: rowIndex + 1,
          col: colIndex + 1
        });
      }
    });
  });
  
  return emptyCells;
}
```

---

## Design Automation

### Auto-Design Features

```javascript
// Apply professional design to sheet
function applyDesign(sheet) {
  // Freeze header row
  sheet.setFrozenRows(1);
  
  // Set header style
  const headerRange = sheet.getRange(1, 1, 1, sheet.getLastColumn());
  headerRange.setBackground("#4CAF50");
  headerRange.setFontColor("#FFFFFF");
  headerRange.setFontWeight("bold");
  headerRange.setHorizontalAlignment("center");
  
  // Auto-resize columns
  for (let i = 1; i <= sheet.getLastColumn(); i++) {
    sheet.autoResizeColumn(i);
  }
  
  // Add borders
  const dataRange = sheet.getDataRange();
  dataRange.setBorder(true, true, true, true, true, true);
  
  // Alternating row colors
  for (let i = 2; i <= sheet.getLastRow(); i++) {
    const rowRange = sheet.getRange(i, 1, 1, sheet.getLastColumn());
    if (i % 2 === 0) {
      rowRange.setBackground("#F5F5F5");
    } else {
      rowRange.setBackground("#FFFFFF");
    }
  }
}
```

### Color Scheme Templates

```javascript
// Professional color schemes
const colorSchemes = {
  business: {
    header: "#2196F3",
    subheader: "#BBDEFB",
    alternating: ["#FFFFFF", "#E3F2FD"],
    accent: "#1976D2"
  },
  modern: {
    header: "#9C27B0",
    subheader: "#E1BEE7",
    alternating: ["#FFFFFF", "#F3E5F5"],
    accent: "#7B1FA2"
  },
  nature: {
    header: "#4CAF50",
    subheader: "#C8E6C9",
    alternating: ["#FFFFFF", "#E8F5E9"],
    accent: "#388E3C"
  },
  minimal: {
    header: "#607D8B",
    subheader: "#CFD8DC",
    alternating: ["#FFFFFF", "#ECEFF1"],
    accent: "#455A64"
  }
};
```

---

## Automation Templates

### On-Edit Trigger

```javascript
// Custom onEdit function
function onEdit(e) {
  const sheet = e.source.getActiveSheet();
  const range = e.range;
  
  // Add your automation logic here
  // Example: Auto-update timestamp
  if (range.getColumn() === 1) { // Column A
    sheet.getRange(range.getRow(), 2).setValue(new Date());
  }
}
```

### Time-Driven Trigger

```javascript
// Daily maintenance task
function dailyMaintenance() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  // Your maintenance logic here
  // Example: Archive old data
  // Example: Send reports
  // Example: Update dashboards
}
```

### Custom Menu

```javascript
// Add custom menu
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  
  ui.createMenu('Custom Tools')
    .addItem('Validate Data', 'validateData')
    .addItem('Generate Report', 'generateReport')
    .addItem('Archive Old Data', 'archiveData')
    .addToUi();
}
```

---

## Quality Checklist

### Sheet Quality

- [ ] Professional design applied
- [ ] Headers formatted
- [ ] Data validation added
- [ ] Conditional formatting applied
- [ ] Auto-filters enabled
- [ ] Protection configured
- [ ] Print area set
- [ ] Documented

### Script Quality

- [ ] All functions tested
- [ ] Error handling added
- [ ] Performance optimized
- [ ] Documentation complete
- [ ] Triggers configured
- [ ] Permissions set
- [ ] Version controlled

### Self-Check Quality

- [ ] Data validation working
- [ ] Duplicate detection active
- [ ] Missing data highlighting
- [ ] Format validation enabled
- [ ] Range validation configured
- [ ] Reference checking active

---

## Improvement Suggestions

### Before Building

**ALWAYS suggest improvements:**

1. **Design Enhancements** — Better colors, fonts, layout
2. **Automation Ideas** — Additional automations
3. **Self-Check Features** — More validation rules
4. **Performance Optimizations** — Faster scripts
5. **Security Improvements** — Better protection
6. **Documentation** — Better usage guides

### Suggestion Format

```markdown
## Improvement Suggestions

### 1. [Suggestion Title]
**Priority:** High/Medium/Low
**Impact:** [What this improves]

**Current Design:**
[description]

**Suggested Improvement:**
[improvement]

**Benefits:**
- [Benefit 1]
- [Benefit 2]
```

---

## Deployment

### Steps

1. Create sheet with proper structure
2. Apply professional design
3. Add data validation
4. Create Apps Script
5. Add automation triggers
6. Test all features
7. Document usage
8. Schedule maintenance

---

## Error Handling

### Common Errors

| Error | Solution |
|-------|----------|
| Permission denied | Check sharing settings |
| Script limit exceeded | Optimize code |
| Trigger failed | Recreate trigger |
| Data validation failed | Check rule syntax |
| Design not applied | Check range references |

---

## Maintenance

### Regular Tasks

| Task | Frequency |
|------|-----------|
| Data cleanup | Weekly |
| Script optimization | Monthly |
| Design updates | Quarterly |
| Security review | Monthly |
| Backup | Daily |

---

## Agent Integration

### Works With

- **Universal Prompt Builder** — For initial requests
- **Tester Agent** — For testing sheets
- **Deployer Agent** — For deployment
- **Skill Builder Agent** — For building skills

---

## Configuration

### Sheet Settings

```json
{
  "sheet_settings": {
    "design": "business",
    "validation": true,
    "self_checks": true,
    "automation": true,
    "documentation": true
  }
}
```

### Script Settings

```json
{
  "script_settings": {
    "triggers": true,
    "custom_menu": true,
    "error_handling": true,
    "performance": true
  }
}
```

---

## Support

For issues or questions:
1. Check the SKILL.md file
2. Review documentation
3. Check error logs
4. Contact support

---

## License

MIT License

---

**Remember:** Always ask for details before building. Always suggest improvements first. Always build only when user says so. Always apply professional design. Always add self-check systems. Always test before deploy. Always document everything.
