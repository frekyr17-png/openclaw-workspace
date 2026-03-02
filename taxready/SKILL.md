---
name: taxready
description: "Indian tax document aggregator platform. Upload PDFs (Form 16, bank statements, MF statements, credit cards) → AI extracts and organizes data → CA-ready export. Use when: building, debugging, deploying, or improving the TaxReady platform."
---

# TaxReady — Skill Guide

Indian tax document aggregator. Users upload financial PDFs → AI extracts → organized dashboard → CA-ready export.

## Architecture

```
┌─────────────────────────────────────────────────┐
│                    Frontend                       │
│              Next.js 14 + Tailwind                │
│         shadcn/ui + App Router                    │
│                                                   │
│  Landing → Auth → Upload → Dashboard → Export     │
└──────────────────────┬────────────────────────────┘
                       │ REST API
┌──────────────────────▼────────────────────────────┐
│                 Backend (FastAPI)                   │
│                                                    │
│  /upload    → receive PDFs, classify               │
│  /extract   → parse + AI extract structured data   │
│  /dashboard → return organized financial summary   │
│  /export    → generate CA-ready PDF/Excel          │
│                                                    │
│  Extractors: Form16, BankStatement, MFStatement,   │
│              CreditCard, AIS, 26AS                 │
│                                                    │
│  AI Engine: Ollama (qwen2.5 / mistral)             │
│  PDF Parse: pdfplumber + tabula-py + pytesseract   │
└──────────────────────┬────────────────────────────┘
                       │
┌──────────────────────▼────────────────────────────┐
│                  Storage                           │
│  SQLite (MVP) → PostgreSQL (scale)                 │
│  File storage: local → S3/MinIO (scale)            │
└───────────────────────────────────────────────────┘
```

## Tech Stack

| Layer | Tech | Why |
|-------|------|-----|
| Frontend | Next.js 14 + Tailwind + shadcn/ui | Fast, modern, SEO for landing page |
| Backend | Python FastAPI | Best PDF/AI ecosystem, async |
| PDF Parsing | pdfplumber + tabula-py + PyMuPDF | Covers text PDFs + tables |
| OCR | pytesseract + Pillow | For scanned documents |
| AI Extraction | Ollama (qwen2.5 local) | Free, private, no API costs |
| Database | SQLite → PostgreSQL | Simple MVP, scalable later |
| Auth | JWT (simple) → NextAuth (scale) | No dependencies for MVP |
| Deploy | Docker Compose | One command, reproducible |

## Document Types Supported

| Document | Source | Key Data Extracted |
|----------|--------|--------------------|
| Form 16 | Employer | Salary, TDS, deductions (80C/80D etc), employer details |
| Bank Statement | Bank | Interest income, transactions, balance |
| MF Statement (CAS) | CAMS/KFintech | Fund names, NAV, gains, STCG/LTCG |
| Credit Card Statement | Bank | Spends summary (for audit trail) |
| AIS | Income Tax Portal | All reported income, TDS, SFTs |
| Form 26AS | Income Tax Portal | TDS credits, advance tax |
| Capital Gains | Broker (Zerodha etc) | P&L, STCG, LTCG, STT paid |

## Key Directories

```
taxready/
├── SKILL.md              # This file
├── README.md             # User-facing docs
├── docker-compose.yml    # Full stack deployment
├── frontend/             # Next.js app
│   ├── app/              # App router pages
│   ├── components/       # UI components
│   └── lib/              # Utils, API client
├── backend/              # Python FastAPI
│   ├── main.py           # API server
│   ├── extractors/       # Per-document-type extractors
│   ├── classifier.py     # AI document type detection
│   ├── ai_engine.py      # Ollama integration
│   ├── models.py         # Pydantic models
│   └── export.py         # PDF/Excel report generator
├── data/                 # User uploads (gitignored)
└── docs/                 # Competitor analysis, PRD
```

## Development

```bash
# Backend
cd taxready/backend
pip install fastapi uvicorn pdfplumber tabula-py pytesseract python-multipart openpyxl
uvicorn main:app --reload --port 8000

# Frontend
cd taxready/frontend
npm install
npm run dev  # port 3000
```

## MCP (Phase 2)
Not needed for v1. In Phase 2, MCP could enable:
- CAs connecting their accounting software to pull client data
- AI agents querying the platform for tax insights
- Integration with other financial tools

## Revenue Model
- Free: Upload + organize (up to 5 docs)
- Paid (₹299/year): Unlimited docs + CA export + reminders + multi-year
- CA Plan (₹1999/year): Bulk client management

## Competitors
See docs/competitors.md (to be updated when Rahul sends list)

## Phases
- **V1 (MVP):** Upload → Extract → Dashboard → Export
- **V2:** Email parsing, AIS auto-parse, payment integration
- **V3:** CA portal, multi-year comparison, tax optimization tips
