# Working with json  file

"""
Json:
Json which is stands for javascript oject notation/.
Json which is contain array and object
-array which is represent by [] braces.
-object which is represent by {} braces.
"""

import json
user={}
name=input("enter the name")
subject=input("Enter the subject")
score=int(input("enter the score"))


user["name"]=name
user["subject"]=subject
user["score"]=score

with open("myfile7.json","w") as f:
    json.dump(user,f,indent=4)
    f.close
    print("Susccsefuly record:")