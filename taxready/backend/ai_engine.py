"""
AI Extraction Engine using Ollama (local, free)
Intelligent extraction of financial data from tax documents
"""
import requests
import json
from typing import Dict, Any, Optional

OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "qwen2.5:latest"


def ask_ollama(prompt: str, model: str = DEFAULT_MODEL, max_tokens: int = 2000) -> str:
    """Send prompt to local Ollama instance"""
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": max_tokens,
                    "temperature": 0.1  # Low temp for extraction tasks
                }
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        print(f"Ollama error: {e}")
        return ""


def extract_with_ai(text: str, doc_type: str) -> Dict[str, Any]:
    """Use AI to extract structured data from document text"""
    
    prompts = {
        "form16": f"""Extract information from this Form 16 (Indian salary tax document).
Return ONLY valid JSON with these fields (use null if not found):
{{
    "pan": "taxpayer PAN number",
    "employer_pan": "employer PAN", 
    "employer_name": "employer name",
    "assessment_year": "AY 2024-25 format",
    "gross_salary": number,
    "taxable_salary": number,
    "tds_deducted": number,
    "professional_tax": number,
    "hra_exemption": number,
    "deductions_80c": number,
    "deductions_80d": number,
    "other_deductions": number,
    "total_tax": number
}}

Document text:
{text[:6000]}""",

        "bank_statement": f"""Extract income and interest data from this bank statement.
Return ONLY valid JSON with these fields:
{{
    "bank_name": "bank name",
    "account_number": "masked account number",
    "period": "statement period",
    "opening_balance": number,
    "closing_balance": number,
    "total_credits": number,
    "total_debits": number,
    "interest_credited": number,
    "transactions": [
        {{"date": "", "description": "", "amount": number, "type": "credit/debit"}}
    ]
}}

Document text:
{text[:6000]}""",

        "mf_statement": f"""Extract mutual fund investments from this CAS (Consolidated Account Statement).
Return ONLY valid JSON:
{{
    "investor_name": "name",
    "investor_pan": "PAN",
    "statement_period": "period",
    "funds": [
        {{
            "fund_name": "",
            "folio_number": "",
            "units": number,
            "nav": number,
            "current_value": number,
            "cost_value": number,
            "gain_loss": number
        }}
    ],
    "total_value": number,
    "total_investment": number,
    "total_gain_loss": number
}}

Document text:
{text[:6000]}""",

        "ais": f"""Extract financial information from this Annual Information Statement (AIS).
Return ONLY valid JSON:
{{
    "taxpayer_name": "",
    "pan": "",
    "assessment_year": "",
    "salary_income": number,
    "interest_income": number,
    "dividend_income": number,
    "mutual_fund_transactions": [],
    "property_transactions": [],
    "tds_entries": [
        {{"deductor": "", "tds_amount": number, "section": ""}}
    ]
}}

Document text:
{text[:6000]}""",

        "default": f"""Extract financial and tax-related information from this document.
Return ONLY valid JSON with relevant fields found:
{{
    "document_type": "type of document",
    "key_data": {{}},
    "amounts_found": [],
    "dates_found": [],
    "relevant_for_tax": true/false
}}

Document text:
{text[:6000]}"""
    }
    
    prompt = prompts.get(doc_type, prompts["default"])
    response = ask_ollama(prompt)
    
    # Parse JSON from response
    try:
        # Find JSON in response
        start = response.find("{")
        end = response.rfind("}") + 1
        if start != -1 and end > start:
            json_str = response[start:end]
            return json.loads(json_str)
    except json.JSONDecodeError:
        pass
    
    # Return empty if parsing failed
    return {"error": "Could not parse AI response", "raw": response[:500]}


def classify_document_ai(text: str) -> str:
    """Use AI to classify document type"""
    prompt = f"""Classify this Indian tax document. Return ONLY one of these types:
- form16
- bank_statement  
- mf_statement
- ais
- form26as
- capital_gains
- credit_card
- other

Document preview:
{text[:1500]}

Type:"""
    
    response = ask_ollama(prompt, max_tokens=20).strip().lower()
    
    valid_types = ["form16", "bank_statement", "mf_statement", "ais", 
                   "form26as", "capital_gains", "credit_card", "other"]
    
    for t in valid_types:
        if t in response:
            return t
    return "other"


def suggest_missing_docs(current_docs: list) -> list:
    """AI-powered analysis of what documents are missing"""
    prompt = f"""A user has uploaded these document types: {current_docs}
Based on typical Indian ITR filing, suggest what documents they might be missing.
Return ONLY a JSON array of missing document types, e.g. ["form16", "ais"]

Missing:"""
    
    response = ask_ollama(prompt, max_tokens=100)
    try:
        start = response.find("[")
        end = response.rfind("]") + 1
        if start != -1 and end > start:
            return json.loads(response[start:end])
    except:
        pass
    return []


if __name__ == "__main__":
    # Test
    print("Testing AI extraction engine...")
    test_text = """
    FORM 16
    Assessment Year: 2024-25
    PAN: ABCDE1234F
    Gross Salary: Rs. 12,00,000
    TDS Deducted: Rs. 1,20,000
    """
    result = extract_with_ai(test_text, "form16")
    print(json.dumps(result, indent=2))