# Week 1.3, Session 1: Task 3a

i = 0

while i < 20:
    i = i + 1
    
    if i % 3 == 0:
        continue
    print(i)   #took out the other print statement and put it here instead and works!

# Add logic using continue so that multiples of 3 are not printed out
# Hint: we discused operators such as % and // in recent weeks

# Hint 2: there are several ways to do this - using truthy/falsey values is the least code



#dont HAVE to use continue, only using it because we're learning about it. could instead do:
i = 0

while i < 20:
    i = i + 1
    if i % 3 != 0:   #if its not a multiple, then print, basically.
        print(i)  


#--------------------------
# NOTES
#break leaves the loop and continue ignores certain cases and continues the loop...less often needed but still sometimes useful
#if you use a break before an else statement, it doesnt go to the else and just breaks 