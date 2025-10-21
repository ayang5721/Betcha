import os
import json

print("This will reset all user data. Are you sure? (yes/no)")
if input().strip().lower() == "yes":
    if os.path.exists("Users.json"):
        with open ("Users.json", "w") as f:
            f.write("")
        print("All user data has been reset.")

print ("This will reset all bets. Are you sure? (yes/no)")
if input().strip().lower() == "yes":
    if os.path.exists("Bets.json"):
        with open("Bets.json", "w") as f:
            f.write("")
        print("All bets have been reset.")

    if os.path.exists("Users.json") and os.path.getsize("Users.json") > 0:
        users_data = json.load(open("Users.json", "r"))
        for user in users_data.keys():
            users_data[user]["bet_keys"] = []
        with open("Users.json", "w") as f:
            json.dump(users_data, f, indent=4)