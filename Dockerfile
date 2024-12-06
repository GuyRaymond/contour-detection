# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the application code
COPY app/ ./app/
COPY images/ ./images/


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable to avoid Python buffering
ENV PYTHONUNBUFFERED=1

# Run the Python script by default
CMD ["python", "app/main.py"]

