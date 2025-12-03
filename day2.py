import pandas as pd

d = {"col1": [1,2,3], "col2": [21, 22, 23]}
df = pd.DataFrame(data=d)

print(df)
count = df.shape[1]
print(count)
mean = df['col2'].mean()
print(mean)