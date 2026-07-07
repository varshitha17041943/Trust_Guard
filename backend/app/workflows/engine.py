from app.agents.core.state import SharedContext
from app.agents.core.orchestrator import DAGOrchestrator
from app.agents.impl.agents import (
    InputValidationAgent, QRProcessingAgent, SecurityAnalysisAgent, 
    BrandVerificationAgent, RiskAssessmentAgent, ExplanationAgent, 
    RecommendationAgent, OfficialWebsiteVerificationAgent, ReportGenerationAgent
)
import json
import asyncio
import logging

logger = logging.getLogger(__name__)

# Configure Antigravity Workflow DAG
antigravity_orchestrator = DAGOrchestrator({
    "Ingestion": [InputValidationAgent(), QRProcessingAgent()],
    "Analysis": [SecurityAnalysisAgent(), BrandVerificationAgent()],
    "Assessment": [RiskAssessmentAgent(), OfficialWebsiteVerificationAgent()],
    "Synthesis": [ExplanationAgent(), RecommendationAgent()],
    "Reporting": [ReportGenerationAgent()]
})

async def stream_workflow(target: str, scan_type: str):
    context = SharedContext(original_target=target, scan_type=scan_type)
    yield f"data: {{ \"event\": \"step_start\", \"step\": \"Initializing Antigravity Engine...\" }}\n\n"
    await asyncio.sleep(0.5)
    
    for phase, agents in antigravity_orchestrator.agents_map.items():
        yield f"data: {{ \"event\": \"step_start\", \"step\": \"Executing {phase}...\" }}\n\n"
        
        tasks = [agent.run(context.model_copy(deep=True)) for agent in agents]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for agent, result in zip(agents, results):
            if isinstance(result, Exception):
                yield f"data: {{ \"event\": \"partial_failure\", \"step\": \"{agent.name} failed\" }}\n\n"
            else:
                for key, val in result.model_dump().items():
                    if val is not None and (not isinstance(val, list) or len(val) > 0):
                        setattr(context, key, val)
                yield f"data: {{ \"event\": \"step_complete\", \"step\": \"{agent.name} Success\" }}\n\n"
                
    yield f"data: {{ \"event\": \"workflow_complete\", \"state\": {context.model_dump_json()} }}\n\n"
