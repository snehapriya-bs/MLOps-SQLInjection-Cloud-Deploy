import os
import pickle
import pandas as pd
from sklearn.ensemble import StackingClassifier, GradientBoostingClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score
from imblearn.over_sampling import SMOTE

def train_and_save_model():
    print("Training the model...")

    # Load dataset
    file_path = "SqlInjection.csv"
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found!")

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError(f"'{file_path}' is empty!")
    except pd.errors.EmptyDataError:
        raise ValueError(f"'{file_path}' is empty or invalid!")

    # Check for missing values
    if df.isnull().sum().sum() > 0:
        print("Found missing values. Dropping them...")
        df = df.dropna(subset=["Query", "Label"]).reset_index(drop=True)

    print(f"Dataset shape after cleaning: {df.shape}")

    # Extract features and labels
    X = df['Query']
    y = df['Label']

    # Vectorize queries
    vectorizer = TfidfVectorizer(max_features=5000)
    X_vectorized = vectorizer.fit_transform(X)

    # Handle imbalance with SMOTE (if at least 2 classes)
    if len(set(y)) > 1:
        smote = SMOTE(random_state=42)
        X_resampled, y_resampled = smote.fit_resample(X_vectorized, y)
    else:
        X_resampled, y_resampled = X_vectorized, y

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
    )

    print(f"Training data shape: {X_train.shape}")
    print(f"Testing data shape: {X_test.shape}")

    # Define base models
    gbm = GradientBoostingClassifier(n_estimators=100)
    adaboost = AdaBoostClassifier(n_estimators=100)
    xgb = XGBClassifier(n_estimators=100, eval_metric="logloss", verbosity=0)
    lgbm = LGBMClassifier(n_estimators=100)

    # Stacking Classifier
    stacking_clf = StackingClassifier(
        estimators=[
            ('gbm', gbm),
            ('adaboost', adaboost),
            ('xgb', xgb),
            ('lgbm', lgbm)
        ],
        final_estimator=LogisticRegression(solver='liblinear'),
        stack_method='predict_proba'
    )

    # Train the model
    print("Training the stacking model...")
    stacking_clf.fit(X_train, y_train)

    # Evaluate
    y_pred = stacking_clf.predict(X_test)
    y_pred_proba = stacking_clf.predict_proba(X_test)[:, 1]

    accuracy = accuracy_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy: {accuracy:.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")
    print(f"F1 Score: {f1:.4f}")

    # Save model and vectorizer
    with open('model.pkl', 'wb') as f:
        pickle.dump(stacking_clf, f)

    with open('vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

    print("✅ Model and vectorizer saved successfully!")

if __name__ == "__main__":
    train_and_save_model()
