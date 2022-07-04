# Data-analytics-for-airpassengers-using-ML

## Overview 
This is an ARIMA (Auto Regressive Integrated Moving Average) model integrated with a web-app to predict the changes in number of air-passengers. for eg: with 11 years of data from 2011 to 2022, the model will be able to predict till 2024 with an user friendly graph plot.

## The problem it solves 
Forecasting is a common data science practice which helps organisations to set their goals/plans. This model essentially helps airlines or aviation businesses in anomaly detection and/or setting goals according to the trend.

## Preview/screenshots



https://user-images.githubusercontent.com/92823408/177051509-2ef32652-9da9-4d9c-a14b-3f20feb43361.mp4

The video displaying the web app with the model 


### Main page
<img width="1440" alt="Screenshot 2022-07-03 at 8 11 18 PM" src="https://user-images.githubusercontent.com/92823408/177051589-f1112210-839f-40f5-96a4-4906e0926aca.png">
This is where you can select years for prediction, change the historical data with your `.csv` file for prediction and view the raw data 

### The graph
<img width="962" alt="Screenshot 2022-07-03 at 8 11 28 PM" src="https://user-images.githubusercontent.com/92823408/177051635-eb94ef27-81f6-4e7a-a05b-e0cc31fdcd6e.png">
The main graph where you can view the plotted value of the prediction. Black dots are the actual number of passengers during the particular time frame and blue line is the predicted value of passengers

### Forecasting attributes 
<img width="786" alt="Screenshot 2022-07-03 at 8 11 36 PM" src="https://user-images.githubusercontent.com/92823408/177051675-5546adf3-3a24-499d-8a37-3aa607988739.png">
some more components to help users understant the trend better 

## Tech stack used 
- Python 
- Streamlit 
- FBProphet 
- Pandas 

## Running/testing the model 
The model is still in beta and training but it can still be accessed locally **A full fletched web app with multiple models and graphs will be made public soon!**
To test the model locally :
1. download this github repo
2. install all the dependencies from `requirements.txt`
3. run `model.py`
4. run `streamlit run model.py` in terminal 

## Changing historical data for prediction 
NOTE: The `.csv` should have two columns, 1 with the name `Month` ( which has all the dates ) and 2 with the name `#Passengers` ( which has all the number of passengers )

### Method 1
You can directly change the `.csv` from here 
<img width="331" alt="Screenshot 2022-07-03 at 8 11 43 PM" src="https://user-images.githubusercontent.com/92823408/177052092-9263f5a2-09c4-46bc-841d-3d2448d4e18e.png">

### Method 2
- download the file from github 
- change `AirPassengers.csv` with your `.csv` containing the historical data (the data should be in two columns with date and closing value)
- In the `df` variable change `AirPassengers.csv` with your path of the data 
- In `df_train = df[['Month','#Passengers']]` and `df_train = df_train.rename(columns={'Month':'ds','#Passengers':'y'})` swap "month" and "#passengers" with your two columns names
- run `model.py` 
- input `streamlit run model.py` in the terminal to start the localhost 

## Future Plans 
- Deploy a full fletched web app with a friendly UI
- Integrate more ML models for prediction in different time frames 
- integrate comparision analysis 
- add more editable parameters 
