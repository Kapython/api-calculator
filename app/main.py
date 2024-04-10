import uvicorn
from fastapi import FastAPI

from app.api.api_v1.api import v1_router
from app.settings.app import AppSettings


def get_application() -> FastAPI:
    settings = AppSettings()

    application = FastAPI(**settings.fastapi_kwargs)

    application.include_router(v1_router, prefix=settings.prefix)

    return application


app = get_application()


@app.get("/healthcheck")
async def healthcheck():
    return {"message": "I'm healthy"}


if __name__ == '__main__':

    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="debug")
