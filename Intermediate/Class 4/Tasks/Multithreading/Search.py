# Parallel Search: Write a script that performs a parallel search on a large dataset using multiprocessing.
# Divide the dataset into smaller chunks and search for a target value in each chunk simultaneously.

import os
import multiprocessing
from functools import partial


def search_chunk(chunk, target):
    for index, value in enumerate(chunk):
        if value == target:
            return index
    return -1  # Return -1 if target is not found in the chunk


def parallel_search(data, target, chunk_size=100):
    # Split the data into chunks
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Create a pool of processes
    pool = multiprocessing.Pool()

    # Map the search_chunk function to each chunk in parallel
    results = pool.map(partial(search_chunk, target=target), chunks)

    # Close the pool of processes
    pool.close()
    # Wait for all processes in the pool to finish
    pool.join()

    # Check results to find the index of the target in the dataset
    for i, result in enumerate(results):
        if result != -1:
            return i * chunk_size + result  # Return the index of the target in the dataset
    return -1  # Return -1 if target is not found in the dataset


def main():
    # Example dataset
    dataset = list(range(1000000))
    target = 876543

    # Perform parallel search
    index = parallel_search(dataset, target)

    if index != -1:
        print(f"Target {target} found at index {index}")
    else:
        print(f"Target {target} not found in the dataset")


if __name__ == "__main__":
    main()
