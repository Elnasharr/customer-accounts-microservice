# Use an official lightweight Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker build caching
COPY requirements.txt .

# Install dependencies safely
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code into the container
COPY service/ ./service/

# Expose the port the microservice runs on
EXPOSE 8080

# Switch user to non-root for security compliance
RUN useradd -u 8888 appuser && chown -R appuser /app
USER appuser

# Define the command to run the service using Gunicorn or Flask
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "service:app"]