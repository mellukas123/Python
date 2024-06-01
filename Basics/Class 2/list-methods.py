cars = ["VW", "Audi", "BMW"]

#Adding value to the list - one at a time
cars.append("Zap")
cars.append("Cupra")
# Joining lists - multiply vales
cars.extend(["Nissan", "Volvo", "Opel", "VW"])
# Length of cars list
print(len(cars))
# Sort the list
cars.sort()
# Get a count of certain cars
print(cars.count("VW"))
print(f'Amount of Volkswagen in the list: {cars.count("VW")} ')
# Get the index of certain record
index_of_cupra = cars.index('Cupra')
print(f"The index of Cupra is this list is: {cars.index('Cupra')} ")
# Inserting at a certain index
cars.insert(index_of_cupra, "Opel")
print(cars)
cars.pop(index_of_cupra)
# Remove the last item from the list
cars.pop()
# Reverse the list
cars.reverse()
# Clear the list
cars.clear()

print(cars)