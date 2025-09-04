import argparse
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

from config import REDDIT_CONFIG, PERPLEXITY_API_KEY, BYTEZ_API_KEY
from scraper import RedditScraper, PerplexityAPI, BytezMaskGenerator, create_circle_mask, clean_text, pil_to_wordcloud_mask

def generate_wordcloud_with_ai_mask(subreddit_name, post_limit=50, comments_per_post=20,
                                    mask_width=800, mask_height=400):
    reddit_scraper = RedditScraper(REDDIT_CONFIG)
    perplexity_api = PerplexityAPI(PERPLEXITY_API_KEY)
    bytez_gen = BytezMaskGenerator(BYTEZ_API_KEY)

    df = reddit_scraper.scrape_subreddit(subreddit_name, post_limit, comments_per_post)
    if df.empty:
        print("No data scraped.")
        return None, None

    df["cleaned"] = (df["Title"].astype(str) + " " + df["Comment"].astype(str)).apply(clean_text)
    combined_sample = " ".join(df["cleaned"].head(10).tolist())

    print("Requesting Perplexity for topic stopwords...")
    ai_stopwords = perplexity_api.generate_topic_stopwords(subreddit_name, combined_sample)
    print("Perplexity stopwords:", ai_stopwords)

    all_stopwords = set(STOPWORDS)
    all_stopwords.update(["amp", "like", "im", "just", "know", "get", "would", "could", "really"])
    all_stopwords.update(ai_stopwords)

    print("Requesting Bytez for mask image...")
    symbol = perplexity_api.get_subreddit_symbol(subreddit_name)
    pil_mask_img = bytez_gen.generate_mask(symbol, width=mask_width, height=mask_height)

    if pil_mask_img is None:
        print("Using fallback circle mask.")
        mask_array = create_circle_mask(mask_width, mask_height)
        mask_desc = "circle_fallback"
        pil_mask_for_save = Image.fromarray(mask_array)
    else:
        mask_array = pil_to_wordcloud_mask(pil_mask_img)
        mask_desc = "bytez_mask"
        pil_mask_for_save = pil_mask_img

    text = " ".join(df["cleaned"].tolist())
    wc = WordCloud(
        width=mask_width,
        height=mask_height,
        background_color="white",
        stopwords=all_stopwords,
        max_words=250,
        mask=mask_array,
        colormap="viridis",
        random_state=42,
        prefer_horizontal=0.7
    ).generate(text)

    # Show results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
    ax1.imshow(pil_mask_for_save, cmap="gray")
    ax1.set_title(f"Mask ({mask_desc})")
    ax1.axis("off")
    ax2.imshow(wc, interpolation="bilinear")
    ax2.set_title(f"r/{subreddit_name} Word Cloud")
    ax2.axis("off")
    plt.tight_layout()
    plt.show()

    # Save outputs
    df.to_csv(f"reddit_{subreddit_name}_scraped.csv", index=False, encoding="utf-8")
    wc.to_file(f"reddit_{subreddit_name}_wordcloud.png")
    pil_mask_for_save.convert("RGB").save(f"reddit_{subreddit_name}_mask.png")

    print("Saved: CSV, mask, and word cloud PNGs.")
    return df, wc


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a word cloud from a subreddit with AI-enhanced mask.")
    parser.add_argument(
        "--subreddit",
        type=str,
        required=True,
        help="Name of the subreddit to scrape and generate word cloud for"
    )
    parser.add_argument(
        "--post_limit",
        type=int,
        default=50,
        help="Number of posts to scrape (default: 50)"
    )
    parser.add_argument(
        "--comments_per_post",
        type=int,
        default=20,
        help="Number of comments to scrape per post (default: 20)"
    )
    args = parser.parse_args()

    generate_wordcloud_with_ai_mask(
        subreddit_name=args.subreddit,
        post_limit=args.post_limit,
        comments_per_post=args.comments_per_post
    )