print("======Welcome to To-Do list======")
print("Choose Thing you want to do:-")

tasklist = []
prgrm = 0

while prgrm != 4 :
    print("1. Add New Task\n"
        "2. View task\n" 
        "3. Delete task\n" 
        "4. Quit")
    prgrm = int(input("Please choose the number = "))
    if prgrm == 1:
        #addtask
        addtask = input("add your new task = ")
        tasklist.append(f"- {addtask}")
        print("Task added!")

    elif prgrm == 2:
        #viewtask
        for task in tasklist:
            print(task)
            
    elif prgrm == 3:
        #deletetask
        for task in tasklist:
            print(task)
        dlt = int(input("which task you want to delete state the number = "))
        tasklist.pop(dlt-1)
    else:
        #wrong input
        print("Wrong input!")
