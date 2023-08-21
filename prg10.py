import numpy as np
import pandas as pd
ser1=pd.Series([10,1,3,6])
ser2=pd.Series([10,5,6,9])
uni=pd.Series(np.union1d(ser1,ser2))
print("union num: \n",uni)
print()
inter=pd.Series(np.intersect1d(ser1,ser2))
print("Intersection of arrays \n",inter)
print()
nc=uni[~uni.isin(inter)]
print("Not common in: \n",nc)
