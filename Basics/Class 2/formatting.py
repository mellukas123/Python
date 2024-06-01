print("Hello Ms. Merlyn, nice to meet you!")

title = "Ms."
name = "Merlyn"

# + method
print("Hello " + title + " " + name + ", nice to meet you!")

# printf
print("Hello %s %s, nice to meet you!" % (title, name))

# str.format()
print("Hello {} {}, nice to meet you!".format(title, name))
print("Hello {name} {title}, nice to meet you!".format(title=title, name=name))
print("Hello {0} {1}, nice to meet you!".format(title, name))

# f-string - most used, cleanest
print(f"Hello {title} {name}, nice to meet you!")

# rounding
number = 109.18794186161168156185
print(f"{number:.3f}")
print(f"{round(number, 3)}") #more logical, readability!
