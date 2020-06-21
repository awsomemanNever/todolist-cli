import pickle
todos = pickle.load(open("names.dat", "rb"))

print(
    "What do you want to do? \n \n For seeing lists - display \n For adding todos - add \n for removing todos - remove \n to exit program - exit")
x = 1
while True:
    enter = input("Enter choice: ")
    print("\n")
    if enter == "display":
        for todo in todos:
            print(str(x) + ". " + todo)
            x += 1
        x = 1

    if enter == "add":
        a = input("Enter the todo: ")
        todos.append(a)

    if enter == "remove":
        b = int(input("Enter the no of the todo: "))
        todos.pop(b - 1)

    if enter == "exit":
        print("Stopping program")
        pickle.dump(todos, open("names.dat", "wb"))
        break
