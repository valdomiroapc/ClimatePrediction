import pandas as pd
import yaml
from Climate_Variable import ClimateVariable

class Humidity(ClimateVariable):
    pass

obj = Humidity()
obj.loadData()
print(obj.getData())
        