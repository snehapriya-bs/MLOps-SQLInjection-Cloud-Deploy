import joblib
import os
from config import MODEL_PATH, VECTORIZER_PATH,VOCAB_PATH

# Load Model & Vectorizer
print("🔄 Loading model and vectorizer...")

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    # Force the vectorizer to use the same training vocabulary
    vocab = joblib.load(VOCAB_PATH)
    vectorizer.vocabulary_ = vocab  # Ensure feature consistency
    print(f"✅ Loaded Vectorizer Vocabulary Size: {len(vectorizer.get_feature_names_out())}")
    
except FileNotFoundError as e:
    print(f"❌ ERROR: {e}")
    exit(1)

    if vectorizer is None or not hasattr(vectorizer, "transform"):
        raise ValueError("❌ ERROR: Vectorizer was not loaded correctly.")

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
        queries = [q.strip() for q in file.readlines() if q.strip()]

    if not queries:
        print("❌ ERROR: No valid SQL queries found in the file.")
        return []

    # ✅ **Fix: Transform queries using the vectorizer**
    X_transformed = vectorizer.transform(queries)

    print(f"✅ Transformed Data Shape: {X_transformed.shape}")  # Debugging step

    # ✅ Use transformed input for prediction
    predictions = model.predict(X_transformed)

    results = [
        {"query": q, "prediction": "SQL Injection" if p == 1 else "Safe"}
        for q, p in zip(queries, predictions)
    ]

    print("✅ Predictions Complete!")
    return results

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
