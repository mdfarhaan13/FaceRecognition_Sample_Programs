# FaceRecognition_Sample_Programs
Sample programs of an AI-powered Missing Person Finder system using face recognition, REST APIs, and modern web technologies to match uploaded images against a database.

#  AI-Powered Missing Person Finder System

An end-to-end **Missing Person Finder system** that uses **face detection, face recognition, REST APIs, and modern web technologies** to match uploaded images against a database of missing persons.

This repository contains **sample implementations** of all major components required to build a real-world AI-based identification system.

---

##  Project Objective

To design a system where:
- Users can **report missing persons**
- Users can **search for missing persons**
- Uploaded images are **matched using AI-based face recognition**
- Results are returned with **match confidence**

- ## Project Structure

FaceRecognition_Sample_Programs/
│
├── python/
│ └── missing_person.py
│
├── javascript/
│ └── search_missing_person.js
│
├── html-css/
│ ├── index.html
│ └── style.css
│
├── react/
│ └── App.js
│
├── django/
│ └── api/
|   └──urls.py
|   └──views.py
│
├── fastapi/
│ └── main.py
│
├── postgre/
│ └── schema.sql
│
├── opencv/
│ └── face_detection.py
│
└── deepface/
└── face_verify.py

### Run

 JavaScript – Missing Person Search Logic
Simulates frontend-side search functionality.

Features
In-memory missing person records

Case-insensitive name search

Run
node search_missing_person.js
Future Scope
API-based search

React integration

🌐 HTML & CSS – User Interface
Provides a basic UI layout for the system.

Features
Simple landing page

Buttons for reporting and searching

Run
Open index.html in a browser.

Future Scope
Responsive design

Form handling

Backend connection

⚛️ React – Frontend Component
Basic React component for user interaction.

Features
Functional component

Clean JSX structure

Run
npm install
npm start
Future Scope
Image upload

API calls

Display match confidence

🧪 Django REST Framework – API Layer
Provides RESTful endpoints for backend communication.

Features
JSON-based API

Clean endpoint design

Run
python manage.py runserver
Future Scope
Authentication

CRUD operations

Database integration

⚡ FastAPI – High Performance Backend
Acts as a lightweight backend service.

Features
Fast execution

Automatic Swagger UI

Run
uvicorn main:app --reload
Swagger:

http://127.0.0.1:8000/docs
Future Scope
Image upload endpoint

Face recognition pipeline

PostgreSQL integration

🗄️ PostgreSQL – Database Schema
Defines relational database structure.

Features
Structured missing person table

Sample data insertion

Run
psql -U username -d database_name -f schema.sql
Future Scope
Face embedding storage

Indexing for faster search

👁️ OpenCV – Face Detection
Detects faces from images using classical computer vision.

Features
Haar Cascade-based face detection

Real-time support

Run
python face_detection.py
Algorithm Used
Haar Cascade Classifier

Future Scope
CNN-based detectors

Multi-face detection

🧠 DeepFace / FaceNet – Face Recognition
Verifies whether two face images belong to the same person.

Features
Pre-trained deep learning models

High accuracy embeddings

Run
pip install deepface
python face_verify.py
Model Used
FaceNet (128-dimensional embeddings)


