import random
import datetime

class User():
    def __init__(self, name, password, auth_key=None, balance=None, transactions=None, temp_money=None):
        self.name = name
        self.password = password

        self.auth_key = auth_key
        if auth_key is None:    
            self.auth_key = random.random() * datetime.datetime.now().second * random.randint(1,1000)
            self.auth_key = str(self.auth_key)

        self.balance = balance
        if balance is None:
            self.balance = 0

        self.transactions = transactions
        if self.transactions is None:
            self.transactions = {}

        self.temp_money = temp_money
        if self.temp_money is None:
            self.temp_money = {}

    def add_money(self, money):
        self.balance += money

    def bet_money(self, money, name):
        self.temp_money[name] = {
            "name": name,
            "amount": money
        }
        self.balance -= money
    



    


    


    