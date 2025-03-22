# Feature Engineering - TF-IDF Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer

def create_vectorizer():
    """Create a TF-IDF vectorizer."""
    return TfidfVectorizer(max_features=5000)

def transform_queries(vectorizer, queries):
    """Transform SQL queries into numerical features."""
    return vectorizer.transform(queries)
