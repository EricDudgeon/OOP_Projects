# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:18:09 2020

@author: Eric Dudgeon
"""
### OOP Bank Account

class BankAccount:
    def __init__(self):
        self.balance = 0 
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdrawl(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds")
    
    def get_balance(self):
        return self.balance
    

eric_account = BankAccount()

eric_account.deposit(1000)

print(eric_account.get_balance())

eric_account.withdrawl(200)

print(eric_account.get_balance())


