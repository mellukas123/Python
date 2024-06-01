# get the average or right side numbers,
# get the average or left side numbers and
# than the average of both side numbers averages.
# Example result:
# rightside: 2
# leftside: 4
# bothsides: 3
import json

with open('data.json') as in_file:
    data = json.load(in_file)

right_side = round(sum(data['right_side']) / len(data['right_side']))
left_side = round(sum(data['left_side']) / len(data['left_side']))

print("Right side", right_side)
print("Left side", left_side)
print("Average or Averages", (right_side + left_side) / 2)