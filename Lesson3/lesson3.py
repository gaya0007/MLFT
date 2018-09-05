'''#lessons
Read in multiple stocks:
	Create an empty pandas.DataFrame with dates as index: pandas.date_range
	Drop missing date rows: pandas.DataFrame.dropna
	Incrementally join data for each stock: pandas.DataFrame.join
Manipulate stock data:
	Index and select data by row (dates) and column (symbols)
	Plot multiple stocks at once (still using pandas.DataFrame.plot)
	Carry out arithmetic operations across stocks
	
Problems to solve
		Data Ranges - read in data only for the required range
		Multiple stocks - create data frame with multiple stocks
		Align dates - Dates should be align for multiple stocks
		Proper order - Dates should be ascending in order

1 Building a data frame - create a empty data frame where that can be filled with 
							required date range and stocks and remove weekends(SPY traded days only.)
							
2 Join data frames   - Joint the SPY df to the empty data frame with weekend removed.
                     - Add in additional data frames (GOOGL, AAPL)							
'''
import pandas as pd
import matplotlib.pyplot as plt


######################################################################
#1. create df using Pandas read_csv
def lesson3_1():
	print("@@@@@@@@@@@@@@@@ lesson3_1 Building a data frame @@@@@@@@@@@@@@@@@@".format(symb))
	start_date = '2017-09-01'
	end_date = '2017-12-01'
	dates = pd.date_range(start_date, end_date)# creates a date time element list
	df1 = pd.DataFrame(index=dates) # creates a empty data frame with dates as index
	return df1

def lesson3_2():
	print("@@@@@@@@@@@@@@@ lesson3_2 Joining data frames @@@@@@@@@@@@@@@@@@@@@")
	df1 = lesson3_1()
	#read the data frame index as 'Date' , and parse the Dates in to date time index,
	#'index_col='Date', parse_dates=True
	#Only read the parameters interested in ['Date', 'Adj Close'] - usecols = ['Date', 'Adj Close']
	#NaN strings should be treated as not a number , na_values = ['nan']
	dfspy = pd.read_csv("./data/SPY.csv", index_col='Date', parse_dates=True, usecols = ['Date', 'Adj Close'], na_values = ['nan'])
	#df1.join() - does a left join by default, rows from left joins with rows from 
	#right, if not present filled with string NaN
	df1 = df1.join(dfspy)
	#drop the na values, days that SPY was not traded
	df1.dropna()
	return df1


def lesson2_3(df):
	print("@@@@@@@@@@@@@@@ lesson2_3 Finding max of the selected 'Close' column @@@@@@@@@@@@@@@@@@@@@")
	print(df['Close'].max())
	
def lesson2_4(df):
	print("@@@@@@@@@@@@@@@ lesson2_4 Finding mean of the selected 'Close' column @@@@@@@@@@@@@@@@@@@@@")
	print(df['Close'].mean())

def lesson2_5(df):
	print("@@@@@@@@@@@@@@@ lesson2_5 plotting 'Close' values @@@@@@@@@@@@@@@@@@@@@")
	df['Close'].plot()
	plt.show()	 #must be called to show the plot
	
if __name__ == '__main__':
	aapl_df = lesson2_1('AAPL')
	lesson2_2(aapl_df)
	lesson2_3(aapl_df)
	lesson2_4(aapl_df)
	lesson2_5(aapl_df)