# Use an official Python image
FROM python:3.10-slim

# Install unzip utility to extract .whl file
RUN apt-get update && apt-get install -y unzip

# Set the working directory
WORKDIR /app

# Copy the .whl file into the container
COPY sql_injection-0.0.1-py3-none-any.whl /app/

# Unzip the .whl file to see its contents
#RUN unzip sql_injection-0.0.1-py3-none-any.whl -d /app/unzipped/

# List the contents of the unzipped directory to verify
#RUN ls -l /app/unzipped/


#Copy the 'api' module (adjust the source path to where your 'api' folder is located)
COPY sql_injection_api /app/sql_injection_api

# Install the wheel file
RUN pip install -r sql_injection_api/requirements.txt

# Expose the application port
EXPOSE 8080

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "sql_injection_api.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
