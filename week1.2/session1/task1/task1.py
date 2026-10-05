# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
shopping.pop(3)
shopping.append("grapes")
print(shopping)                  #or you can simply just do   shopping[3] = "grapes"

# Add yoghurt, just after milk
shopping.insert(1,"yoghut")       #the index number should be where you want it to go, so after milk is index 1, so yoghurt would be index 1 
print(shopping)