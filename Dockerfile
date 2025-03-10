# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port the app runs on
EXPOSE 5001

# Define the default command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "market:app"]
