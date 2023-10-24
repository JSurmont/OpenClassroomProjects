import pytest

from app import create_app
from utilities import clear_all


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    clear_all()
    with app.test_client() as client:
        yield client
