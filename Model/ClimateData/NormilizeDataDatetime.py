# -*- coding: latin-1 -*-
import pandas as pd
import glob
from datetime import datetime
import re
directory = r"C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\Itumbiara_parsed_data"
lowest_datetime = datetime.now()
biggest_datetime = pd.to_datetime("2000/01/01 00:00:00")
datetimeformats = ["%m/%d/%Y %H:%M:%S", "%Y/%m/%d %H:%M:%S"]
print('Normalizing datatime of dataframes')
opened_dfs = []
for path in glob.glob(directory + "\*.csv"):
    df = pd.read_csv(path,low_memory=False)
    df['datetime_new'] = pd.to_datetime(df['datetime'], format=datetimeformats[0], errors="coerce")
    df['datetime_second'] = pd.to_datetime(df['datetime'], format=datetimeformats[1], errors="coerce")
    df['datetime_new'] = df['datetime_new'].where(pd.notnull(df['datetime_new']),df['datetime_second'])
    df['datetime'] = df['datetime_new']
    df.drop(['datetime_new','datetime_second'],axis=1)
    lowest_datetime = min(lowest_datetime, df["datetime"].min())
    biggest_datetime = max(biggest_datetime, df['datetime'].max())
    file_name = "unknown"
    if re.search("_temperature_",path):
        file_name = 'temperature.csv'
    if re.search("_precipitation_",path):
        file_name = 'precipitation.csv'
    if re.search("_solar_irradiance_1_",path):
        file_name = 'solar_irradiance_1.csv'
    if re.search("_solar_irradiance_2_",path):
        file_name = 'solar_irradiance_2.csv'
    if re.search("_wind_speed_",path):
        file_name = 'wind_speed.csv'
    opened_dfs.append((df,file_name))

for df,file_name in opened_dfs:
    col = df.columns
    col_map = {name:0 for name in col}
    for date in pd.date_range(lowest_datetime,biggest_datetime,freq='10min'):
        if df['datetime'].isin([date]).any():
            continue
        col_map['datetime'] = date
        df = pd.concat([df,pd.DataFrame(col_map,index=[0])],axis=0, ignore_index= True)
    path = r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\ProcessedData\\' + file_name  
    df.to_csv(path,sep=',',index=False)
    print(file_name + 'normalized')



