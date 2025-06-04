from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model and scaler
with open("trained_model(1).pkl", "rb") as file:
    model = pickle.load(file)

# Define mappings for categorical features
gender_map = {"Male": 0, "Female": 1}
grade_level_map = {"9th": 0, "10th": 1, "11th": 2, "12th": 3}
parent_education_map = {"High School": 0, "Bachelor's": 1, "Master's": 2}
income_map = {"Low": 0, "Medium": 1, "High": 2}
prev_grade_map = {"A": 0, "B": 1, "C": 2, "D": 3}
extracurricular_map = {"Yes": 1, "No": 0}
health_status_map = {"Good": 0, "Average": 1, "Poor": 2}

# Map model predictions to performance levels
performance_map = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'F'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Collect data from the HTML form
        gender = gender_map[request.form['gender']]
        age = int(request.form['age'])
        grade_level = grade_level_map[request.form['grade_level']]
        attendance = int(request.form['attendance'])
        study_hours = int(request.form['study_hours'])
        parent_education = parent_education_map[request.form['parent_education']]
        income = income_map[request.form['income']]
        prev_grade = prev_grade_map[request.form['prev_grade']]
        extracurriculars = extracurricular_map[request.form['extracurriculars']]
        health_status = health_status_map[request.form['health_status']]

        # Arrange data into a numpy array based on the model's expected input order
        data = np.array([[gender, age, grade_level, attendance, study_hours, 
                          parent_education, income, prev_grade, extracurriculars, health_status]])
        
        # Make prediction
        numerical_prediction = model.predict(data)[0]
        
        # Map the numerical prediction to the actual performance level
        performance_level = performance_map.get(numerical_prediction, "Unknown")

        # Render the result page with the performance level
        return render_template('result.html', prediction=performance_level)

if __name__ == '__main__':
    app.run(debug=True)
