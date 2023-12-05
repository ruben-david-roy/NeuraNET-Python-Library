import requests
import json

class client:
    def __init__(self, api_key, mode='chat'):
        if not api_key:
            raise ValueError("API key must be provided.")
        
        self.api_key = api_key
        self.mode = mode
        self.url = f'https://neuranet-ai.com/api/v1/{mode}'

    def generate(self, data, model=None):
        if self.mode == 'chat' and not model:
            raise ValueError("Model must be specified for chat mode.")

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

        if self.mode == 'chat':
            payload = {
                "settings": {"model": model},
                "conversation": {"history": data}
            }
        elif self.mode == 'image':
            payload = {
                "content": {"model": model, "prompt": data}
            }
        else:
            raise ValueError("Invalid mode. Mode should be either 'chat' or 'image'.")

        try:
            response = requests.post(self.url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            if self.mode == 'chat':
                return response.json()['choices'][0]['text']
            elif self.mode == 'image':
                return response.json()['result'][0]['result-url']
        except requests.exceptions.HTTPError as http_err:
            if http_err.response.status_code == 403:
                raise PermissionError("Incorrect API key provided.")
            else:
                raise ConnectionError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise ConnectionError(f"Error occurred during request: {req_err}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")
