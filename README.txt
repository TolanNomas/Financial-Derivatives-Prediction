Financial Derivatives Predictor with LSTM, ARIMA, and Random Forest Classifier

This project predicts next-day prices for financial derivatives (Gold, Oil, Wheat) using three models: LSTM (Long Short-Term Memory), ARIMA, and Random Forest Classifier (RFC). The models are deployed in a Flask web application for ease of interaction.

Project Overview
The project focuses on forecasting the next-day prices of commodities using historical data and multiple machine learning and time-series models. Users can interact with the models via a simple web interface.

Technologies Used
- Python
- PyTorch (for LSTM)
- scikit-learn (for Random Forest Classifier)
- statsmodels (for ARIMA)
- Flask (for web deployment)
- pandas, NumPy (for data preprocessing)
- Matplotlib (for visualization)
- yfinance (for fetching financial data)

Installation Instructions

1. Clone the repository:
git clone <repo-url>

2. Navigate to the project directory:
cd <project-directory>

3. Install required dependencies:
Create a requirements.txt file with the following content:

flask==2.0.2
pandas==1.3.3
numpy==1.21.2
matplotlib==3.4.3
yfinance==0.1.63
scikit-learn==0.24.2
tensorflow==2.6.0  # Assuming you're using TensorFlow for LSTM
torch==1.9.0  # Assuming PyTorch is used for LSTM models
statsmodels==0.12.2  # For ARIMA model

Then, install the dependencies:
pip install -r requirements.txt

Running the Project

Step 1: Train the Models
Each model is trained separately for Gold, Oil, and Wheat prices.

- To train LSTM models:
python LSTM_Gold.py  # For Gold
python LSTM_Oil.py   # For Oil
python LSTM_Wheat.py # For Wheat

- To train ARIMA models:
python ARIMA_Gold.py  # For Gold
python ARIMA_Oil.py   # For Oil
python ARIMA_Wheat.py # For Wheat

- To train Random Forest Classifier models:
python RFC_Gold.py  # For Gold
python RFC_Oil.py   # For Oil
python RFC_Wheat.py # For Wheat

Step 2: Run the Flask Application
Once the models are trained, you can run the web app.

python app.py

Step 3: Access the Web App
Open your web browser and navigate to:
http://127.0.0.1:5000/
This interface allows you to select the commodity (Gold, Oil, Wheat) and model (LSTM, ARIMA, RFC) to generate predictions.

Model Performance
- LSTM: Best performance for Gold predictions with a MAPE (Mean Absolute Percentage Error) of 1.079.
- ARIMA: Performs well for short-term predictions but less accurate than LSTM.
- Random Forest Classifier: Provides directionality predictions with ~52% accuracy for all three commodities.

Challenges
- LSTM: Fine-tuning hyperparameters to prevent overfitting.
- ARIMA: Struggled to capture seasonality and long-term trends in commodity prices.
- RFC: Limited directional accuracy due to the volatile nature of financial data.

Future Improvements
- Implementing additional time-series models such as Prophet to enhance prediction accuracy.
- Optimizing the Flask app for real-time data updates.
- Further tuning of the models for better accuracy and cross-validation.

License
This project is licensed under the MIT License.
