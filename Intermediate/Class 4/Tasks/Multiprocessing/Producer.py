# Producer-Consumer Problem: Implement a simple producer-consumer scenario using multithreading.
# Have one thread produce items (e.g., numbers) and put them into a shared queue,
# while another thread consumes these items from the queue.

import threading
import queue
import time
import random

SENTINEL = object()  # Sentinel value to signal the end of production


class Producer(threading.Thread):
    def __init__(self, queue):
        super(Producer, self).__init__()
        self.queue = queue

    def run(self):
        for i in range(10):  # Producing 10 items
            item = random.randint(1, 100)  # Generate a random number
            self.queue.put(item)
            print(f"Produced {item}")
            time.sleep(random.random())  # Simulate some processing time

        # Signal the end of production by putting the sentinel value into the queue
        self.queue.put(SENTINEL)


class Consumer(threading.Thread):
    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            if item is SENTINEL:  # Check if it's the sentinel value
                print("Consumer received sentinel. Exiting.")
                break  # Exit the loop
            print(f"Consumed {item}")
            self.queue.task_done()
            time.sleep(random.random())  # Simulate some processing time


def main():
    q = queue.Queue()  # Shared queue
    producer = Producer(q)
    consumer = Consumer(q)

    producer.start()
    consumer.start()

    # Wait for the producer to finish
    producer.join()

    # Wait for the consumer to finish
    q.join()

    # Wait for the consumer thread to finish
    consumer.join()


if __name__ == "__main__":
    main()
