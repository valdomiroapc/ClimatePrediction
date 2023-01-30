import pandas as pd
import yaml
from Climate_Variable import ClimateVariable

class Precipitation(ClimateVariable):
    pass

obj = Precipitation()
obj.loadData()
print(obj.getData())
        