def read_data(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()  # Yield each line from the file
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def chunked_data(data_generator, chunk_size):
    chunk = []
    for record in data_generator:
        chunk.append(record)
        if len(chunk) == chunk_size:
            yield chunk
            chunk = []
    if chunk:  # Yield the remaining records if any
        yield chunk

# Example usage:
filename = "data.txt"  # Replace with the path to your data file
data_generator = read_data(filename)

# Iterate over chunks of data
for chunk in chunked_data(data_generator, chunk_size=5):
    print("Chunk:", chunk)

