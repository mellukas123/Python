import random

def random_sample(collection, sample_size):
    # Convert the collection to a list to support random sampling
    collection_list = list(collection)
    # Generate a random sample of items from the collection
    sample = random.sample(collection_list, min(sample_size, len(collection_list)))
    # Yield each item from the sample
    for item in sample:
        yield item

# Example usage:
my_collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_size = 5

# Generate a random sample of items from the collection
for item in random_sample(my_collection, sample_size):
    print(item)
