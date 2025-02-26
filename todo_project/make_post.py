import requests

# Define the API endpoint
url = "http://localhost:8000/tasks/"

# Define the task data
data = {
    'title': 'New Task',
    'description': 'This is a description of the new task.',
    'due_date': '2025-03-20',
}

# Open the image you want to upload
files = {
    'photo': open(r'C:\Users\imang\OneDrive\Plocha\1013511.jpg', 'rb')  # Provide the path to the image file
}

# Make the POST request
response = requests.post(url, data=data, files=files)

# Check the response status and print the result
if response.status_code == 201:
    print("Task created successfully:")
    print(response.json())  # Print the created task data, including the 'id'
else:
    print(f"Failed to create task: {response.status_code}")
    print(response.json())  # Print the error details