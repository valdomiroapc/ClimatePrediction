from msilib import Directory
from operator import index
from subprocess import CompletedProcess
import pandas as pd
import glob

directory = r"C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Model\ClimateData\PCD_Itumbiara"
completeDataframe = pd.DataFrame()
for path in glob.glob(directory + "\*.csv"):
	currentDF = pd.read_csv(path)
	completeDataframe = pd.concat([completeDataframe,currentDF])
	print('merged:',path)

print(completeDataframe)

completeDataframe.to_csv("ItumbiaraCompleteDataframe.csv",index=False)
print('uai')