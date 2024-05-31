#!/usr/bin/python3
"""
    Module that set up basic HTTP Server
"""

from flask import Flask, jsonify, request


app = Flask(__name__)

user = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


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
    return jsonify(list(user.keys()))


@app.route('/data/<string:username>')
def user_data(username):
    """
    Method that handle GET request
    """
    if username in user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Method that handle POST request
    """
    user[request.json["name"].lower()] = request.json
    return jsonify(user)


if __name__ == "__main__":
    app.run()
