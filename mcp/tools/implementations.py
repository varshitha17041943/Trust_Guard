from .base import BaseTool
from pydantic import BaseModel
from typing import List, Optional
import httpx
import os

# --- 2. SSL Checker (crt.sh real implementation) ---
class SSLInput(BaseModel):
    domain: str
class SSLOutput(BaseModel):
    is_valid: bool
    issuer: str

class SSLTool(BaseTool):
    name = "ssl_checker"
    input_schema = SSLInput
    output_schema = SSLOutput
    async def execute(self, params: SSLInput) -> SSLOutput:
        async with httpx.AsyncClient() as client:
            res = await client.get(f"https://crt.sh/?q={params.domain}&output=json")
            res.raise_for_status()
            data = res.json()
            if data:
                return SSLOutput(is_valid=True, issuer=data[0].get("issuer_name", "Unknown"))
            return SSLOutput(is_valid=False, issuer="None")
    def fallback(self, params: SSLInput) -> SSLOutput:
        return SSLOutput(is_valid=False, issuer="Fallback")

# --- 3. VirusTotal Lookup (Real implementation) ---
class VTInput(BaseModel):
    domain: str
class VTOutput(BaseModel):
    malicious_votes: int

class VirusTotalTool(BaseTool):
    name = "virustotal_lookup"
    input_schema = VTInput
    output_schema = VTOutput
    async def execute(self, params: VTInput) -> VTOutput:
        vt_key = os.getenv("VT_API_KEY")
        if not vt_key:
            raise ValueError("No API key")
        async with httpx.AsyncClient() as client:
            res = await client.get(f"https://www.virustotal.com/api/v3/domains/{params.domain}", headers={"x-apikey": vt_key})
            res.raise_for_status()
            data = res.json()
            stats = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
            return VTOutput(malicious_votes=stats.get("malicious", 0))
    def fallback(self, params: VTInput) -> VTOutput:
        return VTOutput(malicious_votes=0)

# --- 4. Google Safe Browsing ---
class GSBInput(BaseModel):
    url: str
class GSBOutput(BaseModel):
    is_safe: bool

class GoogleSafeBrowsingTool(BaseTool):
    name = "google_safe_browsing"
    input_schema = GSBInput
    output_schema = GSBOutput
    async def execute(self, params: GSBInput) -> GSBOutput:
        api_key = os.getenv("GSB_API_KEY")
        if not api_key:
            raise ValueError("No API key")
        async with httpx.AsyncClient() as client:
            payload = {"client": {"clientId": "trustguard", "clientVersion": "1.0.0"}, "threatInfo": {"threatTypes": ["MALWARE", "SOCIAL_ENGINEERING"], "platformTypes": ["ANY_PLATFORM"], "threatEntryTypes": ["URL"], "threatEntries": [{"url": params.url}]}}
            res = await client.post(f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}", json=payload)
            res.raise_for_status()
            return GSBOutput(is_safe=not bool(res.json().get("matches")))
    def fallback(self, params: GSBInput) -> GSBOutput:
        return GSBOutput(is_safe=True)

# --- 7. DNS Lookup (Cloudflare DoH) ---
class DNSInput(BaseModel):
    domain: str
class DNSOutput(BaseModel):
    records: List[str]

class DNSTool(BaseTool):
    name = "dns_lookup"
    input_schema = DNSInput
    output_schema = DNSOutput
    async def execute(self, params: DNSInput) -> DNSOutput:
        async with httpx.AsyncClient() as client:
            res = await client.get(f"https://cloudflare-dns.com/dns-query?name={params.domain}&type=A", headers={"accept": "application/dns-json"})
            res.raise_for_status()
            answers = res.json().get("Answer", [])
            return DNSOutput(records=[a["data"] for a in answers if a["type"] == 1])
    def fallback(self, params: DNSInput) -> DNSOutput:
        return DNSOutput(records=[])

# --- 10. Threat Aggregator (Redundant, RiskAssessmentAgent handles math now, but keeping for compatibility) ---
class ThreatAggregatorInput(BaseModel):
    flags: List[str]
class ThreatAggregatorOutput(BaseModel):
    risk_score: float
    level: str

class ThreatAggregatorTool(BaseTool):
    name = "threat_aggregator"
    input_schema = ThreatAggregatorInput
    output_schema = ThreatAggregatorOutput
    async def execute(self, params: ThreatAggregatorInput) -> ThreatAggregatorOutput:
        return ThreatAggregatorOutput(risk_score=0, level="Low")
    def fallback(self, params: ThreatAggregatorInput) -> ThreatAggregatorOutput:
        return ThreatAggregatorOutput(risk_score=0, level="Low")

# Keep other mock tools for structural completeness as requested earlier
# (whois_lookup, openphish_lookup, urlhaus_lookup, brand_similarity, official_website_finder, report_generator, embedding_generator)

class EmptyInput(BaseModel):
    pass
class EmptyOutput(BaseModel):
    pass

class WhoisTool(BaseTool):
    name = "whois_lookup"
    input_schema = EmptyInput
    output_schema = EmptyOutput
    async def execute(self, params): return EmptyOutput()
    def fallback(self, params): return EmptyOutput()

class OpenPhishTool(BaseTool):
    name = "openphish_lookup"
    input_schema = EmptyInput
    output_schema = EmptyOutput
    async def execute(self, params): return EmptyOutput()
    def fallback(self, params): return EmptyOutput()

class URLHausTool(BaseTool):
    name = "urlhaus_lookup"
    input_schema = EmptyInput
    output_schema = EmptyOutput
    async def execute(self, params): return EmptyOutput()
    def fallback(self, params): return EmptyOutput()

class BrandSimilarityTool(BaseTool):
    name = "brand_similarity"
    input_schema = EmptyInput
    output_schema = EmptyOutput
    async def execute(self, params): return EmptyOutput()
    def fallback(self, params): return EmptyOutput()

class OfficialWebsiteFinderTool(BaseTool):
    name = "official_website_finder"
    input_schema = EmptyInput
    output_schema = EmptyOutput
    async def execute(self, params): return EmptyOutput()
    def fallback(self, params): return EmptyOutput()

class ReportGeneratorTool(BaseTool):
    name = "report_generator"
    input_schema = EmptyInput
    output_schema = EmptyOutput
    async def execute(self, params): return EmptyOutput()
    def fallback(self, params): return EmptyOutput()

class EmbeddingGeneratorTool(BaseTool):
    name = "embedding_generator"
    input_schema = EmptyInput
    output_schema = EmptyOutput
    async def execute(self, params): return EmptyOutput()
    def fallback(self, params): return EmptyOutput()
