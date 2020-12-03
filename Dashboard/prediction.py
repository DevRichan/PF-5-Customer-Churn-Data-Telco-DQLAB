import pickle
# from pandas import DataFrame, get_dummies
import pandas as pd

model = pickle.load(open('finalized_model.sav','rb'))


def prediction_data(data):
    df = pd.DataFrame(data,index=[0])
    hasil = model.predict(df)
    if round(hasil[0]) == 1:
        return 'Churn'
    else:
        return 'No Churn'

def prediction_proba(data):
    df = pd.DataFrame(data,index=[0])
    hasil = model.predict_proba(df)

    if hasil[0][0] > hasil[0][1]:
        return round(hasil[0][0],4) * 100
    else:
        return round(hasil[0][1],4) * 100