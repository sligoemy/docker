import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database
    DB_DRIVER = 'SQL Server'
    DB_SERVER = 'DESKTOP-HGTC7MT'
    DB_NAME = 'QUOTESUBSCRIBERS'
    
    # Email
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
    SENDER_EMAIL = os.getenv("EMAIL_ADDRESS")
    SENDER_PASSWORD = os.getenv("EMAIL_PASSWORD")
    
    # API
    QUOTE_API_URL = "https://zenquotes.io/api/random"
    API_TIMEOUT = 10
    
    # Logging
    LOG_DIR = "logs"
    LOG_FILE = "quote_service.log"
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    
    # Schedule
    DAILY_RUN_TIME = "07:00"