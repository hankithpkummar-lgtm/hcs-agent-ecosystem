# Link Analyser

> **The permanent Link Analysis & Fix Engine for OpenCode**

---

## Overview

Link Analyser is an autonomous link analysis and fix engine that:

- Detects links in prompts
- Analyzes link functionality
- Tests all features
- Fixes identified issues
- Suggests improvements
- Auto-implements approved fixes
- Triggers Tester and Deployer agents
- Generates update logs

---

## Features

### Link Analysis

- **HTTP Status** — Check if link is accessible
- **Response Time** — Measure loading speed
- **SSL Certificate** — Verify security
- **DNS Resolution** — Check domain resolution
- **Content Loading** — Verify all content loads
- **Asset Loading** — Check CSS, JS, images
- **Redirects** — Track redirect chains
- **Broken Links** — Find broken links

### Issue Detection

- **404 Errors** — Page not found
- **500 Errors** — Server errors
- **SSL Errors** — Certificate issues
- **DNS Errors** — Domain resolution issues
- **Timeouts** — Slow loading
- **Connection Issues** — Server unavailable

### Auto-Fix Capabilities

- **Broken Links** — Update link URLs
- **Missing Assets** — Restore or replace
- **Slow Loading** — Optimize resources
- **SSL Issues** — Fix certificates
- **DNS Issues** — Fix records
- **404 Errors** — Create pages
- **500 Errors** — Fix server issues

### Improvement Suggestions

- **Performance** — Speed optimization
- **Security** — SSL, headers, auth
- **SEO** — Meta tags, structured data
- **Accessibility** — WCAG compliance
- **UX** — Better navigation, design
- **Content** — Better copy, images

### Agent Integration

- **Tester Agent** — Full test suite
- **Deployer Agent** — Deployment

---

## Installation

The Link Analyser skill is installed at:
```
~/.config/opencode/skills/link-analyser/
```

---

## Usage

### Analyze a Link

```
"Analyze this link: https://example.com"
"Check if this site is working: https://example.com"
"Test this URL: https://example.com"
```

### Fix Link Issues

```
"Fix the broken link on https://example.com"
"Repair the 404 error on https://example.com"
"Fix the SSL issue on https://example.com"
```

### Get Improvements

```
"Suggest improvements for https://example.com"
"How can I improve this link?"
"Optimize this website"
```

### Full Analysis

```
"Full analysis of https://example.com"
"Complete check of this link"
"Analyze and fix everything"
```

---

## Auto-Trigger Keywords

| Category | Keywords |
|----------|----------|
| Link Analysis | analyze link, check link, test link, url, link |
| Website | website, webpage, site, page |
| Protocol | http, https, http://, https:// |
| Issues | broken, error, 404, 500, ssl, dns |
| Fix | fix, repair, resolve, correct |
| Improve | improve, optimize, enhance, upgrade |
| Test | test, verify, validate, check |

---

## How It Works

### 12-Stage Pipeline

1. **Link Detection** — Find links in prompt
2. **Link Validation** — Check if accessible
3. **Analysis Scope** — Determine what to analyze
4. **HTTP Analysis** — Check status, response time
5. **SSL Analysis** — Verify certificate
6. **DNS Analysis** — Check resolution
7. **Content Analysis** — Verify all loads
8. **Issue Detection** — Find problems
9. **Fix Generation** — Create fixes
10. **Improvement Suggestions** — Suggest enhancements
11. **Agent Deployment** — Trigger Tester/Deployer
12. **Update Log** — Document everything

---

## Analysis Checklist

### Link Health

- [ ] HTTP status = 200
- [ ] Response time < 3s
- [ ] SSL certificate valid
- [ ] DNS resolves correctly
- [ ] No redirects (or valid)
- [ ] No broken links

### Content Quality

- [ ] All text loads
- [ ] All images load
- [ ] All CSS loads
- [ ] All JavaScript loads
- [ ] No console errors
- [ ] No mixed content

