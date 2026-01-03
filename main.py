import schedule
import time
from config import Config
from quote_manager import QuoteManager
from logger import setup_logger

logger = setup_logger(__name__)

def main():
    """Main entry point for the quote service."""
    logger.info("=== Daily Quote Service Started ===")
    
    # Validate configuration
    if not all([
        Config.SENDER_EMAIL, 
        Config.SENDER_PASSWORD,
        Config.SMTP_SERVER
    ]):
        logger.error("Missing required email configuration in .env file")
        return
    
    quote_manager = QuoteManager()
    
    # Schedule daily job
    schedule.every().day.at(Config.DAILY_RUN_TIME).do(quote_manager.send_daily_quotes)
    #schedule.every(2).minutes.do(quote_manager.send_daily_quotes)
    logger.info(f"Scheduled daily quotes at {Config.DAILY_RUN_TIME}")
    
    # Run immediately on startup (optional - remove if not desired)
    # quote_manager.send_daily_quotes()
    
    # Keep the service running
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()