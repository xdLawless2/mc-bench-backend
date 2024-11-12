""" """

from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, func
from .._metadata import metadata


sample = Table(
    "sample",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "created", TIMESTAMP(timezone=False), server_default=func.now(), nullable=True
    ),
    Column(
        "model_run_id",
        Integer,
        ForeignKey("specification.run_model.id"),
        nullable=False,
    ),
    Column("inspiration_result_text", String, nullable=True),
    Column("description_result_text", String, nullable=True),
    Column("code_result", String, nullable=True),
    comment=__doc__.strip(),
    schema="sample",
)
