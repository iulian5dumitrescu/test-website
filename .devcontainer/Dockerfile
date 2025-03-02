FROM mcr.microsoft.com/devcontainers/python:latest

# Set the working directory
WORKDIR /workspace

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
