# Week 1.2, Session 1: Task 2

fruit = ["cherry", "strawberry", "melon", "grape", "apple"]

# Sort list
fruit.sort()
print(fruit)

# Reverse order of list items
fruit.reverse()
print(fruit)

# Remove all items
fruit.clear()   #wouldnt use fruit.remove() thats for a speciic value. also note that remove(item) removes the actual word, not the index
print(fruit)


# -----------------------
#its different to strings, for example
text = "a string"
print(text[4])   #this would print 'r', not 't'. the char data type does that, but python doesn't have that data type

#another thing to note, strings in python are immutable, you cannot chanage it. 
#for example this wouldnt work:          text[0] = "z"

