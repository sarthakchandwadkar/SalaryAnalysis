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

#Lowest Risk Majors
print(Clean_df['Mid-Career 90th Percentile Salary'] - Clean_df['Mid-Career 10th Percentile Salary'])

#Inserting to dataframe
spread_col = Clean_df['Mid-Career 90th Percentile Salary'] - Clean_df['Mid-Career 10th Percentile Salary']
Clean_df.insert(1, 'Spread', spread_col)
print(Clean_df.head())

#Sorting by the Lowest Spread
low_risk = Clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())

#Top five degrees with higest potential
highest_potential = Clean_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())

#Majors with the Greatest Spread in Salaries
highest_spread = Clean_df.sort_values('Spread', ascending=False)
print(highest_spread[['Undergraduate Major', 'Spread']].head())

#grouping pivot data
Clean_df.groupby('Group').count()

#Number formats in the Output
pd.options.display.float_format = '{:,.2f}'.format
