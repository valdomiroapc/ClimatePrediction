import pandas as pd
import yaml
from Climate_Variable import ClimateVariable

class SolarIrradiance2(ClimateVariable):
    pass

obj = SolarIrradiance2()
obj.loadData()
print(obj.getData())
        