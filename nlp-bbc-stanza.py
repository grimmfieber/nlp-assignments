import stanza
import feedparser
stanza.download('en') # download English model
nlp = stanza.Pipeline('en') # initialize English neural pipeline
#doc = nlp("Barack Obama was born in Hawaii.") # run annotation over a sentence

rss_bbc_europe = "https://feeds.bbci.co.uk/news/world/europe/rss.xml"
rss_feed = feedparser.parse(rss_bbc_europe)


if rss_feed.status == 200:
    for entry in rss_feed.entries:
        print("Title: ", entry.title)
        #print("Link:" , entry.link)
        print("Summary: ", entry.summary, "\n")
        doc = nlp(entry.summary)
        print(doc.entities)
        print("\n-----------------\n")       
else:
    print("Failed to get RSS feed. Status code:", rss_feed.status)
