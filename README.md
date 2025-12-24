# Multi-Client Chat Server (Python)

This project is a TCP-based multi-client chat application developed to understand core networking concepts, client–server architecture, and concurrent programming using Python.

The system allows multiple clients to connect to a central server and exchange messages in real time.

---

## Overview

The application consists of:
- A server program that accepts multiple client connections
- A client program that connects to the server and sends/receives messages

Each connected client runs in a separate thread on the server, enabling simultaneous communication among multiple users.

---

## Key Features

- TCP-based client–server communication  
- Support for multiple concurrent clients using threading  
- Real-time message broadcasting  
- Basic message encryption and decryption using a Caesar cipher  
- Server-side logging of chat messages with timestamps  
- Graceful handling of client join and disconnect events  

---

## Technical Details

- The server listens on a specified port and spawns a new thread for each client connection.
- Messages are encrypted before transmission and decrypted on receipt.
- Chat activity is logged on the server for monitoring and debugging purposes.

---

## Technology Stack

- Python  
- Socket Programming  
- Multithreading  

---

## Project Structure
multi-client-chat-server/
├── server.py
├── client.py
└── README.md

---

## How to Run

1. Start the server:

2. Start one or more clients in separate terminals:

3. Enter a username and begin chatting.

---

## Author

Ujwal Parashar  
B.Tech Information Technology  
Jaypee Institute of Information Technology, Noida  

GitHub: https://github.com/ujwal262006  
LinkedIn: https://linkedin.com/in/ujwal-parashar-3195a735a
