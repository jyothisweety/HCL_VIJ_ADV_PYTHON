import pandas as pd
import numpy as np
data1=pd.read_excel("d://data/Book1.xlsx")
data2=pd.read_excel("D://data/Book3.xlsx")
print(data1)
print(data2)
data1['Price_1']=np.where(data1['Price']==data2['Price'],0,data2['Price']-data1['Price'])
print(data1)
print(data1.compare(data2))
data1.to_excel("d://data/price.xlsx",sheet_name='Price_list',index=False)
print(data1.to_dict())
print(data1.to_html("demo.html"))