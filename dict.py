import json
from difflib import get_close_matches
data=json.load(open("data.json"))


def dict(word):
  word = word.lower()
  if word in data:
     return data[word]
  elif word.title() in data:
     return data[word.title()]
  elif word.upper in data:
     return data[word.upper()]
    
  elif len(get_close_matches(word,data.keys()))>0:
     y=input("Did you mean %s instead?Enter Y if yes or N in no? :" % get_close_matches(word,data.keys())[0])
     if y=="Y" :
        return data[get_close_matches(word,data.keys())[0]]
     elif y=="N" :
        return "There is no such word.Please check the word. "
     else:
        return "This is invalid entry."

  else:
      return "There is no such word.Please check the word."


a=input("Enter the word:")
b=dict(a)
if type(b)==list:
    for item in b:
        print(item)
else:
    print(b)
