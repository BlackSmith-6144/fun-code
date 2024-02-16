task1 = input("Task1:")
task2 = input("Task2:")
task3 = input("Task3:")
print("Write \"Done\" if you do the task or write \"Undo\" if you doesn't do the task.")
dodont1 = input("Task1:")
dodont2 = input("Task2:")
dodont3 = input("Task3:")
do = "Done"
un = "Undo"
if dodont1 == do and dodont2 == do and dodont3 == do:
    print(f"{task1}:{do}")
    print(f"{task2}:{do}")
    print(f"{task3}:{do}")
elif dodont1  == un and dodont2 == un and dodont3 == un:
    print(f"{task1}:{un}")
    print(f"{task2}:{un}")
    print(f"{task3}:{un}")
elif dodont1 == un and dodont2 == do and dodont3 == do:
    print(f"{task1}:{un}")
    print(f"{task2}:{do}")
    print(f"{task3}:{do}")
elif dodont1 == do and dodont2 == un and dodont3 == do:
    print(f"{task1}:{do}")
    print(f"{task2}:{un}")
    print(f"{task3}:{do}")
elif dodont1 == do and dodont2 == do and dodont3 == un:
    print(f"{task1}:{do}")
    print(f"{task2}:{do}")
    print(f"{task3}:{un}")
elif dodont1 == un and dodont2 == un and dodont3 == do:
    print(f"{task1}:{un}")
    print(f"{task2}:{un}")
    print(f"{task3}:{do}")
elif dodont1 == do and dodont2 == un and dodont3 == un:
    print(f"{task1}:{do}")
    print(f"{task2}:{un}")
    print(f"{task3}:{un}")
else:
    print("NOT VALID INPUT")
