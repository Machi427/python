import requests

res = requests.get('http://example.com', auth=('user', 'pass'))

print(res.status_code)

