from unittest.mock import patch
import requests

# Function representing a database lookup
def fetch_user():
    return "Actual User"

# Function to retrieve post details
def fetch_post():
    result = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return result.json()


# Mock the database function
with patch("__main__.fetch_user") as mock_user:
    mock_user.return_value = "Test User"
    print("Database Result:", fetch_user())


# Mock the API response
with patch("requests.get") as mock_request:

    mock_request.return_value.json.return_value = {
        "id": 101,
        "title": "Sample Mock Data"
    }

    print("API Result:", fetch_post())
