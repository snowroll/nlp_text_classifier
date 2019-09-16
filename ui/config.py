import os

class Config(object):  #用户配置选项
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'