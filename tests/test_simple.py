import pytest

from fastapi import FastAPI
from httpx import AsyncClient


pytest_plugins = ("pytest_asyncio",)


@pytest.mark.asyncio
async def test_health(
    app: FastAPI,
    async_client: AsyncClient,
) -> None:
    async with async_client as client:
        response = await client.get(app.url_path_for("root"))
        assert response.status_code == 200
        assert response.json()
        result = response.json()
        assert result["message"] == "I'm healthy"
