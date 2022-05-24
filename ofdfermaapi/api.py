import requests
import json


class FermaApi(object):
    auth_url = 'https://ferma.ofd.ru/api/Authorization/CreateAuthToken'
    receipt_url = 'https://ferma.ofd.ru/api/kkt/cloud/receipt'

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.auth_token = None
        self.auth_token_expiry_date = None
        self.auth()

    def auth(self):
        data = {
            'Login': self.login,
            'Password': self.password
        }
        resp = requests.post(self.auth_url, headers={'Content-Type': 'application/json'}, data=json.dumps(data)).json()
        self.auth_token = resp.get('Data')['AuthToken']
        self.auth_token_expiry_date = resp.get('Data')['ExpirationDateUtc']

    def send_receipt(self, request):
        payload = json.dumps({
            'Request': request.data
        })
        headers = {
            'Content-Type': 'application/json'
        }
        params = {'AuthToken': self.auth_token}
        response = requests.request("POST", self.receipt_url, headers=headers, data=payload, params=params)
        return response


class FermaTestApi(FermaApi):
    auth_url = 'https://ferma-test.ofd.ru/api/Authorization/CreateAuthToken'
    receipt_url = 'https://ferma-test.ofd.ru/api/kkt/cloud/receipt'
