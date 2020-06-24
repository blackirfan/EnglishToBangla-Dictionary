import json
data = json.load(open("bangla_full.json",encoding="utf8"))

# print(data)
li = []
print(data[2])

limit = len(data)
print(limit)

def translate(w):
    w = w.lower()
    for i in range(limit):
        if data[i]['dictionary']  == w:
            li.append(data[i]['mean'])
    if len(li) > 0:
        return li[0]
    else:
        return "The word not available  now. Please recheck your word"

word  = input("Enter English word: ")

print(translate(word))
