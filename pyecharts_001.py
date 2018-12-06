import pandas as pd
from pyecharts import Bar,Line
import time

data = pd.read_excel('D:\Python\Test_Codes\\1.xlsx',sheet_name='Sheet1',header=0)

data_type = data['Object Type']

data_volume = data['Volume']

bar = Bar(title='Volume of Developments',
          subtitle='Data extraction from ERP ' + time.strftime('%Y.%m.%d %H.%M.%S'),
          width=1024,
          height=512,
          renderer='canvas',
          page_title='test page by yu')
bar.use_theme('light')
bar.add('developments',
        data_type,data_volume,
        is_stack=True,
        mark_line=['min','max'],
        is_label_show=True,
        is_datazoom_show=True,
        datazoom_type='both',
        xaxis_rotate=20,
        xaxis_name_size=8)

bar.render('D:\\temp\\render.html')
