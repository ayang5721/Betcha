import numpy as np
import json
import os
import tkinter as tk
from tkinter import messagebox
from Betcha_Python.Classes import User, Bet
from Betcha_Python.Login import login, createUser
from Betcha_Python.BetFunctions import create_bet, accept_bet

bets_data = {}
if os.path.exists("Bets.json") and os.path.getsize("Bets.json") > 0:
    with open("Bets.json", "r") as f:
        bets_data = json.load(f)

users_data = {}
if os.path.exists("Users.json") and os.path.getsize("Users.json") > 0:
    with open("Users.json", "r") as f:
        users_data = json.load(f)


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
        accept_bet(current_user, bets_data, users_data)

elif mainscreen_choice == "create":
    create_bet(current_user, bets_data, users_data)

elif mainscreen_choice == "view":
    for key in current_user.active_bets:
        bet = bets_data.get(key)
        if bet.get("user2") == "None":
            print(f"UNACCEPTED: Key: {key}, Event: {bet['event']}, Case1: {bet['case1']}, User1: {bet['user1']}, Bet1: {bet['bet1']}, Bet2: {bet['bet2']}")
        else:
            print(f"ACCEPTED: Key: {key}, Event: {bet['event']}, Case1: {bet['case1']}, User1: {bet['user1']}, Bet1: {bet['bet1']}, User2: {bet['user2']}, Bet2: {bet['bet2']}")

