# sql_injection/__init__.py

# This file marks the `sql_injection` directory as a Python package.
# You can use it to initialize the package or define package-level variables.

# Optional: Import key components to make them easily accessible when importing the package.
from .config.core import config  # Import configuration settings
from .data_manager import load_data, save_model  # Import data management functions
from .features import extract_features  # Import feature extraction logic
from .validation import validate_input  # Import input validation logic
from .train import train_model  # Import model training function
from .predict import predict   # Import prediction function


# Optional: Initialize logging for the package
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Initializing SQL Injection Detector package...")

# Optional: Add any other package-level initialization code here
