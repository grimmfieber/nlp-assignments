import spacy

def load_model():
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print("Error: The SpaCy language model 'en_core_web_sm' is not installed. Please install it with:")
        print("    python -m spacy download en_core_web_sm")
        exit(1)
    return nlp

def process_text(nlp, text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]