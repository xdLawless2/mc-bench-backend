"""
A prompt. This will include a template id (which should be the same across every given run).
This table is append only. If we choose to use a different template we should make a new prompt row.
"""

from sqlalchemy import Table, Column, Integer, String, ForeignKey, TIMESTAMP, func
from .._metadata import metadata


prompt = Table(
    "prompt",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "created", TIMESTAMP(timezone=False), server_default=func.now(), nullable=True
    ),
    Column("name", String, unique=True, nullable=False),
    Column(
        "template_id", Integer, ForeignKey("specification.template.id"), nullable=False
    ),
    Column("build_specification", String, nullable=False),
    comment=__doc__.strip(),
    schema="specification",
)
