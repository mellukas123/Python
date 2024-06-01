# Define the Entry class
class Entry:
    # Constructor method to initialize an entry with given attributes
    def __init__(self, id, name='', age='', city='', potato_count=''):
        self.id = id                 # Unique identifier for the entry
        self.name = name             # Name of the participant
        self.age = age               # Age of the participant
        self.city = city             # City of the participant
        self.potato_count = potato_count  # Number of potatoes destroyed by the participant

    # Method to format entry as a string for writing to file
    def form_entry(self):
        return f"{self.id},{self.age},{self.city},{self.potato_count}\n"

    # Method to prompt user for input and populate entry attributes
    def get_user_data(self):
        print("Provide the following information please: ")
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.city = input("City: ")
        self.potato_count = input("Potato Count: ")

    # Method to print announcement about the participant
    def announcement(self):
        print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city},"
              f" destroyed {self.potato_count} potatoes yesterday.")


print("Hello to the great annual Potato eating competition")

id_counter = 0   # Initialize ID counter
entries = []     # List to store entries

# Open file for reading and writing
with open("entries.txt", "r+") as f:
    headers = f.readline()  # Read the first line (headers)
    if headers == "":       # If the file is empty, write headers
        f.write("id,name,age,city,potato_count\n")
    else:                   # If file is not empty, read existing entries
        records = f.readlines()
        for record in records:
            # Split each line into fields and create Entry objects
            line = record.strip().split(",")
            entries.append(Entry(line[0], line[1], line[2], line[3], line[4]))
            id_counter = int(line[0])  # Update ID counter with last ID
last_id = id_counter    # Store last ID for comparison

# Main loop for user interaction
while True:
    user_action = input("a - Add entry\n"
                        "v - View the entries\n"
                        "x - Exit and Save\n"
                        ": ")
    if user_action.lower() == "a":
        id_counter += 1
        entry = Entry(id_counter)  # Create new entry with incremented ID
        entry.get_user_data()      # Prompt user for input to populate entry
        entries.append(entry)      # Add entry to list
    elif user_action.lower() == "v":
        for entry in entries:
            entry.announcement()   # Display announcement for each entry
    elif user_action.lower() == "x":
        break   # Exit loop and continue to save entries

# Open file for appending and save new entries
with open("entries.txt", "a") as f:
    f.write(f"id, name, age, city, potato_count\n")  # Write headers
    for entry in entries:
        # If the entry ID is greater than the last ID in the file, write the entry
        if int(entry.id) > last_id:
            f.write(entry.form_entry())

print("Saved")  # Inform user that entries are saved