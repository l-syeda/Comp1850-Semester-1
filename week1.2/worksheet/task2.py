# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

numbers = read_numbers()

if numbers == []:
    sys.exit("Error: no numbers provided")

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers)/len(numbers)

numbers.sort()
middle = (len(numbers)-1)//2
if len(numbers) % 2 == 0:
    
    








