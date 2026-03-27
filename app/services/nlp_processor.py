import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str):
    doc = nlp(text)

    sentences = [sent.text for sent in doc.sents]

    cleaned_tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and not token.is_punct
    ]

    return {
        "sentences": sentences,
        "tokens": cleaned_tokens
    }