### Security

- [ ] HTTPS enabled
- [ ] Security headers present
- [ ] No mixed content
- [ ] CORS configured
- [ ] CSP configured

### Performance

- [ ] Page load < 3s
- [ ] Images optimized
- [ ] CSS minified
- [ ] JavaScript minified
- [ ] GZIP enabled
- [ ] Caching configured

---

## Fix Templates

### Fix Broken Link

```html
<!-- Before -->
<a href="https://old-url.com/page">Link</a>

<!-- After -->
<a href="https://new-url.com/page">Link</a>
```

### Fix Missing Asset

```html
<!-- Before -->
<link rel="stylesheet" href="styles.css">

<!-- After -->
<link rel="stylesheet" href="/assets/css/styles.css">
```

### Fix Slow Loading

```html
<!-- Before -->
<img src="large-image.jpg">

<!-- After -->
<img src="optimized-image.jpg" loading="lazy" alt="Description">
```

---

## Improvement Suggestions

### Performance

| Improvement | Priority | Impact |
|-------------|----------|--------|
| Enable GZIP | High | Faster loading |
| Add caching | High | Faster repeat visits |
| Optimize images | High | Faster loading |
| Minify CSS/JS | Medium | Faster loading |
| Use CDN | Medium | Faster global access |

### Security

| Improvement | Priority | Impact |
|-------------|----------|--------|
| Enable HTTPS | High | Secure connection |
| Add security headers | High | Protect against attacks |
| Fix mixed content | High | Secure loading |
| Add CSP | Medium | Prevent XSS |
| Add CORS | Medium | Control access |

### SEO

| Improvement | Priority | Impact |
|-------------|----------|--------|
| Add title tag | High | Better ranking |
| Add meta description | High | Better CTR |
| Add alt text | High | Image SEO |
| Add schema markup | Medium | Rich snippets |
| Add sitemap | Medium | Better crawling |

---

## Update Log Format

```markdown
## Link Analysis Report

**URL:** [Link]
**Date:** [Timestamp]
**Status:** [Healthy/Issues Found]

### Issues Found
1. [Issue] - [Severity]

### Fixes Applied
1. [Fix] - [Status]

### Improvements Suggested
1. [Improvement] - [Priority]

### Test Results
- [Test]: ✅ Pass / ❌ Fail

### Agent Handoff
- **Tester Agent:** Triggered
- **Deployer Agent:** Pending
```

---

## Agent Integration

### Tester Agent

After analysis, Tester Agent:
- Runs full test suite
- Verifies all fixes
- Checks for regressions
- Confirms all passes

### Deployer Agent

After tests pass, Deployer Agent:
- Deploys changes
- Verifies deployment
- Reports status

---

## Quality Checklist

### Analysis Quality

- [ ] All HTTP checks performed
- [ ] SSL certificate verified
- [ ] DNS resolution checked
- [ ] Content analyzed
- [ ] Assets checked
- [ ] Security headers verified
- [ ] Performance measured
- [ ] SEO analyzed

### Fix Quality

- [ ] All issues identified
- [ ] Fixes verified
- [ ] No regressions
- [ ] Performance improved
- [ ] Security enhanced
- [ ] Documentation updated

---

## Error Handling

### Common Errors

| Error | Solution |
|-------|----------|
| 404 Not Found | Check URL, create page |
| 500 Server Error | Check server logs |
| SSL Error | Fix certificate |
| DNS Error | Fix records |
| Timeout | Check server, optimize |
| Connection Refused | Check server status |

---

## Support

For issues or questions:
1. Check the SKILL.md file
2. Review analysis reports
3. Check error logs
4. Contact support

---

## License

MIT License

---

**Remember:** Always detect links. Always analyze completely. Always generate update logs. Always suggest improvements. Always trigger Tester and Deployer agents. Never fix without approval. Never deploy without testing.
