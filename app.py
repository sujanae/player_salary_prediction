import streamlit as st
import pickle
import sklearn
import numpy as np
import pandas as pd
from PIL import Image
model =pickle.load(open('model.sav','rb'))

st.title('Player Salary Prediction')
st.sidebar.header('Player Data')
Image=Image.open('BB.jpg')
st.image(Image,width=300)



def user_report():
    rating =st.sidebar.slider('Rating', 50,100,1)
    jersey =st.sidebar.slider('Jersey', 0,100,1)
    team =st.sidebar.slider('Team', 0,30,1)
    position =st.sidebar.slider('Position', 0,10,1)
    country =st.sidebar.slider('Country', 0,30,1)
    draft_year =st.sidebar.slider('Draft Year', 2000,2020,2000)
    draft_round =st.sidebar.slider('Draft Round', 1,10,1)
    draft_peak =st.sidebar.slider('draft_peak', 1,30,1)

    user_report_data = {
        'rating':rating,
        'jersey':jersey,
        'team':team,
        'position':position,
        'country':country,
        'draft year':draft_year,
        'draft round':draft_round,
        'draft peak':draft_peak
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data


user_data = user_report()
st.header('Player Data')
st.write(user_data)

user_data.rename(columns={
    'draft peak': 'draft_peak',
    'draft round': 'draft_round',
    'draft year': 'draft_year'
}, inplace=True)

salary=model.predict(user_data)
st.subheader('Salary')
st.subheader('$' + str(np.round(salary[0], 2)))






    