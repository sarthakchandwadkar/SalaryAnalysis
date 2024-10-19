import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
print(df.head())
print(df.shape)
print(df.columns)

#Handling Missing values and junk data
print(df.isna())

Clean_df = df.dropna()
Clean_df.tail()
print(Clean_df)

print(Clean_df['Starting Median Salary'])

#finding the Major with higest salary
print(Clean_df['Starting Median Salary'].max())
print(Clean_df['Starting Median Salary'].idxmax())
print(Clean_df['Undergraduate Major'].loc[43])

#What college major has the highest mid-career salary?
print(Clean_df['Mid-Career Median Salary'].max())
print(f"Index of the max Mid-Career Madian Salary is : {Clean_df['Mid-Career Median Salary'].idxmax()} ")
print(Clean_df['Undergraduate Major'][8])

#The Lowest Starting and Mid-Career Salary
print(Clean_df['Starting Median Salary'].min())
print(Clean_df['Undergraduate Major'].loc[Clean_df['Starting Median Salary'].idxmin()])


#Which college major has the lowest starting salary and how much do graduates earn after university?
print (Clean_df['Mid-Career Median Salary'].max())
print(f"Index for the max mid career salary: {Clean_df[ 'Mid-Career Median Salary'].idxmax()}")
print(Clean_df['Undergraduate Major'][8])

print (Clean_df[ 'Starting Median Salary'].min())
print(Clean_df['Undergraduate Major'].loc[Clean_df[ 'Starting Median Salary'].idxmin()])

print(Clean_df.loc[Clean_df['Mid-Career Median Salary']. idxmin()])