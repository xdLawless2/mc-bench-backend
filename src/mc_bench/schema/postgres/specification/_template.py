""" """

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, func
from .._metadata import metadata


template = Table(
    "template",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "created", TIMESTAMP(timezone=False), server_default=func.now(), nullable=True
    ),
    Column("name", String, unique=True, nullable=False),
    Column("contents", String, nullable=False),
    comment=__doc__.strip(),
    schema="specification",
)
