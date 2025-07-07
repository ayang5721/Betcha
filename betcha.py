import numpy as np
import json
import os
from Classes import User, Bet

all_bets = [None]
all_bets.append(-1)
#load existing bets from JSON file if it exists

# login process
# Current user = new user (load JSON data)
current_user = User()


def create_bet():
    event = input("Enter the event: ")
    case1 = input("Enter your choice: ")
    bet1 = input("Enter your bet: ")
    bet1 = float(bet1)

    if bet1 > current_user.balance:
        print("Insufficient balance. Please try again.")
        return

    bet2 = input("Enter the desired bet of the other user: ")
    bet2 = float(bet2)

    key = -1
    
    while(key in all_bets):
        key = np.random.randfloat(0, 100)


    #publish bet using Bet class
    bet = Bet(key, event = event, case1 = case1, user1 = current_user.name, bet1 = bet1, case2 = "None", user2 = "None", bet2 = bet2)
    
    all_bets.append(key)
    current_user.active_bets.append(key)

    if not os.path.exists("Bets.json"):
        with open("Bets.json", "w") as f:
           adddata = {bet.toJson()}
        json.dump(adddata, f, indent=4)


# Open marketplace
# Display all bets - load bets from the keys in all_bets using JSON data - dont remake the bets

def accept_bet():
    #accept the bet on a button click - key will be known
    key = input("Enter the key of the bet you want to accept: ")

    with open ("Bets.json", "r") as f:
        bets_data = json.load(f)
    bet = bets_data.get(key)

    bet = Bet(key, event = bet["event"], case1 = bet["case1"], user1 = bet["user1"], bet1 = bet["bet1"], case2 = None, user2 = current_user.name, bet2 = bet["bet2"])

    #update the bet in the JSON file
    bets_data[key] = bet.toJson()[key]
    with open("Bets.json", "w") as f:
        json.dump(bets_data, f, indent=4)  
