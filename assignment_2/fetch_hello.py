import requests

url = "https://raw.githubusercontent.com/priyankara96/COE3200_Assignment_2_Part_i/main/assignment_2/hello.py"

try:
    response = requests.get(url)
    response.raise_for_status()

    print("File content:")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Failed to fetch the file: {e}")
