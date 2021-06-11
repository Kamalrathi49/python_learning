import requests

url = "https://api.pwnedpasswords.com/range/" + "0C6F6"
res = requests.get(url)
print(res)
