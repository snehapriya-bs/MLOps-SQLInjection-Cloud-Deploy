#Trains & Saves the Model
import sys
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import StackingClassifier, GradientBoostingClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score
from data_manager import load_dataset, save_model
from features import create_vectorizer
from config import MODEL_PATH, VECTORIZER_PATH


# Dynamically adjust sys.path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

print("✅ Loading dataset...")
df = load_dataset()
X, y = df["Query"], df["Label"]

# Vectorize SQL queries
vectorizer = create_vectorizer()

# Debug: Ensure vectorizer is not None
if vectorizer is None:
    raise ValueError("❌ ERROR: `create_vectorizer()` returned None.")

print(f"✅ Vectorizer Initialized: {type(vectorizer)}")
X_vectorized = vectorizer.fit_transform(X)

# Debug: Ensure data is not empty
if X_vectorized.shape[0] == 0:
    raise ValueError("❌ ERROR: Vectorized data is empty. Check input queries.")

print(f"✅ Vectorized Data Shape: {X_vectorized.shape}")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42, stratify=y)

print(f"✅ Training Data: {X_train.shape}, Testing Data: {X_test.shape}")

# Define Base Models
gbm = GradientBoostingClassifier(n_estimators=100)
adaboost = AdaBoostClassifier(n_estimators=100)
xgb = XGBClassifier(n_estimators=100, eval_metric="logloss")
lgbm = LGBMClassifier(n_estimators=100)

# Stacking Classifier
stacking_clf = StackingClassifier(
    estimators=[
        ("gbm", gbm),
        ("adaboost", adaboost),
        ("xgb", xgb),
        ("lgbm", lgbm),
    ],
    final_estimator=LogisticRegression(solver="liblinear"),
    stack_method="predict_proba",
)

print("🚀 Training the model...")
stacking_clf.fit(X_train, y_train)

# 🔥 **Evaluate Model**
y_pred = stacking_clf.predict(X_test)
y_pred_proba = stacking_clf.predict_proba(X_test)[:, 1]  # Probability for SQL Injection

accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
f1 = f1_score(y_test, y_pred)

print(f"🎯 Model Performance:")
print(f"✔️ Accuracy: {accuracy:.4f}")
print(f"✔️ ROC AUC: {roc_auc:.4f}")
print(f"✔️ F1 Score: {f1:.4f}")

# Save model & vectorizer
try:
    save_model(stacking_clf, vectorizer)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print("✅ Model and vectorizer saved successfully!")
except Exception as e:
    print(f"❌ ERROR: Failed to save model/vectorizer. {e}")
    exit(1)  # Explicitly exit with error
