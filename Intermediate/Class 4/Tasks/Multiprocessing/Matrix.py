# Producer-Consumer Problem: Implement a simple producer-consumer scenario using multithreading.
# Have one thread produce items (e.g., numbers) and put them into a shared queue,
# while another thread consumes these items from the queue.
import threading
import queue
import time
import random

class Producer(threading.Thread):
    def __init__(self, queue):
        super(Producer, self).__init__()
        self.queue = queue

    def run(self):
        while not stop_event.is_set():  # Check if the stop event is set
            item = random.randint(1, 100)  # Generate a random number
            self.queue.put(item)
            print(f"Produced {item}")
            time.sleep(random.random())  # Simulate some processing time

class Consumer(threading.Thread):
    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while not stop_event.is_set():  # Check if the stop event is set
            try:
                item = self.queue.get(timeout=1)  # Add timeout to periodically check for stop event
                print(f"Consumed {item}")
                self.queue.task_done()
                time.sleep(random.random())  # Simulate some processing time
            except queue.Empty:
                continue

def main():
    global stop_event
    stop_event = threading.Event()  # Event to signal threads to stop

    q = queue.Queue()  # Shared queue
    producer = Producer(q)
    consumer = Consumer(q)

    producer.start()
    consumer.start()

    # Let the program run for some time
    time.sleep(10)

    # Set the stop event to signal threads to stop
    stop_event.set()

    # Wait for both threads to finish
    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()
