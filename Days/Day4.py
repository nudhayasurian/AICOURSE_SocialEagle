#dictionary in for loop
my_dict = {"name": "Alice", "age": 30, "city": "New York"}  
for key, value in my_dict.items():
    print(key, ":", value)
#convert 2 list to dictionary using for loop
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
my_dict = {}
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]
print(my_dict)  
task = ['read', 'write', 'code', 'debug']
print("Task list:", task)
task.append("test")
print("Updated task list:", task)
print("Index of 'code':", task.index("code"))
for t in task:
    print("Task:", t)
