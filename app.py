import streamlit as st
import json
from prawcore.exceptions import Redirect, NotFound, OAuthException
from scraper import scrape_subreddit

st.set_page_config(page_title="Reddit Image Scraper", layout="centered")
st.title("Reddit Image Scraper")


subreddit_input = st.text_input("Subreddit Name", value="malaysia", placeholder="e.g., pics, aww, malaysia")

sort_by_input = st.selectbox(
    "Sort posts by",
    options=['Hot', 'New', 'Top'],
    index=0
)

time_filter_input = 'all' 
if sort_by_input == 'Top':
    time_filter_input = st.selectbox(
        "Time range for 'Top' posts",
        options=['All', 'Year', 'Month', 'Week', 'Day', 'Hour'],
        index=0
    )

limit_input = st.number_input("Post Limit (1 page worth of posts is around 25)", min_value=10, max_value=1000, value=100, step=10,
                                help="The number of posts to search through.")


# --- Action Button ---
# The scraping logic is now tied to the click of this button.
if st.button("Scrape Images", type="primary"):
    if not subreddit_input:
        st.warning("Please enter a subreddit name.")
    else:
        sort_by = sort_by_input.lower()
        time_filter = time_filter_input.lower()
        
        with st.spinner(f"Scraping /r/{subreddit_input} (sorted by '{sort_by.capitalize()}')..."):
            try:
                scraped_data = scrape_subreddit(
                    subreddit_name=subreddit_input, 
                    post_limit=limit_input, 
                    sort_by=sort_by,
                    time_filter=time_filter
                )
                # Store results in session state to persist them across reruns
                st.session_state.posts = scraped_data
                st.session_state.subreddit = subreddit_input
                st.session_state.sort_method = sort_by.capitalize()
            
            # --- Error Handling ---
            except ValueError as e:
                st.error(e)
            except (Redirect, NotFound):
                st.error(f"Subreddit '/r/{subreddit_input}' not found or is private. Please check the name.")
            except OAuthException:
                st.error("Authentication failed. Check your Reddit API credentials in config.py.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

st.divider()

# --- Display Results Area ---
if 'posts' in st.session_state:
    if st.session_state.posts:
        posts = st.session_state.posts
        subreddit_name = st.session_state.subreddit
        sort_method = st.session_state.sort_method
        
        st.success(f"Found {len(posts)} image posts in /r/{subreddit_name} (sorted by '{sort_method}')!")

        json_data = json.dumps(posts, indent=4, ensure_ascii=False)
        
        st.download_button(
            label="Download results as JSON",
            data=json_data,
            file_name=f"{subreddit_name}_{sort_method.lower()}_images.json",
            mime="application/json"
        )
        
        # Display each post
        for post in posts:
            st.subheader(post['post_title'])
            st.image(post['image_url'], width='stretch')
            st.divider()
    else:
        # Handle the case where scraping was successful but found 0 images
        st.warning("Scraping complete, but no image posts were found for the given criteria.")
else:
    st.info("Results will be displayed here after you run the scraper.")
