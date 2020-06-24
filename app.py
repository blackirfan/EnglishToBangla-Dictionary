import json
from difflib import get_close_matches
data = json.load(open("bangla_full.json",encoding="utf8"))
word_list = []
li = []
second_time = []
third_time = []

limit = len(data)

'''
Take all key word from the json file as a list

'''
for t in range(limit):# for finout word list
    word_list.append(data[t]['dictionary'])

'''
remove all None type data in list

'''
Not_none_values = filter(None.__ne__, word_list) # for remove None type value from a list
second_time = list(Not_none_values)




def translate(w):
    w = w.lower()

    target_word = get_close_matches(w,second_time)
 
    for i in range(limit):
        if data[i]['dictionary']  == w:
            li.append(data[i]['mean'])
            
    if len(li) > 0: 
        return li[0]
    elif len(get_close_matches(w,second_time))>0:  #ekhane  check kora hoise je 
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % target_word[0])
        if yn == "Y":
            for i in range(limit):
                if data[i]['dictionary']  == str(target_word[0]):
                    third_time.append(data[i]['mean'])

            if len(second_time) > 0:
                return third_time[0]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word not available now. Please recheck your word "

print("                     Welcome to English to Bangla dictionary                    ")
word  = input("Enter English word: ")
print(translate(word))



