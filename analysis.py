import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

df["Return"] = df["Close"].pct_change()

print("Average Return:", df["Return"].mean())
print("Risk:", df["Return"].std())

df["Close"].plot(title="AAPL Price")
plt.show()
