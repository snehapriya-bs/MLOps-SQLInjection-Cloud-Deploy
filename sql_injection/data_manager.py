# Handles Dataset & Model Loading/Saving
import os
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import typing as t

import joblib
import pandas as pd

from sql_injection import __version__ as _version
from pathlib import Path
import pandas as pd
import pickle
import sys
from sql_injection.config.core  import DATASET_PATH, MODEL_PATH, VECTORIZER_PATH

def load_dataset():
    """Load and preprocess the dataset."""
    return pd.read_csv(DATASET_PATH).dropna()

def save_model(model, vectorizer):
    """Save trained model and vectorizer."""
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    with open(VECTORIZER_PATH, "wb") as f:
        pickle.dump(vectorizer, f)

def load_model():
    """Load trained model and vectorizer."""
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer
