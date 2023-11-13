# Use the official Ubuntu image as the base
FROM ubuntu:latest

# Update the package list and install essential packages
RUN apt update 
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y libpq-dev

# Upgrade pip to the latest version
RUN python3 -m pip install --upgrade pip
RUN apt install python3.10-venv -y

# Set the working directory
WORKDIR /app

# Install Django
RUN pip install django

EXPOSE 8000

