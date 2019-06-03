from .import bp
from flask import jsonify
@bp.route('/index',methods=['GET','POST'])
def index():
    return jsonify({'val':'1'})