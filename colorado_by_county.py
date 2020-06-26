import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt 
from matplotlib import dates as mpl_dates

# Read csv file into variable us_county_data
file_path = '/Users/lukepan/Documents/Projects/covid-us-counties/us-counties.csv'
us_county_data = pd.read_csv(file_path)

# Replace null values (in fips) with Unknown
us_county_data.fips = us_county_data.fips.fillna('Unknown')