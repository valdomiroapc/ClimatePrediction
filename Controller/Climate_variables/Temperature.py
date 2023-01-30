import pandas as pd
import yaml
from Climate_Variable import ClimateVariable

class Temperature(ClimateVariable):
    def selfCorrelation(self):
        series = pd.Series(self._Data['avg'])
        correlation = []
        for i in range(1,1000):
            correlation.append(series.autocorr(lag=i))
        return correlation

obj = Temperature()
obj.loadData()
print(obj.selfCorrelation())
        
