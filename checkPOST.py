import requests

# Define the URL for creating posts
url = "https://jsonplaceholder.typicode.com/posts"

# Define the payload (the data to send)
payload = {
    "title": "My New Post in Python",
    "body": "This is a test post from a Python script.",
    "userId": 101
}

# Make the POST request
response = requests.post(url, json=payload)

# Test 1: Check for 201 Created status code
assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"

# Parse the response
data = response.json()

# Test 2: Check if the response title matches what we sent
assert data['title'] == payload['title']

# Test 3: Check if the API assigned an ID
assert 'id' in data

print("All POST tests passed successfully!")