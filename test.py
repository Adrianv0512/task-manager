import requests

print("testing get...")
request_result = requests.get('http://127.0.0.1:5000/test')
print(request_result.text)

print("\ntesting post...")
payload = {"my_oshi": "inui toko", "key": "best vn developer"}
request_result = requests.post('http://127.0.0.1:5000/test', data=payload)
print(request_result.text)
