import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt 
from matplotlib import dates as mpl_dates

# Read csv file into variable us_county_data
file_path = '/Users/lukepan/Documents/Projects/covid_counties/us-counties.csv'
us_county_data = pd.read_csv(file_path)

# Calculate the number of null values in each column and display with a DataFrame
null_values = [ (i, us_county_data[i].isna().sum()) for i in us_county_data ]
null_df = pd.DataFrame(null_values, columns=['column_name', 'count'])

# Replace null values (in fips) with Unknown
us_county_data.fips = us_county_data.fips.fillna('Unknown')

# Extract Boulder county data
boulder_data = us_county_data.loc[(us_county_data.county == 'Boulder') 
	& (us_county_data.state == 'Colorado')].copy()

# Reset indices so they range from 0 to the max number of rows
boulder_data.reset_index(drop=True, inplace=True)

# Create new column representing new cases
boulder_data['new cases'] = boulder_data['cases']

# Populate that column such that it contains the correct number of new cases since the previous date
for i in range(1, len(boulder_data)):
	boulder_data.loc[i, 'new cases'] -= boulder_data.loc[i - 1, 'cases']

boulder_data.date = pd.to_datetime(boulder_data.date)
boulder_data.sort_values('date', inplace=True)

case_date = boulder_data.date
case_count = boulder_data['new cases']

plt.style.use('seaborn')

plt.plot_date(case_date, case_count, linestyle='solid')

plt.axvline(datetime(2020, 3, 25), -2, 45,
	label='Statewide Stay-At-Home Order Implemented', color='r')

plt.title('New COVID-19 Cases in Boulder County by Date')
plt.xlabel('Date')
plt.ylabel('Number of Cases')

plt.gcf().autofmt_xdate()
plt.tight_layout()

plt.legend()

plt.show()


