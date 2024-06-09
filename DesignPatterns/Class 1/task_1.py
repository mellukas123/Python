# Teach our user culture if user will write the name with
# the small letter don't invite him, but if he will use
# capitalized name, say " Hello {name}"

def check_name(func):
    def some_inner(*args):
        for arg in args:
            if arg[0].isupper():
                func(*args)
            return
        else:
            print("You fool! You should have used the capital letter!")
    return some_inner

def greet_user(name):
    if name[0].isupper():
        print(f"Hello {name}")
    else:
        print("You are not invited.")

# Test the function
greet_user("Merlyn")  # Expected output: Hello John
greet_user("merlyn")  # Expected output: You are not invited.

