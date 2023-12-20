num1 = int(input("number enter please : "))
num2 = int(input("number enter please : "))
num3 = int(input("number enter please : "))
num4 = int(input("number enter please : "))

if num1>num2 & num1>num3 & num1>num4:
    print(f"{num1}: is the greatest of all")
elif num2>num1 & num2>num3 & num2>num4:
    print(f"{num2}: is the greatest of all")
elif num3>num1 & num3>num2 & num3>num4:
    print(f"{num3}: is the greatest of all")
else:
    print(f"{num4}: is the greatest of all")

