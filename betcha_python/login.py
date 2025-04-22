import tkinter as tk
from tkinter import messagebox
import json
import os

import betcha_python.User as User

USER_FILE = "users.json"
user_dictionary = json.load(open("users.json", "r"))
login_successful = False 
current_user = None


user_dictionary = {}

def setup_user_dictionary():
    print("yellow")
    with open(USER_FILE, "r") as file:
        users = json.load(file)
        for name, user_data in users.items():
            user_dictionary[name] = User.User(
                name=user_data["name"],
                password=user_data["password"],
                auth_key=user_data["auth_key"],
                balance=user_data["balance"],
                transactions=user_data["transactions"]
            )

print(user_dictionary)    

def load_users():
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_user(user):

    data = load_users()

    data[f"{user.name}"] = {
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
    if str(username) in users:
        if users[username]["password"] == password:
            messagebox.showinfo("Login", "Login successful")
            print(user_dictionary)
            current_user = user_dictionary[f"{username}"]
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
        user_dictionary[f"{username}"] = User.User(username, password)
        save_user(user_dictionary[f"{username}"])
        messagebox.showinfo("Create user", "User created")
    setup_user_dictionary()

# def login_process():
setup_user_dictionary()

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


