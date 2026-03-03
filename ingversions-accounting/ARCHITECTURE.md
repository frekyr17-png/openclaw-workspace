# ingversions digital - MS Teams Integrated Accounting System
## Architecture Design v1.0

### Overview
Complete HR/Payroll/Expense management system integrated with Microsoft Teams for ingversions digital, featuring:
- Employee data management
- Automated payslip generation
- Form 16 (Indian tax) generation
- Expense tracking and reporting
- Monthly financial reports sent to Teams

---

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         MICROSOFT TEAMS                                │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                   │
│  │  Employee    │  │   Admin      │  │   Finance    │                   │
│  │    Forms     │  │   Dashboard  │  │    Reports   │                   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘                   │
│         └─────────────────┼───────────────────┘                         │
│                           │                                             │
└───────────────────────────┼─────────────────────────────────────────────┘
                            │ HTTPS/Graph API
                    ┌───────▼────────┐
                    │   N8n Workflow │
                    │    Engine      │
                    │  (localhost)   │
                    └───────┬────────┘
            ┌───────────────┼───────────────┐
            │               │               │
    ┌───────▼────┐  ┌──────▼─────┐  ┌──────▼──────┐
    │  SQLite/   │  │  PDF Gen   │  │  Email/     │
    │  Postgres  │  │  (HTML→PDF)│  │  MS Graph   │
    │  Database  │  │            │  │  Teams      │
    └────────────┘  └────────────┘  └─────────────┘
```

---

## Module Breakdown

### 1. Data Layer (SQLite/PostgreSQL)
**Tables:**
- `employees` - Employee master data
- `salary_records` - Monthly salary computations
- `attendance` - Days worked tracking
- `expenses` - Client/categorized expenses
- `clients` - Client master with revenue tracking
- `form16_data` - Annual tax data
- `document_logs` - Generated document audit trail

### 2. Workflow Layer (n8n)
**Core Workflows:**
1. **Employee Onboarding** - Teams form → DB entry → Welcome alert
2. **Monthly Salary Processing** - Attendance + Salary calc → Payslip PDF → Teams notification
3. **Expense Entry** - Teams form → Categorization → DB storage
4. **Monthly Report** - Aggregate data → PDF report → Teams channel post
5. **Form 16 Generation** (Annual, Apr) - Compile yearly data → Form 16 PDF → Employee DM
6. **Account Review Dashboard** - Real-time metrics → Adaptive Card → Teams

### 3. Presentation Layer (MS Teams)
**Adaptive Cards:**
- Employee data entry form
- Expense submission form
- Admin dashboard view
- Payslip viewer card
- Monthly report card with PDF attachment

### 4. Document Generation
**Templates:**
- HTML-based payslip template (wkhtmltopdf/Playwright)
- Form 16 template per Indian tax regulations
- Monthly report template with charts

---

## Data Flow Examples

### Payslip Generation Flow
```
[Schedule: 25th of each month]
        │
        ▼
[Query: Get all active employees]
        │
        ▼
[Query: Get attendance for month]
        │
        ▼
[Calculate: Base + Allowances - Deductions = Net Pay]
        │
        ▼
[Generate: HTML Payslip → PDF]
        │
        ▼
[Send: Teams adaptive card with PDF to employee]
        │
        ▼
[Log: Document generated in audit trail]
```

### Expense Tracking Flow
```
[Trigger: Employee submits Teams expense form]
        │
        ▼
[Store: Expense data with client/category tags]
        │
        ▼
[Update: Client profitability metrics]
        │
        ▼
[Notify: Finance team via Teams]
        │
        ▼
[Monthly: Rollup into financial report]
```

---

## Security & Compliance

- **Data Privacy:** Employee PII encrypted at rest
- **Access Control:** Teams SSO for authentication
- **Audit Trail:** All document generation logged
- **Backup:** Daily DB dump to secure storage

---

## Deployment Requirements

| Component | Version | Notes |
|-----------|---------|-------|
| n8n | 1.8+ | Self-hosted with Teams credentials |
| Node.js | 20+ | For PDF generation service |
| SQLite/Postgres | 15+ | Primary database |
| wkhtmltopdf | 0.12+ | HTML to PDF conversion |
| MS Graph API | v1.0 | Teams integration |

---

## File Structure

```
ingversions-accounting/
├── ARCHITECTURE.md          # This document
├── SCHEMA.sql               # Database schema
├── workflows/
│   ├── employee-onboarding.json
│   ├── monthly-payroll.json
│   ├── expense-tracking.json
│   ├── monthly-report.json
│   └── form16-generation.json
├── templates/
│   ├── payslip-template.html
│   ├── form16-template.html
│   └── monthly-report-template.html
└── teams-cards/
    ├── employee-form.json
    ├── expense-form.json
    └── dashboard-card.json
```

---

## Integration Points

### n8n → MS Teams
- **Microsoft Teams Node:** `n8n-nodes-base.microsoftTeams`
- **Auth:** OAuth2 (Microsoft Entra ID app registration)
- **Permissions:** `ChannelMessage.Send`, `ChatMessage.Send`, `TeamsActivity.Send`

### n8n → Database
- **SQLite Node:** For local/embedded deployments
- **Postgres Node:** For production scaling
- **Connection:** Via connection string/credentials

### PDF Generation
- **Method 1:** HTML Template → HTTP Request to PDF service API
- **Method 2:** Code node with puppeteer/playwright
- **Storage:** Local filesystem or cloud blob storage

---

## Success Metrics

| Metric | Target |
|--------|--------|
| Payslip generation time | < 5 seconds per employee |
| Monthly report delivery | Auto-sent by 1st of month |
| Expense entry ease | Single Teams form submission |
| Form 16 availability | Within 24 hrs of FY close |
| Data accuracy | 99.9% (verified against source) |
