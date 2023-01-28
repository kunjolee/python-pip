import requests

def get_categories():
    res = requests.get('https://api.escuelajs.co/api/v1/categories')
    
    print(res.status_code)

    categories = res.json()
    for category in categories:
        print(category['name'])
        print(category['image'])
