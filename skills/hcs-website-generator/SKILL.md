---
name: "HCS Website Generator"
description: "HCS Website Generator v1.0 — Autonomous Website Generation Engine. Takes analyzed content and generates complete website code. Works with any framework (React, Next.js, Vue, HTML)."
metadata:
  author: "HCS"
  version: "1.0"
---

# HCS Website Generator

## Purpose
Generate complete, production-ready websites from analyzed content.

## Framework Support

| Framework | Files Generated | Use Case |
|-----------|----------------|----------|
| **Next.js + Tailwind** | `app/`, `components/`, `public/` | Default, SSG/SSR |
| **React + Tailwind** | `src/`, `components/` | SPA, client-side |
| **Vue + Tailwind** | `src/`, `components/` | Vue ecosystem |
| **HTML + CSS** | `index.html`, `styles/` | Simple, no build tools |

## Website Generation Pipeline

```
INPUT: Structured Content (from Document Analyzer)
    |
    v
STEP 1: CONTENT ANALYSIS
    |-- Analyze content structure
    |-- Identify page requirements
    |-- Determine layout needs
    |-- Plan navigation structure
    |
    v
STEP 2: FRAMEWORK SELECTION
    |-- Detect existing project framework
    |-- Use user-specified framework
    |-- Default to Next.js + Tailwind
    |
    v
STEP 3: PAGE PLANNING
    |-- Generate sitemap
    |-- Plan page layouts
    |-- Design component structure
    |-- Plan responsive behavior
    |
    v
STEP 4: COMPONENT GENERATION
    |-- Generate layout components
    |-- Generate page components
    |-- Generate UI components
    |-- Generate utility functions
    |
    v
STEP 5: PAGE GENERATION
    |-- Generate each page
    |-- Apply content to pages
    |-- Implement responsive design
    |-- Add animations/interactions
    |
    v
STEP 6: STYLING
    |-- Apply color scheme
    |-- Apply typography
    |-- Apply spacing
    |-- Apply responsive styles
    |
    v
STEP 7: QUALITY CHECK
    |-- Validate code
    |-- Test responsiveness
    |-- Check accessibility
    |-- Verify content placement
    |
    v
OUTPUT: Complete Website Code
```

## Standard Pages

| Page | Content Source | Layout |
|------|---------------|--------|
| **Home** | Hero, features, testimonials, CTA | Landing page |
| **About** | Company info, team, story | Content page |
| **Services** | Service list, details, pricing | Grid/list |
| **Products** | Product catalog, details, pricing | Grid/catalog |
| **Portfolio** | Project showcase, case studies | Gallery |
| **Contact** | Contact form, map, details | Form + info |
| **Blog** | Articles, posts, news | List/detail |
| **FAQ** | Questions and answers | Accordion/list |
| **Pricing** | Pricing tiers, features | Comparison table |
| **Testimonials** | Customer reviews | Cards/carousel |

## Component Generation

### Layout Components
| Component | Purpose |
|-----------|---------|
| `Header` | Navigation, logo, CTA |
| `Footer` | Links, copyright, social |
| `Sidebar` | Secondary navigation |
| `Layout` | Page wrapper |

### Page Components
| Component | Purpose |
|-----------|---------|
| `HeroSection` | Hero image, title, subtitle, CTA |
| `FeaturesSection` | Feature grid/list |
| `TestimonialsSection` | Customer reviews |
| `PricingSection` | Pricing tables |
| `ContactSection` | Contact form |
| `AboutSection` | Company info |
| `ServicesSection` | Service cards |
| `PortfolioSection` | Project gallery |

### UI Components
| Component | Purpose |
|-----------|---------|
| `Button` | CTA buttons |
| `Card` | Content cards |
| `Modal` | Popup dialogs |
| `Form` | Input forms |
| `Table` | Data tables |
| `Accordion` | Expandable content |
| `Carousel` | Image/content slider |
| `Tabs` | Tabbed content |

## Content Mapping

| Content Type | Website Element |
|-------------|-----------------|
| **Title** | Page title, hero heading |
| **Headings** | Section headings |
| **Paragraphs** | Body content |
| **Lists** | Feature lists, bullet points |
| **Tables** | Pricing tables, data tables |
| **Images** | Hero images, section images |
| **Links** | Navigation, CTAs |
| **Business Info** | About section, contact info |
| **Services** | Services page, feature cards |
| **Products** | Product catalog, cards |
| **Pricing** | Pricing page, tables |
| **Testimonials** | Testimonial section, cards |

## Quality Standards

### Code Quality
| Standard | Requirement |
|----------|-------------|
| **Clean Code** | Readable, maintainable |
| **Consistent** | Unified patterns |
| **Documented** | Comments where needed |
| **Typed** | TypeScript when possible |

### Performance
| Metric | Target |
|--------|--------|
| **First Contentful Paint** | < 1.5s |
| **Largest Contentful Paint** | < 2.5s |
| **Cumulative Layout Shift** | < 0.1 |
| **Bundle Size** | < 200KB initial |

### Accessibility
| Standard | Requirement |
|----------|-------------|
| **WCAG** | 2.1 AA compliance |
| **Semantic HTML** | Proper heading hierarchy |
| **Alt Text** | All images have alt text |
| **Keyboard Nav** | Full keyboard navigation |

## Generated Files Structure

```
project/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── about/
│   │   └── page.tsx
│   ├── services/
│   │   └── page.tsx
│   ├── contact/
│   │   └── page.tsx
│   └── globals.css
├── components/
│   ├── layout/
│   │   ├── Header.tsx
│   │   └── Footer.tsx
│   ├── sections/
│   │   ├── HeroSection.tsx
│   │   ├── FeaturesSection.tsx
│   │   └── TestimonialsSection.tsx
│   └── ui/
│       ├── Button.tsx
│       └── Card.tsx
├── lib/
│   └── utils.ts
├── public/
│   └── images/
├── tailwind.config.ts
├── package.json
└── README.md
```

## Integration with Other Agents

| Agent | Integration |
|-------|-------------|
| **HCS Document Analyzer** | Receives structured content |
| **HCS Brand Analyzer** | Receives brand guidelines |
| **HCS Content Planner** | Receives sitemap and structure |
| **HCS Design Analyzer** | Receives design specifications |
| **HCS Data Linker** | Links to backend/data sources |
| **HCS UI Designer** | Receives design enhancements |
| **HCS Local Host Testing** | Tests generated website |
| **HCS Human Tester** | Validates user experience |
| **HCS Deployer** | Deploys to production |

## Final Instructions

1. **NEVER skip content analysis** — Always understand content first
2. **NEVER guess content** — Use only extracted content
3. **ALWAYS generate complete code** — No placeholders or TODOs
4. **ALWAYS ensure responsiveness** — Mobile-first design
5. **ALWAYS follow best practices** — Clean, maintainable code
6. **ALWAYS test quality** — Validate before delivering
7. **ALWAYS optimize performance** — Fast loading times
8. **ALWAYS ensure accessibility** — WCAG compliance
9. **ALWAYS integrate** — Work with other agents
10. **ALWAYS save linking_info.json** — For other agents to use
