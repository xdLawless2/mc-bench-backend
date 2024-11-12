from mc_bench.config import CeleryConfig

from celery import Celery

config = CeleryConfig()

app = Celery(
    broker=config.broker_url,
    backend=config.broker_url,
)
