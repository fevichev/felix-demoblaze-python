import base64

import requests
from requests import HTTPError

from definitions import URL, HEADER_API

uri = '/login'
baseServerUrl = URL.get('API')


def get_auth_token_api(session):
    username = session.get('username')
    password = get_encode_to_base64(session.get('password'))
    json_body = '{\"username\":\"' + username + '\",\"password\":\"' + password + '\"}'

    try:
        response = requests.post(baseServerUrl + uri, data=json_body, headers=HEADER_API)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    else:
        print('Success!')

        return response.text.split(': ')[1].replace('"\n', '')


def get_encode_to_base64(convert_string):
    message_bytes = convert_string.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')
