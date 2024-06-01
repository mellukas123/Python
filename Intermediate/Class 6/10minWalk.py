def is_valid_walk(walk):
    # If the walk is not 10 minutes long, it's not valid
    if len(walk) != 10:
        return False

    # Initialize position
    position = {'x': 0, 'y': 0}

    # Iterate through each move and update position
    for direction in walk:
        if direction == 'n':
            position['y'] += 1
        elif direction == 's':
            position['y'] -= 1
        elif direction == 'e':
            position['x'] += 1
        elif direction == 'w':
            position['x'] -= 1

    # Check if the final position is back to the start
    return position['x'] == 0 and position['y'] == 0


# Test cases
print(is_valid_walk(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # True
print(is_valid_walk(['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e']))  # False
print(is_valid_walk(['w']))  # False
print(is_valid_walk(['n', 'n', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))  # False
