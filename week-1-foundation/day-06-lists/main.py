#Day 6: TO-DO List Demo File
to_do_list = []

print("="*40)
print("TO-DO LIST".center(40))
print("="*40)

print("\nAdd your tasks (type 'done' to finish):")
print("-"*40)

task_number = 1
while True:
    task = input(f"Task {task_number}: ")
    
    if task.lower() == 'done':
        break
    
    to_do_list.append(task)
    task_number += 1

print("\n" + "="*40)
print("YOUR TASKS".center(40))
print("="*40)

if to_do_list:
    for i, task in enumerate(to_do_list, 1):
        print(f"{i}. {task}")
else:
    print("No Tasks Added!")

