import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('alldata.csv')
#df.head()
df.columns = ['Date','Tweet','Tweet_Id','User_Id']
#df.head()
A = df.Date.str.slice(3,10)
#df.groupby(A)['Tweet_Id'].count()
df.groupby(A).User_Id.count().plot(kind='line')
plt.xlabel('Date')
plt.ylabel('User_Id')
plt.show()
