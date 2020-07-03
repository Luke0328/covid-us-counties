import numpy as np
from matplotlib import pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk

# Read csv file into variable us_county_data
file_path = '/Users/lukepan/Documents/Projects/covid-us-counties/us-counties.csv'
us_county_data = pd.read_csv(file_path)

# Replace null values (in fips) with Unknown
us_county_data.fips = us_county_data.fips.fillna('Unknown')

# Create and name root window
root = tk.Tk()
root.title("Colorado COVID-19 Cases")

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
fig = Figure(figsize=(4, 4), dpi=100)
subplot = fig.add_subplot()
subplot.pie(adjusted_county_cases_list, labels=county_name_list, autopct='%1.1f%%')
plt.tight_layout()

def search_date(entry):
	print('Button Clicked', entry)

canvas = tk.Canvas(root, height=700, width=700)
canvas.pack()

frame = tk.Frame(root, bg='blue')
frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

label = tk.Label(frame, text='Show Colorado COVID-19 cases by County', font=('Times New Roman', 20))
label.place(anchor='n', relx=0.5, rely=0.05)

entry = tk.Entry(frame)
entry.place(anchor='n', relx=0.5, rely=0.13)

button = tk.Button(frame, text="Get Graph", font=('Times New Roman', 16), 
	command=lambda: search_date(entry.get()))
button.place(anchor='n', relx=0.5, rely=0.2)

chart = FigureCanvasTkAgg(fig, master=frame)
chart.draw()
chart.get_tk_widget().place(anchor='n', relx=0.5, rely=0.3)

root.mainloop()
