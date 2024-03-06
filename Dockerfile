# Use a specific version tag for the base image
FROM python:3.8-slim AS base

# Set the working directory
WORKDIR /usr/src/app

# Copy only the requirements file first
COPY requirements.txt ./

# Create a non-root user and switch to it
RUN adduser  myuser
USER myuser

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use a separate stage for the application
FROM base AS app

# Copy the application code
COPY . .

# Specify the entrypoint command
ENTRYPOINT ["python", "./main.py"]
