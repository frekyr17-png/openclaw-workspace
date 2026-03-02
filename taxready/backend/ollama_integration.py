"""
Ollama AI Integration for TaxReady
Replaces cloud API calls with local Ollama models
"""

import requests
import json
from typing import Dict, Any

OLLAMA_HOST = "http://localhost:11434"

def extract_with_ollama(text: str, doc_type: str) -> Dict[str, Any]:
    """
    Use local Ollama model for intelligent document extraction
    Much cheaper than cloud APIs (free after setup)
    """
    
    prompts = {
        "form16": """You are a tax document parser. Extract these fields from Form 16:
- Employer name
- Employee PAN
- Gross salary
- TDS deducted
- Section 80C deductions
- Section 80D deductions
- Any other deductions

Return ONLY valid JSON format:
{
  "employer_name": "...",
  "pan": "...",
  "gross_salary": number,
  "tds_deducted": number,
  "deductions_80c": number,
  "deductions_80d": number,
  "other_deductions": number
}

Document text:
{text}""",
        
        "bank_statement": """Extract bank interest income from this statement.
Return JSON with:
{
  "total_interest": number,
  "tcs_collected": number
}

Document:
{text}""",
        
        "mf_statement": """Extract mutual fund details:
- Total investment
- Current value
- Realized gains (STCG/LTCG)
- Unrealized gains

Return JSON format.

Document:
{text}"""
    }
    
    prompt = prompts.get(doc_type, prompts["form16"]).format(text=text[:4000])
    
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={
                "model": "qwen2.5",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        result = response.json()
        
        # Parse the response text as JSON
        try:
            extracted = json.loads(result.get("response", "{}"))
            return extracted
        except json.JSONDecodeError:
            # If not valid JSON, return raw text
            return {"raw_response": result.get("response", ""), "parsed": False}
            
    except Exception as e:
        return {"error": str(e), "parsed": False}


def check_ollama_available() -> bool:
    """Check if Ollama is running locally"""
    try:
        response = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False
