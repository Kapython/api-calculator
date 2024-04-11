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


@pytest.mark.asyncio
async def test_add(
    app: FastAPI,
    async_client: AsyncClient,
) -> None:
    async with async_client as client:
        data = {"source": "1+1"}
        response = await client.get(app.url_path_for("calculate"), params=data)
        assert response.status_code == 200
        assert response.json()
        result = response.json()
        assert result["expression"] == data["source"]
        assert result["result"] == 2


@pytest.mark.asyncio
async def test_subtraction(
    app: FastAPI,
    async_client: AsyncClient,
) -> None:
    async with async_client as client:
        data = {"source": "10-20"}
        response = await client.get(app.url_path_for("calculate"), params=data)
        assert response.status_code == 200
        assert response.json()
        result = response.json()
        assert result["expression"] == data["source"]
        assert result["result"] == -10


@pytest.mark.asyncio
async def test_division(
    app: FastAPI,
    async_client: AsyncClient,
) -> None:
    async with async_client as client:
        data = {"source": "1000/4"}
        response = await client.get(app.url_path_for("calculate"), params=data)
        assert response.status_code == 200
        assert response.json()
        result = response.json()
        assert result["expression"] == data["source"]
        assert result["result"] == 250


@pytest.mark.asyncio
async def test_multiplication(
    app: FastAPI,
    async_client: AsyncClient,
) -> None:
    async with async_client as client:
        data = {"source": "4*20"}
        response = await client.get(app.url_path_for("calculate"), params=data)
        assert response.status_code == 200
        assert response.json()
        result = response.json()
        assert result["expression"] == data["source"]
        assert result["result"] == 80
