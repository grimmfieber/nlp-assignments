# Named Entity Recognition on NYT RSS Feeds

This project performs Named Entity Recognition (NER) on RSS feeds from The New York Times using SpaCy or Stanza as NLP backends. The script parses the RSS feeds, processes each article's summary to extract named entities, and displays them in a categorized format based on the region of the feed. Users can choose the NLP backend (SpaCy or Stanza) via a command-line argument.


## Features

- **RSS Feed Parsing**: Parses RSS feeds from The New York Times for various regions (US, EU, Middle East).
- **Named Entity Recognition**: Supports both SpaCy and Stanza as NLP backends to identify entities such as names, organizations, locations, dates, etc., in each article summary.
- **Formatted Output**: Organizes and displays entities found for each feed with clear headings and separators.
- **Dynamic NLP Backend Selection:** Allows users to specify either SpaCy or Stanza as the NLP backend when running the script.

## Folder Structure

📦src
 ┣ 📂nlp_backends
 ┃ ┣ 📜spacy_nlp.py
 ┃ ┗ 📜stanza_nlp.py
 ┣ 📂utils
 ┃ ┗ 📜feed_parser.py
 ┗ 📜 main. py

## Requirements

- Python 3.6 or higher
- See `requirements.txt` for dependencies

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ner-nyt-rss.git
   cd ner-nyt-rss

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv [env-name]
   source myenv/bin/activate  # For Linux/macOS
   myenv\Scripts\activate     # For Windows

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Download the SpaCy language model (if not already installed):**
   ```bash
   python -m spacy download en_core_web_sm

5. **Download the Stanza language model (if not already installed):**
   ```bash
   // from python interpreter
   >>> import stanza
   >>> stanza.download('en') # download English model
   >>> nlp = stanza.Pipeline('en') # initialize English neural pipeline
   >>> doc = nlp("Barack Obama was born in Hawaii.") # run annotation over a sentence

6. **Run the application with selected backend:**
   ```bash
   python main.py [backend]
   // where backend can be "stanza" or "stacy"

7. **Docs:**
   https://stanfordnlp.github.io/stanza/
   https://spacy.io/usage