import pandas as pd
from datadata import estudiantes
df = pd.DataFrame(estudiantes)  
print(df)
df.info()