from database import *
class Office:
    db=Database()
    def __init__(self):
        self.id=input('id:')
        self.name=input('office name:')
        self.location=input('location:')
        self.db.insert_office(self.id,self.name,self.location)
    
  
        
