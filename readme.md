# Reddit Wordcloud AI

Generate AI-powered word clouds from Reddit posts and comments.

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/reddit-wordcloud-ai.git
cd reddit-wordcloud-ai
```


Create and activate a virtual environment (recommended):
```
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

Install dependencies:
```
pip install -r requirements.txt
```
Create a .env file in the project root with your API keys:
```
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=reddit-wordcloud:v1.0 (by u/your_username)

PERPLEXITY_API_KEY=your_perplexity_api_key
BYTEZ_API_KEY=your_bytez_api_key

```

##Usage

##Run the script with the required --subreddit flag and optional parameters:
```
python main.py --subreddit cars --post_limit 10 --comments_per_post 12
```

Arguments:
--subreddit (required): Name of the subreddit to scrape and generate word cloud for
--post_limit (optional, default=50): Number of posts to scrape
--comments_per_post (optional, default=20): Number of comments to scrape per post

Project Structure:
```
reddit-wordcloud-ai/
├── main.py                 # Entry point script
├── config.py               # Loads environment variables
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed)
├── scraper/                # Package with modular scraper and AI code
│   ├── __init__.py
│   ├── reddit_scraper.py
│   ├── perplexity_api.py
│   ├── bytez_mask.py
│   └── utils.py
├── assets/                 # (Optional) saved images and outputs
└── README.md

```

Notes:
Make sure your Reddit API credentials are for a script app and have read-only access.
Perplexity and Bytez APIs require valid API keys.
The script saves outputs in the current directory:
```
reddit_<subreddit>_scraped.csv
reddit_<subreddit>_wordcloud.png
reddit_<subreddit>_mask.png
```
## Acknowledgments

- [PRAW](https://praw.readthedocs.io/en/latest/) for Reddit API  
- [WordCloud](https://github.com/amueller/word_cloud) Python library  
- [Perplexity AI](https://www.perplexity.ai/) for stopwords and symbol generation  
- [Bytez](https://www.bytez.ai/) for AI-generated mask images
