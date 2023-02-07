import pandas as pd
d={'Team':["india","australia","pakistan","punjab","england"],'Rank':[1,2,3,4,5]}
df=pd.DataFrame(d)
#print(df) (or)
#df1=df.rename(columns={"Rank":"Ranking"})#if we want to rename
#df1=df.rename(columns={"Rank":"Ranking"},inplace=True)#inplace=permanant rename takes place for original one like df

#print(df)# or print(df1)
#print(df.loc[:,['Team']])
#print(df.loc[df['Ranking']>=3])
print(df)
#df.drop([0,2],axis=0,inplace=True)
df.drop(['Team'],axis=1,inplace=True)#drop to delete#if axis=0 rows will get as output,if axis=1 columns
print(df)