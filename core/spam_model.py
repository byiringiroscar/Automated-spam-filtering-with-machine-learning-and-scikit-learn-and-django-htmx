from django.conf import settings
import string

from joblib import load
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


KNN_MODE_FILE = settings.BASE_DIR / 'data' / 'spam_model.joblib'
VECTORIZER_FILE = settings.BASE_DIR / 'data' / 'tfidf.joblib'