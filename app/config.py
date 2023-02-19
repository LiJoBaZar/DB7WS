class Config:
    SECRET_KEY = '4W!%FSEDllWeior'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'DB7WS'


config = {
    'development': DevelopmentConfig
}
