import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = 'dev'
    DEBUG: bool = True
    ROOT_DIR = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2])
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000
    JWT_SECRET_KEY: str = "secret"
    JWT_ALGORITHM: str = "HS256"
    CLIENT_MOCK_URL = "https://www.mocky.io/v2/5808862710000087232b75ac"
    POLICY_MOCK_URL = "https://www.mocky.io/v2/580891a4100000e8242b75c5"
    # CORS
    CORS_ORIGINS = [
        f"http://{APP_HOST}:{APP_PORT}",
    ]
    CORS_ALLOW_CREDENTIALS = False
    CORS_METHODS = ["GET"]
    CORS_HEADERS = [
        "Accept",
        "Accept-Encoding",
        "Authorization",
        "Content-Type"
    ]


class DevConfig(Config):
    pass


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    pass


def get_config():
    environment = "dev"
    config_type = {
        "dev": DevConfig(),
        "pre": LocalConfig(),
        "pro": ProductionConfig(),
    }

    return config_type[environment]


config = get_config()
