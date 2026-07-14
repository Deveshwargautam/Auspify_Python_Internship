import os

FILE_NAME = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_name, status = line.strip().split("|")
                tasks.append({"task": task_name, "done": status == "True"})
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['done']}\n")

def show_tasks(tasks):
    if not tasks:
        print("\nThere are no tasks!")
        return
    print("\n--- Your Task List ---")
    for index, task in enumerate(tasks, start=1):
        status = "✅ complete" if task["done"] else "❌ अधूरा"
        print(f"{index}. {task['task']} [{status}]")

def main():
    tasks = load_tasks()
    while True:
        print("\n1.add task | 2. see task | 3. Mark the Task as completedं | 4. Delete Task | 5. Exit")
        choice = input("choose optionं (1-5): ")

        if choice == "1":
            task_name = input("write the task name ")
            if task_name:
                tasks.append({"task": task_name, "done": False})
                save_tasks(tasks)
                print("Task added!")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Select the number of tasks completed: ")) - 1
                    if 0 <= idx < len(tasks):
                        tasks[idx]["done"] = True
                        save_tasks(tasks)
                        print("The task is marked 'completed'!")
                    else:
                        print("worng number!")
                except ValueError:
                    print("put the right number।")
        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                try:
                    idx = int(input("Select the number of tasks to delete: ")) - 1
                    if 0 <= idx < len(tasks):
                        deleted = tasks.pop(idx)
                        save_tasks(tasks)
                        print(f"'{deleted['task']}' was deleted!")
                    else:
                        print("worng number!")
                except ValueError:
                    print("pls put the right number।")
        elif choice == "5":
            print("BYE! Your data is safe।")
            break
        else:
            print("Wrong choice, try again।")

if __name__ == "__main__":
    main()
