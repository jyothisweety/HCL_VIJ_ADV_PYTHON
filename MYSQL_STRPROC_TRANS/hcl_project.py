from datetime import date, timedelta, datetime
from decimal import Decimal
from typing import Dict, Set

from hcl_database_connection import MysqlDatabaseConnection
class Booking(MysqlDatabaseConnection):
    def available_seats(self):
        try:
            self.cursor.callproc("get_no_avl_tkt")
            for r in self.cursor.stored_results():
                seats=r.fetchone()
            return seats
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def book(self):
        pass
b1=Booking()
b1.connect("localhost","root","Jyo@#$767207","hcl_vijayawada")
sts=b1.available_seats()

available_seats={}
available_seats['Train_name']=sts[0]
available_seats['seats']=sts[1]
print(available_seats)
