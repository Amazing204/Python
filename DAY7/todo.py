todoFile = "myToDoFile.txt"
def add_task():
    task = input("enter the input: ")
    with open("myToDoFile.txt",'a') as file:
        file.write(f"{task}\n")
    print("Tast added successfully")


def view_tasks():
    print("**********TO-DO_APP*************")
    with open("myToDoFile.txt", "r") as view:
        tasks = view.readlines()
        for x in tasks:
            print(x.strip())

def main():
    print("Welcome to the ToDo List App")

    while True:
        print("\n1. ****ADD TASK****\n2. ****VIEW TASKS****\n3. ****QUIT****")
        choice = input("enter your choice (1/2/3) : ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice =="3":
            print("No tasks to save. Quitting, Goodbye!")
            break
        else:
            print("please enter valid inputs (1 or 2 or 3)")
            break

if __name__ == "__main__":
    main()
