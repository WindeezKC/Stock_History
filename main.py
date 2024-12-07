import alpaca_trade_api as alpaca
import pandas as pd
import datetime
from alpaca_trade_api.rest import TimeFrame  # Import TimeFrame to use valid constants

API_KEY = "AKFE1SG5OZIWEUQO5B6B"
SECRET_KEY = "ZccJIzAszaHh42gYtUh1tGzAaPGlbIN2OOY4oqVI"  # THE API KEY HAS BEEN CHANGED AFTER BEING RUN TO PROTECT MYSELF AND MY OTHER SCRIPTS FOR THE FUTURE WITH AN OPEN GITHUB
BASE_URL = "https://paper-api.alpaca.markets"

# Only need to run this script one time to get all stocks data
# This is essentially being used to get it to a CSV which will be used in R to create these graphs

api = alpaca.REST(API_KEY, SECRET_KEY, BASE_URL)
stocks = ["NVDA", "RTX", "LMT", "TSLA"]  # 4 stocks ticker symbols, chose 2 tech and 2 with large military contracts 
start_date = "2020-01-01"  # At least 1 year before Russia/Ukraine War started and latest Israel/Palestine conflict
end_date = "2024-11-28"  # today's date as an end date
start_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
end_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")
start_str = start_obj.strftime("%Y-%m-%d")
end_str = end_obj.strftime("%Y-%m-%d")
# Converting this as alapaca expects it as a dateTIme object and string format for use

def stockData(ticker, start, end, timeFrame=TimeFrame.Day):  # Use TimeFrame.Day constant
    try:
        bars = api.get_bars(ticker, timeFrame, start=start, end=end, adjustment='split')
        #Create Data Frame
        data = []
        for bar in bars:
            data.append({
                'time': bar.t,
                'open': bar.o,
                'high': bar.h,
                'low': bar.l,
                'close': bar.c,
                'volume': bar.v,
                'vw': bar.vw
            })
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'])
            df.set_index('time', inplace=True)
        
        return df
    
    except Exception as error:
        print(f"Error getting symbol {ticker}: {error}")  # Print the error message with ticker
        return None


# Save this to CSV
# Pretty standard loop in python to print to a csv
# This is a fairly simple and easy script to make/run

for stock in stocks:
    print(f"Getting {stock} data")
    data = stockData(stock, start_str, end_str)  
    
    if data is not None:
        fName = f"{stock}_data.csv"
        data.to_csv(fName)
        print(f"Data for {stock} saved to {fName}")  
    else:
        print(f"Error: Stock data cannot be retrieved for {stock}")
