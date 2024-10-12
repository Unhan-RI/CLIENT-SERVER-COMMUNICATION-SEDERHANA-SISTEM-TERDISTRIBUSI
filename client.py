import socket

# Fungsi client untuk mengirim permintaan ke coordinator
def client():
    coordinator_host = '127.0.0.1'
    coordinator_port = 8000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((coordinator_host, coordinator_port))

    # Kirim pesan ke server
    message = input("Enter your message: ")
    client_socket.send(message.encode('utf-8'))

    # Terima balasan dari server
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received response: {response}")

    client_socket.close()

if __name__ == "__main__":
    client()
