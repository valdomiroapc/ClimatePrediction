# -*- coding: latin-1 -*-
import pandas as pd
import glob

directory = r"C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\PCD_Itumbiara"
precipitation_data = pd.DataFrame()
for path in glob.glob(directory + "\*.csv"):
	currentDF = pd.read_csv(path,encoding='utf-8', low_memory=False)
	updated_df = currentDF.filter(regex='(.*precipitation.*)|(.*time.*)')
	updated_df = updated_df.dropna(axis=0)
	if "Date/time" in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Date/time':"datetime"})
	if 'Pluviômetro;precipitation;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Pluviômetro;precipitation;Count ()':'Pluviômetro;precipitation;Count'})
	if 'Pluviômetro;precipitation;Sum (mm)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Pluviômetro;precipitation;Sum (mm)':'Pluviômetro;precipitation;Sum'})
	if 'Piranômetro - 2;precipitation;Max (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 2;precipitation;Max (W/m²)':'Piranômetro - 2;precipitation;Max'})
	if 'Piranômetro - 2;precipitation;StdDev (W/m²)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 2;precipitation;StdDev (W/m²)':'Piranômetro - 2;precipitation;StdDev'})
	if 'Piranômetro - 2;precipitation;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piranômetro - 2;precipitation;Count ()':'Piranômetro - 2;precipitation;Count'})
	precipitation_data = pd.concat([precipitation_data,updated_df])

precipitation_data = precipitation_data.rename(columns= 
											   {
												   'Pluviômetro;precipitation;Count': 'count',
												   'Pluviômetro;precipitation;Sum': 'sum',
												   'Piranômetro - 2;precipitation;Max': 'max',
												   'Piranômetro - 2;precipitation;StdDev': 'stddev',
												   'Piranômetro - 2;precipitation;Count': 'count'
												   })

precipitation_data.to_csv(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\Itumbiara_parsed_data\Itumbiara_precipitation_data.csv',sep=',',index=False)
print('precipitation data parsed and saved')