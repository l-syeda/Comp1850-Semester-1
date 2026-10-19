#A function that accepts an integer value and returns a list of even integers between 0 and that value

#longer method:
def even_numbers(limit):
    """
    returns a list of even numbers up to the given limit
    """
    evens= []
    for n in range(limit + 1):
        if n % 2 == 0:
            evens.append(n)
    return evens

print(even_numbers(20))




#shorter method
def even_numbers2(limit):
    return [n for n in range(limit+1) if n % 2 == 0]

print(even_numbers2(20))  
    