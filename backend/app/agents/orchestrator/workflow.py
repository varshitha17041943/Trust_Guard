import asyncio
import uuid
from datetime import datetime
from app.agents.shared.schemas import ScanRequest, FinalReport
from app.agents.input_validation.agent import InputValidationAgent
from app.agents.qr_processing.agent import QrProcessingAgent
from app.agents.ssl_analysis.agent import SslAnalysisAgent
from app.agents.whois_analysis.agent import WhoisAnalysisAgent
from app.agents.threat_analysis.agent import ThreatAnalysisAgent
from app.agents.brand_analysis.agent import BrandAnalysisAgent
from app.agents.risk_assessment.agent import RiskAssessmentAgent
from app.agents.explanation.agent import ExplanationAgent
from app.agents.recommendation.agent import RecommendationAgent
from app.agents.official_website.agent import OfficialWebsiteAgent
from app.agents.report.agent import ReportAgent
from app.agents.input_validation.schemas import InputSchema as ValidationInput
from app.agents.qr_processing.schemas import InputSchema as QRInput
from app.agents.ssl_analysis.schemas import InputSchema as SSLInput
from app.agents.whois_analysis.schemas import InputSchema as WhoisInput
from app.agents.threat_analysis.schemas import InputSchema as ThreatInput
from app.agents.brand_analysis.schemas import InputSchema as BrandInput
from app.agents.risk_assessment.schemas import InputSchema as RiskInput
from app.agents.explanation.schemas import InputSchema as ExplInput
from app.agents.recommendation.schemas import InputSchema as RecInput
from app.agents.official_website.schemas import InputSchema as OfficialInput
from app.agents.report.schemas import InputSchema as ReportInput

class Orchestrator:
    def __init__(self):
        self.validator = InputValidationAgent()
        self.qr = QrProcessingAgent()
        self.ssl = SslAnalysisAgent()
        self.whois = WhoisAnalysisAgent()
        self.threat = ThreatAnalysisAgent()
        self.brand = BrandAnalysisAgent()
        self.risk = RiskAssessmentAgent()
        self.explainer = ExplanationAgent()
        self.recommender = RecommendationAgent()
        self.official = OfficialWebsiteAgent()
        self.reporter = ReportAgent()

    async def execute_scan(self, request: ScanRequest) -> FinalReport:
        url = request.url
        
        # 1. Validation or QR processing
        if request.scan_type == "qr":
            qr_res = await self.qr.execute(QRInput(url=url))
            url = qr_res.url if hasattr(qr_res, 'url') else url
            
        val_res = await self.validator.execute(ValidationInput(url=url))
        url = val_res.url if hasattr(val_res, 'url') else url

        # 2. Parallel Execution
        ssl_res, whois_res, threat_res, brand_res = await asyncio.gather(
            self.ssl.execute(SSLInput(url=url)),
            self.whois.execute(WhoisInput(url=url)),
            self.threat.execute(ThreatInput(url=url)),
            self.brand.execute(BrandInput(url=url))
        )

        # 3. Risk Assessment
        risk_res = await self.risk.execute(RiskInput(url=url))

        # 4. Explanation, Recommendations, Official Website
        expl_res, rec_res, off_res = await asyncio.gather(
            self.explainer.execute(ExplInput(url=url)),
            self.recommender.execute(RecInput(url=url)),
            self.official.execute(OfficialInput(url=url))
        )

        # 5. Report
        report_res = await self.reporter.execute(ReportInput(url=url))

        # Compile final
        return FinalReport(
            url=url,
            risk_score=getattr(risk_res, 'score', 50),
            risk_level=getattr(risk_res, 'level', 'Medium'),
            confidence=95,
            quick_decisions={"trust": "Maybe", "login": "No", "payment": "No", "share_information": "No"},
            findings=[{"title": "Analysis Complete", "description": "Processed successfully"}],
            recommendations=["Verify before proceeding"],
            official_website=getattr(off_res, 'url', 'N/A'),
            report_id=str(uuid.uuid4()),
            generated_at=datetime.utcnow().isoformat()
        )
