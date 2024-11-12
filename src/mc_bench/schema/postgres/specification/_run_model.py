""" """

from sqlalchemy import (
    Column,
    Table,
    Integer,
    ForeignKey,
    UniqueConstraint,
    TIMESTAMP,
    func,
)
from .._metadata import metadata


run_model = Table(
    "run_model",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "created", TIMESTAMP(timezone=False), server_default=func.now(), nullable=True
    ),
    Column("run_id", Integer, ForeignKey("specification.run.id")),
    Column("model_id", Integer, ForeignKey("specification.model.id")),
    Column("state_id", Integer, ForeignKey("specification.run_model_state.id")),
    UniqueConstraint("run_id", "model_id"),
    comment=__doc__.strip(),
    schema="specification",
)
