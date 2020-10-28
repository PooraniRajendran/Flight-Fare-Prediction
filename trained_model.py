# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:02:31 2020

@author: poora
"""
import pickle
import datetime 

class Trained_Model:
    def __init__(self):
        pass
    
    def preprocess(self,features):
        Airline_Dict={'Jet Airways': 0, 
                      'IndiGo': 1, 
                      'Air India': 2, 
                      'Multiple carriers': 3, 
                      'SpiceJet': 4, 
                      'Vistara': 5, 
                      'Air Asia': 6, 
                      'GoAir': 7, 
                      'Multiple carriers Premium economy': 8, 
                      'Jet Airways Business': 9, 
                      'Vistara Premium economy': 10, 
                      'Trujet': 11}
        Source_Dict={'Delhi': 0, 
                     'Kolkata': 1, 
                     'Banglore': 2, 
                     'Mumbai': 3, 
                     'Chennai': 4}
        Destination_Dict={'Cochin': 0, 
                          'Banglore': 1, 
                          'Delhi': 2, 
                          'Hyderabad': 3, 
                          'Kolkata': 4}
        AdditionalInfo_Dict={'No info': 0, 
                             'In-flight meal not included': 1, 
                             'No check-in baggage included': 2, 
                             '1 Long layover': 3, 
                             'Business class': 4, 
                             'Change airports': 5, 
                             '1 Short layover': 6, 
                             'Red-eye flight': 7, 
                             '2 Long layover': 8}
        TotalStop_Dict={'non-stop':0, 
                        '1 stop':1, 
                        '2 stops':2, 
                        '3 stops':3, 
                        '4 stops':4,
                        'Missing':0}
        
        Arrival_Time =0 
        Departure_Time =0
        
        for feature_name,value in features.items():
            if feature_name == 'Airline':
                if value in Airline_Dict.keys():
                    Airline=Airline_Dict.get(value)
                else:
                    Airline=12
            if feature_name == 'Source':
                if value in Source_Dict.keys():
                    Source=Source_Dict.get(value)
                else:
                    Source=5
            if feature_name == 'Destination':
                if value in Destination_Dict.keys():
                    Destination=Destination_Dict.get(value)
                else:
                    Destination=5 
            if feature_name == 'Additional_Info':
                if value in AdditionalInfo_Dict.keys():
                    Additional_Info=AdditionalInfo_Dict.get(value)
                else:
                    Additional_Info=9
            if feature_name == 'Total_Stops':
                if value in TotalStop_Dict.keys():
                    Total_Stops=TotalStop_Dict.get(value)
                else:
                    Total_Stops=0    
            if feature_name == 'Date_Of_Journey':
                if value != ' ':
                    Date_Of_Journey= datetime.datetime.strptime(value, '%Y-%m-%d')
                    Date_of_Journey_month=Date_Of_Journey.month
                else:
                    Date_of_Journey_month = 0
            if feature_name == 'Departure_Time':
                if value != ' ':
                    Departure_Time=datetime.datetime.strptime(value, '%H:%M')
                    Departure_Time_Hour=Departure_Time.hour
                    Departure_Time_Minute=Departure_Time.minute
                else:
                    Departure_Time_Hour=0
                    Departure_Time_Minute=0
            if feature_name == 'Arrival_Time':
                if value != ' ':
                    Arrival_Time=datetime.datetime.strptime(value, '%H:%M')
                    Arrival_Time_Hour=Arrival_Time.hour
                    Arrival_Time_Minute=Arrival_Time.minute
                else:
                    Arrival_Time_Hour=0
                    Arrival_Time_Minute=0
            if feature_name == 'Route':
                if 'DEL' in str(value):
                    DEL = 1
                else:
                    DEL = 0
                if 'BOM' in str(value):
                    BOM = 1
                else:
                    BOM = 0
            if feature_name == 'Total_Stops':
                if value != ' ':
                    DEL = 1
                else:
                    DEL = 0
                if 'BOM' in str(value):
                    BOM = 1
                else:
                    BOM = 0
            if Arrival_Time != 0 and Departure_Time != 0:
                #time_difference= datetime.datetime.strptime(Departure_Time, '%H:%M') - datetime.datetime.strptime(Arrival_Time, '%H:%M')
                time_difference= (Arrival_Time-Departure_Time)
                duration_total_minutes=time_difference.seconds/60
            else:
                duration_total_minutes = 0
        
        print(str(Departure_Time_Minute),str(Arrival_Time_Minute))
                
        return [Airline,
                Source,
                Destination,
                Total_Stops,
                Additional_Info,
                str(Date_of_Journey_month),
                str(Departure_Time_Hour),
                str(Departure_Time_Minute),
                str(Arrival_Time_Hour),
                str(Arrival_Time_Minute),
                str(duration_total_minutes),
                DEL,
                BOM]
    
    def prediction(self,data):
        model=pickle.load(open('final_model.pkl','rb'))
        return model.predict([data])