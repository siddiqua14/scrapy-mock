# Dockerfile for Scrapy Project
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set the default command to run the Scrapy spider
CMD ["scrapy", "crawl", "scraper"]
