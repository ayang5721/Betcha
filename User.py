import random
import datetime

class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.auth_key = random.random() * datetime.datetime.now().second * random.randint(1,1000)
        self.auth_key = str(self.auth_key)
        self.balance = 0
        self.transactions = {}
        self.temp_money = {}

    def add_money(self, money):
        self.balance += money

    def bet_money(self, money, name):
        self.temp_money[name] = {
            "name": name,
            "amount": money
        }
        self.balance -= money
    



    


    


    