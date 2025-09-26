# Interactive Reddit Image Scraper

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://simplewebscraper.streamlit.app/) 

An interactive web application built with Python and Streamlit to scrape image posts from any public subreddit. Users can specify the subreddit, sort method (Hot, New, Top), and post limit, then view the results and download them as a JSON file.


## Features

-   **Interactive UI**: Clean and simple interface powered by Streamlit.
-   **Dynamic Scraping**: Scrape any public subreddit by name.
-   **Advanced Sorting**: Filter posts by 'Hot', 'New', or 'Top'.
-   **Time Filtering**: For 'Top' posts, filter by time ranges (All, Year, Month, Week, etc.).
-   **Data Export**: Download the scraped data (post title, image URL) as a formatted JSON file.
-   **Secure**: API credentials are not hardcoded. They are managed securely using Streamlit's built-in secrets management.
-   **Modular Code**: The scraping logic is separated from the user interface for better maintainability.

## Project Structure

The project is structured to separate the data scraping logic from the web interface.

.
├── .streamlit/
│ └── secrets.toml # Local API credentials (git-ignored)
├── .gitignore # Files to be ignored by Git
├── README.md # This file
├── app.py # The Streamlit web app (UI)
├── scraper.py # The module with the scraping logic
└── requirements.txt # Python dependencies


## Technology Stack

-   **Backend**: Python
-   **Web Framework**: Streamlit
-   **Reddit API Wrapper**: PRAW (Python Reddit API Wrapper)
-   **Hosting**: Streamlit Community Cloud

## Setup and Local Installation

Follow these steps to run the application on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   Git

### 2. Get Reddit API Credentials

You need Reddit API credentials to use this scraper.

1.  Go to [Reddit's App Preferences](https://www.reddit.com/prefs/apps).
2.  Scroll down and click "**create another app...**".
3.  Fill out the form:
    -   **name**: `MyStreamlitScraper` (or any name)
    -   **type**: `script`
    -   **redirect uri**: `http://localhost:8080`
4.  Click "**create app**". You will get a **Client ID** (a string of characters under the app name) and a **Client Secret**.

### 3. Clone and Set Up the Project

#### Clone the repository
git clone https://github.com/yikyaooo/SimpleWebScraper.git
cd SimpleWebScraper

#### Create and activate a virtual environment (recommended)
#### Windows
python -m venv venv
venv\Scripts\activate

#### macOS / Linux
python3 -m venv venv
source venv/bin/activate

#### Install the required dependencies
pip install -r requirements.txt

### 4. Configure Local Secrets
To run the app locally, you need to provide your API credentials in a local secrets file. This file is intentionally ignored by Git to keep your keys safe.
Create a new folder named .streamlit in the project's root directory.
Inside the .streamlit folder, create a new file named secrets.toml.
Open secrets.toml and add your credentials in the following format:

#### .streamlit/secrets.toml

[reddit]
client_id = "YOUR_CLIENT_ID_HERE"
client_secret = "YOUR_CLIENT_SECRET_HERE"
user_agent = "MyStreamlitScraper/1.0 by YourUsername"

To run the website type this on the terminal
streamlit run app.py
