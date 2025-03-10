import pandas as pd
import yfinance as yf
import random
import os

# ✅ Ensure the data directory exists
os.makedirs("../data", exist_ok=True)

### ✅ Fetch Real Stock Prices from Yahoo Finance API ###
print("📈 Fetching Stock Prices for Semiconductor Companies...")

tickers = ["NVDA", "AMD", "TSM", "ASML", "INTC"]
stock_data = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="3mo")  # Last 3 months

    df = hist[["Close"]].reset_index()
    df["Ticker"] = ticker
    stock_data.append(df)

df_stocks = pd.concat(stock_data)
df_stocks.to_csv("../data/semiconductor_stock_prices.csv", index=False)
print("✅ Stock price data saved as 'data/semiconductor_stock_prices.csv'.")

### ✅ Generate Large, Realistic Semiconductor Trade Data ###
print("🌍 Generating Large Semiconductor Trade Data...")

countries = ["USA", "China", "Taiwan", "South Korea", "Germany", "Japan", "India", "Vietnam", "Malaysia", "Mexico"]
trade_data = []

for _ in range(500):  # Create 500 trade transactions
    reporter = random.choice(countries)
    partner = random.choice([c for c in countries if c != reporter])  # Avoid self-trade
    trade_value = random.randint(50000, 10000000)  # Larger trade values
    year = random.choice([2021, 2022, 2023])
    
    trade_data.append({"reporter": reporter, "partner": partner, "trade_value": trade_value, "year": year})

df_trade = pd.DataFrame(trade_data)
df_trade.to_csv("../data/semiconductor_trade.csv", index=False)
print("✅ Semiconductor trade data saved as 'data/semiconductor_trade.csv'.")

### ✅ Generate Large Shipping Data ###
print("🚢 Generating Large Shipping Data...")

ports = ["Shanghai", "Los Angeles", "Singapore", "Rotterdam", "Dubai", "Mumbai", "Busan", "Hamburg"]
statuses = ["In Transit", "Docked", "Anchored", "Delayed"]

shipping_data = []

for i in range(300):  # Create 300 shipping records
    vessel = f"Ship {i+1}"
    location = random.choice(ports)
    status = random.choice(statuses)
    
    shipping_data.append({"vessel": vessel, "location": location, "status": status})

df_shipping = pd.DataFrame(shipping_data)
df_shipping.to_csv("../data/shipping_data.csv", index=False)
print("✅ Shipping data saved as 'data/shipping_data.csv'.")

### ✅ Generate Large Geopolitical Events Data ###
print("🌍 Generating Large Geopolitical Events Data...")

event_severity = ["Low", "Medium", "High", "Critical"]
event_types = ["Trade Restrictions", "Sanctions", "Tech Export Ban", "Tariff Increase", "Supply Chain Disruption"]
geopolitical_data = []

for _ in range(100):  # Generate 100 events
    date = f"{random.randint(2021, 2023)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    mentions = random.randint(100, 10000)  # Increase mentions range
    severity = random.choice(event_severity)
    event_type = random.choice(event_types)

    geopolitical_data.append({"date": date, "mentions": mentions, "severity": severity, "event_type": event_type})

df_events = pd.DataFrame(geopolitical_data)
df_events.to_csv("../data/geopolitical_events.csv", index=False)
print("✅ Geopolitical events data saved as 'data/geopolitical_events.csv'.")

print("🎉 All datasets have been generated successfully!")
