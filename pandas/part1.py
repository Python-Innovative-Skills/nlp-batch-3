import pandas as pd

data ={"Name":['A','B','C'], "Age":[1,2,3],"Dept":["X","Y","Z"]}

df = pd.DataFrame(data)

df["Salary"] = [5000,6000,7000]


df.drop([0,2],axis=0,inplace=True)

print(df)

# print(df[['Name','Age']])