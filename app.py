from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)
modelDTS=pickle.load(open('ShoePredictionModelv2DTS.pkl','rb'))
modelPrice=pickle.load(open('ShoePredictionModelv2Price.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def index():

    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    Brand=request.args.get('Brand')
    Premium=request.args.get('Premium')
    Size=request.args.get('Size')
    Cond=request.args.get('Cond')

    prediction=modelDTS.predict(pd.DataFrame(columns=['Brand', 'Premium' ,'Size', 'Cond'],data=np.array([Brand,Premium,Size,Cond]).reshape(1, 4)))
    dts = str(np.round(prediction[0],0)) 
   
    # predictionPrice=modelPrice.predict(pd.DataFrame(columns=['Brand', 'Premium' ,'Size', 'Cond', 'DTS'],data=np.array([Brand,Premium,Size,Cond,10]).reshape(1, 5)))
    # price = str(np.round(predictionPrice[0],0)) 
  
    ans = "Days To Send: "+ dts
    #+" , "+ "Price: "+ price
    return ans


if __name__=='__main__':
    app.run()


#/predict?Brand=Nike&Premium=0&Size=42&Cond=Nine