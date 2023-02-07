import pandas as pd
data=pd.read_csv("..//data/tips.csv")
#print(data.isna().any())#isna means na(not assigned) value is there or not it will check if nor shows false
#print(data.isna().sum())#it will give sum of na values
#ips_male_fm=data.filter(['tip','sex'])
#print(tips_male_fm.groupby('sex').sum())
#print(tips_male_fm.sex.value_counts())
#print(tips_male_fm.sex.value_counts(normalize=True))
#print(pd.crosstab(index=data['sex'],columns=data['smoker']))
#ay_wise=data.filter(['tip','day'])
#pint(day_wise.groupby('day').sum())
#rint(data.describe())#total description we gets
print(data.head())#we total details with day and time
