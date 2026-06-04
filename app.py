import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import pickle
import flask
from flask import Flask,render_template,request
from sklearn.linear_model import LinearRegression
with open("simple_linear_regression.pkl","rb")as t:
    m=pickle.load(t)

app= Flask(__name__)

@app.route("/")
def check():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def fun3():
    a=[float(i) for i in request.form.values()]
    b=[np.array(a)]
    sol = m.predict(b)[0]
    return render_template("index.html",prediction_text=sol)

if __name__ =="__main__":
    app.run(debug=True)
