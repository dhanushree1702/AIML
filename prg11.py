import pandas as pd
import numpy as np

data=pd.read_csv("C:/Users/SPTINT-09/Downloads/titanic.csv",index_col='Name')
print(data)
print(" ")
print(data.shape)
print(" ")
print(data.info())
print(" ")
print(data.head(10))
print(" ")
print(data.head(5))
print(" ")
print(data[['Age','Survived']])
print(data.loc[data['Age']>50])
