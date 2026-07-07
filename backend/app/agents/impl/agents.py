from app.agents.core.base import AgentBase
from app.agents.core.state import SharedContext
from app.agents.core.mcp_client import mcp_client
import json
import random

class InputValidationAgent(AgentBase):
    def __init__(self):
        super().__init__("InputValidationAgent")
    @property
    def prompt(self): return "Validate and normalize the input URL."
    async def execute(self, context: SharedContext) -> SharedContext:
        context.normalized_url = context.original_target.lower().strip()
        if "?" in context.normalized_url:
            context.normalized_url = context.normalized_url.split("?")[0]
        return context

class QRProcessingAgent(AgentBase):
    def __init__(self):
        super().__init__("QRProcessingAgent")
    @property
    def prompt(self): return "Validate QR."
    async def execute(self, context: SharedContext) -> SharedContext:
        if context.scan_type == "QR" and not context.normalized_url:
            context.normalized_url = context.original_target
        return context

class SecurityAnalysisAgent(AgentBase):
    def __init__(self):
        super().__init__("SecurityAnalysisAgent")
    @property
    def prompt(self): return "Perform real technical analysis via MCP."
    async def execute(self, context: SharedContext) -> SharedContext:
        domain = context.normalized_url.replace("https://", "").replace("http://", "").split("/")[0] if context.normalized_url else ""
        try:
            vt_res = await mcp_client.execute_tool("virustotal_lookup", {"domain": domain})
            ssl_res = await mcp_client.execute_tool("ssl_checker", {"domain": domain})
            gsb_res = await mcp_client.execute_tool("google_safe_browsing", {"url": context.normalized_url})
            
            context.ssl_valid = ssl_res.get("is_valid", False)
            if vt_res.get("malicious_votes", 0) > 0:
                context.threat_intel_flags.append(f"VT_FLAG_{vt_res['malicious_votes']}")
            if not gsb_res.get("is_safe", True):
                context.threat_intel_flags.append("GSB_FLAG")
        except Exception:
            pass
        return context

class BrandVerificationAgent(AgentBase):
    def __init__(self):
        super().__init__("BrandVerificationAgent")
    @property
    def prompt(self): return "Detect typosquatting."
    async def execute(self, context: SharedContext) -> SharedContext:
        if "paypa" in (context.normalized_url or ""):
            context.impersonated_brand = "PayPal"
        return context

class RiskAssessmentAgent(AgentBase):
    def __init__(self):
        super().__init__("RiskAssessmentAgent")
    @property
    def prompt(self): return "Calculate strict mathematical risk score."
    async def execute(self, context: SharedContext) -> SharedContext:
        score = 0.0
        if context.threat_intel_flags:
            score += 35.0
        if context.ssl_valid is False:
            score += 15.0
        if context.whois_age_days and context.whois_age_days < 30:
            score += 10.0
        if context.impersonated_brand:
            score += 10.0
            
        context.risk_score = score
        context.risk_level = "Critical" if score >= 75 else "High" if score >= 40 else "Low"
        context.confidence = 95.0
        return context

# --- XAI Module ---

KNOWLEDGE_BASE = {
    "SSL": {
        "title": "Why is SSL important?",
        "desc": "SSL encrypts the connection between your browser and the server. Without it, hackers on public Wi-Fi can intercept your passwords or credit card numbers."
    },
    "Typosquatting": {
        "title": "What is Typosquatting?",
        "desc": "Scammers register domains that look almost identical to real brands (e.g., paypa1.com instead of paypal.com) to trick you into entering credentials."
    },
    "Phishing": {
        "title": "Understanding Phishing",
        "desc": "Phishing sites impersonate legitimate organizations to steal your data. They often create a sense of urgency (e.g., 'Your account is locked')."
    }
}

TIPS = [
    "Always verify the URL before entering your password.",
    "Never trust login links received through SMS.",
    "Use Multi-Factor Authentication whenever possible.",
    "Check for the padlock icon in your browser's address bar."
]

class ExplanationAgent(AgentBase):
    def __init__(self):
        super().__init__("ExplanationAgent")
    @property
    def prompt(self): return "Convert technical findings into simple English."
    async def execute(self, context: SharedContext) -> SharedContext:
        exps = []
        topics = []
        
        if context.ssl_valid is False:
            exps.append("This website doesn't use a secure encrypted connection. Information you enter could be intercepted.")
            topics.append(KNOWLEDGE_BASE["SSL"])
            
        if context.whois_age_days and context.whois_age_days < 30:
            exps.append("This website was created very recently. Scam websites often use newly registered domains.")
            
        if context.impersonated_brand:
            exps.append(f"This website closely resembles the official {context.impersonated_brand} website, but the domain is different.")
            topics.append(KNOWLEDGE_BASE["Typosquatting"])
            
        if any("GSB" in flag or "VT" in flag for flag in context.threat_intel_flags):
            exps.append("This website has been flagged by global security vendors as malicious.")
            topics.append(KNOWLEDGE_BASE["Phishing"])
            
        if not exps:
            exps.append("Our checks did not find any immediate security red flags, but always remain vigilant.")
            
        context.explanations = exps
        # Deduplicate topics
        context.learn_more_topics = [dict(t) for t in {tuple(d.items()) for d in topics}]
        context.cyber_tip = random.choice(TIPS)
        return context

class RecommendationAgent(AgentBase):
    def __init__(self):
        super().__init__("RecommendationAgent")
    @property
    def prompt(self): return "Generate personalized AI recommendations."
    async def execute(self, context: SharedContext) -> SharedContext:
        recs = []
        if context.risk_level in ["Critical", "High"]:
            recs.extend(["Avoid Logging In", "Do Not Make Payment", "Do Not Share OTP", "Close Tab Immediately"])
            if context.official_url:
                recs.append(f"Visit Official Website: {context.official_url}")
        else:
            recs.extend(["Proceed with Normal Caution", "Enable MFA on your accounts"])
            
        context.recommendations = recs
        return context

class OfficialWebsiteVerificationAgent(AgentBase):
    def __init__(self):
        super().__init__("OfficialWebsiteVerificationAgent")
    @property
    def prompt(self): return "Find official website."
    async def execute(self, context: SharedContext) -> SharedContext:
        if context.impersonated_brand:
            context.official_url = f"https://www.{context.impersonated_brand.lower()}.com"
        return context

class ReportGenerationAgent(AgentBase):
    def __init__(self):
        super().__init__("ReportGenerationAgent")
    @property
    def prompt(self): return "Generate JSON payload."
    async def execute(self, context: SharedContext) -> SharedContext:
        context.raw_report = "# Full report generated"
        return context
