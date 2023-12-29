# Stock Portfolio Diversification Analysis

This Python script performs a portfolio diversification analysis by utilizing financial data from various stocks. It employs the `yfinance` and `yahoo_fin` libraries to fetch live stock prices and additional information for analysis. The analysis includes general distribution, sector distribution, country distribution, and market cap distribution.

## Prerequisites

Before running the script, ensure you have the required Python libraries installed:

```bash
pip install yfinance yahoo_fin matplotlib
```

## Usage

1. Open the Python script (`portfolio_analysis.py`) in your preferred code editor.

2. Customize the list of stocks (`stocks`) and corresponding amounts (`amounts`) according to your portfolio.

3. Run the script.

4. The script will generate four pie charts illustrating the diversification of your portfolio based on general distribution, sector distribution, country distribution, and market cap distribution.

5. The script also saves the calculated distributions to pickle files (`general.pickle`, `industry.pickle`, `country.pickle`, `market_cap.pickle`) for future reloading.
