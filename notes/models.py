from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData, ForeignKey
from datetime import datetime
from auth.models import user


metadata = MetaData()

note = Table(
    "note",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user", Integer, ForeignKey(user.c.id), nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column("content", String, nullable=False),
)
