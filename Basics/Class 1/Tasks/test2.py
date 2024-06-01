radius1 = 32
radius2 = 36
price1 = 15
price2 = 20
def circle_area_to_price(radius, price):
    import math

pi = 3.14
area = pi * radius * radius
return (area/price)
print(circle_area_to_price(radius1, price1))
print(circle_area_to_price(radius2, price2))