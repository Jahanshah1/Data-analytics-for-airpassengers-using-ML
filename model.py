import streamlit as st
import pandas as pd
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go



st.title('Forecasting model')

df = pd.read_csv('AirPassengers.csv')

#with st.sidebar.header('1. Upload your CSV data'):
    #uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    #st.sidebar.markdown('AirPassengers.csv')

#st.subheader('1. Dataset')

n_years = st.slider('Years of prediction:', 1, 2)
period = n_years * 365


#PROPHET

df_train = df[['Month','#Passengers']]
df_train = df_train.rename(columns={'Month':'ds','#Passengers':'y'})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.write(f'Forecast plot for {n_years} year(s)')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast attributes")
fig2 = m.plot_components(forecast)
st.write(fig2)
