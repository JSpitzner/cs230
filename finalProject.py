"""
CS230:      Section HB3
Name:       Juliana Spitzner
Data:       Boston Uber and Lyft Rideshare Data
Description:
This program allows the user to visualize the data in various ways such as charts, pivot tables, and maps.
The sidebar in the Streamlit app gives 6 views for the user to click through.
There are many options to sort, map, filter, graph, and calculate the data to see the information they desire.

I pledge that I have completed the programming assignment independently.
I have not copied the code from a student or any source.
I have not given my code to any student. 
"""

#streamlit run finalProject.py

import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import pandas as pd
import numpy as np
import statistics

#title & header
st.title('Uber/Lyft Data Analysis Project')
st.header('Juliana Spitzner CS230-HB3')
st.write(' ')
df = st.cache(pd.read_csv)("ridesharesample.csv")

#Function 1: pass in parameters and return mean or median
def function1(m, para1, para2):
    thisPrice = []
    for index, row1 in df.iterrows():
        if row1['destination'] == para2:
            if not np.isnan(row1[para1]):
                thisPrice.append(row1[para1])
    if m == 'mean':
        return statistics.mean(thisPrice)
    if m == 'median':
        return statistics.median(thisPrice)

#Function 2: create list of hours, return nothing
def hourLists(zipped):
    hour1, hour2, hour3, hour4, hour5, hour6, hour7, hour8, hour9, hour10, hour11, hour12 = [], [], [], [], [], [], [], [], [], [], [], []
    hour13, hour14, hour15, hour16, hour17, hour18, hour19, hour20, hour21, hour22, hour23, hour0 = [], [], [], [], [], [], [], [], [], [], [], []
    for x in zipped:
        if x[1] == 1: hour1.append(x[0])
        if x[1] == 2: hour2.append(x[0])
        if x[1] == 3: hour3.append(x[0])
        if x[1] == 4: hour4.append(x[0])
        if x[1] == 5: hour5.append(x[0])
        if x[1] == 6: hour6.append(x[0])
        if x[1] == 7: hour7.append(x[0])
        if x[1] == 8: hour8.append(x[0])
        if x[1] == 9: hour9.append(x[0])
        if x[1] == 10: hour10.append(x[0])
        if x[1] == 11: hour11.append(x[0])
        if x[1] == 12: hour12.append(x[0])
        if x[1] == 13: hour13.append(x[0])
        if x[1] == 14: hour14.append(x[0])
        if x[1] == 15: hour15.append(x[0])
        if x[1] == 16: hour16.append(x[0])
        if x[1] == 17: hour17.append(x[0])
        if x[1] == 18: hour18.append(x[0])
        if x[1] == 19: hour19.append(x[0])
        if x[1] == 20: hour20.append(x[0])
        if x[1] == 21: hour21.append(x[0])
        if x[1] == 22: hour22.append(x[0])
        if x[1] == 23: hour23.append(x[0])
        if x[1] == 0: hour0.append(x[0])
    listofhours = hour0, hour1, hour2, hour3, hour4, hour5, hour6, hour7, hour8, hour9, hour10, hour11, hour12, hour13, hour14, hour15, hour16, hour17, hour18, hour19, hour20, hour21, hour22, hour23
    return listofhours

#Function 3: Pivot Table
#User chooses whether they would like to view a pivot table of price or destination, showing Uber vs. Lyft rides for each source/destination combo
def pivot():
    values = st.radio("View Price or Distance Data:", ('price', 'distance'))
    pivTable = pd.pivot_table(df, values=values, index=['source', 'destination'], columns='cab_type', aggfunc=np.sum)
    st.write(pivTable)
    pass

#Simplified Dataframe
df_one = pd.DataFrame({'Hour': df.hour, 'Day': df.day, 'Month': df.month, 'Datetime': df.datetime, 'Source': df.source, 'Destination': df.destination, 'Cab Type': df.cab_type, 'Name': df.name, 'Price': df.price, 'Distance': df.distance, 'Temperature': df.temperature, 'Weather': df.short_summary})
#Variables to be used later
weatherList = ('Clear', 'Drizzle', 'Foggy', 'Light Rain', 'Mostly Cloudy', 'Overcast', 'Partly Cloudy', 'Possible Drizzle', 'Rain')
meanormed = 'mean'
selectedColumn = 'price'
selectedDest = 'Back Bay'

#Sorted Dataframe
#User is able to pick which columns of the dataframe to view, and which columns to sort by
dataset = st.sidebar.checkbox("Sort Original Dataframe")
if dataset:
    options = st.multiselect('What columns would you like to display?', ['Hour', 'Day', 'Month', 'Datetime', 'Source', 'Destination', 'Cab Type', 'Name', 'Price', 'Distance', 'Temperature', 'Weather'], ['Day', 'Cab Type'])
    df_m = pd.DataFrame({})
    for option in options:
        df_m[option] = df_one[option]
    sortColumns = st.multiselect('Choose columns to sort by:', options, 'Day')
    df_s = df_m.sort_values(sortColumns)
    st.write(df_s)

