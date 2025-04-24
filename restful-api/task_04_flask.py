from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# /data endpoint to return all usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))  # Returns the list of usernames as JSON

# /status endpoint to return OK
@app.route('/status')
def status():
    return "OK"

# Dynamic route /users/<username> to return user data
@app.route('/users/<username>')
def user_info(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# /add_user endpoint to add a new user via POST
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    # Ensure username is provided
    if not data.get('username'):
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', 0),
        "city": data.get('city', '')
    }
    
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
