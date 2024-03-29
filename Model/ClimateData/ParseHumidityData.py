# -*- coding: latin-1 -*-
import pandas as pd
import glob
import yaml

with open(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Configuration\Configfile.yaml') as configFile:
	config = yaml.load(configFile, Loader=yaml.FullLoader)

directory = config['SourceDataPath']
humidity_data = pd.DataFrame()
for path in glob.glob(directory + "\*.csv"):
	currentDF = pd.read_csv(path,encoding='utf-8', low_memory=False)
	updated_df = currentDF.filter(regex='(.*humidity.*)|(.*time.*)')
	updated_df = updated_df.dropna(axis=0)
	if "Date/time" in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Date/time':"datetime"})
	if 'Temperatura / Umidade;humidity;Avg (%)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;humidity;Avg (%)':'Temperatura / Umidade;humidity;Avg'})
	if 'Temperatura / Umidade;humidity;Min (%)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;humidity;Min (%)':'Temperatura / Umidade;humidity;Min'})
	if 'Temperatura / Umidade;humidity;Max (%)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;humidity;Max (%)':'Temperatura / Umidade;humidity;Max'})
	if 'Temperatura / Umidade;humidity;StdDev (%)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;humidity;StdDev (%)':'Temperatura / Umidade;humidity;StdDev'})
	if 'Temperatura / Umidade;humidity;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;humidity;Count ()':'Temperatura / Umidade;humidity;Count'})
	humidity_data = pd.concat([humidity_data,updated_df])
	
humidity_data = humidity_data.rename(columns= 
									 {
										 'Temperatura / Umidade;humidity;Avg':'avg',
										 'Temperatura / Umidade;humidity;Min':'min',
										 'Temperatura / Umidade;humidity;Max':'max',
										 'Temperatura / Umidade;humidity;StdDev':'stddev',
										 'Temperatura / Umidade;humidity;Count':'count'
										 })
savePath=config['ParsedDataPath'] + r'\humidity.csv'
humidity_data.to_csv(savePath,sep=',',index=False)

print('humidity data parsed and saved')