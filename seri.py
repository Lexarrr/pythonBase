# serialization
import json
import pickle as p

d = {
    'table': 'стол',
    'chair': 'стул'
}

# with open('dict.json', 'w') as j:
#     json.dump(d, j)

with open('dict.json', 'r') as j:
    d = json.load(j)

print(d)

# with open('dict.txt', 'rb') as pickling:  # .dat
#     d = p.load(pickling)
#
# print(d)
