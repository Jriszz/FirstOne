from . import bp
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
@auth.verify_password
def verify_user(username,password):
    if