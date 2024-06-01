print("Hello World!")

variable1 = 15
variable2 = "String value qweqwe asdfbd"
variable3 = 15.134313
variable4 = True

# integer(int), float, string(str), boolean (bool), None, undefined
int(variable3)
float(variable1)
print(variable1) # Getting the type of variable

len(variable2)#kontrollimiseks tee print, strip eemaldab tähe vms
new_words =[] # new empty list
for word in  variable2.split(): # iterate through words
    new_words.append(word.strip('e')) # append list with striped e from the start and end of words

new_text = ' '.join(new_words) # convert list to text
print(new_text)

list_variable = [ {}, {}, {}]
dictionary = {'key': [{"key": [{}, {}, {}]}]}

user_choice = bool(input("Choose what to do: a: abc"))
print(user_choice)

# 0, '', null, undefined, [], {} = Falsy
# 1, ' ', [0], {"key":"value"} = Truthy

if user_choice:
    print("This happens")
elif user_choice == "potato":
    print("Latvian Gold")
else:
    print("Do whatever for not accounted cases.")

iterable_text= "asdasdadasdadaada"

for letter in iterable_text:
    print(letter)

while True:
    number = int(input("asdasd"))
    if number < 5:
        break


# while True:
#     print("Potato")


def function_name(*args):
    sum = 0
    for arg in args:
        sum += arg
    print(sum)


function_name(1, 2, 3, 4, 5, 6)

with open("test1.txt") as f:
    with open("test2.txt", "r+") as f2:
        print(f, f2)
