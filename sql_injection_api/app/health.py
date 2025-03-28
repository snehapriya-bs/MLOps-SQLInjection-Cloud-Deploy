from fastapi import APIRouter
from app.schemas.health import Health  # ✅ Import only the schema
from app.config import settings
from app import __version__
from sql_injection import __version__ as model_version

router = APIRouter()

@router.get("/", response_model=Health, status_code=200)
def health():
    """
    Health Check Endpoint
    """
    return Health(
        name=settings.PROJECT_NAME, api_version=__version__, model_version=model_version
    )
