import pandas as pd
import yaml

class ClimateVariable:
    def __init__(self):
        self._Data = pd.DataFrame()
        with open(r'C:\Users\vneto\Desktop\Personal files\Climate_prediction\valdomiroapc\ClimatePrediction\Configuration\Configfile.yaml') as configFile:
	        config = yaml.load(configFile, Loader=yaml.FullLoader)
        self._Path_to_data = config['ProcessedVariablesDataPath'][type(self).__name__]

    def loadData(self):
        self._Data = pd.read_csv(self._Path_to_data, low_memory= False)

    def getData(self):
        return self._Data

