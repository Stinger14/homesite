"""
Use the requests library to fetch data from a REST API and process the JSON 
response to extract specific information.
"""

import requests

def fetch_and_process_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        id = data['id']
        title = data['title']
        print(f'ID: {id}')
        print(f'Title: {title}')
    else:
        print("Failed to fetch data!")

fetch_and_process_data("https://jsonplaceholder.typicode.com/todos/1")
