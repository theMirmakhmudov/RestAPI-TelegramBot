import requests

url = "http://127.0.0.1:8000/student-sponsor/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for student in data:
        print(f"Student Name: {student['name']}, Sponsor: {student['sponsor_name']}")
else:
    print("Failed to retrieve data.")
