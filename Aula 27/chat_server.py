import socket
import configparser
import sys
import threading

def load_config():
    config = configparser.ConfigParser()
    config.read('config.txt')
    return config['network']['host'], int(config['network']['port'])

def handle_client(client_socket, client_address):
    print(f"Conexão estabelecida com {client_address}")
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Cliente diz: {message}")
    except ConnectionResetError:
        print(f"Conexão com {client_address} foi resetada")
    finally:
        client_socket.close()
        print(f"Conexão com {client_address} encerrada")

def send_messages(client_socket):
    try:
        while True:
            message = input("Servidor: ")
            if message.lower() == 'sair':
                break
            client_socket.sendall(message.encode('utf-8'))
    except (ConnectionResetError, BrokenPipeError):
        print("Cliente desconectado")

def start_server():
    host, port = load_config()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Servidor ouvindo em {host}:{port}...")
    
    client_socket, client_address = server_socket.accept()
    
    # Thread para receber mensagens
    receive_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address),
        daemon=True
    )
    receive_thread.start()
    
    # Thread para enviar mensagens
    send_thread = threading.Thread(
        target=send_messages,
        args=(client_socket,),
        daemon=True
    )
    send_thread.start()
    
    # Manter as threads rodando
    receive_thread.join()
    send_thread.join()
    
    server_socket.close()

if __name__ == "__main__":
    start_server()