from starlette.config import Config


try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()


DATABASE_URL = config("DATABASE_URL", cast=str)
EMAIL_USERNAME = config("EMAIL_USERNAME", cast=str)
EMAIL_PASSWORD = config("EMAIL_PASSWORD", cast=str)
EMAIL_HOST = config("EMAIL_HOST", cast=str)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
ADMIN_EMAIL = config("ADMIN_EMAIL", cast=str)
ADMIN_PASSWORD = config("ADMIN_PASSWORD", cast=str)
SECRET_KEY = config("SECRET_KEY", cast=str)
ALGORITHM = config("ALGORITHM", cast=str)