# -*- coding: utf-8 -*-

import pandas as pd
from pandas import DataFrame
from pyecharts import Bar, Grid
import time

# dataframe preparation
data = pd.read_excel('D:\Python\Test_Codes\\workload.XLSX', sheet_name='Sheet2', header=0)
df_raw = DataFrame(data)

# General settings of chart overview
bar = Bar(title='System Workload Overview',
          title_pos='left',
          subtitle='Data Source: 201809 \n' + 'Chart was generated at ' + time.strftime('%Y.%m.%d %H.%M.%S'),
          width=1200,
          height=600,
          renderer='canvas',
          page_title='test page by yu')

bar.use_theme('essos')

# Definition of each chart
for i in range(len(df_raw.columns) - 1):

    df_x = df_raw[df_raw.columns[0]]
    df_y = df_raw[df_raw.columns[i + 1]]
    bar.add(df_raw.columns[i + 1],
            df_x, df_y,
            is_stack=True,
            mark_line=['average', 'max'],
            mark_point=['max'],
            mark_point_symbolsize=100,
            is_label_show=True,
            legend_selectedmode='single',
            legend_pos=400,
            xaxis_rotate=20,
            xaxis_name_size=8)

bar.render('D:\\temp\\render_1.html')
