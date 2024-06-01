#Write a program (or function) that will compare the area/price ratio between two pizzas.
print("Let's find out which pizza has the best price/quantity ratio!")
r_1 = input("Please enter the radius of the first pizza: ")
p_1 = input("Please enter the prize of the first pizza: ")
r_2 = input("Please enter the radius of the second pizza: ")
p_2 = input("Please enter the prize of the first pizza: ")

def circle_area_to_price(r, p):

area_1 = r_1 ** 2 * 3.14
area_2 = r_2 ** 2 * 3.14
return r/p

print(circle_area_to_price(r1, p1))
print(circle_area_to_price(r2, p2))