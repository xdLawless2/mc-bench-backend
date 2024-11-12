""" """

from sqlalchemy import (
    Column,
    Table,
    Integer,
    String,
    TIMESTAMP,
    func,
)
from .._metadata import metadata

# e.g. QUEUED, RUNNNIG, DONE
run_model_state = Table(
    "run_model_state",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "created", TIMESTAMP(timezone=False), server_default=func.now(), nullable=True
    ),
    Column("slug", String, unique=True, nullable=False),
    comment=__doc__.strip(),
    schema="specification",
)
