amount_of_cats = int(input("How many cats? "))

if amount_of_cats == 1:
    print(f"Aliec has {amount_of_cats} cat.")
elif 2 < amount_of_cats < 20:
    print(f"Alice has {amount_of_cats} cats")
elif amount_of_cats >= 20:
    print("Alice has a cat shelter.")
else:
    print(f"Someone stole {amount_of_cats * -1} cats")