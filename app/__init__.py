"""
Flask app module
"""
from os import environ
from flask import Flask

app = Flask(__name__)
app.config.from_object("default_config")

US_API_V1_URL = environ.get("US_API_V1_URL") or 'http://localhost:8200/userservice/api/v1.0'
AUTH_USER_SERVICE_URL = US_API_V1_URL + '/auth-user'
