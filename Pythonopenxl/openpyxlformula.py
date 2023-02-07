import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook('..//data//Book3.xlsx')
sheet=wb.active
sheet["A7"]='=SUM(A1:A6)'
#sheet.append['A8']='=SUM(A1:A6)'
wb.save("..//data//Book1.xlsx")