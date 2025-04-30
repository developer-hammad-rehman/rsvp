from fastapi_mail import ConnectionConfig
from pydantic import SecretStr
from .env_config import EMAIL_USERNAME, EMAIL_PASSWORD, EMAIL_HOST, EMAIL_PORT


email_config = ConnectionConfig(
    MAIL_USERNAME=EMAIL_USERNAME,
    MAIL_PASSWORD=SecretStr(EMAIL_PASSWORD),
    MAIL_PORT=EMAIL_PORT,
    MAIL_SERVER=EMAIL_HOST,
    MAIL_FROM=EMAIL_USERNAME,
    MAIL_FROM_NAME="Invite Management System",
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    MAIL_STARTTLS=True,
)


