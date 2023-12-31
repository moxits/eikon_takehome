# Use an official Python runtime as a parent image
FROM python:3.7-slim-buster

RUN mkdir /app

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_ENV="docker"

# Make port 80 available to the world outside this container
EXPOSE 80

