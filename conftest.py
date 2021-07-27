import logging
import pytest
from api.client import Client

logger = logging.getLogger("OCS")


@pytest.fixture(scope="session")
def client(request):
    url = request.config.getoption("--url")
    client = Client(url)
    yield client


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="http://localhost:5000/",
        help="enter base_url",
    )


