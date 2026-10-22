# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value to be "-". The function returns the formatted date as a string
# in the format day-month-year with the default separator.


def format_data(day, month, year, separator = "-"):
    # complete your code here
    formatted_date = f"{day:02d}{separator}{month:02d}{separator}{year:04d}"    #02d means it will be 2 digits
    return formatted_date


# Write code to test the function with separators such as "/", ":", "."
print(format_data(22,10,2026)) 
print(format_data(22,10,2026,separator = "."))   #can also change it here again 
print(format_data(7,1,2026,separator = ".")) # here i used smaller values so u can see it adds leading zeroes, cause i used 02d
