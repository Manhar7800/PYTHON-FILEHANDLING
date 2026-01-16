# loop json

import json
user_list=[]#array
user={}#bject

for i in range(1,4):
    user={}#object
    name=input("Enter the name:")
    subject=input("Enter the subject:")
    score=int(input("Enter the score:"))


    user["name"]=name
    user["subject"]=subject
    user["score"]=score

    user_list.append(user)

    with open("myfile8.json","w") as f:
        json.dump(user_list,f,indent=4)

    print("succsesfully record inserted")