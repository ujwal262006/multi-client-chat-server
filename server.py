import socket
import threading
from datetime import datetime

# Simple Caesar cipher
def encrypt(message, shift=3):
    result = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(message, shift=3):
    return encrypt(message, -shift)

# Store connected clients and their usernames
clients = {}
log_file = "chat_log.txt"

def broadcast(message, sender_socket=None):
    """Send message to all clients except the sender"""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(encrypt(message).encode())
            except:
                client.close()
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        username = clients[client_socket]
        del clients[client_socket]
        print(f"[-] {username} disconnected")
        broadcast(f"*** {username} has left the chat ***")

def handle_client(client_socket, addr):
    try:
        # First message is username
        username = decrypt(client_socket.recv(1024).decode())
        clients[client_socket] = username
        print(f"[+] {username} connected from {addr}")
        broadcast(f"*** {username} has joined the chat ***", client_socket)

        while True:
            encrypted_msg = client_socket.recv(1024).decode()
            if not encrypted_msg:
                break
            message = decrypt(encrypted_msg)
            timestamp = datetime.now().strftime("%H:%M")
            formatted = f"[{timestamp}] {username}: {message}"
            print(formatted)

            # Save to log file
            with open(log_file, "a") as f:
                f.write(formatted + "\n")

            # Send to all other clients
            broadcast(formatted, client_socket)

    except:
        pass
    finally:
        remove_client(client_socket)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("[*] Server started on port 5555...")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
