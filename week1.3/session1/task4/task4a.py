# Week 1.3, Session 1: Task 4a

sum = 0

for k in range(1,10):
    if k%2==0:
        print(sum)     #prints the sum at each iteration
        sum = sum + k ** 2     #the ** means to the power of

print(sum)



# modify the code to sum the squares of even numbers up to and including 20

# modify the code to print the sum at each iteration


# !!!
#teacher did this instead
sum = 0

for k in range(2, 21, 2):    #icl idk why he did this range 
    sum = sum + k ** 2 
print(sum)



#-----------------------
# NOTES
#python doesnt have a do while loop because you can acheive the same thing with a while true, if and then break

#print(range(4)) prints (0,4)
#print(list(range(4)))  this prints 0,1,2,3
#with the range function, we can print going up, and also going down  