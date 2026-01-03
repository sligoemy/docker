import pyodbc
from datetime import datetime
from config import Config
from logger import setup_logger

logger = setup_logger(__name__)

class Database:
    def __init__(self):
        self.connection_string = (
            f'DRIVER={{{Config.DB_DRIVER}}};'
            f'SERVER={Config.DB_SERVER};'
            f'DATABASE={Config.DB_NAME};'
            'Trusted_Connection=yes;'
        )
    
    def get_connection(self):
        """Create and return a database connection."""
        try:
            conn = pyodbc.connect(self.connection_string)
            return conn
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            raise
    
    def get_active_subscribers(self):
        """Fetch all active subscribers."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT Name, EmailAddress FROM users WHERE SubscriberStatus = 1"
                )
                subscribers = cursor.fetchall()
                logger.info(f"Retrieved {len(subscribers)} active subscribers")
                return subscribers
        except Exception as e:
            logger.error(f"Error fetching subscribers: {e}")
            return []
    
    def log_quote(self, quote_text, author):
        """Log a sent quote to the database."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO Quotes (Quote, Author, DATETIME) VALUES (?, ?, ?)",
                    (quote_text, author, datetime.now())
                )
                conn.commit()
                logger.info("Quote logged to database")
        except Exception as e:
            logger.error(f"Error logging quote: {e}")