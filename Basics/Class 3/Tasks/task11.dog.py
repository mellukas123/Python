#Write a Python program to calculate a dog's age in dog years.
# Note: For the first two years, a dog year is equal to 10.5 human years.
# After that, each dog year equals 4 human years.
years = int(input("Enter your dog age:"))

if years <= 2:
    dog_years = years * 2
    print("Your dog age in human years is ", dog_years)
else:
    dog_years_2 = 2 * 10.5 + (years - 2) * 4
    print("Your dog age in human years is ", dog_years_2)

