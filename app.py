# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:55:47 2020

@author: poora
"""
from flask import Flask,render_template,request
from trained_model import Trained_Model
import numpy as np
app=Flask(__name__)

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Airline=request.form['Airline']
    Source=request.form['Source']
    Destination=request.form['Destination']
    Additional_Info=request.form['AdditionalInfo']
    Date_Of_Journey=request.form['DateOfJourney']
    Departure_Time=request.form['DepartureTime']
    Arrival_Time=request.form['ArrivalTime']
    Route=request.form['Route']
    Total_Stops=request.form['TotalStops']
    
    model=Trained_Model()
    data=model.preprocess({'Airline':Airline,
                           'Source':Source,
                           'Destination':Destination,
                           'Additional_Info':Additional_Info,
                           'Date_Of_Journey':Date_Of_Journey,
                           'Departure_Time':Departure_Time,
                           'Arrival_Time':Arrival_Time,
                           'Route':Route,
                           'Total_Stops':Total_Stops})
    
    price=np.round(model.prediction(data),2)
    
    if price < 0:
        return render_template('index.html', prediction_text='Sorry!! Could not predict with the information given')
    else:
        return render_template('index.html', prediction_text='The approximate flight fare is {}'.format(price))
    
if __name__ == "__main__":
    app.run(debug=True)
    