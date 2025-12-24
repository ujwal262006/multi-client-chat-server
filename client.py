import socket
import threading

# Caesar cipher
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

def receive_messages(client_socket):
    while True:
        try:
            encrypted_msg = client_socket.recv(1024).decode()
            if encrypted_msg:
                print(">>", decrypt(encrypted_msg))
        except:
            print("Disconnected from server.")
            client_socket.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))  # Change IP if server is remote

    username = input("Enter your username: ")
    client.send(encrypt(username).encode())

    print("Connected to chat server. Type 'exit' to leave.")

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input("")
        if msg.lower() == "exit":
            break
        client.send(encrypt(msg).encode())

    client.close()

if __name__ == "__main__":
    start_client()
