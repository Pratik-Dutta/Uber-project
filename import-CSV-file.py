import numpy as np
import pandas as pd
from IPython.display import display
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
import folium
import folium.plugins as HeatMap
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from plotly.offline import download_plotlyjs , init_notebook_mode , plot , iplot
init_notebook_mode(connected=True)



df = pd.read_csv(r"C:/Users/PRATIK/OneDrive/Desktop/Call projects/Datasets/uber-raw-data-jul14.csv") #paste any csv file path
df.columns = df.columns.str.strip()

fig = px.box(data_frame=df, x='dispatching_base_number', y='active_vehicles')
fig.update_layout(title='Plot', xaxis_title='X-axis Label', yaxis_title='Y-axis Label')
fig.show()

fig = px.violin(data_frame=df, x='dispatching_base_number', y='active_vehicles')
fig.update_layout(title='Plot', xaxis_title='X-axis Label', yaxis_title='Y-axis Label')
fig.show()




df['date'] = pd.to_datetime(df['date'])

df['monthName'] = df['date'].dt.month_name()   
print(df['monthName'])

df['DayName'] = df['date'].dt.day_name()
print(df['DayName'])

df['Hour'] = df['date'].dt.hour
print(df['Hour'])

df['minute'] = df['date'].dt.minute
print(df['minute'])

df['WeekdayName'] = df['date'].dt.weekday_name()
print(df['WeekdayName'])

print(df.head())

pivot_table = df.pivot_table(index=df['active_vehicles'], columns=df['trips'])
print(df['pivot_table'])
pivot_table.plot(kind='bar' , figsize=(8,6))
plt.show()

grouped = df.groupby(['date','trips'])
data = {'index': [1/1/2015,1/3/2015,1/4/2015],
        'column': [1132,1764,29421],
   }
df = pd.DataFrame(data)
print(df)
display(df)


sns.pointplot(x='date', y='trips', data=df)
plt.figure(figsize=(8,6))
plt.show()



sns.pointplot(x='x_variable', y='y_variable', data=df, color='blue')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')                                        #it is another process of draw a plot
plt.title('Title of the Point Plot')
plt.show()


fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()                                               # This set is applicable for basemap by using cartopy
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.RIVERS)
ax.set_title('Basemap Example')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
plt.legend(['Data Points'])
plt.show()


#use folium

map = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
folium.Marker(location=["marker_Latitude", "marker_Longitude"], popup='Marker Popup').add_to(map)
map.save('map.html')

latitude = 40.7586
longitude = -73.9706
map = folium.Map(location=[latitude,longitude], zoom_start=10)

# Add markers to the map
folium.Marker(location=[40.7128, -74.0060], popup='New York City').add_to(map)
folium.Marker(location=[34.0522, -118.2437], popup='Los Angeles').add_to(map)
folium.Marker(location=[51.5074, -0.1278], popup='London').add_to(map)


# Save the map as an HTML file
map.save('map.html')

print(df.head(3))




df['Month'] = pd.to_MonthName(df['Month'])
date_counts = df['date'].value_counts()
print(date_counts)

x_values = [1/1/2015,1/1/2015,1/1/2015,1/1/2015]
y_values = [190,1132,225,1762]
print(df['date'].value_counts().plot(kind='bar'))
plt.plot(x_values, y_values)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Plot Title')
plt.show()


print(df.head())

#import os
# Get the current working directory
#current_dir = os.getcwd()
#print("Current directory:", current_dir)            #This is another method for print total dataset dszx
# List the contents of the current directory
#file_list = os.listdir(current_dir)
#print("Files in current directory:")
#for file in file_list:
    #print(file)
    
print(df.isnull())    
print(df.isnull().sum())
print(type(df.head()))
print(df.duplicated())
print(df.duplicated().sum())
print(df.drop_duplicates(inplace=True))
print(df.shape)
print(df.dtypes)
print(df['date'])
print(df.groupby)


#It is a method to merge some dataset together:
df = pd.DataFrame()
path = r"C:Users/PRATIK/OneDrive/Desktop/Call projects/Datasets"
for file in df :
    current_df = pd.read_CSV(path+'/'+file)
    df = pd.concat([current_df , df])
print(df.duplicated) #print all things


def gen_pivot_table(df,col1,col2):
    pivot = df.groupby([col1,col2]).size().unstack()
    return pivot.style.background_gradient()

df.columns
gen_pivot_table(df,"date","Base")











    
    
     