#Map
#User can view a map of all the locations in the data, which a list on the right of all of the locations
mapData = pd.DataFrame({
    'Source' : df_one['Source'],
    'lat' : df['latitude'],
    'lon' : df['longitude'] })
sourceList = []
for source in mapData['Source']:
    if source not in sourceList:
        sourceList.append(source)
view_map = st.sidebar.checkbox("View Map")
if view_map:
    col1, col2 = st.beta_columns([3, 1])
    col1.subheader("Map")
    col1.map(mapData)
    col2.subheader("Locations")
    col2.table(sourceList)

#Filtered Dataframe
#User can filter out ride data from a particular day, and can also filter on temperature and destination if they would like to
view_dayMonth = st.sidebar.checkbox("Filter Table")
if view_dayMonth:
    columns = ['Hour', 'Day', 'Month', 'Datetime', 'Source', 'Destination', 'Cab Type', 'Name', 'Price', 'Distance', 'Temperature', 'Weather']
    month = st.radio("Select month:", ('November', 'December'))
    if month == 'December':
        day = st.select_slider('Select day', options=[1, 2, 3, 4, 9, 10, 13, 14, 15, 16, 17, 18])
        mon = 12
    if month == 'November':
        day = st.select_slider('Select day', options=[26, 27, 28, 29, 30])
        mon = 11
    monthDay = pd.DataFrame({})
    monthDay = df_one[(df_one.Month == mon) & (df_one.Day == day)]
    tempanddest = st.checkbox("Filter by temperature and destination")
    if tempanddest:
        temp = st.selectbox("View all entries with temperatures greater than:", (range(40,56)))
        sourceList.insert(0, 'None')
        dest = st.selectbox("View all entries with a destination of:", (sourceList))
        if dest == 'None':
            monthDay = df_one[(df_one.Month == mon) & (df_one.Day == day) & (df_one.Temperature > temp)]
        else: monthDay = df_one[(df_one.Month == mon) & (df_one.Day == day) & (df_one.Temperature > temp) & (df_one.Destination == dest)]
        st.write(monthDay)
    else:
        st.write(monthDay)

#Pivot Table
view_pivTable = st.sidebar.checkbox("View Pivot Table")
if view_pivTable:
    pivot()

#Line Chart
#User chooses to view count, mean, median, or both mean & median in the line chart and also chooses the color of the line

#create price & hour lists
priceList = []
hourList = []
for index, row2 in df.iterrows():
    if not np.isnan(row2['price']):
        price = float(row2['price'])
        hour = int(row2['hour'])
        priceList.append(price)
        hourList.append(hour)
#zip price & hour lists into a tuple
z = zip(priceList, hourList)

#calculate count, mean, median lists
countList = []
meanList = []
medianList = []
listofhours = hourLists(z)
for hour in listofhours:
    countList.append(len(hour))
    meanList.append(statistics.mean(hour))
    medianList.append(statistics.median(hour))

#Line Chart
view_linechart = st.sidebar.checkbox("View Line Chart")
if view_linechart:
    countmeanmed = st.sidebar.radio("Plot the line based on:", ('Count', 'Mean', 'Median', 'Mean & Median'))
    color = st.sidebar.color_picker('Pick A Line Color', '#B9159D')
    fig, ax = plt.subplots()
    if countmeanmed == 'Count':
        plt.plot(countList, label='Trip Count', color=color)
        plt.ylabel('Number of trips')
        plt.title('Number of Trips per Hour')
    if countmeanmed == 'Mean':
        plt.plot(meanList, label='Mean Price', color=color)
        plt.ylabel('Price (USD)')
        plt.title('Mean Trip Price per Hour')
    if countmeanmed == 'Median':
        plt.plot(medianList, label='Median Price', color=color)
        plt.ylabel('Price (USD)')
        plt.title('Median Trip Price per Hour')
    if countmeanmed == 'Mean & Median':
        plt.plot(meanList, label='Mean Price', color=color)
        plt.ylabel('Price (USD)')
        plt.title('Mean Trip Price per Hour')
        color2 = st.sidebar.color_picker('Pick A Line Color', '#4C7EDA')
        plt.plot(medianList, label='Median Price', color=color2)
    plt.legend()
    plt.xlabel('Hour of Day')
    plt.xticks(hourList)
    plt.show()
    st.pyplot(fig)

#Calculate mean or median
meanFunction = st.sidebar.checkbox("Mean & Median Function")
if meanFunction:
    meanormed = st.selectbox("Mean or Median:", ('mean', 'median'))
    selectedColumn = st.selectbox("Choose a column to get the mean of:", ('price', 'distance'))
    selectedDest = st.selectbox("Choose a destination: ", (sourceList))
    st.write('')
    st.write(meanormed, selectedColumn, 'for rides to', selectedDest, 'is', function1(meanormed, selectedColumn, selectedDest))

def main():
    function1(meanormed, selectedColumn, selectedDest)

main()

