FROM mcr.microsoft.com/devcontainers/javascript-node:20

# Install Python 3.10
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    python3.10 \
    python3-pip \
    python3.10-venv \
    git \
    curl \
    wget \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.10 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# [Optional] Install global node packages
RUN su node -c "npm install -g typescript ts-node"

# Create and set working directory
WORKDIR /workspace

# Copy package.json and requirements.txt (if they exist)
COPY package*.json requirements.txt* ./

# Install dependencies (if files exist)
RUN if [ -f "package.json" ]; then npm install; fi && \
    if [ -f "requirements.txt" ]; then pip install -r requirements.txt; fi

# Copy the rest of the application
COPY . .