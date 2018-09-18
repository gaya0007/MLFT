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
import os
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
	dfspy = pd.read_csv("./data/SPY.csv", index_col='Date', parse_dates=True, 
		usecols = ['Date', 'Adj Close'], na_values = ['nan'])
	'''Rename the Adj Close column to make sure final df does not contain the same name'''	
	dfspy = dfspy.rename(columns={'Adj Close':'SPY'})
	'''df1.join() - does a left join by default, rows from left joins with rows from 
	right, if not present filled with string NaN'''
	df1 = df1.join(dfspy, how=inner)
	'''Pandas join how argument can be used to drop the na values, inner join  
	'''
	#drop the na values, days that SPY was not traded, inner join is used to drop na values 
	#df1.dropna()
	
	'''Joining more data frames in to df1'''
	for symbol in ['GOOG', 'AAPL']:
		df_temp = pd.read_csv("../data/{}.csv".format(symbol),index_col='Date', parse_dates=True, 
			usecols=['Date', 'Adj Close'], na_values = ['nan'])
		df_temp.rename(columns={'Adj Close':symbol}	
		df1.join(df_temp)	#use the default join 
	return df1


def lesson3_3(df):
	print("@@@@@@@@@@@@@@@ lesson3_3 Slicing data @@@@@@@@@@@@@@@@@@@@@")
	'''selcting a portion of the data frame, certain dates and sertain stocks'''
	start_date = pd.date_range('2018-01-01','2018-03-03-31')
	'''row slicing, using df.ix[] selector, start and end date should be ascending order'''
	print (df.ix['2018-01-01':'2018-03-03-31'])
	'''Column slicing'''
	print (df['GOOG', 'AAPL'])
	'''row and column slicing'''
	print (df.ix['2018-01-01':'2018-03-03-31',['GOOG', 'AAPL']])

def lesson3_4(df):
	print("@@@@@@@@@@@@@@@ lesson3_4 Plotting @@@@@@@@@@@@@@@@@@@@@")	
	'''
	Quizz : normalize price data  df1 = df1/df1[0]
	use matplotlib.pyplot library for plotting
	'''
	#plotting data, to see the graph have to call plt.show(), use fontsize parameter to make the graph more readable
	title = "Stock Price"
	df = df/df.ix[0,:] #normalising the data
	ax  = df.plot(title=title, fontsize=2)
	#setting x and y lables
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()
	
if __name__ == '__main__':
	print(lesson3_1().top())
	print(lesson3_2().top())