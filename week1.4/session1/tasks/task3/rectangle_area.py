
# function implementation

def rectangle_area():  # define suitable input data
    # ...               # implement the function
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    area = int(base*height)
    return area         # return an appropriate value

# testing the function

print(f"Area is {rectangle_area( )}")   # provide suitable data matching your inputs



#----------------
#what the teacher did
def rectangle_area2(base,height):  
    area2 = int(base*height)          # or could just write in one line and do:  return base*height
    return area2         

print(f"Area is {rectangle_area2(2, 5)}")   



"""
testing out doctrings lol
"""

