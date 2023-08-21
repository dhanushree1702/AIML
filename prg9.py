#Panda series using numpy array
import numpy as np
import pandas as pd

info=np.array([10,20,30,40])
s=pd.Series(info)
print(s)
print()

a=pd.Series(4,index=[0,1,2,3])
print(a)
print()

i=pd.Index([2,1,1,np.nan,3])
print(i.value_counts())
print()

ser1=pd.Series([10,1,3,6])
ser2=pd.Series([10,5,6,9])
print(ser1)
print(ser2)

