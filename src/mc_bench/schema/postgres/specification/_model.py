"""
A reference table of model names, such as "NousResearch/Hermes-3-Llama-3.1-8B" (from hugging face) or "claude-3-5-sonnet-20240620".

While some systems may have specific variants, we will mediate any of these differences by recording timestamps and other
metadata for how the model was run, accessed, or called.

Unless it becomes necessary, we will generally consider this model name the system under test.
"""

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, func
from .._metadata import metadata


model = Table(
    "model",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "created", TIMESTAMP(timezone=False), server_default=func.now(), nullable=True
    ),
    Column("name", String, unique=True, nullable=False),
    comment=__doc__.strip(),
    schema="specification",
)
