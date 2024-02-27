from pathlib import Path
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles

from poetry_python_api.database import SessionLocal
from poetry_python_api.models import DBEvent
from poetry_python_api.schemas import Event

app = FastAPI()


PROJECT_ROOT = Path(__file__).parent.parent


def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# Add an operation @app.get
@app.get("/event/{id}", response_model=Event)
def get_event(id: int, db: Annotated[Session, Depends(get_session)]) -> DBEvent:
    event = db.get(DBEvent, id)
    if event is None:
        raise HTTPException(status_code=404, detail=f"No product with id {id}")
    return event


# Return all events in the database
@app.get("/event", response_model=list[Event])
def get_all_events(db: Annotated[Session, Depends(get_session)]) -> list[DBEvent]:
    return db.execute(select(DBEvent)).scalars()


app.mount("/", StaticFiles(directory=PROJECT_ROOT / "static", html=True))
