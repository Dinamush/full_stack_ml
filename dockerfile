# Use the official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Install system dependencies and create a non-root user
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libffi-dev && \
    useradd -m appuser

# Switch to the non-root user
USER appuser

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the application using Gunicorn and Uvicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
