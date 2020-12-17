"""
CS230:      Section HB3
Name:       Juliana Spitzner
Data:       Boston Uber and Lyft Rideshare Data
Description:
This program ... (a few sentences about your program and the queries and charts)
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

st.title('Uber/Lyft Data Analysis Project')
st.header('Juliana Spitzner CS230-HB3')
st.write(' ')

df = st.cache(pd.read_csv)("ridesharesample.csv")

#simplified dataframe
df_one = pd.DataFrame({'Hour': df.hour, 'Day': df.day, 'Month': df.month, 'Datetime': df.datetime, 'Source': df.source, 'Destination': df.destination, 'Cab Type': df.cab_type, 'Name': df.name, 'Price': df.price, 'Distance': df.distance, 'Temperature': df.temperature, 'Weather': df.short_summary})

weatherList = ('Clear', 'Drizzle', 'Foggy', 'Light Rain', 'Mostly Cloudy', 'Overcast', 'Partly Cloudy', 'Possible Drizzle', 'Rain')
meanormed = 'mean'
selectedColumn = 'price'
selectedDest = 'Back Bay'

#choose what columns to view
dataset = st.sidebar.checkbox("Sort Original Dataframe")
if dataset:
    options = st.multiselect('What columns would you like to display?', ['Hour', 'Day', 'Month', 'Datetime', 'Source', 'Destination', 'Cab Type', 'Name', 'Price', 'Distance', 'Temperature', 'Weather'], ['Day', 'Cab Type'])
    df_m = pd.DataFrame({})
    for option in options:
        df_m[option] = df_one[option]
        #if option == 'Price':
            #df_m[option] = '{:.2f}'.format(df_one[option])
    #for price in df_m['Price']:

    sortColumns = st.multiselect('Choose columns to sort by:', options, 'Day')
    df_s = df_m.sort_values(sortColumns)
    #pd.options.display.float_format = '{:,.2f}'.format
    #df_s.Price = df_s.Price.round(2)
    st.write(df_s)

#map
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

#select slider
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
        sourceList = ['None'] + [sourceList]
        dest = st.selectbox("View all entries with a destination of:", (sourceList))
        if dest == 'None':
            monthDay = df_one[(df_one.Month == mon) & (df_one.Day == day) & (df_one.Temperature > temp)]
        else: monthDay = df_one[(df_one.Month == mon) & (df_one.Day == day) & (df_one.Temperature > temp) & (df_one.Destination == dest)]
        st.write(monthDay)
    else:
        st.write(monthDay)

#pivot table
view_pivTable = st.sidebar.checkbox("View Pivot Table")
if view_pivTable:
    values = st.radio("View Price or Distance Data:", ('price', 'distance'))
    pivTable = pd.pivot_table(df, values=values, index=['source', 'destination'], columns='cab_type', aggfunc=np.sum)
    st.write(pivTable)

#line chart
priceList = []
hourList = []
for index, row2 in df.iterrows():
    if row2['source'] == 'Beacon Hill':
        #print('row2', row2['price'])
        if not np.isnan(row2['price']):
            price = float(row2['price'])
            hour = int(row2['hour'])
            priceList.append(price)
            hourList.append(hour)
print(priceList)
print(hourList)
z = zip(priceList, hourList)
hour1, hour2, hour3, hour4, hour5, hour6, hour7, hour8 = [], [], [], [], [], [], [], []
hour9, hour10, hour11, hour12, hour13, hour14, hour15, hour16 = [], [], [], [], [], [], [], []
hour17, hour18, hour19, hour20, hour21, hour22, hour23, hour0 = [], [], [], [], [], [], [], []

#LISTNames = ['hour1', 'hour2', 'hour3', 'hour4']
for x in z:
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
print('1', len(hour1), statistics.mean(hour1), hour1)
print('2', len(hour2), statistics.mean(hour2), hour2)
print('3', len(hour3), statistics.mean(hour3), hour3)
print('4', len(hour4), statistics.mean(hour4), hour4)
print('5', len(hour5), statistics.mean(hour5), hour5)
print('6', len(hour6), statistics.mean(hour6), hour6)
print('7', len(hour7), statistics.mean(hour7), hour7)
print('8', len(hour8), statistics.mean(hour8), hour8)
print('9', len(hour9), statistics.mean(hour9), hour9)
print('10', len(hour10), statistics.mean(hour10), hour10)
print('11', len(hour11), statistics.mean(hour11), hour11)
print('12', len(hour12), statistics.mean(hour12), hour12)
print('13', len(hour13), statistics.mean(hour13), hour13)
print('14', len(hour14), statistics.mean(hour14), hour14)
print('15', len(hour15), statistics.mean(hour15), hour15)
print('16', len(hour16), statistics.mean(hour16), hour16)
print('17', len(hour17), statistics.mean(hour17), hour17)
print('18', len(hour18), statistics.mean(hour18), hour18)
print('19', len(hour19), statistics.mean(hour19), hour19)
print('20', len(hour20), statistics.mean(hour20), hour20)
print('21', len(hour21), statistics.mean(hour21), hour21)
print('22', len(hour22), statistics.mean(hour22), hour22)
print('23', len(hour23), statistics.mean(hour23), hour23)
print('0', len(hour0), statistics.mean(hour0), hour0)

#listoflens = len(hour0), len(hour1),len(hour2),len(hour3),len(hour4),len(hour5),len(hour6),len(hour7),len(hour8),len(hour9),len(hour10),len(hour11),len(hour12),len(hour13),len(hour14),len(hour15),len(hour16),len(hour17),len(hour18),len(hour19),len(hour20),len(hour21),len(hour22),len(hour23)
listofhours = hour0, hour1, hour2, hour3, hour4, hour5, hour6, hour7, hour8, hour9, hour10, hour11, hour12, hour13, hour14, hour15, hour16, hour17, hour18, hour19, hour20, hour21, hour22, hour23

countList = []
meanList = []
medianList = []
for hour in listofhours:
    countList.append(len(hour))
    meanList.append(statistics.mean(hour))
    medianList.append(statistics.median(hour))

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

#fileName = "ridesharesample.csv"
#with open (fileName, 'r') as csv_file:
    #data = csv.DictReader(csv_file)

def function1(m, para1, para2):
    thisPrice = []
    for index, row1 in df.iterrows():
        if row1['destination'] == para2:
            if not np.isnan(row1[para1]):
                thisPrice.append(row1[para1])
    #print('Mean', para1, 'for rides to', para2, 'is', statistics.mean(thisPrice))
    if m == 'mean':
        return statistics.mean(thisPrice)
    if m == 'median':
        return statistics.median(thisPrice)

meanFunction = st.sidebar.checkbox("Mean & Median Function")
if meanFunction:
    meanormed = st.selectbox("Mean or Median:", ('mean', 'median'))
    #selectedColumn = str(input("Choose a column to get the mean of: "))
    selectedColumn = st.selectbox("Choose a column to get the mean of:", ('price', 'distance'))
    #selectedColumn = 'price'
    selectedDest = st.selectbox("Choose a destination: ", (sourceList))
    #selectedDest = 'Back Bay'
    st.write('')
    st.write(meanormed, selectedColumn, 'for rides to', selectedDest, 'is', function1(meanormed, selectedColumn, selectedDest))

def main():
    function1(meanormed, selectedColumn, selectedDest)

main()

