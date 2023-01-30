# -*- coding: latin-1 -*-
import pandas as pd
import glob
import yaml
with open(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Configuration\Configfile.yaml') as configFile:
	config = yaml.load(configFile, Loader=yaml.FullLoader)

directory = config['SourceDataPath']
solar_irradiance1 = pd.DataFrame()
for path in glob.glob(directory + "\*.csv"):
	currentDF = pd.read_csv(path,encoding='utf-8', low_memory=False)
	updated_df = currentDF.filter(regex='(.*1.*solar_irradiance.*)|(.*time.*)')
	updated_df = updated_df.dropna(axis=0)
	if "Date/time" in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Date/time':"datetime"})
	if 'Piranômetro - 1;solar_irradiance;Avg (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 1;solar_irradiance;Avg (W/m²)':'Piranômetro - 1;solar_irradiance;Avg'})
	if 'Piranômetro - 1;solar_irradiance;Min (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 1;solar_irradiance;Min (W/m²)':'Piranômetro - 1;solar_irradiance;Min'})
	if 'Piranômetro - 1;solar_irradiance;Max (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 1;solar_irradiance;Max (W/m²)':'Piranômetro - 1;solar_irradiance;Max'})
	if 'Piranômetro - 1;solar_irradiance;StdDev (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 1;solar_irradiance;StdDev (W/m²)':'Piranômetro - 1;solar_irradiance;StdDev'})
	if 'Piranômetro - 1;solar_irradiance;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 1;solar_irradiance;Count ()':'Piranômetro - 1;solar_irradiance;Count'})
	solar_irradiance1 = pd.concat([solar_irradiance1,updated_df])
	
solar_irradiance1 = solar_irradiance1.rename(columns= 
											 {
												 'Piranômetro - 1;solar_irradiance;Avg': 'avg',
												 'Piranômetro - 1;solar_irradiance;Min': 'min',
												 'Piranômetro - 1;solar_irradiance;Max': 'max',
												 'Piranômetro - 1;solar_irradiance;StdDev': 'stddev',
												 'Piranômetro - 1;solar_irradiance;Count': 'count'
												 })
savePath = config['ParsedDataPath'] + r'\solar_irradiance_1_data.csv'
solar_irradiance1.to_csv(savePath,sep=',',index=False)
print('instrument 1 solar irradiance data parsed and saved')

