import pandas as pd
import yaml
from Climate_Variable import ClimateVariable

class WindSpeed(ClimateVariable):
    pass

obj = WindSpeed()
obj.loadData()
print(obj.getData())
        