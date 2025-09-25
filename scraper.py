import praw
import json
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT



SUBREDDIT_NAME = "malaysia"
POST_LIMIT = 250
OUTPUT_FILENAME = "output.json"


def main():
    """Main function to run the scraper."""
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Error: Reddit API credentials not found.")
        print("Please set the REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET environment variables.")
        return

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
    )

    print(f"Connecting to Reddit and scraping /r/{SUBREDDIT_NAME}...")
    subreddit = reddit.subreddit(SUBREDDIT_NAME)

    image_posts = []
    for submission in subreddit.hot(limit=POST_LIMIT):

        if not submission.stickied and submission.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
            image_posts.append({
                "post_title": submission.title,
                "image_url": submission.url
            })
            print(f"Found image post: {submission.title[:50]}...")

    print(f"\nScraping complete. Found {len(image_posts)} image posts.")

if __name__ == "__main__":
    main()