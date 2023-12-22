import calC_module as c 


num1 = int(input("enter number one : "))
num2 = int(input("enter number two : "))

operation = input("Enter the operation you want to perform:\n*\n+\n-\n/\nenter here : ")
if operation == '+':
    print(f"addition of the given numbers are : {c.add(num1,num2)}")
elif operation == '-':
    print(f"substracion of the given numbers are : {c.sub(num1,num2)}")
elif operation == '*':
    print(f"multiplicton of the given numbers are : {c.mul(num1,num2)}")
elif operation == '/':
    print(f"division of the given numbers are : {c.div(num1,num2)}")
else:
    print("please enter valid option :")


          