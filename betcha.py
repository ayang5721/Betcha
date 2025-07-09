import numpy as np
import json
import os
from Classes import User, Bet
from Login import login, createUser

bets_data = {}
if os.path.exists("Bets.json") and os.path.getsize("Bets.json") > 0:
    with open("Bets.json", "r") as f:
        bets_data = json.load(f)

loginOrCreate = input("Do you want to login or create a new user? (login/create): ").strip().lower()
if loginOrCreate == "create":
    createUser(input("Enter your username: "), input("Enter your password: "), float(input("Enter your starting balance: ")))

current_user = None
while(current_user is None):
    login_user = input("Enter your username: ")
    login_password = input("Enter your password: ")
    current_user = login(login_user, login_password)


mainscreen_choice = input("Do you want to enter Marketplace, create a bet, or view current bets? (marketplace/create/view): ").strip().lower()

if mainscreen_choice == "marketplace":
    print("Welcome to the Marketplace!")
    print("Here are the current bets:")
    for key, bet_info in bets_data.items():
        if bet_info["user2"] == "None":
            print(f"Key: {key}, Event: {bet_info['event']}, Case1: {bet_info['case1']}, User1: {bet_info['user1']}, Bet1: {bet_info['bet1']}, Bet2: {bet_info['bet2']}")


    betAccept = input("Do you want to accept a bet? (yes/no): ").strip().lower()
    if betAccept == "yes":
        accept_bet()

elif mainscreen_choice == "create":
    create_bet()
elif mainscreen_choice == "view":
    for key in current_user.active_bets:
        bet = bets_data.get(key)
        if bet.get("user2") == "None":
            print(f"UNACCEPTED: Key: {key}, Event: {bet['event']}, Case1: {bet['case1']}, User1: {bet['user1']}, Bet1: {bet['bet1']}, Bet2: {bet['bet2']}")
        else:
            print(f"ACCEPTED: Key: {key}, Event: {bet['event']}, Case1: {bet['case1']}, User1: {bet['user1']}, Bet1: {bet['bet1']}, User2: {bet['user2']}, Bet2: {bet['bet2']}")



def create_bet():
    event = input("Enter the event: ")
    case1 = input("Enter your choice: ")

    bet1 = 0.0
    while(bet1 <= 0):
        bet1 = input("Enter your bet: ")
        bet1 = float(bet1)
        if bet1 > current_user.balance:
            print("Insufficient balance. Please try again.")
            bet1 = 0.0

    bet2 = 0.0
    while (bet2 <= 0):
        bet2 = input("Enter the desired bet of the other user: ")
        bet2 = float(bet2)

    key = -1
    
    while(key in bets_data.keys()):
        key = np.random.randfloat(0, 100)


    #publish bet using Bet class
    bet = Bet(key, event = event, case1 = case1, user1 = current_user.name, bet1 = bet1, case2 = "None", user2 = "None", bet2 = bet2)
    
    current_user.active_bets.append(key)
        
    added_bet = bet.toJson()
    bets_data.update(added_bet)  # Update the existing bets data with the new bet

    with open("Bets.json", "w") as f:
        json.dump(bets_data, f, indent=4)

def accept_bet():
    #accept the bet on a button click - key will be known
    key = None
    while(key not in bets_data.keys()):
        key = input("Enter the key of the bet you want to accept: ")


    bet = bets_data.get(key)

    bet = Bet(key, event = bet["event"], case1 = bet["case1"], user1 = bet["user1"], bet1 = bet["bet1"], case2 = None, user2 = current_user.name, bet2 = bet["bet2"])

    #update the bet in the JSON file
    bets_data[key] = bet.toJson()[key]
    with open("Bets.json", "w") as f:
        json.dump(bets_data, f, indent=4)

    current_user.active_bets.append(key)  
