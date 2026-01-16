f=open("myfile5.txt","w")
n=int(input("Enter your data:"))

for i in range(n):
    name=input("enter the name:")
    age=int(input("Enter the age:"))
    gender=input("Enter the gender ")


    f.write(f"name is {name} and ge is {age} and {gender}")

    f.close

    print("Data file succsesfully write:")