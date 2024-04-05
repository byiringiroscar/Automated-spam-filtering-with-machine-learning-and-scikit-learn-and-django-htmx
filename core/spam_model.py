from django.conf import settings
import string

from joblib import load
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


KNN_MODE_FILE = settings.BASE_DIR / 'data' / 'spam_model.joblib'
VECTORIZER_FILE = settings.BASE_DIR / 'data' / 'tfidf.joblib'

knn = load(KNN_MODE_FILE)
tfidf = load(VECTORIZER_FILE)

def preprocess(text):
  # remove punctuation and lowercase
  text = "".join([t.lower() for t in text if t not in string.punctuation])
  # tokenize
  tokens = text.split(" ") # 'color printing' == ['color', 'printing']

  # filter out stopwords
  return " ".join(t for t in tokens if t not in ENGLISH_STOP_WORDS)