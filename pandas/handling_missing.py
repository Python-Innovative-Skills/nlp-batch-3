import pandas as pd
import numpy as np

data = {"A":[1,np.nan,3,4],"B":[np.nan,'b',np.nan,'d'],"C":[1.1,np.nan,np.nan,4.1]}

df = pd.DataFrame(data)

# df_dropped = df.dropna(subset=['A'])

df_fill = df.bfill()


# print(df)
# print(df_fill)

#interpolate, polynomial, spline, time-series

custom_fill ={
    "A": df['A'].mean(),
    "B":"unknown",
    "C":df['C'].median()
}

custom_fill_df= df.fillna(value=custom_fill)
print(custom_fill_df)