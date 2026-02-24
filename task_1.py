from queue import Queue
import random
import time

queue = Queue()

def generate_request():
    request = random.randint(1, 100)
    print(f"Request added: {request}")
    queue.put(request)

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Request is processing: {request}")
        print("")
    else:
        print(f"Queue is empty.")

try:
    while True:
        generate_request()
        time.sleep(2)
        process_request()
        time.sleep(2)

except KeyboardInterrupt:
    print("Exit") # press "ctrl + c" or "control + c" to exit.