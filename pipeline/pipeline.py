import sys
print("arguments", sys.argv)

month= int(sys.argv[1])

print(f'hello pipeline, month={month}')


import pandas as pd

df = pd.DataFrame({"A": [1, 2], "num_passengers": [3, 4]})
df['month'] = month

print(df.head())

df.to_parquet(f"output_{month}.parquet")

print(f'hello pipeline, month={month}')