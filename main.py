from tasks import tasks

name = input("what is your name? ")
print("Welcome " + name)
while True:
    user_tasks = input("put a task: ")

    if user_tasks == "done":
        with open("tasks.txt", "a") as file:
            file.write(f"user name is '{name}' user tasks are {tasks}\n")
            break

    tasks.append (user_tasks)
    print(f"your tasks are {tasks}")