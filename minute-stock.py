import sys
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import time

def convert_time(time_string):
    # Parse the time string
    time_object = datetime.strptime(time_string, "%H:%M")

    # Convert to 12 hour format
    time_12_hour = time_object.strftime("%I:%M %p")

    return time_12_hour

def analyze_stocks(stock_list, date):
    for ticker in stock_list:

        if date:
            # If a date argument was given, download data for that specific day
            data = yf.download(tickers=ticker, start=date, end=date, interval='1m')
        else:
            # If no date argument was given, download the most recent day's data
            data = yf.download(tickers=ticker, period='1d', interval='1m')

        # If data is empty, then skip this ticker
        if data.empty:
            print(f"No data available for {ticker} on {date}")
            continue

        # Identify the time with the lowest and highest price
        min_price_time = data['Low'].idxmin()
        min_price = data['Low'].min()
        
        max_price_time = data['High'].idxmax()
        max_price = data['High'].max()

        # Convert Timestamp to string with format "%H:%M"
        min_price_time_str = min_price_time.strftime("%H:%M")
        max_price_time_str = max_price_time.strftime("%H:%M")

        # Convert the times
        min_price_time_converted = convert_time(min_price_time_str)
        max_price_time_converted = convert_time(max_price_time_str)

        last_open_value = data.iloc[-1]['Open']
        print(f"Current stock price of {ticker}: {last_open_value}")

if __name__ == "__main__":
    date = None
    # Check if a date argument is given
    if len(sys.argv) > 1:
        # Parse the date string to a date
        date = datetime.strptime(sys.argv[1], '%m/%d/%Y').strftime('%Y-%m-%d')
    
    # Analyze the stocks
    #analyze_stocks(['AAPL', 'MSFT', 'GOOGL'], date)
    while True:
        analyze_stocks(['AREB', 'RCM'], date)
        print('\n\n')
        time.sleep(60)
