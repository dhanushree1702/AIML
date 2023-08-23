import pandas as pd
import numpy as np
dict={'first score':[10,20,np.nan,30],
      'second score':[np.nan,10,20,30],
      'third score':[np.nan,20,30,np.nan]}

data=pd.DataFrame(dict)
print(data)
print(" ")
print(data.isnull())
print(" ")
print(data.notnull())
print(" ")
print(data.fillna(20))
print(" ")
print(data.fillna(method="pad"))
print(" ")
print(data.fillna(method="bfill"))
print(" ")
print(data.replace(to_replace=np.nan,value=-99))
