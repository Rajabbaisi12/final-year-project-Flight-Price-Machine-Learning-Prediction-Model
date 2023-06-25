from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("Algeria_flights_prediction", "rb"))


@app.route("/")
@cross_origin()
def HOME():
    return render_template("HOME.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # scan_date
        date_scan = request.form["departure_time"]
        scan_day = int(pd.to_datetime(date_scan, format="%Y-%m-%dT%H:%M").day)
        scan_month = int(pd.to_datetime(date_scan, format ="%Y-%m-%dT%H:%M").month)
        # print("Scan_Date : ",Scan_day, Scan_month)


        # scan_time
        Shours = int(pd.to_datetime(date_scan, format ="%Y-%m-%dT%H:%M").hour)
        Sminutes = int(pd.to_datetime(date_scan, format ="%Y-%m-%dT%H:%M").minute)
       # Sseconds = int(pd.to_datetime(date_scan, format ="%Y-%m-%dT%H:%M").seconds)
        # print("Scan_Time : ",Shours, Sminutes, Sseconds)



        # departure_time
        Dhours = int(pd.to_datetime(date_scan, format ="%Y-%m-%dT%H:%M").hour)
        Dminutes = int(pd.to_datetime(date_scan, format ="%Y-%m-%dT%H:%M").minute)
      #  Dseconds = int(pd.to_datetime(date_scan, format ="%Y-%m-%dT%H:%M").seconds)
        # print("Departure_Time : ",Dhours, Dminutes, Dseconds)

        # arrival_time
        date_arr = request.form["arrival_time"]
        Ahours = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Aminutes = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
       # Aseconds = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").seconds)
        # print("Arrival_Time : ", Ahours, Amins, Aseconds)

        # Duration
       # Duration_hours = abs(Ahours - Dhours)
       # Duration_minutes = abs(Aminutes - Dminutes)
        # print("Duration : ", Dhours, Dminutes)

        # Total Stops
        stops = int(request.form["stops"])
        # print(stops)



        airline_name=request.form['airline_name']
        if(airline_name=='Air_Canada'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 1
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            

        elif (airline_name=='Air_Arabia_Etihad '):
            airline_name_Air_Arabia_Etihad = 1
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            

        elif (airline_name=='Norwegian_Flyr_AS'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 1
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            
            
        elif (airline_name=='Wizz_Air_Turkish_Airlines_EgyptAir'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 1
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            
            
        elif (airline_name=='Air_Canada_Azul'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 1
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            
            
        elif (airline_name=='United'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 1
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            

        elif (airline_name=='American'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 1
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            

        elif (airline_name=='LATAM'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 1
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            

        elif (airline_name=='Lufthansa'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 1
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
               

        elif (airline_name=='Aegean_Brussels_Airlines'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 1
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
               

        elif (airline_name=='Air_India_Scoot'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 1
            airline_name_Aegean_EgyptAir = 0
                  

        elif (airline_name=='Aegean_EgyptAir'):
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 1
                    


        else:
            airline_name_Air_Arabia_Etihad = 0
            airline_name_Norwegian_Flyr_AS = 0
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir = 0
            airline_name_Air_Canada_Azul = 0
            airline_name_United = 0
            airline_name_Air_Canada = 0
            airline_name_American = 0
            airline_name_LATAM = 0
            airline_name_Lufthansa = 0
            airline_name_Aegean_Brussels_Airlines = 0
            airline_name_Air_India_Scoot = 0
            airline_name_Aegean_EgyptAir = 0
            







        from_country = request.form["from_country"]
        if (from_country == 'Denmark'):
            from_country_Denmark = 1
            from_country_Canada = 0
            from_country_Columbia= 0
            from_country_Brazil = 0
            from_country_India = 0
            from_country_Greece = 0
            from_country_China = 0
            from_country_Dublin = 0
            from_country_Chile  = 0

        elif (from_country == 'Canada'):
            from_country_Denmark = 0
            from_country_Canada = 1
            from_country_Columbia= 0
            from_country_Brazil = 0
            from_country_India = 0
            from_country_Greece = 0
            from_country_China = 0
            from_country_Dublin = 0
            from_country_Chile  = 0

        elif (from_country == 'Columbia'):
            from_country_Denmark = 0
            from_country_Canada = 0
            from_country_Columbia= 1
            from_country_Brazil = 0
            from_country_India = 0
            from_country_Greece = 0
            from_country_China = 0
            from_country_Dublin = 0
            from_country_Chile  = 0

        elif (from_country == 'Brazil'):
            from_country_Denmark = 0
            from_country_Canada = 0
            from_country_Columbia= 0
            from_country_Brazil = 1
            from_country_India = 0
            from_country_Greece = 0
            from_country_China = 0
            from_country_Dublin = 0
            from_country_Chile  = 0

        elif (from_country == 'India '):
            from_country_Denmark = 0
            from_country_Canada = 0
            from_country_Columbia= 0
            from_country_Brazil = 0
            from_country_India = 1
            from_country_Greece = 0
            from_country_China = 0
            from_country_Dublin = 0
            from_country_Chile  = 0

        elif (from_country == 'Greece'):
            from_country_Denmark = 0
            from_country_Canada = 0
            from_country_Columbia= 0
            from_country_Brazil = 0
            from_country_India = 0
            from_country_Greece = 1
            from_country_China = 0
            from_country_Dublin = 0
            from_country_Chile  = 0

        elif (from_country == 'China'):
            from_country_Denmark = 0
            from_country_Canada = 0
            from_country_Columbia= 0
            from_country_Brazil = 0
            from_country_India = 0
            from_country_Greece = 0
            from_country_China = 1
            from_country_Dublin = 0
            from_country_Chile  = 0

        elif (from_country == 'Dublin'):
            from_country_Denmark = 0
            from_country_Canada = 0
            from_country_Columbia= 0
            from_country_Brazil = 0
            from_country_India = 0
            from_country_Greece = 0
            from_country_China = 0
            from_country_Dublin = 1
            from_country_Chile  = 0

        elif (from_country == 'Chile'):
            from_country_Denmark = 0
            from_country_Canada = 0
            from_country_Columbia= 0
            from_country_Brazil = 0
            from_country_India = 0
            from_country_Greece = 0
            from_country_China = 0
            from_country_Dublin = 0
            from_country_Chile  = 1

        

        else:
            from_country_Denmark = 0
            from_country_Canada = 0
            from_country_Columbia= 0
            from_country_Brazil = 0
            from_country_India = 0
            from_country_Greece = 0
            from_country_China = 0
            from_country_Dublin = 0
            from_country_Chile  = 0





        from_country = request.form["dest_country"]
        if (from_country == 'United_States'):
            dest_country_United_States= 1
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

            
        elif (from_country == 'Australia'):
            dest_country_United_States= 0
            dest_country_Australia = 1
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Austria'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 1
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Belgium'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 1
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0


        elif (from_country == 'Brazil'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 1
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'China'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 1
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Columbia'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 1
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Denmark'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 1
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Dublin'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 1
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Egypt'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 1
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'France'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 1
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Germany'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 1
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'India'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 1
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Kenya'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 1
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Mexico'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 1
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Morocco'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 1
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Norway'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 1
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Panama'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 1
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Philippines'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 1
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Portugal'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 1
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Russia'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 1
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Spain'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 1
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Taiwan'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 1
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Turkey'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 1
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'United_Kingdom'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 1
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Vietnam'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 1
            dest_country_Zurich= 0
            dest_country_Thailand = 0

        elif (from_country == 'Zurich'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 1
            dest_country_Thailand = 0

        elif (from_country == 'Thailand'):
            dest_country_United_States= 0
            dest_country_Australia = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Brazil = 0
            dest_country_China = 0
            dest_country_Columbia = 0
            dest_country_Denmark = 0
            dest_country_Dublin = 0
            dest_country_Egypt= 0
            dest_country_France= 0
            dest_country_Germany= 0
            dest_country_India = 0
            dest_country_Kenya = 0
            dest_country_Mexico = 0
            dest_country_Morocco = 0
            dest_country_Norway = 0
            dest_country_Panama = 0
            dest_country_Philippines = 0
            dest_country_Portugal= 0
            dest_country_Russia = 0
            dest_country_Spain = 0
            dest_country_Taiwan = 0
            dest_country_Turkey = 0
            dest_country_United_Kingdom = 0
            dest_country_Vietnam = 0
            dest_country_Zurich= 0
            dest_country_Thailand = 1                
    
    
    
    

        else:
             dest_country_United_States= 0
             dest_country_Australia = 0
             dest_country_Austria = 0
             dest_country_Belgium = 0
             dest_country_Brazil = 0
             dest_country_China = 0
             dest_country_Columbia = 0
             dest_country_Denmark = 0
             dest_country_Dublin = 0
             dest_country_Egypt= 0
             dest_country_France= 0
             dest_country_Germany= 0
             dest_country_India = 0
             dest_country_Kenya = 0
             dest_country_Mexico = 0
             dest_country_Morocco = 0
             dest_country_Norway = 0
             dest_country_Panama = 0
             dest_country_Philippines = 0
             dest_country_Portugal= 0
             dest_country_Russia = 0
             dest_country_Spain = 0
             dest_country_Taiwan = 0
             dest_country_Turkey = 0
             dest_country_United_Kingdom = 0
             dest_country_Vietnam = 0
             dest_country_Zurich= 0
             dest_country_Thailand = 0              
    
    


        prediction=model.predict([[
            stops,
            scan_day,
            scan_month,
            Shours,
            Sminutes,
            #Sseconds,
            Dhours,
            Dminutes,
           # Dseconds,
            Ahours,
            Aminutes,
          #  Aseconds,
            #Duration_hour,
            #Duration_mins,
            airline_name_Air_Canada,
            airline_name_Air_Arabia_Etihad,
            airline_name_Norwegian_Flyr_AS,
            airline_name_Wizz_Air_Turkish_Airlines_EgyptAir,
            airline_name_Air_Canada_Azul,
            airline_name_United,
            airline_name_American,
            airline_name_LATAM,
            airline_name_Lufthansa,
            airline_name_Aegean_Brussels_Airlines,
            airline_name_Air_India_Scoot,
            airline_name_Aegean_EgyptAir,
            from_country_Canada,
            from_country_Chile,
            from_country_China,
            from_country_Columbia,
            from_country_Denmark,
            from_country_Dublin,
            from_country_Greece,
            from_country_India,
            from_country_China,
            from_country_Brazil,
            dest_country_United_States,
            dest_country_Australia,
            dest_country_Austria,
            dest_country_Belgium,
            dest_country_Brazil,
            dest_country_China,
            dest_country_Columbia,
            dest_country_Denmark,
            dest_country_Dublin,
            dest_country_Egypt,
            dest_country_France,
            dest_country_Germany,
            dest_country_India,
            dest_country_Kenya,
            dest_country_Mexico,
            dest_country_Morocco,
            dest_country_Norway,
            dest_country_Panama,
            dest_country_Philippines,
            dest_country_Portugal,
            dest_country_Russia,
            dest_country_Spain,
            dest_country_Taiwan,
            dest_country_Turkey,
            dest_country_United_Kingdom,
            dest_country_Vietnam,
            dest_country_Zurich,
            dest_country_Thailand, 
        ]])

        output=round(prediction[0],2)

        return render_template('HOME.html',prediction_text="Your Flight price is USD. {}".format(output))


    return render_template("HOME.html")




if __name__ == "__main__":
    app.run(debug=True)
