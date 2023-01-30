import pandas as pd
import yaml
from Climate_Variable import ClimateVariable

class Temperature(ClimateVariable):
    pass

obj = Temperature()
obj.loadData()
print(obj.getData())
        
