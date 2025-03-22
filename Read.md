sql_injection_detector/
│── sql_injection/                # 🚀 Core Application Code
│   ├── __init__.py               # Initializes app as a package
│   ├── config.py                 # Stores file paths & API settings
│   ├── data_manager.py           # Handles dataset loading & model saving
│   ├── features.py               # TF-IDF feature extraction
│   ├── validation.py             # Input validation
│   ├── train.py                  # Model training script
│   ├── predict.py                # Model prediction logic
│   ├── api.py                    # FastAPI app for predictions
│   ├── main.py  
│   ├── route.py  
│── data/                          # 📊 Training & Test Data
│   ├── sql_injection_dataset.csv  # Training dataset
│   ├── test_sql_file.sql          # Example SQL file for testing
│── trained_models/                # 🎯 Trained Models
│   ├── model.pkl                  # Trained ML model
│   ├── vectorizer.pkl             # TF-IDF vectorizer
│── tests/                         # 🧪 Unit Tests
│   ├── test_predict.py            # Tests for model predictions
│   ├── test_data/                 # Sample SQL queries
│   │   ├── safe_query.sql
│   │   ├── sql_injection.sql
│── deployment/                    # ☁️ Deployment & CI/CD
│   ├── Dockerfile                 # Docker container setup
│   ├── setup.py                   # Builds a .whl package
│   ├── requirements.txt            # Dependencies
│   ├── .github/workflows/deploy.yml # GitHub Actions for Cloud Run
│── SQLInjection_Detector.ipynb      # 📝 Jupyter Notebook
│── README.md                       # 📖 Documentation


C:\Users\sneha\mlops-sqlinjection\MLOps-SQLInjection-Detection

python -m venv .venv
.\.venv\Scripts\activate
pip install -r .\deployment\requirements.txt
python sql_injection/train.py
python .\sql_injection\predict.py
pytest tests/test_predict.py
python .\sql_injection\main.py
