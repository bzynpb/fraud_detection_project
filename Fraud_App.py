import pickle
import pandas as pd
import numpy as np
import streamlit as st
import base64

st.set_page_config(page_title='Fraud Detection', page_icon="🔎", layout="wide")

button_style = """ 
<style> div.stButton > button:first-child { 
display: block;
width: 100%;
border: none;
background-color: #008080;
color: white;
padding: 14px 28px;
font-size: 24px;
cursor: pointer;
text-align: center; 
}
.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}
.button span:after {
  content: '\00bb';
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}
.button:hover span {
  padding-right: 25px;
}
.button:hover span:after {
  opacity: 1;
  right: 0;
  }
</style>
"""
st.markdown(button_style, unsafe_allow_html=True) 

## Header
html_temp = """
<div style="background-color:#008080;padding:10px">
<h1 style="color:white;text-align:center;">FRAUD DETECTION</h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)
st.write('\n')

## Background function
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
  
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('b1.jpeg')


c1, c2, c3  = st.columns((3)) # ekrani 2 kolona ayirdik
with c1:
    V4=st.slider("Employee satisfaction point", 0.01, 1.00, 0.50, step=0.01)
    V10=st.slider("Evaluated performance by the employer", 0.01, 1.00, 0.50, step=0.01)
    
with c2:
    V12=st.slider("How many of projects assigned to an employee?", 2 ,7, 5, step=1)
    V17=st.slider("How many hours in averega an employee worked in a month?", 96, 310, 200, step=1)
    
with c3:
    Amount=st.slider("How many hours in averega an employee worked in a month?", 96, 310, 200, step=1)

## Slider color	
ColorMinMax = st.markdown(''' <style> div.stSlider > div[data-baseweb = "slider"] > div[data-testid="stTickBar"] > div { background: rgb(1 1 1 / 0%); } </style>''', unsafe_allow_html = True)
Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{ background-color: rgb(0, 51, 102); box-shadow: rgb(14 38 74 / 20%) 0px 0px 0px 0.3rem;} </style>''', unsafe_allow_html = True)
Slider_Number = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div > div { color: rgb(14, 38, 74); } </style>''', unsafe_allow_html = True)

col = f''' <style> div.stSlider > div[data-baseweb = "slider"] > div > div {{ background: linear-gradient(to right, rgb(1, 183, 158) 0%, 
					rgb(14, 38, 74) {Amount}%, 
					rgba(14, 38, 74, 0.25) {Amount}%, 
					rgba(14, 38, 74, 0.25) 100%); }} </style>'''

ColorSlider = st.markdown(col, unsafe_allow_html = True)   







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


# def predict():
#     print('Enter input values')
#     my_dict = [float(x) for x in request.form.values()]
#     my_dict = pd.DataFrame([my_dict])
#     # my_dict = scaler.transform(my_dict)
#     prediction = model.predict(my_dict)




c1, c2, c3,c4,c5= st.columns((1,3,4,3,1)) 
with c3:
    if c3.button("Predict Now!"):
      
      if prediction[0] > 0.50:
          return st.error('ATTENTION PLEASE !!!')
      elif prediction[0]  <= 0.50:
          return st.success('EVERYTHING SEEMS OKAY...')
      else:
          return st.write('PLEASE ENTER THE CORRECT VALUES IN THE FIELDS TO PREDICT THE FRAUD OF THE TRANSACTION.') 

      
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

