# -*- coding: latin-1 -*-
import pandas as pd
import glob
import yaml

with open(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Configuration\Configfile.yaml') as configFile:
	config = yaml.load(configFile, Loader=yaml.FullLoader)

directory = config['SourceDataPath']
solar_irradiance2 = pd.DataFrame()
for path in glob.glob(directory + "\*.csv"):
	currentDF = pd.read_csv(path,encoding='utf-8', low_memory=False)
	updated_df = currentDF.filter(regex='(.*2.*solar_irradiance.*)|(.*time.*)')
	updated_df = updated_df.dropna(axis=0)
	if "Date/time" in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Date/time':"datetime"})
	if 'Piranômetro - 2;solar_irradiance;Avg (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 2;solar_irradiance;Avg (W/m²)':'Piranômetro - 2;solar_irradiance;Avg'})
	if 'Piranômetro - 2;solar_irradiance;Min (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 2;solar_irradiance;Min (W/m²)':'Piranômetro - 2;solar_irradiance;Min'})
	if 'Piranômetro - 2;solar_irradiance;Max (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 2;solar_irradiance;Max (W/m²)':'Piranômetro - 2;solar_irradiance;Max'})
	if 'Piranômetro - 2;solar_irradiance;StdDev (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 2;solar_irradiance;StdDev (W/m²)':'Piranômetro - 2;solar_irradiance;StdDev'})
	if 'Piranômetro - 2;solar_irradiance;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 2;solar_irradiance;Count ()':'Piranômetro - 2;solar_irradiance;Count'})
	solar_irradiance2 = pd.concat([solar_irradiance2,updated_df])

solar_irradiance2 = solar_irradiance2.rename(columns = 
											 {
												 'Piranômetro - 2;solar_irradiance;Avg': 'avg',
												 'Piranômetro - 2;solar_irradiance;Min': 'min',
												 'Piranômetro - 2;solar_irradiance;Max': 'max',
												 'Piranômetro - 2;solar_irradiance;StdDev': 'stddev',
												 'Piranômetro - 2;solar_irradiance;Count': 'count'
												 })
savePath = config['ParsedDataPath'] + r'\solar_irradiance_2_data.csv'
solar_irradiance2.to_csv(savePath,sep=',',index=False)
print('instrument 2 solar irradiance data parsed and saved')