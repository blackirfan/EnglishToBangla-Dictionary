import json
from difflib import get_close_matches
data = json.load(open("bangla_full.json",encoding="utf8"))
word_list=[]
second_time =[] 
third_time = []


li = []




limit = len(data)

for t in range(limit):
    word_list.append(data[t]['dictionary'])

Not_none_values = filter(None.__ne__, word_list)
second_time = list(Not_none_values)

print(len(second_time))

def translate(w):
    w = w.lower()
    target_word = get_close_matches(w,second_time)
    for i in range(limit):
        if data[i]['dictionary']  == w:
            li.append(data[i]['mean'])
    if len(li) > 0:
        return li[0]
    elif len(get_close_matches(w,second_time))>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % target_word[0])
        if yn == "Y":
            for i in range(limit):
                if data[i]['dictionary'] == str(target_word[0]):
                    third_time.append(data[i]['mean'])
            if len(second_time) > 0:
                return third_time[0]
        elif yn == "N":
            return "The word doesn't exist . please double check it."
        else:
            return "We did not understand your entry"
    else:
        return "The word not available  now. Please recheck your word"


print("                            welcome  to English to Bangla dictionary                         ")
word  = input("Enter English word: ")

print(translate(word))
