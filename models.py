# -*- coding: utf-8 -*-
from .database import Model,Column,db
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as serializer
from flask_login import UserMixin
from flask import current_app
class User(Model,UserMixin):
    __tablename__ = 'user'
    user_id  = Column(db.SmallInteger,nullable=False,primary_key=True,comment='用户Id')
    user_name = Column(db.String(255),nullable=False,comment='用户姓名')
    user_password = Column(db.String(128),nullable=False,comment='用户密码')
    create_time = Column(db.DateTime,nullable=False,default=db.func.now(),comment='创建时间')
    update_time = Column(db.DateTime,nullable=False,default=db.func.now(),comment='更新时间')
    def __repr__(self):
        return "This is %r Table" % self.user_name

    @property
    def user_name(self):
        return self.user_name
    @proprty
    def user_password(self):
        raise AttributeError('password is not a readable attribute')
    @user_password.setter
    def generate_password(self,password):
        self.user_password=generate_password_hash(password)
    def check_password(self,password):
        check_password_hash(self.user_password,password)
    def generate_token(self):
        s = serializer(current_app.config['SERCRET_KEY'],EXPIRES_IN=1800)
        return s.dumps({'token_value':self.id})
    def confirm_token(self,token):
        s = serializer(current_app.config['SERCRET_KEY'])
        try:
            res = s.loads(token)
        except:
            return False
        if s.get('token_value') != self.id:
            return False
        return True
class HouseInfo(Model):
    __tablename__ = 'houseinfo'
    house_id = Column(db.Integer,nullable=False,primary_key=True)
    house_address = Column(db.String(255),nullable=False)
    house_areas = Column(db.String(64),nullable=False)
    house_use_lifetime=Column(db.SmallInteger,nullable=False)
    create_time = Column(db.DateTime, nullable=False, default=db.func.now(), comment='创建时间')
    update_time = Column(db.DateTime, nullable=False, default=db.func.now(), comment='更新时间')
    def __repr__(self):
        return "This is %r Table" % self.house_id

    @property
    def user_name(self):
        return self.user_name
    @user_name.setter
    def set_house_address(self,address):
        self.house_address = address

class RecruitInfo(Model):
    __tablename__ = 'recruitinfo'
    position_id=Column(db.Integer,nullable=False,primary_key=True,autoincrement=True,comment='职位编号')
    position = Column(db.String(64),nullable=False,comment='职位')
    position_requirements = Column(db.String(255),comment='职位要求')
    salary = Column(db.String,nullable=False,comment='薪水')
    create_time = Column(db.DateTime, nullable=False, default=db.func.now(), comment='创建时间')
    update_time = Column(db.DateTime, nullable=False, default=db.func.now(), comment='更新时间')
