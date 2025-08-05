import os
import json
import numpy as np

class User:
    def __init__(self, name, password, balance = 0, active_bets = []):
        self.name = name
        self.password = password
        self.balance = balance
        self.active_bets = active_bets

    def toJson (self):
        return {

            self.name: {
                "username": self.name,
                "password": self.password,
                "balance": self.balance,
                "bet_keys": self.active_bets
            }

        }
    
class Bet:
    def __init__(self, key, event, case1, user1, bet1, case2, user2, bet2):
        self.key = key
        self.event = event
        self.user1 = user1
        self.bet1 = bet1
        self.case1 = case1
        self.user2 = user2
        self.bet2 = bet2  
        self.case2 = case2



    def toJson(self):
        return {
            self.key: {
                "key": self.key,
                "event": self.event,
                "case1": self.case1,
                "user1": self.user1,
                "bet1": self.bet1,
                "case2": self.case2,
                "user2": self.user2,
                "bet2": self.bet2
            }
        }

      