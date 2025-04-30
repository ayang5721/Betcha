#TODO/NOTES
"""
Add security for every request for user info
    server side info storing. 
    Only pass transformed (maybe SHA256) data to server and see if matches
    Make sure to not hardcore/store any info in python or swift files
"""



from flask import Flask, request, jsonify
from flask_cors import CORS

import User
import USERS

app = Flask(__name__)
CORS(app)

users = "USERS.json"
bets = "BET.json"
current_User = None

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')

    #Add security
    if username in users:
        if users[username]['password'] == data.get('password'):
            return jsonify({"status": "success", "message": "Login successful"}), 200
        else:
            return jsonify({"status": "error", "message": "Invalid password"}), 401
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404
    

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    #Add security
    if username in users:
        return jsonify({"status": "error", "message": "User already exists"}), 409
    else:
        current_User = User(NM = username, PW = password)
        users[username] = {
           current_User.to_dict()
        }
        return jsonify({"status": "success", "message": "User registered successfully"}), 201
    

