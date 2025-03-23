#Stores Constants & Paths
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "..", "data", "sql_injection_dataset.csv")  # Move one level up
MODEL_PATH = os.path.join(BASE_DIR, "trained_model", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR,"trained_model", "vectorizer.pkl")

API_VERSION = "1.0.0"
PROJECT_NAME = "SQL Injection Detector"
DESCRIPTION = "A FastAPI service to detect SQL injection attempts."
