#!/usr/bin/env python
# coding: utf-8

# In[7]:


from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Homepage.html')

@app.route('/prediction')
def prediction_interface():
    return render_template('prediction.html')

def ARIMA_load_model_data(stock):
    price_path = f'C:/Users/jackc/Documents/FYP_ML_Predict/models/ARIMA_{stock}.pkl'
    with open(price_path, 'rb') as file:
        data_loaded = pickle.load(file)
    return data_loaded


def LSTM_load_model_data(stock):
    price_path = f'C:/Users/jackc/Documents/FYP_ML_Predict/models/LSTM_{stock}.pkl'
    with open(price_path, 'rb') as file:
        data_loaded = pickle.load(file)
    return data_loaded


def RFC_load_next_day_price(stock):
    
    price_path = f'C:/Users/jackc/Documents/FYP_ML_Predict/models/RFC_{stock}.pkl'
    with open(price_path, 'rb') as file:
        next_day_price = pickle.load(file)
    return next_day_price

@app.route('/predict', methods=['POST'])
def predict():
    stock = request.form.get('stock')

    ARIMA_data = ARIMA_load_model_data(stock)  
    LSTM_data = LSTM_load_model_data(stock)  
    RFC_next_day_price = RFC_load_next_day_price(stock)  

    # Pass predictions and model details to the results page
    return render_template('results.html',
			   stock=stock,
                           ARIMA_prediction=ARIMA_data['next_day_price'], 
                           ARIMA_rmse=ARIMA_data['rmse'], 
                           ARIMA_best_order=ARIMA_data['best_order'],
                           LSTM_prediction=LSTM_data['next_day_price'], 
                           LSTM_rmse=LSTM_data['rmse'], 
                           LSTM_mae=LSTM_data['mae'], 
                           LSTM_mape=LSTM_data['mape'],
                           RFC_prediction=RFC_next_day_price)


@app.route('/results')
def results():
    return render_template('results.html')


if __name__ == '__main__':
    app.run(debug=True)


# In[8]:


get_ipython().run_line_magic('tb', '')


# In[ ]:




