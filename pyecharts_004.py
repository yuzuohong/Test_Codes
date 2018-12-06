# -*- coding: utf-8 -*-

import pandas as pd
from pandas import DataFrame
from pyecharts import Bar, Grid, Page

page = Page()

# dataframe preparation
data = pd.read_excel('D:\Python\Test_Codes\\workload.XLSX', sheet_name='Sheet2', header=0)
df_raw = DataFrame(data)

# Create subplots for the page

df_raw = df_raw.sort_values('Number of Dialog Steps')
bar1 = Bar(title='Number of Dialog Steps',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar1.use_theme('vintage')

bar1.add('Number of Dialog Steps',
         df_raw['Task Type Name'], df_raw['Number of Dialog Steps'],
         is_stack=True,
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=30,
         xaxis_name_size=5)
page.add(bar1)

df_raw = df_raw.sort_values('Average response Time/Dialog Step (ms)')
bar2 = Bar(title='Average response Time/Dialog Step (ms)',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar2.use_theme('macarons')

bar2.add('Average response Time/Dialog Step (ms)',
         df_raw['Task Type Name'], df_raw['Average response Time/Dialog Step (ms)'],
         is_stack=True,
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=30,
         xaxis_name_size=5)
page.add(bar2)

df_raw = df_raw.sort_values('Avg. Processing Time')
bar3 = Bar(title='Avg. Processing Time',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar3.use_theme('infographic')

bar3.add('Avg. Processing Time',
         df_raw['Task Type Name'], df_raw['Avg. Processing Time'],
         is_stack=True,
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=30,
         xaxis_name_size=5)
page.add(bar3)

df_raw = df_raw.sort_values('Average CPU Time (ms)')
bar4 = Bar(title='Average CPU Time (ms)',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar4.use_theme('roma')

bar4.add('Average CPU Time (ms)',
         df_raw['Task Type Name'], df_raw['Average CPU Time (ms)'],
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=30,
         xaxis_name_size=5)
page.add(bar4)

df_raw = df_raw.sort_values('Average CPU Time (ms)')
bar5 = Bar(title='Average CPU Time (ms)',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar5.use_theme('westeros')

bar5.add('Average CPU Time (ms)',
         df_raw['Task Type Name'], df_raw['Average CPU Time (ms)'],
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=30,
         xaxis_name_size=5)
page.add(bar5)

df_raw = df_raw.sort_values('Requested Data (KB)')
bar6 = Bar(title='Requested Data (KB)',
           title_pos='left',
           width=1000,
           height=500,
           renderer='canvas')

bar6.use_theme('wonderland')

bar6.add('Requested Data (KB)',
         df_raw['Task Type Name'], df_raw['Requested Data (KB)'],
         mark_line=['average', 'max'],
         mark_point=['max'],
         mark_point_symbolsize=100,
         is_label_show=True,
         legend_selectedmode='single',
         legend_pos=400,
         xaxis_rotate=30,
         xaxis_name_size=5)
page.add(bar6)

page.page_title = 'System Performance Overview'
page.render('D:\\temp\\render_4.html')
