#Data Visualization
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:/Users/SPTINT-09/Desktop/tips (1).csv')
plt.scatter(data['day'],data['tip'])
plt.show()
plt.plot(data['tip'])
plt.plot(data['size'])
plt.show()
plt.bar(data['day'],data['tip'])
plt.show()
plt.hist(data['total_bill'])
plt.show()
