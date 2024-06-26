from pathlib import Path
from typing import Dict, Any

from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    prefix: str = "/api/v1"
    debug: bool
    base_dir: Path = Path.cwd()

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
        }
