
#FUnctions with list

# def student(name,*subjects):
#     print(f"student name is : {name}")
#     for subj in subjects:
#        print(f"enrolled in : {subj}")

# student('sahil','science','maths','physiscs','chemistry')


#functions with dictionary

def student(name,**details):
    print(f"student name is : {name}")
    for key,value in details.items():
       print(f"{key} : {value}")

student("sahiil", course = 'Ai', age = 19 , college = 'raisoni' , relationship = 'available' )