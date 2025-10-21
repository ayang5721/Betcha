import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from Betcha_Python.Classes import User, Bet
from Betcha_Python.Login import login, createUser
from Betcha_Python.BetFunctions import create_bet, accept_bet

# Load Data
bets_data = {}
if os.path.exists("Bets.json") and os.path.getsize("Bets.json") > 0:
    with open("Bets.json", "r") as f:
        bets_data = json.load(f)

users_data = {}
if os.path.exists("Users.json") and os.path.getsize("Users.json") > 0:
    with open("Users.json", "r") as f:
        users_data = json.load(f)

current_user = None

# ---- GUI App ----
root = tk.Tk()
root.title("Betting App")
root.geometry("600x400")

def show_login_screen():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Button(root, text="Login", command=do_login).pack(pady=10)
    tk.Button(root, text="Create New User", command=do_create_user).pack(pady=10)

def do_login():
    global current_user
    username = simpledialog.askstring("Login", "Enter username:")
    
    if username is None:
        return
    
    password = simpledialog.askstring("Login", "Enter password:", show='*')

    if password is None:
        return
    
    current_user = login(username, password)
    if current_user:
        messagebox.showinfo("Success", f"Logged in as {username}")
        show_main_menu()
    else:
        messagebox.showerror("Error", "Invalid credentials")

def do_logout():
    global current_user
    current_user = None
    messagebox.showinfo("Logged Out", "You have been logged out.")
    show_login_screen()

def do_create_user():
    username = simpledialog.askstring("Create User", "Enter username:")

    if username is None:
        return

    password = simpledialog.askstring("Create User", "Enter password:", show='*')

    if password is None:
        return
    
    balance = simpledialog.askfloat("Create User", "Enter starting balance:")
    createUser(username, password, balance)
    messagebox.showinfo("Success", f"User {username} created!")

def do_accept_bet():
    global current_user
    key = simpledialog.askstring("Accept Bet", "Enter the key of the bet you want to accept:")
    while key not in bets_data.keys() and key is not None:
        key = simpledialog.askstring("Accept Bet", "Invalid key. Please enter a valid key:")

    if key is None:
        return
    
    accept_bet(current_user, bets_data, users_data, key)
    messagebox.showinfo("Bet Accepted", f"You have accepted the bet with key: {key}")
    enter_marketplace()

def open_create_bet_screen():
    create_window = tk.Toplevel()
    create_window.title("Create a Bet")
    create_window.geometry("400x300")

    # --- Input Fields ---
    tk.Label(create_window, text="Event Name:").grid(row=0, column=0, sticky="w")
    event_entry = tk.Entry(create_window)
    event_entry.grid(row=0, column=1)

    tk.Label(create_window, text="Case 1 (what you believe will happen):").grid(row=1, column=0, sticky="w")
    case1_entry = tk.Entry(create_window)
    case1_entry.grid(row=1, column=1)

    tk.Label(create_window, text="Your Bet Amount ($):").grid(row=2, column=0, sticky="w")
    bet1_entry = tk.Entry(create_window)
    bet1_entry.grid(row=2, column=1)

    tk.Label(create_window, text="Opponent Bet Amount ($):").grid(row=3, column=0, sticky="w")
    bet2_entry = tk.Entry(create_window)
    bet2_entry.grid(row=3, column=1)

    def submit_bet():
        try:
            event = event_entry.get().strip()
            case1 = case1_entry.get().strip()
            bet1 = float(bet1_entry.get().strip())
            bet2 = float(bet2_entry.get().strip())

            if not event or not case1:
                raise ValueError("Text fields cannot be empty.")
            
            if bet1 <= 0 or bet2 <= 0 or bet1 > current_user.balance:
                raise ValueError("Bet amounts must be positive and within your balance.")

            create_bet(current_user, bets_data, users_data, event, case1, bet1, bet2)
            messagebox.showinfo("Bet Created", f"Event: {event}\nCase: {case1}\nYour Bet: ${bet1}\nOpponent Bet: ${bet2}")
            create_window.destroy()  # Close window

        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")

    # --- Submit Button ---
    tk.Button(create_window, text="Submit Bet", command=submit_bet).grid(row=4, columnspan=2, pady=20)


def show_main_menu():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text=f"Welcome, {current_user.name}", font=("Arial", 16)).pack(pady=10)
    tk.Button(root, text="Enter Marketplace", command=enter_marketplace).pack(pady=5)
    tk.Button(root, text="Create Bet", command=open_create_bet_screen).pack(pady=5)
    tk.Button(root, text="View My Bets", command=view_bets).pack(pady=5)
    tk.Button(root, text="Logout", command=do_logout).pack(pady=20)

def enter_marketplace():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Marketplace Bets", font=("Arial", 14)).pack(pady=10)
    for key, bet in bets_data.items():
        if bet["user2"] == "None" and bet["user1"] != current_user.name:
            info = f"{key}: {bet['event']} | {bet['user1']} (${bet['bet1']}) vs ? (${bet['bet2']})"
            tk.Label(root, text=info).pack()

    tk.Button(root, text = "Accept A Bet", command = do_accept_bet).pack(pady=10)
    tk.Button(root, text="Back", command=show_main_menu).pack()

def view_bets():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="My Bets", font=("Arial", 14)).pack(pady=10)
    for key in current_user.active_bets:
        bet = bets_data.get(key)
        status = "UNACCEPTED"
        if bet.get("user2") != "None":
            status = "ACCEPTED"

        info = f"{status} | {key}: {bet['event']} | {bet['user1']} (${bet['bet1']}) vs {bet.get('user2', '?')} (${bet['bet2']})"

        tk.Label(root, text=info).pack()
    tk.Button(root, text="Back", command=show_main_menu).pack()

# ---- Login/Create Screen ----
show_login_screen()

root.mainloop()
