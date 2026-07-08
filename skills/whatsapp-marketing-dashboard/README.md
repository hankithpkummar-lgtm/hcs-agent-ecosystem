# WhatsApp Marketing Dashboard

> **The permanent WhatsApp Marketing Dashboard for OpenCode**

---

## Overview

WhatsApp Marketing Dashboard is an autonomous WhatsApp marketing engine that:

- Analyzes website links
- Generates professional WhatsApp messages
- Provides one-click WhatsApp send
- Manages customer database
- Tracks message history
- Analytics and reporting

---

## Features

### Link Analysis

- **Auto-Detect Links** — Find all links on website
- **Categorize Links** — Products, services, blogs, etc.
- **Filter Shareable** — Only shareable links
- **Link Metadata** — Title, description, image

### Message Generation

- **Product Share** — Share products with customers
- **Service Share** — Share services with customers
- **Blog Share** — Share articles with customers
- **Offer Share** — Share special offers
- **Custom Messages** — User-defined templates

### One-Click WhatsApp

- **WhatsApp URL API** — `https://wa.me/{number}?text={message}`
- **Auto-Open WhatsApp** — Open WhatsApp Web/App
- **Pre-filled Message** — Message ready to send
- **Copy to Clipboard** — One-click copy

### Customer Management

- **Customer List** — Store customer numbers
- **Customer Names** — Associate names with numbers
- **Customer Groups** — Group customers
- **Quick Access** — Quick access to recent

### Dashboard Features

- **Admin Dashboard Only** — Only visible in admin panel
- **Suitable Placement** — Under Marketing section
- **Message Preview** — Preview before sending
- **Message History** — Track sent messages

---

## Installation

The WhatsApp Marketing Dashboard skill is installed at:
```
~/.config/opencode/skills/whatsapp-marketing-dashboard/
```

---

## Usage

### Extract Links from Website

```
"Extract links from my website"
"Analyze links on example.com"
"Get all shareable links"
```

### Generate WhatsApp Message

```
"Generate WhatsApp message for product"
"Create message for service"
"Make message for blog post"
```

### Send WhatsApp Message

```
"Send message to +1234567890"
"Open WhatsApp for customer"
"Send product link to customer"
```

### Manage Customers

```
"Add customer to list"
"Show recent customers"
"Group customers by type"
```

---

## Auto-Trigger Keywords

| Category | Keywords |
|----------|----------|
| WhatsApp | whatsapp, message, send, chat |
| Marketing | marketing, campaign, promote, share |
| Dashboard | dashboard, admin, panel |
| Customer | customer, client, contact |
| Links | links, share, shareable |

---

## How It Works

### 9-Stage Pipeline

1. **Request Detection** — Detect marketing request
2. **Link Analysis** — Extract and categorize links
3. **Message Generation** — Create professional messages
4. **Template Selection** — Choose message template
5. **Message Preview** — Preview before sending
6. **Customer Selection** — Select or enter customer
7. **Phone Validation** — Validate phone number
8. **WhatsApp Open** — Open WhatsApp with message
9. **History Tracking** — Track sent messages

---

## Dashboard Layout

```
┌─────────────────────────────────────────────────────────────┐
│                    WhatsApp Marketing Dashboard              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Total Links │  │ Messages    │  │ Customers   │        │
│  │     25      │  │    Sent     │  │    150      │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Link Analysis                                      │   │
│  │  [Extract Links from Website]                       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Message Generator                                  │   │
│  │  [Select Link] [Template] [Preview] [Send]         │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Send to Customer                                  │   │
│  │  [Customer] [Phone] [Open WhatsApp]                │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Message Templates

### Product Share

```
🛍️ *Check out this amazing product!*

{product_name}

{product_description}

💰 Price: {product_price}

👉 {product_link}

_Direct message me for orders!_
```

### Service Share

```
💼 *Our Professional Service*

{service_name}

{service_description}

✅ Trusted by 1000+ clients

👉 {service_link}

_Schedule a free consultation!_
```

### Blog Share

```
📚 *Interesting Article*

{blog_title}

{blog_excerpt}

👉 {blog_link}

