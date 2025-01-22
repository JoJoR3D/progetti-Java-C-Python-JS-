import yfinance as yf

titolo= yf.Ticker("1TSLA.MI")

history= titolo.history(period= "max")

# ritorna in numero di split azionari eseguit e se sono stati eseguiti
print(titolo.splits)

print("\n")