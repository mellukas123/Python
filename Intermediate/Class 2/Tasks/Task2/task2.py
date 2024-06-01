import csv
import json

with open('info_output.csv', 'r') as file:
    data = [row for row in csv.DictReader(file)]

with open('info_output.csv', 'w', newline='') as output:
    headers = reader[0].keys()
    writer = csv.DictWriter(output, fieldnames=headers)

    writer.writeheader()
    writer.writerows(data)