#! /usr/bin/env python3
class Person:
    def __init__(self,full_name,money,sleepmood='unKnown',healthRate='unKnown'):
        self.full_name=full_name
        self.money=money
        self.sleepmood=sleepmood
        self.healthRate=healthRate

    def sleep(self,hours):
        self.sleepmood=Person.get_sleep_mode(hours)
        return self.sleepmood
            

    def eat(self,meals):
        self.healthRate=Person.get_healthrate(meals)
        return self.healthRate

    def buy(self,items):
        self.money=self.money-items*10
        return self.money
        

    @staticmethod
    def get_sleep_mode(hours):
        if(hours==7):
           return 'happy'
        elif(hours<7):
            return 'tired'
        else:
            return 'lazy'

    @staticmethod
    def get_healthrate(meals):
        if(meals>=3):
           return 100
        elif(meals==2):
            return 75
        elif(meals==1):
            return 50
        elif(meals==0):
            return 0




