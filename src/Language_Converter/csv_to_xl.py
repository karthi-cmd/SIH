import pandas as pd
import numpy as np

# Reading the csv file
df_new = pd.read_csv('file_path_of_csv')

# saving xlsx file
GFG = pd.ExcelWriter('file_path_of_xlsx')
df_new.to_excel(GFG, index = False) 

GFG.save()