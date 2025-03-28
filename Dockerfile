# Use an official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the wheel file into the container
COPY sql_injection-0.0.1-py3-none-any.whl /app/

# Install the wheel package
RUN pip install --no-cache-dir sql_injection-0.0.1-py3-none-any.whl

# Expose the application port
EXPOSE 8080

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "sql_injection_api.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
