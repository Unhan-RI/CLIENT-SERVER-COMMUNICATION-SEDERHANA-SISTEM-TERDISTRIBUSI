import socket
import threading

# Fungsi untuk menangani permintaan dari coordinator
def handle_client(client_socket):
    try:
        request = client_socket.recv(1024).decode('utf-8')
        if not request:
            raise ValueError("No data received")

        print(f"Received: {request}")
        
        # Balasan server
        response = f"Processed request: {request}"
        client_socket.send(response.encode('utf-8'))
        
    except Exception as e:
        print(f"Error handling client: {e}")
    
    finally:
        client_socket.close()  # Pastikan soket selalu ditutup
        print("Connection closed")

# Fungsi untuk menjalankan server backend
def start_server(server_host, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Opsi agar server bisa langsung di-restart tanpa menunggu timeout
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((server_host, server_port))
        server_socket.listen(5)
        print(f"Server running on {server_host}:{server_port}")

        while True:
            try:
                client_socket, addr = server_socket.accept()
                print(f"Accepted connection from {addr}")
                # Set timeout untuk koneksi klien agar tidak menggantung
                client_socket.settimeout(10)
                
                # Gunakan threading untuk menangani klien
                client_handler = threading.Thread(target=handle_client, args=(client_socket,))
                client_handler.start()
                
            except socket.error as e:
                print(f"Error accepting connections: {e}")
    
    except socket.error as e:
        print(f"Socket error: {e}")
    
    finally:
        server_socket.close()  # Pastikan soket server ditutup saat terjadi masalah
        print("Server socket closed")

if __name__ == "__main__":
    # Sesuaikan IP dan port setiap server backend
    server_host = '127.0.0.1'
    try:
        server_port = int(input("Enter server port (e.g., 9001, 9002, 9003): "))
        start_server(server_host, server_port)
    except ValueError:
        print("Invalid port number. Please enter a valid integer port.")
