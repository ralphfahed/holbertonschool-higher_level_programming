from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user store
users = {}

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Data route - returns a list of usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))  # Return list of usernames or empty list

# Add user route
@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400
    if user_data['username'] in users:
        return jsonify({"error": "Username already exists"}), 400
    users[user_data['username']] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201

# Get user route
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# Status route
@app.route('/status')
def status():
    return jsonify({"status": "API is up and running!"})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

