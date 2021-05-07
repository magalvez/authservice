import json
import requests

from app import AUTH_USER_SERVICE_URL
from util.response import DecimalEncoder


def auth_user(username, password):
    """
    Authenticate user
    :param username: user email. String, Ie. 'name@domain.com'
    :param password: user password. String, Ie. 'password'
    :return json_response: JSON object, Ie, {'status': 'OK', 'client_id': 1}
    """

    data = {
        'user_name': username,
        'password': password
    }

    response = requests.post(
        AUTH_USER_SERVICE_URL,
        data=json.dumps(data, cls=DecimalEncoder),
        headers={'Content-Type': 'application/json'})

    json_response = json.loads(response.text)
    return json_response
