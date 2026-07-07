from app.workflows.retry_policy import with_retry
from app.workflows.timeout_policy import with_timeout
from app.workflows.progress_tracker import ProgressTracker
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

class WorkflowNodes:
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

    async def execute_node(self, node_name: str, scan_id: int, agent_func, input_data, progress_pct: int):
        await ProgressTracker.update(scan_id, f"Running {node_name}", progress_pct)
        try:
            # Wrap with timeout and retry
            result = await with_retry(with_timeout, agent_func, input_data)
            await ProgressTracker.update(scan_id, f"Completed {node_name}", progress_pct + 2, output_key=node_name, output_data=dict(result))
            return result
        except Exception as e:
            await ProgressTracker.update(scan_id, f"Failed {node_name}", progress_pct, error=str(e))
            return None # Graceful partial failure

nodes = WorkflowNodes()
