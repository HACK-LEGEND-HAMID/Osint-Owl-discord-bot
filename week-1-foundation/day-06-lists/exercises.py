#Day 6:Exercise 6 Solve all the error this file...
todo_list = []

print("="*40)
print("TO-DO LIST".center40))
print("="*40)

print("\nAdd your tasks (type 'done' to finish):")
print("-"*40)

task_number = 1
while true:
    task = input(f"Task {Task_number}: ")
    
    if task.lower() == 'done':
        break
    
    to_do_list.append(task)
    task_number += 1

print("\n" + "="*40)
print("YOUR TASKS".center(40))
print("="*40)

if to_do_list:
    for i, task in enumerate(to_do_list, 1):
        print(f"[i]. {task}")
else
    print("No Tasks Added!")


