""" """

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, func
from .._metadata import metadata


metric = Table(
    "metric",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "created", TIMESTAMP(timezone=False), server_default=func.now(), nullable=True
    ),
    Column("name", String(), unique=True, nullable=False),
    Column("description", String(), nullable=False),
    schema="scoring",
)
