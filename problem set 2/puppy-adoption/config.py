import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'sM\xe4\xfcF\xbf>9\x93\xdf\xfa\x98'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///pups.db'
   

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False