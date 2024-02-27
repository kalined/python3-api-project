import decimal
from datetime import date

from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    declarative_base,
    mapped_column,
    relationship,
)

from poetry_python_api.database import SessionLocal

Base: DeclarativeBase = declarative_base()


class DBCategory(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    events: Mapped[list["DBEvent"]] = relationship(back_populates="category")


class DBEvent(Base):
    __tablename__ = "event"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_code: Mapped[str] = mapped_column(unique=True)
    date: Mapped[date]
    price: Mapped[decimal.Decimal]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    category: Mapped["DBCategory"] = relationship(back_populates=("events"))


session = SessionLocal()
results = session.execute(select(DBCategory)).scalars()
print("\n".join(f"{category.name}: {len(category.events)}" for category in results))
