from mysql.connector import Error
from hcl_database_connection import MysqlDatabaseConnection
class HclstoredProcedure(MysqlDatabaseConnection):
    def execute_str_procedure(self):
        try:
            self.cursor.callproc("get_cust_dtls",args=mydata)
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()

connect_obj=HclstoredProcedure()
connect_obj.connect("localhost","root","Jyo@#$767207","hcl_vijayawada")
print(connect_obj)