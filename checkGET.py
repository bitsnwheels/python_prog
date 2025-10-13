import requests
import json

# Define the URL for the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make the GET request
response = requests.get(url)

# Test 1: Check if the status code is 200 (OK)
assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

# Parse the JSON response
data = response.json()

# Test 2: Check the User ID in the response
assert data['userId'] == 1, f"Expected userId to be 1, but got {data['userId']}"

# Test 3: Check the data type of the title
assert isinstance(data['title'], str), f"Expected title to be a string, but it was {type(data['title'])}"

# Test 4: Check the Content-Type header
expected_content_type = "application/json; charset=utf-8"
assert response.headers['Content-Type'] == expected_content_type

print("All GET tests passed successfully!")