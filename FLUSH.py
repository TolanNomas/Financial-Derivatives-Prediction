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

def load_next_day_price(model_type, stock):
    
    price_path = f'C:/Users/jackc/Documents/FYP_ML_Predict/models/{model_type}_{stock}.pkl'
    with open(price_path, 'rb') as file:
        next_day_price = pickle.load(file)
    return next_day_price

@app.route('/predict', methods=['POST'])
def predict():
    stock = request.form.get('stock')
    model_type = request.form.get('model_type')

    # Load the next day price for the selected stock
    next_day_price = load_next_day_price(model_type, stock)
    # Directly pass the next_day_price to the results page
    return render_template('results.html', prediction=next_day_price)

@app.route('/results/<prediction>')
def results(prediction):
    return render_template('results.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)


# In[8]:


get_ipython().run_line_magic('tb', '')


# In[ ]:




