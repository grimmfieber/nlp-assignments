import spacy
import feedparser

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

rss_bbc_europe = "https://feeds.bbci.co.uk/news/world/europe/rss.xml"
rss_feed = feedparser.parse(rss_bbc_europe)


if rss_feed.status == 200:
    for entry in rss_feed.entries:
        print("Title: ", entry.title)
        #print("Link:" , entry.link)
        print("Summary: ", entry.summary, "\n")
        doc = nlp(entry.summary)
        print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
        print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
        for entity in doc.ents:
            print(entity.text, entity.label_)
        print("\n-----------------\n")       
else:
    print("Failed to get RSS feed. Status code:", rss_feed.status)



