# Use the official Python image from Docker Hub as the base image
FROM python:3.8-slim
# Set working directory
WORKDIR /usr/src/app
# Copy
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# run
CMD [ "pytest", "./test_sparse_recommender.py" ]