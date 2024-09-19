import requests
import json

payload = {
    "user_key": "MYUSERKEY",
    "firm_key": "MYFIRMKEY",
}
aia_ddx_api_host = "https://2030ddx.aia.org"
aia_authenticate_url = "{0}/api/v1/authenticate".format(aia_ddx_api_host)
headers = {'Content-type': 'application/json'}
r = requests.post(aia_authenticate_url, data=json.dumps(payload), headers=headers)
authToken = None

if r.status_code == 200:
    content = json.loads(r.text)
    authToken = content.get("authToken")
    print(content)
    print(authToken)
else:
    print(f"Failed to authenticate: {r.status_code}")
    print(r.text)
