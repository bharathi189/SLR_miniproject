<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Simple Linear Regression - Salary Prediction</title>
</head>
<body>

<h1 align="center">📈 Salary Prediction Using Simple Linear Regression</h1>

<p align="center">
A Machine Learning web application that predicts employee salary based on years of experience using a trained Simple Linear Regression model.
</p>

<hr>

<h2>📌 Project Overview</h2>

<p>
This project demonstrates the implementation of a <strong>Simple Linear Regression</strong> model using Python and Scikit-Learn.
The model is trained to predict an employee's salary based on their years of professional experience.
</p>

<p>
The trained model is deployed using <strong>Flask</strong> and provides an easy-to-use web interface where users can enter experience values and receive salary predictions instantly.
</p>

<hr>

<h2>🎯 Problem Statement</h2>

<p>
Organizations often need to estimate employee salaries based on experience levels. Manual estimation can be inconsistent and time-consuming.
This project uses Machine Learning to establish a mathematical relationship between:
</p>

<ul>
<li><strong>Independent Variable (X):</strong> Years of Experience</li>
<li><strong>Dependent Variable (Y):</strong> Salary</li>
</ul>

<p>
The model learns this relationship and predicts salary values for new experience inputs.
</p>

<hr>

<h2>🧠 Machine Learning Algorithm Used</h2>

<h3>Simple Linear Regression</h3>

<p>
Simple Linear Regression is a supervised learning algorithm used to model the relationship between two continuous variables.
It attempts to fit the best straight line through the data points.
</p>

<h4>Mathematical Equation</h4>

<p>
Salary Prediction follows the equation:
</p>

<pre>
Y = mX + c
</pre>

Where:

<ul>
<li><strong>Y</strong> = Predicted Salary</li>
<li><strong>X</strong> = Years of Experience</li>
<li><strong>m</strong> = Slope (Coefficient)</li>
<li><strong>c</strong> = Intercept</li>
</ul>

<h4>Model Parameters</h4>

<pre>
Coefficient (m) = 9825.7609
Intercept (c)   = 22587.9854
</pre>

<p>
Final Prediction Formula:
</p>

<pre>
Salary = (9825.7609 × YearsExperience) + 22587.9854
</pre>

<hr>

<h2>📂 Project Structure</h2>

<pre>
Simple-Linear-Regression/
│
├── app.py
├── simple_linear_regression.pkl
├── templates/
│   └── index.html
├── requirements.txt
├── README.md
└── dataset/
    └── Salary_Data.csv
</pre>

<hr>

<h2>📄 File Description</h2>

<h3>1. app.py</h3>

<p>
Main Flask application file.
</p>

Responsibilities:

<ul>
<li>Loads the trained model (.pkl file)</li>
<li>Receives user input from HTML form</li>
<li>Processes prediction requests</li>
<li>Returns predicted salary to the webpage</li>
</ul>

<hr>

<h3>2. simple_linear_regression.pkl</h3>

<p>
Serialized Machine Learning model created using Pickle.
</p>

Contains:

<ul>
<li>Trained Linear Regression Model</li>
<li>Learned coefficient</li>
<li>Intercept value</li>
<li>Model parameters</li>
</ul>

<hr>

<h3>3. index.html</h3>

<p>
Frontend interface of the application.
</p>

Features:

<ul>
<li>User-friendly design</li>
<li>Input field for years of experience</li>
<li>Salary prediction display</li>
<li>Responsive web page</li>
</ul>

<hr>

<h3>4. requirements.txt</h3>

<p>
Contains all project dependencies required to run the application.
</p>

Major Libraries:

<ul>
<li>Flask</li>
<li>Scikit-Learn</li>
<li>NumPy</li>
<li>Pandas</li>
<li>Matplotlib</li>
<li>Joblib</li>
<li>Gunicorn</li>
</ul>

<hr>

<h2>⚙️ Technologies Used</h2>

<table border="1" cellpadding="8">
<tr>
<th>Technology</th>
<th>Purpose</th>
</tr>

<tr>
<td>Python</td>
<td>Programming Language</td>
</tr>

<tr>
<td>Scikit-Learn</td>
<td>Machine Learning Model</td>
</tr>

