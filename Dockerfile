FROM python:3.8-slim

WORKDIR /app

# Install some basic tools
# RUN apt update && apt install -y \
#     nano \
#     curl \
#     wget \
#     git \
#     unzip \
#     zip \
#     inetutils-ping

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
