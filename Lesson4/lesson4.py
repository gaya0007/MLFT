'''#lessons
numpy python library:
	Create a NumPy array:
			from a pandas dataframe: pandas.DataFrame.values
			from a Python sequence: numpy.array
			with constant initial values: numpy.ones, numpy.zeros
			with random values: numpy.random
	Access array attributes: shape, ndim, size, dtype
	Compute statistics: sum, min, max, mean
	Carry out arithmetic operations: add, subtract, multiply, divide
	Measure execution time: time.time, profile
	Manipulate array elements: Using simple indices and slices, integer arrays, boolean arrays						
'''
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
Numpy ndarray 
	pandas data frame is a wrapper around numpy nd array
	if access df.values provides numpy ndarray element
Accessing array
	nd1[row, col]
	':' for ranges nd1[0:3,1:3] -> {0,1,2} rows {1,2} columns
	-1, -2 -> negative numbers refer from last row or columns
'''

######################################################################
#1. creating numpy arrays
def lesson4_1():
	print("@@@@@@@@@@@@@@@@ lesson4_1 creating numpy arrays @@@@@@@@@@@@@@@@@@"))
	#List to 1D array
	print(np.array([2,3,4]))
	#List to 2D array
	print(np.array([(2,3,4), (5,6,7)]))
	#empty 1d array
	np.empty(5)
	#empty multi d array
	np.empty((3,4,5))
	'''empty function doesn't initialize the values, default data type is float'''
	#arrays of 1s
	np.ones((5,4), dtype=np.int_)
	#arrays of zeros
	np.zeros((2,3))
	#generating random numbers [0.0, 1.0)
	print(np.random.random((5,4)))
	#rand function accepts rows and col number directly instead of a tuple
	print(np.random.random(5,4))
	#Sample numbers froma Gaussian(normal distribution
	print np.random.normal(size=(2,3)) # standard normal (mean =0, s.d =1)
	print np.random.normal(50, 10, size=(2,3)) # change mean to 50 s.d = 10
	
	#random integers
	print(np.random.randint(10)) # a single int in [0,10)
	print(np.random.randint(10)) # same as above specifying low and high explicitly
	print(np.random.randint(0, 10, size=5)) #5 random integers as a 1D array
	print(np.random.randint(0, 10, size=(2,3))) #2x3 array of random integers

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