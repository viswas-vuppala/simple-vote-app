import pytest
from starlette.testclient import TestClient

@pytest.fixture
def client():
    from ddd_votes.main import app

    return TestClient(app)