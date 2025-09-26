import streamlit as st
import praw
from prawcore.exceptions import Redirect, NotFound, OAuthException

VALID_SORTS = ['hot', 'new', 'top']
VALID_TIME_FILTERS = ['all', 'day', 'hour', 'month', 'week', 'year']

try:
    CLIENT_ID = st.secrets["reddit"]["client_id"]
    CLIENT_SECRET = st.secrets["reddit"]["client_secret"]
    USER_AGENT = st.secrets["reddit"]["user_agent"]
except (KeyError, FileNotFoundError):
    # Handle case where secrets are not set, especially for initial local run
    CLIENT_ID = ""
    CLIENT_SECRET = ""
    USER_AGENT = ""

def scrape_subreddit(subreddit_name, post_limit, sort_by = 'hot', time_filter = 'all'):
    if not CLIENT_ID or not CLIENT_SECRET:
        raise ValueError("Reddit API credentials not found.")
    
    sort_by = sort_by.lower()
    if sort_by not in VALID_SORTS:
        raise ValueError(f"Invalid sort option: '{sort_by}'. Must be one of {VALID_SORTS}.")

    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
    )
    
    subreddit = reddit.subreddit(subreddit_name)
    _ = subreddit.display_name  

    submissions = None
    if sort_by == 'hot':
        submissions = subreddit.hot(limit=post_limit)
    elif sort_by == 'new':
        submissions = subreddit.new(limit=post_limit)
    elif sort_by == 'top':
        if time_filter.lower() not in VALID_TIME_FILTERS:
            raise ValueError(f"Invalid time filter: '{time_filter}'. Must be one of {VALID_TIME_FILTERS}.")
        submissions = subreddit.top(limit=post_limit, time_filter=time_filter.lower())
    
    image_posts = []
    for submission in submissions:
        if not submission.stickied and submission.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
            image_posts.append({
                "post_title": submission.title,
                "image_url": submission.url
            })
            
    return image_posts