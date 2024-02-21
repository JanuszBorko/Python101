import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts/3')
print(r.status_code)
print(r.text)
#print(r.json())