# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install -r requirments.txt

# Run application
CMD ["python", "app.py"]