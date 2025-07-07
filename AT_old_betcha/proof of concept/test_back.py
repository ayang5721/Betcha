import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hash', methods=['POST'])
def hash_input():
    data = request.get_json()
    input_str = data.get('input', '')
    sha256_hash = hashlib.sha256(input_str.encode()).hexdigest()
    return jsonify({'hash': sha256_hash})


if __name__ == '__main__':
    app.run(debug=True)


