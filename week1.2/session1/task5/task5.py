# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Newcastle"] = "River Tyne"
print(rivers)

# Display all the keys
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
print(rivers.items())

# Delete an entry from the rivers database
print(rivers.pop("London"))



#   SIDE NOTEE
#   if you want to look up something within it, you need to use the key, which would be the thing after the colon

#   prices = {"apple": 21, "orange": 30, "banana": 45}
#   print(prices["apple"]) # prints 21
#   prices["apple"] = 25 # replaces value for key 'apple'
#   print(prices["apple"]) # prints 25
#   print(prices["kiwi"]) # what happens here?              this would give a key error 
#   prices["kiwi"] = 53 # adds new key-value pair
