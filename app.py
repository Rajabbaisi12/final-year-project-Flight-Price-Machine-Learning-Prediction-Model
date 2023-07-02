from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd


app = Flask(__name__)
model = pickle.load(open("flight2_reg.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
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
            airline_name_Air_Canada = 1,
            airline_name_Air_Canada_United = 0,
            airline_name_Air_France	= 0,
            airline_name_Air_France_Aer_Lingus = 0,
            
         
            

        elif (airline_name=='Air_Canada_United'):
            airline_name_Air_Canada = 0,
            airline_name_Air_Canada_United = 1,
            airline_name_Air_France	= 0,
            airline_name_Air_France_Aer_Lingus = 0,
            

            

        elif (airline_name=='Air_France	'):
            
            airline_name_Air_Canada = 0,
            airline_name_Air_Canada_United = 0,
            airline_name_Air_France	= 1,
            airline_name_Air_France_Aer_Lingus = 0,
          
            
        elif (airline_name=='Air_France_Aer_Lingus'):
            
            airline_name_Air_Canada = 0,
            airline_name_Air_Canada_United = 0,
            airline_name_Air_France	= 0,
            airline_name_Air_France_Aer_Lingus = 1,
           

        else:
            airline_name_Air_Canada = 0,
            airline_name_Air_Canada_United = 0,
            airline_name_Air_France	= 0,
            airline_name_Air_France_Aer_Lingus = 0,
       







        from_country = request.form["from_country"]
        if (from_country == 'Algeria'):
            from_country_Algeria = 1
            

        else:
            from_country_Algeria = 0
           



        from_country = request.form["dest_country"]
        if (from_country == 'Canada'):
            
            dest_country_Canada = 1
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Denmark = 0
            dest_country_Argentina = 0

            
        elif (from_country == 'Austria'):
            
            dest_country_Canada = 0
            dest_country_Austria = 1
            dest_country_Belgium = 0
            dest_country_Denmark = 0
            dest_country_Argentina = 0
            
        elif (from_country == 'Belgium'):
            
            dest_country_Canada = 0
            dest_country_Austria = 0
            dest_country_Belgium = 1
            dest_country_Denmark = 0
            dest_country_Argentina = 0
            
        elif (from_country == 'Denmark'):
            
            dest_country_Canada = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Denmark = 1
            dest_country_Argentina = 0

        
        
        elif (from_country == 'Argentina'):
            
            dest_country_Canada = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Denmark = 0
            dest_country_Argentina = 1
    
    

        else:
            
            dest_country_Canada = 0
            dest_country_Austria = 0
            dest_country_Belgium = 0
            dest_country_Denmark = 0
            dest_country_Argentina = 0
    


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
            airline_name_Air_Canada_United,
            airline_name_Air_France,
            airline_name_Air_France_Aer_Lingus,
         
            

            from_country_Algeria,
            dest_country_Austria,
            dest_country_Belgium,
            dest_country_Canada,
            dest_country_Denmark,
            dest_country_Argentina,
             
        ]])

        output=round(prediction[0],2)

        return render_template('HOME.html',prediction_text="Your Predicted Flight price is USD. {}".format(output))


    return render_template("HOME.html")




if __name__ == "__main__":
    app.run(debug=True)
