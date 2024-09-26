stock_list = 'ETH-USD'
training_data_start_date = '01/09/2023'
training_data_end_date = '01/09/2024'

# ------ DO NOT CHANGE CODE BELOW THIS LINE --------

import yfinance as yf
from predictor import *
train_model(stock_list, training_data_start_date, training_data_end_date)