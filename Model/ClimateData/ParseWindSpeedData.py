# -*- coding: latin-1 -*-
from msilib import Directory
from operator import index
from subprocess import CompletedProcess
from tkinter import CURRENT
import pandas as pd
import glob

import yaml

with open(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Configuration\Configfile.yaml') as configFile:
	config = yaml.load(configFile, Loader=yaml.FullLoader)

directory = config['SourceDataPath']

wind_speed_data = pd.DataFrame()
for path in glob.glob(directory + "\*.csv"):
	currentDF = pd.read_csv(path,encoding='utf-8', low_memory=False)
	updated_df = currentDF.filter(regex='(.*wind_speed.*)|(.*time.*)')
	updated_df = updated_df.dropna(axis=0)
	if "Date/time" in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Date/time':"datetime"})
	if 'Anem�metro;wind_speed;Max (m/s)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Anem�metro;wind_speed;Max (m/s)':'Anem�metro;wind_speed;Max'})
	if 'Anem�metro;wind_speed;Avg (m/s)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Anem�metro;wind_speed;Avg (m/s)':'Anem�metro;wind_speed;Avg'})
	if 'Anem�metro;wind_speed;Min (m/s)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Anem�metro;wind_speed;Min (m/s)':'Anem�metro;wind_speed;Min'})
	if 'Anem�metro;wind_speed;StdDev (m/s)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Anem�metro;wind_speed;StdDev (m/s)':'Anem�metro;wind_speed;StdDev'})
	if 'Anem�metro;wind_speed;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Anem�metro;wind_speed;Count ()':'Anem�metro;wind_speed;Count'})
	wind_speed_data = pd.concat([wind_speed_data,updated_df])

wind_speed_data = wind_speed_data.rename(columns={
	'Anem�metro;wind_speed;Max': 'max',
	'Anem�metro;wind_speed;Avg': 'avg',
	'Anem�metro;wind_speed;Min': 'min',
	'Anem�metro;wind_speed;StdDev': 'stddev',
	'Anem�metro;wind_speed;Count': 'count'
})
savePath = config['ParsedDataPath'] + r'\wind_speed_data.csv'
wind_speed_data.to_csv(savePath,sep=',',index=False)
print('wind speed data parsed and saved')