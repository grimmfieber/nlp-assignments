import feedparser
import requests

def parse_feeds(rss_urls):
    feeds = {}
    for region, url in rss_urls.items():
        try:
            response = requests.head(url, timeout=5)
            response.raise_for_status()
            feeds[region] = feedparser.parse(url)
        except requests.RequestException as e:
            print(f"Error: Unable to access RSS feed for region {region} at {url}. Reason: {e}")
        except Exception as e:
            print(f"Unexpected error occurred while parsing feed for region {region}: {e}")
    return feeds