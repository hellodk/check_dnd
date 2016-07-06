import requests

# curl http://ncprstatus.in/api/v1/status?numbers={9964014500,8791134412}
url = "http://ncprstatus.in/api/v1/status"
payload = {"numbers": [9964014500]}
resp = requests.get(url, params=payload)
print resp.content

