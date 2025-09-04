<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Reddit Wordcloud AI</title>
<style>
    body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; background-color: #f9f9f9; color: #333; }
    h1, h2, h3 { color: #222; }
    pre { background-color: #eee; padding: 10px; border-radius: 5px; overflow-x: auto; }
    code { font-family: monospace; }
    ul { margin-top: 0; }
    a { color: #1a0dab; text-decoration: none; }
    a:hover { text-decoration: underline; }
</style>
</head>
<body>

<h1>Reddit Wordcloud AI</h1>

<h2>Installation</h2>

<p>Clone the repository:</p>
<pre><code>git clone https://github.com/yourusername/reddit-wordcloud-ai.git
cd reddit-wordcloud-ai</code></pre>

<p>Create and activate a virtual environment (recommended):</p>
<pre><code>python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate</code></pre>

<p>Install dependencies:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<p>Create a <code>.env</code> file in the project root with your API keys:</p>
<pre><code>REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=reddit-wordcloud:v1.0 (by u/your_username)

PERPLEXITY_API_KEY=your_perplexity_api_key
BYTEZ_API_KEY=your_bytez_api_key</code></pre>

<h2>Usage</h2>
<p>Run the script with the required <code>--subreddit</code> flag and optional parameters:</p>
<pre><code>python main.py --subreddit cars --post_limit 10 --comments_per_post 12</code></pre>

<h3>Arguments</h3>
<ul>
    <li><code>--subreddit</code> (required): Name of the subreddit to scrape and generate word cloud for</li>
    <li><code>--post_limit</code> (optional, default=50): Number of posts to scrape</li>
    <li><code>--comments_per_post</code> (optional, default=20): Number of comments to scrape per post</li>
</ul>

<h2>Project Structure</h2>
<pre><code>reddit-wordcloud-ai/
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
└── README.md</code></pre>

<h2>Notes</h2>
<ul>
    <li>Make sure your Reddit API credentials are for a script app and have read-only access.</li>
    <li>Perplexity and Bytez APIs require valid API keys.</li>
    <li>The script saves outputs in the current directory:
        <ul>
            <li>reddit_<subreddit>_scraped.csv</li>
            <li>reddit_<subreddit>_wordcloud.png</li>
            <li>reddit_<subreddit>_mask.png</li>
        </ul>
    </li>
</ul>

<h2>License</h2>
<p>MIT License</p>

<h2>Acknowledgments</h2>
<ul>
    <li><a href="https://praw.readthedocs.io/en/latest/" target="_blank">PRAW</a> for Reddit API</li>
    <li><a href="https://github.com/amueller/word_cloud" target="_blank">WordCloud</a> Python library</li>
    <li><a href="https://www.perplexity.ai/" target="_blank">Perplexity AI</a> for stopwords and symbol generation</li>
    <li><a href="https://www.bytez.ai/" target="_blank">Bytez</a> for AI-generated mask images</li>
</ul>

</body>
</html>
