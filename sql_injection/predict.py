#Loads Model & Predicts from .sql Files
import joblib
import os
from config import MODEL_PATH, VECTORIZER_PATH

#Load Model & Vectorizer
print("🔄 Loading model and vectorizer...")

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    # Debug: Ensure vectorizer is loaded correctly
    if vectorizer is None:
        raise ValueError("❌ ERROR: Loaded vectorizer is None.")
    
    print(f"✅ Vectorizer Loaded Successfully: {type(vectorizer)}")

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
        queries = file.readlines()

    print("🔄 Making predictions...")
    predictions = [
        {"query": q.strip(), "prediction": "SQL Injection" if model.predict(vectorizer.transform([q]))[0] == 1 else "Safe"}
        for q in queries
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

