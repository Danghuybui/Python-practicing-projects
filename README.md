Python for Finance Report
A Study on Covered Call Writing Strategy

Authors:
Dang Huy Bui
Patrick Guth

Project Description
This Jupyter Notebook, titled "Python for Finance Report," presents a quantitative analysis of the covered call writing (CCW) strategy. The primary goal is to determine if this strategy can lead to portfolio outperformance against a fixed benchmark, such as the S&P 500. The analysis specifically focuses on major market-capitalization stocks that are constituents of the S&P 500.

The covered call strategy involves holding a long position in an underlying stock or index and simultaneously selling a call option on that same asset. The premium collected from selling the call option can enhance returns, particularly in quiet or sideways market conditions.

Methodology and Data
The analysis uses a two-pronged data approach:

Stock Data: Historical stock data for the "MAG7" companies (Apple, Microsoft, Nvidia, Amazon, Berkshire Hathaway, Eli Lilly, Walmart) is retrieved from the CRSP (Center for Research in Security Prices) database. The data includes daily prices, returns, and factors to adjust for stock splits.

Option Data: Call option data for the same set of tickers is sourced from OptionMetrics. The code specifically focuses on call options with a null expiry indicator, which typically expire on the third Friday of each month.

Code Workflow
The notebook is structured to perform the following steps:

Library Imports: Imports essential libraries such as pandas, numpy, statsmodels, and wrds.

Database Connection: Establishes a connection to the WRDS database.

Data Retrieval: Queries WRDS to fetch historical stock and option data for the defined list of tickers and saves the raw data into separate CSV files.

Data Processing: Filters the option data to align it with specific stock dates, and then merges the stock and option data into a single DataFrame for each ticker.

Key Findings
The analysis in this notebook concludes that, for the period and stocks studied, the implemented covered call strategy underperforms the respective stock. This is attributed to aggressive outliers that significantly draw down returns.

However, the regression analysis suggests that the strategy's returns are largely uncorrelated with market returns. This finding is significant from a diversification perspective, as the strategy could potentially improve the Sharpe ratio of a broader portfolio by providing uncorrelated returns.

Future Improvements
The notebook suggests several avenues for further research and strategy improvement:

Implementing better prediction models.

Using a rolling window for volatility adjustment.

Running volatility prediction models such as ARCH or GARCH.
