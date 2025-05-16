import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the stock symbols and date range
stock_symbols = ['NVDA', 'TSLA']
start_date = '2025-01-01'
end_date = '2025-05-17'

# Download the stock prices with adjusted closing prices
data = yf.download(stock_symbols, start=start_date, end=end_date, auto_adjust=True)["Close"]

# Plot the stock prices
plt.figure(figsize=(12,6))
for symbol in stock_symbols:
    plt.plot(data.index, data[symbol], label=symbol)

plt.title("YTD Stock Prices for NVDA and TSLA (2025)")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price (USD)")
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig("stock_prices_YTD_plot.png")
plt.close()
