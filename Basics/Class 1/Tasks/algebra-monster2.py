# This algebra monster, equation to solve a3 – b3, formula: (a – b)(a2 + ab + b2)
print("Let's solve an algebra monster a3 - b3!")
a = int(input("Please provide a: "))
b = int(input("Please provide b: "))
total = int((a - b)*(a**2 + a*b + b**2))
print("Solution is: ", total)
