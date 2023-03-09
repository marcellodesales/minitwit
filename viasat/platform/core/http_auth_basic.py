from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# https://pypi.org/project/Flask-HTTPAuth/
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

user = 'viasat'
pw = 'camper'
users = {
    user: generate_password_hash(pw)
}
