# Python 3.12 slim image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Run the script directly
CMD ["python", "__main__.py"]
