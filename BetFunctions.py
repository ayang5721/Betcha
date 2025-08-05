import json
import os
import numpy as np
from Classes import Bet, User

def create_bet(current_user, bets_data, users_data, event, case1, bet1, bet2):

    key = -1
    while(key in bets_data.keys() or key < 0):
        key = (np.random.uniform(0.00000, 100.00000))

    key = str(key)  # Ensure the key is a string for JSON compatibility

    #publish bet using Bet class
    bet = Bet(key, event = event, case1 = case1, user1 = current_user.name, bet1 = bet1, case2 = "None", user2 = "None", bet2 = bet2)

    current_user.balance -= bet1  # Deduct the bet amount from the user's balance

    current_user.active_bets.append(key)  # Update the user's active bets
    users_data[current_user.name] = current_user.toJson()[current_user.name]  # Update the user's data in JSON
    with open("Users.json", "w") as f:
        json.dump(users_data, f, indent=4)

    added_bet = bet.toJson()
    bets_data.update(added_bet)  # Update the existing bets data with the new bet
    with open("Bets.json", "w") as f:
        json.dump(bets_data, f, indent=4)

def accept_bet(current_user, bets_data, users_data, key):
    #accept the bet on a button click - key will be known
    

    bet = bets_data.get(key)
    bet = Bet(key, event = bet["event"], case1 = bet["case1"], user1 = bet["user1"], bet1 = bet["bet1"], case2 = None, user2 = current_user.name, bet2 = bet["bet2"])

    current_user.balance -= bet.bet2  # Deduct the bet amount from the user's balance

    #update the bet in the JSON file
    bets_data[key] = bet.toJson()[key]
    with open("Bets.json", "w") as f:
        json.dump(bets_data, f, indent=4)

    current_user.active_bets.append(key)  # Update the user's active bets
    users_data[current_user.name] = current_user.toJson()[current_user.name]  # Update the user's data in JSON
    with open("Users.json", "w") as f:
        json.dump(users_data, f, indent=4)
