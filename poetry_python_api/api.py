from pathlib import Path

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI()

PROJECT_ROOT = Path(__file__).parent.parent
app.mount("/", StaticFiles(directory=PROJECT_ROOT / "static", html=True))
