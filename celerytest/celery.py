from celery import Celery
import os

broker_url = os.environ.get("BROKER_URL", "redis://localhost:6379/0")
results_url = os.environ.get("RESULTS_URL", "")

conf = {
    "broker_url": broker_url,
    "imports": ("celerytest.tasks",),
}
if results_url:
    conf["result_backend"] = results_url

app = Celery("celery")
app.conf.update(conf)
