import pandas as pd
import yaml
from Climate_Variable import ClimateVariable

class SolarIrradiance1(ClimateVariable):
    pass

obj = SolarIrradiance1()
obj.loadData()
print(obj.getData())
        