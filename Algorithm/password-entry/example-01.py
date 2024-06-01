def password_entry():
    correct_password = "my_password"
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        password = input("Enter the password: ")

        if password == correct_password:
            print("Login successful")
            break
        else:
            print("Incorrect password. PLease try more")
            attempts = attempts + 1
    if attempts == max_attempts:
        print("Max attempts reached, Login failed.")

password_entry()