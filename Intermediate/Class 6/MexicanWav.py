def wave(people):
    # Result list for storing waves
    result = []

    # Iterate through the string by index
    for i in range(len(people)):
        # If the current character is not a space, create a wave
        if people[i] != ' ':
            # Create a wave by uppercasing the current character
            wave_str = people[:i] + people[i].upper() + people[i + 1:]
            result.append(wave_str)

    return result


# Test cases
print(wave("hello"))  # Expected: ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
print(wave(""))  # Expected: []
print(wave(
    "two words"))  # Expected: ["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
print(wave("a       b    "))  # Expected: ["A       b    ", "a       B    "]
