# Week 1.2, Session 1: Task 3

fruit = ("apple", "banana", "cherry")
print(fruit)

# Find and display position of "banana"
print(fruit.index("banana"))

# Display how many times "cherry" occurs
print(fruit.count("cherry"))

# Display how many times "strawberry" occurs
print(fruit.count("strawberry"))

# Unpack tuple into variables
(a,b,c) = fruit
print(a,b,c)
print(c)


#   SIDE NOTEE
#   tuples are immuetable too
#    you can do this too:
#          t = (1,2)    create a tuple
#          type(t)      would print tuple
#          dir(x)       would show all the methods a tuple can do
