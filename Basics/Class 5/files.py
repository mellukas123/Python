# "r" - read mode (default value)
# "w" - write mode
# "x" - creation mode. If the file already exists, the operation fails
# "a" - appending mode
# "b" - binary mode
# "t" - text mode
# "+" - updating mode (read/write)


# f = open("example.txt")
# print(f.readline())

# Used to be that way:
# f = open ("example.txt")
# print(f.readline())
# f.close()

with open("example.txt", "r+") as f:
    print(f)
    #f.write("\nLines")
    #f.writelines(["some\n", "New\n", "text\n", "TO\n", "FILE\n"])

   # print(f.readlines())
    keys = f.readline().strip().split(',') # [name, surname, age, potatoes]
    lines = f.readlines() # [Merlyn, Mey, 22, 3, Jarno, Ahi, 23, 4]
    my_people = []
    for line in lines:
        person = line.strip().split(",")
        person_dict = {}
        for index, attribute in enumerate(person):
            person_dict[keys[index]] = attribute
        my_people.append(person_dict)

        # my_people.append({keys[0]: deeper_value[0], keys[2]: deeper_value[2]})

print(my_people)