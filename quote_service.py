import requests
from config import Config
from logger import setup_logger

logger = setup_logger(__name__)

class QuoteService:
    @staticmethod
    def fetch_random_quote():
        """Fetch a random quote from the API."""
        try:
            logger.info("Fetching random quote from API...")
            response = requests.get(Config.QUOTE_API_URL, timeout=Config.API_TIMEOUT)
            
            if response.status_code != 200:
                logger.warning(f"API returned status code {response.status_code}")
                return None
            
            data = response.json()
            
            if not isinstance(data, list) or len(data) == 0:
                logger.warning("Invalid API response format")
                return None
            
            quote_text = data[0].get("q")
            author = data[0].get("a")
            
            if quote_text:
                return f'"{quote_text}" - {author}'
            else:
                logger.warning("API returned incomplete quote data")
                return None
                
        except requests.exceptions.Timeout:
            logger.error("API request timed out")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error fetching quote: {e}")
            return None
