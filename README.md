# Hackhound - Advanced Web Security Testing Tool

A powerful web application security testing tool built with React and Python, designed for security researchers and penetration testers. Hackhound combines modern frontend technologies with robust backend fuzzing capabilities to provide comprehensive web application security testing.

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v20 or later)
- Python 3.10 or later
- npm or yarn package manager

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hackhound.git
   cd hackhound
   ```

2. **Install Dependencies**
   ```bash
   # Install root project dependencies
   npm install

   # Install frontend dependencies
   cd frontend
   npm install

   # Install Python dependencies
   cd ../app
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   # In frontend directory
   cp .env.example .env

   # In app directory
   cp .env.example .env
   ```

### Starting the Application

You can start the application in several ways:

1. **Start everything (recommended)**
   ```bash
   npm start
   ```
   This will run both frontend and backend concurrently

2. **Start frontend only**
   ```bash
   npm run start:frontend
   ```
   Frontend will be available at http://localhost:5173

3. **Start backend only**
   ```bash
   npm run start:backend
   ```
   API will be available at http://localhost:5000

### Open Using Daytona  

1. **Install Daytona**: Follow the [Daytona installation guide](https://www.daytona.io/docs/installation/installation/).  
2. **Create the Workspace**:  
   ```bash  
   daytona create <SAMPLE_REPO_URL> 
   ```  

---

## ✨ Features

- **Multi-Mode Fuzzing**
  - Directory fuzzing
  - Subdomain enumeration
  - Virtual host discovery
  - API endpoint fuzzing

- **Advanced Security Testing**
  - Parameter injection testing
  - Header manipulation
  - Authentication bypass attempts
  - Custom payload support

- **Modern Tech Stack**
  - React frontend with Vite
  - FastAPI backend
  - Real-time updates
  - Responsive UI
  - Customizable wordlists

- **Developer Experience**
  - Hot reloading
  - Concurrent frontend/backend development
  - Standardized development environment
  - Comprehensive logging
  - Easy deployment

---

## 🛠 Tech Stack

### Frontend
- React 18
- Vite
- React Router DOM
- Axios
- Firebase Authentication
- Lucide React Icons

### Backend
- Python 3.10
- FastAPI
- CORS middleware
- Pydantic for validation

---

## 📄 API Documentation

The API documentation is available at `http://localhost:5000/docs` when running the backend server.

Key endpoints:
- `POST /fuzz`: Main fuzzing endpoint
- `GET /health`: Health check endpoint

---

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.