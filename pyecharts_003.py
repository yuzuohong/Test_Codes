# -*- coding: utf-8 -*-

import pandas as pd
from pandas import DataFrame
from pyecharts import Bar, Grid, Page

# dataframe preparation
data = pd.read_excel('D:\Python\Test_Codes\\workload.XLSX', sheet_name='Sheet2', header=0)
df_raw = DataFrame(data)

# General settings of chart overview
bar1 = Bar(title='Number of Dialog Steps',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar1.use_theme('essos')

bar1.add('Number of Dialog Steps',
         df_raw['Task Type Name'], df_raw['Number of Dialog Steps'],
         is_stack=True,
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=20,
         xaxis_name_size=8)

bar2 = Bar(title='Average response Time/Dialog Step (ms)',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar2.use_theme('essos')

bar2.add('Average response Time/Dialog Step (ms)',
         df_raw['Task Type Name'], df_raw['Average response Time/Dialog Step (ms)'],
         is_stack=True,
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=20,
         xaxis_name_size=8)

bar3 = Bar(title='Avg. Processing Time',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar3.use_theme('essos')

bar3.add('Avg. Processing Time',
         df_raw['Task Type Name'], df_raw['Avg. Processing Time'],
         is_stack=True,
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=20,
         xaxis_name_size=8)

grid = Grid()

grid.add(bar1, grid_top='30%')
grid.add(bar2, grid_top='90%')
grid.add(bar3, grid_top='100%')
# grid.add(bar4,grid_bottom='60%')
# grid.add(bar5,grid_bottom='60%')
# grid.add(bar6,grid_bottom='60%')


grid.render('D:\\temp\\render_2.html')
