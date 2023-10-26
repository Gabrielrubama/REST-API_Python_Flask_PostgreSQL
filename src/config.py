from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')  # pylint: disable=not-callable


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
