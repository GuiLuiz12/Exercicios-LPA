import socket
import configparser
import sys
import threading

def load_config():
    config = configparser.ConfigParser()
    config.read('config.txt')
    return config['network']['host'], int(config['network']['port'])

def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Servidor desconectado")
                break
            print(f"Servidor diz: {message}")
    except ConnectionResetError:
        print("Conexão com o servidor foi perdida")

def send_messages(client_socket):
    try:
        while True:
            message = input("Cliente: ")
            if message.lower() == 'sair':
                break
            client_socket.sendall(message.encode('utf-8'))
    except (ConnectionResetError, BrokenPipeError):
        print("Não foi possível enviar a mensagem - servidor desconectado")

def start_client():
    host, port = load_config()
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
        print(f"Conectado ao servidor em {host}:{port}")
        
        # Thread para receber mensagens
        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client_socket,),
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
        
    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor")
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        print("Uso: python chat_client.py")
        print("Digite mensagens para enviar ao servidor. Digite 'sair' para encerrar.")
    else:
        start_client()