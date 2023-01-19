#Program to Read any csv file to its maximum(Pandas),&limit the number of rows readed
import pandas as pd
df = pd.read_csv('govtData.csv',nrows=10)
print(df.to_string())