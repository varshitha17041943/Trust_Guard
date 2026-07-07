import pytest
from app.agents.core.state import SharedContext

@pytest.fixture
def mock_context():
    return SharedContext(original_target="https://example.com", scan_type="URL")
