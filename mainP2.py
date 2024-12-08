import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Read all the excel files

nvda = pd.read_csv("NVDA_data.csv")
tesla = pd.read_csv("TSLA_data.csv")
lock= pd.read_csv("LMT_data.csv")
raytheon = pd.read_csv("RTX_data.csv")

stocks = {
    "NVDA": nvda,
    "TSLA": tesla,
    "LMT": lock,
    "RTX": raytheon
}
#Pre processing crap,  i swear a about 6 million times now in grad school
for ticker, df in stocks.items():
    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    df = df.dropna(subset=['time'])
    #MAKE SURE THERES NO TIME ZONE THIS TOOK LITERAL HOURS TO FIGURE OUT
    df['time'] = df['time'].apply(lambda x: x.replace(tzinfo=None) if x.tzinfo is not None else x)

#taken this code from myself from another self-project fore miving averages
#https://github.com/WindeezKC/Quant/blob/main/Trade%20Engine/moving_average_strategy.py
    df['short_mavg'] = df['close'].rolling(window=30).mean()  # 30-Day SMA
    df['long_mavg'] = df['close'].rolling(window=90).mean()  # 90-Day SMA
    df['EMA_50'] = df['close'].ewm(span=50, adjust=False).mean()  # 50-Day EMA
    df = df.sort_values(by='time')
    stocks[ticker] = df



#Set the events we are interested in
events = { #picked kinda randomish end dates on some and googled the rest

    "Ukraine/Russia": {"start": "2022-02-24"},
    "Israel/Palestine": {"start": "2023-10-07"},
    "Election 2020": {"start": "2020-01-02"},
    "Election 2024": {"start": "2024-01-18"},
    "China/HongKong": {"start": "2020-06-30"},
    "US Afghanistan": {"start": "2021-08-15"}
}
#Took this from online about the naive issue found in the preprocessin (THIS WAS ANNOYING)
def make_naive(dt):
    if dt.tzinfo is not None:
        dt = dt.replace(tzinfo=None)
    return dt

for ticker, df in stocks.items():
    #plot everything
    #pretty standard with matplotlib

    plt.figure(figsize=(10, 6))
    plt.plot(df['time'], df['close'], label='Close Price', color='blue', alpha=0.5)
    plt.plot(df['time'], df['short_mavg'], label='30-Day SMA', color='green')
    plt.plot(df['time'], df['long_mavg'], label='90-Day SMA', color='orange')
    plt.plot(df['time'], df['EMA_50'], label='50-Day EMA', color='red')
    y_offset = 0
    for event, period in events.items():
        start_date = pd.to_datetime(period['start'])
        start_date = make_naive(start_date)
        plt.axvline(x=start_date, color='purple', linestyle='--', label=f'{event} Start')
        #add the dotted lines for the start dates of events
        plt.annotate(f'{event} Start', 
                     (start_date, df['close'].min()), 
                     textcoords="offset points", 
                     xytext=(0, y_offset),  
                     ha='center', 
                     fontsize=8, 
                     color='purple',
                     rotation=0)
        y_offset -= 20
    plt.title(f"{ticker} Stock Price and Moving Averages with Events")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()















