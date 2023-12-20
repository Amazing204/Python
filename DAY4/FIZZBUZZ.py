numberBatao = int(input("enter the length : "))
i = 0
numbers = []
while i<numberBatao:
    num = int(input(f"insert at index {i} : "))
    numbers.insert(i, num)
    i+=1

for test in numbers:
    if test % 3 == 0 and test % 5 == 0 : 
        print(f"{test} : fizzbussss")
    elif test % 5 == 0 : 
        print(f"{test} : buzz")  
    elif  test % 3 == 0  : 
        print(f"{test} : Fizz")  
    else:
        print(f"{test} : " )
        
print(numbers)

