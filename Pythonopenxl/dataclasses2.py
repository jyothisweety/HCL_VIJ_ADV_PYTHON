from dataclasses import dataclass
from openpyxl import Workbook
import pandas as pd
wb=Workbook()
sheet=wb.active
@dataclass

class FullSales():
    month:str
    profit:int
    loss:int
    unit_price:int
    quatity_on_hand:int=0

F=[FullSales('january',20000,1000,90000,1),FullSales('febrauary',30000,800,8000,2),FullSales('march',30000,800,8000,2),FullSales('april',30000,800,8000,2),FullSales('may',30000,800,8000,2),FullSales('june',30000,800,8000,2),FullSales('july',30000,800,8000,2),FullSales('August',30000,800,9000,2),FullSales('september',30000,800,80090,2),FullSales('october',30000,900,8000,2),FullSales('november',30000,800,80090,2,),FullSales('december',30000,800,80090,2)]
data=[[f.month,f.profit,f.loss,f.unit_price,f.quatity_on_hand]for f in F]
data=[['month','profit','loss','unit_price','quatity_on_hand']]+data

for d in data:
    sheet.append(d)

wb.save("..//data//dataclasses2.xlsx")
