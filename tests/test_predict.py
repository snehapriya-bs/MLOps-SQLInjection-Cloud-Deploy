#Unit testing
import sys
import os
from pathlib import Path
import pytest

# Dynamically add `app/` to `sys.path`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "app"))

from predict import predict_from_sql_file  
 


# Dynamically adjust sys.path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

@pytest.fixture
def sample_sql_queries():
    return [
        "SELECT name FROM employees WHERE salary > 50000",
        "' OR '1'='1' --"
    ]

def test_safe_sql(sample_sql_queries):
    result = predict_from_sql_file("tests/test_data/safe_query.sql")
    assert result[0]["prediction"] == "Safe"

def test_sql_injection(sample_sql_queries):
    result = predict_from_sql_file("tests/test_data/sql_injection.sql")
    assert result[0]["prediction"] == "SQL Injection"

if __name__ == "__main__":
    pytest.main()

