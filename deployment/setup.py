from setuptools import setup, find_packages

setup(
    name="sql_injection_detector",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "xgboost",
        "lightgbm",
        "fastapi",
        "uvicorn",
        "gunicorn",
        "joblib",
        "pandas"
    ]
)
