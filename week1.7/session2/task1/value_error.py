# Week 1.7, Session 2: Task 1 - ValueError

# Run this program and observe what happens

user_profile = {"username": "alice99", "role": "admin"}

for key, value in user_profile.items():   #error here cause we're iterating over a dictiionary instead of using 'items()'. we add '.items()'
	print(f"{key} : {value}") 