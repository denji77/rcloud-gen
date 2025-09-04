import os
from dotenv import load_dotenv
load_dotenv()
REDDIT_CONFIG = {
    "client_id": os.getenv("REDDIT_CLIENT_ID"),
    "client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "user_agent": os.getenv("REDDIT_USER_AGENT"),
}
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
BYTEZ_API_KEY = os.getenv("BYTEZ_API_KEY")
PERPLEXITY_BASE_URL = "https://api.perplexity.ai/chat/completions"