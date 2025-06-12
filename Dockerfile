# Use an official Python base image (ARM version works on M2 chip)
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy everything into the container's /app directory
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Flask app and Celery worker together
CMD ["sh", "-c", "flask run --host=0.0.0.0 & celery -A tasks worker --loglevel=info"]
