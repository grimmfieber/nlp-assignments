import stanza as st
import feedparser as fp

#st.download('en')
nlp = st.Pipeline('en')
#doc = nlp("Barack Obama was born in Hawaii.")

nyt_rss = {
    "US": "https://rss.nytimes.com/services/xml/rss/nyt/Americas.xml", 
    "EU": "https://rss.nytimes.com/services/xml/rss/nyt/Europe.xml",
    "EAST": "https://rss.nytimes.com/services/xml/rss/nyt/MiddleEast.xml"
}

nyt_feed = {key: fp.parse(value) for key, value in nyt_rss.items()}
for region, feed in nyt_feed.items():
    print(f"\033[1;96m{'=' * 10} Region: {region} {'=' * 10}\033[0m")
    for entry in feed.entries:
        print("Title:", entry.title)
        print("Summary:", entry.summary)
        
        doc = nlp(entry.summary)
        
        print(doc.entities)
        print("-" * 40)
"""         print("Entities found:")
        for ent in doc.ents:
            print(ent.entities) """
        