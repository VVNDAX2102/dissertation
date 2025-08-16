import yfinance as yf
import datetime
import os

# Set up dates
end_date = datetime.datetime.today()
start_date = end_date - datetime.timedelta(days=5*365)

ticker = 'IYW'

# Download data
df = yf.download(
    tickers=ticker,
    start=start_date.strftime("%Y-%m-%d"),
    end=end_date.strftime("%Y-%m-%d"),
    interval="1d",
    auto_adjust=True,
    progress=False
)

# Reset index so Date becomes a column
df.reset_index(inplace=True)

# Build save path one folder outside, inside 'data/India'
save_path = os.path.join('technology.csv')

# Save CSV
df.to_csv(save_path, index=False)

print(f"Data saved to: {os.path.abspath(save_path)}")
