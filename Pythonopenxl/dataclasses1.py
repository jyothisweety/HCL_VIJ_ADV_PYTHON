from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass

class People():
    name:str
    num:int
    age:int=0
p=People('jyothi',24,22)
P=[People('steve',1,23),People('Raju',2,34),People('Rahul',3,25)]
data=[[p.name,p.num,p.age]for p in P]
data=[['Name','Num','Age']]+data
print(p)
for d in data:
    sheet.append(d)
wb.save("..//data//dataclasses1.xlsx")

