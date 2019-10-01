class Task:

    def __init__(self, name, deadline, level):
        self.name = name
        self.deadline = deadline
        self.level = level

class TaskManager:

    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    def printTheMostImportantTasks(self):
        for task in self.tasks:
            if task.level > 5:
                print(task.name, task.deadline)
            else:
                continue

def main():
    auaTasks = TaskManager()
    personalTasks = TaskManager()
    t = Task("Calculus HW", "10/10/19", 8)
    auaTasks.addTask(t)

    t = Task("Get Ready for Midterms", "26/10/19", 5)
    auaTasks.addTask(t)

    t = Task("Pay Cellphone Bill", "22/10/19", 2)
    personalTasks.addTask(t)

    t = Task("sister's birthday gift", "22/10/19", 10)
    personalTasks.addTask(t)

    auaTasks.printTheMostImportantTasks()

main()


