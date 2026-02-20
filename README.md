
# 📊 Survey Chatbot Backend

## 📌 1. Project Overview

The Survey Chatbot Backend is a FastAPI-based system designed to collect and process customer feedback through an intelligent questionnaire-driven chatbot.

The system uses compressed survey logic and response tracking to improve engagement and data collection efficiency.

---

## 🎯 2. Problem Statement

Traditional survey systems suffer from:
- Low engagement rates
- Repetitive questionnaires
- Poor response tracking

This project aims to build an API-driven chatbot system that dynamically handles survey responses and stores analytics efficiently.

---

## 🎯 3. Objectives

- Build a RESTful chatbot API
- Store survey responses in database
- Compress questionnaire logic
- Provide analytics endpoint
- Enable Docker deployment

---

## 🏗️ 4. System Architecture

Client (Frontend)
        ↓
FastAPI Backend
        ↓
SQLite Database

The backend handles:
- Session-based chat
- Question flow management
- Response storage
- Analytics generation

---

## 🛠️ 5. Technology Stack

- Python 3.x
- FastAPI
- SQLite
- Uvicorn
- Docker

---

## 📂 6. Project Structure

app/
 ├── main.py
 ├── models.py
 ├── schemas.py
 ├── database.py
 ├── survey_engine.py
 ├── routes/
 ├── utils/

dockerfile  
requirement.txt  

---

## ⚙️ 7. Installation Guide

### Clone Repository

git clone https://github.com/ghoshhindola5-a11y/project1.git  
cd project1  

### Create Virtual Environment

python -m venv venv  
venv\Scripts\activate  

### Install Dependencies

pip install -r requirement.txt  

### Run Server

uvicorn app.main:app --reload  

Server URL: http://127.0.0.1:8000  

---

## 🔌 8. API Endpoints

### Chat Endpoint
POST /api/chat/{session_id}

Handles chatbot interaction per user session.

### Analytics Endpoint
GET /api/analytics

Returns survey response statistics.

### Swagger Documentation
/docs

---

## 🗄️ 9. Database Design

- SQLite database (survey.db)
- Stores:
  - Session ID
  - Questions
  - User Responses
  - Timestamps

---

## 🚀 10. Future Enhancements

- AI-based dynamic question selection
- JWT Authentication
- PostgreSQL integration
- Cloud deployment
- Admin dashboard

---

## 👩‍💻 Author

Hindola Ghosh  
GitHub: https://github.com/ghoshhindola5-a11y