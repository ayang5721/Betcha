import json

with open('users.json', 'w') as file:
    json.dump({}, file)