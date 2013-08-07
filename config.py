#coding=utf8
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

#DEBUG = True
FRAGMENT_PER_PAGE = 10

# -- Flask - SQLALCHEMY --
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASS = 'YourPasswd'
MYSQL_DB = 'myblogdb'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' % (MYSQL_USER, MYSQL_PASS, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
