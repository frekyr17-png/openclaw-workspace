"""
TaxReady Backend API
Indian tax document aggregator - PDF extraction and organization
"""
from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
import uuid
import json
from datetime import datetime
import shutil

# API Cost Optimization imports (COMMENTED - will enable after modules tested)
# from api_middleware import APICostMiddleware, log_external_api_call
# from cache_layer import cache_result
# from ollama_integration import extract_with_ollama, check_ollama_available

app = FastAPI(
    title="TaxReady API",
    description="Indian tax document aggregator - Upload PDFs, extract data, generate CA reports",
    version="0.1.0"
)

# CORS for frontend
# DISABLED: Need to install modules in container first
# app.add_middleware(APICostMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DISABLED: Need Ollama wired in container
# Check Ollama availability on startup
# ollama_available = check_ollama_available()
# if ollama_available:
#     print("✓ Ollama is available - will use local AI for extraction")
# else:
#     print("⚠ Ollama not available - falling back to regex extraction")


# Data directories
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
UPLOADS_DIR = os.path.join(DATA_DIR, "uploads")
EXTRACTS_DIR = os.path.join(DATA_DIR, "extracts")

os.makedirs(UPLOADS_DIR, exist_ok=True)
os.makedirs(EXTRACTS_DIR, exist_ok=True)


# Models
class DocumentInfo(BaseModel):
    id: str
    filename: str
    doc_type: str
    status: str  # pending, processing, done, error
    created_at: str
    file_path: str


class ExtractedData(BaseModel):
    doc_type: str
    income: List[Dict[str, Any]] = []
    tds: List[Dict[str, Any]] = []
    deductions: List[Dict[str, Any]] = []
    investments: List[Dict[str, Any]] = []
    transactions: List[Dict[str, Any]] = []
    summary: Dict[str, Any] = {}
    raw_text: Optional[str] = None


class DashboardSummary(BaseModel):
    total_income: float
    total_tds: float
    total_deductions: float
    documents_processed: int
    documents_pending: int
    missing_docs: List[str]


# In-memory storage (TODO: replace with SQLite/PostgreSQL)
documents_db: Dict[str, DocumentInfo] = {}
extracts_db: Dict[str, ExtractedData] = {}


# Document classifier
def classify_document(text: str) -> str:
    """Classify document type based on content"""
    text_lower = text.lower()
    
    if "form 16" in text_lower or "salary" in text_lower and "tds" in text_lower:
        return "form16"
    elif "annual information statement" in text_lower or "ais" in text_lower:
        return "ais"
    elif "form 26as" in text_lower or "tax deducted at source" in text_lower:
        return "form26as"
    elif "consolidated account statement" in text_lower or "mutual fund" in text_lower:
        return "mf_statement"
    elif "capital gains" in text_lower or "p&l" in text_lower:
        return "capital_gains"
    elif "bank" in text_lower and ("statement" in text_lower or "account" in text_lower):
        return "bank_statement"
    elif "credit card" in text_lower:
        return "credit_card"
    else:
        return "unknown"


