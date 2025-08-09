FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy FastAPI app into the container
COPY lab2Main.py .

# Expose port for FastAPI
EXPOSE 8080

# Run FastAPI with Uvicorn
CMD ["uvicorn", "lab2Main:app", "--host", "0.0.0.0", "--port", "8080"]