from app.workflows.state import WorkflowState
from typing import Dict
import asyncio
import json

# In-memory store for prototype
_progress_store: Dict[int, WorkflowState] = {}
_progress_queues: Dict[int, asyncio.Queue] = {}

class ProgressTracker:
    @staticmethod
    def init_scan(scan_id: int, url: str, scan_type: str):
        state = WorkflowState(scan_id=scan_id, url=url, scan_type=scan_type)
        _progress_store[scan_id] = state
        _progress_queues[scan_id] = asyncio.Queue()
        return state

    @staticmethod
    async def update(scan_id: int, stage: str, percentage: int, output_key: str = None, output_data: dict = None, error: str = None):
        if scan_id not in _progress_store: return
        state = _progress_store[scan_id]
        
        state.current_stage = stage
        state.progress_percentage = percentage
        if stage not in state.completed_stages:
            state.completed_stages.append(stage)
            
        if output_key and output_data:
            state.agent_outputs[output_key] = output_data
            
        if error:
            state.errors.append(error)
            
        if scan_id in _progress_queues:
            event_data = {
                "stage": stage,
                "percentage": percentage,
                "estimated_time": state.estimated_time_remaining
            }
            await _progress_queues[scan_id].put(json.dumps(event_data))

    @staticmethod
    def get_state(scan_id: int):
        return _progress_store.get(scan_id)
        
    @staticmethod
    def get_queue(scan_id: int):
        if scan_id not in _progress_queues:
            _progress_queues[scan_id] = asyncio.Queue()
        return _progress_queues[scan_id]
