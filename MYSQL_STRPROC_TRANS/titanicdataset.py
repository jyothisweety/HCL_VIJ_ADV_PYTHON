import pandas as pd
import numpy as np
df=pd.read_csv('..//data//tested.csv')#loading data by using read_csv
#print(df)
#print(df.isna())#displays which one is true/false like boolean
print(df.shape)#displays rows and columns
df.drop(['Cabin'],axis=1,inplace=True)
df.fillna(method='ffill',inplace=True)
#print(df.isna().sum())
#print(df['Embarked'])
#print(pd.crosstab(index=df['Sex'],columns=df['Survived']))
#print(df.groupby(['Sex','Survived'])['Survived'].count())
#print(df.groupby(['Embarked','Sex'])['Sex'].count())
#print(pd.crosstab(index=df['Embarked'],columns=df['Sex']))
#print(pd.pivot_table(df,index=['Sex','Age'],aggfunc=np.sum))
#print(df.sort_values(by=['Pclass','Age'],ascending=False))
df['Survived']=df["Survived"].apply(lambda val:'Yes' if val==1 else 'No')
print(df)