import streamlit as st
import plotly.express as px
from backend import get_data
st.title("Weather Forecast")
place=st.text_input("Place: ")
days=st.slider("Forecast days",min_value=1,max_value=5)
option=st.selectbox("Select data to view",("temperature","sky"))
st.subheader(f"{option} for {days} in {place}")
filtered_data=get_data(place,days)
if option =="Temperature":
    temp_data=[dict["main"]["temp"] for dict in filtered_data]
    dates=[dict["dt.text"] for dict in filtered_data]
    figure=px.line(x=dates,y=temp_data,labels={"x":"Date","y":"Temp"})
    st.plotly_chart(figure)
if option=="Sky":
    images={"clear":"images/clear.png","cloud":"images/cloud.png","rain":"images/rain.png","snow":"images/snow.png"}
    sky_cond=[dict["weather"][0]["main"] for dict in filtered_data]
    image_paths=[images[condition] for condition in sky_cond]
    print(sky_cond)
    st.image(image_paths)
