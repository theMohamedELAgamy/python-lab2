#! /usr/bin/env python3
import enum
from inspect import isdatadescriptor
from database import *
from person import *
from office import Office

class Employee(Person):
    db=Database()

    def __init__(self):
        self.id=input('enterid:')
        full_name=input('entername:')
        self.email=input('email:')
        self.workmood=input('workmood:')
        self.salary=input('salary:')
        self.office=input('office id:')
        manager=input('is_manager (yes/no):')
        if(manager=='yes'):
            self.is_manager=True
        else:
            self.is_manager=False
        super().__init__(full_name,self.salary,sleepmood='unKnown',healthRate='unKnown')
        Employee.db.insert_emp(self.id,full_name,self.email,self.workmood,self.salary,self.is_manager,self.office)
         
    @staticmethod
    def hire():
        emp=Employee()

    @staticmethod
    def get_employee(name):
        return Employee.db.get_emp(name)
    
    @staticmethod
    def get_all():
        return Employee.db.get_all_emps()
    @staticmethod
    def fire(id):
        return Employee.db.delete_emp(isdatadescriptor)

    def sendEmail(self,subject,bodyreceiver_name):
        name=self.full_name
        f2=open('emails.txt','a')
        
        f2.write('''name={}
                subject={}
                to={}
        '''.format(name,subject,bodyreceiver_name))
        
        f2.close()

emp=Employee()
emp.sendEmail('email subject','ali')

def menue():
    while(True):
        print('''
        1-add emp
        2-select
        3-select all
        4-fire
        5-add office
        6-quit
        ''')
        x=input()
        if(x=='add'):
            Employee.hire()
        if(x=='select'):
            y=input('enter name: ')
            print(Employee.get_employee(y))
            p=input()
        if(x=='select all'):
            Employee.get_all()
            p=input()
        if(x=='fire'):
            id=input('enter id:')
            Employee.fire(id)
            p=input()
        if(x=='add office'):
            office=Office()


        elif(x=='quit'):
            break




menue()     
    
   

    


     


