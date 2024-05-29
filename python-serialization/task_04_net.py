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
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', 1245))
            s.listen()
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                print('Received Dictionary from Client:')
                print(json.loads(data.decode('utf-8')))
    except ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def send_data(data):
    """
        send data to a server
   """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 1245))
            serialized_data = json.dumps(data).encode('utf-8')
            s.sendall(serialized_data)
    except ConnectionError as e:
        print(f"Connection error: {e}")
    except Exception as e:
        print(f"Error: {e}")
