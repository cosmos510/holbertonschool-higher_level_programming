#!/usr/bin/python3
"""
    Module that serialization and deserialization
    """
import socket
import json


def start_server():
    """
        start a server on localhost
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 1245))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            print(data.decode('utf-8'))


def send_data(data):
    """
        send data to a server
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 1245))
        s.sendall(json.dumps(data).encode('utf-8'))
        s.send("closed".encode("utf-8"))
