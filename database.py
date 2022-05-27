#! /usr/bin/env python3

import mysql.connector


class Database():
     def __init__(self):
        try:
            self.db_connection = mysql.connector.connect(
            host="localhost",
            user="mohamed",
            password="Printf(01276316958)",
            database='emps_db',
            auth_plugin='mysql_native_password' 
            )
            print("Connected")
        except:
            print("Can't connect to database")
            

     def insert_emp(self,id,name,email,workmood,salary,is_manager,office_id):
        try:
            cur = self.db_connection.cursor()
            cur.execute('''Insert into employee (id,name, email, workmood, salary,is_manager,office_id)
                values({},'{}', '{}', '{}', '{}',{},{})
                '''.format(id,name, email, workmood, salary,is_manager,office_id))
            self.db_connection.commit()
        except:
            print('error in database')
      


     def insert_office(self,id,name,location):
        try:
            cur = self.db_connection.cursor()
            cur.execute('''Insert into office (id,name,location)
                values({},'{}', '{}')
                '''.format(id,name, location))
            self.db_connection.commit()
        except:
             print('error in database')


     def get_emp(self,name):
        try:
            cur = self.db_connection.cursor()
            cur.execute('''select * from employee where name='{}'
                '''.format(name))
            rows = cur.fetchall()
            for row in rows:
                if(row[5]==0):
                    return(row[0], row[1], row[2],row[3], row[4], row[5],row[6])
                else:
                    return(row[0], row[1], row[2],row[3],row[5],row[6])
        except:
             print('error in database')
    
     def get_all_emps(self):
        try:
            cur = self.db_connection.cursor()
            cur.execute('''select * from employee ''')
            rows = cur.fetchall()
            for row in rows:
                 print(row[0], row[1], row[2],row[3], row[4], row[5],row[6])
        except:
             print('error in database')


     def delete_emp(self,empid):
        try:
            cur = self.db_connection.cursor()
            cur.execute('''delete from employee where id={}'''.format(empid))
            self.db_connection.commit()
            print('deleted')
        except:
             print('error in database')




# d1=Database()
# # d1.insert_office(1,'office1','alex')
# # d1.insert_emp(70,'mohamed','mohamedgmail','moded',1000,True,1)
# d1.get_all_emps()
# d1.fire(50)
# d1.get_all_emps()
