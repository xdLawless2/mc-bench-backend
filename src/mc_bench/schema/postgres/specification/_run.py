""" """

from sqlalchemy import Table, Column, Integer, TIMESTAMP, func

from .._metadata import metadata


run = Table(
    "run",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "created", TIMESTAMP(timezone=False), server_default=func.now(), nullable=True
    ),
    comment=__doc__.strip(),
    schema="specification",
)
