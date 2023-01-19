#Program to Read any csv file to its maximum(Pandas)
import pandas as pd
df = pd.read_csv('govtData.csv')
print(df.to_string())