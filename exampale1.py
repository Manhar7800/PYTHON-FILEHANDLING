f=open("myfile1.txt","r")
print(f.read())

# with open
with open("myfile1.txt","r") as f:
    print(f.read())