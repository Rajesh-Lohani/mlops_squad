FROM python:3.9-slim
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose ports for Flask API and MLflow UI

# Flask API Generation and Port update
EXPOSE 5000 
# MLflow UI 
EXPOSE 5001  

# Start Flask app and MLflow UI
CMD ["sh", "-c", "mlflow ui --host 0.0.0.0 --port 5001 & python app.py"]