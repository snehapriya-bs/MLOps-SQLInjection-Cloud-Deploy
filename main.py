from fastapi import FastAPI
import os
import uvicorn
from app.routes import router

app = FastAPI()

# Register router
app.include_router(router)

def main():
    port = int(os.getenv("PORT", 8080))  # ✅ Default to 8080 for Cloud Run
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

if __name__ == "__main__":
    main()



