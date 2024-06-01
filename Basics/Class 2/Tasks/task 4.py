#Create a list with 5 names in it. Append one name, insert one name at the start of the list, sort and reverse the list. Print out the indexes of these added names.
names = ["Tom", "Olaf", "Laura", "Marjen", "Annabel"]
print(names)
names.append("Hugo")
index_of_tom = names.index('Tom')
# print(f"The index of Tom is this list is: {names.index('Tom')} ")
names.insert(index_of_tom, "Kuldar")

names.sort()

names.reverse()
print(names)

index_of_hugo = names.index('Hugo')
# print(f"The index of Hugo is this list is: {names.index('Hugo')} ")
index_of_kuldar = names.index('Kuldar')
# print(f"Te index of Kuldar in this list is: {names.index('Kuldar')}")