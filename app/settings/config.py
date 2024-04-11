from functools import lru_cache

from .app import AppSettings


@lru_cache
def get_app_settings() -> AppSettings:
    """The function prepares settings"""

    return AppSettings()
