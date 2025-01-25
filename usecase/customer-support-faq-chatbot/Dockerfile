# Use the official Python image with the specific version
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
# RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files to the container
# COPY pyproject.toml poetry.lock* /app/

COPY requirements.txt /app/

RUN pip install --require-hashes --no-deps -r requirements.txt
# Install dependencies
# RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code to the container
COPY . /app

# Download the SpaCy model
RUN python -m spacy download en_core_web_md

# Expose the port that Streamlit will run on
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the Streamlit app
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]