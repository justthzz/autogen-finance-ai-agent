import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the tickers and the time period
tickers = ["NVDA", "TSLA"]
start_date = "2025-01-01"
end_date = "2025-05-17"

# Fetch the stock data
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Calculate YTD gains (%)
ytd_gains = data.apply(lambda x: (x / x.iloc[0] - 1) * 100)

# Plotting
plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(ytd_gains.index, ytd_gains[ticker], label=ticker)

plt.title("Year-To-Date (YTD) Stock Gains: NVDA vs TSLA (2025)")
plt.xlabel("Date")
plt.ylabel("Gain (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig("ytd_stock_gains.png")
plt.show()
