import pickle
import os

vectorizer = None
model = None

def load_model():
    global vectorizer, model
    if vectorizer is None:
        with open('vectorizer.pkl', 'rb') as f:
            vectorizer = pickle.load(f)
    if model is None:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)

def predict_query(query):
    load_model()
    if isinstance(query, str):
        # Handle single query
        query_transformed = vectorizer.transform([query])
        prediction = model.predict(query_transformed)[0]
        probability = model.predict_proba(query_transformed)[0][1]
        return prediction, probability
    elif isinstance(query, list):
        # Handle batch prediction (if DataFrame is passed)
        query_transformed = vectorizer.transform(query)
        predictions = model.predict(query_transformed)
        probabilities = model.predict_proba(query_transformed)[:, 1]
        return list(zip(predictions, probabilities))
