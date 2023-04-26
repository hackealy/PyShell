import socket

HOST = 'localhost'  # Definir o IP local do seu servidor
PORT = 1234  # Escolher uma porta disponível para uso

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Aguardando conexão na porta {PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Conexão estabelecida por {addr}")
        while True:
            command = input("Digite um comando: ")
            conn.sendall(command.encode())
            data = conn.recv(1024)
            print(data.decode())
