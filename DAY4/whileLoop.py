# number = int(input("enter the number you : "))
# upto = int(input("upto : "))
# i = 1
# while i<=upto:
#     if upto<1:
#         break

#     print(f"{number} * {i} = {number*i}")
#     i += 1 
    
len = int(input("enter the number you want to add it in the list : "))
i = 0
friends = []
while i<len :
    name= input(f"enter name at index {i} : ")
    friends.insert(i,name)
    i += 1

print(friends)
