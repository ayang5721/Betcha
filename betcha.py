import tkinter as tk
import datetime
from tkinter import messagebox
import json

import User
import login

active_bets = {}

login.run()
current_user = login.current_user

main__window = tk.Tk()
main__window.title("BetCha")
main__window.geometry("1500x700")

def friends():
    friends_window = tk.Tk()
    friends_window.title("Friends")
    friends_window.geometry("1500x700")

def marketplace():
    marketplace_window = tk.Tk()
    marketplace_window.title("Marketplace")
    marketplace_window.geometry("1500x700")

    tk.Button(marketplace_window, text = "Create bet", command = create_bet_window).pack()
    
    for bet in active_bets:
        tk.Label(marketplace_window, text = f"{active_bets[bet]['title']} - {active_bets[bet]['description']} - {active_bets[bet]['amount']} - {active_bets[bet]['end_date']} - {active_bets[bet]['user']}").pack()

def create_bet_window():
    create_bet_window = tk.Tk()
    create_bet_window.title("Create bet")
    create_bet_window.geometry("1500x700")

    var = tk.IntVar()

    def create_bet_button():
        var.set(1)

    tk.Label(create_bet_window, text = "Title").pack()
    title_entry = tk.Entry(create_bet_window)
    title_entry.pack()

    tk.Label(create_bet_window, text = "Description").pack()
    description_entry = tk.Entry(create_bet_window)
    description_entry.pack()

    tk.Label(create_bet_window, text = "Amount").pack()
    amount_entry = tk.Entry(create_bet_window)
    amount_entry.pack()

    tk.Label(create_bet_window, text = "End date").pack()
    end_date_entry = tk.Entry(create_bet_window)
    end_date_entry.pack()

    tk.Button(create_bet_window, text = "Create bet", command = create_bet_button).pack()
    
    create_bet_window.mainloop()

    create_bet_window.wait_variable(var)
    create_bet_window.destroy()

    active_bets[title_entry.get()] = {
        "title": title_entry.get(),
        "description": description_entry.get(),
        "amount": amount_entry.get(),
        "end_date": end_date_entry.get(),
        "user": current_user.name
    }

    current_user.bet_money(amount_entry.get(), title_entry.get())












tk.Button(main__window, text = "Friends", command = friends).pack()
tk.Button(main__window, text = "Marketplace", command = marketplace).pack()

