import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse

from app.api.api_v1.api import v1_router
from app.settings.app import AppSettings
from app.settings.config import get_app_settings


def get_application() -> FastAPI:
    settings = get_app_settings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.include_router(v1_router, prefix=settings.prefix)

    return application


app = get_application()


@app.get("/")
async def get_index(
    settings: AppSettings = Depends(get_app_settings)
):
    return FileResponse(settings.base_dir / "static/index.html")


@app.get("/healthcheck")
async def healthcheck():
    settings = get_app_settings()
    return {"message": "I'm healthy"}


if __name__ == '__main__':

    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="debug")
