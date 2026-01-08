# Dockerfile for Flask YOLO + Gemini Server

FROM python:3.10-slim

# System dependencies for OpenCV / Ultralytics
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libgl1 \
       libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Workdir inside container
WORKDIR /app

# Install Python dependencies first (better layer caching)
COPY flask_server/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY flask_server/ ./

# Expose Flask port
EXPOSE 8080

# Default environment variables (can be overridden at runtime)
ENV FLASK_ENV=production \
    PYTHONUNBUFFERED=1

# Start the Flask server
CMD ["python", "app.py"]
