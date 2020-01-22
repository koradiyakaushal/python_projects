# from yahoo_fin.stock_info import get_live_price, get_day_gainers
# from time import sleep
# # https://finance.yahoo.com/quote/IDEA.NS/analysis?p=IDEA.NS&.tsrc=fin-srch
# while True:
#     print(get_live_price("IDEA.NS"))
#     print(get_day_gainers())
#     sleep(10)
# Install yfinance package.
# !pip install yfinance
 
# Import yfinance
import yfinance as yf  
 
# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('IDEA.NS','2019-01-01','2020-01-01')
 
# Plot the close prices
import matplotlib.pyplot as plt
data.Close.plot()
plt.show()