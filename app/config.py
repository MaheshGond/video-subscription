import os
from pathlib import Path
from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    base_dir: Path = Path(__file__).resolve().parent
    templates_dir: Path = Path(__file__).resolve().parent / "templates"

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()
