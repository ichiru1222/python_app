import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

tickers = {
    "apple": "AAPL",
    "facebook": "FB",
    "google": "GOOGL",
    "microsoft": "MSFT",
    "amazon": "AMZN",
    "サイバーエージェント": "4751.T",
    "リクルート": "6098.T",
    "メルカリ": "4385.T",
    "Sansan": "4443.T",
    "DeNA": "2432.T",
    "LINE": "3938.T"
}
days = 20

def get_company(tickers, days):

    df = pd.DataFrame()

    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f"{days}d")
        hist.index = hist.index.strftime("%d %B %Y")
        hist = hist[["Close"]]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = "Name"
        df = pd.concat([df, hist])
    return df

print(get_company(tickers, days))

