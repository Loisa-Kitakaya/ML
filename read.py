import pandas as pd

path = input ("Enter path/to/csv/file.csv: ")

read = pd.read_csv(path)

print (read)