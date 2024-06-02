#!/usr/bin/python3
"""
    Module that set up basic HTTP Server
"""

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    Method that handle GET request
    """
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """
    Method that handle GET request
    """
    return "OK"


@app.route('/data')
def data():
    """
    Method that handle GET request
    """
    return jsonify(list(users.keys()))


@app.route('/users/<string:username>')
def users_data(username):
    """
    Method that handle GET request
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Method that handle POST request
    """
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
