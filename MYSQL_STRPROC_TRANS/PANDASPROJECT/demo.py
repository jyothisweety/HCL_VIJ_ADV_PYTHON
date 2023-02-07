import pandas as pd
import numpy as np
df=pd.read_csv("..//data/BOOK1.csv")
df['Total']=df.iloc[:].sum(axis=1)
df['avg']=df['Total']/5
df['Rank']=df['avg'].rank()
df['Result']=np.where((df['M1']>=35 and df['M2']>=35 and df['M3']>=35 and df['M4']>=35 and df['M5']>=35),"Pass","Fail")
print(df.sort_values(by=['Rank']))