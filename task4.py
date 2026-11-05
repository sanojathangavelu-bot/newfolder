import numpy as np
import pandas as pd



df4=df[(df["Sex"]=="male")&(df["Survived"]==0)]
print(df4)

df5=df[(df["Sex"]=="female")&df["Survived"]==1]
print(df5)

df6=df[(df["Survived"]==0)]
print(df6)

df7=df[(df["Survived"]==1)]
print(df7)

df8=df[(df["Age"]>30)]
print(df8)


miss=df.isnull().sum()
print(miss)

age=df["Age"].isnull().sum()
print(age)

dup=df.duplicated().sum()
print(dup)

age=df["Age"].notnull()
print(age)


avg=df["Age"].mean()
print(avg)

ma=df["Fare"].max()
print(ma)

mi=df["Fare"].min()
print(mi)

aver=np.mean(df['Fare'])
print(aver)

sur=[(df["Survived"]==1).sum()]
print(sur)

sur=[(df["Survived"]==1).mean()]
print(sur)



female=df[(df["Sex"]=="female")&(df["Survived"]==1)&(df["Age"]>25)]
print(female)

male=df[(df["Sex"]=="male")&(df["Fare"]>50)&(df["Survived"]==0)]
print(male)













