from flask import Flask,request,jsonify,render_template 
import pickle 
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)


# let's import the our model (scalar standar and ElasticnetCV)
elasticnetcv_model = pickle.load(open('./models/model.pkl','rb'))
standard_scaler = pickle.load(open('./models/scalar.pkl','rb'))


# route for predict 
@app.route('/',methods=['GET','POST'])
def predict_data():
    if request.method == "POST":
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = int(request.form.get('Region'))
       
        #    scaling the input value 
        new_scaled_data = standard_scaler.transform([[RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = elasticnetcv_model.predict(new_scaled_data)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)