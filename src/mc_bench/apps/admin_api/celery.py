from mc_bench.config import CeleryConfig

from celery import Celery

config = CeleryConfig()

celery = Celery(broker=config.broker_url, backend=config.broker_url)


def send_task(name, *args, **kwargs):
    kwargs.setdefault("queue", "admin")
    return celery.send_task(name, *args, **kwargs)
