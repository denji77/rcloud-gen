import praw
import pandas as pd

class RedditScraper:
    def __init__(self, reddit_cfg):
        self.reddit = praw.Reddit(**reddit_cfg)
        self.reddit.read_only = True

    def scrape_subreddit(self, subreddit_name, post_limit=50, comments_per_post=20):
        print(f"Scraping r/{subreddit_name} (posts={post_limit}, comments/post={comments_per_post})...")
        subreddit = self.reddit.subreddit(subreddit_name)
        rows = []
        for post in subreddit.hot(limit=post_limit):
            try:
                post.comments.replace_more(limit=0)
                for comment in post.comments.list()[:comments_per_post]:
                    if not hasattr(comment, "body"):
                        continue
                    body = comment.body
                    if body in ("[deleted]", "[removed]"):
                        continue
                    rows.append({
                        "Title": post.title,
                        "Comment": body,
                        "Post_Score": post.score,
                        "Comment_Score": getattr(comment, "score", 0),
                        "Created_UTC": getattr(post, "created_utc", None)
                    })
            except Exception as e:
                print("Warning: error processing post:", e)
                continue
        df = pd.DataFrame(rows)
        print(f"Scraped {len(df)} comment rows.")
        return df