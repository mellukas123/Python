# Calculate what was the most points collected, list all the participants
# that collected that amount of points,
# order them by the user that solved the most tasks.

# Read the data from the source file
with open('coding_competition.txt', 'r') as file:
    lines = file.readlines()

# Extracting data from each line
num_participants = int(lines[0].strip())
max_time_per_task = list(map(int, lines[1].strip().split()))
max_points_per_task = list(map(int, lines[2].strip().split()))

# Initializing a dictionary to hold the total points for each participant
participant_points = {}

# Processing participant data
for line in lines[3:]:
    parts = line.strip().split()
    participant_name = ' '.join(parts[:-len(max_time_per_task)])  # Handle participant names with spaces
    task_times = list(map(int, parts[-len(max_time_per_task):]))

    # Calculate points for each task solved
    total_points = 0
    tasks_solved = 0
    for task_time, max_time, max_points in zip(task_times, max_time_per_task, max_points_per_task):
        if task_time > 0:  # Task solved
            # Calculate points based on the time taken
            points = max(0, max_points - (task_time - 1))  # Deduct 1 minute from time taken
            total_points += points
            tasks_solved += 1

    # Store the total points and tasks solved for the participant
    participant_points[participant_name] = (total_points, tasks_solved)

# Find the maximum points collected
max_points_collected = max(participant_points.values(), key=lambda x: x[0])[0]

# Filter participants who collected the maximum points
participants_with_max_points = [participant for participant, (points, _) in participant_points.items() if points == max_points_collected]

# Sort participants by the number of tasks solved
participants_with_max_points.sort(key=lambda x: participant_points[x][1], reverse=True)

# Write results to a new file
with open('results_file.txt', 'w') as output_file:
    output_file.write(f"{max_points_collected}\n")
    for participant in participants_with_max_points:
        points, tasks_solved = participant_points[participant]
        output_file.write(f"{participant} {tasks_solved} {points}\n")

print("Results have been written to results_file.txt")
