'''#lessons
# 1. create df using Pandas read_csv
# 2. select rows
# 3. compute max closing price from selected rows
# 4. compute mean from selected rows 
# 5. plotting data using matplotlib pyplot 
'''
import pandas as pd
import matplotlib.pyplot as plt


######################################################################
#1. create df using Pandas read_csv
def lesson2_1(symb):
	print("@@@@@@@@@@@@@@@@ lesson2_1 Reading data from {}.csv file@@@@@@@@@@@@@@@@@@".format(symb))
	df = pd.read_csv("../data/{}.csv".format(symb))
	print(df.head()) #notice the index is coloumn added(integer)
	return df

def lesson2_2(df):
	print("@@@@@@@@@@@@@@@ lesson2_2 Selecting rows from inde 10-21@@@@@@@@@@@@@@@@@@@@@")
	print(df[10:21]) #rows between index 10 - 21
	#selecting entire column df['close']

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