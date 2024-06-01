import json

text = "Cupcake ipsum dolor sit amet I love halvah cotton candy I love. Bear claw I love croissant I love pie sesame snaps marshmallow marshmallow bonbon. Sesame snaps candy canes wafer dragée danish. Ice cream jujubes tiramisu I love pudding carrot cake icing jelly tart."
words_counter = {}

words_list = text.split()

for word in words_list:
    if words_counter.get(word.strip(".")):
        words_counter[word.strip(".")] += 1
        print("In")
    else:
        words_counter[word.strip(".")] = 1
        print("Not in")

print(json.dumps(words_counter, indent=2))
