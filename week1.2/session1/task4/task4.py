# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetables)
print(both) #this prints out whats common in both sets, which is 'tomato'

# Why does the following code diplay five items?

food = fruit.union(vegetables)
print(food) #this prints out everything from both sets, without duplicates

# Add an item to fruit
fruit.add("mango")
print(fruit)

# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)

# Find and display symmetric difference of the two sets
SymmetricDifference = fruit.symmetric_difference(vegetables)
print(SymmetricDifference)

#-------------
#SIDE NOTEE
#       data = ["apple", "orange", "apple", "grape"]
#       unique_data = list(set(data))       converts to a set(so no duplicates) and then converts to a list 
# doing help(x.symmetric_difference) x being the name of the set, tells you what the method does 
 
