# Path setup, and access the config.yml file, datasets folder & trained models
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from pathlib import Path
from typing import Dict, List

from pydantic import BaseModel
from strictyaml import YAML, load

import sql_injection

# Project Directories
PACKAGE_ROOT = Path(sql_injection.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
#print(CONFIG_FILE_PATH)

DATASET_DIR = PACKAGE_ROOT /".."/ "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
DATASET_PATH = os.path.join(BASE_DIR, "..", "data", "sql_injection_dataset.csv")  # Move one level up
MODEL_PATH = os.path.join(BASE_DIR, "trained_model", "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR,"trained_model", "vectorizer.pkl")
VOCAB_PATH = os.path.join(BASE_DIR,"trained_model", "vocab.pkl")

class AppConfig(BaseModel):
    """Application-level config."""
    package_name: str
    training_data_file: str

class MLModelConfig(BaseModel):
    features: List[str]  # ✅ Add this field
    target: str
    test_size: float
    random_state: int
    n_estimators: int
    max_depth: int

class Config(BaseModel):
    """Master config object."""

    app_config_: AppConfig
    model_config_: MLModelConfig

def find_config_file() -> Path:
    """Locate the configuration file."""
    
    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    
    raise Exception(f"Config not found at {CONFIG_FILE_PATH!r}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """Parse YAML containing the package configuration."""

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
        
    raise OSError(f"Did not find config file at path: {cfg_path}")

        
def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """Run validation on config values."""
    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        app_config_ = AppConfig(**parsed_config.data),
        model_config_ = MLModelConfig(**parsed_config.data),
    )

    return _config

# Load and validate configuration at runtime
config = create_and_validate_config()
