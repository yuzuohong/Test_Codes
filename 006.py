import xlwt
from datetime import datetime

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='DD-MMM-YYYY')
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
ws.write(0,0,1234.56)
ws.write(1,0,datetime.now())
ws.write(2,0,1)
ws.write(2,1,1)
ws.write(2,2,xlwt.Formula('A3+B3'))

wb.save('temp1.xls')
