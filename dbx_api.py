import requests
import json
import datetime
from datetime import datetime

class dbx_api:
    @staticmethod
    def create_token(workspace_url, token, payload):
        api_url = f'{workspace_url}/api/2.0/token/create'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            token_value = response.json()['token_value']
            token_id = response.json()['token_info']['token_id']
            expiry_timestamp = datetime.datetime.fromtimestamp(response.json()['token_info']['expiry_time']/1000.0).replace(microsecond=0)
            return token_value, token_id, expiry_timestamp # response.text
        else:
            print(f"Error: {response.status_code}, Text: {response.text}")
            return None
        
    @staticmethod
    def put_secret(workspace_url, token, payload):
        api_url = f'{workspace_url}/api/2.0/secrets/put'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, Text: {response.text}")
            return None
        
    @staticmethod
    def update_job(workspace_url, token, payload):
        api_url = f'{workspace_url}/api/2.2/jobs/update'
        headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, Text: {response.text}")
            return None