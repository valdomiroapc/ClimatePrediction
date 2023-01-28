# -*- coding: latin-1 -*-
import pandas as pd
import glob

directory = r"C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\PCD_Itumbiara"
solar_irradiance2 = pd.DataFrame()
for path in glob.glob(directory + "\*.csv"):
	currentDF = pd.read_csv(path,encoding='utf-8', low_memory=False)
	print(currentDF.columns)
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
	

print(solar_irradiance2)
solar_irradiance2.to_csv('Itumbiara_solar_irradiance2.csv',sep=',',index=False)

Index(['Date/time', 'Anemômetro;wind_speed;Avg', 'Anemômetro;wind_speed;Max',
       'Anemômetro;wind_speed;Min', 'Anemômetro;wind_speed;StdDev',
       'Anemômetro;wind_speed;Count', 'Temperatura / Umidade;humidity;Avg',
       'Temperatura / Umidade;humidity;Max',
       'Temperatura / Umidade;humidity;Min',
       'Temperatura / Umidade;humidity;StdDev',
       'Temperatura / Umidade;humidity;Count',
       'Temperatura / Umidade;temperature;Avg',
       'Temperatura / Umidade;temperature;Max',
       'Temperatura / Umidade;temperature;Min',
       'Temperatura / Umidade;temperature;StdDev',
       'Temperatura / Umidade;temperature;Count',
       'Piranômetro - 1;solar_irradiance;Avg',
       'Piranômetro - 1;solar_irradiance;Max',
       'Piranômetro - 1;solar_irradiance;Min',
       'Piranômetro - 1;solar_irradiance;StdDev',
       'Piranômetro - 1;solar_irradiance;Count',
       'Piranômetro - 2;solar_irradiance;Avg',
       'Piranômetro - 2;solar_irradiance;Max',
       'Piranômetro - 2;solar_irradiance;Min',
       'Piranômetro - 2;solar_irradiance;StdDev',
       'Piranômetro - 2;solar_irradiance;Count',
       'Pluviômetro;precipitation;Count', 'Pluviômetro;precipitation;Sum',
       'Abertura_porta;status;Count', 'Abertura_porta;status;Sum',
       'Botão de Limpeza;status;Count', 'Botão de Limpeza;status;Sum',
       'A1;Avg', 'A1;Max', 'A1;Min', 'A1;StdDev', 'A1;Count', 'A2;Avg',
       'A2;Max', 'A2;Min', 'A2;StdDev', 'A2;Count', 'A3;Avg', 'A3;Max',
       'A3;Min', 'A3;StdDev', 'A3;Count', 'A4;Avg', 'A4;Max', 'A4;Min',
       'A4;StdDev', 'A4;Count', 'C1;Avg', 'C1;Max', 'C1;Min', 'C1;StdDev',
       'C1;Count', 'C2;Avg', 'C2;Max', 'C2;Min', 'C2;StdDev', 'C2;Count',
       'D1;Avg', 'D1;Max', 'D1;Min', 'D1;StdDev', 'D1;Count', 'D2;Avg',
       'D2;Max', 'D2;Min', 'D2;StdDev', 'D2;Count', 'V;Avg', 'V;Max', 'V;Min',
       'I;Avg', 'I;Max', 'I;Min', 'T;Avg', 'addr'],
      dtype='object')