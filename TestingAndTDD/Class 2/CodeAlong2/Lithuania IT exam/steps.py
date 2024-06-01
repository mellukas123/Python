# Function to calculate distance covered in kilometers
def calculate_distance(steps_cm, step_length_cm):
    total_cm = sum(steps_cm)  # Total steps in centimeters
    distance_km = (total_cm * step_length_cm) / 100000.0  # Convert steps to kilometers
    return distance_km

# Read data from input file
with open('u1.txt', 'r') as file:
    lines = file.readlines()

# Parse data and calculate distances
grades_data = {}
for line in lines[1:]:
    elements = line.strip().split()
    if len(elements) >= 8 and elements[0].isdigit():  # Check if there are at least 8 elements in the line and the first element is numeric
        grade, step_length_cm, *steps = map(int, elements)
        if 0 not in steps:  # Check if there's at least one non-zero step count
            distance = calculate_distance(steps, step_length_cm)
            if grade in grades_data:
                grades_data[grade]['participants'] += 1
                grades_data[grade]['distance'] += distance
            else:
                grades_data[grade] = {'participants': 1, 'distance': distance}

# Write results to output file
with open('u1result.txt', 'w') as output_file:
    for grade, data in sorted(grades_data.items()):
        output_file.write(f"{grade} {data['participants']} {data['distance']:.2f}\n")
