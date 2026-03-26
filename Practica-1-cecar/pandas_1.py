import pandas as pd
from datadata import estudiantes
df = pd.DataFrame(estudiantes)  
# print(df)
# df.info()
# print(df.isna().sum())
# print(df.isna().sum().sum())
# print(df.isna().mean()*100)
# print(df[df.isna().all(axis=1)])
df= df.dropna(how='all')
df.info()
print(df[df.isna().all(axis=1)])