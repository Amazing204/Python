age = int(input(" enter your age: "))

if age>=18:
    voter_id =input("do you have voter id (y/n): ")
    if voter_id == 'y' or voter_id == 'Y':
        print("you can vote")
    else:
        print("apply for voter id")
else:
    print("under age")