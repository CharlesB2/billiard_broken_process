import time

from celerytest.celery import app

@app.task(bind=True)
def long_running_task(self, seconds):
    print(f"Hello! Request id: {self.request.id}")
    time.sleep(seconds)
    return self.request.id

@app.task()
def print_error():
    print("FAILED")
