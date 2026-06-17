import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer



stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def light_clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    return " ".join(text.split())


def heavy_clean(text):
    text = light_clean(text)

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)