<tr>
<td>Pandas</td>
<td>Data Handling</td>
</tr>

<tr>
<td>NumPy</td>
<td>Numerical Computation</td>
</tr>

<tr>
<td>Matplotlib</td>
<td>Data Visualization</td>
</tr>

<tr>
<td>Flask</td>
<td>Web Framework</td>
</tr>

<tr>
<td>HTML</td>
<td>User Interface</td>
</tr>
</table>

<hr>

<h2>🔄 Project Workflow</h2>

<ol>
<li>Load Salary Dataset</li>
<li>Perform Data Preprocessing</li>
<li>Separate Features and Target Variables</li>
<li>Train Simple Linear Regression Model</li>
<li>Evaluate Model Performance</li>
<li>Save Model Using Pickle</li>
<li>Create Flask Application</li>
<li>Develop HTML User Interface</li>
<li>Deploy and Predict Salaries</li>
</ol>

<hr>

<h2>📊 Model Training Process</h2>

<h3>Step 1: Import Libraries</h3>

<pre>
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
</pre>

<h3>Step 2: Load Dataset</h3>

<pre>
data = pd.read_csv("Salary_Data.csv")
</pre>

<h3>Step 3: Define Variables</h3>

<pre>
X = data[['YearsExperience']]
y = data['Salary']
</pre>

<h3>Step 4: Train Model</h3>

<pre>
model = LinearRegression()
model.fit(X, y)
</pre>

<h3>Step 5: Save Model</h3>

<pre>
import pickle

with open('simple_linear_regression.pkl','wb') as file:
    pickle.dump(model,file)
</pre>

<hr>

<h2>🚀 Installation Guide</h2>

<h3>Clone Repository</h3>

<pre>
git clone https://github.com/your-username/simple-linear-regression.git

cd simple-linear-regression
</pre>

<h3>Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<h3>Activate Environment</h3>

Windows:

<pre>
venv\Scripts\activate
</pre>

Linux/Mac:

<pre>
source venv/bin/activate
</pre>

<h3>Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>▶️ Run Application</h2>

<pre>
python app.py
</pre>

Open Browser:

<pre>
http://127.0.0.1:5000
</pre>

<hr>

<h2>🧪 Example Prediction</h2>

<table border="1" cellpadding="8">
<tr>
<th>Years of Experience</th>
<th>Predicted Salary</th>
</tr>

<tr>
<td>2</td>
<td>≈ 42,239</td>
</tr>

<tr>
<td>5</td>
<td>≈ 71,716</td>
</tr>

<tr>
<td>10</td>
<td>≈ 120,845</td>
</tr>

</table>

<hr>

<h2>📈 Advantages of Simple Linear Regression</h2>

<ul>
<li>Easy to implement and understand</li>
<li>Fast training process</li>
<li>Interpretable results</li>
<li>Suitable for small datasets</li>
<li>Good baseline model</li>
</ul>

<hr>

<h2>⚠️ Limitations</h2>

<ul>
<li>Assumes linear relationship between variables</li>
<li>Sensitive to outliers</li>
<li>Limited performance on complex datasets</li>
<li>Cannot capture nonlinear patterns</li>
</ul>

<hr>

<h2>🔮 Future Enhancements</h2>

<ul>
<li>Add Multiple Linear Regression</li>
<li>Improve UI using Bootstrap</li>
<li>Deploy on Render/Heroku/AWS</li>
<li>Add graphical prediction charts</li>
<li>Integrate database storage</li>
<li>Add model performance metrics dashboard</li>
</ul>

<hr>

<h2>📚 Learning Outcomes</h2>

<ul>
<li>Understanding Supervised Learning</li>
<li>Implementing Linear Regression</li>
<li>Model Serialization using Pickle</li>
<li>Building Flask Applications</li>
<li>Frontend-Backend Integration</li>
<li>Machine Learning Deployment</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>

<p>
Developed as a Machine Learning project to demonstrate Salary Prediction using Simple Linear Regression and Flask deployment.
</p>

<hr>

<h2>⭐ Support</h2>

<p>
If you found this project useful, please consider giving the repository a star ⭐ on GitHub.
</p>

</body>
</html>
