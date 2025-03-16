from setuptools import setup, find_packages

setup(
    name="sql_injection_detector",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'scikit-learn',
        'xgboost',
        'lightgbm',
        'pandas'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'run-sql-detector = main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
