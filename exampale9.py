import json

with open("myfile7.json","r") as f:
    data=json.load(f)
    print(data)

    print(data["name"])


# json me se data ko fatch kiya 