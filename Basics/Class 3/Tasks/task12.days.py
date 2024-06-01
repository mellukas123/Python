#Write a Python program to convert a month name to a number of days.
import calendar
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
user_input_month = input("Enter the month: ")
# Capitalize the month to match our months list
user_input_month = user_input_month.capitalize()

if user_input_month in months:
    month_index = months.index(user_input_month) + 1
    days_in_month = calendar.monthrange(2024, month_index)[1]
    print(f"{user_input_month} has {days_in_month} days.")
else:
    print("Error. Try again.")
