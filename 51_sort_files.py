import pandas
from pandas import DataFrame

n = input("enter file path with name: ")
result = pandas.read_csv(n)
print(result)
sc = input("select column to sort values: ")
ad = input("Ascending(True) or Descending(False)?:  ")
result.sort_values(sc, ascending=bool(ad), inplace=True, na_position='last')
df = DataFrame(result)
export_csv = df.to_csv(n, index=None, header=True)
print(df)