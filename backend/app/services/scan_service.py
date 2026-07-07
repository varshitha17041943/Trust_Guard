from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.scan import URLScanRequest, QRScanRequest
from app.models.scan import Scan
from app.models.details import ThreatResult, Recommendation, OfficialWebsite
from app.agents.core.state import SharedContext
from app.agents.core.orchestrator import DAGOrchestrator
from app.agents.impl.agents import (
    InputValidationAgent, QRProcessingAgent, SecurityAnalysisAgent, 
    BrandVerificationAgent, RiskAssessmentAgent, ExplanationAgent, 
    RecommendationAgent, OfficialWebsiteVerificationAgent, ReportGenerationAgent
)

# Configure DAG Orchestrator
orchestrator = DAGOrchestrator({
    "Phase_1_Ingestion": [InputValidationAgent(), QRProcessingAgent()],
    "Phase_2_Analysis": [SecurityAnalysisAgent(), BrandVerificationAgent()],
    "Phase_3_Assessment": [RiskAssessmentAgent(), OfficialWebsiteVerificationAgent()],
    "Phase_4_Synthesis": [ExplanationAgent(), RecommendationAgent()],
    "Phase_5_Reporting": [ReportGenerationAgent()]
})

class ScanService:
    @staticmethod
    async def _execute_workflow(db: AsyncSession, target: str, scan_type: str, user_id: int | None = None):
        # 1. Create Initial State
        context = SharedContext(original_target=target, scan_type=scan_type)
        
        # 2. Run ADK Multi-Agent Orchestrator
        final_state = await orchestrator.run(context)
        
        # 3. Map to Relational Database Models
        scan = Scan(
            target=final_state.original_target,
            scan_type=scan_type,
            status="completed",
            risk_score=final_state.risk_score,
            risk_level=final_state.risk_level,
            confidence_score=final_state.confidence,
            user_id=user_id
        )
        db.add(scan)
        await db.flush() # Get scan.id
        
        # Add relations
        for flag in final_state.threat_intel_flags:
            db.add(ThreatResult(scan_id=scan.id, agent_name="ThreatIntelAgent", status="Fail", description=flag, passed=False))
            
        for rec in final_state.recommendations:
            db.add(Recommendation(scan_id=scan.id, text=rec, priority="High"))
            
        if final_state.impersonated_brand:
            db.add(OfficialWebsite(scan_id=scan.id, brand_name=final_state.impersonated_brand, official_url=final_state.official_url or ""))
            
        await db.commit()
        
        # 4. Return formatted JSON response
        return {
            "id": scan.id,
            "target": scan.target,
            "scan_type": scan.scan_type,
            "status": scan.status,
            "risk_score": scan.risk_score,
            "risk_level": scan.risk_level,
            "created_at": str(scan.created_at)
        }

    @staticmethod
    async def process_url_scan(db: AsyncSession, scan_req: URLScanRequest):
        return await ScanService._execute_workflow(db, str(scan_req.target_url), "URL")

    @staticmethod
    async def process_qr_scan(db: AsyncSession, scan_req: QRScanRequest):
        return await ScanService._execute_workflow(db, scan_req.qr_data, "QR")
