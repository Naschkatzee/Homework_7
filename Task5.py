import pandas as pd

read_file = pd.read_excel (r'C:\Users\Tatsiana\Homework_7\data.xlsx')
read_file.to_csv (r'C:\Users\Tatsiana\Homework_7\data.csv', index = None, header=True)

