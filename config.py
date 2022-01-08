import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xe7\x84\xc5\x0c\xce0\x13c*\x14t\x12\xb0\x88\t\xa03%'

    MONGODB_SETTINGS = {'db' : 'UTA_Enrollment', 'host':'localhost', 'port' : 27888, 'USERNAME' : 'mongoadmin' , 'PASSWORD' : 'secret'}


    