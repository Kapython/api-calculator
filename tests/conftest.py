import pytest

from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport


@pytest.fixture
def app() -> FastAPI:
    from app.main import get_application  # local import for testing purpose

    app = get_application()
    return app


@pytest.fixture
def async_client(app: FastAPI) -> AsyncClient:
    return AsyncClient(
        transport=ASGITransport(**{"app": app}),
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    )