_Share with friends who need this!_
```

### Offer Share

```
🎉 *Special Offer Just For You!*

{offer_title}

{offer_description}

⏰ Limited time only!

👉 {offer_link}

_Don't miss out!_
```

---

## Link Categorization

| Category | Patterns |
|----------|----------|
| **Product** | /product/, /shop/, /buy/, /item/, /store/ |
| **Service** | /service/, /consulting/, /agency/, /freelance/ |
| **Blog** | /blog/, /article/, /post/, /news/, /story/ |
| **About** | /about/, /team/, /company/, /story/, /mission/ |
| **Contact** | /contact/, /support/, /help/, /faq/, /chat/ |
| **Offer** | /offer/, /deal/, /discount/, /sale/, /promo/ |

---

## Customer Management

### Customer Groups

| Group | Description |
|-------|-------------|
| **vip** | High-value customers |
| **regular** | Regular customers |
| **new** | New customers |
| **inactive** | Inactive customers |
| **leads** | Potential customers |

### Quick Access

- **Recent** — Last 7 days
- **Favorites** — Pinned customers
- **VIP** — High-value customers
- **All** — All customers

---

## Phone Validation

### International Support

| Country | Code | Flag |
|---------|------|------|
| USA/Canada | +1 | 🇺🇸 |
| UK | +44 | 🇬🇧 |
| India | +91 | 🇮🇳 |
| Australia | +61 | 🇦🇺 |
| China | +86 | 🇨🇳 |
| Japan | +81 | 🇯🇵 |
| Germany | +49 | 🇩🇪 |
| France | +33 | 🇫🇷 |

### Validation Rules

- Length: 7-15 digits
- Format: Numbers only
- Country code required

---

## Analytics & Tracking

### Message Analytics

- Total messages sent
- Messages today/week/month
- Top template used
- Top customer group
- Average messages per day

### Link Analytics

- Total links found
- Most shared link
- Links by type
- Share frequency

---

## Security & Privacy

### Admin Only Access

- Restrict to admin users
- Role-based access control
- Audit logging

### Rate Limiting

- Max 50 messages per hour
- Cooldown period
- Prevent spam

### Data Privacy

- Encrypt phone numbers
- Anonymize analytics
- Data retention policy
- Require consent

---

## Quality Checklist

### Dashboard Quality

- [ ] Admin only access
- [ ] Suitable heading
- [ ] Clean layout
- [ ] Mobile responsive
- [ ] Fast loading
- [ ] Error handling

### Message Quality

- [ ] Professional tone
- [ ] Clear CTA
- [ ] Proper formatting
- [ ] Working links
- [ ] Emoji usage

### WhatsApp Integration

- [ ] URL generation works
- [ ] Message encoding correct
- [ ] Opens WhatsApp
- [ ] Copy to clipboard works
- [ ] History tracking

---

## Agent Integration

### Works With

- **Universal Prompt Builder** — For initial requests
- **Link Analyser Agent** — For link analysis
- **Tester Agent** — For testing
- **Deployer Agent** — For deployment

---

## Configuration

### Dashboard Settings

```json
{
  "dashboard_settings": {
    "admin_only": true,
    "placement": "marketing",
    "heading": "WhatsApp Marketing Dashboard",
    "theme": "professional"
  }
}
```

### Message Settings

```json
{
  "message_settings": {
    "default_template": "product",
    "auto_preview": true,
    "copy_to_clipboard": true,
    "track_history": true
  }
}
```

### Customer Settings

```json
{
  "customer_settings": {
    "store_customers": true,
    "quick_access": true,
    "groups": true,
    "notes": true
  }
}
```

---

## Error Handling

### Common Errors

| Error | Solution |
|-------|----------|
| Invalid phone | Check format, add country code |
| WhatsApp not opening | Check URL, try manual copy |
| Links not found | Check website URL |
| Message too long | Shorten message |
| Rate limit exceeded | Wait for cooldown |

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

**Remember:** Always analyze website links. Always generate professional messages. Always validate phone numbers. Always track message history. Always provide message preview. Always use admin only access. Never spam customers. Never skip phone validation.
