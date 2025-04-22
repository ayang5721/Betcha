import random
import datetime

class User():
    def __init__(self, NM, PW, AK=None, BAL=None, TRAN=None, TM=None):

        """
        NN: name
        PW: password
        AK: auth key
        BAL: balance
        TRAN: transactions
        TM: temp money
        """

        self.NM = NM
        self.PW = PW

        self.auth_key = AK
        if AK is None:    
            self.AK = random.random() * datetime.datetime.now().second * random.randint(1,1000)
            self.AK = str(self.AK)

        self.BAL = BAL
        if BAL is None:
            self.BAL = 0

        self.TRAN = TRAN
        if self.TRAN is None:
            self.TRAN = {}

        self.TM = TM
        if self.TM is None:
            self.TM = {}

    def add_money(self, money):
        self.BAL += money

    def bet_money(self, money, NM):
        self.TM[NM] = {
            "name": NM,
            "amount": money
        }
        self.BAL -= money
    
    def to_dict(self):
        return {
            "name": self.NM,
            "password": self.PW,
            "auth_key": self.AK,
            "balance": self.BAL,
            "transactions": self.TRAN,
            "temp_money": self.TM
        }



    


    


    