from pathlib import Path
from typing import List
from pydantic import BaseModel
from strictyaml import YAML, load

# Define project directories
CONFIG_FILE_PATH = Path(__file__).resolve().parent / "config.yml"
DATASET_PATH = Path(__file__).resolve().parent.parent / "data"
MODEL_PATH = Path(__file__).resolve().parent.parent / "trained_model" / "model.pkl"
VECTORIZER_PATH = Path(__file__).resolve().parent.parent / "trained_model" / "vectorizer.pkl"

class AppConfig(BaseModel):
    """Application-level config."""
    package_name: str
    training_data_file: str

class MLModelConfig(BaseModel):  # ✅ Renamed from `ModelConfig`
    """Configuration for model training & feature engineering."""
    target: str
    features: List[str]
    test_size: float
    random_state: int
    n_estimators: int
    max_depth: int

class Config(BaseModel):
    """Master configuration object."""
    app_config: AppConfig
    ml_model_config: MLModelConfig  # ✅ Renamed to avoid conflict

def find_config_file() -> Path:
    """Locate the configuration file."""
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise FileNotFoundError(f"❌ Config file not found at {CONFIG_FILE_PATH!r}")

def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""
    if not cfg_path:
        cfg_path = find_config_file()
    
    with open(cfg_path, "r", encoding="utf-8") as conf_file:
        parsed_config = load(conf_file.read())
        print(f"✅ Config Loaded from {cfg_path}")
        return parsed_config

def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Validate and create a config object."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # Ensure correct structure
    return Config(
        app_config=AppConfig(**parsed_config.data["app_config"]),
        ml_model_config=MLModelConfig(**parsed_config.data["model_config"]),  # ✅ Updated reference
    )

# Load and validate configuration at runtime
config = create_and_validate_config()
