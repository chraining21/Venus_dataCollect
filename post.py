import requests
url = 'http://127.0.0.1:8000/upload'
with open('./test.jpg', 'rb') as f:
    img = f.read()
file = {'file': ('test.jpg',img, 'image/jpg')}
r=requests.post(url,files=file)

print(r.text)