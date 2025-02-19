# Dockerfile

# Use a lightweight Python base image
FROM python:3.9-slim

# Disable Python buffering
ENV PYTHONUNBUFFERED=1

# Create an app directory
WORKDIR /app

# Copy requirements first (caching advantage)
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose ports that will be used by Streamlit (8501) and Jupyter (8888)
EXPOSE 8501
EXPOSE 8888

# By default, do nothing or pick one service (we'll override in docker-compose)
CMD ["bash"]
