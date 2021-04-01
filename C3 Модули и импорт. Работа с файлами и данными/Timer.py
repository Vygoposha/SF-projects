import time
from datetime import datetime
from contextlib import contextmanager

class Timer:
    def __init__(self):
        pass

    def __enter__(self):
        self.start = datetime.utcnow()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print((datetime.utcnow()-self.start).total_seconds())


@contextmanager
def timer():
    start = datetime.utcnow()
    yield
    print((datetime.utcnow()-start).total_seconds())

with Timer():
    time.sleep(2)

with timer():
    time.sleep(2)
