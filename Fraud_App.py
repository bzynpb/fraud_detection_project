import numpy as np
import pandas as pd

import pickle


st.set_page_config(page_title='Fraud Detection', page_icon="🔎", layout="wide")


model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))



coll_dict = {'V4':V4,
             'V10':V10,
             'V12':V12,
             'V14': V14,
             'V17': V17,
    	     'Amount':Amount
            }

columns = ['V4',
           'V10', 
           'V12',
           'V14', 
           'V17',
           'Amount'
          ]

df_coll = pd.DataFrame.from_dict([coll_dict])
prediction = model.predict(user_inputs)


def predict():
    print('Enter input values')
    my_dict = [float(x) for x in request.form.values()]
    my_dict = pd.DataFrame([my_dict])
    # my_dict = scaler.transform(my_dict)
    result = model.predict(my_dict)
    
    if result > 0.50:
        return render_template('index.html', prediction_text='ATTENTION PLEASE !!!')
    elif result <= 0.50:
        return render_template('index.html', prediction_text='EVERYTHING SEEMS OKAY...')
    else:
        return render_template('index.html', prediction_text='PLEASE ENTER THE CORRECT VALUES IN THE FIELDS TO PREDICT THE FRAUD OF THE TRANSACTION.') 



