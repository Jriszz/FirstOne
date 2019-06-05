from . import bp
from flask_httpauth import HTTPBasicAuth
from wechat_app.models import User
from flask import g
from wechat_app.utils.exceptions import BizException
auth = HTTPBasicAuth()
@auth.verify_password
def verify_user(token,password,user_name):
    if token == ''and user_name == '':
        return False
    if password == '':
        g.current_users = User.generate_token(token)
        g.token_used = True
        return user is not None
    users = User.query.filter_by(user_name=user_name).first()
    if users is None:
        return False
    g.token_used = False
    return User.check_password(password)

@bp.route(/token,methods=['GET','POST'])
def get_token():
    if g.current_users.is_anonoymous or g.token_used:
