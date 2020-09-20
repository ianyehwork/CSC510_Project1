from get_all_tickers import get_tickers as gt
import pandas as pd
import csv
df = pd.read_csv('secwiki_tickers.csv')
dp = pd.read_csv('tickers.csv', names=['pTicker'])
list_of_tickers = gt.get_tickers()
# or if you want to save them to a CSV file
gt.save_tickers()
tmpTickers = []
stocks=[]
for i in range(len(list_of_tickers)):
    test = df[df.Ticker == list_of_tickers[i]]
    if not (test.empty):
        stocks.append((list_of_tickers[i], list(test.Name.values)[0]))

with open("stocks.csv","w", newline='') as csv_file:
    fieldnames = ["ticker","name"]
    writer= csv.writer(csv_file)
    writer.writerows(stocks)
