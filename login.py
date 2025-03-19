import tkinter as tk
from tkinter import messagebox
import json
import os

import User

USER_FILE = "users.json"
user_dictionary = {}
login_successful = False 

def load_users():
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

def save_user(user):

    data = load_users()

    data[user.name] = {
        "name": user.name,
        "password": user.password,
        "auth_key": user.auth_key,
        "balance": user.balance,
        "transactions": user.transactions
    }

    with open(USER_FILE, "w") as file:
        json.dump(data, file, indent = 4)

def login():
    username = username_entry.get()
    password = password_entry.get()
    users = load_users()
    if username in users:
        if users[username]["password"] == password:
            messagebox.showinfo("Login", "Login successful")
            login_window.destroy()
            login_successful = True
        else:
            messagebox.showerror("Login", "Invalid password")
    else:
        messagebox.showerror("Login", "Invalid username")

def create_user():
    username = username_entry.get()
    password = password_entry.get()
    users = load_users()
    if username in users:
        messagebox.showerror("Create user", "Username already exists")
    else:
        user_dictionary[f"{username}_object"] = User.User(username, password)
        save_user(user_dictionary[f"{username}_object"])
        messagebox.showinfo("Create user", "User created")

def login_process():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("1500x700")
        
    tk.Label(login_window, text = "Username").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text = "Password").pack()
    password_entry = tk.Entry(login_window, show = "*")
    password_entry.pack()

    tk.Button(login_window, text = "Login", command = login).pack(pady = 5)
    tk.Button(login_window, text = "Create user", command = create_user).pack()

    while True:
        login_window.mainloop()

        if login_successful:
            break


