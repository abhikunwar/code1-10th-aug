import os
from config import DevelopmentConfig, ProductionConfig, TestingConfig
def run_app():
    env = os.getenv('ENV','development')
    print(f'Current environment: {env}')
    if env == 'development':
        config = DevelopmentConfig()
    elif env == 'production':
        config = ProductionConfig()
    elif env == 'testing':
        config = TestingConfig()
    else:
        raise ValueError("Invalid environment name")

    print(f"Running in {env} environment")
    print(f"DEBUG: {config.DEBUG}")
    print(f"TESTING: {config.TESTING}")
    print(f"DATABASE_URL: {config.DATABASE_URL}")
    print(f"secret_key: {config.SECRET_KEY}")
    print(f"log_level: {config.LOG_LEVEL}")
    print(f"API_END_POINT: {config.API_END_POINT}")
    print(f"LOG_FILE_PATH: {config.LOG_FILE_PATH}")
if __name__ == "__main__":
    run_app()   
