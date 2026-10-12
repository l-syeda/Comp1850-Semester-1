# Week 1.3, Session 1: Task 2b

print("This program will repeat everything you type.")
print("To exit the program type quit")

while True:
    user_input = input("Say something: ")
    if user_input.lower()=="quit":                #the   .lower() makes the input lower and exits whether its capitalised or not 
        break
    print(f"You said: {user_input}")
    #if user_input=="quit" or "Quit" or "QUIT":           dont put it here.... put it before it copies the message 
     #   break


# As written the program has an infinite loop.
# Add a break statement so that if the user types 'quit' the program exits. 