"""start
|
Do
| ---- Loop body -----> condition
|                            |
| <-----------------         | yes
|
End
"""
# Initialize a variable
count = 0

while True:
    # This is going to represent what we want to do
    print("This is iteration", count)
    # Increment count
    count += 1

    # Check the condition at the end the loop
    if count >= 5:
        break