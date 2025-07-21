FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy frontend code and set working directory
COPY frontend/ ./frontend/
WORKDIR /app/frontend

#Set environment variable so Streamlit shows "localhost" in the logs
ENV STREAMLIT_BROWSER_SERVER_ADDRESS=localhost

# Run Streamlit on all interfaces, port 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
