
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import json
from typing import Any

import numpy as np
import pandas as pd
from typing import Dict, Any
from fastapi import APIRouter, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from sql_injection import __version__ as model_version
from sql_injection.predict import predict_from_sql_file

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Root Get
    """
    health = schemas.Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )

    return health.dict()


@api_router.post("/predict", status_code=200)
async def predict(input_data: Dict[str, Any] = Body(...)) -> Dict[str, Any]:
    """
    SQL Injection Prediction
    """
    test_file = "data/test_sql_file.sql"  # Ensure this file exists!
    if not os.path.exists(test_file):
        print(f"❌ ERROR: Test file '{test_file}' not found! Please provide a valid SQL file.")
        exit(1)

    results = predict_from_sql_file(test_file)
    if results["errors"] is not None:
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    return results
