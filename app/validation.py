#Validates SQL Queries
def validate_query(query: str):
    """Validate input query before processing."""
    if not query.strip():
        raise ValueError("Invalid query: Must not be empty.")
    return query.strip()
