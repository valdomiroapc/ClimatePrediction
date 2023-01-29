# -*- coding: latin-1 -*-
import pandas as pd
import glob

directory = r"C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\PCD_Itumbiara"
temperature_data = pd.DataFrame()
for path in glob.glob(directory + "\*.csv"):
	currentDF = pd.read_csv(path,encoding='utf-8', low_memory=False)
	updated_df = currentDF.filter(regex='(.*temperature.*)|(.*time.*)')
	updated_df = updated_df.dropna(axis=0)
	if "Date/time" in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Date/time':"datetime"})
	if 'Temperatura / Umidade;temperature;Avg (°C)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;temperature;Avg (°C)':'Temperatura / Umidade;temperature;Avg'})
	if 'Temperatura / Umidade;temperature;Min (°C)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;temperature;Min (°C)':'Temperatura / Umidade;temperature;Min'})
	if 'Temperatura / Umidade;temperature;Max (°C)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;temperature;Max (°C)':'Temperatura / Umidade;temperature;Max'})
	if 'Temperatura / Umidade;temperature;StdDev (°C)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;temperature;StdDev (°C)':'Temperatura / Umidade;temperature;StdDev'})
	if 'Temperatura / Umidade;temperature;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Temperatura / Umidade;temperature;Count ()':'Temperatura / Umidade;temperature;Count'})
	temperature_data = pd.concat([temperature_data,updated_df])
	
temperature_data = temperature_data.rename(columns = 
										   {
												'Temperatura / Umidade;temperature;Avg': 'avg',
												'Temperatura / Umidade;temperature;Min': 'min',
												'Temperatura / Umidade;temperature;Max': 'max',
												'Temperatura / Umidade;temperature;StdDev': 'stddev',
												'Temperatura / Umidade;temperature;Count': 'count'
											})
temperature_data.to_csv(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\Itumbiara_parsed_data\Itumbiara_temperature_data.csv',sep=',',index=False)
print('temperature data parsed and saved')

