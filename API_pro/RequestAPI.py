import requests
import random
import json
import string

base_url = "https://gorest.co.in"
auth_token = "Bearer fe14d5965993faf0a757d43e57eaa83a571e73cfeebfa8d72461a3b303b596c9"

# baseurl
def get_request():
    url = base_url + "/public/v2/users/"
    headers = {"Authorisation:",auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data,indent=4)
    print("json response body:",json_str)





get_request()