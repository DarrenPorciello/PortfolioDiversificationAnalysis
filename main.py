import yfinance as yf
from yahoo_fin import stock_info as si
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pickle
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# Set the light blue background color
light_blue = '#add8e6'

plt.style.use("default")

# Define stocks and amounts
stocks = ['AAPL', 'TSLA', 'META', 'GOOG', 'BABA', 'NVDA', 'CCL', 'OMV.VI', 'NSRGY']
amounts = [20, 15, 20, 10, 40, 50, 20, 25, 20]

# Function to get live price with error handling
def get_live_price(symbol):
    try:
        return si.get_live_price(symbol)
    except Exception as e:
        print(f"Error fetching live price for {symbol}: {e}")
        return 0

# Fetch latest data for each stock
values = [get_live_price(stock) * amount for stock, amount in zip(stocks, amounts)]

# Fetch additional information for analysis
sectors = [yf.Ticker(x).get_info()['industry'] for x in stocks]
countries = [yf.Ticker(x).get_info()['country'] for x in stocks]
market_caps = [yf.Ticker(x).get_info()['marketCap'] for x in stocks]

# Calculate general distribution
cash = 40000
general_dist = {
    'Stocks': sum(values),
    'Cash': cash
}

# Calculate sector distribution
sector_dist = {}
for i, sector in enumerate(sectors):
    sector_dist[sector] = sector_dist.get(sector, 0) + values[i]

# Calculate country distribution
country_dist = {}
for i, country in enumerate(countries):
    country_dist[country] = country_dist.get(country, 0) + values[i]

# Calculate market cap distribution
market_cap_dist = {'small': 0.0, 'mid': 0.0, 'large': 0.0, 'huge': 0.0}
for i, market_cap in enumerate(market_caps):
    if market_cap < 2000000000:
        market_cap_dist['small'] += values[i]
    elif market_cap < 10000000000:
        market_cap_dist['mid'] += values[i]
    elif market_cap < 1000000000000:
        market_cap_dist['large'] += values[i]
    else:
        market_cap_dist['huge'] += values[i]

# Save data to pickle files for reloading
with open('general.pickle', 'wb') as f:
    pickle.dump(general_dist, f)

with open('industry.pickle', 'wb') as f:
    pickle.dump(sector_dist, f)

with open('country.pickle', 'wb') as f:
    pickle.dump(country_dist, f)

with open('market_cap.pickle', 'wb') as f:
    pickle.dump(market_cap_dist, f)

# Plotting pie charts
fig, axs = plt.subplots(2, 2, figsize=(10, 8), facecolor=light_blue)

fig.suptitle("Portfolio Diversification Analysis", fontsize=18)
axs[0, 0].pie(general_dist.values(), labels=general_dist.keys(), autopct="%1.1f%%", pctdistance=0.8,
              colors=mcolors.TABLEAU_COLORS)
axs[0, 0].set_title("General Distribution")

axs[0, 1].pie(sector_dist.values(), labels=sector_dist.keys(), autopct="%1.1f%%", pctdistance=0.8,
              colors=mcolors.TABLEAU_COLORS)
axs[0, 1].set_title("Sector Distribution")

axs[1, 0].pie(country_dist.values(), labels=country_dist.keys(), autopct="%1.1f%%", pctdistance=0.8,
              colors=mcolors.TABLEAU_COLORS)
axs[1, 0].set_title("Country Distribution")

axs[1, 1].pie(market_cap_dist.values(), labels=market_cap_dist.keys(), autopct="%1.1f%%", pctdistance=0.8,
              colors=mcolors.TABLEAU_COLORS)
axs[1, 1].set_title("Market Cap Distribution")

plt.show()