# Extractors (placeholder - will expand each in separate files)
def extract_form16(text: str) -> ExtractedData:
    """Extract data from Form 16"""
    # TODO: Use Ollama for intelligent extraction
    import re
    
    data = ExtractedData(doc_type="form16")
    
    # Simple regex patterns (will be enhanced with AI)
    patterns = {
        "gross_salary": r"gross salary[:\s]*₹?\s*([\d,]+)",
        "tds_deducted": r"tax deducted[:\s]*₹?\s*([\d,]+)",
        "pan": r"PAN[:\s]*([A-Z]{5}\d{4}[A-Z])",
        "employer_name": r"employer[:\s]*([A-Za-z\s]+)",
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            data.summary[key] = match.group(1).strip()
    
    data.raw_text = text[:5000]  # Store partial text
    return data


def extract_bank_statement(text: str) -> ExtractedData:
    """Extract data from bank statement"""
    data = ExtractedData(doc_type="bank_statement")
    # TODO: Parse tables, find interest income
    data.raw_text = text[:5000]
    return data


def extract_mf_statement(text: str) -> ExtractedData:
    """Extract data from Mutual Fund CAS"""
    data = ExtractedData(doc_type="mf_statement")
    # TODO: Parse fund details, calculate gains
    data.raw_text = text[:5000]
    return data


# PDF Processing
async def process_pdf(file_path: str, doc_id: str):
    """Process uploaded PDF and extract data"""
    import fitz  # PyMuPDF
    
    try:
        # Update status
        documents_db[doc_id].status = "processing"
        
        # Extract text
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        
        # Classify document
        doc_type = classify_document(text)
        documents_db[doc_id].doc_type = doc_type
        
        # Extract based on type
        if doc_type == "form16":
            extracted = extract_form16(text)
        elif doc_type == "bank_statement":
            extracted = extract_bank_statement(text)
        elif doc_type == "mf_statement":
            extracted = extract_mf_statement(text)
        else:
            extracted = ExtractedData(doc_type=doc_type, raw_text=text[:5000])
        
        # Store extract
        extracts_db[doc_id] = extracted
        documents_db[doc_id].status = "done"
        
        # Save to file
        with open(os.path.join(EXTRACTS_DIR, f"{doc_id}.json"), "w") as f:
            json.dump(extracted.model_dump(), f, indent=2, default=str)
            
    except Exception as e:
        documents_db[doc_id].status = "error"
        print(f"Error processing {doc_id}: {e}")


# API Endpoints
@app.get("/")
async def root():
    return {"message": "TaxReady API v0.1", "status": "running"}


@app.post("/upload", response_model=DocumentInfo)
async def upload_document(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    """Upload a PDF document for processing"""
    
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files supported")
    
    doc_id = str(uuid.uuid4())[:8]
    file_path = os.path.join(UPLOADS_DIR, f"{doc_id}_{file.filename}")
    
    # Save file
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    # Create document record
    doc_info = DocumentInfo(
        id=doc_id,
        filename=file.filename,
        doc_type="unknown",
        status="pending",
        created_at=datetime.now().isoformat(),
        file_path=file_path
    )
    documents_db[doc_id] = doc_info
    
    # Process in background
    background_tasks.add_task(process_pdf, file_path, doc_id)
    
    return doc_info


@app.get("/documents", response_model=List[DocumentInfo])
async def list_documents():
    """List all uploaded documents"""
    return list(documents_db.values())


@app.get("/documents/{doc_id}", response_model=DocumentInfo)
async def get_document(doc_id: str):
    """Get document info"""
    if doc_id not in documents_db:
        raise HTTPException(status_code=404, detail="Document not found")
    return documents_db[doc_id]


@app.get("/extracts/{doc_id}", response_model=ExtractedData)
async def get_extract(doc_id: str):
    """Get extracted data for a document"""
    if doc_id not in extracts_db:
        raise HTTPException(status_code=404, detail="Extract not found")
    return extracts_db[doc_id]


@app.get("/dashboard", response_model=DashboardSummary)
async def get_dashboard():
    """Get dashboard summary"""
    total_income = 0.0
    total_tds = 0.0
    total_deductions = 0.0
    
    # Aggregate from extracts
    for extract in extracts_db.values():
        summary = extract.summary
        # TODO: Parse monetary values properly
        pass
    
    # Determine missing docs
    doc_types = [d.doc_type for d in documents_db.values()]
    required = ["form16", "bank_statement", "mf_statement", "ais"]
    missing = [d for d in required if d not in doc_types]
    
    return DashboardSummary(
        total_income=total_income,
        total_tds=total_tds,
        total_deductions=total_deductions,
        documents_processed=len([d for d in documents_db.values() if d.status == "done"]),
        documents_pending=len([d for d in documents_db.values() if d.status in ["pending", "processing"]]),
        missing_docs=missing
    )


@app.get("/health")
async def health():
    return {"status": "healthy", "documents": len(documents_db)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)