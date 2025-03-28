import sys
import aiofiles
import os
import tempfile
from pathlib import Path
import joblib
from typing import Any, Dict
from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.encoders import jsonable_encoder

from sql_injection import __version__ as model_version
from sql_injection.config.core import MODEL_PATH, VECTORIZER_PATH
from sql_injection.predict import predict_from_sql_file


from app import __version__, schemas
from app.config import settings
from app.health import router as health_router  # ✅ Correct import now

# Create the API router
api_router = APIRouter()

# Include health router
api_router.include_router(health_router, prefix="/health", tags=["Health"])


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> Dict[str, Any]:
    """
    Health Check Endpoint
    """
    health_status = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )
    return health_status.dict()


# Load Model & Vectorizer
print("🔄 Loading model and vectorizer...")
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("✅ Model & Vectorizer Loaded Successfully.")
except FileNotFoundError as e:
    print(f"❌ ERROR: {e}")
    exit(1)


@api_router.post("/predict")
async def predict(file: UploadFile = File(...)):
    """Predict SQL injection from an uploaded .sql file"""
    try:
        # Save the uploaded file to a temporary location
        file_location = os.path.join(tempfile.gettempdir(), file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())

        print(f"📄 Processing uploaded file: {file_location}")

        # Read and process the file
        with open(file_location, "r", encoding="utf-8") as f:
            queries = [q.strip() for q in f.readlines() if q.strip()]

        if not queries:
            raise HTTPException(status_code=400, detail="Uploaded file is empty!")

        print("🔄 Making predictions...")

        # Transform the queries using the trained vectorizer
        X_transformed = vectorizer.transform(queries)

        # Get the probability predictions
        y_pred_proba = model.predict_proba(X_transformed)

        # Make final predictions based on probability threshold
        predictions = [
            {"query": q, "prediction": "SQL Injection" if p[1] > 0.5 else "Safe"}
            for q, p in zip(queries, y_pred_proba)
        ]

        print("✅ Predictions Complete!")
        return {"predictions": predictions}

    except Exception as e:
        print(f"❌ ERROR: {e}")
        raise HTTPException(status_code=500, detail=f"File processing failed: {str(e)}")