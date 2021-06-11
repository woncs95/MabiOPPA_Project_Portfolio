import threading
from CommandWorker import myThread
from ServerWorker import *


myThread()
run_bot()
run_server()
print(threading.active_count())
print(threading.enumerate())