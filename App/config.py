import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if SECRET_KEY == None:
        SECRET_KEY = '447cc3d7257853eafabc30fd9c373ff8'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    if SQLALCHEMY_DATABASE_URI == None:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'noreplyb77988443@gmail.com'
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')