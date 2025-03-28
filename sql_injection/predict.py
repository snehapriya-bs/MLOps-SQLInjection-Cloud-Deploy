# Loads Model & Predicts from .sql Files

import os
import sys
import joblib
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from sql_injection.config.core import MODEL_PATH, VECTORIZER_PATH

# Load Model & Vectorizer
print("🔄 Loading model and vectorizer...")

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("✅ Model & Vectorizer Loaded Successfully.")
except FileNotFoundError as e:
    print(f"❌ ERROR: {e}")
    exit(1)

def predict_from_sql_file(filepath):
    """Predict SQL injection from a .sql file."""
    if not os.path.exists(filepath):
        print(f"❌ ERROR: File {filepath} not found!")
        return []

    print(f"📄 Reading SQL file: {filepath}")
    with open(filepath, "r", encoding="utf-8") as file:
        queries = [q.strip() for q in file.readlines() if q.strip()]

    print("🔄 Making predictions...")

    # ✅ Transform the queries using the trained vectorizer
    X_transformed = vectorizer.transform(queries)

    # ✅ Get the probability predictions
    y_pred_proba = model.predict_proba(X_transformed)

    # ✅ Debug: Print confidence scores
    for query, prob in zip(queries, y_pred_proba):
        print(f"🔍 Query: {query}")
        print(f"   🟢 Probability Safe: {prob[0]:.4f}, 🔴 Probability SQL Injection: {prob[1]:.4f}")

    # ✅ Make final predictions based on probability threshold
    predictions = [
        {"query": q, "prediction": "SQL Injection" if p[1] > 0.5 else "Safe"}
        for q, p in zip(queries, y_pred_proba)
    ]

    print("✅ Predictions Complete!")
    return predictions

# ✅ Run Prediction Automatically When Script is Executed
if __name__ == "__main__":
    test_file = "data/test_sql_file.sql"  # Ensure this file exists!

    if not os.path.exists(test_file):
        print(f"❌ ERROR: Test file '{test_file}' not found! Please provide a valid SQL file.")
        exit(1)

    result = predict_from_sql_file(test_file)

    if not result:
        print("❌ No predictions were made. Check for errors above.")
    else:
        print("🔎 Prediction Results:")
        for res in result:
            print(res)
