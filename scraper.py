import praw
import json
import os

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID", "SZa-Mt-8JLPXesFcBSOefg")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET", "8SVXsJPSrDVPZHQYkVLzUTPGAKBLjg")
USER_AGENT = "MySimpleScraper/0.1 by u/Lazy-Share-4347"

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

    print("Connection successful.")

if __name__ == "__main__":
    main()