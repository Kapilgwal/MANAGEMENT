import requests

URL = "http://127.0.0.1:8000/api/user/login/"

def post_data():
    data = {
        'email': 'ravi@gmail.com',
        'password': '12345',
    }
    response = requests.post(url=URL, json=data)
    print(response.status_code)
    print(response.json())

post_data()
