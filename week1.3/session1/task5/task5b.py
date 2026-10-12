# Week 1.3, Session 1: Task 5b

rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# loop through the dict extracting key and value

for c, r in rivers.items():     # items() returns them both as a tuple(as a pair) 
    print(c, r)


# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
# hint: we looked at built in function for dicts last session

for city in rivers.keys():
    print(city)     #this only prints the cities and not them as a pair
    #using a 'for loop' on a dictionary iterates over the keys anyway, so dont need .keys()  -so we can lowk just take out the .keys() and do print(city)

for river in rivers.values():     #only prints the values and not the keys
    print(river) 


