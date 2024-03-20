from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline

# Flask is framework for web implementation


app = Flask(__name__) # initializing a flask app. We can get the steps from Flask documention

# @app.route('/',methods=['GET'])  # route to display the home page
# def helloworl():
#     return "<p>Hello, World</p>"   # whenever you hit the Api, it will print hello world


# As a user I need 2 routes . 1. Train the model and 2. Predict

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!"


#Get the HTML code from Bootstrap documentation website and paste in index (landing page and result page to showing results)
# or download any template for website and use HTML.

# first we load the landing form and next we render the resukt page on the same form:

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI #/predit is given in index.html on button click
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user with the help of request.form and we convert in into float as my values in float and form stores in string format
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
         # creating a list based on received inputs from user and store in array
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]  
            data = np.array(data).reshape(1, 11)
            
            obj = PredictionPipeline()  # we are calling out prediction pipeline class with the help of object: obj
            predict = obj.predict(data) # passing the data/array to the prediction pipeline and it will return the predictions

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')




if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080)