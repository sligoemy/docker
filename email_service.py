import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config
from logger import setup_logger

logger = setup_logger(__name__)

class EmailService:
    @staticmethod
    def send_email(recipient_email, recipient_name, quote):
        """Send a daily quote email to a recipient."""
        try:
            msg = MIMEMultipart()
            msg['From'] = Config.SENDER_EMAIL
            msg['To'] = recipient_email
            msg['Subject'] = "Your Daily Dose"
            
            body = (
                f"Hello {recipient_name},\n\n"
                f"Here's your Daily Quote:\n{quote}\n\n"
                f"Have a great day!\n\n"
                f"— Daily Quotes Bot"
            )
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP_SSL(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
                server.login(Config.SENDER_EMAIL, Config.SENDER_PASSWORD)
                server.send_message(msg)
            
            logger.info(f"Email sent successfully to {recipient_email}")
            return True
            
        except Exception as e:
            logger.error(f"Error sending email to {recipient_email}: {e}")
            return False
