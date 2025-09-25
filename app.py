import streamlit as st
import json
import os

# --- Configuration ---
JSON_FILE = "output.json"

def display_posts():
    """Loads data from the JSON file and displays it on the page."""
    st.set_page_config(page_title="Reddit Image Feed", layout="centered")
    st.title("Reddit Image Scraper Feed")
    st.markdown("Displaying images scraped from Reddit.")

    # Check if the JSON file exists
    if not os.path.exists(JSON_FILE):
        st.error(f"Error: The data file '{JSON_FILE}' was not found.")
        st.info("Please run the `scraper.py` script first to generate the data.")
        return

    # Load the data from the JSON file
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            posts = json.load(f)
    except json.JSONDecodeError:
        st.error(f"Error: Could not decode JSON from '{JSON_FILE}'. The file might be corrupted or empty.")
        return
    except Exception as e:
        st.error(f"An unexpected error occurred while reading the file: {e}")
        return

    if not posts:
        st.warning("No image posts were found in the data file.")
        return

    # Display each post
    for post in posts:
        st.subheader(post['post_title'])
        st.image(post['image_url'], use_container_width=True)
        st.divider()

if __name__ == "__main__":
    display_posts()