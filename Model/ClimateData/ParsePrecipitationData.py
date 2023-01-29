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
	if 'Pluvi�metro;precipitation;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Pluvi�metro;precipitation;Count ()':'Pluvi�metro;precipitation;Count'})
	if 'Pluvi�metro;precipitation;Sum (mm)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Pluvi�metro;precipitation;Sum (mm)':'Pluvi�metro;precipitation;Sum'})
	if 'Piran�metro - 2;precipitation;Max (W/m�)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piran�metro - 2;precipitation;Max (W/m�)':'Piran�metro - 2;precipitation;Max'})
	if 'Piran�metro - 2;precipitation;StdDev (W/m�)' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piran�metro - 2;precipitation;StdDev (W/m�)':'Piran�metro - 2;precipitation;StdDev'})
	if 'Piran�metro - 2;precipitation;Count ()' in updated_df.columns:
		updated_df = updated_df.rename(columns= {'Piran�metro - 2;precipitation;Count ()':'Piran�metro - 2;precipitation;Count'})
	precipitation_data = pd.concat([precipitation_data,updated_df])

precipitation_data = precipitation_data.rename(columns= 
											   {
												   'Pluvi�metro;precipitation;Count': 'count',
												   'Pluvi�metro;precipitation;Sum': 'sum',
												   'Piran�metro - 2;precipitation;Max': 'max',
												   'Piran�metro - 2;precipitation;StdDev': 'stddev',
												   'Piran�metro - 2;precipitation;Count': 'count'
												   })

precipitation_data.to_csv(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\Itumbiara_parsed_data\Itumbiara_precipitation_data.csv',sep=',',index=False)
print('precipitation data parsed and saved')