# a basic Hello World program - write your code under this line
print("hello world")
name = "Nick"
age = 42
print(f"Hello {name}")
name = "Emma"
print(f"Hello {name}")
name = "Holly"
print(f"Hello {name}")

question1 = input("What is your name?")
print(f"oh cool! i know someone called {question1}")




try:
    num1 = int(input("Enter your number: "))
    num2 = int(input("Enter your number: "))
    answer = num1 + num2
    print(f"{num1} + {num2} = {answer}")
except:
    print("Please enter numbers only.")


message="hello"
print(message.upper()) #makes the message all uppercase



