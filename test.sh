#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "🔍 Testing Docker setup for HackHound..."

# Test 1: Check if Docker is installed and running
echo -n "Testing Docker installation... "
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed${NC}"
    exit 1
else
    echo -e "${GREEN}✅ Docker is installed${NC}"
fi

# Test 2: Build the Docker image
echo -n "Building Docker image... "
if docker build -t hackhound . &> /dev/null; then
    echo -e "${GREEN}✅ Image built successfully${NC}"
else
    echo -e "${RED}❌ Image build failed${NC}"
    exit 1
fi

# Test 3: Test Node.js version
echo -n "Testing Node.js version... "
NODE_VERSION=$(docker run --rm hackhound-test node --version)
if [[ $NODE_VERSION == *"v20"* ]]; then
    echo -e "${GREEN}✅ Node.js v20 confirmed${NC}"
else
    echo -e "${RED}❌ Wrong Node.js version: ${NODE_VERSION}${NC}"
fi

# Test 4: Test Python version
echo -n "Testing Python version... "
PYTHON_VERSION=$(docker run --rm hackhound-test python3 --version)
if [[ $PYTHON_VERSION == *"3.10"* ]]; then
    echo -e "${GREEN}✅ Python 3.10 confirmed${NC}"
else
    echo -e "${RED}❌ Wrong Python version: ${PYTHON_VERSION}${NC}"
fi

# Test 5: Test npm dependencies
echo -n "Testing npm dependencies... "
if docker run --rm hackhound-test npm list | grep -q "react@"; then
    echo -e "${GREEN}✅ npm dependencies installed${NC}"
else
    echo -e "${RED}❌ npm dependencies missing${NC}"
fi

# Test 6: Test Python dependencies
echo -n "Testing Python dependencies... "
if docker run --rm hackhound-test pip freeze | grep -q "fastapi"; then
    echo -e "${GREEN}✅ Python dependencies installed${NC}"
else
    echo -e "${RED}❌ Python dependencies missing${NC}"
fi

# Test 7: Test port exposure
echo -n "Testing port configuration... "
if docker inspect hackhound-test | grep -q '"5000/tcp"' && docker inspect hackhound-test | grep -q '"5173/tcp"'; then
    echo -e "${GREEN}✅ Ports correctly exposed${NC}"
else
    echo -e "${RED}❌ Port configuration incorrect${NC}"
fi

echo -e "\n🎉 Docker setup test complete!"