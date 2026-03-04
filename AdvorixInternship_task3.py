from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "users.json"


# ------------------ Helper Functions ------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ------------------ Routes ------------------

# 1️⃣ GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(load_data())


# 2️⃣ GET single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    users = load_data()
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# 3️⃣ CREATE new user
@app.route("/users", methods=["POST"])
def add_user():
    users = load_data()
    new_user = request.json

    new_user["id"] = users[-1]["id"] + 1 if users else 1
    users.append(new_user)

    save_data(users)
    return jsonify(new_user), 201


# 4️⃣ UPDATE user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    users = load_data()

    for user in users:
        if user["id"] == user_id:
            user.update(request.json)
            save_data(users)
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404


# 5️⃣ DELETE user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    users = load_data()
    users = [user for user in users if user["id"] != user_id]

    save_data(users)
    return jsonify({"message": "User deleted"})


# ------------------ Run Server ------------------

if __name__ == "__main__":
    app.run(debug=True)