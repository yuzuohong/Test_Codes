import pandas as pd

sourcefile = 'D:\\1.xlsx'
destfile = 'D:\\2.xlsx'

#change xxx with the sheet name that includes the data
data = pd.read_excel(sourcefile, sheet_name="1")

#save it to the 'new_tab' in destfile
data.to_excel(destfile, sheet_name='new_tab')
