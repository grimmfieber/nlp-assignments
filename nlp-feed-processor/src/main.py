import sys
from utils.feed_parser import parse_feeds

if len(sys.argv) < 2 or sys.argv[1] not in ["spacy", "stanza"]:
    print("Usage: python main.py <nlp_backend>")
    print("Choose <nlp_backend> as 'spacy' or 'stanza'")
    exit(1)

nlp_backend = sys.argv[1]

if nlp_backend == "spacy":
    from nlp_backends.spacy_nlp import load_model, process_text
elif nlp_backend == "stanza":
    from nlp_backends.stanza_nlp import load_model, process_text

nlp = load_model()

nyt_rss = {
    "US": "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml", 
    "EU": "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml",
    "EAST": "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml"
}

def process_entries(region, feed):
    print(f"\033[1;96m{'=' * 10} Region: {region} {'=' * 10}\033[0m")
    for entry in feed.entries:
        print("Title:", entry.title)
        print("Summary:", entry.summary)
        
        entities = process_text(nlp, entry.summary)
        
        if entities:
            print("Entities found:")
            for text, label in entities:
                print(text, label)
        else:
            print("No entities found.")
        print("-" * 40)

def main():
    feeds = parse_feeds(nyt_rss)
    for region, feed in feeds.items():
        process_entries(region, feed)

if __name__ == "__main__":
    main()
