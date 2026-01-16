import json

with open("myfile8.json","r") as f:
    data=json.load(f)
    for stu in data:
  
     print(stu["name"])


# json 8 me name ko fatch kiya loop se