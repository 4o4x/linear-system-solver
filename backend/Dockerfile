# Dockerfile for Python API

# Step 1: Use a Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Python API code
COPY . ./

# Expose the port for the API
EXPOSE 8080

# Step 2: Run the API with Flask (or your specific framework)
CMD ["python", "main.py"]
