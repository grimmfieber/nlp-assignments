import stanza

def load_model():
    try:
        stanza.download('en')
        nlp = stanza.Pipeline('en')
    except Exception as e:
        print(f"Error: Unable to load Stanza model. Reason: {e}")
        exit(1)
    return nlp

def process_text(nlp, text):
    doc = nlp(text)
    return [(ent.text, ent.type) for ent in doc.entities]