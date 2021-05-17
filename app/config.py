class Configuration(object):
	DEBUG = True
	host = '0.0.0.0'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/flask'
