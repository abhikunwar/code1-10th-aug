class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URL = 'sqlite:///:memory:'
    
class ProductionConfig(Config):
    DATABASE_URL = 'mysql://user@localhost/foo'
    LOG_LEVEL = 'CRITICAL'
    LOG_FILE_PATH = 'abc'
    API_END_POINT = "/prod"
    SECRET_KEY = 'dsbvjklhe'
class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'CRITICAL'
    LOG_FILE_PATH = 'abc'
    API_END_POINT = "/development"
    SECRET_KEY = 'dsbvjklhe'

class TestingConfig(Config):
    TESTING = True 
    LOG_LEVEL = 'CRITICAL' 
    LOG_FILE_PATH = 'abc'  
    API_END_POINT = "/testing" 
    SECRET_KEY = 'dsbvjklhe'
