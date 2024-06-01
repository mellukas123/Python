import json

sample_dict = {
    "name": "Merlyn",
    "age": 22,
    "city": "Espoo",
    "cats": ["Ronny", "Magorian"],
    "family":  [
        {
            "name": "Jarno",
            "age": 23
        },
        {
            "name": "Lumilee",
            "age": 1
        }
    ],
    "Married": False
}

# Add new Key, Value pair
sample_dict['favorite_color'] = "Red"
# Adjust existing key, value pairs
sample_dict['age'] += 1
sample_dict['cats'].append('Macrory')
print(sample_dict)

# Get specific data from dictionary
print(sample_dict['cats'])
print(sample_dict['family'][0]['age'])
print(sample_dict.get('city'))
print(sample_dict.get('food', 'DefaultValue'))

# Deleting values from dictionary
del sample_dict['favorite_color']
deleted_value = sample_dict.pop('family')
print(deleted_value)

# Making more readable - import json
print(json.dumps(sample_dict, indent=4))
