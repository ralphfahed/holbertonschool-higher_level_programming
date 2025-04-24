#!/usr/bin/python3
"""Flask API module"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Store users in memory
users = {}

@app.route('/', methods=['GET'])
def home():
    """Return welcome message"""
    return "Welcome to the Flask API!"

@app.route('/status', methods=['GET'])
def status():
    """Return status"""
    return "OK"

@app.route('/data', methods=['GET'])
def get_data():
    """Return list of usernames"""
    return jsonify(list(users.keys()))

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Return user data for given username"""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    data = request.get_json()
    
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    user_data = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    
    users[username] = user_data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201

if __name__ == "__main__":
    app.run()
