FROM node:20

# Install Python and basic utilities
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Create and activate virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Copy package files first
COPY package.json .
COPY requirements.txt .

# Install root dependencies
RUN npm install

# Copy frontend files and install its dependencies
COPY frontend frontend/
WORKDIR /workspace/frontend
RUN npm install
RUN npm install @rollup/rollup-linux-x64-gnu

# Back to workspace root
WORKDIR /workspace

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose ports
EXPOSE 5173 5000

CMD ["npm", "start"]