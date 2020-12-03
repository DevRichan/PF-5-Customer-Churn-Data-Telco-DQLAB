from flask import Flask, render_template, request
from cleaning_data import data_auto
from data import decision,gender 
from prediction import prediction_data, prediction_proba
# inisialisasi Flask
app = Flask(__name__)

# home 
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        
        # hasil2 = feature_importances(data)
        data['tenure'] = float(data['tenure'])
        data['MonthlyCharges'] = float(data['MonthlyCharges'])
        data['TotalCharges'] = float(data['TotalCharges'])
        
        # gender
        if data['gender'] == 'Male':
            tmpgender = 1
        else:
            tmpgender = 0
        data['gender'] = tmpgender
        
        # seniorCitizen
        if data['SeniorCitizen'] == 'Yes':
            tmpSenior = 1
        else:
            tmpSenior = 0
        data['SeniorCitizen'] = tmpSenior 

        # Partner
        if data['Partner'] == 'Yes':
            tmpPartner = 1
        else:
            tmpPartner = 0
        data['Partner'] = tmpPartner

        #Phone
        if data['PhoneService'] == 'Yes':
            tmpPhone = 1
        else:
            tmpPhone = 0
        data['PhoneService'] = tmpPhone

        if data['StreamingTV'] == 'Yes':
            tmpTV = 1
        else:
            tmpTV = 0
        data['StreamingTV'] = tmpTV

        if data['InternetService'] == 'Yes':
            tmpInet = 1
        else:
            tmpInet = 0
        data['InternetService'] = tmpInet

        if data['PaperlessBilling'] == 'Yes':
            tmpBilling = 1
        else:
            tmpBilling = 0
        data['PaperlessBilling'] = tmpBilling
        
        hasil = prediction_data(data)
        hasil2 = prediction_proba(data)

        return render_template('result.html',hasil_prediction=hasil,hasil_proba = hasil2 )
    return render_template('prediction.html',data_gender = gender, data_decision = decision)





if __name__ == '__main__':
    app.run(debug=True,port=1111)



