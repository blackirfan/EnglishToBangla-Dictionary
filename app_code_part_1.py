import json
data = json.load(open("bangla_full.json",encoding="utf8"))

# print(data)

print(data[2])

limit = len(data)
print(limit)

def translate(w):
    for i in range(limit):
        if data[i]['dictionary']  == w:
            return data[i]['mean']

word  = input("Enter English word: ")

print(translate(word))