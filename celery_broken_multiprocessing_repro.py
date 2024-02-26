import os
import signal
from multiprocessing import Pipe, Process

from celerytest.celery import app


def fun(conn):
    print(f"child: {conn.closed=}, {conn.fileno()=}, {conn.readable=}, {conn.writable=}")
    conn.send(42)


def subprocess_fun():
    parent_conn, child_conn = Pipe()
    process = Process(target=fun, args=(child_conn,))
    process.start()
    timeout = 5
    process.join(timeout=timeout)
    print(f"{child_conn.closed=}, {child_conn.fileno()=}, {child_conn.readable=}, {child_conn.writable=}")
    child_conn.close()
    if process.is_alive():  # Kill the process if it's still alive
        os.kill(int(process.pid), signal.SIGKILL)
        print("process killed")
    try:
        print(f"Result: {parent_conn.recv()}")
    finally:
        parent_conn.close()


@app.task
def subprocess_fun_task():
    subprocess_fun()


if __name__ == '__main__':
    print("calling function")
    subprocess_fun()
    print("calling function as task")
    subprocess_fun_task()
    print("getting active tasks")
    app.control.inspect().active()
    print("calling function")
    subprocess_fun()
    print("calling function as task")
    subprocess_fun_task()
