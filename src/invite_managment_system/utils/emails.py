from fastapi_mail import FastMail, MessageSchema  , MessageType
from ..config.email_config import email_config



class EmailUtil:
    def __init__(self):
        self.fast_mail = FastMail(email_config)
    async def send_email(self, recipients: str):
        message = MessageSchema(
            subject="Wedding Confirmation - Thank You for Your RSVP",
            recipients=[recipients],
            body="""
        Dear Valued Guest,

        Thank you for your RSVP to our wedding celebration! We are delighted that you will be joining us on our special day.

        We are looking forward to celebrating this joyous occasion with you.

        If you have any questions or need additional information before the event, please don't hesitate to contact us.

        Best regards
            """,
            subtype=MessageType.plain
        )
        await self.fast_mail.send_message(message)
