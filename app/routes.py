import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException
from .prediction import predict_query

router = APIRouter()

@router.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        if 'Query' not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must have a 'Query' column")

        queries = df['Query'].tolist()
        results = predict_query(queries)

        return [{"query": q, "prediction": int(p), "probability": round(prob, 4)} 
                for q, (p, prob) in zip(queries, results)]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
