import pandas as pd
Team=["india","Australia","pakistan","srilanka","England"]
s=pd.Series(Team)
#print(s)
#print(s[0]) # (or)
#print(s[1]) (or)
#print(s[:2])  (or)
print(s.iloc[0])#labled(both rows and columns include) based selection we took iloc func()