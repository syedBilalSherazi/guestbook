# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (same as used in your app)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
