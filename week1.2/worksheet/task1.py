# Worksheet 1.2: Task 1 Solution
import sys

UserInput = input("Please enter an integer within the range 0-100: ")
if UserInput.isdecimal():
    UserInput = int(UserInput)

    if UserInput>=0 and UserInput<=39:
        print(f"{UserInput} is a Fail.")
    elif UserInput>=40 and UserInput<=69:
        print(f"{UserInput} is a Pass.")
    elif UserInput>=70 and UserInput<=100:
        print(f"{UserInput} is a Distinction!")
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")      
else:
    sys.exit("Error: Grade must be an integer between 0 and 100")
    

        




