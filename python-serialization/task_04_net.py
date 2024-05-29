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
        print("Received Dictionary from Client:")
        s.bind(('localhost', 1245))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            data = conn.recv(1024)
            print(json.loads(data.decode('utf-8')))
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                print(data.decode('utf-8'))

def send_data(data):
    """
        send data to a server
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 1245))
        s.sendall(json.dumps(data).encode('utf-8'))
        s.close()