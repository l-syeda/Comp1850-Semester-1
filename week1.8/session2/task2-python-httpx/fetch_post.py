"""
Task 2: Fetch and display a post Using GET Request
"""

import httpx

url = "https://httpbin.io/json"

response = httpx.get(url)   # httpx object, get() method, returns a response object

#We should check first to see if the request succeeded



print(response.json())      # response object, json() method 
