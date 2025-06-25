# 🎓 Student Performance Prediction Web App

A Flask-based machine learning web application that predicts a student’s academic performance level (A, B, C, D, or F) based on multiple input factors such as attendance, study hours, health status, and more.

---

## 🚀 Features

- Predicts academic performance level using a trained ML model (`Random Forest` or similar)
- User-friendly web interface built with Flask
- Encodes multiple categorical and numerical features like:
  - Gender, Grade Level, Age, Parent Education
  - Attendance, Study Hours, Previous Grade
  - Income Level, Extracurricular Participation, Health Status

---

## 🧠 ML Model

- **Model Type:** Trained and saved using `pickle`
- **Input Features:**
  - Gender
  - Age
  - Grade Level
  - Attendance
  - Study Hours
  - Parent Education
  - Income Level
  - Previous Grade
  - Extracurricular Activities
  - Health Status
- **Output Labels:** Predicted performance levels – A, B, C, D, F

---

## 🛠 Tech Stack

- **Backend:** Flask
- **Frontend:** HTML, Jinja2 templates
- **ML Model:** Pickle-serialized Scikit-learn model
- **Libraries:** 
  - `Flask`
  - `pickle`
  - `NumPy`

---

## 📂 Project Structure
student-performance-app/
│
├── app.py # Flask server logic
├── trained_model(1).pkl # Trained ML model
├── templates/
│ ├── index.html # Input form
│ └── result.html # Output display
├── static/ # (Optional) CSS/JS
└── README.md # Project guide


---

## ⚙️ Running the App Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/student-performance-app.git
cd student-performance-app
pip install flask numpy
http://127.0.0.1:5000/


