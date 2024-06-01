#Write a program to based on current time of day would return a word Morning 6-12, Day12-17, Evening17-22 or Night 22-6.
#hint: use datetime library. To get current time you will need to

from datetime import datetime
current_hour = datetime.now().hour
if 6 <= current_hour < 12:
    print("Good Morning!")
if 12 <= current_hour < 17:
    print("Good Day!")
if 17 <= current_hour < 22:
    print("Good Evening!")
else:
    print("Good Night!")