import requests as req
import os
from PIL import Image
from IPython.display import IFrame

# resp = req.get("https://www.ibm.com")
# print(resp.status_code)
# print(resp.headers)

url = 'http://httpbin.org/get'
resp = req.get(url)
# print(resp.text)
print(resp.json())
print(resp.request.headers)
print(resp.request.body)

payload = {'id': 27, "name": "Awi"}
resp = req.get(url, params=payload)

print(resp.json())

post_url = 'http://httpbin.org/post'
post_resp = req.post(post_url, data=payload)
print(post_resp.json()['form'])

print(resp.url)
print(post_resp.url)

resp = req.get(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png')
path = os.path.join(os.getcwd(), 'image.png')
print('path ', path)
with open(path, 'wb') as f:
    f.write(resp.content)
Image.open(path)
