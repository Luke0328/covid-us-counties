import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 

# Read csv file into variable us_county_data
file_path = '/Users/lukepan/Documents/Projects/covid-us-counties/us-counties.csv'
us_county_data = pd.read_csv(file_path)

# Replace null values (in fips) with Unknown
us_county_data.fips = us_county_data.fips.fillna('Unknown')

# Create variables to store data
selected_date = '2020-06-19'
county_name_list = ['Denver', 'Arapahoe', 'Adams', 'Weld', 'Jefferson', 'El Paso']
county_cases_list = []

# Extract Colorado data
colorado_data = us_county_data.loc[us_county_data.state == 'Colorado'].copy()

# Add the case number for each county to county_case_list
for county in county_name_list:
	county_cases_list.append(colorado_data.loc[(us_county_data.date == selected_date) 
	& (us_county_data.county == county)].cases.item())

# Get the total number of cases on the selected date
total_cases = colorado_data.loc[us_county_data.date == selected_date].cases.sum()

# Adjust the county_cases_list such that it contains the percentage of cases in each county
adjusted_county_cases_list = [round(i / total_cases * 100, 1) for i in county_cases_list]

# Add a element "Other" for counties not selected in the county_name_list 
other_counties = 100
for percentage in adjusted_county_cases_list:
	other_counties -= percentage
county_name_list.append('Other')
adjusted_county_cases_list.append(other_counties)

# Change plot visual style
plt.style.use("fivethirtyeight")

# Generate the pie chart with county and percentage labels
plt.pie(adjusted_county_cases_list, labels=county_name_list, autopct='%1.1f%%')

# Set the title
plt.title('Percentage of Colorado COVID-19 Cases by County')

plt.tight_layout()

plt.show()

