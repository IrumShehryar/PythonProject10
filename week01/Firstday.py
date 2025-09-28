import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("../AI with Python/iris.csv")
"""print(df.head())
print(df.tail())
print(df.describe)
print(df.dtypes)
print(df.index)
print(df.columns)
print(df.values)"""
df2=df.sort_values('sepal_width',ascending=False)
print(df2)
print(df[['sepal_width','sepal_length']])
print(df[15:20])
print(df.loc[15:20,['sepal_width']])
print(df.iloc[15:20,[0,1]])
print(df[df.sepal_width > 4])
print(df[df["species"].isin(["Iris-setosa"])])
df['sepal_area'] = df['sepal_width']*df['sepal_length']
print(df)
df.to_csv("Irum-dataset.csv") # save to csv file
to_append = [5.1,6.1,7.1,8.1,9.1,"new_line"]
"""df.loc[len(df)] = to_append
print(df)"""
df=df.drop(["sepal_area"],axis=1)
print(df)
df=df.rename(columns={'sepal_length': 'sep_len'}) #better approach
print(df)
df.columns=['1','2','3','4','5'] # to rename all the columns
print(df.head())
print("reading rows")
for ind,row in df.iterrows():
    print(ind,row)
