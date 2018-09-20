"""Utility functions"""

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="../data"):
	"""Return CSV file path given ticker symbol."""
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
	"""Read stock data (adjusted close) for given symbols from CSV files."""
	df = pd.DataFrame(index=dates)
	#print(df)
	if 'SPY' not in symbols:  # add SPY for reference, if absent
		symbols.insert(0, 'SPY')

	for symbol in symbols:
		# TODO: Read and join data for each symbol
		dftemp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
		dftemp = dftemp.rename(columns={'Adj Close':symbol})
		print(dftemp)
		df = df.join(dftemp, how='inner')

	return df


def test_run():
	# Define a date range
	dates = pd.date_range('2017-09-01', '2017-12-01')

	# Choose stock symbols to read
	symbols = ['GOOGL', 'AAPL']
	
	# Get stock data
	df = get_data(symbols, dates)
	print(df)


if __name__ == '__main__':
	test_run()