import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or b"\xa7N5\xf8\x86\x06'zz\xf0)g[\x0f\xc7\xd9"
    
    MONGODB_SETTINGS = { 'db' : 'Capstone_project'}