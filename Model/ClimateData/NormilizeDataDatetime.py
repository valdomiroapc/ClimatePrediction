# -*- coding: latin-1 -*-
import pandas as pd
import glob
from datetime import datetime
import re
import yaml
with open(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Configuration\Configfile.yaml') as configFile:
	config = yaml.load(configFile, Loader=yaml.FullLoader)
directory = config['ParsedDataPath']
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
    df.drop(columns=['datetime_new','datetime_second'],inplace=True)
    lowest_datetime = min(lowest_datetime, df["datetime"].min())
    biggest_datetime = max(biggest_datetime, df['datetime'].max())
    file_name = "unknown"
    if re.search("temperature",path):
        file_name = 'temperature.csv'
    if re.search("precipitation",path):
        file_name = 'precipitation.csv'
    if re.search("solar_irradiance_1",path):
        file_name = 'solar_irradiance_1.csv'
    if re.search("solar_irradiance_2",path):
        file_name = 'solar_irradiance_2.csv'
    if re.search("wind_speed",path):
        file_name = 'wind_speed.csv'
    if re.search("humidity",path):
        file_name = 'humidity.csv'
    opened_dfs.append((df,file_name))

for df,file_name in opened_dfs:
    col = df.columns
    col_map = {name:0 for name in col}
    for date in pd.date_range(lowest_datetime,biggest_datetime,freq='10min'):
        if df['datetime'].isin([date]).any():
            continue
        col_map['datetime'] = date
        df = pd.concat([df,pd.DataFrame(col_map,index=[0])],axis=0, ignore_index= True)
    path = config['ProcessedDataPath'] + '\\' + file_name  
    df.to_csv(path,sep=',',index=False)
    print(file_name + ' normalized')



