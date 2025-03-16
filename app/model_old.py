import os
import joblib
from sklearn.ensemble import StackingClassifier, GradientBoostingClassifier, AdaBoostClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.linear_model import LogisticRegression

# Load the model (replace path with actual model location)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

def load_model():
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        return model
    else:
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
