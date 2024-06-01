#The first century spans from the year 1 up to and including the year 100,
# the second century - from the year 101 up to and including the year 200,
# etc. Task Given a year, print the century it is in.
# The year would be passed by user input

# Input year from the user
year = int(input("Enter the year: "))

# Calculate the century
century = (year - 1) // 100 + 1

# Print the result
print(f"The year {year} is in the {century}. century.")

def convert_to_century(year):
    century = (int(year) - 1) // 100 + 1
    return century

# Funktsiooni kasutamine
year = input("Enter a year: ")
century = convert_to_century(year)
print("The century of the year", year, "is:", century)
