# Week 1.3, Session 1: Task 5a

course = "computer science"
characters = []

for ch in course:
	characters.append(ch)
characters.sort()           #needs to have this indentation because the first part adds and...
print(characters)


#could also just do characters = list(course)      to turn a string into a list of characters 
# and then print(characters)

# !!!!!!!!!! ALSO TO TOGGLE AND COMMENT SOME CODE, THEN DO CONTROL AND FORWARD SLASH! 


# create a list data structure of the characters from the course string
# sort the list into alphabetical order 



#-----------
#NOTES
#the word 'in' is inbuilt in python and you can use it to extract an item from a list 
#like this:
#			animals = ['dog', 'cat', 'hamster', 'goldfish']
#				for item in animals:
#					print(item)