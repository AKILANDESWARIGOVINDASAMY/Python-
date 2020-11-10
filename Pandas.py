import pandas as pd
import numpy as np
df = pd.read_csv('C:\\Users\\Akila\\Downloads\\nba.csv') #original values
data = pd.DataFrame(df,columns=['Name','Age']) #only name and age
a=data.head(10)
print(a)
#a.replace(to_replace=['29.0'],value=['35'],inplace=True)
b=a
b.at[5,'Age']=35
#a=a.replace(29,35)
#a.replace({'Age':{29.0:35}})
print(b)
c=df.isnull().sum() #count of null in each column
print(c-1)
d=df.loc[15:29,['Team','Salary']].mean()
print(d)
e=df.groupby('Team').count() #count of members in each team
e=e['Name']
print(e)
f=df['Age']
f.astype(int,errors='ignore')
print(f.dtypes)
g=df
g.sort_values(["Salary","Name"],axis=0,ascending=[False,True],inplace=True)
print(g.head(3))
#h.sort_values(["Age","Name"],axis=0,ascending=[False,True],inplace=True)
h=df[df.Age>35]
h=pd.DataFrame(h,columns=['Name','Age'])
print(h)
i=pd.merge()

