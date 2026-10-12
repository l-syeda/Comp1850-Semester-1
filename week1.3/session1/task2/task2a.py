# Week 1.3, Session 1: Task 2a

k = 2
while True:
    k = 2 * k 
    print(k)
    if k>1000:
        break
    

# As written this is an infinite loop.
# If you run it, use <Ctrl>C to exit the running program.

# 1. Add a break statement to exit the loop if k>200

# 2. Rewrite the code to directly use the while loop instead of break.
p=2
while p<100:
    p=2*p
    print(p)


#can just do this instead of what i did:
k = 2
while k<=20:
    k = 2 * k 
    print(k)
