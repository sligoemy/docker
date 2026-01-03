from database import Database
from quote_service import QuoteService
from email_service import EmailService
from logger import setup_logger

logger = setup_logger(__name__)

class QuoteManager:
    def __init__(self):
        self.db = Database()
        self.quote_service = QuoteService()
        self.email_service = EmailService()
    
    def send_daily_quotes(self):
        """Send daily quotes to all active subscribers."""
        subscribers = self.db.get_active_subscribers()
        logger.info(f"Sending quotes to {len(subscribers)} subscribers...")
        
        success_count = 0
        
        for name, email in subscribers:
            quote = self.quote_service.fetch_random_quote()
            
            if quote:
                if self.email_service.send_email(email, name, quote):
                    success_count += 1
            else:
                logger.warning(f"Could not fetch quote for {name}")
        
        logger.info(f"Quote delivery complete: {success_count}/{len(subscribers)} successful")
