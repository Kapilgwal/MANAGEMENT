import requests

URL = "http://127.0.0.1:8000/api/doctor/"

def get_data(id=None):
    if id is not None:
        response = requests.get(f"{URL}{id}/")
    else:
        response = requests.get(URL)

    try:
        data = response.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Invalid or empty JSON response")
        print("Status Code:", response.status_code)
        print("Text:", response.text)


def post_data():
    data = {
        'name': 'Ravi Kumar',
        'age': 45,
        'specialty': 'ENT',
        'phone' : '9999999999',
        'email' : 'example@gmail.com'

    }
    response = requests.post(url=URL, json=data)
    print(response.json())


def update_data():
    data = {
        'id': 4,
        'name': 'Deck',
        'city': 'London'
    }
    response = requests.put(url=URL, json=data)
    print(response.json())


def delete_data(id):
    response = requests.delete(url=f"{URL}{id}/")
    try:
        print(response.json())
    except requests.exceptions.JSONDecodeError:
        print("Deleted successfully or no content returned.")
        print("Status Code:", response.status_code)

# Example usage:
get_data()
# post_data()
# update_data()
# delete_data(3)
